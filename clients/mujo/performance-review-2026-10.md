# Mujo Learning Systems: SEO performance review, October 2026

- **Prepared by:** Francis Uy (SEO), for Andrew's performance review with Brittni (original date 2026-10-20, being rescheduled)
- **Prepared on:** 2026-10-21 (v3: adds keyword detail, leads, AI visibility, search volume, competitors, quick wins, site speed)
- **Source:** Google Search Console, sc-domain:mujo.com, web search only. Pulled 2026-10-21.
- **Periods compared (92 days each):**
  - **This quarter:** 2026-07-19 to 2026-10-18
  - **Previous quarter:** 2026-04-18 to 2026-07-18 (includes the new-site launch on 2026-06-12)
  - **Same quarter last year:** 2025-07-19 to 2025-10-18
- **Also used (section 3b):** GA4 (organic leads, with Singapore and China bot traffic excluded), Google Keyword Planner (US search volume), a live Google spot check, and WP Rocket's stored speed test.
- **Not included:** Semrush position tracking (API units at zero on 2026-10-21; top it up and add the visibility trend before the meeting if possible).

---

## 1. Headline numbers

| Metric | This quarter | Previous quarter | Change | Same quarter 2025 | Change YoY |
|---|---|---|---|---|---|
| Clicks from Google | **1,673** | 1,556 | **+7.5%** | 1,448 | **+15.5%** |
| Impressions | 105,807 | 178,380 | -40.7% | 171,542 | -38.3% |
| Click-through rate | **1.58%** | 0.87% | +0.71 pts | 0.84% | **+0.74 pts (nearly double)** |
| Average position | 11.5 | 11.2 | flat | 29.5 | see note |

**The short version:** more people are clicking through to mujo.com than a year ago, and a much bigger share of the people who see Mujo in Google now click. Fewer impressions, but better ones.

**Reading the impressions drop honestly**
- **YoY:** In September 2025 Google stopped supporting the &num=100 results parameter, which removed a lot of rank-tracker "impressions" from Search Console and made average position look better across the industry overnight (reported by Search Engine Land and others, mid-September 2025; verify and link the article before this goes to the client). Our own daily data shows it: average position sat around 30 to 45 until 2025-09-10, then dropped to the low teens within days. So last year's impression total and position are inflated and not a fair comparison. Clicks are the trustworthy YoY number.
- **QoQ:** The previous quarter was the new-site launch. Old shop URLs (separate teacher-copy and student-edition products) were retired or redirected, and their impressions went with them. Some of that is healthy consolidation. Some of it is a real dip on a couple of key pages (see section 3).
- **Junk impressions on both sides:** the previous quarter included about 10,300 impressions (0 clicks) from templated searches like "influencer marketing equipment for teachers", which have now disappeared. This quarter includes 7,501 impressions (0 clicks) from one meaningless query ("iaijodojo.com business type and classes offered"). Neither reflects real demand.

---

## 2. What's going well

**The site migration held and is paying off**
- The rebuilt site went live 2026-06-12 with a full redirect map. Clicks didn't dip after launch; this quarter is up on both the quarter before and last year.
- Pages on the new URL structure are now among the top performers:

| Page | Clicks (this Q) | Same Q 2025 | Position now | Position then |
|---|---|---|---|---|
| /high-school/digital-marketing-textbooks/social-media-marketing/ | 83 | 6 | 8.0 | 50.9 |
| /teacher-blog/creative-lesson-planning-marketing/ | 86 | 17 | 12.9 | 12.8 |
| /higher-education/ai-textbooks/ | 49 | 21 | 8.7 | 14.5 |
| /high-school/ (hub) | 28 | 2 | 19.0 | 5.1 |
| /high-school/ai-textbooks/ | 24 | 2 | 9.0 | 12.0 |

