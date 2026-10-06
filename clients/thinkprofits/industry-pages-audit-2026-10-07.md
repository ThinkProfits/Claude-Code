# thinkprofits.com: industry page audit and keyword research (v2)

> **Status:** DRAFT v2, 2026-10-07. Prepared by Francis (with Claude) for Andrew and Shawn. **v2 replaces v1** (sent to Lovable earlier today). v1 missed a third set of 20 industry pages and the old WordPress industry URLs, and its keyword research was too thin.
> **Why:** Shawn flagged the garage door and auto repair pages as spam-like. Andrew's rule: quality over quantity, and every page we keep is rewritten by hand.
> **Open question for Andrew:** one hub page for sales, or separate indexable pages? Answered with data in section 6.
>
> **Sources (all pulled 2026-10-07):**
> - Live sitemap (300 URLs) and HTTP checks of every industry URL.
> - Google Search Console `sc-domain:thinkprofits.com`, 6 months (2026-04-07 to 2026-10-06): 17,186 query/page rows, read in full.
> - Google Ads Keyword Planner: 1,774 agency-intent keywords across 32 industries, for Canada, British Columbia and the US (12-month averages to Aug 2026). Plus Keyword Planner "ideas" from 41 seed terms across 14 industries (about 6,500 suggestions in Canada and the same in the US).
> - All 22 case studies on our site, read for industry and real results.
> - Ranking competitor pages and their FAQs (US-located web search; see the limits below).
>
> **Raw data:** `data/industry-research/`
> - `keyword_matrix.csv`: every keyword with CA/BC/US volume, competition and top-of-page bid.
> - `vertical_totals.json`, `keyword_ideas.json`, `ideas_digest.txt`.
> - `gsc_industry_queries_sitewide.json`, `gsc_offsitemap_pages.json`, `local_seo_industry_pages.json`.
>
> **Limits:**
> - Semrush wasn't used (API units at zero).
> - Google and Bing blocked automated searches, so People Also Ask was replaced by the FAQs on the pages that rank (section 8).
> - Keyword Planner rounds low volumes (10, 20, 30…) and groups close variants. "Lawyer seo", "attorney seo" and "seo for lawyers" share one figure.
> - British Columbia figures are floored at 10 per keyword, so they're too noisy to rank industries. They're shown for reference only.

---

## 1. Summary

1. **We have 51 industry pages, not 31.** Each industry can have up to three near-duplicate pages:
   - `/seo-services/local-seo/local-seo-<industry>/`: 20 pages. Indexable, linked from the Local SEO page, **missing from sitemap.xml**.
   - `/aeo-services/<industry>/`: 21 pages.
   - `/ppc-advertising/ppc-for-<industry>/`: 10 pages.

   All three sets are AI-templated. Together they produced **3 clicks in 6 months**. Three thin pages per industry, each competing with the others, is the pattern Shawn spotted.
2. **Several of these industries have no demand from businesses looking for an agency.** "aeo for plumbers", "ai seo for dentists" and every "aeo for <industry>" term show no measurable search volume in Canada or the US. The garage door industry gets about 140 searches a month across all its agency terms in all of Canada; dermatology about 100; towing about 70.
3. **The industries where we have real case studies mostly have no page at all.** We have strong, numbers-backed case studies for:
   - **hotels and hospitality**: Executive Hotels, "$3M increased revenue over 15 months"; Liz Moore; Prestons.
   - **manufacturing and industrial**: Merit Kitchens, "50+ new leads per month"; Euro-Rite; QSD; Can-Four.
   - **ecommerce**: Golf Ball Planet, "315.9% revenue increase"; MVP.
   - **law firms**: Thomas & Associates, "354% organic form fills"; Hoogbruin.
   - **education**: Sprott Shaw; Mujo.

   The AI-generated set skipped most of these and built pages for garage doors, med spas and vets instead, where we have no case study at all.
