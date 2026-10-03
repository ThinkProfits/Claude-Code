# Google Ads Keyword Planner MCP

Gives Claude free Keyword Planner data via the Google Ads API.

## Tools
- `find_location`: place names to geo target IDs (e.g. "Surrey" + `CA`)
- `keyword_ideas`: ideas from seed keywords and/or a URL, sorted by volume
- `keyword_volume`: volume, competition, bid range and 12-month trend for a set keyword list

Defaults (Canada, English) are in `settings.json`. Override per call with `locations` / `language`.

## Setup (per machine)
1. Google Cloud project: enable **Google Ads API**, then request API access on its Google Ads API Overview page. Developer tokens were retired in Sept 2026, and access levels now belong to the Cloud project. Test access can't read real accounts. Basic needs brand verification, then approval is automated.
2. In the same project, create an OAuth client of type **Desktop app** and download the JSON as `client_secrets.json` into this folder.
3. `python -m venv .venv` then `.venv\Scripts\pip install -r requirements.txt`
4. `.venv\Scripts\python.exe setup_auth.py` (prompts for the MCC and client account IDs, opens a browser sign-in, writes `google-ads.yaml`)
5. `claude mcp add google-ads-keywords -s user -- <path>\.venv\Scripts\python.exe <path>\server.py`, then restart Claude.

`google-ads.yaml` and `client_secrets.json` hold secrets and are git-ignored. Don't share them.

## Notes
- Keyword Planner must target a client Ads account, not the MCC itself (`customer_id` in `settings.json`).
- Accounts with little or no ad spend can get rounded volume figures.
- No keyword difficulty or SERP data. Pair it with Semrush for that.
