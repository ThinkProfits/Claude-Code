"""One-time OAuth sign-in for the GA4 MCP server (Google's `analytics-mcp`).

Opens a browser so you can grant read-only Google Analytics access, then writes
an "authorized_user" credentials file that analytics-mcp picks up through
GOOGLE_APPLICATION_CREDENTIALS.

Usage:
    python auth.py <path-to-oauth-client_secret.json> <output-credentials.json>

Keep both files OUTSIDE this repo. See README.md.
"""
import json
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    client_secret, out_path = sys.argv[1], sys.argv[2]

    flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "type": "authorized_user",
                "client_id": creds.client_id,
                "client_secret": creds.client_secret,
                "refresh_token": creds.refresh_token,
            },
            f,
        )
    print(f"Saved GA4 credentials to {out_path}")


if __name__ == "__main__":
    main()