4. **We already had real industry pages, and the migration threw their equity away.** Old WordPress pages still show up in Google:
   - `/lawyer-seo/`: 2,624 impressions.
   - `/seo-for-home-service-contractors/`: 1,379.
   - `/seo-for-education/`: 1,227.
   - `/seo-hotels-resorts/`: 1,206, at about position 18 for "hotel seo services".
   - `/seo-for-plumbers`: 668.
   - `/dentist-seo-services`: 345.
   - `/seo-for-manufacturing-companies/`: 146.

   All of them 301 to the generic `/seo-services/` page, which doesn't answer those searches. Pointing them at matching new pages is the cheapest win in this audit.
5. **Site-wide technical bug:** `https://www.thinkprofits.com/` returns a **302 (temporary)** to the non-www site instead of a 301. Google still shows the www homepage (23,583 impressions in 6 months). This needs fixing regardless of the industry work.
6. **Recommendation:** collapse 51 pages into **one strong page per industry where we have proof, 9 in total**. Each page covers SEO, AI search and Google Ads for that industry. Everything else becomes a short section on the `/industries/` hub or is dropped. Then redirect every old URL to its closest new page. Details in sections 6 and 7.

---

## 2. What's on the site today

| Set | Count | In sitemap? | 6-month impressions | Clicks | Notes |
|---|---|---|---|---|---|
| `/seo-services/local-seo/local-seo-<industry>/` | 20 | **No** (linked from the `/seo-services/local-seo/` page, 10 of them) | 2,163 | 0 | Strongest of the three: Butler case study on plumbing, about 1,500–2,700 words. Still templated. |
| `/aeo-services/<industry>/` | 21 | Yes | 450 | 2 | One template; the body is mostly consumer questions ("garage door won't close"). |
| `/ppc-advertising/ppc-for-<industry>/` | 10 | Yes | 1,234 | 1 | Landscaping (455) and dentists (413) get the most impressions; positions 36–76. |
| Old WordPress industry URLs | 9+ | No (301 to generic pages) | about 8,200 | 0 | Real history; now wasted on generic redirect targets. |

**Copy problems across the templated sets:**
- **Consumer-facing copy:** AEO pages are mostly homeowner and patient questions.
- **Unsourced statistics:**
  - "'Plumber near me' alone gets 368,000 US searches every month."
  - "converts at almost any offered price."
- **Overclaims:** "your brand is in its [AI] training and retrieval set".
- **Risky tactics in the copy:**
  - "Reddit threads": reads as forum seeding.
  - "Q&A seeding": reads as manipulating Google Business Profile Q&A.
- **US wording on a Canadian site:** "attorney", "bar-association rules". In Canada it's lawyers and the Law Society.
- **Identical blocks on every page:** the same "Related Reading" posts (Lovable canonical QA), unrelated to the industry.

---

## 3. Keyword research: demand by industry

Keyword Planner, agency-intent terms only ("seo for X", "X seo company", "X marketing agency", "google ads for X", "X web design", "aeo for X" and so on, 13–14 patterns per synonym). Totals are deduplicated for grouped close variants. Volumes are average monthly searches.

