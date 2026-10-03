"""
Google Business Profile API client.
Handles authentication and all GBP read/write operations.
"""

import json
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/business.manage"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "credentials.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "token.json")


def authenticate() -> Credentials:
    """
    Run OAuth2 flow on first use, then load saved token on subsequent runs.
    Uses console-based flow (no browser required) — prints a URL to visit,
    then prompts for the authorization code to paste back.
    """
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(
                    "credentials.json not found. Download it from Google Cloud Console "
                    "(APIs & Services → Credentials) and place it in the project folder."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            flow.redirect_uri = "http://localhost"
            auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
            print("\n--- Google Authentication Required ---")
            print("1. Open this URL in your browser:\n")
            print(f"   {auth_url}\n")
            print("2. Log in and grant access.")
            print("3. Your browser will redirect to localhost (it will show an error — that is OK).")
            print("4. Copy the FULL URL from your browser's address bar and paste it below.\n")
            redirect_response = input("Paste the full redirect URL here: ").strip()
            flow.fetch_token(authorization_response=redirect_response)
            creds = flow.credentials

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds


def _account_management_service():
    creds = authenticate()
    return build("mybusinessaccountmanagement", "v1", credentials=creds)


def _business_info_service():
    creds = authenticate()
    return build("mybusinessbusinessinformation", "v1", credentials=creds)


# ---------------------------------------------------------------------------
# Accounts
# ---------------------------------------------------------------------------

def list_accounts() -> list[dict]:
    """Return all GBP accounts the authenticated user manages."""
    service = _account_management_service()
    response = service.accounts().list().execute()
    return response.get("accounts", [])


# ---------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------

def list_locations(account_name: str) -> list[dict]:
    """
    Return all locations under an account.
    account_name format: 'accounts/123456789'
    """
    service = _business_info_service()
    read_mask = (
        "name,title,phoneNumbers,categories,storefrontAddress,"
        "websiteUri,regularHours,businessHours,serviceItems,"
        "attributes,profile,relationshipData,moreHours"
    )
    response = (
        service.accounts()
        .locations()
        .list(parent=account_name, readMask=read_mask)
        .execute()
    )
    return response.get("locations", [])


def get_location(location_name: str) -> dict:
    """
    Return full profile details for a single location.
    location_name format: 'accounts/123/locations/456'
    """
    service = _business_info_service()
    read_mask = (
        "name,title,phoneNumbers,categories,storefrontAddress,"
        "websiteUri,regularHours,businessHours,serviceItems,"
        "attributes,profile,relationshipData,moreHours"
    )
    return (
        service.accounts()
        .locations()
        .get(name=location_name, readMask=read_mask)
        .execute()
    )


def update_location(location_name: str, update_data: dict, update_mask: str) -> dict:
    """
    Update fields on a location.

    update_data: dict of fields to update (e.g. {"title": "New Name"})
    update_mask: comma-separated field paths (e.g. "title,phoneNumbers")
    """
    service = _business_info_service()
    return (
        service.accounts()
        .locations()
        .patch(name=location_name, updateMask=update_mask, body=update_data)
        .execute()
    )


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

def get_services(location_name: str) -> list[dict]:
    """Return the services list for a location."""
    location = get_location(location_name)
    return location.get("serviceItems", [])


def update_services(location_name: str, service_items: list[dict]) -> dict:
    """
    Replace the services list on a location.

    service_items: list of service item dicts, e.g.:
    [
        {
            "structuredServiceItem": {
                "serviceTypeId": "gcid:plumber",
                "description": "Emergency plumbing repairs"
            }
        },
        {
            "freeFormServiceItem": {
                "category": {"displayName": "Plumbing"},
                "label": {"displayName": "Drain Cleaning", "description": "Full drain cleaning service"}
            }
        }
    ]
    """
    update_data = {"serviceItems": service_items}
    return update_location(location_name, update_data, "serviceItems")


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = [
    "title",
    "phoneNumbers",
    "storefrontAddress",
    "websiteUri",
    "regularHours",
    "categories",
    "profile",
]


def audit_location(location: dict) -> dict:
    """
    Check a location dict for missing or incomplete fields.
    Returns a report dict with a completeness score and list of issues.
    """
    issues = []

    if not location.get("title"):
        issues.append("Missing business name")
    if not location.get("phoneNumbers", {}).get("primaryPhone"):
        issues.append("Missing primary phone number")
    if not location.get("storefrontAddress"):
        issues.append("Missing address")
    if not location.get("websiteUri"):
        issues.append("Missing website URL")
    if not location.get("regularHours"):
        issues.append("Missing regular business hours")
    if not location.get("categories", {}).get("primaryCategory"):
        issues.append("Missing primary category")
    if not location.get("profile", {}).get("description"):
        issues.append("Missing business description")
    if not location.get("serviceItems"):
        issues.append("No services listed")

    total_fields = len(REQUIRED_FIELDS)
    filled_fields = total_fields - len(issues)
    score = round((filled_fields / total_fields) * 100)

    return {
        "name": location.get("name"),
        "title": location.get("title", "Unknown"),
        "completeness_score": score,
        "issues": issues,
        "has_services": bool(location.get("serviceItems")),
        "service_count": len(location.get("serviceItems", [])),
    }


def bulk_audit(account_name: str) -> list[dict]:
    """Audit every location under an account and return a report for each."""
    locations = list_locations(account_name)
    return [audit_location(loc) for loc in locations]


# ---------------------------------------------------------------------------
# Bulk operations
# ---------------------------------------------------------------------------

def bulk_update_services(
    account_name: str, service_items: list[dict]
) -> list[dict]:
    """
    Push the same services list to every location under an account.
    Returns a list of results (location name + success/error).
    """
    locations = list_locations(account_name)
    results = []

    for loc in locations:
        loc_name = loc.get("name")
        try:
            update_services(loc_name, service_items)
            results.append({"location": loc_name, "title": loc.get("title"), "status": "success"})
        except HttpError as e:
            results.append({"location": loc_name, "title": loc.get("title"), "status": "error", "detail": str(e)})

    return results


if __name__ == "__main__":
    print("Authenticating with Google...")
    creds = authenticate()
    print("Authentication successful! token.json has been saved.")
    print("You are now ready to use the GBP Audit MCP server.")
