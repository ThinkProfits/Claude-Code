# Semrush API replacement stack (free tools)

*Researched 2026-10-29. Reusable reference for the whole team. Limits below come from third-party reviews unless marked "official"; check each vendor's pricing page before quoting a limit to a client.*

## Why this exists

Semrush API units have been at zero since 2026-10-07, so the Semrush MCP returns "unable to charge units". Every workflow below used to lean on it. This doc maps each job to free tools we can use instead, with the honest gaps called out.

## What we actually used Semrush for

Pulled from skills, scheduled tasks, client CARD/CLIENT/keywords files in this repo:

1. Keyword volume, difficulty, trend, CPC (keyword briefs, GBP topic finder, blog briefs; CA, US and PH databases)
2. Question research (`phrase_questions`, our People Also Ask proxy) for FAQs and briefs
3. Indexed/ranking pages per domain (`resource_organic_unique`) for the blog cannibalization check and GBP link checks
4. Domain's ranking keywords + traffic estimates (Organic Research, domain overview)
5. Position Tracking + visibility % (weekly SEO report to Slack, client reviews)
6. Competitor research, keyword gap, SERP features
7. Site Audit (some projects)
8. Backlinks

## Replacement map

| # | Job | Free replacement (primary) | Backup / cross-check | Quality vs Semrush |
|---|-----|---------------------------|---------------------|--------------------|
| 1 | Keyword volume + CPC | **Google Ads Keyword Planner MCP** (`google-ads-keywords`, already live, Basic access approved 2026-09-30) | Google Trends for trend line; Keywords Everywhere / Glimpse browser extensions (free tiers) | **Equal or better** for volume. Google's own data; Semrush's is modelled. Accounts without ad spend may see ranges (e.g. 1K–10K), so check our MCP output shows exact figures. |
| 1 | Keyword difficulty | Manual SERP check: who ranks top 10 (built-in browser) + Ahrefs free Keyword Difficulty checker | Moz free (10 queries/month) | **Weaker.** No single free KD score at scale. Use a SERP read instead; it is often more honest for local terms anyway. |
| 2 | PAA / question research | Live Google SERP (built-in browser or WebSearch) expanding PAA boxes | AlsoAsked free (about 3 searches/day per its help centre); AnswerThePublic free tier; Keyword Planner `keyword_ideas` filtered for who/what/how/why | **Equal.** Real PAA boxes are the source Semrush approximates. |
| 3 | Indexed pages for cannibalization | **GSC MCP** (`get_search_by_page_query`, pages with impressions) + XML sitemap + `site:` search | WordPress MCP post/page lists for sites we manage | **Better** for our own clients. GSC is ground truth; Semrush only saw pages it tracked. |
| 4 | Own-site ranking keywords + traffic | **GSC MCP** (queries, positions, clicks) + **GA4 MCP** (sessions, conversions) | Ahrefs Webmaster Tools (free for verified sites: Site Explorer up to ~1,000 keywords/backlinks shown) | **Better** for clients. Real clicks, not estimates. |
| 4 | Competitor traffic estimates | Ahrefs free Website Traffic Checker; Similarweb free extension | Bing Webmaster Tools competitor compare | **Weaker.** Directional only. Present as estimates. |
| 5 | Rank tracking (organic) | **GSC average position** per query (weekly via GSC MCP) | SerpBear (open source, self-hosted, MIT) using a free scraping tier (ScrapingAnt ~10k lookups/month, ScrapingRobot ~5k/month per Unraid listing) | **Equal** for trend reporting; GSC is national average, not city-specific. |
| 5 | Local / map-pack tracking | **BrightLocal MCP** (Local Rank Tracker, Local Search Grid; already paid for) | SEO PowerSuite Rank Tracker free (one project, local settings) | **Equal or better** for local clients. BrightLocal API key needs fixing (rejected 2026-10-23, per Jamie Davis audit). |
| 5 | Visibility % metric | Build from GSC: clicks/impressions share for tracked keyword list | BrightLocal share of local voice | **Different metric.** Tell clients the metric changed; don't compare to old Semrush %. |
| 6 | Competitor keywords / gap | Ahrefs free Keyword Generator (about 100 ideas per seed) + manual SERP review | Ubersuggest free (about 3 searches/day) | **Weaker.** No free tool shows a competitor's full keyword list. Biggest gap. |
| 6 | SERP features / AI Overviews | Live SERP check (built-in browser) | BrightLocal AI Visibility (AIV) for AI answers | **Equal.** Live view beats a cached report. |
| 7 | Site audit | Screaming Frog free (500 URLs, official) | Ahrefs Webmaster Tools Site Audit (verified sites); GSC Pages/Core Web Vitals; Rank Math/Yoast/WP Rocket abilities on client WP MCPs | **Equal** for sites under 500 URLs, which covers most of our local clients. |
| 8 | Backlinks (own site) | Ahrefs Webmaster Tools + GSC Links report | Bing Webmaster Tools backlinks | **Equal.** |
| 8 | Backlinks (competitor) | Bing Webmaster Tools (shows backlinks for domains you don't own, compare 2 competitors) | Moz Link Explorer free (10 queries/month); Ahrefs free Backlink Checker (top 100) | **Weaker.** Fine for spot checks, not full link-gap audits. |

## Setup to-dos

- [ ] Add every client site to **Ahrefs Webmaster Tools** (verify via GSC import, one click per property). Unlocks free site audit, organic keywords and backlinks for clients.
- [ ] Add every client site to **Bing Webmaster Tools** (import from GSC). Free backlinks + competitor compare.
- [ ] Confirm `google-ads-keywords` MCP returns exact volumes, not ranges.
- [ ] Fix **BrightLocal** API key so local rank tracking and grids work.
- [ ] Decide on SerpBear: only worth it if we need daily city-level organic ranks that GSC and BrightLocal don't cover.
- [ ] Update skills/tasks that hard-code Semrush (`gbp-topic-finder`, `agency-blog-writer`, `gbp-saturday-drafting`, `weekly-seo-report-slack-check`, CLAUDE.md "never substitute" line) to use this map.
- [ ] If the Semrush **UI** subscription is still active, its scheduled PDF reports keep working without API units; only the Claude/MCP calls are blocked.

## Honest gaps

Free tools fully replace Semrush for **our own clients' data** (GSC, GA4 and Keyword Planner are better sources). They don't fully replace it for **competitor intelligence**: competitor keyword lists, keyword gap and full competitor backlink profiles. Forum consensus matches this. Users on BlackHatWorld say combining free tools gets solid results but won't match Ahrefs/Semrush depth for audits. If competitor work is a big part of a deliverable, a pay-as-you-go API (DataForSEO, roughly US$0.60–2 per 1,000 SERP calls per vendor-adjacent comparisons) is cheaper than a Semrush API top-up. Check current pricing first.

## Sources

- Ahrefs Webmaster Tools free features: https://www.allable.ai/blog/ahrefs-webmaster-tools/ , https://superframeworks.com/articles/best-free-ahrefs-alternatives
- AlsoAsked free searches (official help centre): https://help.alsoasked.com/en/articles/6577966-how-can-i-get-free-searches
- Bing Webmaster Tools / Moz / Ubersuggest limits: https://www.searchscientists.com/the-ultimate-guide-to-the-best-backlink-checkers-in-2026/ , https://technovapartners.com/en/insights/best-free-seo-tools-2026
- Screaming Frog 500-URL free limit (official): https://screamingfrog.co.uk/pricing
- SerpBear + free scraping tiers: https://gigazine.net/gsc_news/en/20260315-serpbear , https://ca.unraid.net/apps/serpbear-0evclgc0h6xkrk
- Free rank trackers: https://www.link-assistant.com/news/free-rank-tracking-tools.html , https://www.theseoagent.ai/blog/best-free-rank-trackers
- Keyword Planner ranges without spend: https://www.dataslayer.ai/blog/how-to-master-google-keyword-planner-in-2026
- SERP API pricing: https://www.openwebninja.com/blog/best-serp-apis-2026 , https://dev.to/serpbase/top-5-serp-apis-worth-trying-in-2026-ranked-by-budget-4gpd
- Forum threads (BlackHatWorld): https://www.blackhatworld.com/seo/best-free-alternatives-to-ahrefs-semrush.1774981/ , https://www.blackhatworld.com/seo/which-are-the-best-tools-to-check-website-backlinks-for-free.1825949/
