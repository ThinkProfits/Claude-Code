# Mujo Learning Systems: SEO performance review, October 2026

- **Prepared by:** Francis Uy (SEO), for Andrew's performance review with Brittni (original date 2026-10-20, being rescheduled)
- **Prepared on:** 2026-10-21
- **Source:** Google Search Console, `sc-domain:mujo.com`, web search only. Pulled 2026-10-21.
- **Periods compared (92 days each):**
  - **This quarter:** 2026-07-19 to 2026-10-18
  - **Previous quarter:** 2026-04-18 to 2026-07-18 (includes the new-site launch on 2026-06-12)
  - **Same quarter last year:** 2025-07-19 to 2025-10-18
- **Not included:** Semrush position tracking (API units at zero on 2026-10-21; top it up and add the visibility trend before the meeting if possible). GA4 is left out on purpose: bot traffic from Singapore (Aug to Sept 2026) still skews users and sessions, so GSC is the reliable source for now.

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
- **YoY:** In September 2025 Google stopped supporting the `&num=100` results parameter, which removed a lot of rank-tracker "impressions" from Search Console and made average position look better across the industry overnight (reported by Search Engine Land and others, mid-September 2025; verify and link the article before this goes to the client). Our own daily data shows it: average position sat around 30 to 45 until 2025-09-10, then dropped to the low teens within days. So last year's impression total and position are inflated and not a fair comparison. Clicks are the trustworthy YoY number.
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

**The pattern:** product and AI-textbook searches are much stronger. The losses cluster around **lesson plans, teacher manuals and "publisher"** searches, which old pages used to catch and the new site doesn't have a clear page for. That feeds directly into next step 3.

---

## 4. Recommended next steps (next 90 days)

Ranked by impact for effort, within the 10 hours/month retainer. Results depend on Google and competitors, so these are targets, not guarantees.

1. **Rewrite the title and meta on "AI for Business" (high school)** and the other high-impression, low-CTR pages. Lowest effort, quickest signal. Measure CTR change after 4 to 6 weeks.
2. **Roll out the Book schema to all 38 titles.** Drafted and tested; needs Andrew's OK on the method (Rank Math per-product vs one WPCode snippet). Helps Google and AI answer engines understand each title, author, ISBN and format.
3. **Refresh /high-school/digital-marketing-curriculum/ and /high-school/web-design-curriculum/**: tighten copy around "curriculum", "lesson plans" and "teaching materials", add an FAQ, and link to them from the related blog posts. Target the searches that slipped: "digital marketing teacher manual" variants (were 1.6–1.9, now 16.6–19.3), "social media marketing lesson plans" (were 3.5–6.1, now 13.7–14.1), "digital marketing lesson plans" and "digital marketing textbook publisher". This may need one dedicated lesson-plans / teacher-resources page rather than a refresh alone.
4. **Two teacher-blog posts per quarter** modelled on the two winners (lesson planning, textbook selection guide). Suggested angles: AI lesson ideas for CTE business classes; how to choose an AI textbook for college business programs. Run the overlap check against existing posts first.
5. **Settle the open site decisions with Brittni** (these are blocking SEO work):
   - High School / Higher Education wording in every title and H1
   - Product consolidation (separate student/teacher products)
   - Whether the Shop page should be indexed
   - Current proof points ("250+ schools" etc.) and the ADA claim
   - Whether local SEO / Google Business Profile is paused or active
6. **Texas push:** support the Texas Edition pages (IMRA Cycle 2026) with internal links from the CTE hubs and one Texas-focused blog post.
7. **Measurement clean-up:** filter the Singapore bot traffic in GA4 and set up a key event for instructor sample / exam copy requests, so the next review can report leads, not just clicks. Top up Semrush API units so position tracking can be included.

---

## 5. Talking points for the meeting (for Andrew)

- Clicks from Google are **up 15.5% on last year** and **up 7.5% on last quarter**, through a full site rebuild.
- **CTR has nearly doubled** (0.84% to 1.58%): Mujo is showing up for more relevant searches.
- New AI titles and teacher-blog posts are already ranking on page one and bringing in traffic.
- The impressions drop is mostly a Google reporting change (Sept 2025) plus retired old URLs, not lost rankings.
- Next quarter's focus: turn high-visibility pages into clicks (titles/meta), launch Book schema, refresh the two curriculum pages, and get decisions on the five open site items.
