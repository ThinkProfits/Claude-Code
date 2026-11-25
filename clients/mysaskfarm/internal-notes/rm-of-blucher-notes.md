# Internal notes: RM of Blucher page draft (2026-11)

Internal only. Never paste into the client doc. Client-facing copy: [../rm-page-draft-rm-of-blucher-2026-11.md](../rm-page-draft-rm-of-blucher-2026-11.md).

## Original draft header (v1, 2026-11-24)


- **Status:** DRAFT, not built, not sent. Prepared 2026-11-24 by Francis (with Claude) so it's ready if Grant hasn't replied about Corman Park by Wed 2026-11-25 / Thu 2026-11-26 (scrum 2026-11-23). New page, so Grant approves before it goes live (CLIENT.md s8).
- **Pattern:** follows the live `/rm-of-corman-park/` page (Andrew published Francis's edits 2026-11-20), section for section. Brand-new page, so standard content layout, not the Current | Replacement table (`memory/page-update-doc-format.md`).
- **Before publishing:** clear every `[VERIFY]` tag below. Sources and the open list are in "Implementation Notes" at the end.

| Field | Value |
|---|---|
| Page URL (slug) | `https://mysaskfarm.com/rm-of-blucher/` (matches the existing `/rm-of-[name]/` pattern) |
| Title tag (53 chars) | RM of Blucher No. 343 Farmland for Sale \| MySaskFarm |
| Meta description (150 chars) | Farmland for sale in the RM of Blucher No. 343, southeast of Saskatoon near Allan, Clavet and Bradwell. Crop yields, land values and current listings. |
| Primary keyword | farmland for sale rm of blucher (no Planner volume; GSC-level term) |
| Secondary keywords | rm of blucher (320/mo), rm of blucher map (50/mo), rm 343 (40/mo) |
| Search intent | Primary: transactional / local (buyers and sellers of land in the RM). Secondaries: navigational (ratepayers and landowners looking up the RM), which is the seller audience Grant wants |

Volumes: Google Ads Keyword Planner, Canada, 12-month average to Oct 2026, pulled 2026-11-24. "land for sale blucher" and "farmland for sale rm of blucher" return no Planner data.

---


## Implementation Notes (internal, not page copy)

### Dev notes
- Build by duplicating the live Corman Park page (ID 521) in Elementor and swapping RM-specific copy. Keep shared blocks identical.
- Listing feed: point the BenchMetrics widget at RM 343. Check the feed returns land listings (not just acreages) before publishing.
- AIOSEO: set the title and meta above. Schema: one WebPage + AdministrativeArea (`name` "Rural Municipality of Blucher No. 343", `sameAs` https://rm343.com/) + BreadcrumbList + FAQPage matching the visible FAQ. One WebPage node only.
- **Fix the sitewide "Browse Other RMs" list:** it labels the RM "Blucher No. 434". The correct number is 343 (434 is Blaine Lake). Change the label and point it to `/rm-of-blucher/`. Minor fix, no Grant approval needed.

### Internal links on this page
| Anchor text | Target |
|---|---|
| See Blucher Listings | `#listings` |
| What's My Land Worth? / free, no-pressure evaluation | https://mysaskfarm.com/sell/ |
| How Much Is an Acre of Farmland Worth in Saskatchewan? | https://mysaskfarm.com/blog/how-much-farmland-acre/ |
| Saskatchewan Farmland Prices: Are Land Values Still Going Up? | https://mysaskfarm.com/blog/saskatchewan-farmland-prices/ |
| The Best Time to Sell Farmland in Saskatchewan | https://mysaskfarm.com/blog/best-time-sell-farmland-saskatchewan/ |
| Contact Grant Ostapowich / Buy or Sell Sask Farmland Today! | https://mysaskfarm.com/contact/ |
| Corman Park No. 344, Dundurn No. 314, Aberdeen No. 373 (Browse block) | https://mysaskfarm.com/rm-of-corman-park/ , https://mysaskfarm.com/rm-of-dundurn/ , https://mysaskfarm.com/rm-of-aberdeen/ |

**Links in (add when this page goes live; minor edits, no Grant approval needed):**
- `/rm-of-corman-park/`, `/rm-of-dundurn/`, `/rm-of-aberdeen/`: add a Blucher No. 343 card/link to `/rm-of-blucher/` in their Browse block.
- `/rm-of-dundurn/` copy says the RM includes "the hamlets of Blucher and Pike Lake". Blucher is a hamlet in the RM of Blucher (Wikipedia) `[VERIFY]`, so that sentence is wrong and also uses the word "Blucher" on the wrong page. Fix it when Dundurn is rewritten.

**Outbound:** rm343.com, FCC Farmland Values Report, Sask RM Yields dashboard. No competitor realtors.

### Sources (each fact on the page)
| Fact | Value | Source | Status |
|---|---|---|---|
| Population 2021 / 2016 | 1,984 / 2,006 (-1.1%) | StatCan 2021 Census Profile, CSD 4711069, via the official API: https://api.statcan.gc.ca/census-recensement/profile/sdmx/rest/data/STC_CP,DF_CSD/A5.2021A00054711069.1.1+2+3+7.1?format=csv . Human link to cite: https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&DGUIDlist=2021A00054711069 | Confirmed 2026-11-24 |
| Land area | 789.40 km² | Same StatCan API | Confirmed |
| Census division | No. 11 | StatCan code 4711069 | Confirmed |
| "10 minutes south-east of Saskatoon"; potash mines (Patience Lake, Allan), Clavet fertilizer depot, Cargill Clavet, CN and CP rail; "four primary weight highways" | | https://rm343.com/rm-information/ | Confirmed |
| RM office | 34 Struan Street, Bradwell; Hwy 5 | https://rm343.com/contact/ | Confirmed |
| Communities (Allan town; Bradwell, Clavet villages; Elstow special service area; Blucher, Cheviot hamlets) | | https://en.wikipedia.org/wiki/Rural_Municipality_of_Blucher_No._343 | `[VERIFY]` |
| Neighbours (Corman Park, Dundurn, Lost River, Colonsay, Grant, Aberdeen) | | RM council minutes March 2023 (reeves of those RMs): https://rm343.com/wp-content/uploads/2023/04/03-March-2023.MIN_.pdf ; 1921 census GIS | Likely, `[VERIFY]` against a current map |
| Highways 16, 316, 397 | | Wikipedia | `[VERIFY]` |
| Soil zone | | Not found | `[VERIFY]` |
| Crop yields 2016 to 2025 | table above | Sask RM Yields CSV (`/export/rm-yields-data/4950.csv`), RM 343, computed 2026-11-24 (method reproduces live Corman Park figures exactly). Corman Park 2021 spring wheat = 11.3 | Confirmed |
| Provincial FCC % changes | 15.7 / 13.1 / 9.4; regions 12.1 / 4.8 | FCC Farmland Values Report (already cited on live pages) | Confirmed (as published) |
| SAMA assessment explainer | | Word for word from the approved Corman Park page | Approved copy |

### Open `[VERIFY]` items
1. Soil zone (likely Dark Brown, unsourced).
2. Communities: Elstow's status and the hamlets of Blucher and Cheviot.
3. Neighbouring RMs against a current boundary map.
4. Highway 16 (used in the price section) and the full highway list.
5. FCC region for RM 343 (only for the optional region sentence).
6. "Patience Lake was Canada's first potash mine (1958)" is a nice local fact but Wikipedia-only, so it's left out.

### PAA / question research
- Semrush `phrase_questions` unavailable (API units at zero, 2026-11-24).
- Google.ca SERP "rm of blucher" (2026-11-24) People Also Ask: "Where is the RM of Blucher?" (used as the first FAQ). Google rate-limited further checks; not bypassed.
- Other FAQ questions come from the template PAA set (rm-page-template-research.md s3.2) and Grant's top FAQs (CLIENT.md s8). "What is the RM of Blucher known for?" is inferred from search results, not a PAA box.
- The SERP for "farmland for sale rm of blucher" is all listing portals and other realtors (one portal title showed 12 land listings in RM 343 on 2026-11-24). We don't quote listing counts on the page.

### Cannibalization check (2026-11-24)
- No `/rm-of-blucher/` page or draft exists (wp-mysaskfarm page list, status any).
- The word "Blucher" appears on `/rm-of-dundurn/` (wrong-RM hamlet mention, see above) and in the sitewide RM list (wrong number). Neither targets Blucher, but fix both so Google doesn't associate Blucher with the Dundurn page.
- No blog post covers Blucher.

### Rules check
- Farmland only (no acreage or residential angle), no price or ranking guarantees, no "best" claims, every figure sourced, free evaluation kept separate from paid appraisals, no competitor links, Century 21 Fusion named as the brokerage, no em dashes.

## Review log

### Pass 1 (2026-11-24): independent fact-check + standards review, applied in v2
- Client file now holds only page URL, title, meta, keywords, intent and the page copy. Everything internal moved here (memory/client-facing-blog-drafts.md).
- Cut shared boilerplate: per-RM intro (40-60 words), listings blurb, price section, Buying/Selling copy and FAQs. Dropped the SAMA FAQ (duplicated the H3), the "how much is it worth" and "crop yields" FAQs (repeated H2s) and the "best time" FAQ (moved to an inline link in the Selling H3). Added an RM-office contact FAQ and Grant's top FAQ ("Are farmland prices still going up?").
- Yields shown as bullets to match the live Corman Park page (and the portrait, no-table docx standard for new pages).
- Soil zone removed from the page until sourced (it would have shown an empty field).
- Added `/listings/` link, census division, neighbour links in the Browse block. "FAQs About the RM of …" (added "the").
- Fixed: Cargill described exactly as the RM does ("Cargill's Clavet facility"), potash mines phrased as part of the RM's economy (RM wording), rail "served by", 2021 wheat "fell to 22 … still about double Corman Park's 11.3". Highway 16 cleared (Clavet/Elstow on Hwy 16; Gov. of SK Clavet twinning backgrounder Oct 2016 per reviewer).
- 2025 canola (46.3) is the RM's highest of 2016-2025 (next 45.4 in 2017).

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
- v3 specifics: dropped "Blucher's 2021 wheat was about double Corman Park's". It's true (22 vs 11.3) but cherry-picked: the median RM in the province reported 30.8 bu/ac that year, so Blucher was below the provincial median. Office line corrected (the "south of Highway 5" wording on rm343.com/contact refers to the waste transfer station, not the office). Elstow removed (Wikipedia-only). Highways 5 and 16 sourced: RM 343 commercial-nodes memo, https://rm343.com/wp-content/uploads/2025/05/commercialnodes.pdf ("Highway Nos. 5 and 16"). Neighbour list removed from the copy (council-minutes inference only); Browse block says "Nearby RMs".
- **Open `[VERIFY]` (2 tags, same fact):** Allan (town), Bradwell and Clavet (villages) inside the RM (Wikipedia only; the RM site names Clavet and Allan facilities but doesn't list its communities).
- Still open in notes only: soil zone.

## Google Doc (uploaded 2026-11-24)

- [MySaskFarm | New RM Page: RM of Blucher No. 343 (Draft for Review)](https://docs.google.com/document/d/17HMMTpOTtor81WsEhwnOeOkSjpMkyu-QkhR1O-7RxEM/edit), in Drive > Mysaskfarm > SEO & AEO 2026, next to the Corman Park template doc. The folder is readable by anyone with the link (inherited), so do not paste internal notes into it.
- The Google Doc does not sync with the `.md`/`.docx`. If you edit one, update the other.
