# Mujo Learning Systems: keywords

> Updated 2026-10-07. DRAFT for Francis's review.
> Sources: GSC `sc-domain:mujo.com` (2026-07-09 to 2026-10-06; queries, pages, countries); Semrush project 2160205 (campaigns call only, 2026-10-07); Slack #mujo automated report reviews (2026-06-26, 07-08, 08-08, 09-09) and Andrew/Francis DMs (2026-06-24, 07-03); Drive: "Mujo_Institution_Keywords_Optimization.xlsx" (`1fnAo8DF3_JHvVMIIPOfTkxmXL6QZrrb6`, 2026-03-18), "Mujo | Local Keyword Research" (`1L9HM18aJ_qOwNEMkhnKWzrTHUMSMe3R7Psyt4AuXm9M`, 2025-02), "Mujo Ads 2025" (`1sFTBfmUtak1c5FbgJs9C2A_FAfnSnMiAAKTsLkk7_Js`, 2025-03); live site and WooCommerce Store API (2026-10-07); [CLIENT.md](CLIENT.md).
> Reusable: section 4 (keyword rules) is the checklist to run any new tracked, PPC or content keyword against before it goes live.

## 1. Tracked keywords (Semrush)

**Source:** Semrush Position Tracking, project **2160205** ("Mujo", www). Attempted 2026-10-07.

