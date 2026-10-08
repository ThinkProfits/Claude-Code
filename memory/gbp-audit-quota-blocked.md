---
name: gbp-audit-quota-blocked
description: The gbp-audit MCP tool is hard-blocked by a 0 requests/min Business Profile API quota; neither Cloud project has GBP API access approved yet
metadata:
  type: reference
  originSessionId: ea9903ab-3a9e-4429-942f-88d7c4e4ae4b
  modified: 2026-10-05T18:56:58.806Z
---

Every call to `mcp__gbp-audit__list_accounts` fails with `HttpError 429 ... quota_limit_value: '0'`
(seen 2026-09-08 and again 2026-10-06). A 0 quota means Google has not approved GBP API access for
the project. Retrying never helps.

Two Cloud projects are involved (checked 2026-10-06):
- `gbp-audit-tool-492719` (number 461689527641): the project whose OAuth client the gbp-audit server
  uses (`E:\123\Claude-Code\gbp-mcp-server\credentials.json` + `token.json`). Quota 0.
- `gsc-claude-connection-510115` (number 1059297179447): used by the gsc and google-ads-keywords MCPs.
  The user enabled My Business Account Management API here, but the quota is also 0 (Console,
  authuser=4 in the user's Chrome).

The gbp-audit token has only the `business.manage` scope, so the connected Google account's email
can't be read from it.

**How to apply:** Don't retry the tool expecting it to recover. The fix is Google's GBP API access
request form (developers.google.com/my-business/content/prereqs#request-access) for whichever project
will be used. Once a project shows a quota above 0, point gbp-audit at that project's OAuth client and
re-auth. The Google Cloud Integration Connectors "MyBusiness" connector does not bypass this; it is
paid, Pre-GA and calls the same APIs.
