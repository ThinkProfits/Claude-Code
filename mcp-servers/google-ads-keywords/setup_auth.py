"""One-time setup: sign in with Google and write google-ads.yaml.

Run this yourself in a terminal:
    .venv\\Scripts\\python.exe setup_auth.py

Needs client_secrets.json (a Google Cloud OAuth client of type "Desktop app",
in a project with the Google Ads API enabled) in this folder.
Secrets are written straight to google-ads.yaml and never printed.
"""

import json
import re
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

HERE = Path(__file__).resolve().parent
SECRETS = HERE / "client_secrets.json"
YAML_PATH = HERE / "google-ads.yaml"
SETTINGS_PATH = HERE / "settings.json"
SCOPES = ["https://www.googleapis.com/auth/adwords"]


def main():
    if not SECRETS.exists():
        raise SystemExit(f"Put your OAuth client file at {SECRETS} first.")

    info = json.loads(SECRETS.read_text(encoding="utf-8"))
    client = info.get("installed") or info.get("web")
    if not client:
        raise SystemExit("client_secrets.json doesn't look like an OAuth client file.")

    # Developer tokens were retired Sept 2026; API access now comes from the Cloud project
    # that owns the OAuth client, so no token is prompted for or written.
    login_customer_id = re.sub(r"\D", "", input("Manager (MCC) account ID, e.g. 123-456-7890: "))
    customer_id = re.sub(r"\D", "", input("Client Ads account ID to run Keyword Planner on: "))

    print("\nOpening browser to sign in with the Google account that has access to the MCC...")
    flow = InstalledAppFlow.from_client_secrets_file(str(SECRETS), scopes=SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")
    if not creds.refresh_token:
        raise SystemExit("Google didn't return a refresh token. Remove the app's access at "
                         "myaccount.google.com/permissions and run this again.")

    YAML_PATH.write_text(
        "\n".join([
            f"client_id: {client['client_id']}",
            f"client_secret: {client['client_secret']}",
            f"refresh_token: {creds.refresh_token}",
            f"login_customer_id: {login_customer_id}",
            "use_proto_plus: True",
            "",
        ]),
        encoding="utf-8",
    )

    settings = json.loads(SETTINGS_PATH.read_text(encoding="utf-8")) if SETTINGS_PATH.exists() else {}
    settings["customer_id"] = customer_id
    SETTINGS_PATH.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")

    print(f"\nDone. Wrote {YAML_PATH.name} and {SETTINGS_PATH.name}. Restart Claude to load the server.")


if __name__ == "__main__":
    main()