**Not pulled this session.**
- The `campaigns` report for 2160205 returned **no targets** (same API quirk as John Sadler's project).
- `tracking_position_organic` on campaign `2160205` failed with "unable to charge units".
- The `resource_organic` fallback returned **"API UNITS BALANCE IS ZERO"**.
- **Redo this section once Semrush API units are topped up.** Pull positions, competitors and visibility for both campaigns.

**What we know about the tracked set** (from the automated report reviews, which read the Semrush PDF)
- Two campaigns: **USA** and **Canada**. Campaign IDs aren't visible through the API.
- May 2026: US visibility 24.72% (-15.74); CA 24.11% (-3.46). US 13 up / 32 down; CA 11 up / 21 down.
  - Wins: "what is marketing in high school" #1 (+31) and "social media marketing lesson plans" #1 (US); "marketing automation syllabus" #1 (+21) and "high school marketing curriculum" #1 (+18) (CA).
- July 2026: **26 US keywords in the top 3**; mujo.com ahead of McGraw Hill, Cengage and Pearson on visibility.
- August 2026: US visibility -2.75% (12 up / 22 down); CA +4.80% (14 up / 11 down).

**Project clean-up**
- **24450287** "mujo.com" and **14590131** "mujo.com (no www)" duplicate 2160205. Confirm they hold no unique tracking or audit history, then archive them so reports don't split.
- The 5xx CSV in this folder came from a Semrush Site Audit on `www.mujo.com` (2026-09-08). Check which project owns that audit before archiving anything.

### GSC stand-in: non-brand queries (90 days)

Until Semrush is back, this is the best view of what Google already associates with the site. Sorted by impressions; positions are GSC averages. **Volume** isn't available (no Semrush), so impressions stand in.

The top 1,000 non-brand queries total only **77 clicks** on 13,496 impressions. Brand ("mujo", "mujo learning systems", "mujo ai") drives most clicks.

**Commercial: curriculum, textbooks, teaching materials** (the money terms)

| Query | Clicks | Impr. | Pos. | Likely page |
|---|---|---|---|---|
| digital marketing teaching materials | 0 | 416 | 30.0 | HE/HS digital marketing hubs |
| marketing curriculum high school | 4 | 267 | 11.8 | /high-school/digital-marketing-curriculum/ |
| digital marketing teachers manual | 0 | 262 | 18.3 | teacher manual / resource pages |
| ai textbook | 1 | 252 | 6.8 | /higher-education/ai-textbooks/ |
| digital marketing high school | 0 | 250 | 8.4 | /high-school/digital-marketing-curriculum/ |
| digital marketing lesson plans | 0 | 249 | 7.5 | curriculum pages / blog |
| high school marketing class curriculum | 5 | 245 | 15.7 | /high-school/digital-marketing-curriculum/ |
| artificial intelligence textbook | 1 | 245 | 6.4 | /higher-education/ai-textbooks/ |
| digital marketing teacher manual | 0 | 244 | 19.3 | teacher manual / resource pages |
| high school marketing curriculum | 4 | 230 | 11.5 | /high-school/digital-marketing-curriculum/ |
| foundations of marketing | 0 | 221 | 5.5 | /high-school/digital-marketing-textbooks/foundations-of-marketing/ |
| digital marketing teaching resources | 0 | 212 | 16.9 | /teacher-resources/ |
| digital marketing teacher's manual | 0 | 200 | 20.0 | teacher manual / resource pages |
| college textbook for digital marketing | 0 | 187 | 8.9 | HE digital marketing hub |
| high school marketing textbook | 1 | 166 | 5.5 | HS hub |
| digital marketing textbook | 0 | 166 | 26.5 | HE Digital Marketing title |
| digital marketing textbook publisher(s) | 0 | 283 | 9.8 / 14.8 | /digital-marketing-textbook-publisher/ |
| marketing class in high school | 1 | 148 | 7.3 | HS hub / blog |
| digital marketing course book | 0 | 124 | 29.8 | HE Digital Marketing title |
| digital marketing essentials textbooks | 0 | 106 | 14.6 | HE digital marketing hub |
| ai textbooks | 4 | 91 | 5.6 | /higher-education/ai-textbooks/ |
| ai school textbook / ai school books | 0 | 170 | 2.2 / 6.2 | /high-school/ai-textbooks/ |
| high school marketing class | 2 | 87 | 6.2 | HS hub |
| digital marketing for higher education | 0 | 87 | 24.0 | /higher-education/digital-marketing-textbooks/ |
| digital marketing curriculum high school | 4 | 46 | 1.7 | /high-school/digital-marketing-curriculum/ |
| high school web design curriculum | 3 | 31 | 4.6 | /high-school/web-design-curriculum/ |
| cte textbooks | 2 | 27 | 7.1 | HS hub |
| entrepreneurship curriculum | 0 | 94 | 33.0 | /high-school/business-textbooks/entrepreneurship-fundamentals/ |

**Off-target or irrelevant queries** (don't chase; some may be worth de-optimising or pruning)
- "2018 social media trends", "2018 social trends", "2018 trends social media" (~280 impressions): old trend posts.
- "chupa chups logo" (216), "content writing ideas / topics" (~450), "persona development tool" (157), "inbound marketing and seo" (99): blog posts pulling non-buyers.
- "cdi college" (115), "university of miami": other institutions' brand terms.
- "business writing with ai for dummies" (106): another publisher's title. **Don't target.**
- "ai generated textbooks": **conflicts with "100% Human Authored". Don't target.**
- "ai97805..." / "ai97891...": ISBN-style lookups (positions ~4). Make sure ISBNs are on product pages, then leave them.

## 2. Priority targets by page

**Sources:** GSC (2026-10-06), Institution Keywords sheet (2026-03-18; its proposed titles need superlatives removed), Local Keyword Research (2025-02), live titles/H1s (2026-10-07). Intent is commercial-investigational unless noted. Keywords are proposals until Brittni signs off.

| Page | Primary keyword | Secondary | Intent | Current state / note |
|---|---|---|---|---|
| / | AI, business & digital marketing curriculum | digital marketing textbooks for universities, colleges & high schools | Commercial / navigational | Pos 6.1, 19.5K impressions; mostly brand |
| /high-school/ | high school CTE curriculum | CTE marketing textbooks, high school marketing textbook | Commercial | Pos 20.4; H1 "High School CTE Curriculum & Textbooks" |
| /high-school/digital-marketing-curriculum/ | high school marketing curriculum | marketing curriculum high school, digital marketing curriculum high school, high school marketing class curriculum | Commercial | Best non-brand page (91 clicks); H1 is stuffed ("...Curriculum & Marketing Curriculum for High School Students"), so simplify |
| /high-school/digital-marketing-textbooks/social-media-marketing/ | high school social media marketing curriculum | social media marketing lesson plans, social media marketing high school class | Commercial | 79 clicks; title OK |
| /high-school/digital-marketing-textbooks/foundations-of-marketing/ | foundations of marketing high school curriculum | foundations of marketing textbook, marketing class in high school | Commercial | **Title has no HS signal** ("Foundations of Marketing \| Mujo Learning Systems"); pos 5.5 on "foundations of marketing" with 0 clicks |
| /high-school/business-textbooks/ai-for-business/ | AI for business high school curriculum | ai for business textbook | Commercial | **7,833 impressions at 0.2% CTR**: check which queries (possibly "mujo ai" brand collision) before rewriting |
| /high-school/ai-textbooks/ | AI curriculum for high school | ai textbooks for high school, ai school textbook | Commercial | Pos 8.5 |
| /high-school/web-design-curriculum/ | high school web design curriculum | website and e-commerce strategy textbook | Commercial | Pos 4.6 on primary |
| /high-school/business-textbooks/entrepreneurship-fundamentals/ | high school entrepreneurship curriculum | entrepreneurship fundamentals textbook | Commercial | Brittni: "doing well organically" (2026-01-22); "entrepreneurship curriculum" pos 33 |
| /texas/ and /texas/cte-funding/ | Texas CTE marketing curriculum | IMRA approved CTE materials *confirm wording*, Texas entrepreneurship I curriculum, CTE funding Texas | Commercial / informational (funding) | New 2026-09-24; no GSC data yet. Don't say "approved" until IMRA results are out |
| /higher-education/ | digital marketing and AI textbooks for higher education | college digital marketing textbooks, university marketing curriculum | Commercial | — |
| /higher-education/ai-textbooks/ | AI textbooks for higher education | ai textbook, artificial intelligence textbook | Commercial | 53 clicks, pos 9; good momentum |
| /higher-education/digital-marketing-textbooks/ | digital marketing textbooks for college | college textbook for digital marketing, digital marketing for higher education | Commercial | "digital marketing textbook" pos 26.5: weak |
| /digital-marketing-textbook-publisher/ | digital marketing textbook publisher | digital marketing textbook publishers | Commercial | Pos 9.8 / 14.8. Title has "Best Digital Marketing Publishers": **superlative, revise** |
| /teacher-resources/ | digital marketing teaching resources | digital marketing teacher manual, teaching materials | Commercial | Teacher-manual queries (~950 impr.) have no clear landing page |
| /higher-education/business-textbooks/artificial-intelligence-accounting-principles/ | AI accounting principles textbook | ai in accounting textbook | Commercial | Pos 6.5, 33 clicks |
| /teacher-blog/creative-lesson-planning-marketing/ | marketing lesson plans (informational) | great ideas for teaching marketing | Informational | 77 clicks; link it to the HS curriculum page |

**Duplicate-URL warning:** most titles exist as a curriculum page **and** a /shop/ product page (e.g. Sports & Entertainment: curriculum page 33 clicks vs shop page 31 clicks). Pick one primary URL per title before pushing keywords (see "Mujo GSC Product Version Comparison").

**PAA / FAQ:** no PAA pull was run this session (Semrush unavailable). Apply `memory/paa-research-standard.md` when Semrush is back. Starter questions from the 2025 sheet: "what is marketing in high school", "marketing project ideas for students", "introduction to marketing for high school students".

## 3. PPC keywords

**Campaigns** (Ads 2025 sheet, March 2025; current status unknown, see CLIENT.md section 7)
- **TP - High School (USA):** General Digital Marketing; Niche Industry Marketing (sports, entertainment, fashion); Social Media & Content Creation; Web Design & E-commerce.
- **TP - Higher Ed (CAN & USA):** AI Literacy; Big Data & Analytics; Business & Sales; General Marketing; HR Management; PPC Advertising; Project Management & Accounting; SEO; Social Media & Influencer Marketing; Web Design & E-commerce; Writing & Communications.

**Keyword themes** (from RSA headlines and paths; the live keyword lists weren't readable from Drive)
- [topic] curriculum / textbooks / lesson plans / syllabus (e.g. digital marketing lesson plans, social media lesson plans, SEO curriculum, PPC & Google Ads lesson plans, HR & recruitment lesson plans)
- teacher resources & courseware, free teacher exam copy
- marketing textbook publisher / business textbook publisher

**Issues to fix before any relaunch**
- Final URLs use **pre-June-2026 paths** (e.g. `/digital-marketing-textbooks/digital-marketing-textbooks-for-high-schools/...`). Point them at the new URLs.
- Headline "Top SEO Textbook Publisher" is a **superlative**; "5-Star Rated By Teachers" and "ADA Compliant" need substantiation.
- Proof points (34000+ Students & 210+ Schools, Trusted By 290+ Teachers) differ from the live site (250+ / 325+).
- Add new products not in the 2025 build: AI Literacy for Healthcare, AI Sales Fundamentals, Prompt Engineering and LLMs, Texas Editions.

### Negatives and standing exclusions

**Standing:** the ThinkProfits TLD placement-exclusion bot runs daily across the MCC, including this account (e.g. .top, .online and some .br domains, Jan–Feb 2026).

**Proposed negatives** (not confirmed in the account; check the search terms report)
- free, pdf, download, torrent, "for dummies"
- jobs, salary, careers, internship
- course near me, certification online (student-side demand, unless targeting the certificate programs)
- competitor publisher brands (mcgraw hill, cengage, pearson): decide deliberately; no rule found
- k-8, elementary, middle school (not in catalogue *confirm*)

## 4. Keyword rules

- **2026-06-24 (Andrew):** every HS and HE product/curriculum title and H1 should include "High School" or "Higher Education" (HE pages already say "for Higher Education"; HS pages are inconsistent). Exact pattern pending: Francis sent options 2026-07-03; Brittni's choice *confirm*.
- **2026-04-30 (Shawn):** content is "100% Human Authored". **Never target "AI-generated textbook" style terms.** AI as a *subject* (AI textbooks, AI curriculum) is core.
- **2026-02-05 (Andrew):** set a Rank Math focus keyword on every page.
- **2026-02-12 (Andrew):** student editions are the primary URLs for product keywords (85% of product clicks); teacher manual and resource-cloud versions consolidate into them.
- **2026-01-22 (Brittni):** any keyword-driven copy change goes to Brittni for approval first.
- **Standing (agency):** no superlatives ("best", "leading", "top", "#1", "definitive", "go-to") in titles, metas or ads; no ranking guarantees.
- **Standing (scope):** target only titles in CLIENT.md section 2. **Flag before use** these terms from the 2026-03 Institution Keywords sheet, because the offerings aren't confirmed:
  - CPA continuing education
  - corporate training programs
  - MBA electives
  - trade school / vocational college
  - "district-level volume pricing" and "statewide volume pricing" (pricing claims)
  - "grade 10–12" (fine if accurate *confirm*)
- **Texas:** only use TEKS / IMRA language on the two Texas Edition titles; don't imply state adoption until results are published.
- **Spelling:** US English in mujo.com keywords and copy ("program", "center") *confirm*.

## 5. Opportunities

**Page-2 commercial terms with existing impressions (GSC, 90 days)**
- "digital marketing teacher manual" cluster (~950 impressions, positions 18–20): no strong landing page. Either strengthen /teacher-resources/ or give the teacher-manual offer a clear section on each HE title page (not separate thin pages, given the consolidation plan).
- "digital marketing teaching materials" (416, pos 30) and "digital marketing teaching resources" (212, pos 16.9).
- "high school marketing class curriculum" (245, pos 15.7) and "marketing curriculum high school" (267, pos 11.8): tidy the stuffed H1 on /high-school/digital-marketing-curriculum/ and strengthen internal links from the blog.
- "digital marketing textbook" (166, pos 26.5) and "digital marketing course book" (124, pos 29.8): HE Digital Marketing title page.

**CTR fixes (high position, low clicks)**
- "foundations of marketing" (pos 5.5, 221 impressions, 0 clicks): add "High School Curriculum" to the title.
- /high-school/business-textbooks/ai-for-business/ (7,833 impressions, 0.2% CTR): diagnose the queries first.
- "ai school textbook" (pos 2.2, 90 impressions, 0 clicks): title/snippet test on /high-school/ai-textbooks/.

**Institution-type modifiers** (2025 Local Keyword Research + 2026 Institution sheet). Pattern: [topic] + [curriculum / textbooks / lesson plans / syllabus / teaching materials] + [for high school / college / universities / higher education]. Examples:
- AI curriculum for high school
- AI curriculum for higher education
- digital marketing curriculum for higher education
- digital marketing syllabus for colleges
- teaching artificial intelligence in high school
- university digital marketing textbooks
- CTE marketing pathway curriculum

Use 2–3 natural fits per page, as the sheet itself advises.

**New products with no keyword work yet**
- AI Literacy for Healthcare (Shawn asked for it on the homepage, 2026-04-29)
- AI Sales Fundamentals (timeline broken, Feb 2026)
- Prompt Engineering and LLMs
- Texas Editions

**AEO/GEO:** AI Assistant appears as a GA4 channel (Aug 2026 report). Product pages with clear "who it's for / what's included / LMS compatibility" Q&A blocks would help answer engines. No AEO scope is signed *confirm*.

## 6. Gaps

- **No Semrush data this session:** no tracked keyword list, volumes, competitors, or US/CA domain overview (API units at zero, 2026-10-07). Calls used: 3 `execute_report` attempts (campaigns: OK, no targets; positions: "unable to charge units"; organic: "balance is zero") plus 1 rejected for bad parameters.
- No PAA / question data pulled.
- Google Ads keyword lists, search terms and negatives not read; account status unknown.
- Francis's 2026-07-03 title/H1 suggestions (likely in "Website Audit - Mujo") not re-read; adoption status unknown.
- GSC non-brand view is capped at the top 1,000 queries; much long-tail is anonymised.
- Brand-name collision on "mujo" / "mujo ai" (low CTR) not investigated.
