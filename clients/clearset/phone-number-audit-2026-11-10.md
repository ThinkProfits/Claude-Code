# Clearset: phone number audit (2026-11-10)

**Rule (Andrew, #clearset, 2025-11-22 and 2026-11-10):** the site only ever contains the main number **(778) 825-1032**, and every mention is a `tel:` link. CallRail's website pool swaps it on the live page. Never hard-code a pool number: (778) 652-6317, (778) 655-4208, (778) 907-9875, (778) 400-6421 (full list in CLIENT.md).

**How this was checked:** pulled the raw server HTML (before CallRail runs) of all 28 URLs in `page-sitemap.xml` (no posts or Divi projects are published), scanned visible text, `tel:` links and JSON-LD schema. Then loaded the pages with CallRail running to confirm what visitors see. Swap test on 2026-11-10: CallRail served (778) 655-4208, and every hard-coded pool number below stayed on the page beside it, so visitors see two different numbers.

## 1. Hard-coded pool numbers in page copy (fix first)

Replace each with `<a href="tel:7788251032">(778) 825-1032</a>`.

| Page | Where | Current |
|---|---|---|
| `/` (homepage) | Service areas section (`cs-areas-note`): "Not sure if we cover your area? Call **(778) 652-6317**" | bold text, no link |
| `/services/septic-tank-cleaning/` | Content section, paragraph starting "Most residential tanks in BC range from 1,000 to 1,500 gallons..." | **(778) 907-9875**, bold, no link |
| `/services/hydrovac-excavation-and-hot-water-services/` | Content section: "For an accurate quote on your project, call **(778) 907-9875**" | bold, no link |
| `/services/hydrovac-excavation-and-hot-water-services/` | Button "Call (778) 652-6317 for a free consultation" | link goes to the main number but the **visible text** is a pool number, so it never swaps |
| `/services/portable-toilet-rentals/` | Intro (`cs-page-intro`), paragraph starting "Clearset VAC Truck Services rents clean, fully serviced portable toilets..." | **(778) 907-9875**, bold, no link |
| `/services/portable-toilet-rentals/` | Sizing guide subhead: "Use this guide as a starting point. Call us at **(778) 907-9875**..." | no link |
| `/services/water-hauling/` | Intro (`cs-page-intro`), paragraph starting "Clearset VAC Truck Services provides non-potable water truck delivery..." | **(778) 400-6421**, bold, no link |
| `/services/water-hauling/` | FAQ: "Water hauling pricing is based on volume... Contact Clearset at **(778) 400-6421** for a quote." | no link |

## 2. Main number written as plain text (needs to become a link)

| Page | Where |
|---|---|
| `/` | FAQ: "Yes. Clearset operates a 24/7 emergency dispatch line at (778) 825-1032..." |
| `/services/septic-tank-cleaning/` | Intro paragraph starting "Septic tank pumping is the process of removing accumulated sludge..." |
| `/services/septic-tank-cleaning/` | Content: "Call (778) 825-1032 for 24/7 emergency septic service across Metro Vancouver..." |
| `/services/septic-tank-cleaning/` | FAQ: "Septic tank pumping in the Metro Vancouver area typically ranges from $250 to $500..." |
| `/services/hydrovac-excavation-and-hot-water-services/` | Intro paragraph starting "Hydrovac excavation is a non-destructive digging method..." |
| `/services/hydrovac-excavation-and-hot-water-services/` | FAQ: "...Emergency situations are handled on a priority basis — call (778) 825-1032." |
| `/services/portable-toilet-rentals/` | Pricing paragraph: "...Contact Clearset at (778) 825-1032 for a current quote." |
| `/services/portable-toilet-rentals/` | Service area paragraph: "...Call (778) 825-1032 to confirm coverage." |
| `/services/trailers-and-rvs-pumping/` | FAQ: "RV pump-out pricing varies... Contact Clearset at (778) 825-1032 for a current quote." |

## 3. Schema (JSON-LD): wrong number on every page

- A custom `LocalBusiness` schema block on **all 28 pages** has `"telephone": "+1-778-907-9875"` (a pool number). It is not Yoast's output, so it is a sitewide snippet: check Divi > Theme Options > Integration (head code), Divi Theme Builder, or a code-snippet plugin. CallRail cannot swap schema, so Google reads the pool number as the business phone. Change to `+1-778-825-1032`.
- `/septic-system-service-burnaby/` and `/septic-tank-cleaning-richmond/` carry a second `LocalBusiness` block with `"telephone": "778-655-0608"`. That number is not on our CallRail list in CLIENT.md, so ask Andrew whether it is anything at all, then change it to the main number. These two pages therefore output two LocalBusiness blocks; one should go.

## 4. Minor

- `/septic-system-service-burnaby/` and `/septic-tank-cleaning-richmond/` have a link written as `tel:+1(778)8251032`. In the swap test it came out malformed. Use the same `tel:7788251032` format as the rest of the site.
- Homepage Instagram feed (Smash Balloon, `sbi_bio`) prints the Instagram bio, which includes "778-825-1032" as plain text. That comes from Instagram, not WordPress, so it can't become a link there. Either hide the bio in the feed settings or leave it (it is the main number, so it's harmless, and CallRail swapped it in the test).
- BC One Call (1-800-474-6886) on the hydrovac page is a third-party number and is fine as is.

