---
name: google-ads-keyword-planner-mcp
description: "Local MCP server for free Google Ads Keyword Planner data. Setup state, account IDs, and the Basic-access blocker."
metadata:
  node_type: memory
  type: project
  originSessionId: bee90295-5452-4891-af50-ce090633e9f6
  modified: 2026-09-29T15:44:25.189Z
---

The `google-ads-keywords` local MCP server (code in `mcp-servers/google-ads-keywords/` here; Francis's live copy runs from `E:\Claude\mcp-servers\google-ads-keywords`) is registered at user scope as `google-ads-keywords`. It exposes three tools: find_location, keyword_ideas and keyword_volume. The Cloud project is `gsc-claude-connection`, and the OAuth consent screen is published to production.

State as of 2026-09-29:
- OAuth completed and credentials are written to `google-ads.yaml` (git-ignored).
- login_customer_id is the Think Profits MCC, 362-716-7231. The signed-in user sees 86 client accounts under it.
- customer_id in settings.json is "ThinkProfits (Self Account)", 2916941762. Keyword Planner can't run on the MCC itself, and 803-818-7193 is not reachable through this login.
- All three tools work. Basic access was approved 2026-09-30, after brand verification (the app is named "ThinkProfits" to match the homepage, and it is published to production).

**Why:** the user wanted a cheap, Claude-driven keyword volume source alongside Semrush, and needed it to never touch Ads.

**How to apply:** the server code is read-only and makes no mutate calls. If a refresh token ever expires (invalid_grant), rerun setup_auth.py. seo@thinkprofits.com is passkey-only and the passkey isn't on this PC; the sign-in that eventually worked was done in Edge. Developer tokens were retired in Sept 2026, so don't ask for one.
