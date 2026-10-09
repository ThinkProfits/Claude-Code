# GA4 MCP server (local)

Gives Claude Code read-only access to Google Analytics 4 by running Google's official [`analytics-mcp`](https://pypi.org/project/analytics-mcp/) package. Its tools are `get_account_summaries`, `get_property_details`, `run_report`, `run_realtime_report`, `get_custom_dimensions_and_metrics` and `list_google_ads_links`.

Like `gsc` and `google-ads-keywords`, this runs only on a PC where it has been installed and authenticated. It does **not** run in claude.ai cloud sessions. **This folder holds no credentials.** Each person authenticates their own copy.

## Setup (Windows)

You need:
- Python 3.10+.
- A Google Cloud **Desktop** OAuth client JSON. The one used for `mcp-gsc` works.
- In that client's Google Cloud project, these two APIs enabled:
  - **Google Analytics Data API**
  - **Google Analytics Admin API**

1. Create the venv outside the repo:
   ```
   python -m venv E:\Claude\mcp-servers\ga4\.venv
   E:\Claude\mcp-servers\ga4\.venv\Scripts\python -m pip install analytics-mcp==0.7.0 google-auth-oauthlib
   ```
2. Sign in. A browser window opens; sign in with the Google account that has GA4 access.
   ```
   E:\Claude\mcp-servers\ga4\.venv\Scripts\python mcp-servers\ga4\auth.py E:\Claude\mcp-servers\mcp-gsc\client_secret.json E:\Claude\mcp-servers\ga4\credentials.json
   ```
3. Register the server with Claude Code at user scope:
   ```
   claude mcp add ga4 --scope user -e GOOGLE_APPLICATION_CREDENTIALS=E:\Claude\mcp-servers\ga4\credentials.json -e GOOGLE_PROJECT_ID=gsc-claude-connection-510115 -- E:\Claude\mcp-servers\ga4\.venv\Scripts\analytics-mcp.exe
   ```
4. Restart Claude Code. Then ask it to "list my GA4 accounts" to confirm the connection works.

Never commit `credentials.json` or `client_secret*.json`.