**The AI catalogue is getting found**
New AI and business title pages that didn't exist a year ago are already bringing in traffic, all ranking in the top 10 on average:
- Generative AI for Business (shop page): 40 clicks, 7.3% CTR, position 7.8
- AI Accounting Principles: 33 clicks, position 6.4
- Sports & Entertainment Marketing (CTE): 29 clicks, position 7.5
- Entrepreneurship Fundamentals (CTE): 27 clicks
- Foundations of Artificial Intelligence (CTE): 25 clicks, position 6.9
- AI Business Writing: 18 clicks, position 7.4

**Teacher blog content is working**
- "Creative lesson planning for marketing" is the #2 page on the site by clicks (86, up from 17).
- The newer "Social media marketing textbook selection guide 2026" post already has 26 clicks at position 9.
- This is the kind of content teachers search for before they pick a textbook, so it's worth more of the same.

**Strong rankings on buying-intent searches (non-brand, US-heavy)**

| Search | Avg. position | Notes |
|---|---|---|
| digital marketing curriculum high school | 1.6 | 9.8% CTR |
| high school marketing textbook | 4.9 | |
| high school web design curriculum | 5.0 | 12% CTR |
| ai textbooks | 5.3 | |
| ai business administration | 5.3 | |
| artificial intelligence textbook | 6.3 | 274 impressions |
| marketing class in high school | 6.9 | new this quarter |
| cte textbooks | 7.3 | |

Rising this quarter vs last: "marketing curriculum high school" (7 clicks, up from 2), "high school marketing curriculum" (position 14.8 to 11.6), "high school marketing class curriculum" (19.3 to 15.0).

**Behind-the-scenes work this quarter** (supports future results; not reflected in the numbers yet)
- Schema clean-up on 2026-10-10: removed hand-coded LocalBusiness markup from 71 pages, added CollectionPage schema to 9 hub pages and FAQ schema to 22 pages.
- Book schema drafted for all 38 titles, with named authors confirmed for 26 of them.
- Redirects and 404 fixes after launch; robots.txt tightened against filter/add-to-cart crawl waste and a scraper bot (2026-09-30).

---

## 3. What to watch

- **"AI for Business" (high school) is seen a lot but rarely clicked.** 7,978 impressions at position 5.5, but only 18 clicks (0.23% CTR). It's the most-seen page after the homepage. The title and meta description likely aren't matching what searchers want. Biggest quick win on the site.
- **/high-school/digital-marketing-curriculum/ has slipped.** 79 clicks vs 145 last year; impressions down 70%. Position actually improved (12.9 to 7.8), so it's ranking for fewer searches rather than ranking worse. Needs a content refresh and stronger internal links.
- **Homepage clicks down 22.5% YoY** (248 vs 320) while impressions rose 28%. CTR fell from 2.1% to 1.3%. Partly the brand collision below.
- **"Mujo" is a shared name.** "mujo ai" fell from 69 to 23 clicks quarter over quarter on 3,667 impressions; "mujo" gets 0.7% CTR on 11,000 impressions. Most of those searchers are looking for a different Mujo. Not a problem to fix, but it means brand impressions overstate demand.
- **Old PDF assets are fading.** The 2024 "UGC with Starbucks and Stanley" PDF dropped from 34 to 8 clicks. Low priority, but these could be turned into proper blog pages that link to the textbooks.
- **Web design curriculum page:** clicks 48 to 27 YoY, impressions down 60%, position improved. Same pattern as the digital marketing curriculum page.

---

## 3a. Keyword detail: what moved

**Read this first:** Google hides most individual searches for privacy. The non-brand searches it names account for only 76 of this quarter's 1,673 clicks (brand searches containing "mujo" add 169). So these lists show direction, not totals. Positions are Google's average for that search; lower is better.

**Keywords that improved (same quarter last year → now)**

