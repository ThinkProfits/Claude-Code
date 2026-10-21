# MySaskFarm.com: RM page template research and blueprint

> **Date:** 2026-10-22. **Author:** Francis (research with Claude). **Status:** DRAFT for Andrew's review. Nothing has gone to Grant yet.
> **Why:** Scrum 2026-10-21. We agreed to build one RM page template, get Grant's approval on it, then copy the format to the other RMs (Andrew: "they should definitely just follow a template").
> **Sources:** live site (2026-10-22), GSC URL-prefix property (2026-07-01 to 2026-10-20), Google Ads Keyword Planner (CA, Oct 2025 to Sep 2026), Google.ca SERPs (2026-10-22), Google Search Central docs, and the third-party studies cited inline.
> **Not available:** Semrush. The API has no units left (2026-10-22), so there's no KD or SERP-feature data. Re-pull it once units are topped up.
> **Reusable:** sections 4–7 work as a template for location/area pages for any client that has a listing feed.

---

## 1. TL;DR

1. **Fix the metadata first.** Five of the seven RM pages show another RM's title tag and meta description. The Corman Park page, our best performer, is titled "RM of Dundurn No. 314". This is a minor fix and can go live without Grant's approval.
2. **Most RM searches are people looking for the municipality itself.** "rm of corman park" / "corman park sk" gets about 3,600 searches a month, and the RM's own website holds the top spot. Searches like "farmland for sale rm of X" barely register. The template has to work for both groups. The bigger group, people searching the RM name, includes the landowners who become Grant's sellers.
3. **The page has to be a farmland guide to the RM, not a listings page with a paragraph on top.** Our current pages fit the pattern Google's doorway policy describes: the same template with the name swapped and about 70 words of Wikipedia-style text. Every page needs its own data: crop yields, land values, soil, and the towns and roads in the RM. It also needs a short local note from Grant.
4. **Grant's knowledge is what sets us apart.** realtor.ca and Kent Braaten both have RM listing pages. Neither has a farmer who has worked that land writing about it. A five-question local-knowledge sheet per RM gets us that content.
5. **Roll out in stages.** Build Corman Park as the model page and get Grant's approval. Then do Wave 1 in blocks, and only publish an RM page once it has its own data.

---

## 2. What's on the live RM pages (2026-10-22)

### 2.1 Metadata is attached to the wrong pages

| URL | H1 (correct) | Title tag now shows | Meta description now describes |
|---|---|---|---|
| /rm-of-corman-park/ | Corman Park | **RM of Dundurn No. 314** | **Dundurn** |
| /rm-of-dundurn/ | RM of Dundurn | **RM of Kindersley No. 290** | **Kindersley** |
| /rm-of-kindersley/ | RM of Kindersley | **RM of Tisdale No. 427** | **Tisdale** |
| /rm-of-biggar/ | RM of Biggar | **RM of Corman Park No. 344** | **Corman Park** |
| /rm-of-arlington/ | RM of Arlington | **RM of Biggar No. 347** | **Biggar** |
| /rm-of-aberdeen/ | RM of Aberdeen | Aberdeen (correct) | Aberdeen (correct) |
| /rm-of-tisdale/ | RM of Tisdale | Tisdale (correct) | Tisdale (correct) |
| /rm-of-antler/ | RM of Antler | Antler (correct) | Antler (correct) |

- **The pattern:** the wrong titles follow a chain from one page to the next. That points to a bulk paste into AIOSEO that went one row out of step.
- **Schema is affected too.** AIOSEO's WebPage schema on Corman Park is named "RM of Dundurn". The page also carries a second, hand-built WebPage block with a correct AdministrativeArea for Corman Park. The two blocks share the same `@id` but give different names.
- **Fix:**
  - Correct the title and meta description in AIOSEO for the five pages above.
  - Remove the duplicate WebPage node from the hand-built schema, or turn off AIOSEO's version for these pages. Only one should stay.
  - This is a minor correction, so Grant doesn't need to approve it (Client Overview: "Keyword-level word changes and SEO rewording of existing content do NOT require client approval"). Tell Andrew once it's done.

### 2.2 Content

- **Original text:** about 65–110 words per page, all in one paragraph. It reads like Wikipedia: population, density, the towns in the RM, a landmark.
  - The Corman Park population figure (8,568, density 4.5/km²) matches older census figures. Check it against the 2021 Census Profile before reusing it.
  - The Tisdale page has no paragraph at all.
