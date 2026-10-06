# MySaskFarm.com: keywords

> Updated 2026-10-07. DRAFT for Francis's review.
> Sources: Drive "MySaskFarm Master Keyword Research 2026" (`1GNRXa9jvbJOWZ3MTPBJy6ficT4UbnI8Z4DZbQOfhU30`, FINAL LIST tab, 244 rows, last edited 2026-09-10; full CSV read); "MySaskFarm.com keywords for approval | 2026" (`1qr8epymVB4CgT3du4W3vfoqPBWHI7NZhTeBbqtoAtm8`, 73 keywords, 2026-08-17); "MySaskFarm-Keyword-Tracker" (`1cxQz5KFeRoztOJEq9ix8__JRVu5lbWW_m8P0Fhgm2_A`, Semrush CA volumes Sep 2026, ranks 2026-09-30; sample rows read); 90-Day Roadmap (`10wV0T5_r-SbxSRQ1GJv0Cq2qqpIfUK1eWtzKLg2k7rA`, 2026-07-23); Client Overview (2026-07-10); Semrush domain overview CA (2026-10-07); GSC `https://mysaskfarm.com/` (2026-07-09 to 2026-10-07); Slack #mysaskfarm; [CLIENT.md](CLIENT.md).
> Reusable: section 4 (keyword rules) is the checklist to run any new tracked or content keyword against before it goes live.
> **Volume caveat:** the master sheet's notes mix Semrush CA, "SK" estimates and pre-tool guesses. Many different keywords carry an identical "SK: 1000/mo", which looks like a parent-topic figure rather than per-keyword volume. Treat every volume here as **directional**. The Keyword Tracker's "Semrush Vol (CA, Sep-26)" column is the most reliable source.

## 1. Tracked keywords (Semrush)

**Source:** Semrush project **30622784**. Checked 2026-10-07.

- **No Position Tracking campaign is visible through the API.** The `campaigns` report returns `targets: null`; a lookup with campaign ID `30622784` returns "campaign not found". Either the campaign was never created, or the API can't see it. **Check the Semrush UI**, and if it's missing, load the 73 "Track Now" keywords below once Grant signs off.
- A keyword-level organic pull wasn't possible (Semrush API units balance hit zero on 2026-10-07).

**Domain snapshot, Semrush CA (2026-10-07)**

| Metric | Value | Baseline 2026-07-23 |
|---|---|---|
| Organic keywords | 30 | 32 |
| Top 3 | 0 | 0 |
| Positions 4–10 | 2 | — |
| Positions 11–20 | 10 | — |
| Est. organic traffic/mo | 3 | ~6 |
| Keywords with AI Overview | 12 | — |
| Keywords with People Also Ask | 17 | 15 |

**Tracker rank check, 2026-09-30** (Keyword Tracker, Semrush CA): every sampled core and Wave 1 RM keyword is "Not in top 100". Includes "saskatchewan farmland prices" (40/mo, KD 0) before the blog went live.

**GSC proxy for tracking (90 days to 2026-10-07)**: the only queries with meaningful impressions:

| Query | Impressions | Avg position | Page | In approved list? |
|---|---|---|---|---|
| corman park sk | 145 | 9.6 | /rm-of-corman-park/ | No (navigational) |
| corman park, sk | 57 | 8.8 | /rm-of-corman-park/ | No |
| corman park rm | 40 | 8.0 | /rm-of-corman-park/ | No |
| rm of kindersley | 33 | 17.5 | /rm-of-kindersley/ | **Yes** |
| corman park saskatchewan | 32 | 11.3 | /rm-of-corman-park/ | No |
| rm of corman park | 27 | 12.8 | /rm-of-corman-park/ | No |
| farm mortgage calculator | 23 | 9.7 | /mortgage-calculator/ | No |
| rm of aberdeen | 14 | 10.6 | /rm-of-aberdeen/ | No |
| farmland for sale rm of tisdale | 12 | 17.2 | /rm-of-tisdale/ | **Yes** |
| sask farms for sale | 8 | 44.5 | / | **Yes** |
| sask farmland | 6 | 34.3 | / | **Yes** |
| farmland saskatchewan | 4 | 48.0 | / | **Yes** |
| sell my farm | 1 | 45.0 | /sell/ | **Yes** |

- "my farm" (238 impressions, pos 49) is brand-name noise. Don't target it.
- Plain RM-name queries ("rm of corman park", "corman park sk") already reach page 1. Add RM-name-only variants for Wave 1 to tracking (section 5).

## 2. Priority targets by page

**Source:** Master Keyword Research 2026, FINAL LIST (Track Now rows), cross-checked with the 90-Day Roadmap and the live site (2026-10-07). Volumes: (T) = Keyword Tracker Semrush CA Sep 2026; otherwise the master sheet's note.