| Industry | Canada | US | Biggest agency-intent terms (CA / US) | Our proof | We have a page? |
|---|---|---|---|---|---|
| **Law firms** | **4,910** | **34,130** | seo for lawyers/attorneys group 1,000 / 3,600 · law firm seo 480 / 4,400 · legal seo 320 / 1,000 · law firm seo company 320 / 480 · seo for personal injury lawyers 320 / 1,300 · law firm web design 260 / 2,400 · law firm marketing 140 / 1,600 | **Strong**: Thomas & Associates (family law, real numbers), Hoogbruin (personal injury, real numbers) | 3 templated pages + old `/lawyer-seo/` |
| **Dental** | **3,040** | 11,370 | dental marketing 590 / 1,600 · dental seo 480 / 1,300 · seo for dental office 390 / 140 · dental seo services 390 / 1,300 · dental seo agency 260 / 480 · advertising for dentists 210 / 720 · local seo for dentists 170 / 880 · dental google ads 90 / 390 | Medium: Tsawwassen Family Dental (detailed story, **no hard numbers on the page**, confirm metrics) | 3 templated pages + old `/dentist-seo-services` |
| **Ecommerce** | **2,890** | 15,980 | ecommerce seo services/agency/company 390 / 1,000–1,300 · shopify seo 210 / 1,600 · ecommerce web design 260 / 1,600 · ecommerce marketing 110 / 1,000 | **Strong**: Golf Ball Planet (+315.9% revenue), MVP Athletic | Only `/ecommerce-website-design/` (design, not SEO/PPC) |
| Small business (generic) | 2,880 | 23,780 | seo for small businesses 590 / 3,600 · small business seo services 720 / 4,400 | Everything | That's what `/seo-services/` is for. Not an industry page. |
| Real estate | 2,820 | 15,360 | real estate seo / realtor seo 720 / 1,300 · real estate lead generation 320 / 2,900 | **None** | No (not recommended without proof) |
| **B2B / manufacturing / industrial** | 2,230 + 430 | 15,650 + 4,130 | b2b marketing agency 480 / 5,400 · b2b seo agency 390 / 1,000 · b2b lead generation 170 / 1,900 · manufacturing seo 50 / 390 · manufacturing website design 50 / 590 · industrial marketing 30 / 390 | **Strong**: Merit Kitchens (50+ leads/month), Euro-Rite, QSD, Can-Four, CCD Energy, Catapult ERP; live clients Wiseworth, SPIEDR | Old `/seo-for-manufacturing-companies/` only |
| **Contractors / home services (umbrella)** | 1,600 | 8,290 | seo for contractors 260 / 590 · contractor seo 260 / 880 · home builder marketing 210 / 320 · trades marketing 170 / 1,300 · contractor web design 90 / 1,000 · seo for general contractors 70 / 170 · seo for construction companies 50 / 480 | Medium–strong: Ultimate Fence, Anago (both thin pages), live clients Jamie Davis Towing, Clearset, PowerUp Electric, Arbor Green, Drainage Pro | Old `/seo-for-home-service-contractors/` (1,379 impressions) |
| **Hotels & hospitality** | 1,010 | 7,200 | advertising for restaurants 210 / 1,000 · restaurant seo 90 / 390 · marketing for restaurants 90 / 720 · hotel seo 30 / 590 · hospitality marketing agency 30 / 590 · google ads for hotels 40 / 320 | **Strong**: Executive Hotels ($3M revenue), Liz Moore Destination Weddings, Prestons | Old `/seo-hotels-resorts/` (1,206 impressions, position ~18) |
| **HVAC** | 820 | 7,400 | seo for hvac 140 / 320 · hvac seo 110 / 720 · hvac marketing 70 / 480 · hvac web design 70 / 480 · hvac marketing agency 50 / 880 · hvac lead generation 50 / 880 · plumbing and hvac seo 50 / 480 | **Strong**: Lone Star and Butler (plumbing & heating), live Vision, Waywest, ProWest | 3 templated pages |
| **Plumbing** | 810 | 5,990 | plumber web design 170 / 480 · advertising for plumbers 110 / 480 · seo for plumbers 70 / 590 · digital marketing for plumbers 50 / 260 · plumber marketing agency 40 / 720 · local seo for plumbers 40 / 590 · google ads for plumbers 40 / 260 | **Strongest**: John Sadler (4x organic traffic), Lone Star (+730% PPC conversions), Butler (150+ calls/month); live Vision, McMullen | 3 templated pages + old `/seo-for-plumbers` |
| Roofing | 740 | 7,740 | roofer seo 320 / 2,400 · seo for roofing companies 70 / 880 · marketing for roofers 30 / 590 | **None found** | 3 templated pages |
| Accountants | about 300* | 3,780* | cpa marketing 210 / 1,300 (*mostly affiliate "CPA" marketing, not accountants*) · accounting marketing 50 / 390 · marketing for accountants 50 | None | 2 templated pages |
| **Education** | about 300* | about 1,500* | seo for educational institutions (GSC shows 140 impressions to our old page) · higher education marketing 110 / 260 · digital marketing for schools 50 / 480 · higher ed marketing agencies 20 / 320 (*"education marketing" is mostly people looking for marketing courses*) | **Strong**: Sprott Shaw College (32+ page-1 placements), Mujo Learning Systems; live AANMC | Old `/seo-for-education/` (1,227 impressions) |
| Landscaping | 500 | 3,730 | landscaping marketing 70 / 390 · advertising for landscapers 50 / 480 · landscape marketing agency 40 / 260 | Weak: Arbor Green (live client, no case study) | 3 templated pages |
| Electricians | 410 | 2,940 | advertising for electricians 70 / 320 · seo for electricians / electrician seo 70 / 720 · electrician marketing 40 / 320 | Weak: PowerUp Electric (live client, no case study) | 3 templated pages |
| Auto repair | 350 | 2,410 | auto repair marketing 70 / 720 · seo for auto repair shops 20 / 320 | None | 3 templated pages |
| Cleaning | 350 | 2,300 | cleaning advertising 110 / 480 · seo for cleaning companies 10 / 260 | Weak: Anago (101-word case study, no results), Cleaning 4 U (PPC client) | 2 templated pages |
| Moving | 340 | 2,960 | moving company seo / seo for movers 90 / 1,000 | None | 2 templated pages |
| Physiotherapy | 310 | 810 | physio marketing 40 · marketing for physiotherapists 40 | None | 2 templated pages |
| Pest control | 300 | 2,990 | pest control seo 90 / 880 | None | 2 templated pages |
| Chiropractors | 230 | 2,230 | chiropractic marketing 40 / 480 · chiropractic seo 30 / 480 | None | 2 templated pages |
| Med spa | 230 | 2,540 | marketing for med spas 50 / 390 | None | 3 templated pages |
| Restoration | 220 | 910 | seo for restoration companies 20 / 90 | Drainage Pro (*confirm*) | 2 templated pages |
| Veterinarians | 180 | 1,250 | marketing for veterinarians 20 / 260 | None | 2 templated pages |
| Immigration | 150 | 880 | marketing for immigration lawyers 30 / 210 | Magellan Immigration (live PPC client) | None |
| Garage door | 140 | 930 | seo for garage door companies 20 / 140 · garage door advertising 30 / 320 | None | 2 templated pages |
| Dermatology | 100 | 820 | dermatology marketing 20 / 260 | None | 1 templated page |
| Kitchens/cabinets, towing, fencing, drain/septic | 30–70 each | under 260 each | Too small to measure | Merit, Euro-Rite, Jamie Davis, Ultimate Fence, Clearset | None |

