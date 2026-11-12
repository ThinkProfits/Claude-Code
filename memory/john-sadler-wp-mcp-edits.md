---
name: john-sadler-wp-mcp-edits
description: How to edit johnsadler.ca safely through the wp-john-sadler MCP (Bold Builder, base64 raw blocks, CRLF) and why bulk writes must be paced
metadata:
  type: reference
---

Learned on 2026-11-11/12 while applying live page edits (log: clients/john-sadler/HANDOFF-live-page-edits-2026-11-11.md).

- **The host is fragile.** A run of writes through Easy MCP AI (even one at a time) knocked www.johnsadler.ca offline three times on 2026-11-12, for 5 to 10+ minutes each; the Cloudflare edge stayed up. Pace bulk work at about 1 write every 20 to 30 seconds, never run parallel write calls, clear caches per post (not `scope: site`), and scan the REST API in small pages (per_page=20, 3 s gaps). Ask Kinsta to check server limits before the next bulk run.
- **`wp_replace_in_post` limits:** search max 500 chars; regex is off for fields over 20 KB; live content mixes CRLF and LF and has non-breaking spaces, and CR can't be typed into a search. Keep searches on one line and set `expected_count`.
- **Bold Builder `bt_bb_raw_content` blocks are base64.** Edit them with same-length changes: decode, change the bytes without changing the length (pad shorter text with JSON whitespace outside quotes), re-encode, and replace only the few changed base64 characters. The public REST `content.rendered` equals the decoded block, so the edit window can be computed without reading the raw page. To disable a schema script, change `type="application/ld+json">` to `type="text/x-ld-disabled" >`.
- **Yoast meta:** the Yoast SEO integration in Easy MCP AI is now on; use `wp_yoast_update_post_seo`.
- **Spam schema:** about 73 pages and posts carried a copied Organization block with 354 junk `sameAs` URLs. See the handoff log for which are done.

Related: [[john-sadler-context]], [[page-update-doc-format]]
