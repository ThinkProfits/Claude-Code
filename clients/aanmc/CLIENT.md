# AANMC (Association of Accredited Naturopathic Medical Colleges): client profile

> **Status:** DRAFT v0.1, 2026-10-06. Pending review by Francis.
> **Sources:** Slack (#aanmc C019H89BB8T, plus "aanmc" search across channels and DMs, 2025-10-06 → 2026-10-06), Drive (Updated Roadmap, Content Audit and Recommendations, Blog Topics sheet, Naturopathic Schools USA draft, Conversion Tracking Jan 2026, Website Audit sheet), Semrush (project 3439424 + domain ranks), GSC (`sc-domain:aanmc.org`, 2026-07-08 → 10-06), live site (aanmc.org, fetched 2026-10-06), repo.
> **Not checked:** Gmail (connector broken), BrightLocal (tool error, one attempt), Flowlu/Teamwork (not in scope of this run).
> **Related files:** [memory/aanmc-context.md](../../memory/aanmc-context.md) (Oct 2026 click-loss diagnosis and open questions; not duplicated here), [AANMC_Naturopathic-Doctor-Click-Recovery_2026-10.md](AANMC_Naturopathic-Doctor-Click-Recovery_2026-10.md), [keywords.md](keywords.md).
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Organisation**
- Non-profit association representing the accredited naturopathic medical colleges of North America. Founded 2001 (live /about/, 2026-10-06).
- Mission (paraphrased from /about/): help member schools deliver high-quality naturopathic medical education and research; advocate for outcomes-based education, public awareness, research and clinical training. Values line on site: "Collaboration. Excellence. Inclusivity."
- Website: https://aanmc.org
- Address: 1717 K Street NW, Suite 900, Washington, DC 20006 (live footer)
- Phone: 800-345-7454. Email: info@aanmc.org (Conversion Tracking sheet, Jan 2026)
- Timezone: Eastern (DC office) *confirm*; staff and schools span Pacific to Atlantic time.
- **Spelling on their site: US English** ("center", "program", "licensure"). Our internal docs stay Canadian; client-facing page copy should follow the client's US spelling *confirm with client* (open question in the click-recovery doc).

**Relationship**
- Long-standing client. Slack channel created 2020-08-26; Semrush tracked keywords were first added 2020-06-17.
- **Work was paused 2025-11-13** because AANMC was behind on payments (Andrew, on Shawn's instruction). Payment arrived 2026-02-18 ("Aanmc checks arrived", Shawn, group DM) and work resumed. *Confirm current account standing with Shawn.*
- **2026-09-26 incident:** three "Getting Started" cards on the site stopped displaying. Shawn had to step in; Francis fixed it the same day and apologised for the delay. Andrew separately noted (2026-10-03, #vision-plumbing) that WP Rocket "can sometimes cause problems with visuals" and cited AANMC as an example. *Confirm whether WP Rocket caused the card issue.*

**Client contacts** (business contacts only)
- **Stephanie** (events@aanmc.org): approvals contact per the #aanmc channel topic. *Confirm surname/title.*
- **Dr. Yanez:** second approver per the channel topic. *Confirm full name/title.*
- The client asked Andrew for the 2025 annual report on 2026-01-13 ("she asked today", for a next-day meeting); this is likely Stephanie *confirm*.
- The client owns a Drive folder "2026 TP Marketing Reports" (owner events@aanmc.org, created 2026-01-13) where our monthly reports land.

**ThinkProfits team**
- Andrew Silbernagel: account manager. Sends anything larger than small edits to the client.
- Francis Marc Uy: SEO lead
- Shawn Moore: owner; billing decisions
- Brittni Woodson: original channel creator and listed "TP Lead" in the channel topic (outdated; *confirm and update topic*).

**Stack**
- WordPress with **WPBakery** page builder and the "skilled" theme/plugin (asset paths in the 2025 crawl)
- Yoast SEO (schema graph per click-recovery doc)
- **Easy Testimonial plugin used for FAQ accordions** (added by Andrew 2026-01-24, same as Munro & Crawford). FAQ questions use H3 and schema enabled.
- Manual JSON-LD on school pages (Course, Event, FAQ, Organization)
- GTM + GA4 key events (see section 11), live chat (`chat_started`), Popup Maker
- WP Rocket *confirm* (see incident note above)
- Footer credits ThinkProfits for web design and SEO.
- **The client edits the site constantly.** Andrew (2026-05-23): avoid testing new WordPress 7.0 AI features on "super active clients like AANMC".

## 2. Services: what they offer, and what they don't

AANMC is not a clinic and not a school. It's the umbrella body that markets accredited ND education. Its "services" are information and referral to member schools.

**What they offer (audience: prospective ND students, career changers, pre-med advisers)**
- **School directory and profiles** for member campuses, each with Apply Now / Contact / Request Info CTAs that pass UTM-tagged traffic to the school.
- **Member campuses on the live site (2026-10-06):**
  1. Bastyr University, San Diego, CA
  2. Bastyr University, Seattle (Kenmore), WA
  3. CCNM Boucher Campus, Vancouver (New Westminster), BC
  4. CCNM Toronto Campus, Toronto, ON
  5. National University of Health Sciences (NUHS), Chicago (Lombard), IL
  6. National University of Natural Medicine (NUNM), Portland, OR
  7. Sonoran University of Health Sciences, Phoenix (Tempe), AZ
  8. Universidad Ana G. Méndez (UAGM), Gurabo, PR
- **University of Western States (UWS):** AANMC published a UWS school page in December 2025 and Andrew built its GTM events (Slack 2026-01-13). Our draft for /naturopathic-schools-usa/ lists UWS as "Candidate". **UWS is not in the live school list as of 2026-10-06.** *Confirm UWS status and whether its page is live.*
- **Request Information form** (/request-info/) and homepage form: the core lead.
- **Events:** virtual college fair, webinars, "CCNM in your town" style school events.
- **Career and education resources:** how to become an ND, curriculum, prerequisites, licensure map, income expectations, residencies, online-education explainer, ND vs MD comparison, 6 principles.
- **Consumer-health blog** (Naturopathic Kitchen, natural remedies, treatments). This drives most organic traffic but isn't the lead audience (section 5).
- **Ambassador programme** (Drive folder "AANMC Ambassador Agreements", client-owned, 2026-08) and a social media ambassador portal.
- Federal student aid updates for students (e.g. a 2025 post on loan changes).

**What they don't do**
- Don't provide patient care, appointments or referrals to individual NDs. "Find an ND" intent belongs to AANP (US) and CAND (Canada) directories.
- Don't accredit programmes. **CNME** accredits ND programmes; **NABNE** runs the NPLEX exams; state/provincial boards license. Never imply AANMC accredits or licenses.
- Don't offer online ND degrees. No accredited ND programme is fully online.
- Don't promote non-accredited "naturopath" programmes.

**Regulatory and accuracy sensitivities (hard)**
- **Health claims.** Naturopathic medicine is YMYL territory. Never write that a remedy cures, treats or prevents a disease. Frame as "research suggests", cite primary sources (NIH/NCCIH, PubMed, Cochrane), and include "talk to a licensed healthcare provider" guidance. Top-traffic pages (oil of oregano, natural antibiotics, natural ADHD treatments, dandruff, detox, adrenal support) need this most.
- **Scope of practice varies by jurisdiction.** Prescribing rights, title use ("naturopathic physician", "Dr.") and licensure differ by state/province. Always say so; don't generalise.
- **Licensed ND vs traditional naturopath.** Keep the distinction precise; it's central to AANMC's positioning.
- **Accreditation facts** (school count, statuses, NPLEX eligibility, licensed jurisdictions: 26 US jurisdictions and 7 provinces + 1 territory per our 2026 drafts *confirm*) must match across pages. AI answers already get school names and counts wrong (Content Audit doc).
- **Salary figures:** the site uses the AANMC 2020 Graduate Success and Compensation Study ($80,000–150,000 USD). Always date it. The client has newer survey data but worried about small sample sizes (Roadmap, Month 5). Our Feb/Mar 2026 USA-schools draft contains an **unsourced state-by-state salary table and tuition table**; don't publish without sources.
- **The AMA critique:** the AMA's ND-vs-physician page ranks for comparison queries. Our approach is factual and fair (acknowledge clinical-hour differences), never combative.

## 3. Target market and geography

**Primary audience:** prospective ND students (US and Canada), career changers into health care, pre-health advisers. Secondary: curious patients researching NDs (useful for trust and links, not the conversion audience).

**Geography**
- US national (GSC 2026-07-08 → 10-06: USA 82,066 of 105,780 clicks, 78%)
- Canada (7,980 clicks, 7.5%). BC and Ontario matter because of the two CCNM campuses.
- Puerto Rico (UAGM) is new; there's no Spanish-language content *confirm whether wanted*.
- Australia, India, UK and the Philippines also send traffic (consumer-health posts); low value.
- Andrew (2026-03-19): location-specific keywords are "not really" relevant for AANMC. The Roadmap (Month 5) still proposed city/state/province content if the client supplies local data.

## 4. Competitors

AANMC competes for attention, not enrolments: its competitors are other information sources ranking for ND-career and naturopathy queries.

**SERP competitors seen in our research** (Content Audit doc 2026-07-07; click-recovery doc 2026-10-02)
- **naturopathic.org (AANP):** owns "what is a naturopathic doctor" (#1 for "naturopathic doctor" in Semrush US). Partner organisation, so compete on content, not tone.
- **cnme.org:** authority for accredited-programme lists.
- **Member schools** (bastyr.edu, nunm.edu, nuhs.edu, sonoran.edu, ccnm.edu): rank for "how to become an ND" and ND-vs-MD content. They're members, so don't position against them.
- **Clinic blogs, Indeed, Learn.org, Rupa Health:** career and salary queries
- **getlicensemap.com, state boards, AANP regulated-states page:** licensure queries
- **AMA:** ND-vs-physician comparisons
- **WebMD, Cleveland Clinic, NIH/NCCIH:** holistic and consumer-health queries
- **Non-accredited online programmes** (e.g. Blue Marble University): "online naturopathic degree" queries
- **Local clinics in the map pack:** "naturopathic doctor" and "nd doctor" (patient intent)

**Semrush Position Tracking competitors:** not pulled. The API returned "unable to charge units" twice on 2026-10-06. *Pull from the Semrush UI.*

## 5. Current SEO status

**Semrush domain ranks (2026-10-06)**

| Database | Organic keywords | Est. organic traffic | Semrush Rank |
|---|---|---|---|
| US | 37,769 | 158,199 | 13,639 |
| US mobile | 6,496 | 130,131 | 12,401 |
| Canada | 7,266 | 14,403 | 18,277 |
| UK | 4,110 | 5,230 | 87,778 |
| Australia | 3,915 | 3,733 | 55,568 |

No paid keywords in any database.

**GSC, last 90 days (2026-07-08 → 2026-10-06)**
- **105,780 clicks, 36.6M impressions, 0.29% CTR, avg position 7.3**
- Daily clicks steady at ~1,000–1,500. Impressions dropped from ~500K/day in early September to ~220–300K/day from late September, while CTR rose to ~0.4–0.5%. The low-value "dandruff" and "bell pepper" impressions are probably fading *confirm in GSC*.
- Brand ("aanmc"): 202 clicks, position 1.0

**Top pages by clicks (90 days)**

| Page | Clicks | Impressions | CTR | Pos. |
|---|---|---|---|---|
| /natural-remedies/oil-of-oregano/ | 27,381 | 1.67M | 1.6% | 5.1 |
| /natural-remedies/natural-antibiotics/ | 8,994 | 576K | 1.6% | 4.6 |
| /naturopathic-medicine/dandruff-treatments/ | 5,124 | 12.78M | 0.04% | 8.9 |
| /natural-remedies/science-behind-sound-therapy/ | 4,572 | 412K | 1.1% | 6.3 |
| /naturopathic-schools/ | 2,990 | 78K | 3.8% | 5.7 |
| /natural-remedies/natural-adhd-treatments/ | 2,600 | 261K | 1.0% | 6.8 |
| /licensure/ | 1,485 | 70K | 2.1% | 6.6 |
| / (homepage) | 1,120 | 55K | 2.0% | 11.7 |
| /naturopathic-news/become-licensed-naturopathic-doctor/ | 1,114 | 80K | 1.4% | 7.6 |
| /comparing-nd-md-curricula/ | 1,086 | 154K | 0.7% | 6.2 |
| /holistic-medicine-schools/ | 748 | 98K | 0.8% | 14.1 |

**The core problem: traffic up, leads down** (Automated Report Reviews)
- 2026-07-09: GSC impressions +204.8% YoY, but key events -22.2% YoY and organic-attributed conversions -33.3% YoY
- 2026-08-07: sessions +22.1% YoY, key events -26.5% YoY, organic key events -35.9% YoY. More tracked keywords fell than rose (US 58 down / 23 up; Canada 63 / 24).
- 2026-09-09: organic sessions +53.6% YoY, organic key events -34% YoY, site CTR -44.5% YoY. Visibility up in US (+12.01%) and Canada (+12.64%); US 51 up / 28 down, Canada 57 up / 34 down.
- The growth is consumer-health content. Student-intent pages are flat or down.

**"Naturopathic doctor" click loss:** fully diagnosed in the click-recovery doc and memory (275 → 42 clicks Jul–Sep YoY; cannibalisation across 5+ URLs; local pack; weak metas; AI answers). Don't duplicate here.

**Technical/schema history**
- Expanded school-page schema (Course, Event, FAQ) rolled out from Sept 2025; school pages on the new template by 2025-10-08.
- Schema leaking onto the front end: /naturopathic-residencies (reported by the client 2026-06-09, fixed) and /naturopathic-schools/ccnm-boucher/ (2026-09-03, fixed). **Recurring issue: check after every schema edit.**
- Jan 2026: missing metas, orphaned pages and GSC indexing issues fixed; schema updated on blogs, video pages and school pages (Francis, 2026-01-13).
- The 2025 crawl shows ~2,300 URLs in the "Missing Meta Description" tab. *Confirm how many remain.*
- The Website Audit sheet has a 34-row schema plan (Organization/WebSite on home, AboutPage, ContactPage etc.).

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-06).

**What's tracked:** Semrush project 3439424 returned **one campaign with 155 keywords** (location/device not exposed by the API; volumes look US national). The report reviews mention separate **US and Canada** campaigns, and flagged the Canada report section as possibly duplicating US data (2026-08-07). *Confirm campaign setup in the Semrush UI.*

| Snapshot 2026-10-05 | Count |
|---|---|
| Ranking in top 100 | 153 of 155 |
| Position 1 | 91 |
| Top 3 | 107 |
| Top 10 | 136 |
| Ranking via AI Overview citation (not a blue link) | 70 |
| Moved up / down over 30 days | 22 / 41 |

**Movement, 2026-09-05 → 10-05**

| | Keyword | Position |
|---|---|---|
| Win | doctor of naturopathic medicine (4,400) | 14 → 1 |
| Win | naturopathy (33,100) | 25 → 13 |
| Win | natural doctor (2,400) | 17 → 8 |
| Loss | what is a naturopathic doctor (2,900) | 1 → 8 |
| Loss | is a naturopath a doctor (2,900) | 1 → 7 |
| Loss | nd school (210) | 1 → 35 |
| Loss | naturopathist (33,100) | 34 → 63 |
| Loss | naturopathic doctor (60,500) | 22 → 24 (-13 in the last 7 days) |

**Caveat:** 70 of the "rankings" are AI Overview citations, and Semrush counts them as position 1. A #1 here doesn't mean a #1 blue link or a click. Report AIO citations separately.

## 6. Current marketing programme and scope

**Recurring work**
- **SEO retainer:** technical/schema, on-page optimisation, content recommendations, keyword research. Hours are capped monthly (Roadmap: "September's hours are mostly used after our meeting"). *Confirm hours and retainer fee; not found.*
- **Blog topic research:** TP delivers keyword research + topic lists; Andrew edits and sends to the client.
  - June 2025, Oct 2025 (sent by email 2025-10-06) and March 2026 rounds
  - March 2026 brief: 4 Naturopathic Kitchen, 4 Career & Professional Development, 12 General Health / Treatments / Nutrition / Trending
  - *Confirm who writes the blogs now.* The Dec 2024 tab shows TP drafts "Sent to AANMC for content approval"; 2026 threads only show topic lists.
- **Page optimisation:** small edits and back-end work need no client review; **major rewrites need client review via Andrew** (Andrew, 2026-07-03).
- **Monthly report:** an automated HTML report around the 7th, plus an Automated Report Review thread in #aanmc that needs a "read" reply from Francis.
- **Annual report** prepared by Andrew in January (2025 report sent 2026-01-13).
- **Conversion tracking:** GTM events for every school page (see section 11).

**Roadmap** ("AANMC - Updated Roadmap", Sept 2025 → March 2026; Jan–Mar fleshed out 2026-01-24)
- Done ✅: UWS page build; Oct 2025 blog topic list; "How to Become an ND" refresh (Andrew updated it with client content 2026-01-24)
- Partly done: schema repairs, FAQ schema on key blogs, How-To schema list (13 URLs)
- Open: E-E-A-T outbound citations; Success Stories and Research page refresh (last alumni stories 2021); GBP enhancement; citations/NAP review; Bing Places; localised content research; Income Expectations refresh (blocked on survey data); key-page rewrites (drafts delivered 2026-03-18/19, see section 9); 6-month review and next 6-month calendar (Month 6, March 2026) *confirm whether done*.
- Roadmap content ideas: Naturopathic vs Functional Medicine; Holistic Health Certification vs ND Degree; student-debt and career-outlook content; localised content; **press releases** (TP could handle at extra cost).

**Pricing:** not found. *Confirm.*

**Project tracking:** new Teamwork tasklist created 2026-07-03 (tasklist 3774190).

## 7. PPC overview

- **No PPC managed by ThinkProfits.** Semrush shows 0 paid keywords in every database (2026-10-06), and there's no PPC discussion in #aanmc.
- If PPC is ever scoped, keep any budget as a range with stated assumptions. Lead value differs by school, so agree on conversion values first.

## 8. Content guidelines

**Approval flow**
- Major rewrites and new pages: TP drafts, then Andrew, then the client (Stephanie / Dr. Yanez via Google Doc approvals). **Never publish major changes without client sign-off.**
- Small edits, metas, schema, technical fixes: TP can do them directly (Andrew, 2026-07-03).
- FAQs: the client supplies answers where possible. Andrew: "you can suggest pages and questions, and I can get them to answer them" (2026-01-24).

**Voice:** informative, encouraging, student-focused, evidence-aware. US spelling on the site (*confirm*). No hype.

**Rules**
- Health content: no cure/treat claims, primary-source citations, "consult a licensed provider" guidance, visible reviewer and update date (E-E-A-T). Name a medical reviewer ND *(open question)*.
- Always distinguish licensed NDs from traditional naturopaths. Always say scope varies by jurisdiction.
- Don't recommend non-accredited programmes or imply online ND degrees lead to licensure.
- Don't position against member schools or partner bodies (AANP, CAND, CNME).
- Date every statistic (salary study 2020; tuition by academic year).
- Avoid "best" superlatives unless the page explains the criteria (e.g. accreditation).
- FAQ sections: Easy Testimonial accordion, H3 questions, schema on. Pages without visible FAQs get manual JSON-LD.
- **Cannibalisation check before new topics:** Andrew's March 2026 edits removed topics the site already ranks for. Andrew's topic-mix rule (2026-03-19): include a few each of poorly ranking keywords, competitor gaps, brand-new keywords, interlinkable not-yet-top-3 topics, low-KD intent matches, and high-volume stretch topics.
- **Consumer-health posts should link to student pages:** add a contextual link from high-traffic remedy posts to ND career/school pages (report review action item, July 2026).

## 9. Key priorities and strategic notes

**Open priorities (in rough order)**
1. **Lead tracking before content.** Three straight report reviews flag organic key events -26% to -36% YoY while traffic grows. Verify GA4 key events and GTM firing (Jan 2026 tracking list) before blaming content. GBP call/direction metrics read 0 for two years, which is likely a tracking gap.
2. **"Naturopathic doctor" click recovery:** execute the Oct 2026 plan (titles/metas first, then a new /what-is-a-naturopathic-doctor/ page). Status: deliverable written 2026-10-02; *confirm whether it's been sent to Andrew/the client.*
3. **Key-page rewrites awaiting approval:** drafts sent to Andrew 2026-03-18/19 for /naturopathic-schools-usa/, /naturopathic-medicine/, /comparing-nd-md-curricula/, /6-principles/ and /licensure/, plus the July 2026 Content Audit doc (7 pages). *Confirm client approval status; none found in Slack.*
4. **Monetise consumer-health traffic:** internal links and CTAs from oil-of-oregano / natural-antibiotics / ADHD / sound-therapy posts towards "become an ND" pages.
5. **De-prioritise or re-scope "dandruff treatment"** (12.8M impressions, 0.04% CTR). It drags site CTR down but brings few relevant visitors.
6. **Refresh stale pages:** Can I Take an Online ND Degree? (COVID-era, flagged Aug 2026); Income Expectations (2020 data); Success Stories (2021).
7. **Schema QA** after every change (two front-end leaks in 2026).
8. Fix the report template: Canada Position Tracking section duplicating US figures (Aug 2026 review).

**Strategic read**
- AANMC already wins most ND-education queries, often as the AI Overview source. The upside is converting visibility into Request Info submissions, not more rankings.
- Consumer-health content is a traffic engine with YMYL risk. Quality and sourcing matter more than volume.
- The client is hands-on with the site, so coordinate before plugin/theme changes.

## 10. Social profiles and other channels

- Footer links: Facebook, X (Twitter), YouTube, Instagram, LinkedIn, TikTok. Handles not captured *confirm*.
- YouTube/video pages (/videos/) carry webinars; they have video schema.
- GBP exists (the report tracks GBP interactions) *confirm the listing and address*. The Roadmap (Month 3) recommended GBP posts, FAQs and category review; there's no AANMC entry in the #gbp-post-approvals pipeline or the repo `gbp-handoffs/`.
- Ambassador programme (social media ambassador portal on site).
- The client manages its own social; TP recommended posting blogs to GBP and social as they publish (Roadmap).

## 11. Working rules and tool IDs

**Approvals**
- Major content: Andrew, then the client (Stephanie, events@aanmc.org / Dr. Yanez) via Google Doc approvals.
- Small/technical edits: TP direct.
- Billing holds: Shawn decides. Stop work if told the account is paused.

**Standing rules**
- No health cure/treat claims; cite primary sources
- Scope of practice varies by jurisdiction: always say so
- Licensed ND ≠ traditional naturopath
- Check schema renders cleanly (no front-end leak) after edits
- Don't test experimental plugins/AI features on this site
- Reply "read" to each Automated Report Review thread
- Don't repurpose /comparing-nd-md-curricula/ (memory)

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | Project **3439424** (one campaign returned via API, 155 keywords; mask `*.aanmc.org/*`). US/Canada campaign split *confirm in UI*. |
| GSC | `sc-domain:aanmc.org` (agency gsc MCP, siteOwner) |
| Slack | #aanmc **C019H89BB8T** (in the `seo-report-roadmap` scheduled task) |
| Teamwork | tasklist 3774190 (created 2026-07-03) |
| GBP automation key | none |
| Scheduled tasks | `seo-report-roadmap` (includes AANMC). `blog-masterlist-planning-run` **excludes** AANMC. |

**Drive**

| File | ID |
|---|---|
| AANMC - Updated Roadmap (6-month, Sept 2025 → Mar 2026) | `1gETY0hZhsDrwZzA8QKGiBZDkzq177u7A9GJcg8bK3v8` |
| AANMC Blog Topics: as of Oct 2025 (Mar 2026, Oct 2025, Jun 2025 keyword tabs) | `1Ydp2G3jlDl8itFFemf370xVI5rK-h2DHT_FUbQdhcss` |
| Content Audit and Recommendations - AANMC (2026-07-07, 7 pages) | `1D83mlOznB8miBuLb8FqO02ZJi5Mw_6DX6ZCN2mTXP-s` |
| Naturopathic Schools in the USA draft (2026-03-03) | `1qajgWDdsWsGV6uJDGDYA05flN1MBCpBbCwQSO0EBBWs` |
| Content suggestions doc (2026-03-03, not opened) | `15Jd7M404UXnqhT3_jZjxiT3pvOqSe-wx2Ml-aq4Oqwg` |
| How to Become an ND additions (2026-01-14) | `16NzHsu03CTiQOEdTXLiSJGoEqZ6KjwYvDDD7RzIiUMY` |
| AANMC Updated Conversion Tracking, Jan 2026 | `1WKJNx1iUR2gg1N2qjzd2FMxl5_dm8k7RS8GltetbKmM` |
| AANMC Conversion Tracking Review 2025 | `1BTIH-1oJy7hiW6y2c4X6YjgW-kuQUktD_gjm2OcSndk` |
| Website Audit - AANMC (crawl 2025-07-29, schema plan, broken links) | `1_UeD7EcoOTqoXy631Wf5Fxa44QJyqic_C0H-KYF_muM` |
| Page rewrite drafts (2026-03-18/19): schools-usa, naturopathic-medicine, ND-vs-MD, 6-principles, licensure | `1giMztivZn9-h9R4Pb5afCOGPXjuPtvvu`, `1LoPr32iAQn_egn96-mBCJ-sqHU5VgoPk`, `13MhOrcFwDZYOUUBjCegD7gWi7Ye4y8Sb`, `1y7567Q3XsQN8VgRICplXxwvG4Qn6NI2v`, `1jpUyx-2cwvuZNUjOKqGBLzZYNt8CriML` |
| Client folder: 2026 TP Marketing Reports (client-owned) | `1Zx3Tia3on5O6Dnwh48GsMlZchklRz8Hm` |

**Key GA4 events** (Jan 2026 list): `contact_form_submit`, `aanmc_home_form_submission`, `chat_started`, `aanmc-phone-click`, `aanmc-email-click`, plus per-school `*-apply-now-button`, `*-form-submit`, `*-phone-click`, `*-email-click` and `*_click` outbound events. Note the typo `bastyr-san-deigo-email-click` and mixed naming conventions.

## 12. Open items

**Waiting on the client**
- [ ] Answers to the click-recovery open questions (ND medical reviewer, newer salary data, patient-facing "verify an ND" section, US vs Canadian spelling, merging /naturopathic-schools-usa/). See memory.
- [ ] Approval status of the March 2026 page rewrites and the July 2026 Content Audit recommendations.
- [ ] UWS status (live page vs not in the school list) and whether UAGM needs schema/GTM events like the other schools.
- [ ] Income survey data release decision (Roadmap Month 5).
- [ ] New alumni/student success stories (last ones from 2021).
- [ ] FAQ answers for pages we suggest.

**Live site / SEO**
- [ ] Ship titles/metas from the click-recovery plan; build /what-is-a-naturopathic-doctor/ after approval.
- [ ] Audit GA4 key events and GTM firing (traffic-up / leads-down gap). Check GBP call/direction tracking.
- [ ] Refresh /can-earn-nd-degree-online/ (COVID-era content).
- [ ] Internal links from top consumer-health posts to student pages.
- [ ] Decide what to do with /naturopathic-medicine/dandruff-treatments/ (12.8M impressions, 0.04% CTR).
- [ ] Schema QA sweep for front-end leaks on all school pages.
- [ ] Confirm whether WP Rocket caused the 2026-09-26 "Getting Started" cards outage; add exclusions.

**Ops**
- [ ] Reply to the 2026-08-07 and 2026-09-07 Automated Report Review threads (follow-ups unanswered as of 2026-09-29).
- [ ] Confirm Semrush campaign structure (US + Canada?) and pull competitor visibility from the UI.
- [ ] Fix the Canada Position Tracking section in the monthly report template.
- [ ] Update the #aanmc channel topic (TP Lead still says Brittni).
- [ ] Confirm retainer, monthly hours and account standing after the Nov 2025 payment pause.
- [ ] Decide whether AANMC joins the GBP posting pipeline (Roadmap recommended GBP posts).

**Security:** none found. No credentials seen in Slack (#aanmc, 12 months) or in the Drive files opened.

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked (connector broken); approvals and client emails likely live there.
- BrightLocal: tool error, no data.
- Semrush: competitor visibility and campaign location/device not available (API "unable to charge units"); Canada campaign not found via API.
- Retainer fee, hours and contract not found.
- Client contact full names/titles not confirmed.
- The 2026-03-03 "content suggestions" doc (`15Jd7M40...`) and the Oct 2025 roadmap meeting notes weren't opened.
- No record of the 6-month review (Roadmap Month 6, March 2026) or the next roadmap.

**Conflicts**
- **UWS:** published as a member page (Dec 2025) and listed as "Candidate" in our draft, but absent from the live school list, which now includes UAGM.
- **Spelling:** our click-recovery doc uses Canadian spelling, but the client site is US English. Page copy should follow the client *confirm*.
- **"Naturopathic doctor" ranking:** GSC avg position 13.2 (Jul–Sep), Semrush tracked #24 and Semrush US organic #2 (click-recovery doc). Different measures (local pack, AIO, device, location); don't compare them directly.
- **Semrush "#1" counts include AI Overview citations** (70 keywords); report reviews may overstate blue-link rankings.
- **Our own drafts:** the USA-schools draft has unsourced salary-by-state and tuition tables plus "best naturopathic schools" wording; the Content Audit doc cites a clinic blog and Rupa Health as sources. Replace these with primary sources before client use.
- **Location content:** the Roadmap pushes localised content, but Andrew says location is "not really" relevant for AANMC.
