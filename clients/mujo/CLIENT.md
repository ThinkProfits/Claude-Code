# Mujo Learning Systems: client profile

> **Status:** DRAFT v0.1, 2026-10-07. Pending review by Francis.
> **Sources:** Slack (#mujo C019H2Q5HS6, private #think-mujo C07QWJWGSLD, DMs with Andrew / Brittni / Shawn, #thinkprofits-ppc-team), Drive (change orders, Ads 2025 sheets, Local Keyword Research, Institution Keywords Optimization, GSC Product Version Comparison, 404 Review), GSC (`sc-domain:mujo.com`, 90 days to 2026-10-06), live site (curl + WooCommerce Store API, 2026-10-07), repo (`clients/mujo/` CSVs).
> **Not checked:** Gmail (connector broken), BrightLocal (connector broken), Semrush keyword data (API units balance is zero, 2026-10-07; see section 11), Google Ads account, GA4.
> **Related files:** [keywords.md](keywords.md), `clients/mujo/mujo_redirection_import.csv`, `clients/mujo/www.mujo.com_http_5xx_server_errors_20260908.csv`. No `memory/mujo-*.md` file exists yet.
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Business**
- Independent education publisher: digital marketing, applied AI for business, business and marketing **textbooks, curriculum and courseware** for **higher education** (universities, colleges) and **high school CTE** (career and technical education) programs.
- Founded 2014 (live About page). CEO & Founder **Shawn Moore**; President **Alex Strauss**.
- Live site claims (homepage, 2026-10-07): 250+ schools, 34,000+ students, 325+ instructors, "100% Human Authored". Older ads (2025) say 210+ schools / 290+ teachers. *Confirm current figures before reusing.*
- Website: https://www.mujo.com
- Canada / head office: #602-1388 Homer St, Vancouver, BC V6B 6A7 (same building and suite number as ThinkProfits).
- USA office: #A13-5295 Lower Honoapiilani Rd, Lahaina, HI 96761.
- Toll-free support: 1.888.536.6856. Support form on /contact-us/ (24–48 hour reply promise).
- Two GBP listings appear in reporting: **Vancouver** and **Lahaina** (matches the two offices).

**Relationship**
- Long-standing client: Success Track docs go back to June 2015; ThinkProfits has run the website since at least 2017 (Website Training Guide, 2017).
- **Sister-company relationship** *confirm*: Shawn Moore is Mujo's CEO/founder and also holds a thinkprofits.com account; Brittni Woodson (Mujo) also posts from a thinkprofits.com Slack account. Treat Mujo as a client for scope and approvals regardless.

**Client contacts** (business only)
- **Brittni Woodson** (bwoodson@mujo.com; Slack U017GPS99U0): Mujo's marketing lead and **primary approver for content**. Builds pages herself in WordPress. Started in her current Mujo role around late 2025 ("since I started with Mujo", 2026-01-22). Formerly Brittni Chessa, TP Business Manager (2017 Success Track) *confirm*.
- **Shawn Moore** (shawn@mujo.com; Slack U019FGL4CR4): CEO & Founder. Weighs in on design/imagery and scope; wants shawn@mujo.com on meeting invites (2026-03-07).
- **Alex Strauss** (Slack "Alex", U0896UPDBSM): President; sales and international growth. Gets security summaries (2026-08-14).
- Channel topic lists "Client Lead: Shawn & Alex".

**ThinkProfits team**
- Andrew Silbernagel: account manager, PPC lead, does most technical/dev work on the site
- Francis Marc Uy: SEO lead
- Ian: developer (looped in for site/CWV work, Jan 2026) *confirm role*
- Clarissa: admin (change orders)

**Stack** (live site, 2026-10-07, unless noted)
- WordPress 7.1.2 on **Kinsta** (staging: `env-mujolearningsystem-mujo.kinsta.cloud`)
- WPBakery Page Builder, WP Rocket, **WooCommerce** (USD pricing), Gravity Forms + Gravity SMTP (set up Nov 2025)
- **Rank Math Pro** (replaced Yoast, Feb 2026; Rank Math writes robots.txt)
- WP Hide Login (custom login slug), 2FA plugin (added 2026-08-14), Simple History (60-day log)
- Courses/teacher platform: **Teachable** at courses.mujo.com ("Mujo Teacher Cloud")
- Zoho plugin (PageSense removed Dec 2025), Calendly bookings
- Kinsta bot protection raised to "block automations" (2026-09-30); AI crawlers still allowed
- **Easy MCP AI** (`wp-mujo` MCP) installed 2026-10-08, authenticating as user 7 (Francis, admin). Tested 2026-10-08: reads work; Rank Math schema/settings writable via `rankmath/v1` REST routes (untested write); post meta not REST-exposed. Details: `memory/mujo-context.md`
- WP 7.1.3 as of 2026-10-08. Also active: WPCode Lite, Simple Custom CSS and JS, CompressX (WebP/AVIF), Trustindex ("Widgets for Google Reviews")

## 2. Products: what they sell and don't

**What they sell** (WooCommerce Store API, 46 products, 2026-10-07)
- **High school CTE textbooks & courseware** (13 titles, from **US$59**): Website & E-commerce Strategy, Online Marketing Fundamentals, Foundations of Marketing, Social Media Marketing, Creating Digital Media Content, Sports & Entertainment Marketing, Fashion Marketing, AI Marketing Fundamentals, Influencer Marketing, Foundations of Artificial Intelligence, Entrepreneurship Fundamentals: In An AI World, Principles of Business: In An AI World, AI for Business.
- **Higher ed textbooks & courseware** (24 titles; listed at $0 with variable pricing up to ~$119, so pricing is set per edition/format): digital marketing (Digital Marketing, Principles of Marketing, Social Media Marketing, SEO, PPC, Strategic Web Design & E-Commerce, Big Data Analytics & Reporting, Writing Digital Media Content, Influencer Marketing, CRM Marketing Automation, PR Strategy & Communications, AI Marketing, UI/UX Design) and AI/business (AI Literacy, AI Literacy for Healthcare, AI Business Analytics, AI Accounting Principles, AI Sales Fundamentals, AI Project Management, AI for HR Management, AI for Entrepreneurs, AI Business Administration, AI Business Writing, Generative AI for Business, Prompt Engineering and LLMs).
- **Programs and bundles:** Full Digital Marketing Diploma, Full Applied AI for Business Diploma, 6- and 9-Course Certificate Programs, school-branded Digital Marketing and Applied AI for Business Certifications, CTE Full Digital Marketing Pathway class set (shop shows "From $1,194"; API price $2,655 *confirm*), Custom CTE Program.
- **Texas Edition** titles (new, pages published 2026-09-24): Foundations of Marketing (Texas Edition) and Entrepreneurship Fundamentals: In An AI World (Texas Edition), written to TEKS and submitted to Texas **IMRA Cycle 2026**. Pages: /texas/ and /texas/cte-funding/.
- **Formats:** student editions (print or e-book), teacher manuals, Teacher Resource Cloud, LMS integration. Lead magnet: **free instructor sample / exam copy**.
- **Purchase model:** schools and instructors adopt; students buy student editions. Per Andrew's GSC analysis (2026-02-12), student editions drive 85% of product-page clicks and 87% of impressions.

**What they don't sell / don't claim** *confirm each*
- Not an LMS vendor: they integrate with LMSs (Canvas etc.) and host teacher resources on Teachable.
- Not K–8: catalogue is high school (CTE, grades 10–12 per our keyword sheet) and post-secondary.
- **No AI-written content:** "100% Human Authored" is a brand promise (Shawn, 2026-04-30: AI images OK on the site, but "it's the book content statement we stand by"). Never position anything as AI-generated.
- Keyword-sheet terms that imply offerings not on the site (CPA continuing education, corporate training, MBA electives, trade/vocational schools): **don't target until the client confirms** (see keywords.md section 4).

**Regulatory / claims**
- Texas IMRA/TEKS alignment is a formal claim; only use it for the two Texas Edition titles.
- Ads (2025) claim "ADA Compliant" and "5-Star Rated By Teachers/Professors". *Confirm substantiation before reusing.*
- Student-facing products: keep privacy and data claims to what the client provides.

## 3. Target market and geography

**Buyers:** high school CTE teachers, CTE directors and instructional-materials coordinators, Education Service Centers (Texas); university/college professors, instructors, department heads, curriculum directors.

**Markets**
- **USA is the main market.** GSC, 90 days to 2026-10-06: USA 1,049 clicks (65%) and 64,146 impressions; Canada 154 clicks (10%); India 61; then Pakistan, Philippines, Hong Kong, UK, South Africa.
- High school ads run **USA only**; higher ed ads run **Canada & USA** (Ads 2025 sheet).
- Semrush tracking runs separate **USA** and **Canada** campaigns (monthly report reviews, May–Sept 2026).
- **New focus: Texas** (IMRA Cycle 2026, Texas pages, Brittni uploading Texas content Aug 2026).

**Spelling and market conventions:** the site declares `lang="en-CA"` but the copy is **US English** ("center", "program", CTE/TEKS terminology) and prices are in **USD**. Write mujo.com copy in US English unless Brittni says otherwise *confirm*; our internal docs stay Canadian English. The `en-CA` declaration is worth fixing to `en-US` (or leaving, if Canada is a deliberate signal) *confirm*.

## 4. Competitors

**From Semrush tracking** (Automated Report Review, 2026-08-08): mujo.com leads **McGraw Hill, Cengage and Pearson** in visibility on the tracked set, with 26 US keywords in the top 3.

**Likely CTE / curriculum competitors** (not tracked; *confirm with client*): Goodheart-Willcox, MBA Research, iCEV, AES (Applied Educational Systems), Knowledge Matters (simulations), VitalSource (distribution, referenced in site code).

Competitor detail for this profile is thin because Semrush couldn't be queried (section 11). Pull `tracking_competitors_organic` for both campaigns once units are restored.

## 5. Current SEO status

**GSC, 90 days (2026-07-09 to 2026-10-06)**
- 1,606 clicks, 105,546 impressions, CTR 1.52%, average position 12.1.
- Average position improved from ~14–17 in July to ~8–10 in September.
- **Brand carries the clicks.** "mujo" (80 clicks, 10,768 impressions, CTR 0.7%), "mujo learning systems" (61), "mujo ai" (21 clicks, 4,032 impressions). The low CTR on "mujo" / "mujo ai" suggests a brand-name collision with other "Mujo" products *confirm*.
- The top 1,000 non-brand queries add up to only **77 clicks** on 13,496 impressions. Most non-brand demand is long-tail or anonymised.

**Top pages, 90 days**

| Page | Clicks | Impr. | Pos. |
|---|---|---|---|
| / | 233 | 19,464 | 6.1 |
| /high-school/digital-marketing-curriculum/ | 91 | 4,659 | 7.8 |
| /high-school/digital-marketing-textbooks/social-media-marketing/ | 79 | 2,555 | 8.4 |
| /teacher-blog/creative-lesson-planning-marketing/ | 77 | 3,015 | 13.9 |
| /higher-education/ai-textbooks/ | 53 | 2,300 | 9.0 |
| /shop/higher-ed/generative-ai-for-business-textbook/ | 40 | 580 | 8.3 |
| /high-school/business-textbooks/ai-for-business/ | 16 | **7,833** | 5.5 (CTR 0.2%) |

**Monthly report reviews** (automated, Slack #mujo)
- **May 2026** (posted 2026-06-26): GSC 568 clicks (+144.8% YoY), avg rank 10.35. Wins: "what is marketing in high school" #1, "social media marketing lesson plans" #1 (US); "marketing automation syllabus" #1, "high school marketing curriculum" #1 (CA). Tracking visibility fell: US -15.74 to 24.72%; CA -3.46 to 24.11%.
- **June 2026** (2026-07-08): Direct traffic +237% MoM to 72.8% of sessions; GSC clicks -21.8% MoM; slight position loss in both markets.
- **July 2026** (2026-08-08): GSC clicks +57.8% YoY, avg position 13.73; 26 US keywords in top 3.
- **August 2026** (2026-09-09): GSC clicks +37.3% MoM / +36.7% YoY, avg position 13.15. US tracking -2.75% visibility (22 down, 12 up); Canada +4.80% (14 up, 11 down).
- **GA4 is unreliable.** It shows ~89–90% YoY user drops that GSC contradicts, a June Direct-traffic spike, and **Singapore bot traffic** (about 3,800 users, ~78% of all users, 2026-08-25 to 09-21; 5-second sessions, zero conversions). **Don't quote GA4 YoY to the client until it's cleaned up.**

**Site migration:** a rebuilt site went **live 2026-06-12** (staging merged into live). Francis built the redirect map; Andrew fixed more redirects and built a GA4 404 exploration ("Mujo 404 Review | June 2026"). URL structure changed (e.g. `/digital-marketing-textbooks-for-high-schools/...` became `/high-school/digital-marketing-textbooks/...`).

**Known technical issues**
- **wp-login 500s:** the 5xx CSV (Semrush Site Audit, 2026-09-08) lists **42 URLs**, all `wp-login.php?redirect_to=<teacher-blog post>`, first seen 2026-07-01 to 2026-09-02 (most on 08-12 and 08-19). The companion redirect CSV maps each one to its blog post. The test URL still returned **500** on 2026-10-07. Andrew traced earlier 500s (Feb 2026) to WooCommerce crashing before WP Hide Login could serve a 404.
- **Duplicate product URLs (cannibalization):** each title has curriculum pages (`/high-school/...`, `/higher-education/...`) plus `/shop/...` product pages, and historically separate student / teacher-manual / resource-cloud products. Consolidation plan in "Mujo GSC Product Version Comparison" (Feb 2026). Outcome **unresolved** as of 2026-04-17 (WooCommerce variations can't handle per-variation quantities; Barn2 plugins considered).
- **Inconsistent HS / HE naming in titles and H1s** (Andrew, 2026-06-24). E.g. /foundations-of-marketing/ still has title "Foundations of Marketing | Mujo Learning Systems" and no "high school" in the H1 (2026-10-07). Francis sent suggested titles/H1s on 2026-07-03; whether they were applied is *confirm*.
- `http://mujo.com/` goes through two 301 hops (to https://mujo.com/, then https://www.mujo.com/).
- Core Web Vitals: mobile failing late 2025; Andrew raised performance from ~30 to ~75 (2026-01-21). PHP limit and threads raised by Brittni (Jan 2026).
- Broken videos and circular infographics on the digital marketing and applied AI curriculum pages (Brittni, 2026-09-09). Fix status *confirm*.
- robots.txt now blocks WooCommerce filter / add-to-cart parameters and the `tphotobot` scraper (2026-09-30).

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-07).

**What's tracked:** Semrush project **2160205** ("Mujo", www) runs a USA and a Canada campaign, but the API returned no campaign targets and then hit a **zero API-unit balance**, so the live tracked list couldn't be pulled. Projects **24450287** ("mujo.com") and **14590131** ("mujo.com (no www)") look like duplicates; consolidate them.

**Strongest non-brand positions (GSC, 90 days):** digital marketing curriculum high school (1.7), high school web design curriculum (4.6), ai textbooks (5.6), high school marketing textbook (5.5), foundations of marketing (5.5), artificial intelligence textbook (6.4).

**Biggest gaps:** "digital marketing teaching materials" (416 impressions, position 30), "digital marketing teacher manual" variants (~950 impressions combined, position 18–20), "digital marketing textbook" (position 26.5).

**Keyword rules**
- Every product/curriculum title and H1 should say **High School** or **Higher Education** (decision direction 2026-06-24; final pattern *confirm*).
- No "AI-generated" angles; content is 100% human authored.
- No superlatives ("best", "leading", "#1", "top") in our copy; the Institution Keywords sheet and old ads use them, so flag them.
- Target only products in section 2.

## 6. Current marketing programme and scope

**Recurring work**
- **SEO: 10 hours/month** (Brittni, 2026-01-22; Andrew's time logs). Hours regularly overrun (June–July 2026 migration work). Andrew suggested either billing more, skipping August work, or handing smaller items to Brittni (2026-06-24).
- **Ad hoc tech/dev and security** done by Andrew (hack clean-up, bot blocking, plugin swaps) and partly billed to the SEO hours *confirm*.
- **Schema** on new pages on request (e.g. Texas pages, 2026-09-24).
- **Reporting:** monthly PDF plus an automated report review in #mujo around the 7th–9th; Brittni asked for a monthly log of SEO work done (2026-01-15).
- **Local SEO** for the two GBPs: Shawn suggested pausing it (2026-06-18, "Maybe we pause that local SEO for Mujo and aloha"). Current status *confirm*.

**Content ownership:** Brittni writes and publishes most content herself. **She wants any TP content changes sent to her for approval first** (2026-01-22).

**Pricing**
- Change order 2025-04-08: resumed **PPC Silver at $699/month**; monthly total went from **$1,737 to $2,436**. The split of the $1,737 base isn't documented *confirm*.
- Earlier change order 2025-03-28 exists (not read). A time-tracking contract dated 2024-07-29 exists (PDF, not read).

**Project tracking:** Teamwork project **1146973** (created March 2026; Francis added in April 2026).

## 7. PPC overview

**Google Ads** (account "Mujo Learning Systems" in the TP MCC)
- Campaigns per the Ads 2025 sheet:
  - **TP - High School (USA):** General Digital Marketing, Niche Industry Marketing, Social Media & Content Creation, Web Design & E-commerce
  - **TP - Higher Ed (CAN & USA):** AI Literacy, Big Data & Analytics, Business & Sales, General Marketing, HR Management, PPC Advertising, Project Management & Accounting, SEO, Social Media & Influencer Marketing, Web Design & E-commerce, Writing & Communications
- All RSAs, "Excellent" strength. CTA: "Get A Free Teacher Exam Copy".
- **Final URLs in that sheet point to pre-migration paths**; check they resolve via 301 or update them.
- **Status unclear:** the Jul, Aug and Sep 2026 report reviews found **no PPC data** in the report (one paid session in July). The TLD placement-exclusion bot was still excluding placements for this account in Jan–Feb 2026. **Confirm whether campaigns are live, paused, or the reporting feed is broken.**
- May 2026 (report of 2026-06-26): e-commerce revenue $1.07K (+670.5% YoY), 9 purchases, top item AI for HRM textbook; meetings scheduled +71.4% YoY.
- Budget/spend: not found. Present any future budget as a range with assumptions.

## 8. Content guidelines

**Approval flow**
- **Brittni approves all content changes** before they go live (2026-01-22). Andrew runs bigger recommendations past Brittni rather than Francis editing directly (2026-06-24).
- Shawn has final say on imagery and brand positioning.

**Brand rules**
- **"100% Human Authored"** is the core claim. Prefer real photoshoot images over AI images; Andrew and Brittni strongly prefer no AI images at all (2026-04-30). Shawn is OK with AI images on the site but not AI-written content.
- Audience language: teachers, instructors, professors, CTE directors. Practical, career-focused, "always current, free updates".
- Use the live proof points (250+ schools / 34,000+ students / 325+ instructors) only after confirming them.
- US English on mujo.com *confirm*.

**Formatting / SEO conventions**
- Rank Math focus keyword on every page (Andrew, 2026-02-05: many pages lack one; Rank Math now tracks rankings and pulls GSC/GA4).
- Rank Math auto-generates image alt text (filename + keyword + site title) on the front end; manual alt text is lower priority.
- Blog lives at /teacher-blog/.

**Topics to avoid:** AI-written-content angles; products not in the catalogue; old trend posts that attract off-topic traffic ("2018 social media trends", "chupa chups logo").

## 9. Key priorities and strategic notes

1. **Security and access first.** Get Brittni a working admin login (locked out with "access denied" on reset links, Sept 2026), confirm 2FA is on for all admins, and clear the plaintext credentials in Drive (section 12).
2. **Fix the wp-login 500s** (42 URLs, still 500 on 2026-10-07) and confirm bot mitigations are holding.
3. **Clean GA4** (Singapore bot filter, Direct spike, YoY comparisons) so reports stop contradicting GSC.
4. **Product consolidation:** decide the student-edition-as-parent approach and kill the cannibalization between curriculum pages and /shop/ pages.
5. **Title/H1 standardisation** (HS / HE in every title) and Rank Math focus keywords site-wide.
6. **Texas push:** schema, internal links and keyword targets for the Texas pages (Texas CTE marketing curriculum, IMRA, CTE funding).
7. **Institution-type keywords** (university, community college, CTE pathway) into hub and textbook pages, per the March 2026 sheet, after cutting superlatives and unconfirmed offerings.
8. **PPC:** confirm status; fix final URLs post-migration.

**Strategic read**
- Organic is improving (GSC clicks up YoY, position ~9–10 in September) but is brand-heavy. Non-brand curriculum and textbook terms sit mostly on page 2.
- The scope is small (10 hours) and keeps getting consumed by security and dev fires. Flag overruns early.

## 10. Social profiles and other channels

- Facebook: facebook.com/MujoLearning (plus a Facebook group)
- Instagram: @mujolearning
- LinkedIn: linkedin.com/company/mujo-learning-systems (plus a LinkedIn group)
- YouTube: youtube.com/c/MujoLearning
- X: @MujoLearning
- Meta pixel on site.
- GBP: Vancouver and Lahaina. Vancouver interactions -48.3% YoY (May 2026); Lahaina interactions -26.5% YoY while impressions doubled (Aug 2026); 0 call clicks on both (July 2026).
- Social posting is not in our scope as far as found *confirm*.

## 11. Working rules and tool IDs

**Approvals**
- Content and on-page changes: Brittni.
- Strategy, imagery and budget: Shawn (and Alex for sales).

**Standing rules**
- Don't edit the live or staging site during Andrew's database merges (precedent: 2026-06-11).
- Log all hours to the Teamwork project.
- Never post passwords in Slack; use the password tool.
- Don't quote GA4 YoY figures until cleaned.
- No AI-written-content positioning.

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | **2160205** "Mujo" (www, position tracking: USA + Canada campaigns; main). Duplicates: **24450287** "mujo.com", **14590131** "mujo.com (no www)"; consolidate. API units were **zero on 2026-10-07**. |
| GSC | `sc-domain:mujo.com` (agency account has access) |
| Slack | #mujo C019H2Q5HS6 (public); #think-mujo C07QWJWGSLD (private, design/site build); report roadmap task watches C019H2Q5HS6 |
| Teamwork | project 1146973 |
| Kinsta | live + staging `env-mujolearningsystem-mujo.kinsta.cloud` |
| Teachable | courses.mujo.com |

**Drive**

| File | ID |
|---|---|
| Website Audit - Mujo (edited 2026-07-02; holds Francis's title/H1 suggestions *confirm*) | `1QfoYV1XEhjUGl0kBF_dHPbEgz9-xjZjoFW6Jzv3rg50` |
| Mujo_Institution_Keywords_Optimization.xlsx (2026-03-18) | `1fnAo8DF3_JHvVMIIPOfTkxmXL6QZrrb6` |
| Mujo GSC Product Version Comparison (2026-02 to 06) | `1FHQZwU3VAbv6_JnB62G5sBBUZ_mPMptmYOwvz32JHbs` |
| Mujo 404 Review, June 2026 | `1whHc1X3ZE20j27pajb7gxsd0i43cGnh-B1y1jjCfKjI` |
| Mujo - Working Sheet (work log, Jan 2026) | `19jenqcToGOeRN6jYsUKebDOTc_1wuaBj1FFVm4fJSsk` |
| Mujo, Local Keyword Research (2025-02) | `1L9HM18aJ_qOwNEMkhnKWzrTHUMSMe3R7Psyt4AuXm9M` |
| Mujo Ads 2025 | `1sFTBfmUtak1c5FbgJs9C2A_FAfnSnMiAAKTsLkk7_Js` |
| Mujo Silver Ads 2025 | `118xy4Fm96-9j7Oc9A6P1OrTWM8NctRxkYO4jW4Htb74` |
| Mujo - PPC Monthlies | `1HTSQ_A7Oi_I5GwhkTFmbUGfZKQdmfd5goOK_ZD88T9Q` |
| Change Order 2025-04-08 | `1ae6aqO8u2MM6gEoue778A4Dhx8UA5cW2RN5ZG-vH3kI` |
| Mujo Performance Review, July 2025 (not read) | `1qit6f2x-fZNdmcRifus8Qi3GaOt_7hhHNv56ipq7poU` |

## 12. Open items

**Security**
- [ ] **Plaintext credentials in Drive.** "Digital Marketing Password Manager Mujo Learning Systems" (3 copies: `1FblrvpOEQHQI0xu7NkV0Zz93pwhIkRSGRmnPmo0HZ1o`, `1orcB6Husf8A_WacQta3KjOY3qhSLek9JMx346LmwzRs`, `19s4a2OREtsToyKB0i-Nh6uXe8lATtH06`) holds WordPress admin, FTP, cPanel/WHM and Kinsta logins. "Mujo Social Media Usernames and Passwords.docx" (`1xKlgEZRk_nSPXGpYucXo9lA06MBhpH4M`) holds social logins. They're old (2016–2020), but **rotate anything still valid** (especially Kinsta and WP admin after the August breach), move them to the password manager and delete the files. Values not copied here.
- [ ] Confirm Brittni has a working admin login (reset links gave "access denied", 2026-09-12 to 09-22) and that 2FA is enforced for every admin.
- [ ] Follow up on the 2026-08-06 compromise. Anyone who ran the fake Cloudflare prompt should run a malware scan. Brute-force attempts were logged on Sept 3 and 9.
- [ ] Fix the wp-login 500s (42 URLs; still 500 on 2026-10-07). Decide whether the redirect CSV should be imported or the login endpoint should return a clean 404/403.
- [ ] Check that the Singapore bot traffic stopped after the 2026-09-30 changes (IP blocks, robots.txt, Kinsta "block automations").

**Waiting on the client**
- [ ] Product consolidation decision (variations vs product-options plugin vs status quo).
- [ ] Which title/H1 pattern for HS/HE pages (Francis's suggestions sent 2026-07-03).
- [ ] Confirm current proof points (schools/students/instructors) and the ADA claim.
- [ ] Confirm US English for site copy, and whether `lang="en-CA"` should change.
- [ ] Local SEO / GBP: paused or active?

**Site fixes**
- [ ] Broken videos and circular infographics on the curriculum pages (reported 2026-09-09).
- [ ] Rank Math focus keywords on all pages (from 2026-02-05).
- [ ] Remove the double redirect hop on `http://mujo.com/`.
- [ ] Schema on the Texas pages (requested 2026-09-24): confirm done.

**Ops**
- [ ] Confirm PPC status and fix the report's missing PPC section (flagged Jul, Aug, Sep 2026).
- [ ] Clean up GA4: bot filters, Direct spike, YoY comparisons.
- [ ] Restore Semrush API units, pull both tracking campaigns, and consolidate the duplicate projects 24450287 / 14590131.
- [ ] Send the monthly SEO work log Brittni asked for (2026-01-15).
- [ ] Create `memory/mujo-context.md` and add it to `memory/INDEX.md` once this profile is reviewed.

## 13. Gaps and conflicts

**Gaps**
- Gmail and BrightLocal not checked (connectors broken).
- Semrush: no tracked-keyword list, competitors or domain overview (API units at zero, 2026-10-07).
- Google Ads account, budgets and keyword lists not read.
- Current retainer split, current contract and SEO hourly rate not found.
- Website Audit - Mujo (3 MB), July 2025 Performance Review, March 2025 change order and 2024 time-tracking contract not read in full.

**Conflicts**
- **Proof points:** 210+ schools / 290+ teachers (2025 ads, March 2026 keyword sheet) vs 250+ / 325+ instructors (live site). Use the live figures once confirmed.
- **Language:** `lang="en-CA"` vs US English copy and USD pricing.
- **AI imagery:** Shawn OK with AI images; Andrew and Brittni prefer none given the "100% Human Authored" claim.
- **Class set price:** shop shows "From $1,194", Store API returns $2,655.
- **PPC:** paid via change order ($699/month, April 2025), but no PPC data in Jul–Sep 2026 reports.
- **Our own keyword sheet** (Institution Keywords, March 2026) uses superlatives ("leading", "definitive", "go-to") and names offerings not confirmed (CPA CE, corporate training, MBA, trade schools). Revise before use.
- **Brittni's role:** the 2017 Success Track lists her as TP Business Manager; she now acts as Mujo's marketing lead with a mujo.com email but a thinkprofits.com Slack identity.
