# Internal notes: RM of Rosthern page draft (2026-11)

Internal only. Never paste into the client doc. Client-facing copy: [../rm-page-draft-rm-of-rosthern-2026-11.md](../rm-page-draft-rm-of-rosthern-2026-11.md).

## Original draft header (v1, 2026-11-24)


- **Status:** DRAFT, not built, not sent. Prepared 2026-11-24 by Francis (with Claude) so it's ready if Grant hasn't replied about Corman Park by Wed 2026-11-25 / Thu 2026-11-26 (scrum 2026-11-23). New page, so Grant approves before it goes live (CLIENT.md s8).
- **Pattern:** follows the live `/rm-of-corman-park/` page (Andrew published Francis's edits 2026-11-20), section for section. Brand-new page, so standard content layout, not the Current | Replacement table (`memory/page-update-doc-format.md`).
- **Before publishing:** clear every `[VERIFY]` tag below. Sources and the open list are in "Implementation Notes" at the end.

| Field | Value |
|---|---|
| Page URL (slug) | `https://mysaskfarm.com/rm-of-rosthern/` (matches the existing `/rm-of-[name]/` pattern) |
| Title tag (54 chars) | RM of Rosthern No. 403 Farmland for Sale \| MySaskFarm |
| Meta description (141 chars) | Farmland for sale in the RM of Rosthern No. 403, north of Saskatoon around Rosthern and Hague. Crop yields, land values and current listings. |
| Primary keyword | farmland for sale rm of rosthern (no Planner volume; GSC-level term) |
| Secondary keywords | rm of rosthern (260/mo), rm of rosthern map (30/mo), rosthern rm real estate (10/mo), rm 403 (10/mo) |
| Search intent | Primary: transactional / local (buyers and sellers of land in the RM). Secondaries: navigational (ratepayers and landowners looking up the RM), which is the seller audience Grant wants |

Volumes: Google Ads Keyword Planner, Canada, 12-month average to Oct 2026, pulled 2026-11-24. **Not targeted:** "rosthern acreage for sale" (110/mo) is excluded by the farmland-only rule (keywords.md s4). "rosthern sk" (2,400/mo) is the town name, not the RM.

---


## Implementation Notes (internal, not page copy)

### Dev notes
- Build by duplicating the live Corman Park page (ID 521) in Elementor and swapping RM-specific copy. Keep shared blocks identical.
- Listing feed: point the BenchMetrics widget at RM 403. Check it returns land listings, not just acreages: acreage demand around Rosthern is strong (see the excluded keyword above), so the feed may lean that way.
- AIOSEO: set the title and meta above. Schema: one WebPage + AdministrativeArea (`name` "Rural Municipality of Rosthern No. 403", `sameAs` https://rmofrosthern.ca/) + BreadcrumbList + FAQPage matching the visible FAQ. One WebPage node only.
- Possible local-interest line for a later revision (not in the copy yet): Seager Wheeler's Maple Grove Farm National Historic Site sits about 6.5 km east of Rosthern (https://historicplaces.ca/en/rep-reg/place-lieu.aspx?id=12136). Only add it if Grant wants local colour.

### Internal links on this page
| Anchor text | Target |
|---|---|
| See Rosthern Listings | `#listings` |
| What's My Land Worth? / free, no-pressure evaluation | https://mysaskfarm.com/sell/ |
| How Much Is an Acre of Farmland Worth in Saskatchewan? | https://mysaskfarm.com/blog/how-much-farmland-acre/ |
| Saskatchewan Farmland Prices: Are Land Values Still Going Up? | https://mysaskfarm.com/blog/saskatchewan-farmland-prices/ |
| The Best Time to Sell Farmland in Saskatchewan | https://mysaskfarm.com/blog/best-time-sell-farmland-saskatchewan/ |
| Contact Grant Ostapowich / Buy or Sell Sask Farmland Today! | https://mysaskfarm.com/contact/ |
| RM of Corman Park No. 344 (Browse block) | https://mysaskfarm.com/rm-of-corman-park/ |

**Links in (add when this page goes live; minor edits, no Grant approval needed):**
- `/rm-of-corman-park/` Browse block: add a Rosthern No. 403 card/link to `/rm-of-rosthern/`.
- The sitewide "Browse Other RMs" list: change the Rosthern No. 403 entry to link to `/rm-of-rosthern/` (it currently points to a listings-search URL with map coordinates).

**Outbound:** rmofrosthern.ca, FCC Farmland Values Report, Sask RM Yields dashboard. No competitor realtors.

### Sources (each fact on the page)
| Fact | Value | Source | Status |
|---|---|---|---|
| Population 2021 / 2016 | 2,473 / 2,300 (+7.5%) | StatCan 2021 Census Profile, CSD 4715031, via the official API: https://api.statcan.gc.ca/census-recensement/profile/sdmx/rest/data/STC_CP,DF_CSD/A5.2021A00054715031.1.1+2+3+7.1?format=csv . Human link to cite: https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&DGUIDlist=2021A00054715031 | Confirmed 2026-11-24 |
| Land area | 944.28 km² | Same StatCan API. The RM's OCP says its planning area is about 564 km²; StatCan's figure is used | Confirmed |
| Census division | No. 15 | StatCan code 4715031 | Confirmed |
| "35 kms north of the City of Saskatoon"; North Sask. River NW, South Sask. River east; Hwy 11 and 312; Valley Regional Park | | https://rmofrosthern.ca/map.html | Confirmed |
| RM office | 1001 6th Street, Rosthern | https://rmofrosthern.ca/ | Confirmed |
| Neighbours (Corman Park S, Laird W, Duck Lake N, river E); towns Rosthern and Hague; hamlets Neuanlage, Gruenthal, Blumenthal, Carlton; Class 2 and 3 "prime" land | | RM of Rosthern Official Community Plan (Oct 2021): https://www.rmofrosthern.ca/mrws/filedriver/RM_Rosthern_Official_Community_Plan_4.2008_-_Oct_2021.pdf | Confirmed |
| Soil zone | | Not found. Check AAFC "Soils of the Saskatoon Map Area (73B)": https://sis.agr.gc.ca/cansis/publications/surveys/sk/sks4/index.html | `[VERIFY]` |
| Crop yields 2016 to 2025 | table above | Sask RM Yields CSV (`/export/rm-yields-data/4950.csv`), RM 403, computed 2026-11-24 (method reproduces live Corman Park figures exactly) | Confirmed |
| Provincial FCC % changes; West Central $3,700/ac, North regions +12.1% | | FCC 2025 Farmland Values Report (also on the live how-much-farmland-acre blog) | Confirmed (as published) |
| SAMA assessment explainer | | Word for word from the approved Corman Park page | Approved copy |

### Open `[VERIFY]` items
1. Soil zone (the Class 2 and 3 land fact is sourced; the zone name isn't).
2. FCC region for RM 403 (optional sentence; matters most here because Rosthern is near a region boundary).
3. Fish Creek No. 402 as the neighbour across the South Saskatchewan River (not used in copy; check before linking in future).

### PAA / question research
- Semrush `phrase_questions` unavailable (API units at zero, 2026-11-24).
- Google.ca SERP "rm of rosthern" (2026-11-24) showed no People Also Ask box. Google rate-limited further checks; not bypassed.
- FAQ uses the template PAA set (rm-page-template-research.md s3.2: "Is there any land for sale in [RM]?", "price of an acre"), Grant's top FAQs (CLIENT.md s8), and questions inferred from search results ("What RM is Rosthern in?", "Is Hague in the RM of Rosthern?").
- The SERP for "farmland for sale rm of rosthern" is all listing portals, other realtors and an acreage page (one portal title showed 4 land listings in RM 403 on 2026-11-24). Low supply; we don't quote counts on the page.

### Cannibalization check (2026-11-24)
- No `/rm-of-rosthern/` page or draft exists (wp-mysaskfarm page list, status any). No post mentions Rosthern except the sitewide RM list.
- No overlap with Corman Park: Rosthern copy says "north of Saskatoon" and doesn't use "land for sale near Saskatoon".

### Rules check
- Farmland only (acreage keyword excluded, no residential angle), no price or ranking guarantees, no "best" claims, every figure sourced, free evaluation kept separate from paid appraisals, no competitor links, Century 21 Fusion named as the brokerage, no em dashes.

## Review log

### Pass 1 (2026-11-24): independent fact-check + standards review, applied in v2
- Client file now holds only page URL, title, meta, keywords, intent and the page copy. Everything internal moved here (memory/client-facing-blog-drafts.md).
- Cut shared boilerplate: per-RM intro (40-60 words), listings blurb, price section, Buying/Selling copy and FAQs. Dropped the SAMA FAQ (duplicated the H3), the "how much is it worth" and "crop yields" FAQs (repeated H2s) and the "best time" FAQ (moved to an inline link in the Selling H3). Added an RM-office contact FAQ and Grant's top FAQ ("Are farmland prices still going up?").
- Yields shown as bullets to match the live Corman Park page (and the portrait, no-table docx standard for new pages).
- Soil zone removed from the page until sourced (it would have shown an empty field).
- Added `/listings/` link, census division, neighbour links in the Browse block. "FAQs About the RM of …" (added "the").
- **Flax removed.** RM 403 flax 2018 = 110 bu/ac in the provincial CSV, an obvious data error. With it the 10-year "average" was 39.0; without it 28.9. Dropped the row and flax from the crop list.
- "starts about 35 km north" changed to "about 35 km north" (RM's own wording). Added population growth (+7.5%, the other two RMs fell), census division 15, a land-quality FAQ, river-land price factor. Comparison now names the three RMs instead of "RMs closer to Saskatoon".
- Meta now ends with a CTA. 2025 canola (50.5) is the highest of 2016-2025 (next 49.5 in 2018). Spring wheat's best year was 2020 (63.7), so no "best wheat" claim.
- Open: OCP says ~564 km² planning area vs StatCan 944.28 km². StatCan used; confirm with the RM office if anyone asks.

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
- v3 specifics: **lentils removed.** RM 403 lentils 2019 = 324 lb/ac in the provincial CSV while neighbouring RMs reported 1,446-2,185 and Rosthern's own peas had their best year; same kind of entry error as flax 2018. With it the average was 1,750, without it 1,909. Rather than publish an adjusted figure, the row is out. Outlier scan of all six crops for RMs 343, 345 and 403 (each year vs. the provincial RM median) found no other errors; the other flags were real 2021 drought lows.
- "Most of its 944 km² is Class 2 and 3" fixed: the Class 2 and 3 claim comes from the OCP (planning area ~564 km²), so the copy now attributes it to the OCP and keeps 944.28 km² (StatCan) in the at-a-glance list only.
- FCC H3 now notes the two northern regions led 2025 at 12.1% (regional fact, no claim about which region RM 403 is in).
- **No open `[VERIFY]` tags in the copy.** Still open in notes only: soil zone; FCC region.

## Google Doc (uploaded 2026-11-24)

- [MySaskFarm | New RM Page: RM of Rosthern No. 403 (Draft for Review)](https://docs.google.com/document/d/1vEtMWjNLtk0OUg0pGPYWWAvw2frs7I_1Z02HJaWFy0s/edit), in Drive > Mysaskfarm > SEO & AEO 2026, next to the Corman Park template doc. The folder is readable by anyone with the link (inherited), so do not paste internal notes into it.
- The Google Doc does not sync with the `.md`/`.docx`. If you edit one, update the other.