| Page URL | Status (live, 2026-10-07) | Primary keyword | Secondary keywords | Intent | Notes |
|---|---|---|---|---|---|
| / (homepage) | Live; title/H1 already "Farmland for Sale in Saskatchewan" | farmland for sale saskatchewan | farmland for sale (720 CA), farmland for sale in saskatchewan, farmland saskatchewan (390), farms for sale saskatchewan (1,000 CA), sask farmland (390), sask farmland for sale | Transactional | Hammond and Sheppard own the head terms; long game |
| /listings/ | Live; thin (~130 words outside the feed) | farm land for sale in saskatchewan | farm land for sale saskatchewan (880 CA), saskatchewan farm for sale (~2,400 CA), sask farm for sale, farm for sale saskatchewan (210 CA), farms for sale near me (1,600 CA), farmland for sale near me (170), farmland near me (210), saskatchewan farmland (260), sk farmland for sale (140), buying farmland saskatchewan, cropland / pasture (50) / irrigated land for sale saskatchewan, ranch(es) for sale saskatchewan (90), farm ground for sale (70) | Transactional | Hammond's #1 page type. Add original intro copy above the feed. Land-type terms may move to a buyer pillar (Roadmap Month 3) |
| /sell/ | Live; title "Sell Farmland in Saskatchewan \| Free Evaluation" | sell farmland saskatchewan | selling farmland in saskatchewan (30 CA), how to sell farmland (10), sell my farm, sell land saskatchewan, list farmland for sale, farmland listing saskatchewan | Transactional (seller) | **Highest business value.** Sheet says "needs full SEO rewrite"; *confirm whether done* |
| /about/ | **Doesn't exist** | farmland realtor saskatchewan | farm realtor saskatchewan, land realtor saskatchewan, farmland agent saskatchewan, farmland realtor saskatoon / regina, farm realtor saskatoon / prince albert / north battleford, good farmland realtor saskatchewan; best / top farm(land) realtor saskatchewan **(track only)** | Commercial (hire) | Needs About Us questionnaire answers (sent 2026-08-18). Add RealEstateAgent/Person schema |
| /farmland-appraisal-saskatchewan/ | **Doesn't exist** | farmland appraisal saskatchewan | farm appraisal saskatchewan, land appraisal saskatchewan, farm land appraisal, how much is my farmland worth | Commercial | Confirmed service (appraisals ~2% of revenue, target 5%). 0 CA volume; warm-lead play |
| /rm-of-corman-park/ | Live; best GSC page (985 impressions, pos 10.4) | farmland for sale rm of corman park | rm of corman park, corman park sk, rm 344, land for sale saskatoon (390 CA, KD 12), saskatoon land for sale (390) | Transactional / local | **Flag:** "land for sale saskatoon" SERPs likely include urban/residential lots. Vet before use |
| /rm-of-aberdeen/ | Live | farmland for sale rm of aberdeen | rm of aberdeen, rm 373 | Transactional / local | Wave 1. Template ~85–95% duplicated (tracker) |
| /rm-of-kindersley/ | Live | farmland for sale rm of kindersley | rm of kindersley | Transactional / local | South of Hwy 7, west-central; outside the priority RM list but already gets impressions |
| /rm-of-tisdale/, /rm-of-biggar/, /rm-of-arlington/ | Live | farmland for sale rm of [name] | name + number forms | Transactional / local | Tisdale and Arlington aren't on Grant's priority list; keep since live |
| /rm-of-antler/, /rm-of-dundurn/ | *Confirm live* (not in sitemap 2026-10-07) | farmland for sale rm of [name] | | Transactional / local | In the Track Now list. Antler (RM 61) is far south-east, outside the priority zone |
| /saskatchewan-farmland-prices/ (published ~2026-10) | Live | saskatchewan farmland prices (40 T, KD 0) | saskatchewan land prices (110), sask land prices, land prices in saskatchewan, farmland prices in saskatchewan (70), price of land in saskatchewan, farmland value saskatchewan, are saskatchewan land prices going up, saskatchewan land prices by rm map (110–170) | Informational / commercial investigation | Sheet planned `/blog/saskatchewan-farmland-prices-guide/`; **live URL is the root slug**. Grant FAQ #1 |
| /best-time-sell-farmland-saskatchewan/ (published 2026-10-01) | Live | best time to sell farmland saskatchewan | when is the best time to sell farmland in saskatchewan, when to sell farmland | Informational (seller) | Sheet planned `/blog/best-time-to-sell-farmland-saskatchewan/`; live slug differs |

**Planned blog targets (FINAL LIST "Blog" rows, 71 keywords).** Highest fit for Grant's FAQs and the Nov–Mar season first:

