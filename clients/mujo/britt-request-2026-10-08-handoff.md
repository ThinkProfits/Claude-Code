# Mujo: Britt's SEO request (handoff, 2026-10-08)

> **Source:** `clients/mujo/email from britt.txt` (Brittni Woodson to Andrew, Francis in scope).
> **Client profile:** read [CLIENT.md](CLIENT.md) first (approvals, stack, security history).
> **Start the next session with:** "test wp-mujo", then work the schema tasks (section 3).

## 1. Setup status: `wp-mujo` MCP

- Easy MCP AI plugin installed on mujo.com.
- MCP server `wp-mujo` added at **user scope** (`~/.claude.json`), HTTP, endpoint `https://www.mujo.com/wp-json/easy-mcp-ai/v1/mcp`, Bearer auth header.
- **Key hygiene:** the first API key was exposed in a screenshot during setup (2026-10-08). Confirm it was revoked in Easy MCP AI and that the server was re-added with a new key. Never store the key in this repo (it auto-syncs to GitHub).
- **Sign-off:** confirm Andrew (and ideally Shawn) are aware the plugin is installed. The site was compromised in August 2026; Andrew owns dev/security.
- Recommended: the MCP should authenticate as a dedicated WP user, not Brittni's or Andrew's account.

### First-run test (do before any write)
1. Confirm the server is connected to mujo.com (site info/settings call), not LocalPulse (`wordpress`) or SPIEDR (`wp-spiedr`).
2. Pick one textbook page and read its post meta. Check whether Rank Math schema keys (`rank_math_schema_*`, `rank_math_rich_snippet`) are visible.
3. If visible: test a write on **staging or a draft** first, then verify the front-end JSON-LD output.
4. If not visible (same issue as Yoast meta on LocalPulse, where meta wasn't REST-exposed for pages): fall back to drafting JSON-LD and pasting it via Rank Math > Schema Generator > Import.
5. Record what the MCP can and can't do on this site in `CLIENT.md` (stack section) and in a `memory/mujo-context.md` file.

## 2. Working rules for this job

- **Brittni approves all content and schema changes before they go live.** Draft, show her, then push.
- Don't edit the site during any database merge Andrew is running.
- Log hours to Teamwork project **1146973**. SEO scope is **10 hours/month** and this list will likely exceed it; flag the estimate to Andrew/Brittni before starting the dev items.
- Site copy is US English; internal docs Canadian English.
- Test performance and theme changes on Kinsta staging (`env-mujolearningsystem-mujo.kinsta.cloud`) first.
- Take a PageSpeed baseline (mobile + desktop, homepage + one textbook page + one hub) **before** any performance change, so the hours breakdown can show results.

## 3. Schema tasks (Rank Math)

Can likely be done via `wp-mujo` if the meta test passes; otherwise paste-in.

- [ ] **Book schema on textbook pages.** `isbn`, `author`, `publisher`, `bookFormat: EBook` via Rank Math custom schema.
  - **Needs from client:** ISBN per title and format, author names, publisher legal name (Mujo Learning Systems Inc.? confirm).
  - Product list: 13 high school CTE titles + 24 higher ed titles (see CLIENT.md section 2).
- [ ] **FAQPage schema** only on pages with a visible FAQ. List which pages have one first.
- [ ] **Hub pages: LocalBusiness to CollectionPage.** A textbook hub is not a local business.
- [ ] **Duplicate Organization `@id` (`/#organization`).** One from Rank Math, one hand-coded (LocalBusiness + Person).
  - Put full details in Rank Math > Titles & Meta > Local SEO: both addresses (Vancouver #602-1388 Homer St; Lahaina #A13-5295 Lower Honoapiilani Rd), phone 1.888.536.6856, logo, sameAs (Facebook, Instagram, LinkedIn, YouTube, X: see CLIENT.md section 10), founder Shawn Moore.
  - Find and delete the hand-coded block (check page content, widgets, theme header/footer, Simple Custom CSS and JS, any snippets plugin).
  - Rank Math settings are **not** reachable via the MCP; needs WP admin (or Claude in Chrome).
- [ ] **Product schema names.** Remove `&amp;` and the "| Higher Ed | Mujo" suffix. Check which variable Rank Math's product schema name uses (likely `%seo_title%`; should be `%title%`). Settings change: WP admin.
- [ ] **Trustindex schema.** Turn off its rich snippet/schema output (Trustindex settings). It injects a self-serving Product schema with a 5-star rating and the staging URL `mujolearningsystem.kinsta.cloud`.
- [ ] **Staging URL sweep.** Search content, meta and options for any other `kinsta.cloud` references.
- [ ] **Validate** every changed template in Google's Rich Results Test and Schema.org validator; screenshot results for the report.

## 4. On-page and indexing

- [ ] **Shop page `/shop/`.** Currently noindex, meta description is the template default "Products Archive | Mujo Learning Systems", H1 "All Products".
  - Decide with Britt: keep noindex on purpose (textbook hubs rank instead) or write real copy and index it. Recommendation to bring: keep noindex unless the shop gets unique copy, to avoid adding another competitor to the existing hub vs /shop/ cannibalization.
  - Fix the meta description and H1 either way.
- [ ] **Stray "was successfully added to your cart" text** rendering in page content site-wide. Likely a WooCommerce notice output in the wrong hook or a cached fragment. Find the source before removing.
- [ ] **llms.txt (Rank Math settings).** Exclude utility pages and calendar embeds. Add a short intro: who Mujo serves, the five pathways, number of titles, state approvals (Texas IMRA only for the two Texas Edition titles; confirm others), links to the two audience hubs, the Shop and the FAQ pages. Draft the intro for Britt's approval first.

## 5. Accessibility and performance (dev: coordinate with Andrew)

- [ ] **Zoom lock.** Viewport has `maximum-scale=1, user-scalable=0`. Change to `width=device-width, initial-scale=1` via Salient theme settings or a child-theme filter.
- [ ] **Inline CSS 686 KB.** WP Rocket > File Optimization > Remove Unused CSS: clear Used CSS, trim the safelist to specific selectors, regenerate. If still over 150 KB, switch to Load CSS Asynchronously and compare in PageSpeed.
- [ ] **Hero image lazy-load.** Add `Jul062023-MujoLearningSystems_0654` to WP Rocket lazy-load exclusions. Serve as WebP, max 1600 px wide.
- [ ] **WebP/AVIF.** Enable MyKinsta CDN image optimization, or Imagify/ShortPixel, and bulk-convert the Media Library.
- [ ] **Render-blocking head scripts.** Move `custom-css-js/30075.js` to footer (Simple Custom CSS and JS). Test disabling jQuery Migrate in Salient performance settings.
- [ ] **Regression check** after the above: menus, mobile nav, cart, checkout, forms (Gravity Forms), Calendly embeds.
- [ ] PageSpeed after-scores vs the baseline.

## 6. Replies owed to Britt

- [ ] **Monthly SEO hours breakdown.** Where hours go each month, by category (technical/dev, schema, content, reporting, security). Source: Teamwork project 1146973 time logs. She also asked for a monthly work log on 2026-01-15.
- [ ] **Language tag answer.** Recommendation: switch Settings > General > Site Language to **English (United States)** (`en-US`), since most buyers are in the US (65% of GSC clicks), prices are USD and copy is US English. Points to include:
  - `lang` is a weak signal; Google infers audience mostly from content, currency and links. Consistency fix, not a ranking lever.
  - No hreflang needed (single-language site).
  - Also switches WP admin and WooCommerce strings to US English; harmless.
  - Confirm Rank Math's `inLanguage` follows the change.
  - Confirm nothing deliberately relies on the Canada signal (Canada is ~10% of clicks; higher ed ads run CA + US).
- [ ] **Estimate.** Hours estimate for this whole list vs the 10-hour monthly scope; agree priority order with Britt/Andrew.

## 7. Suggested order

1. MCP test (section 1) and PageSpeed baseline.
2. Quick schema wins with no client input: Trustindex off, hub CollectionPage, product name variable, Organization merge.
3. Shop page meta/H1, stray cart text.
4. Book schema (once ISBNs arrive), FAQPage.
5. llms.txt (after Britt approves the intro).
6. Performance items with Andrew, on staging first.
7. Reply to Britt: hours breakdown, language tag, estimate.

## 8. Open questions for the client

- ISBNs, author names and publisher legal name for Book schema.
- Shop page: index or keep noindex?
- "State approvals" for llms.txt: which states besides Texas, if any?
- Is the Canada signal (`en-CA`) deliberate for higher ed?
