# Handoff: John Sadler live page edits (from session of 2026-11-11)

Start a new session in `E:\ThinkProfits\Claude-Code` and paste or point it at this file.

## Goal

Apply agreed content fixes to the live site www.johnsadler.ca, **one page at a time**. After each page is finished and checked, stop and report to Francis before starting the next page. Francis reviews proposed edits in chat first (a Current | Replacement table). Small text tweaks only, no layout or content overhauls.

## Read first

1. `clients/john-sadler/CLIENT.md`, sections 8 (content rules) and 11 (working rules)
2. `clients/john-sadler/CARD.md` (status)
3. `clients/john-sadler/site-crawl-2026-11-11.md` (crawl findings and priority list)
4. `clients/john-sadler/page-update-heating-cooling-hub-2026-11-11.md` (page 1, approved by Francis)

## Before any live edit

- **Confirm Andrew's OK.** At the 2026-11-10 check-in Andrew asked us to hold site edits ("don't go wild") until he shares the client-meeting outcome. Ask Francis to confirm the hold is lifted before writing anything.
- **Connection:** the `wp-john-sadler` MCP server (Easy MCP AI 2.4.1, `https://www.johnsadler.ca/wp-json/easy-mcp-ai/v1/mcp`). The token is valid (tested 2026-11-11). Kinsta's edge firewall returns an HTML **403** to requests without a browser User-Agent. If the MCP tools fail with 403, add a browser `User-Agent` header next to `Authorization` in the `wp-john-sadler` entry of `~/.claude.json` (with Francis's OK), or ask Kinsta to allowlist the endpoint.
- **Site setup:** WordPress on Kinsta, "prohauz" child theme, **Bold Page Builder**. Page text sits inside builder shortcodes, so edit with `wp_replace_in_post` (literal search, `expected_count` set) rather than rewriting whole pages. Check whether the "Why Choose John Sadler" 7-item block is a shared/reusable element before editing it page by page: the crawl found the same block on 7 pages.
- **After each page:** re-fetch the page (REST API or `wp_get_page`) and confirm every change, clear the cache (`wp_clear_cache`), note the revision for rollback, and log the page as done in this file and in CARD.md.

## Page queue

### 1. /services/heating-cooling/ (page ID 4042): approved, not yet applied

Apply `page-update-heating-cooling-hub-2026-11-11.md` exactly.

- **Do first:** remove the "barrie" link chip in Why Choose item 6. It's a pasted ChatGPT citation linking to barrieheatingcooling.ca. Delete the whole wrapping `<span>` and the word "barrie".
- Meta description: Yoast field, so change it via post meta or the Yoast ability, not post content.
- Held back until the client confirms: the emergency/24/7 wording (already removed in the replacements), and the Colin and client questions listed in the doc's Implementation Notes. Don't invent answers.

### 2. /services/plumbing/hot-water-tanks/ (page ID 8439): proposed in chat, NOT yet approved

Francis was shown these edits but hadn't approved them when the session ended. Show the table again and get a yes before applying. Then build `page-update-hot-water-tanks-2026-11-11.md/.docx` in the same format as the hub doc (verbatim Current, Keep Section rows, link table).

| # | Section | Current | Replacement |
|---|---|---|---|
| 1 | Meta description | Hot water tank repairs & maintenance in the GVA & Lower Mainland. Reliable service by licensed plumbers & gas fitters since 1976. | Hot water tank repair and maintenance in Surrey, White Rock and Langley. Licensed plumbers and gas fitters with 50 years in the Lower Mainland. Book today. |
| 2 | Call button | link `tel:1-(604)531-4355` | Same visible text, link `tel:+16045314355` |
| 3 | Why Choose subline | Serving White Rock, Surrey & Langley for over 50 years! | Serving White Rock, Surrey and Langley for 50 years. |
| 4 | Why Choose items 1, 3, 4, 6, 7 | Same shared block as the hub page | Same replacements as the hub doc |
| 5 | Paragraph after the items | We have been the trusted choice for hot water tank service in Langley and Surrey for over 45 years. | We have provided hot water tank service in Surrey, White Rock and Langley for 50 years. |
| 6 | H2 "24/7 Emergency Hot Water Tank Repair" + paragraph | (on-call 24 hours a day, 7 days a week; rapid-response emergency service) | H2 "Leaking Hot Water Tank? Call Us": A leaking hot water tank can cause water damage fast. Turn off the gas or power to the tank and close the cold water supply valve at the top, then call us at (604) 531-4355. We repair hot water tanks across Surrey, White Rock and Langley. (Interim, until the client confirms 24/7.) |
| 7 | Area line | We proudly serve: Langley \| Surrey \| White Rock \| Maple Ridge \| Abbotsford | We proudly serve: South Surrey \| White Rock \| Surrey \| Langley |
| 8 | Button | Get a Free Quote Today! | Book Your Repair Today |
| 9 | FAQ: How much does a hot water tank repair cost? | Most standard hot water tank repairs range from $150 to $450… | The cost depends on the part that has failed, such as a thermocouple, gas valve or heating element. We diagnose the problem first and give you a clear repair estimate before any work begins, so you can decide whether a repair is worth it compared with a replacement. (Only if Andrew confirms prices are still off-limits; his new AC/heat pump pages show prices.) |
| 10 | FAQ: How often should I have my traditional tank serviced? | by 3–5 years | by three to five years |
| 11 | FAQ: Repair or replace? | …half the price of a new unit—or if the tank… / Minor issues like a $150 thermocouple replacement are worth doing… | …half the price of a new unit, or if the tank… / Minor repairs like replacing a thermocouple are worth doing… |
| 12 | FAQ: Can I do repairs myself? | …T&P safety valve is correctly calibrated and the high-voltage wiring meets BC Hydro safety standards. Attempting a DIY repair can void your home insurance… | …electric tanks run on high-voltage wiring, so repairs should be done by a qualified professional to BC electrical code. A DIY repair can also affect your home insurance and manufacturer warranty. |

