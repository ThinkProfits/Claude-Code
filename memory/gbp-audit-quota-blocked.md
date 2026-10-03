---
name: gbp-audit-quota-blocked
description: The gbp-audit MCP tool (mybusinessaccountmanagement.googleapis.com) is hard-blocked by a 0-requests/min Google Cloud quota, not a transient rate limit
metadata:
  type: reference
  originSessionId: ea9903ab-3a9e-4429-942f-88d7c4e4ae4b
  modified: 2026-09-08T15:27:46.429Z
---

Every call to `mcp__gbp-audit__list_accounts` (and by extension the other gbp-audit tools) has failed
across at least 3 separate client audits (as of 2026-09-08) with the same error:

```
HttpError 429 ... quota metric 'Requests' and limit 'Requests per minute' ...
quota_limit_value: '0'
```

The `quota_limit_value` is literally `'0'` — this is not a transient rate limit that clears on retry,
it's the Google Cloud project's quota for `mybusinessaccountmanagement.googleapis.com` being
configured at zero requests/minute. Retrying does not help.

**How to apply:** Don't retry this tool expecting it to recover on its own. When a client audit needs
GBP category/data cross-checks, tell the user directly that GBP audit access is blocked by this quota
issue and needs a fix in Google Cloud Console (the project tied to the gbp-audit integration needs its
quota raised above zero) — not something fixable from within a session. Flag it once per audit where
it's relevant, then proceed with the rest of the audit using other data sources.
