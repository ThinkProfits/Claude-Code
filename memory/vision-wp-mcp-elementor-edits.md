---
name: vision-wp-mcp-elementor-edits
description: How to edit Vision's Elementor pages through the wp-vision Easy MCP server, and the cache steps needed before the change shows live
metadata:
  type: reference
---

The `wp-vision` MCP server (Easy MCP AI, connected 2026-10-14) gives administrator access to visionplumbingandheating.com as `francis-TP`.

**Editing Elementor pages (tested 2026-10-14 on the phone-number fixes):**
1. Page text lives in post meta `_elementor_data`, a JSON string of about 60 to 100K characters per page. `post_content` holds only a fallback copy. You must edit both.
2. There's no partial-update route. To change something, read the full `_elementor_data`, make a string replace in a local script, check it's still valid JSON, and write it back with `wp_update_post_meta` (`post_type: "pages"`). Never retype the JSON by hand. The script `fixphones.py` (in the 2026-10-14 session scratchpad) does this by calling the MCP endpoint directly, with the auth header from `~/.claude.json`. Then fix `post_content` with `wp_replace_in_post`.
3. **Elementor element cache:** after a meta write, the live page still shows the old text until you delete post meta `_elementor_element_cache` (`wp_delete_post_meta`). Elementor rebuilds it on the next visit.
4. **Kinsta page cache:** after that, trigger a save with an empty `PATCH /wp/v2/pages/{id}` through `wp_rest_write`, which purges the cached page. Order matters: clear the Elementor cache first, then save, or Kinsta re-caches the stale render.
5. Verify on the live URL (the `x-kinsta-cache` header shows MISS/HIT) and compare the stored values against a backup.

**Limits:** the server rate-limits after roughly 30 quick calls (error -32003), so space calls about 4 seconds apart in scripts. There's no `wp_rest_delete` tool, so Elementor's sitewide `DELETE /elementor/v1/cache` route can't be called. WP Rocket tools exist (`wp_rocket_clear_url_cache`), but their instructions require an explicit user confirmation first.

Approval rules still apply: wording changes need Andrew's check (see `clients/Vision/CLIENT.md`). Related: [[page-additions-merge-into-existing-sections]].
