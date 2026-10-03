---
name: gsc-mcp-thinkprofits-auth
description: "The local `gsc` MCP server is signed in as the ThinkProfits Google account (96 properties). How to re-auth it."
metadata:
  node_type: memory
  type: project
  originSessionId: bee90295-5452-4891-af50-ce090633e9f6
  modified: 2026-09-29T18:02:41.793Z
---

On 2026-09-30 the `gsc` MCP server (`E:\Claude\mcp-servers\mcp-gsc`) was fixed. Its `client_secret.json` was missing, and it now uses the same OAuth client as [[google-ads-keyword-planner-mcp]], from the Cloud project `gsc-claude-connection` with the app named "ThinkProfits" and published to production.

It is signed in with the ThinkProfits agency Google account, which sees 96 properties: ThinkProfits clients such as johnsadler.ca, jamiedavistowing.com, spiedr.com and butlerplumbing.ca.

**Why:** properties outside this agency account aren't visible through this server. Check the property list before assuming a client is missing data.

**How to apply:** if GSC tools fail on auth, run `gsc_auth.py` from the server folder (`mcp-servers/mcp-gsc/` in this repo; Francis's live copy runs from `E:\Claude\mcp-servers\mcp-gsc\`) in PowerShell, paste the printed URL into Edge (seo@thinkprofits.com is passkey-only and Chrome can't use the passkey), then restart Claude. The token lives in `%LOCALAPPDATA%\mcp-gsc\mcp-gsc\token.json`.