| Planned URL (sheet) | Primary keyword | Vol | Fit / flags |
|---|---|---|---|
| /blog/farmland-prices-by-rm-saskatchewan/ | how much is farmland worth in my rm | niche | **Grant FAQ #2 and #4**; Roadmap Month 3 flagship AEO piece (the Hammond gap) |
| /blog/capital-gains-farmland-saskatchewan/ | how to avoid capital gains on inherited farmland canada | 30 SK / 210 (Roadmap) | Roadmap Month 2 "AEO sleeper". Needs a not-tax-advice line |
| /blog/qualified-farm-property-capital-gains-exempt | qualified farm property | 110 CA | Pair with the capital-gains post |
| /blog/making-an-offer-on-farmland-saskatchewan/ | making an offer on farmland | niche | **Grant FAQ #5** |
| /blog/farm-succession-planning-saskatchewan/ | farm succession planning | 90 CA | Retiring-seller audience |
| /blog/what-is-a-quarter-section-saskatchewan/ | acres in a quarter section | 480 CA | Easy AEO definition win |
| /blog/how-much-is-an-acre-of-farmland-worth-saskat… | how much is an acre of land | 390 CA | Overlaps the farmland-prices post; **cannibalization check** |
| /blog/hunting-land-for-sale-saskatchewan/ | hunting land for sale saskatchewan | 70, KD 5 | Roadmap's best low-competition buyer bet |
| /blog/land-for-sale-in-saskatchewan/ | land for sale saskatchewan | 1,000 CA | **Flag:** mixed residential/acreage SERP; sheet says vet SERP |
| /blog/farmland-lease-vs-sale-saskatchewan/ | farm for rent near me | 320 CA | **Flag:** Grant sells land; leasing/rentals aren't a listed service. *Confirm before writing* |
| /blog/hobby-farm-vs-farmland-saskatchewan/ | small hobby farms for sale saskatchewan | 40 | **Flag:** hobby farms usually include a house (acreage bleed). *Confirm with Grant* |
| /blog/dairy-farms-for-sale-saskatchewan/ | dairy farm for sale saskatchewan | 70 CA | Fits farmland, but dairy sales hinge on quota; *confirm Grant handles them* |
| /blog/what-is-farmland/ | farmland / farm land | 1,300 / 590 CA, KD 41 / 35 | Broad, low intent; low priority |
| /blog/types-of-farmland-for-sale-saskatchewan/ | ranch land, canadian farmland, buy farmland in canada | 5,400 / 720 / 480 CA | National terms; Saskatchewan angle only |

Note: the blog plan uses a `/blog/` URL prefix, but the two published posts sit at the root (`/saskatchewan-farmland-prices/`). **Pick one pattern and update the sheet.**

**Track Future (100 rows):** mostly Wave 1–2 RM pages (`/rm-of-bayne/`, `/rm-of-fish-creek/`, `/rm-of-grant/`, etc., name + number forms) and a planned `/farmland-near-saskatoon/` hub (farmland near saskatoon / prince albert / north battleford / yorkton / swift current / moose jaw; land for sale near regina).

## 3. PPC keywords

- **No PPC in scope** (90-Day Roadmap, 2026-07-23). No Google Ads account or keyword lists found.
- If PPC is pitched later, the negatives in section 4 apply as a starting negative list. Budget as a range with assumptions, inside Grant's ~$2,000/month total ceiling.

## 4. Keyword rules

Run every new tracked or content keyword against this list.