- **Listing feed:**
  - **Correction (checked 2026-10-22):** listings are not in the raw HTML. BenchMetrics' JavaScript (`client-includes.benchmetrics.app`, `bnm_featured_listings.js`) injects them in the browser, with photos served from CREA's DDF CDN (`ddfcdn.realtor.ca`). Google can usually render JS, but a server-rendered feed would be safer. See Andrew's feed workstream.
  - **Bad:** the feed shows "0 BEDS | 0 BATHS | UNKNOWN SQFT" on land listings, includes acreages (out of scope), and shows one listing twice ("Johnson Land").
- **Rest of the page:** a "Browse By RMs" block that links six RMs, plus a contact form. No FAQ, no data, no land values, no map, no seller section beyond a single link, and nothing from Grant.
- **Internal links:**
  - The Aberdeen link points to `/RM-of-aberdeen` (uppercase, no trailing slash). That relies on a redirect.
  - "Browse other RMs" goes to listing searches with map coordinates in the URL, not to RM pages.
  - There's no RM hub page.

### 2.3 How the pages perform (GSC, 2026-07-01 to 2026-10-20)

- **Clicks:** zero on any RM page.
- **Corman Park** gets almost all the impressions. Its queries are about the place, not about buying land:
  - "corman park sk": 154 impressions, position 9.9
  - "corman park, sk": 64 impressions, position 9.3
  - "corman park rm": 40 impressions, position 8.0
  - "rural municipality of corman park": 16 impressions, position 8.8
  - "where is corman park sk": 10 impressions, position 11.6
  - map variants: about 16 impressions combined, positions 25–40
- **Buyer searches are scattered:**
  - "farmland for sale rm of tisdale": 21 impressions, position 14.6
  - "farmland for sale rm of corman park": 2 impressions, position 30
  - "farmland for sale rm of kindersley": 2 impressions, position 15
- **Zero CTR at about position 10 is what you'd expect** when the title tag names the wrong RM.

---

## 3. Search demand and intent

### 3.1 Volumes (Google Ads Keyword Planner, Canada, 12-month average)

| Keyword | Avg/mo | Notes |
|---|---|---|
| rm of corman park / corman park sk | 3,600 | Planner merges close variants into one figure. It's a single bucket, not two to add together. Peaks in Apr–May (5,400). |
| rm of corman park map | 390 | Clear demand for a map |
| land for sale corman park | 70 | The real commercial term. Peaks in March. |
| rm 344 | 10 | Low, but GSC shows it at position 7 |
| farmland for sale rm of corman park | 0 (no data) | GSC shows a few impressions. Too small for Planner. |
| rm map saskatchewan | 880 | Province-wide. A candidate for an RM hub page. |
| land for sale near saskatoon | 70 | Mixed intent (urban lots). Check the SERP before targeting it. |
| saskatchewan land prices by rm | 10 | Small, but exactly what the RM value blog is about |

**RM-name searches for other RMs (rm of [name]):**

| RM | Avg/mo | RM | Avg/mo |
|---|---|---|---|
| Kindersley | 590 | Laird | 170 |
| Dundurn | 390 | Hoodoo | 170 |
| Vanscoy | 390 | Biggar | 90 |
| Aberdeen | 320 | Bayne | 70 |
| Blucher | 320 | Grant | 70 |
| Rosthern | 260 | Tisdale | 50 |
| Fish Creek | 210 | Colonsay | 50 |

### 3.2 What the SERPs show (Google.ca, 2026-10-22)

**"rm of corman park"**
- Navigational. Results 1–5 are rmcormanpark.ca and its LinkedIn page. Then come CBC news, a People Also Ask box ("How many people live in the Rural Municipality of Corman Park?", "What is a rural municipality?"), SREDA and Reddit.
- People search the RM name for council business, maps, offices, taxes and news.
- We won't outrank the RM's own site, and we shouldn't try. A solid page-1 spot, with a title that promises something different ("farmland, land values and listings"), can still win the landowner-minded clicks.

**"farmland for sale rm of corman park"**
- realtor.ca holds positions 1 and 3. A competing farmland realtor's RM page is at 2.
- An AI Overview quotes listing price ranges and zoning (AG/DAG1) and cites realtor.ca plus six other sources.
- People Also Ask: "Is there any land for sale in Corman Park?", "What is the current price of an acre of farmland in Saskatchewan?", "How much is 1 acre of land in Saskatchewan?"
- **mysaskfarm.com isn't on page 1.**

