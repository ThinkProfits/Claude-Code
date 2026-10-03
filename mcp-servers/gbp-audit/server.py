"""
GBP Audit MCP Server
Exposes Google Business Profile audit and edit operations as Claude tools.
"""

import json
from mcp.server.fastmcp import FastMCP
import gbp_client

mcp = FastMCP("GBP Audit Tool")


# ---------------------------------------------------------------------------
# Accounts
# ---------------------------------------------------------------------------

@mcp.tool()
def list_accounts() -> str:
    """List all Google Business Profile accounts the authenticated user manages."""
    accounts = gbp_client.list_accounts()
    if not accounts:
        return "No accounts found for the authenticated user."
    lines = [f"Found {len(accounts)} account(s):\n"]
    for acc in accounts:
        lines.append(f"  - {acc.get('accountName', 'Unnamed')}  |  ID: {acc.get('name')}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------

@mcp.tool()
def list_locations(account_name: str) -> str:
    """
    List all locations under a GBP account.

    Args:
        account_name: The account resource name, e.g. 'accounts/123456789'
    """
    locations = gbp_client.list_locations(account_name)
    if not locations:
        return f"No locations found under {account_name}."
    lines = [f"Found {len(locations)} location(s) under {account_name}:\n"]
    for loc in locations:
        address = loc.get("storefrontAddress", {})
        city = address.get("locality", "")
        state = address.get("administrativeArea", "")
        lines.append(f"  - {loc.get('title', 'Unnamed')}  |  {city}, {state}  |  ID: {loc.get('name')}")
    return "\n".join(lines)


@mcp.tool()
def get_location(location_name: str) -> str:
    """
    Get full profile details for a single location.

    Args:
        location_name: The location resource name, e.g. 'accounts/123/locations/456'
    """
    loc = gbp_client.get_location(location_name)
    return json.dumps(loc, indent=2)


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------

@mcp.tool()
def audit_location(location_name: str) -> str:
    """
    Audit a single GBP location and report missing or incomplete fields.

    Args:
        location_name: The location resource name, e.g. 'accounts/123/locations/456'
    """
    loc = gbp_client.get_location(location_name)
    report = gbp_client.audit_location(loc)

    lines = [
        f"Audit Report: {report['title']}",
        f"Completeness Score: {report['completeness_score']}%",
        f"Services Listed: {report['service_count']}",
        "",
    ]
    if report["issues"]:
        lines.append("Issues Found:")
        for issue in report["issues"]:
            lines.append(f"  - {issue}")
    else:
        lines.append("No issues found. Profile is complete.")

    return "\n".join(lines)


@mcp.tool()
def audit_all_locations(account_name: str) -> str:
    """
    Audit every location under a GBP account and return a summary report.

    Args:
        account_name: The account resource name, e.g. 'accounts/123456789'
    """
    reports = gbp_client.bulk_audit(account_name)
    if not reports:
        return f"No locations found under {account_name}."

    avg_score = round(sum(r["completeness_score"] for r in reports) / len(reports))
    lines = [
        f"Audit Summary — {len(reports)} location(s)",
        f"Average Completeness Score: {avg_score}%",
        "",
    ]

    for r in sorted(reports, key=lambda x: x["completeness_score"]):
        status = "OK" if not r["issues"] else f"{len(r['issues'])} issue(s)"
        lines.append(
            f"  [{r['completeness_score']}%] {r['title']}  |  Services: {r['service_count']}  |  {status}"
        )
        for issue in r["issues"]:
            lines.append(f"         - {issue}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

@mcp.tool()
def get_services(location_name: str) -> str:
    """
    Get the services list for a GBP location.

    Args:
        location_name: The location resource name, e.g. 'accounts/123/locations/456'
    """
    services = gbp_client.get_services(location_name)
    if not services:
        return "No services listed on this profile."
    return json.dumps(services, indent=2)


@mcp.tool()
def update_services(location_name: str, services_json: str) -> str:
    """
    Replace the services on a GBP location.

    Args:
        location_name: The location resource name, e.g. 'accounts/123/locations/456'
        services_json: JSON array of service item objects. Example:
            [
              {
                "freeFormServiceItem": {
                  "category": {"displayName": "Plumbing"},
                  "label": {"displayName": "Drain Cleaning", "description": "Full drain cleaning service"}
                }
              }
            ]
    """
    service_items = json.loads(services_json)
    result = gbp_client.update_services(location_name, service_items)
    return f"Services updated successfully on {location_name}.\n" + json.dumps(result, indent=2)


@mcp.tool()
def bulk_push_services(account_name: str, services_json: str) -> str:
    """
    Push the same services list to every location under a GBP account.

    Args:
        account_name: The account resource name, e.g. 'accounts/123456789'
        services_json: JSON array of service item objects (same format as update_services)
    """
    service_items = json.loads(services_json)
    results = gbp_client.bulk_update_services(account_name, service_items)

    success = [r for r in results if r["status"] == "success"]
    errors = [r for r in results if r["status"] == "error"]

    lines = [
        f"Bulk Services Update — {len(results)} location(s)",
        f"  Succeeded: {len(success)}",
        f"  Failed:    {len(errors)}",
        "",
    ]
    for r in success:
        lines.append(f"  [OK]    {r['title']}")
    for r in errors:
        lines.append(f"  [FAIL]  {r['title']}  — {r.get('detail', '')}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Profile editing
# ---------------------------------------------------------------------------

@mcp.tool()
def update_profile(location_name: str, field: str, value: str) -> str:
    """
    Update a single field on a GBP location profile.

    Args:
        location_name: The location resource name, e.g. 'accounts/123/locations/456'
        field: The field to update. Supported: 'title', 'websiteUri', 'phoneNumber', 'description'
        value: The new value as a string
    """
    field_map = {
        "title": ("title", lambda v: v),
        "websiteUri": ("websiteUri", lambda v: v),
        "phoneNumber": ("phoneNumbers", lambda v: {"primaryPhone": v}),
        "description": ("profile", lambda v: {"description": v}),
    }

    if field not in field_map:
        supported = ", ".join(field_map.keys())
        return f"Unsupported field '{field}'. Supported fields: {supported}"

    api_field, transform = field_map[field]
    update_data = {api_field: transform(value)}
    gbp_client.update_location(location_name, update_data, api_field)
    return f"Successfully updated '{field}' on {location_name}."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    if "--sse" in sys.argv:
        port = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8000
        print(f"Starting GBP Audit MCP server on http://0.0.0.0:{port}/sse")
        mcp.run(transport="sse")
    else:
        mcp.run()