| Rule | Status | Date | Source |
|---|---|---|---|
| **Farmland only.** One service category (farmland), one area (Saskatchewan) | Active | 2026-07-10 | Client Overview |
| **Never target:** residential real estate, homes for sale, houses for sale saskatoon, condos, commercial property / real estate, urban real estate | Excluded | 2026-07-10 | Client Overview; Negative Keywords tab |
| **Acreage / acreages for sale** (all variants) | Excluded / WATCH. Real demand (Sheppard ranks #2 for "acreages for sale saskatchewan", ~1,300/mo), but listings usually include a house. Future scope conversation only | 2026-07-23 | Roadmap; Negative Keywords tab |
| "land for sale" with no geo | WATCH: too broad, mixed residential intent | 2026-07 | Negative Keywords tab |
| Out-of-province (e.g. "mb farms for sale") and urban lots ("lots for sale regina sk") | Excluded | 2026-07 (Semrush audit) | Negative Keywords tab |
| City "land for sale" terms (saskatoon, regina, prince albert) | **Vet the SERP first**; often urban/residential lots | 2026-09 | FINAL LIST notes |
| RM keywords: track **both name and number forms** ("rm of corman park", "rm 344"), 4 patterns × 2 forms = 8 per RM | Active | 2026-07 | Keyword Tracker |
| Zero/low-volume RM terms: **keep** for local, voice and AEO; verify with GSC impressions | Active | 2026-07 | Keyword Tracker READ ME |
| Wave order: Wave 1 = Saskatoon/Warman ring (12 RMs); north of Hwy 1 before south | Active | 2026-07/09 | Tracker; Client Overview |
| "best / top / good farmland realtor" | **Track only.** No "best" or "#1" claims in copy. Unverifiable superlatives are also risky under real-estate advertising rules | 2026-10-07 | This file; CLIENT.md section 2 |
| Appraisal keywords: allowed (confirmed service) | Active | 2026-07-10 | Client Overview |
| Tax / capital-gains / investment keywords: allowed for blogs with a not-tax/financial-advice line | Active | 2026-07-23 | Roadmap |
| Grant signs off the final keyword list before tracking/content | **Pending** (chased 2026-08-27) | 2026-07-10 | Client Overview; Slack |
| Minor keyword rewording of existing copy: no client approval needed | Active | 2026-07-10 | Client Overview |

**Flags in the current lists (services not offered or off-scope)**
- **farm acreage for sale** (approval list row 72): acreage is excluded. **Remove.**
- **land for sale saskatoon / saskatoon land for sale** (approval list, mapped to Corman Park): urban-lot risk. Vet the SERP or move to Track Future.
- **crop land for sale, agriculture land for sale** (approval list): no geo; low intent match. OK to track, but expect national/US SERPs.
- **farmland for sale rm of antler**: RM 61, far south-east, outside the priority zone. Fine to keep, low priority.
- **farm for rent near me / farmland for lease / farmland for rent saskatchewan** (blog rows): leasing isn't a listed service. *Confirm.*
- **small hobby farms for sale saskatchewan** (blog row): acreage bleed. *Confirm.*
- **best / top farm(land) realtor saskatchewan**: track only.

## 5. Opportunities

**Quick wins from GSC (2026-07-09 to 2026-10-07)**
- **Corman Park** already ranks page 1 for RM-name queries (pos 8–11). Rewrite it first as the model RM page and add "rm of corman park" / "corman park sk" / "rm 344" as tracked secondaries.
- **Aberdeen** (pos ~10) and **Kindersley** (pos 13–17) are next.
- **/sell/** averages position 3.5 on its few impressions. A full seller-intent rewrite could lift "sell farmland saskatchewan" fast.
- **/mortgage-calculator/** ranks 9.7 for "farm mortgage calculator" (23 impressions). If the page stays, reframe it as a **farm** mortgage calculator.

**The Hammond gap (Roadmap, 2026-07-23)**
- Hammond ranks #1 for "saskatchewan land prices by rm map" (~110–170/mo). Grant's site is already organised by RM, so RM-level land-value content (blog "How much is farmland worth in my RM?" + data blocks on RM pages) is the flagship AEO play.
- kentbraaten.com publishes a monthly SK farmland market report. A recurring "market update" from Grant could compete for the same AI citations.

**AEO / PAA**
- 17 ranking keywords trigger PAA and 12 trigger AI Overviews (Semrush CA, 2026-10-07).
- Grant's top-5 FAQs map directly to question content: land prices going up (done), what's my RM worth, land for sale in my area, what did the neighbour's parcel sell for, what do we need to offer.
- Published farmland-prices FAQ already covers: average price per acre, will prices drop, NE vs SW values, SAMA assessment vs market value, is farmland a good investment.
- **No fresh PAA pull was run this session** (Semrush units ran out). Per the team PAA standard (`memory/paa-research-standard.md`), pull question data before each new blog.

**Gap keywords worth adding to tracking**
- RM-name-only and RM-number variants for Wave 1 (GSC shows these get impressions).
- "farm mortgage calculator" (if the page stays).
- "saskatchewan land prices by rm map" and "how much is farmland worth in my rm" once the RM-value post is live.
- "qualified farm property", "acres in a quarter section" (informational AEO wins).

## 6. Gaps

- **Semrush Position Tracking:** no campaign visible via API in project 30622784. Confirm in the UI.
- **Semrush keyword-level data:** `resource_organic` failed (API units balance zero, 2026-10-07). No current per-keyword positions; the latest are the tracker's 2026-09-30 column (sample rows only read).
- **Keyword approval:** no record of Grant's sign-off on the 73-keyword list.
- **Volume reliability:** master-sheet volume notes mix sources (see header caveat). Re-pull Semrush CA volumes for the final list.
- **GSC:** only the URL-prefix property is accessible; `sc-domain:mysaskfarm.com` = 403. Data starts ~July 2026.
- **"Initial Keyword Research" sheet** (`1DEPiwS_eVywyyxogiFWqmcN3ccVQubw6BoTRXbQQPaE`, 2026-07-29) and the "Search Atlas" tabs of the master sheet were not read in full.
- **RM page inventory:** only 8 `/rm-of-*/` pages in the sitemap vs "~400" in the brief, so Track Now RM targets for Antler and Dundurn may point at pages that don't exist yet.
