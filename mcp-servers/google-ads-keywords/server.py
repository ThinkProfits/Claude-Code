"""Google Ads Keyword Planner MCP server.

Exposes Keyword Planner (KeywordPlanIdeaService) to Claude as three tools:
find_location, keyword_ideas, keyword_volume.

Credentials live in google-ads.yaml next to this file (created by setup_auth.py).
The client account ID to query comes from GOOGLE_ADS_CUSTOMER_ID or `customer_id`
in settings.json. Keyword Planner does not run against a manager (MCC) account.
"""

import json
import os
from pathlib import Path

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from mcp.server.fastmcp import FastMCP

HERE = Path(__file__).resolve().parent
YAML_PATH = Path(os.environ.get("GOOGLE_ADS_CONFIG", HERE / "google-ads.yaml"))
SETTINGS_PATH = HERE / "settings.json"

# Common language constants. Full list: developers.google.com/google-ads/api/data/codes-formats#languages
LANGUAGES = {"en": 1000, "english": 1000, "fr": 1002, "french": 1002, "es": 1003, "spanish": 1003}

mcp = FastMCP("google-ads-keywords")
_client = None


def _settings():
    if SETTINGS_PATH.exists():
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    return {}


def _get_client():
    global _client
    if _client is None:
        if not YAML_PATH.exists():
            raise RuntimeError(f"Missing {YAML_PATH}. Run setup_auth.py first.")
        _client = GoogleAdsClient.load_from_storage(str(YAML_PATH))
    return _client


def _customer_id(override):
    cid = override or os.environ.get("GOOGLE_ADS_CUSTOMER_ID") or _settings().get("customer_id")
    if not cid:
        raise RuntimeError("No customer ID. Set customer_id in settings.json or pass customer_id.")
    return str(cid).replace("-", "")


def _language(lang):
    if lang is None:
        lang = _settings().get("default_language", "en")
    lang_id = LANGUAGES.get(str(lang).lower(), lang)
    return f"languageConstants/{lang_id}"


def _resolve_locations(client, locations, country_code):
    """Accept geo IDs ("9001234") or names ("Vancouver, BC"); return resource names."""
    if not locations:
        locations = _settings().get("default_locations", ["2124"])  # 2124 = Canada
    ids, names = [], []
    for loc in locations:
        (ids if str(loc).isdigit() else names).append(str(loc))
    resources = [f"geoTargetConstants/{i}" for i in ids]
    if names:
        for match in _suggest_locations(client, names, country_code):
            resources.append(match["resource_name"])
    return resources


def _suggest_locations(client, names, country_code):
    service = client.get_service("GeoTargetConstantService")
    request = client.get_type("SuggestGeoTargetConstantsRequest")
    request.locale = "en"
    if country_code:
        request.country_code = country_code
    request.location_names.names.extend(names)
    response = service.suggest_geo_target_constants(request=request)
    out, seen = [], set()
    for s in response.geo_target_constant_suggestions:
        g = s.geo_target_constant
        # Suggestions come back per search term; keep the top hit for each.
        if s.search_term in seen:
            continue
        seen.add(s.search_term)
        out.append({
            "search_term": s.search_term,
            "resource_name": g.resource_name,
            "id": g.id,
            "name": g.name,
            "canonical_name": g.canonical_name,
            "target_type": g.target_type,
        })
    return out


def _metrics(m):
    return {
        "avg_monthly_searches": m.avg_monthly_searches,
        "competition": m.competition.name,
        "competition_index": m.competition_index,
        "low_top_of_page_bid": round(m.low_top_of_page_bid_micros / 1_000_000, 2),
        "high_top_of_page_bid": round(m.high_top_of_page_bid_micros / 1_000_000, 2),
        "monthly_searches": [
            {"year": v.year, "month": v.month.name, "searches": v.monthly_searches}
            for v in m.monthly_search_volumes
        ],
    }


def _ads_error(ex):
    errors = "; ".join(e.message for e in ex.failure.errors)
    return {"error": errors, "request_id": ex.request_id}


