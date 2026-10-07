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

**Write test passed (2026-10-08)** on draft product 30423 ("Foundations of Marketing (Texas Edition) ... (Copy)").
- Call: `wp_rest_write` POST `/rankmath/v1/updateSchemas`, body `{"objectType":"post","objectID":<id>,"schemas":{"new-1":{"@type":"Book","metadata":{"title":"Book","type":"custom","isPrimary":false}, ...fields}}}`. Returns `{"new-1": <meta_id>}`. To update later, key by `"schema-<meta_id>"`.
- Front end (checked via `wp_create_preview_link` + browser): the Book node renders in Rank Math's `@graph`, and `%url%` resolves.
- **Side effect:** with a custom schema saved, Rank Math stops showing its default `WooCommerceProduct` type. Price data still comes from a second JSON-LD block, WooCommerce core's own Product (AggregateOffer $59–$398). Its name is double-encoded (`&amp;amp;`). Before rolling Book out, decide how Book and Product relate (e.g. Book linked to the Product via `@id`, or Product + Book as one multi-type node). Then validate in Rich Results Test so the price snippets don't get lost.

**Book + Product schema test (Rich Results Test, 2026-10-08)**
- Live product pages output a Rank Math `ProductGroup` with variants, 0 errors. **ISBNs are already stored as each variant's GTIN** (e.g. AI Business Analytics: 9781998671663 student, 9781998671687 instructor).
- Proposed pattern: keep ProductGroup, type each variant `["Product","Book"]` with `isbn`, `bookFormat`, `publisher` (`@id` to Organization), `inLanguage`. Template: `clients/mujo/schema-test-product-book.html`.
- Result: Product snippets (1) and Merchant listings (2) both **valid**. $0 instructor variant passed.
- Non-critical issues: `audience` with `EducationalAudience` is rejected on Product (removed); variant `description` missing (added); `shippingDetails`, `hasMerchantReturnPolicy`, `validFrom` missing; `aggregateRating`/`review` missing. Don't fake ratings.

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