Colin to confirm: "Red Seal Plumbers"; logos for Bosch, GE, NTI, Rinnai and Triangle Tube (not on the serviced-brands list); the "8 to 12 years" tank life.

### 3 onwards: from the crawl priority list (`site-crawl-2026-11-11.md`, section 2)

For each page, pull the live copy, draft small fixes, show Francis, apply, verify, report, then move on. Suggested order:

1. The rest of the shared-block pages (unless the block was fixed once in step 1):
   - /services/plumbing/hot-water-tanks-installs-replacement/
   - /services/plumbing/tankless-water-heaters/
   - /services/plumbing/tankless-water-heater-repair/
   - /boiler-installs-replacement/
   - /services/heating-cooling/boiler-repair/
2. Sitewide footer: remove Abbotsford (/home-2-2/footer/)
3. "Over 40/45 years" pages (list in the crawl file)
4. "Free estimate" pages
5. Superlatives
6. /plumbers-near-me/ is blocked: it waits for the client's answers on estimate fees, response time and 24/7

## Rules that apply to every edit

- Canadian English, no em or en dashes in new copy, "50 years"
- No Abbotsford
- No out-of-scope services: general plumbing repairs, drain cleaning, commercial (stratas are the exception), propane/oil, new construction
- No 24/7, emergency or same-day claims until the client confirms
- No "free estimate", no superlatives, no prices unless Andrew confirms otherwise
- Gas licence written as LGA0092486
- Phone numbers as `tel:+16045314355` links (CallRail)
- Never add new links to other companies' sites

## Log

