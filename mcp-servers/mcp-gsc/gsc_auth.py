"""One-time sign-in for the GSC MCP server. Writes token.json where gsc_server.py looks for it.

Run in PowerShell:
    & "E:\\Claude\\mcp-servers\\mcp-gsc\\.venv\\Scripts\\python.exe" "E:\\Claude\\mcp-servers\\mcp-gsc\\gsc_auth.py"
"""

import os
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from platformdirs import user_config_dir

HERE = Path(__file__).resolve().parent
SECRETS = HERE / "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/webmasters"]
config_dir = Path(os.environ.get("GSC_CONFIG_DIR") or user_config_dir("mcp-gsc"))
config_dir.mkdir(parents=True, exist_ok=True)

flow = InstalledAppFlow.from_client_secrets_file(str(SECRETS), scopes=SCOPES)
creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")
(config_dir / "token.json").write_text(creds.to_json(), encoding="utf-8")
print("\nDone. Search Console sign-in saved. Restart Claude to reconnect the gsc server.")