**What this means:**
- The money term needs listings plus price-per-acre context.
- To be cited in the AI Overview, we need short, factual answers on price ranges, zoning and what's for sale.
- The PAA questions become the template's FAQ.

### 3.3 The strategic read

The RM-name crowd (thousands a month for Saskatoon-ring RMs) is mostly ratepayers and landowners: exactly the 55–65+ landholders Grant wants as sellers. They aren't searching "sell my farm" yet. A page that gives them what they came for (where the RM is, a map, the towns, what land is worth there), then offers "Thinking about selling? Here's what land in this RM is going for", turns navigational traffic into seller leads. Buyers get the listings and the same land-value context.

**Targeting rule per page:**
- **Primary keyword:** "farmland for sale RM of [name]" (commercial intent, the page's purpose).
- **Secondary keywords:** "rm of [name]", "[name] sk", "rm [number]", "land for sale [name]", "rm of [name] map".
- The title and H1 carry both the RM name and "farmland".

---

## 4. Guardrails: what Google says about pages like these

| Guidance | What it says | What it means for RM pages |
|---|---|---|
| **Doorway abuse** (Google spam policies, updated 2026-08-28: https://developers.google.com/search/docs/essentials/spam-policies) | Its examples include "pages targeted at specific regions or cities that funnel users to one page" and "substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy." | Our current pages are the same template with a different name, and they send people to the listings search. Each page needs its own substance, and the pages need to sit in a real hierarchy (province → region → RM). |
| **Scaled content abuse** (March 2024 policy: https://developers.google.com/search/blog/2024/03/core-update-spam-policies) | Penalises many pages made mainly to manipulate rankings "without adding value", however they're produced. | Templates and AI help are fine. Pages with no unique value are not. A person reviews every RM page before it goes live. |
| **Helpful content** (updated 2026-10-05: https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Rewards "original information, research, or analysis" and "substantial value when compared to other pages in search results." Warns against "mainly summarizing what others have to say." | Wikipedia-style blurbs are the warning sign. RM yields, land values and Grant's notes are the original value. |
| **AI features** (https://developers.google.com/search/docs/appearance/ai-features, 2025) | "No additional requirements" and "no special schema" are needed for AI Overviews. Structured data must match what's visible on the page. | Do the basics well: crawlable text, internal links, accurate schema. |

**Ranking still matters for AI citations, but less than before.**
- Ahrefs, July 2025: 76.1% of AI Overview citations came from top-10 pages (https://ahrefs.com/blog/ai-overview-citations-top-10/).
- A 2026 re-run on 4 million URLs found only 37.9% from the top 10 (https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/).
- Clear, factual, well-sourced answers can be cited from lower positions.

**Schema isn't a citation lever.** Ahrefs (May 2026) found no lift in AI Overview citations after 1,885 pages added JSON-LD (https://ahrefs.com/blog/schema-ai-citations/). Treat schema as groundwork.

**Google Business Profile matters for local AI answers.** BrightLocal's 2025–26 study of 1,365 locations found GBP is the source AI Overviews and AI Mode cite most for local queries (https://www.brightlocal.com/resources/ai-directory-sources/). That makes the open GBP decision (CLIENT.md §10) part of this project too.

---

## 5. The template: page blueprint

**Target length:** 900–1,400 words of original copy, not counting listings. Shared boilerplate (the seller CTA, Grant's bio box) should be under about 30% of the copy. The rest must be specific to the RM. Google publishes no uniqueness percentage; this is our own internal standard.

**Section key:** **U** = unique per RM, **S** = shared block, **G** = Grant's input needed.

| # | Section | Type | What goes in it | Why |
|---|---|---|---|---|
| 1 | **H1:** Farmland for Sale in the RM of [Name] No. [###] | U | Name and number together | Covers buyer and RM-name searches; number form matches "rm 344" searches |
| 2 | **Answer-first summary** (40–60 words) | U | Where the RM is (distance/direction from the nearest city), main towns, land character (grain/pasture/mixed), current listing count, Grant's link to the area | Gives AI Overviews and featured snippets a quotable answer; matches the AI Overview style seen in the SERP |
| 3 | **Quick facts table** | U | RM number; Census Division; FCC region; soil zone (Brown/Dark Brown/Black/Grey); main crops; area; 2021 population; towns, villages and hamlets; main highways; RM office link | Easy for AI to extract; shows depth; serves the RM-name crowd |
| 4 | **Current listings** | Feed | The existing feed. Ask the developer to hide "0 beds / 0 baths / unknown sqft" on land listings and remove duplicates | Buyers' main task; crawlable HTML is already in place |
| 5 | **What farmland sells for in [RM]** (H2) | U | FCC regional average $/acre and % change, cited with year; listing $/acre range from current listings; SAMA assessed vs market value explained; link to the provincial prices blog | Answers the PAA "price of an acre" question; Grant's FAQ #2 and #4; the Hammond gap |
| 6 | **Land, soil and crops** (H2) | U | Soil zone and what it means; 5–10-year average RM yields for wheat, canola and barley (Ministry RM Yields data); moisture and drainage notes; land mix (crop/pasture/hunting) | Original data no competitor shows |
| 7 | **Grant's take on [RM]** (H2) | **G** | 100–200 words in Grant's voice: what buyers look for here, which roads and corners sell fastest, past deals in the area (no confidential details), what sellers should know | E-E-A-T; the one thing realtor.ca can't copy |
| 8 | **Map** (H2: Map of the RM of [Name]) | U | Embedded map of RM boundaries (Google My Maps or a static image with alt text) plus a link to the RM's official map PDF | 390/mo "rm of corman park map" demand |
| 9 | **Selling land in [RM]?** | S + U | Seller CTA ("free evaluation", kept separate from paid appraisals) with one RM-specific line; link to /sell/ | Turns RM-name traffic into seller leads |
| 10 | **FAQ** (5–7 questions) | U | Taken from PAA and Grant's FAQs: Is there land for sale in [RM]? What does an acre sell for in [RM]? What soil zone is [RM] in? How is farmland assessed in [RM] (SAMA)? Who do I contact at the RM office? How long does farmland take to sell in [RM]? | PAA coverage; quotable answers |
| 11 | **Nearby RMs** | U | Links to the 4–6 bordering RMs that have pages, plus the RM hub | A browsable hierarchy (the doorway-policy safeguard); spreads authority |
| 12 | **About Grant box** | S | Photo, 30 years farming + 17 years selling farmland, phone, "Century 21 Fusion" written out as the brokerage | Entity signal for Grant; regulatory brokerage disclosure (CLIENT.md §2) |

**Hard rules for every page** (from CLIENT.md §8):
- Farmland only. No acreage or residential angle in the copy, even though the feed shows acreages.
- No price guarantees.
- No "best" claims.
- Cite every land-value statistic with its source and year.
- "Free evaluation" is not an appraisal.
- No links to competing realtors.

---

## 6. On-page specs

| Element | Formula | Corman Park example |
|---|---|---|
| URL | Keep the existing `/rm-of-[name]/`. Don't change slugs. | /rm-of-corman-park/ |
| Title (≤60 characters) | Farmland for Sale: RM of [Name] No. [###] \| MySaskFarm | Farmland for Sale: RM of Corman Park No. 344 \| MySaskFarm |
| Meta description (≤155 characters) | Farmland for sale in the RM of [Name] No. [###], [location]. Land values, soil, crop yields and listings from a farmer-turned-realtor. | …around Saskatoon, Warman and Martensville… |
| H1 | Farmland for Sale in the RM of [Name] No. [###] | |
| H2s | Listings · What farmland sells for · Land, soil and crops · Grant's take · Map · Selling land · FAQ · Nearby RMs | |
| Images | One real local photo (Grant's own or licensed). Alt text naming the RM. No equipment on private property without permission. | |
| Internal links in | Homepage, /listings/, RM hub, bordering RMs, farmland-prices blog, future "farmland worth in my RM" blog | |
| Internal links out | /sell/, the prices blog, bordering RMs, the hub | |
| Outbound links | RM's official site, FCC report, Ministry RM Yields, StatCan. Never competitors. | |

**Schema** (one clean JSON-LD graph per page, replacing the duplicate):
- **WebPage** with `about` pointing to the RM.
- **AdministrativeArea** (the RM): `name` "Rural Municipality of [Name] No. [###]", `containedInPlace` Saskatchewan, `sameAs` the RM's official site and Wikipedia/Wikidata.
- **RealEstateAgent** (Grant): `areaServed` this RM, plus Saskatchewan.
- **BreadcrumbList:** Home → RMs → [RM].
- **FAQPage** matching the visible FAQ. Google has shown FAQ rich results only for government and health sites since August 2023 (https://developers.google.com/search/blog/2023/08/howto-faq-changes), so this is for machine-readable Q&A only.
- **Skip ItemList for listings.** It earns no rich result for real estate, and the data changes daily.

---

## 7. Where each RM's unique data comes from

| Data | Source | Licence / note |
|---|---|---|
| Annual crop yields per RM | Sask Ministry of Agriculture RM Yields dashboard: https://dashboard.saskatchewan.ca/agriculture/rm-yields/rm-yields-data (CSV) | **Best free per-RM source.** Read its terms before publishing; some values are suppressed. |
| Regional land value and % change | FCC Farmland Values Report: https://www.fcc-fac.ca/en/knowledge/economics/farmland-values-report | Six SK regions, not RMs. Map each RM to its region and cite "FCC, [year]". |
| Population, dwellings | StatCan 2021 Census Profile (each RM is a census subdivision) | Statistics Canada Open Licence, attribution required |
| Farm counts, tenure, farm types | StatCan Census of Agriculture 2021 (Census Consolidated Subdivision level, not exact RM) | Same licence. Say "census area" when it isn't exactly the RM. |
| Soil zone, CLI class | Gov. of SK soils GIS: https://gis.saskatchewan.ca/arcgis/rest/services/Soils/MapServer/1 ; SKSIS: https://sksis.usask.ca | Gov. of SK Unrestricted Use Data Licence v2.0. **Attribution line required.** |
| RM office, website, map | RM's own site; SK municipal directory | Link out; use for `sameAs` |
| Recent sales $/acre | Comparable Land Sales Database (subscription since 2024-03-27): https://saskatchewan.ca/business/agriculture-natural-resources-and-industry/agribusiness-farmers-and-ranchers/comparable-land-sales-database | **Licence limits use to market value comparison. Don't publish individual sales.** Ask whether aggregated medians are allowed. Grant may already have access. |
| Assessment explainer | SAMA (2025 revaluation, 2023 base date) | Use for the explainer only. No public RM-level table found. |
| Local knowledge | **Grant** (five-question sheet per RM) | Needs his time. Batch requests by wave. |

**Grant's five questions per RM:**
1. What kind of land is typical here, and what do buyers ask about first?
2. Roughly what range per acre have you seen good land trade at in the last two years? A range is fine.
3. What makes land here sell faster or slower (roads, drainage, rocks, distance to elevators)?
4. Any deals or stories from this RM you're happy to mention (no names)?
5. What should someone thinking of selling here know?

---

## 8. Rollout plan

1. **Now (no approval needed):** fix the shuffled titles, meta descriptions and duplicate schema (section 2.1). Fix the `/RM-of-aberdeen` link.
2. **Model page:** draft the Corman Park rewrite in a Google Doc using section 5. Send Grant's five questions with it. Andrew sends it to Grant (new, substantial content, so Grant approves per the Client Overview and Andrew's 2026-10-21 rule).
3. **Developer asks:** feed tidy-up (hide beds/baths/sqft on land listings, remove duplicates); an RM hub page listing all RMs that have pages, plus the provincial RM map (880/mo "rm map saskatchewan"). Fold in Andrew's feed solution once it's ready.
4. **Wave 1 in blocks of 3–4 per month** (Bronze capacity), in Keyword Tracker order. Priority by demand: Dundurn, Vanscoy, Blucher, Aberdeen, Rosthern, Fish Creek, Hoodoo, Laird.
5. **Publishing gate:** an RM page goes live, or gets rewritten, only when sections 2, 3, 5 and 6 contain real RM data and Grant has answered at least questions 1–3. Thin RM pages (Tisdale, which has no copy) wait for their wave or get `noindex` until then. *Confirm with Andrew before noindexing anything live.*
6. **Measure:** GSC per page (impressions, CTR, queries) 4 and 8 weeks after each block; Semrush Position Tracking once the campaign is set up and units are available.

**Expectations:** no ranking or AI-citation guarantees. The GEO paper's "up to 40%" visibility lift (https://arxiv.org/abs/2311.09735) is a lab ceiling. Never quote it as a forecast.

---

## 9. Open questions

- [ ] Andrew: OK to fix the shuffled metadata live now?
- [ ] Andrew: noindex thin RM pages until their wave, or leave them?
- [ ] Grant: does he have a Comparable Land Sales Database subscription, and what can be published from it?
- [ ] Terms of use for the RM Yields dashboard and the FCC report (not yet read).
- [ ] Which FCC region each Wave 1 RM falls in (map it; don't guess).
- [ ] Can the feed plugin hide residential fields and filter out acreages? (Plugin name still unconfirmed.)
- [ ] Re-pull Semrush (KD, SERP features, competitor RM rankings) once API units are topped up.