## Already clean

Header, footer and button links site-wide use `tel:7788251032` and swap correctly. The RV page's quick answer section (fixed by Andrew) now has only the main number.

## Re-test after fixes

Open each page above in an incognito window. Every number on the page should match, and none should be (778) 825-1032.

---

## Fixes applied 2026-11-11 (Francis + Claude, via the wp-clearset MCP)

All edits were made in raw post_content (back end, not the Divi visual builder), so CallRail could not save a swapped number. Each edit is in WordPress revisions.

**Status: every item in sections 1, 2 and 4 is fixed, and so is the 655-0608 schema. One item is left for wp-admin: the sitewide head schema (section 3, first bullet).**

| # | Item | Done |
|---|---|---|
| 1 | Homepage areas note: (778) 652-6317 | Replaced with `<a href="tel:7788251032">(778) 825-1032</a>` |
| 1 | Septic tank cleaning: (778) 907-9875 | Same |
| 1 | Hydrovac: (778) 907-9875 in content | Same |
| 1 | Hydrovac button text "Call (778) 652-6317 for a free consultation" | Text now "Call (778) 825-1032 for a free consultation" (button already links to the main number) |
| 1 | Portable toilets: (778) 907-9875 ×2 (intro, sizing guide) | Replaced with the linked main number |
| 1 | Water hauling: (778) 400-6421 ×2 (intro, FAQ) | Replaced with the linked main number |
| 2 | Plain-text main number: homepage FAQ, hydrovac ×2, portable toilets ×2, septic tank cleaning ×3, RV FAQ | Wrapped in `tel:7788251032` links. FAQ JSON-LD copies were left as plain text, since a link would break the JSON. |
| 3 | Burnaby + Richmond: `"telephone": "778-655-0608"` | Changed to `+1-778-825-1032` |
| 3 | Old FAQ/LocalBusiness code block (broken JSON with doubled quotes) on 22 pages: `""telephone"": ""+1-778-907-9875""` | Changed to `+1-778-825-1032` |
| 4 | City pages: `tel:+1(778)8251032` / `tel:+1(778)825-1032` (desktop) and `tel:+1(778)208251032` (tablet/phone variants; this is where "(778) 208-2510" came from) | All changed to `tel:7788251032` on Port Coquitlam, Surrey, Burnaby, Richmond and Port Moody |

**Not changed:** the homepage Instagram bio (main number, comes from Instagram), BC One Call 1-800-474-6886, and the existing `tel:+1-778-825-1032` / `tel:1-778-825-1032` links (valid main-number links, CallRail swaps them).

### Re-test results (2026-11-11)

- **Raw server HTML, all 28 sitemap URLs:** no 652-6317, 655-4208, 400-6421, 655-1265, 724-1612, 655-0608 or malformed `tel:+1(` links anywhere. **907-9875 appears exactly once per page, and only in the sitewide head schema below.** No plain-text main numbers are left in page copy.
- **Swap test (built-in browser, 7 s wait, all 28 pages):** CallRail served (778) 907-9875 for this session. Every visible number and every tel: link on every page showed that one number. No page showed (778) 825-1032 or a second, different number.
- **JSON-LD:** none of these edits broke a valid block. Two broken blocks were already there and are still invalid (see below).

### Still to do in wp-admin (the MCP can't reach these)

1. **Sitewide head schema, `"telephone": "+1-778-907-9875"`.** It prints in `<head>` after the shortlink tag on every page. It is not from Yoast and not from WPCode snippets (only one PHP snippet is active). Check, in this order: **Settings › Head, Footer and Post Injections** (Head tab), **Code Snippets › Header & Footer** (WPCode Lite global header), then **Divi › Theme Options › Integration** ("Add code to the < head >"). Change the number to `+1-778-825-1032`. Also add `"@context": "https://schema.org",` as the first property, since the block has none.
2. **Old broken JSON-LD code block on 22 pages** (`""@context""` with doubled quotes, plus `[et_pb_line_break_holder]`). Google ignores it as invalid. Either delete it (Yoast and the newer blocks already cover the schema) or rewrite it with normal quotes. Richmond also has a block ending in `}} ] }}}` ("Extra data") that needs its brackets fixed.
3. Optionally switch on the **Divi** and **Yoast SEO** integrations under Easy MCP AI › Tools so future edits like these can be done over MCP.