| Page | Status | Date | Notes |
|---|---|---|---|
| /services/heating-cooling/ | **Done, verified live** (meta description set 2026-11-11) | 2026-11-11 | Francis confirmed Andrew's hold lifted and approved all hub-doc edits in chat. Barrie chip removed first. Rollback: revision 8559 (pre-edit, 2026-09-11). Kinsta cache cleared. Live check: no barrie link, single H1, all phone links `tel:+16045314355`, no em dashes, no free estimate/emergency/same-day wording. The meta description was set later the same day (see the Yoast row). An empty `[bt_bb_text][/bt_bb_text]` was left where the install-only section was (harmless). |
| /services/plumbing/hot-water-tanks/ | **Done, verified live** (meta description set 2026-11-11) | 2026-11-11 | Francis approved rows 1–12 including row 9 (prices removed). Rollback: revision 8580. Kinsta cache cleared. Live check: all 7 phone links `tel:+16045314355`, one H1, no 24/7, free quote, prices, Maple Ridge or "over 45/50" wording. Doc: [page-update-hot-water-tanks-2026-11-11.md](page-update-hot-water-tanks-2026-11-11.md). Flagged for later: the JSON-LD schema still has 24/7, prices and Abbotsford; the button tooltip says "GIVE ME FREE QUOTE"; item 5 has an en dash. |
| Yoast meta descriptions (both pages above) | **Done, verified live** | 2026-11-11 | Francis approved the doc wording in chat and switched on the Yoast SEO integration in Easy MCP AI. Set with `wp_update_post_meta` (`_yoast_wpseo_metadesc`, post_type `pages`). Kinsta cache cleared. Live source shows the new `description` and `og:description` on both pages. |
| /services/plumbing/hot-water-tanks-installs-replacement/ (ID 8429) | **Done, verified live** (incl. meta description) | 2026-11-12 | Francis approved all 17 rows in chat, including removal of the $1,200 to $2,600 FAQ price. Rollback: revision 8436. Kinsta cache cleared. Live check: every row present, the only phone link is `tel:+16045314355`, one H1, the meta is in the source. Also fixed the "hot water wank" typo and the tankless link, which pointed to the repair page. Doc: [page-update-hot-water-tank-installs-2026-11-12.md](page-update-hot-water-tank-installs-2026-11-12.md). Flagged: the JSON-LD schema has the price and Abbotsford/Maple Ridge, the "GIVE ME FREE QUOTE" tooltip, the item 5 en dash. |
| /services/plumbing/tankless-water-heaters/ (ID 4872) | **Done, verified live** (incl. meta + focus keyphrase) | 2026-11-12 | Francis approved all 10 rows. **This page also had the barrie chip, which was removed first.** Rollback: revision 8396. Kinsta cache cleared. Live check: no barrieheatingcooling.ca, only `tel:+16045314355`, one H1, the meta is in the source. Doc: [page-update-tankless-water-heaters-2026-11-12.md](page-update-tankless-water-heaters-2026-11-12.md). **Barrie chip still live on /tankless-water-heater-repair/ (6377) and /boiler-repair/ (4155)**, the next two in the queue. |
| /services/plumbing/tankless-water-heater-repair/ (ID 6377) | **Done, verified live** (incl. meta) | 2026-11-12 | Francis approved all 18 rows. Barrie chip removed first. Rollback: revision 8398. Kinsta cache cleared. Live check: no barrieheatingcooling.ca, only `tel:+16045314355` (3 phone numbers fixed or linked), one H1, the meta is in the source; "immediate service", "in no time", superlatives and free quote buttons removed. Doc: [page-update-tankless-water-heater-repair-2026-11-12.md](page-update-tankless-water-heater-repair-2026-11-12.md). Colin: the "tankless brands" list is mostly boiler brands. **Barrie chip still live on /boiler-repair/ (4155).** |
| /services/heating-cooling/boiler-repair/ (ID 4155) | **Done, verified live** (incl. meta + focus keyphrase) | 2026-11-12 | Francis chose to do it ahead of /boiler-installs-replacement/ because of the barrie chip, and approved all 14 rows. Barrie chip removed first. **No live page checked has the barrie link any more.** Rollback: revision 8388. Kinsta cache cleared. Also fixed the "Contact Us Today for Tankless Water Heater Repairs" section, which had been pasted onto the boiler page, and the /boiler-replacement/ link that redirected. Doc: [page-update-boiler-repair-2026-11-12.md](page-update-boiler-repair-2026-11-12.md). Colin: the boiler paragraph wrongly describes a hot water tank. Schema: "over 40 years" and an unverified Peace Arch News award. |
| /boiler-installs-replacement/ (ID 5138) | **Done, verified live** (incl. meta) | 2026-11-12 | Francis approved all 17 rows, including removal of the $8,000 to $15,000 FAQ price. Rollback: revision 8425. Kinsta cache cleared. Live check: only `tel:+16045314355`, no "GIVE ME FREE QUOTE" tooltips, one H1, the meta is in the source. "New build", "Is it an Emergency?", Maple Ridge/Abbotsford and the superlatives are gone. Doc: [page-update-boiler-installs-2026-11-12.md](page-update-boiler-installs-2026-11-12.md). **All 7 shared-block pages are now done.** Next in the queue: the sitewide footer (Abbotsford). |
| Sitewide footer /home-2-2/footer/ (ID 2153) | **Done, verified live** | 2026-11-12 | Francis approved both rows: (1) removed the "Abbotsford" list item from the Service Area list; (2) removed hidden `<span style="color: transparent">Plumber</span>` text from the Langley and White Rock links (hidden-text spam risk, on every page). Rollback: revision 8209. **Whole-site cache cleared** (Kinsta, Yoast sitemaps, Popup Maker, Smash Balloon). Spot-checked /, /services/heating-cooling/, /services/plumbing/hot-water-tanks/ and /contact-us/: no Abbotsford or hidden "Plumber" in the footer. Aldergrove kept, pending the client. The Abbotsford still on hot-water-tanks is its JSON-LD `areaServed` (already flagged). |

## Notes for whoever continues

- **Yoast meta:** the Yoast SEO integration is now on, so `wp_update_post_meta` with `_yoast_wpseo_metadesc` (post_type `pages`) works.
- **The "Why Choose" block is not shared.** On the hub page it's an inline `bt_bb_accordion` in the page content, so fix it page by page.
- **`wp_replace_in_post` limits:** search max 500 chars, and regex mode is off for pages over 20 KB. Live content uses CRLF line endings and some non-breaking spaces, neither of which can be typed into a search. Keep each search on one line, split around NBSPs, and check uniqueness with `expected_count: 1`. Never split a shortcode pair across two edits: a half-applied split briefly exposed a fragment on page 4042 until it was repaired.