**AI-search terms per industry:** every "aeo for <industry>" and "ai seo for <industry>" term returned **0** in both Canada and the US. Demand for AI search exists at the service level ("generative engine optimization" 590/month in Canada, "answer engine optimization" 320, "ai seo agency" 110), which `/aeo-services/` and `/aeo-services/geo/` already target. **Per-industry AEO pages have no search demand behind them.**

**Per-industry Google Ads terms are small:** for example "google ads for dentists" 90, "google ads for plumbers" 40, "law firm ppc" 70. That's too thin to justify separate PPC pages per industry. Each industry page should cover Google Ads as a section instead.

---

## 4. What the ranking pages look like (competitor check)

Searches: "seo for plumbers canada", "hvac seo canada agency", "dental seo company canada", "law firm seo vancouver", "hotel marketing agency vancouver", "manufacturing seo agency canada". These ran through a US-located search tool, so Canadian results may differ; treat this as a picture of the page types that rank, not exact positions.

- **The format that ranks: one dedicated page per industry per agency.**
  - Examples: Pilot SEO `/plumber-seo/`, Seologist `/industries/hvac-seo-company.html`, Volt Studios `/industries/hvac-seo/`, L8P `/seo-for-lawyers/`, 1st On The List `/industry/dental-seo/`.
  - Industry specialists also rank: HVAC SEO Pros, dentistseo.ca, Dental Digital Agency.
  - Nobody ranking runs a separate SEO + AEO + PPC page for the same industry.