@mcp.tool()
def find_location(names: list[str], country_code: str = "CA") -> list[dict] | dict:
    """Look up Google Ads geo target IDs for place names, e.g. ["Vancouver", "Surrey"].

    country_code narrows matches (ISO 2-letter, e.g. "CA", "US"); pass "" for worldwide.
    Use the returned id values as `locations` in the other tools.
    """
    try:
        return _suggest_locations(_get_client(), names, country_code)
    except GoogleAdsException as ex:
        return _ads_error(ex)


@mcp.tool()
def keyword_ideas(
    seed_keywords: list[str] | None = None,
    url: str | None = None,
    locations: list[str] | None = None,
    country_code: str = "CA",
    language: str | None = None,
    include_adult: bool = False,
    limit: int = 100,
    customer_id: str | None = None,
) -> dict:
    """Generate keyword ideas from seed keywords and/or a page or site URL (Keyword Planner "Discover").

    locations: geo IDs or place names ("Vancouver", "British Columbia"); defaults to settings.json.
    language: "en", "fr", "es" or a numeric language constant ID.
    Returns avg monthly searches, competition, top-of-page bid range (account currency) and
    12-month trend, sorted by volume. Low-spend accounts may get rounded volume figures.
    """
    if not seed_keywords and not url:
        return {"error": "Provide seed_keywords, url, or both."}
    try:
        client = _get_client()
        service = client.get_service("KeywordPlanIdeaService")
        request = client.get_type("GenerateKeywordIdeasRequest")
        request.customer_id = _customer_id(customer_id)
        request.language = _language(language)
        request.geo_target_constants.extend(_resolve_locations(client, locations, country_code))
        request.include_adult_keywords = include_adult
        request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH

        if seed_keywords and url:
            request.keyword_and_url_seed.url = url
            request.keyword_and_url_seed.keywords.extend(seed_keywords)
        elif seed_keywords:
            request.keyword_seed.keywords.extend(seed_keywords)
        elif "/" in url.split("://", 1)[-1].rstrip("/"):
            request.url_seed.url = url
        else:
            request.site_seed.site = url

        ideas = []
        for idea in service.generate_keyword_ideas(request=request):
            ideas.append({"keyword": idea.text, **_metrics(idea.keyword_idea_metrics)})
        ideas.sort(key=lambda r: r["avg_monthly_searches"], reverse=True)
        return {
            "locations": list(request.geo_target_constants),
            "language": request.language,
            "total_ideas": len(ideas),
            "ideas": ideas[:limit],
        }
    except (GoogleAdsException,) as ex:
        return _ads_error(ex)


@mcp.tool()
def keyword_volume(
    keywords: list[str],
    locations: list[str] | None = None,
    country_code: str = "CA",
    language: str | None = None,
    customer_id: str | None = None,
) -> dict:
    """Get search volume, competition, bids and 12-month trend for an exact list of keywords.

    Use this to check volume on keywords you already have (up to 10,000 per call).
    Keywords with no data come back with zero volume.
    """
    try:
        client = _get_client()
        service = client.get_service("KeywordPlanIdeaService")
        request = client.get_type("GenerateKeywordHistoricalMetricsRequest")
        request.customer_id = _customer_id(customer_id)
        request.keywords.extend(keywords)
        request.language = _language(language)
        request.geo_target_constants.extend(_resolve_locations(client, locations, country_code))
        request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH

        response = service.generate_keyword_historical_metrics(request=request)
        rows = []
        for r in response.results:
            row = {"keyword": r.text, **_metrics(r.keyword_metrics)}
            if r.close_variants:
                row["close_variants"] = list(r.close_variants)
            rows.append(row)
        returned = {v.lower() for r in rows for v in [r["keyword"], *r.get("close_variants", [])]}
        missing = [k for k in keywords if k.lower() not in returned]
        return {"locations": list(request.geo_target_constants), "results": rows, "no_data": missing}
    except GoogleAdsException as ex:
        return _ads_error(ex)


if __name__ == "__main__":
    mcp.run()
