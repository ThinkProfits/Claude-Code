# Internal notes: RM of Vanscoy page draft (2026-11)

Internal only. Never paste into the client doc. Client-facing copy: [../rm-page-draft-rm-of-vanscoy-2026-11.md](../rm-page-draft-rm-of-vanscoy-2026-11.md).

## Original draft header (v1, 2026-11-24)


- **Status:** DRAFT, not built, not sent. Prepared 2026-11-24 by Francis (with Claude) so it's ready if Grant hasn't replied about Corman Park by Wed 2026-11-25 / Thu 2026-11-26 (scrum 2026-11-23). New page, so Grant approves before it goes live (CLIENT.md s8).
- **Pattern:** follows the live `/rm-of-corman-park/` page (Andrew published Francis's edits 2026-11-20), section for section. Brand-new page, so standard content layout, not the Current | Replacement table (`memory/page-update-doc-format.md`).
- **Before publishing:** clear every `[VERIFY]` tag below. Sources and the open list are in "Implementation Notes" at the end.

| Field | Value |
|---|---|
| Page URL (slug) | `https://mysaskfarm.com/rm-of-vanscoy/` (matches the existing `/rm-of-[name]/` pattern) |
| Title tag (53 chars) | RM of Vanscoy No. 345 Farmland for Sale \| MySaskFarm |
| Meta description (149 chars) | Farmland for sale in the RM of Vanscoy No. 345, southwest of Saskatoon. Crop yields, land values and current listings, or get a free land evaluation. |
| Primary keyword | farmland for sale rm of vanscoy (no Planner volume; GSC-level term) |
| Secondary keywords | rm of vanscoy (390/mo), rm of vanscoy map (110/mo), vanscoy land for sale (10/mo), rm 345 (10/mo) |
| Search intent | Primary: transactional / local (buyers and sellers of land in the RM). Secondaries: mostly navigational (ratepayers and landowners looking up the RM), which is the seller audience Grant wants |

Volumes: Google Ads Keyword Planner, Canada, 12-month average to Oct 2026, pulled 2026-11-24. "vanscoy sk" (1,000/mo) is the village name, not the RM, so it's not a target; the page will still mention the village naturally.

---


## Implementation Notes (internal, not page copy)

### Dev notes
- Build by duplicating the live Corman Park page (ID 521) in Elementor and swapping RM-specific copy. Keep shared blocks (assessment H3, Work with Grant intro, contact) identical.
- Listing feed: point the BenchMetrics widget at RM 345. Check the feed returns land listings (not just acreages) before publishing.
- AIOSEO: set the title and meta above. Schema: one WebPage + AdministrativeArea (`name` "Rural Municipality of Vanscoy No. 345", `sameAs` https://www.rmvanscoy.ca/) + BreadcrumbList + FAQPage matching the visible FAQ. Don't duplicate the WebPage node (the Corman Park double-node issue, rm-page-template-research.md s2.1).
- Map: optional H2 "Map of the RM of Vanscoy" ("rm of vanscoy map", 110/mo). Only embed a map we're licensed to use, or link to the RM's own map.

### Internal links on this page
| Anchor text | Target |
|---|---|
| See Vanscoy Listings | `#listings` |
| What's My Land Worth? / free, no-pressure evaluation | https://mysaskfarm.com/sell/ |
| How Much Is an Acre of Farmland Worth in Saskatchewan? | https://mysaskfarm.com/blog/how-much-farmland-acre/ |
| Saskatchewan Farmland Prices: Are Land Values Still Going Up? | https://mysaskfarm.com/blog/saskatchewan-farmland-prices/ |
| The Best Time to Sell Farmland in Saskatchewan | https://mysaskfarm.com/blog/best-time-sell-farmland-saskatchewan/ |
| Contact Grant Ostapowich / Buy or Sell Sask Farmland Today! | https://mysaskfarm.com/contact/ |
| RM of Corman Park No. 344 (Browse block) | https://mysaskfarm.com/rm-of-corman-park/ |

**Links in (add when this page goes live; minor edits, no Grant approval needed):**
- `/rm-of-corman-park/` Browse block: "Vanscoy No. 345" card/link to `/rm-of-vanscoy/` (it currently points to a listings-search URL with map coordinates).
- The sitewide "Browse Other RMs" list: change the Vanscoy No. 345 entry to link to `/rm-of-vanscoy/`.
- `/rm-of-dundurn/` copy currently says the RM includes "the hamlets of Blucher and Pike Lake". Pike Lake is in the RM of Vanscoy per Wikipedia `[VERIFY]` and Blucher is a hamlet in the RM of Blucher, so that sentence is wrong. Fix it when Dundurn is rewritten.

**Outbound:** rmvanscoy.ca, FCC Farmland Values Report, Sask RM Yields dashboard. No competitor realtors.

### Sources (each fact on the page)
| Fact | Value | Source | Status |
|---|---|---|---|
| Population 2021 / 2016 | 2,799 / 2,840 (-1.4%) | StatCan 2021 Census Profile, CSD 4712054, via the official API: https://api.statcan.gc.ca/census-recensement/profile/sdmx/rest/data/STC_CP,DF_CSD/A5.2021A00054712054.1.1+2+3+7.1?format=csv . Human link to cite: https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&DGUID=2021A00054712054 | Confirmed 2026-11-24 |
| Land area | 861.10 km² | Same StatCan API | Confirmed |
| Census division | No. 12 | Wikipedia + citypopulation.de | Wikipedia-level |
| RM office, website | 300 Main St, Vanscoy; rmvanscoy.ca | https://www.rmvanscoy.ca/ | Confirmed |
| Communities (Delisle, Asquith, Vanscoy, Grandora) | | https://en.wikipedia.org/wiki/Rural_Municipality_of_Vanscoy_No._345 | `[VERIFY]` |
| Neighbours (Corman Park N, Perdue W, Montrose S; river on east) | | Same Wikipedia page | `[VERIFY]` (east side not named) |
| Highways 7, 45 (also 672, 673) | | Same Wikipedia page | `[VERIFY]` |
| Soil zone | | Not found. Check AAFC "Soils of the Saskatoon Map Area (73B)": https://sis.agr.gc.ca/cansis/publications/surveys/sk/sks4/index.html | `[VERIFY]` |
| Crop yields 2016 to 2025 | table above | Sask RM Yields CSV (`/export/rm-yields-data/4950.csv`), RM 345, computed 2026-11-24. Same method reproduces the live Corman Park figures exactly | Confirmed |
| Provincial FCC % changes | 15.7 / 13.1 / 9.4; regions 12.1 / 4.8 | FCC Farmland Values Report (already cited on the live Corman Park page and the farmland-prices blog) | Confirmed (as published) |
| SAMA assessment explainer | | Carried over word for word from the approved Corman Park page | Approved copy |

### Open `[VERIFY]` items
1. Soil zone (likely Dark Brown, unsourced).
2. Communities inside the RM, and whether Grandora is a village or hamlet.
3. Neighbouring RMs, especially across the South Saskatchewan River on the east.
4. Highway numbers.
5. FCC region for RM 345 (only if we want the optional region sentence; FCC's region map is behind its sign-in).
6. Nutrien's Vanscoy potash mine was left out of the copy on purpose: only seen in a search snippet. Add it as a local fact only once confirmed.

### PAA / question research
- Semrush `phrase_questions` unavailable (API units at zero, 2026-11-24).
- Google.ca SERP "rm of vanscoy" (2026-11-24) People Also Ask: "Where is Vanscoy located?" and an RM dump-station hours question (not relevant). Google rate-limited further checks; not bypassed.
- FAQ also uses the PAA questions pulled for the RM template (rm-page-template-research.md s3.2): "Is there any land for sale in [RM]?", "price of an acre", plus Grant's top FAQs (CLIENT.md s8).
- The SERP for "farmland for sale rm of vanscoy" is all listing portals and other realtors (one portal title showed 14 land listings in RM 345 on 2026-11-24). We don't quote listing counts on the page.

### Cannibalization check (2026-11-24)
- No `/rm-of-vanscoy/` page or draft exists (wp-mysaskfarm page list, status any). No post mentions Vanscoy except the sitewide "Browse Other RMs" list.
- GSC (URL-prefix property, 2026-07-01 to 2026-11-22): zero queries containing "vanscoy", so no existing page is ranking for it.
- Overlap risk: low. Corman Park targets "land for sale near Saskatoon"; this page avoids that phrase and says "southwest of Saskatoon" instead.

### Rules check
- Farmland only (no acreage or residential angle), no price or ranking guarantees, no "best" claims, every land-value figure sourced, free evaluation kept separate from paid appraisals, no competitor links, Century 21 Fusion named as the brokerage, no em dashes.

## Review log

### Pass 1 (2026-11-24): independent fact-check + standards review, applied in v2
- Client file now holds only page URL, title, meta, keywords, intent and the page copy. Everything internal moved here (memory/client-facing-blog-drafts.md).
- Cut shared boilerplate: per-RM intro (40-60 words), listings blurb, price section, Buying/Selling copy and FAQs. Dropped the SAMA FAQ (duplicated the H3), the "how much is it worth" and "crop yields" FAQs (repeated H2s) and the "best time" FAQ (moved to an inline link in the Selling H3). Added an RM-office contact FAQ and Grant's top FAQ ("Are farmland prices still going up?").
- Yields shown as bullets to match the live Corman Park page (and the portrait, no-table docx standard for new pages).
- Soil zone removed from the page until sourced (it would have shown an empty field).
- Added `/listings/` link, census division, neighbour links in the Browse block. "FAQs About the RM of …" (added "the").
- Fixed: H1 geography (towns are inside the RM), neighbour "north and northwest", Grandora dropped (Wikipedia conflict: village vs hamlet), highways now "7, 14 and 45". Hwy 7 in the RM confirmed by the Gov. of SK Vanscoy-bypass twinning release (https://www.saskatchewan.ca/en/government/news-and-media/2019/september/23/twinning-on-highway-7); 14 and 45 Wikipedia-only.
- "Matched or beaten Corman Park for every major crop": true for all six; oats gap is only 0.7 bu, so wording is "matched or beaten". 2025 canola (54.9) is the RM's highest of 2016-2025 (next best 43.9 in 2020).
- Removed "including some who aren't farming the land" (acreage hint).

### Pass 2 (2026-11-24): fresh fact-check + standards review of v2, applied in v3 (current)
- Shared copy cut from about 54-62% (v2, sentence-level, names normalized) to 25-31% vs. the other drafts and 7-15% vs. Corman Park (v3, same script). What's left is mostly the brokerage line, the RM Yields source credit and address formats.
- Removed lines no source supports (local market claims such as "good quarters near Saskatoon don't sit long", "get noticed", "the convenience shows up in what buyers will pay"). Price factors are now stated as general factors, not observations about this RM. If Grant confirms local observations, add them back in his voice.
- Removed the "farmland has been in short supply… retiring farmers rent instead of selling" line: no source found (it's also on the live Corman Park page; worth sourcing or cutting there).
- Dropped the FAQ "Are farmland prices still going up?" (repeated the FCC H3). Linked the farmland-prices blog from the FCC H3 instead. FCC citation now says "annual Farmland Values Report" (2023 +15.7% and 2024 +13.1% come from earlier editions).
- SAMA H3 cut to one or two sentences. "Crops grown most years" bullet cut (the yield list covers it).
- Map keywords and other weak secondaries dropped from the client keyword line (no map on the page yet).
- All FAQ answers 40-60 words; titles 52-53 chars; metas 149-152 chars; no em dashes; all internal links returned 200 (checked by reviewer 2026-11-24).
- Browse block links the other two new pages. **Only add those links once both pages are live**; until then show Corman Park (and Dundurn/Aberdeen on Blucher) only.

### Before this goes to Grant
- Clear the inline `[VERIFY]` tags (see below), or cut the tagged facts.
- Send Grant the five local-knowledge questions (rm-page-template-research.md s7) in the cover message, not in the doc. A short "Grant's take on [RM]" section (100-200 words, his voice) is the single biggest way to make each page unique.
- Optional later: a "Map of the RM of [Name]" section (rm of vanscoy map = 110/mo) once we have a map we're allowed to use.
- v3 specifics: highways cut to "7" only (Hwy 7 through the RM and the Vanscoy bypass confirmed by Gov. of SK, 2019-09-23 release; 14 and 45 unconfirmed, and Wikipedia's RM page lists 7, 45, 672, 673 but not 14). River boundary and neighbour list cut from the copy (Wikipedia-only). Area now "861 km² of farmland around Vanscoy, Delisle and Asquith" rather than "crop land and pasture".
- **Open `[VERIFY]` (2 tags, same fact):** the towns of Delisle and Asquith and the village of Vanscoy are inside the RM's boundaries (Wikipedia only; rmvanscoy.ca doesn't list them). Grandora left out (Wikipedia calls it both a village and a hamlet).
- Still open in notes only: soil zone; census division 12 is from the StatCan CSD code 4712054 (47 = SK, 12 = division), so that one is confirmed.

## Google Doc (uploaded 2026-11-24)

- [MySaskFarm | New RM Page: RM of Vanscoy No. 345 (Draft for Review)](https://docs.google.com/document/d/1Ox34GpzBAYWGmpDCo89ZJnM3dTchRq0BjNjKo3d2Hx0/edit), in Drive > Mysaskfarm > SEO & AEO 2026, next to the Corman Park template doc. The folder is readable by anyone with the link (inherited), so do not paste internal notes into it.
- The Google Doc does not sync with the `.md`/`.docx`. If you edit one, update the other.