- **Length and contents:** about 1,200–2,600 words, testimonials and reviews throughout, FAQ schema, and published pricing or a pricing range (Canada Create publishes "from CAD 1,500/month" for dental SEO).
- **Hospitality and manufacturing** are dominated by specialist agencies and agency directories (Kika, Wallop, Digital Hospitality; Semrush and Clutch agency lists). With Executive Hotels and Merit Kitchens we have proof most generalists can't show.
- **"law firm seo vancouver"** results are full of Vancouver, **WA** agencies. There's an opening for a page that's clearly Vancouver, **BC** and uses Canadian legal terms (Law Society of BC rules, lawyers not attorneys).

Sources: [Pilot SEO plumber SEO](https://pilotseo.ca/plumber-seo/) · [Seologist SEO for plumbers](https://www.seologist.com/knowledge-sharing/seo-for-plumbers/) · [Seologist HVAC](https://www.seologist.com/industries/hvac-seo-company.html) · [Volt Studios HVAC](https://voltstudios.ca/industries/hvac-seo/) · [HVAC SEO Pros](https://hvacseopros.com/) · [dentistseo.ca](https://dentistseo.ca/) · [Canada Create dental SEO](https://canadacreate.com/dental-seo-services-in-toronto/) · [1st On The List dental SEO](https://www.1stonthelist.ca/industry/dental-seo/) · [L8P SEO for lawyers](https://l8p.ca/digital-marketing-services/seo-for-lawyers/) · [Kika hospitality](https://www.kika.ca/industries/hospitality-hotel-marketing-agency/) · [enoptimize manufacturing SEO](https://enoptimize.ca/manufacturing-seo/)

---

## 5. Our own search history for these topics

Across 6 months of GSC, 1,760 query/page rows combine an industry term with an agency term (27,771 impressions, **0 clicks**). Where Google already associates us with an industry:

| Topic | Strongest signal | Where it lands today |
|---|---|---|
| Law firms | "lawyer seo" 337 impressions, "law firm seo" 177, "seo for lawyers" 121; `/lawyer-seo/` 2,624 total | 301 to generic `/seo-services/` |
| Ecommerce | "ecommerce website designers" 1,710; dozens of ecommerce design terms | `/ecommerce-website-design/` (positions 25–60) |
| Hotels | "hotel seo services" 322 at **pos 17**, "seo services for hotels" 146 at 19.5, "hotel seo agency" 133 at 18 | `/seo-hotels-resorts/`, which 301s to generic `/seo-services/` |
| Home services | "seo for home service contractors" 211 at **pos 15**, "home services seo" 146 at 22 | `/seo-for-home-service-contractors/`, which 301s to `/seo-services/` |
| Education | "seo for educational institutions" 140 at **pos 13**, "seo services for education" 133 | `/seo-for-education/`, which 301s to `/seo-services/` |
| Plumbing | "plumber seo company" 303, "plumber seo toronto" 204 (via `/seo-company-toronto/`) | City page, not an industry page |
| Manufacturing | "vancouver industrial seo marketing" 154 | `/seo-company-vancouver/` |

**Reading:** Google ranked our old hotel, home services and education pages on page 2, without them having been touched for a long time. Those industries are where a rebuilt page has the best starting point.

---

## 6. Hub or separate pages? (Andrew's open question, answered with data)

**Recommendation: both, in tiers.** This follows Andrew's lean (hub for sales, separate pages for search), with one change: **one page per industry, not separate SEO and AI-search pages**, because per-industry AI-search terms have no demand (section 3).

**Tier 1: dedicated, indexable industry pages (9)**

Each meets both tests: a real ThinkProfits result **and** measurable agency-intent demand. Each page covers SEO, AI search (AEO/GEO) and Google Ads for that industry.

| # | Page | Why |
|---|---|---|
| 1 | **Law firms** | Biggest demand (CA 4,910 / US 34,130); 2 case studies with numbers; old `/lawyer-seo/` history. |
| 2 | **Plumbing** | Strongest proof (3 case studies, 2 live clients); core client base. |
| 3 | **HVAC** | Shares the plumbing & heating proof; separate demand ("hvac seo" is its own term, and competitors run separate pages). |
| 4 | **Dental** | Demand 3,040 in Canada; Tsawwassen case study (add hard numbers). |
| 5 | **Hotels & hospitality** | Executive Hotels "$3M" is our single biggest published result; old page ranked about 18. |
| 6 | **Ecommerce** (SEO + Google Ads) | Golf Ball Planet and MVP; demand 2,890. Must not overlap `/ecommerce-website-design/`, which keeps the design terms. |
| 7 | **Manufacturing & industrial (B2B)** | 6 case studies plus live Wiseworth and SPIEDR; "b2b seo agency" 390 / 1,000. |
| 8 | **Home services & trades** (umbrella) | "seo for contractors", "trades marketing"; old page ranked about 15. Covers roofing, electrical, landscaping, cleaning, towing, drainage, fencing, garage door, pest control and restoration as short sections, with proof from Ultimate Fence, Anago, Jamie Davis, Clearset, PowerUp and Arbor Green. |
| 9 | **Education** | Sprott Shaw and Mujo case studies, AANMC live; old page ranked about 13. |

**Tier 2: promote to its own page once we have a case study**

| Industry | Why it isn't Tier 1 yet |
|---|---|
| Roofing | Demand is real (740 / 7,740) but no client proof. |
| Electricians | PowerUp is a live client; write their case study first. |
| Landscaping | Arbor Green is a live client; write their case study first. |

Until then they live as sections on the Home services & trades page.

**Tier 3: hub only, or drop**

These get no page of their own: auto repair, garage door, moving, pest control, restoration, cleaning, med spa, dermatology, chiropractors, physiotherapy, veterinarians, accountants.
- Trades go into the Home services & trades umbrella.
- Health clinics get one short "Healthcare & clinics" section on `/industries/`, pointing to the Dental page and the AANMC experience.
- Accountants get a single line in the hub's "Professional services" list.

**Not recommended:** real estate (2,820 / 15,360). Demand is high but we have no proof, and it's a crowded specialist market. Revisit only if Shawn wants to sell into it.

**Why not separate pages for every industry?** For 12 of these industries we have no proof, and demand is roughly 100–350 searches a month across all of Canada. Hand-writing 36 pages for them is the opposite of quality over quantity, and three near-identical pages per industry is what got flagged.

**Why not hub only?** The ranking pattern (section 4) is one dedicated page per industry. Our own old pages ranked on page 2 for hotels, home services and education. A hub alone gives up law, dental and plumbing, where we have both demand and proof.

---

## 7. URL plan and redirect map

**Proposed URLs:** `/industries/<slug>/` (e.g. `/industries/law-firms/`, `/industries/plumbing/`).
- Short, consistent, and nested under the hub, which supports the sales-hub and SEO-page split.
- Fallback if Phase 0 shows the redirect setup can't take about 60 more rules: keep the existing `/seo-services/local-seo/local-seo-<slug>/` URLs for the Tier 1 trades (no new redirects for those) and add only the missing pages.

| New page | Redirect into it (both slash and no-slash versions) |
|---|---|
| /industries/law-firms/ | /seo-services/local-seo/local-seo-law-firms/ · /aeo-services/law-firms/ · /ppc-advertising/ppc-for-law-firms/ · /lawyer-seo/ (repoint) |
| /industries/plumbing/ | /seo-services/local-seo/local-seo-plumbing/ · /aeo-services/plumbing/ · /ppc-advertising/ppc-for-plumbing/ · /seo-for-plumbers (repoint) · /plumbing-seo-company-toronto/ (repoint) |
| /industries/hvac/ | /seo-services/local-seo/local-seo-hvac/ · /aeo-services/hvac/ · /ppc-advertising/ppc-for-hvac/ |
| /industries/dental/ | /seo-services/local-seo/local-seo-dentists/ · /aeo-services/dentists/ · /ppc-advertising/ppc-for-dentists/ · /dentist-seo-services (repoint) |
| /industries/hotels-hospitality/ | /seo-hotels-resorts/ (repoint) |
| /industries/ecommerce/ | /seo-for-retail (repoint) |
| /industries/manufacturing-industrial/ | /seo-for-manufacturing-companies/ (repoint) |
| /industries/home-services/ | /seo-for-home-service-contractors/ (repoint) · local-seo, AEO and PPC pages for roofing, electricians, landscaping, cleaning, garage door, pest control, restoration, home remodeling, moving and auto repair |
| /industries/education/ | /seo-for-education/ (repoint) |
| /industries/ (hub) | local-seo and AEO pages for med spa, dermatology, chiropractors, physiotherapy, veterinarians and accountants; /ppc-advertising/ppc-for-med-spa/ |

Count: about 51 templated URLs plus 9 repointed old URLs, roughly 60 rules (about 120 if slash variants need separate rules). **Phase 0 must confirm capacity first.**

**GSC check before removal:** no templated industry URL has more than 1 click in 6 months (section 2), so the traffic risk is negligible. Re-check the week before cut-over.

**Also fix, site-wide:** `www.thinkprofits.com` 302 → **301** to `https://thinkprofits.com/`.

---

## 8. Keyword targets per Tier 1 page

Intent for all of these is **commercial** (a business owner hiring an agency). Volumes are CA / US monthly. The primary keyword goes in the title, H1, first paragraph and URL slug; secondary keywords go in H2s and body copy. Write for Canadian readers (lawyers, Law Society, provinces) and serve US searchers as a secondary market.

| Page | Primary | Secondary | Notes |
|---|---|---|---|
| Law firms | **law firm seo** (480 / 4,400) | seo for lawyers (1,000 / 3,600 group) · legal seo (320 / 1,000) · law firm seo company (320 / 480) · seo for personal injury lawyers (320 / 1,300) · law firm marketing (140 / 1,600) · law firm web design (260 / 2,400) · google ads for lawyers (20) | Proof: Thomas & Associates (family), Hoogbruin (personal injury). Use Law Society of BC advertising rules, not "bar association". |
| Plumbing | **seo for plumbers** (70 / 590 incl. "plumbing seo") | plumber marketing agency (40 / 720) · local seo for plumbers (40 / 590) · advertising for plumbers (110 / 480) · plumber web design (170 / 480) · google ads for plumbers (40 / 260) · digital marketing for plumbers (50 / 260) | Proof: John Sadler, Lone Star, Butler. Cover Local Services Ads (a common FAQ). |
| HVAC | **hvac seo** (110 / 720) | seo for hvac (140 / 320) · hvac marketing agency (50 / 880) · hvac lead generation (50 / 880) · hvac marketing (70 / 480) · hvac web design (70 / 480) · plumbing and hvac seo (50 / 480) | Seasonal demand and heat-pump rebate content are good angles. Link to Plumbing. |
| Dental | **dental seo** (480 / 1,300) | dental marketing (590 / 1,600) · seo for dental office (390 / 140) · dental seo services (390 / 1,300) · dental seo agency (260 / 480) · advertising for dentists (210 / 720) · local seo for dentists (170 / 880) · dental google ads (90 / 390) | Get real numbers for Tsawwassen. Cover the BC College of Oral Health Professionals advertising rules (*confirm the current regulator name and rules*). |
| Hotels & hospitality | **hotel seo** (30 / 590) | hospitality marketing agency (30 / 590) · hotel marketing (30 / 320) · google ads for hotels (40 / 320) · restaurant seo (90 / 390) · marketing for restaurants (90 / 720) · advertising for restaurants (210 / 1,000) | Small volumes but high value per client. Lead with the Executive Hotels result. |
| Ecommerce | **ecommerce seo agency** (390 / 1,000) | ecommerce seo services (390 / 1,300) · shopify seo (210 / 1,600) · shopify seo agency (210 / 1,300) · ecommerce marketing (110 / 1,000) · shopify advertising (170 / 720) | Leave "ecommerce web design" terms to `/ecommerce-website-design/` and link across. |
| Manufacturing & industrial | **b2b seo agency** (390 / 1,000) | b2b marketing agency (480 / 5,400) · manufacturing seo (50 / 390) · industrial marketing (30 / 390) · manufacturing website design (50 / 590) · b2b lead generation (170 / 1,900) | Six case studies to choose from. Name the sub-sectors: cabinetry, industrial supply, staging, energy services. |
| Home services & trades | **seo for contractors** (260 / 590) | contractor seo (260 / 880) · trades marketing (170 / 1,300) · home services marketing agency (30 / 590) · contractor web design (90 / 1,000) · roofer seo (320 / 2,400) · seo for electricians (70 / 720) · landscaping marketing (70 / 390) · pest control seo (90 / 880) · moving company seo (90 / 1,000) | One H2 section per trade with its own term. Promote a trade to its own page once it has a case study. |
| Education | **seo for educational institutions** (GSC-proven; Keyword Planner too small to measure) | higher education marketing (110 / 260) · higher ed marketing agencies (20 / 320) · digital marketing for schools (50 / 480) · website design for schools (40 / 480) | Avoid "education marketing" as the main term; those searchers mostly want marketing courses. |

---

## 9. FAQ question bank (stand-in for People Also Ask)

Google and Bing blocked automated searches, so these questions come from the FAQ sections of the pages that rank (section 4). Questions that come up again and again across industries:

- How much does [industry] SEO cost per month?
- How long does [industry] SEO take to show results?
- SEO or Google Ads (or Local Services Ads): which is better for my [business]?
- How do I get into the Google Map Pack?
- How many reviews do I need?
- Does SEO help with ChatGPT and AI answers?
- Do you work with my competitors? (exclusivity)
- Do you lock me into a long-term contract? (Our answer: month-to-month, a real differentiator.)
- Can you help a practice in a smaller town or with several locations?
- Industry rules: Law Society advertising rules (law), dental regulator advertising rules (dental).

Re-check against real People Also Ask results (Semrush or a manual incognito search) before final copy.

---

## 10. Rules for every Tier 1 page (written by hand)

- **Write to the business owner.** Customer search examples only as short, labelled illustrations.
- **At least one proof block** with a named client and a result taken from the case study or GSC/Ads data. No result means no claim.
- **No guarantees** (rankings, "first AI citations in 60–90 days") and no unsourced statistics. Cite every number.
- **Canadian English and Canadian terms.** Price in CAD; link to our published tiers, not a promised total.
- **Service-page layout:** hero, what we do (SEO / AI search / Google Ads), proof, process, pricing link, FAQ, CTA. About 1,200–2,000 words, written by hand.
- **Links:** to `/industries/`, the matching case studies, `/seo-services/`, `/aeo-services/`, `/ppc-advertising/`, and sibling industries where they're relevant (Plumbing ↔ HVAC).
- **Schema:** Service + FAQPage (real FAQ text only) + BreadcrumbList.

---

## 11. Decisions needed from Andrew

1. Approve the tiered model: 9 dedicated pages, plus the hub, plus everything else removed.
2. Approve `/industries/<slug>/` URLs, or use the fallback (section 7).
3. Confirm we can name these clients and show their results publicly: Executive Hotels, Thomas & Associates, Hoogbruin, Golf Ball Planet, Merit Kitchens, Sprott Shaw, John Sadler, Lone Star, Butler, Tsawwassen Family Dental.
4. Roofing, electricians, landscaping: can we write PowerUp and Arbor Green case studies, or find a roofing result?
5. Order of work. Suggested: Law firms → Plumbing → HVAC → Dental → Hotels → Manufacturing → Ecommerce → Home services → Education. That puts demand times proof first.

## 12. Next steps

- [ ] Lovable Phase 0 report (inventory and redirect capacity), including the 20 local-seo pages and the old URLs (see the addendum message).
- [ ] Andrew's decisions (section 11).
- [ ] Fix the www 302 → 301 (independent; can go now if Andrew agrees).
- [ ] Repoint the 9 old WordPress redirects as soon as the new pages exist.
- [ ] Francis hand-writes Tier 1 pages in the order above; Andrew reviews; Lovable pastes the final copy in.
- [ ] Re-run People Also Ask once Semrush units are topped up.
- [ ] After launch: request indexing, watch GSC weekly for 6 weeks (404s, redirect chains, cannibalisation between `/industries/ecommerce/` and `/ecommerce-website-design/`).
- [ ] Separate audit: the 40 city pages (same template risk).
