# SPIEDR blog pipeline: link + Quick Answer fixes (test copy)

Status (2026-10-28): **live in scenario 6209700 as v1.5** (still inactive, run by hand). Not yet exercised on a real queue row.

- Live scenario: `SPIEDR Blog Draft Publisher` (Make 6209700, inactive, run by hand). Updated 2026-10-28 00:02 UTC with modules 35, 30, 31, 36, 32, 33, 37, 34; module 16 now reads `{{31.text}}`, module 23 reads `{{34.text}}`. Everything else (sheet queue, slug check, image upload, createPost, read-back, error handlers) unchanged. The v1.4 blueprint is in Make's scenario version history if a rollback is needed.
- Test copy: `SPIEDR Blog Draft Publisher [TEST - link + Quick Answer fixes - INACTIVE]` (Make 6803456, on-demand, left deactivated). It only exports a Doc and runs the cleanup chain. It writes nothing to the sheet or WordPress.
- `test-blueprint-6803456.json` is that test copy's blueprint. `replay_chain.py` re-runs the same patterns locally against a Doc's HTML export, because Make doesn't keep module output for API runs.

## New steps (inserted into the existing chain)

| Module | After | Does |
|---|---|---|
| 35 | 15 (body extract) | Drops everything up to and including the H1: the doc's Meta Title / Meta description / URL slug lines, `<hr>`, and the title (WordPress sets the title from the sheet). |
| 30 | 35 | Unwraps `https://www.google.com/url?q=<real>&sa=D…` to `<real>`. |
| 31 | 30 | Decodes `%23` back to `#` (broke the WorkSafeBC section link). |
| 36 | 22 (id strip) | Cuts the `GBP POST` heading and everything after it. Without this the GBP post became two extra FAQ items. |
| 32 | 36 | Removes the empty `&nbsp;` anchors Docs splits links into. |
| 33 | 32 | Removes empty headings. |
| 37 | 33 | Removes empty paragraphs and leftover `<hr>`. |
| 34 | 37 | Turns the first `Quick answer:` paragraph into the post-8921 table: `<table><tbody><tr><td><p><b>Quick Answer:</b></p><p>…</p></td></tr></tbody></table><p>&nbsp;</p>`. |

## Test result (drills Doc `1eUshhUIs3Ji4PST3DNuAlaF5UPnEOb2ChuCBtDgNolw`)

- Make run 7719d22f460b4d73a8a4e50d39a683e3: success (all patterns valid in Make).
- Local replay of the same patterns: 0 google.com links, 0 empty anchors or headings, 0 `%23`; all 12 links point at the real pages; output starts with the Quick Answer table; FAQ has exactly the 5 real questions; GBP post and preamble gone.

## Still open

- FAQs: the chain still builds the native `<details>` block, which SPIEDR can't use (needs Easy Accordion, see `clients/spiedr/CLIENT.md` section 8). Decide between a manual group step or a WPCode snippet that exposes the accordion meta.
- First real run: check the WordPress draft for links, Quick Answer table, no preamble or GBP post before publishing.
- Other client publishers (Vision 6209699, Jamie Davis 6209702, John Sadler 6209698) have the same link bug; the Quick Answer step is SPIEDR-specific.

## FAQ group endpoint (DRAFT, not installed)

`wpcode-faq-group-endpoint.php` adds `POST /wp-json/spiedr/v1/faq-group` so Make (or the `wp-spiedr` MCP via `wp_rest_write`) can create an Easy Accordion group without a person in wp-admin.

**Why a route rather than exposing the meta:** the questions live in `sp_eap_upload_options` and the display settings in `sp_eap_shortcode_options`, both serialized arrays. Registering them as raw REST meta would let any caller overwrite the plugin's whole settings array. The route only takes questions and answers. It copies every display setting from group 8925 and forces `eap_schema_markup` on. If the same title is sent again, it returns the existing group (`created: false`), so a Make retry won't make duplicates.

**Request:** `{"title": "FAQ for <post title>", "faq_html": "<h3>Q</h3><p>A</p>..."}`, or `faqs: [{question, answer}]`.
**Response:** `{"id": 9001, "shortcode": "[sp_easyaccordion id=\"9001\"]", "title": "...", "count": 5, "created": true}`.

### Install (needs Andrew's OK first: it adds code to the client's site)
1. wp-admin → Code Snippets (WPCode) → Add New → PHP Snippet. Paste the file **without** the opening `<?php` line.
2. Insert method: Auto Insert, Location: Run Everywhere. Save as **inactive** first, then activate.
3. WPCode's error handler deactivates the snippet on a fatal error. The `wp-spiedr` MCP can read that via `wp_ability_wpcode_detect_snippet_errors` / `get_error_logs`.
4. Not linted yet: there was no PHP on the drafting machine. WPCode checks the syntax on save.

### Test (in this order)
1. `wp_rest_routes` with search "faq-group": the route is listed.
2. `wp_rest_write` POST `/spiedr/v1/faq-group` with title "TEST FAQ group - delete me" and two short Q&As. Expect `created: true`.
3. Read the new group back (`wp_get_post_full`, post_type `sp_easy_accordion`, context edit). The `sp_eap_upload_options` items match. `sp_eap_shortcode_options` matches 8925 except `eap_accordion_uniq_id`.
4. Send the same request again. Expect the same id and `created: false`.
5. Put the shortcode on a **draft** post, open a preview link, and check that the accordion renders and the page has `FAQPage` JSON-LD.
6. Move the test group and the draft to Trash.

### Make wiring (after the endpoint passes)
- After module 23 (FAQ parser), add a WordPress "Make an API call" step: POST `spiedr/v1/faq-group`, body `{"title": "FAQ for {{1.`0`}}", "faq_html": "{{23.faq}}"}`. **Check first:** Make's WordPress module may prefix `wp/v2/` to the URL. If it does, use an HTTP module with the same credentials instead.
- Module 25 becomes `{{23.before}}<h2>Frequently Asked Questions: {{1.`0`}}</h2>{{new.shortcode}}{{23.after}}`. Module 24 (native `<details>`) goes. Agree the heading wording with Andrew. The live examples use a short topic, not the full post title.
- If the call fails, the error handler should still create the draft. Write the plain FAQ HTML and set the sheet status to "Draft Created – FAQ group needed", so a person can fall back to the manual group step.
