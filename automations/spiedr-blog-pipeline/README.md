# SPIEDR blog pipeline: link + Quick Answer fixes (test copy)

Status (2026-10-28): **tested, not yet in the live scenario.**

- Live scenario: `SPIEDR Blog Draft Publisher` (Make 6209700, inactive, run by hand). Unchanged.
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
- Promote to the live scenario only after a sign-off. Copy modules 35, 30, 31, 36, 32, 33, 37, 34 into 6209700 and repoint module 16's input to `{{31.text}}` and module 23's input to `{{34.text}}`.
- Other client publishers (Vision 6209699, Jamie Davis 6209702, John Sadler 6209698) have the same link bug; the Quick Answer step is SPIEDR-specific.
