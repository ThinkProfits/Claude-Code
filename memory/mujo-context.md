# Mujo: `wp-mujo` MCP capabilities (tested 2026-10-08)

Easy MCP AI 2.1.0 on mujo.com. MCP server `wp-mujo` (user scope, HTTP, Bearer key). Client profile: `clients/mujo/CLIENT.md`.

**Connection**
- Confirmed connected to mujo.com (site name "Mujo Learning Systems", WP 7.1.3, language `en-CA`).
- Authenticates as WP user ID 7 `francis@thinkprofits.com`, role **administrator**. Handoff recommends a dedicated WP user instead; not done yet.
- Diagnostics: 0 fails. One API token exists ("Claude Francis"), 0 OAuth grants. "Privileged" tool category is off.
- Change history on 2026-10-08 showed only the plugin's own diagnostics options. No content edits via MCP so far.

**Can do**
- Read posts, pages, products (`rest_base: product`, 46 items), plugins, users.
- Rank Math abilities: read per-post SEO meta and schema (`rank_math_get_post_seo_meta`, `rank_math_get_post_schema`), plus setters for global settings, homepage SEO, website identity, sitemap, breadcrumbs, modules.
- `wp_rest_write` reaches `rankmath/v1/updateSchemas` (args: `objectType`, `objectID`, `schemas`), `updateMeta`, `updateMetaBulk` and `updateSettings`. So per-post custom schema and Rank Math settings **are** writable via MCP. Untested; try on a draft first.
- Available Rank Math schema types include `book`, `product`, `course`, `service`, `person`.

**Can't do (or not directly)**
- `wp_get_post_meta` returns nothing: Rank Math meta keys (`rank_math_schema_*`) aren't REST-registered. Use the Rank Math abilities / `rankmath/v1` routes instead.
- Products currently carry only the default `WooCommerceProduct` schema, no custom schemas.

**Watch-outs**
- WP Rocket caches without excluding `/wp-json/easy-mcp-ai/` (diagnostic warning). Add the exclusion so a revoked key can't keep working from cache.
- Kinsta intercepts `/.well-known/`. Claude works around it; nothing needed.
- Active plugin "Timeline Event History" (wpdiscover, v3.2) has Hello Dolly's description text. That pattern is common for disguised malicious plugins, and the site was compromised in August 2026. Flagged to Andrew; don't touch it.
- WPCode Lite and Simple Custom CSS and JS are both active, so check both when hunting the hand-coded Organization schema.
- Trustindex plugin is listed as "Widgets for Google Reviews".

Related: [[spiedr-context]]