| Search | Position then | Position now | Impressions now | Clicks then → now |
|---|---|---|---|---|
| ai textbooks | 26.6 | 5.3 | 85 | 1 → 4 |
| ai textbook | 20.8 | 6.9 | 252 | 0 → 1 |
| artificial intelligence textbook | 22.5 | 6.3 | 274 | 0 → 1 |
| cte textbooks | 21.3 | 7.3 | 33 | 0 → 2 |
| ai in business administration | 65.5 | 3.2 | 85 | 0 → 0 |
| ai writing for business communication | 46.9 | 3.8 | 16 | 0 → 0 |
| business analytics fundamentals | 37.9 | 6.0 | 23 | 0 → 1 |
| great ideas for teaching marketing | 44.7 | 8.7 | 58 | 0 → 1 |
| high school web design curriculum | 11.0 | 5.0 | 33 | 3 → 4 |
| marketing class in high school | 11.5 | 6.9 | 153 | 1 → 2 |
| digital marketing for higher education | 67.4 | 29.4 | 45 | 0 → 0 |
| digital marketing curriculum high school | 1.4 | 1.6 | 51 | 3 → 5 (holding #1–2) |

**Climbing since last quarter**

| Search | Last quarter | Now | Impressions now | Clicks last Q → now |
|---|---|---|---|---|
| foundations of marketing | 16.3 | 5.6 | 241 | 1 → 0 |
| high school marketing textbook | 10.4 | 4.9 | 178 | 1 → 2 |
| marketing textbook high school | 15.3 | 8.5 | 211 | 1 → 0 |
| marketing class in high school | 13.2 | 6.9 | 153 | 0 → 2 |
| high school marketing class curriculum | 19.3 | 15.0 | 249 | 2 → 4 |
| high school marketing curriculum | 14.8 | 11.6 | 238 | 1 → 4 |
| marketing curriculum high school | 12.8 | 11.3 | 272 | 2 → 7 (top non-brand search) |

**New searches showing up this quarter** (weren't there last quarter): seo textbook (position 4.6, 345 impressions), seo textbook publisher (3.9), seo lesson plans (5.7), ai school textbook (2.2), ai school books (6.2), instructors manual (7.6), marketing lessons (10.9), social media marketing teaching materials (16.4).

**Keywords that dropped (same quarter last year → now)**

| Search | Position then | Position now | Impressions now | Clicks then → now | Likely cause |
|---|---|---|---|---|---|
| digital marketing teacher manual (+ "teacher's" / "teachers" variants) | 1.6–1.9 | 16.6–19.3 | ~740 combined | 0 → 0 | Old teacher-manual product pages were retired in the rebuild; best page now is the higher-ed Digital Marketing shop page (position 9.4) |
| digital marketing textbook publisher(s) | 2.0–2.6 | 9.7–14.9 | 277 | 0 → 0 | /digital-marketing-textbook-publisher/ no longer the ranking page |
| social media marketing lesson plans for high school students | 3.5 | 14.1 | 279 | 2 → 0 | Lesson-plan intent not matched by a current page |
| social media marketing lesson plans | 6.1 | 13.7 | 223 | 0 → 0 | Same |
| digital marketing lesson plans | 4.3 | 6.8 | 245 | 4 → 0 | Same |
| high school marketing curriculum | 4.9 | 11.6 | 238 | 9 → 4 | Recovering since last quarter |
| marketing curriculum high school | 7.0 | 11.3 | 272 | 12 → 7 | Recovering since last quarter |
| high school marketing class curriculum | 4.1 | 15.0 | 249 | 2 → 4 | Recovering since last quarter |
| marketing automation syllabus | 8.2 | 29.0 | 24 | 0 → 0 | |
| big data textbook | 7.6 | 18.8 | 20 | 0 → 0 | |
| digital marketing essentials textbooks | 6.8 | 15.8 | 98 | 0 → 0 | |
| social media marketing curriculum high school | 4.5 | not showing | 0 | 3 → 0 | |

**Dipped since last quarter:** "ai textbooks" slipped from 4.3 to 5.3, with clicks down from 9 to 4 and impressions from 232 to 85.

**Gone, and not worth chasing:** broad "SEO book" searches from last year (e.g. "manual seo" 2,452 impressions, "book seo" 1,381), which ranked at positions 60+ and never brought clicks.

**The pattern:** product and AI-textbook searches are much stronger. The losses cluster around **lesson plans, teacher manuals and "publisher"** searches. Section 3b puts those losses in proportion: each is only about 10 searches a month in the US, and the site already has pages for them (/teacher-resources/digital-marketing-lesson-plans/ and a Teacher Manuals page) that need strengthening, not replacing.

---

## 3b. Deeper research (added 2026-10-21)

### Leads from organic search (GA4, Singapore and China bot traffic excluded)

GA4 property "https mujo" (262512439). Same three periods as above.

| Organic search | This quarter | Previous quarter | Same quarter 2025 | Change YoY |
|---|---|---|---|---|
| Sessions | 2,025 | 1,823 | 1,884 | +7.5% |
| Engaged sessions | 1,866 | 1,623 | 1,674 | +11.5% |
| **Exam copy requests (high school + higher ed)** | **115** | 108 | 86 | **+34%** |
| – High school exam requests | 72 | 82 | 46 | +57% |
| – Higher ed exam requests | 43 | 26 | 40 | +8% |
| Chat conversations connected | 130 | 114 | 82 | +59% |
| Online purchases (transactions) | 14 | 18 | 3 | +11 |
| Online revenue | US$2,338 | US$2,142 | US$1,023 | +129% |

- **Headline for the meeting:** organic search produced **115 instructor exam copy requests** this quarter, up 34% on last year. For a textbook publisher, that's the lead that matters.
- Phone clicks (168 this quarter) are left out of the headline; tap-to-call events are noisy and can't be tied to a real call.
- Revenue numbers are small and may reflect tracking changes after the rebuild, so treat them as directional. Most adoption revenue comes offline (school purchase orders), which GA4 can't see.

### AI search visibility

- **AI assistants are now a real referral source.** GA4 recorded **107 sessions from AI assistants** this quarter (51 last quarter, none in the same quarter last year), with 34 key events. Sources: ChatGPT 82 sessions (28 key events), Gemini 21, Perplexity 3, Claude 2, Copilot 1.
- That works out to about 1 key action (exam request, chat, purchase, etc.) for every 3 visits, far above the site average, so people who arrive from AI answers tend to arrive ready to act.
- **No AI visibility tracking is set up yet.** Rank Math's AI Visibility module on mujo.com has no brand configured, and our BrightLocal API key is currently invalid. Recommended: set up tracking for 10 to 15 buyer prompts (e.g. "best AI textbook for college business courses", "high school digital marketing curriculum") so the next review can report mention share, not just referrals.

### Search volume (Google Keyword Planner, US, last 12 months)

| Search | Avg. monthly US searches | Trend | Mujo's position (GSC, this quarter) |
|---|---|---|---|
| ai textbook / artificial intelligence textbook | **590** | Rising: 320 in Jun–Jul, 880 in Aug, 720 in Sep | 6.3–6.9 |
| ai literacy curriculum | 50 | Rising: 110 in Sep | 22.1 |
| foundations of marketing | 70 | Rising: 140 in Sep | 5.6 |
| digital marketing teacher manual (each variant) | ~10 | Flat | 14–22 |
| digital marketing lesson plans | ~10 | Flat | 5.8 (Oct) |
| social media marketing lesson plans | ~10 | Flat | 12.6 (Oct) |
| digital marketing textbook publisher | ~10 | Flat | 9.7 |
| cte textbooks | ~10 | Flat | 7.3 |

- **What this changes:** the keywords that dropped are low-volume. The real prize is **"AI textbook"**: about 590 US searches a month, climbing into back-to-school, with Mujo already on page one (position 6–7) but getting a 0.4% CTR. Moving that into the top 3 is worth far more than recovering the teacher-manual terms.
- **"AI literacy curriculum"** is small but doubling, with Mujo on page 3. It's an early-mover opportunity that fits the Artificial Intelligence Literacy title.
- Keyword Planner returns zero for many long-tail curriculum phrases (e.g. "high school marketing curriculum") that Search Console shows getting 200–300 impressions a quarter. Search Console is the better guide for these niche terms.

### Who Mujo competes with on Google (spot check)

Logged-out Google searches (US settings) from our browser on 2026-10-21. One location, one moment, so this is directional: Search Console averages for some of these are lower (12–22), so most US searchers likely see Mujo further down, below ads and other features.

| Search | Mujo's spot (organic) | Who else ranks |
|---|---|---|
| high school marketing curriculum | #4 (with 5.0★, 23 reviews) | Park Hill School District PDF, Virginia Dept. of Education, MyCareerTech, JA USA, Teachers Pay Teachers, Business Education with Denise Leigh, CTE Resource |
| social media marketing lesson plans for high school | #1 (5.0★) | Digital Promise, Illinois State Board of Ed, Savvas, Great Ideas for Teaching Marketing, Teachers Pay Teachers, Denise Leigh ($145 course) |
| digital marketing teacher manual | #1 and #5 | HubSpot Academy, Open Textbook Library, VitalSource (Mujo's own manual listed at CA$399) |
| digital marketing lesson plans | #1 (Teacher Resources page) | ESL lesson sites, Scribd, Teachers Pay Teachers, HubSpot Academy |
| ai textbook for college business | #2 (Business Analytics Fundamentals, 5.0★) | McGraw Hill (#1 and #5), University of Delaware guide, Amazon |
| digital marketing textbook publisher | #6 | McGraw Hill, Vibrant Publishers, Open Textbook Library, Sage |
| cte textbooks | Not in top 10 | G-W (Goodheart-Willcox), McGraw Hill, OER Commons, Saddleback, iCEV, Cengage |

- **The 5.0★ review stars are showing** on Mujo's results. That's a real click advantage, and worth protecting.
- **Competitor set:** big publishers (McGraw Hill, Cengage, G-W, Savvas) plus low-cost teacher marketplaces (Teachers Pay Teachers, Denise Leigh). Mujo's angle against both is complete, turnkey courseware.
- **Gap:** generic "CTE textbooks" is owned by the big CTE publishers. Not worth chasing head-on at ~10 searches a month; Mujo wins on subject-specific terms instead.

### Quick-win pages: seen a lot, clicked rarely

Pages on page one (position ≤ 11) with a CTR under 1.5% this quarter. Each needs a better title and meta description.

| Page | Impressions | Position | CTR | Clicks |
|---|---|---|---|---|
| /high-school/business-textbooks/ai-for-business/ | 7,978 | 5.5 | 0.23% | 18 |
| /teacher-blog/digital-marketing-skills-every-high-school-graduate-should-have-in-2026/ | 4,065 | 10.4 | 0.37% | 15 |
| /shop/high-school-cte/foundations-artificial-intelligence-textbook/ | 1,787 | 6.9 | 1.40% | 25 |
| /high-school/digital-marketing-textbooks/foundations-of-marketing/ | 1,622 | 6.7 | 0.86% | 14 |
| /higher-education/ai-textbooks/prompt-engineering-curriculum/ | 1,272 | 7.5 | 0.86% | 11 |
| /higher-education/business-textbooks/artificial-intelligence-business-administration/ | 764 | 8.1 | 1.05% | 8 |

**Page-two pages to push onto page one** (high impressions, position 15–25): /higher-education/digital-marketing-textbooks/ (1,620 impressions, position 23.6), /higher-education/digital-marketing-textbooks/influencer-marketing-fundamentals/ (1,400, 15.7), /shop/higher-ed/digital-marketing-textbook/ (1,179, 18.8), /higher-education/digital-marketing-textbooks/social-media-marketing-strategies/ (948, 19.2), /teacher-resources/digital-marketing-lesson-plans/ (909, 24.4).

**Housekeeping found along the way:** a tracked homepage URL (/?utm_campaign=gmb_canada...) is getting its own impressions in Google (371 this quarter). The homepage canonical tag should consolidate it; worth a quick check.

### Site speed

- Fresh PageSpeed tests couldn't run today (Google's free testing quota was used up).
- Last stored result (WP Rocket / GTmetrix, homepage, mobile, April 2026): **score 97, grade A**, largest content loaded in 0.6 s, layout shift 0.05. That's well inside Google's "good" thresholds, but it predates the June rebuild and covers the homepage only.
- Action: re-run WP Rocket's page insights on the homepage and the top 5 landing pages after the meeting, so we can confirm the rebuilt site holds up.

---

## 4. Recommended next steps (next 90 days)

Ranked by impact for effort, within the 10 hours/month retainer. Results depend on Google and competitors, so these are targets, not guarantees.

1. **Rewrite the titles and meta descriptions on the six quick-win pages in section 3b**, starting with "AI for Business" (high school). Lowest effort, quickest signal. Measure CTR change after 4 to 6 weeks.
   - **Then go after "AI textbook" (about 590 US searches a month and rising).** Mujo sits at position 6–7. Strengthen /higher-education/ai-textbooks/ and /high-school/ai-textbooks/ for that phrase (copy, FAQ, internal links from every AI title page) and aim for the top 3.
2. **Roll out the Book schema to all 38 titles.** Drafted and tested; needs Andrew's OK on the method (Rank Math per-product vs one WPCode snippet). Helps Google and AI answer engines understand each title, author, ISBN and format.
3. **Refresh /high-school/digital-marketing-curriculum/ and /high-school/web-design-curriculum/**: tighten copy around "curriculum", "lesson plans" and "teaching materials", add an FAQ, and link to them from the related blog posts. Target the searches that slipped: "digital marketing teacher manual" variants (were 1.6–1.9, now 16.6–19.3), "social media marketing lesson plans" (were 3.5–6.1, now 13.7–14.1), "digital marketing lesson plans" and "digital marketing textbook publisher". These are low-volume (about 10 searches a month each), so fold them into the existing /teacher-resources/ pages rather than building new ones.
4. **Two teacher-blog posts per quarter** modelled on the two winners (lesson planning, textbook selection guide). Suggested angles: AI lesson ideas for CTE business classes; how to choose an AI textbook for college business programs. Run the overlap check against existing posts first.
5. **Settle the open site decisions with Brittni** (these are blocking SEO work):
   - High School / Higher Education wording in every title and H1
   - Product consolidation (separate student/teacher products)
   - Whether the Shop page should be indexed
   - Current proof points ("250+ schools" etc.) and the ADA claim
   - Whether local SEO / Google Business Profile is paused or active
6. **Texas push:** support the Texas Edition pages (IMRA Cycle 2026) with internal links from the CTE hubs and one Texas-focused blog post.
7. **Measurement clean-up:** add a GA4 data filter for the Singapore bot traffic so reports are clean by default (exam copy requests are already tracked as key events). Top up Semrush API units so position tracking can be included. Re-run site speed tests on the rebuilt site.
8. **Set up AI visibility tracking** (Rank Math AI Visibility or BrightLocal, once its API key is fixed) for 10 to 15 buyer prompts, so we can measure how often ChatGPT, Gemini and Google's AI answers mention Mujo. Book schema (step 2) is the main lever here.

---

## 5. Talking points for the meeting (for Andrew)

- Organic search produced **115 instructor exam copy requests** this quarter, **up 34% on last year**.
- Clicks from Google are **up 15.5% on last year** and **up 7.5% on last quarter**, through a full site rebuild.
- **ChatGPT and Gemini now send traffic** (107 visits this quarter, none a year ago), producing 34 key actions such as exam requests and chats.
- The biggest growth opportunity is **"AI textbook"** (about 590 US searches a month and rising); Mujo is already on page one.
- **CTR has nearly doubled** (0.84% to 1.58%): Mujo is showing up for more relevant searches.
- New AI titles and teacher-blog posts are already ranking on page one and bringing in traffic.
- The impressions drop is mostly a Google reporting change (Sept 2025) plus retired old URLs, not lost rankings.
- Next quarter's focus: turn high-visibility pages into clicks (titles/meta), launch Book schema, refresh the two curriculum pages, and get decisions on the five open site items.
