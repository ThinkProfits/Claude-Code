"""
Two-step auth helper for cloud environments.
Step 1: python auth_helper.py          → prints the auth URL
Step 2: python auth_helper.py <url>    → completes the token exchange
"""

import json
import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/business.manage"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "credentials.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "token.json")


def step1_get_url():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    flow.redirect_uri = "http://localhost"
    auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
    # Save flow state so step 2 can reuse it
    state = {"redirect_uri": flow.redirect_uri, "client_config": CREDENTIALS_FILE}
    print("\n=== STEP 1: Open this URL in your browser ===\n")
    print(auth_url)
    print("\n=== After approving, copy the full redirect URL (starting with http://localhost) and paste it back ===\n")


def step2_exchange(redirect_response: str):
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    flow.redirect_uri = "http://localhost"
    flow.fetch_token(authorization_response=redirect_response)
    creds = flow.credentials
    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())
    print("\nAuthentication successful! token.json saved.")
    print("Your GBP MCP server is ready to use.\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        step1_get_url()
    else:
        step2_exchange(sys.argv[1])
