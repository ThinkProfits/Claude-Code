# MVP Athletic Supplies: client profile

> **Status:** DRAFT v0.1 (2026-10-07), pending review by Francis.
> **Sources:** Slack #mvp (C019AAJKPK8, read back to Dec 2023) and #gbp-post-approvals, Slack DMs, Drive, GSC, live site (Shopify storefront and `products.json`), repo (`gbp-handoffs/`, `scheduled-tasks/seo-report-roadmap/`).
> **Not checked:** Gmail and BrightLocal (connectors broken). Semrush returned "unable to charge units" / "API units balance is zero", so no live position-tracking, competitor or domain data was pulled. Gaps are listed in section 13.
> **Rule:** facts marked *confirm* are unverified. Don't use them in client-facing work until they're checked.

## 1. Client overview

**Business**
- **Name:** MVP Athletic Supplies Ltd. (site, GSC brand queries)
- **What they do:** family-owned specialty sporting goods retailer and team dealer for **baseball, softball (fastpitch and slowpitch), football and lacrosse**. Online store ships Canada-wide.
- **Founded:** 1973 by Harold "Hanch" Hancheroff (About page; "celebrating 50 years").
- **History:** first 30 years mostly supplied schools and institutions. Moved to New Westminster (Auckland St.) 1979–2007, now in Langley.
- **Website:** https://www.mvpathleticsupplies.com (www is canonical)
- **Address:** 20215 97th Avenue, Langley, BC V1M 4B9 (Langley Township)
- **Phones:** 604-525-8833 local, 1-800-910-1012 toll-free
- **Email:** customerservice@mvpathleticsupplies.com
- **Timezone:** Pacific

**Relationship**
- **Client since:** at least 2011 (Drive "MVP Ranking Report Aug 30", 2011). Older ranking reports (2005, 2008) also show up in MVP Drive searches. *Confirm the start date.*
- **Status: ACTIVE** (checked 2026-10-07). Evidence:
  - Andrew's last change requests in #mvp were 2026-09-18 and 2026-09-29.
  - GBP posts for `mvp_langley` are being drafted every week (latest drafts 2026-10-05 and 10-08).
  - Automated monthly report reviews were posted Jun–Sep 2026.
  - A new Teamwork tasklist was set up 2026-07-03.

**Client contacts** (from /pages/meet-our-team and Slack; business roles only)
- **Shawn Hancheroff:** President & Sales Manager
- **Matt Wilcott:** Vice President & Head Buyer
- **Sylvia Wilcott:** Accounts Payable. Long-standing approver for content and GBP (approved landing pages 2023; gave us GBP admin 2024-11-08).
- **Julia Oulton:** Social Media. Sends website and filter change requests.
- **Tyler Klassen:** Associate Buyer and **Lacrosse Lead**. Useful contact for lacrosse content.
- **Kodai Fujie:** glove break-in and relacing expert. A possible source for glove content.
- Who signs off on keywords now isn't clear. The 2026 keyword brief came from a female contact ("her requested prefixes"). *Confirm whether it was Sylvia or Julia.*

**ThinkProfits team**
- **Francis Marc Uy:** SEO lead
- **Andrew Silbernagel:** account manager and client contact. Also does Shopify page builds and filter edits.
- **Clarissa (Admin):** Teamwork projects and billing
- **Shawn Moore:** raised MVP site issues with Francis by email/DM (2026-09-24). *Confirm his role on the account.*
- **Past:** Brittni Woodson (former TP lead), Ian Yin (dev: banners, menus), Marc Pilon (2023–24 monthly reports)

**Stack**
- **Shopify** (shop ID 13813325, `mvp-athletic-supplies.myshopify.com`). Theme "BoostCommerce - 2026/05/15", with Boost search and filters.
- **About 1,426 published products** (`products.json`, 2026-10-07)
- **Uniform customizer** at /pages/customizer, built by a third party. Francis can't edit it from our side (DM, 2026-09-24).
- **Tracking:** GA4 `G-57C9MHRFW4`; Google Merchant Center tag `MC-JT8HVKX0ST` is on the site.
- **Project tracking:** Teamwork project 1069636 (2024–25), new tasklist 3774173 (July 2026 onward)

## 2. Products and services: what they sell and don't sell

**What they sell** (Shopify `product_type` counts, 2026-10-07)
- **Baseball and softball:**
  - gloves and mitts (254), bats (231 + 19 "Baseball Bats")
  - catcher's gear (61), batting gloves (32), batting helmets (8)
  - footwear (70), training and coaching aids (71)
  - field equipment and maintenance (39), bags (22), balls
- **Lacrosse:**
  - protective (99), shafts (62), heads (61), accessories (51)
  - women's sticks (25), complete sticks (13), goalie gear, mesh and string
- **Football:**
  - gloves (23), protective (16), cleats (10), balls (10)
  - helmet accessories (7), **helmets (3 only)**, apparel
  - flag football
- **Other:**
  - apparel and accessories, snacks and hydration, sunglasses (5)
  - Yeti (5), gift cards

**Top brands:** Rawlings (226), Easton (130), Mizuno (92), Warrior (66), Wilson (65), Maverik (53), Marucci (48), East Coast Dyes (47), StringKing (45), New Balance (39), All-Star, Under Armour, Louisville, STX, Victus, Battle, DeMarini, Nike, SKLZ, EvoShield, Loading Lacrosse (12), Jugs (10), Schutt (5). Vicis appears on 1 product.

**Services**
- Custom team uniforms and jerseys:
  - sublimated: about 3–4 weeks turnaround
  - tackle twill: about 4–6 weeks
  - (both counted from supplier approval)
- Custom company apparel; custom sports team apparel
- Association, team and corporate sales
- Glove break-in and relacing
- Sports customization (in-house seamstress)
- Warranty and defective-product handling

**What they don't sell** (no products found, 2026-10-07)
- **No hockey, basketball, soccer, volleyball or pickleball.** Those collection URLs return 404, and none of 1,426 products mention them.
- **Pickleball:** keyword research was done 2026-01-27, but there are **no pickleball products**. Don't target pickleball until MVP confirms it's stocking it.
- **Vicis:** only 1 product listed (football focus, Feb 2026). *Confirm range depth before targeting Vicis terms.*
- **Football helmets:** only 3 helmet SKUs online. Helmet terms are fine to target, but the collection is thin.
- **No international shipping.** Canada only (/pages/shipping).

**Shipping (Canada)**
- Flat rates by order value: $10 up to $300, $18 for $300–600, $26 for $600–1,000, $32 over $1,000.
- Ships within 24 hours by Expedited Post or Purolator.

**Regulatory:** none, apart from league bat-certification rules (USA Baseball, USSSA, BBCOR, BC Minor Baseball). /pages/british-columbia-minor-baseball-bat-rules covers these. Keep bat-rule content factual and dated.

## 3. Target market and geography

**Who they buy for**
- **B2C:** players and parents
- **B2B:** associations, teams, schools and companies (uniforms, team orders, corporate apparel)

**Where:** Canada-wide ecommerce plus the Langley storefront serving Metro Vancouver and the Fraser Valley.

**Search traffic (GSC, 90 days to 2026-10-07)**

| Country | Clicks | Impressions | Avg position |
|---|---|---|---|
| Canada | 28,571 | 700k | 9.0 |
| US | 1,313 | 231k | 22.8 |

They don't ship to the US, so **treat Canada as the only market.**

**GBP:** one location, Langley (`mvp_langley`).
- 4.8 rating, 428 reviews (Aug 2026 report).
- Sylvia doesn't want products added to GBP: "just go to the website" (2025-01-09).

**Rank tracking**
- Semrush project **2049385**, capped at **150 keywords**.
- Local modifiers (Vancouver, Langley, near me) were added for the store (2026-03-19).
- Tracked location and device weren't pulled (API out of units). *Confirm in the Semrush UI.*

## 4. Competitors

Semrush competitor data couldn't be pulled (units). From the automated report reviews:
- **baseballtown.ca:** the fastest-rising competitor, with visibility +8.55% (May 2026 report) and +3.76 pts (Jul 2026 report). It's closing the gap on baseball and softball terms.
- Other tracked competitors aren't recorded anywhere we can read. *Pull the Semrush competitor list.* A 2023-12-15 Slack note shows the report was once missing competitors and nobody knew the top 3 offhand.

**Brand note:** MVP is a retailer for the brands it sells. Rawlings, Easton, Marucci and others also rank for their own brand + "canada" terms. Position MVP as the Canadian place to buy them, never as the brand itself.

## 5. Current SEO status

**Semrush:** not available this run (API units at zero).

**Automated report reviews (Slack #mvp)**

| Report | GSC clicks | Tracked visibility | Notes |
|---|---|---|---|
| May 2026 | 14.47k (+18% YoY) | 25.36% | Avg rank 12.05; 37 keywords declined vs 24 improved |
| Jun 2026 | down 10.5% MoM | 18.68% (+8.02) | 48 in Top 3, 101 in Top 10. GA4 organic sessions down 35.5% YoY while organic key events up 21.2% (attribution conflict) |
| Jul 2026 | — | +1.78 pts | Organic key events down 37.9% MoM / 40.5% YoY. Ecommerce revenue up YoY |
| Aug 2026 | +14.8% YoY | 18.46% (−2.57) | GA4 organic sessions −16.5% MoM / −34.4% YoY; avg tracked position 28.06; 63 down vs 53 up |

**GSC (https://www.mvpathleticsupplies.com/, 2026-07-09 to 10-07)**
- About 30k clicks.
- **Roughly 40% of clicks are branded:** "mvp athletics" 4,467, "mvp sports" 2,212, "mvp" 1,988, "mvp langley" 1,540, plus variants.

**Top pages (90 days, by clicks)**

| Page | Clicks | Impressions | Avg position |
|---|---|---|---|
| / | 15,311 | 144k | 8.5 |
| /collections/pitching-machines | 424 | 15.1k | 7.3 |
| /collections/baseball-catchers-gear | 407 | 14.2k | 7.9 |
| /collections/lacrosse-helmets | 352 | 8.0k | 11.9 |
| /pages/british-columbia-minor-baseball-bat-rules (new Feb 2026) | 268 | 5.1k | 5.1 |
| Marucci Block Party bat product pages (3) | about 490 | about 4k | 5.5–6.4 |
| /pages/baseball-cleats | 147 | **27.5k** | 13.5 |
| /pages/fastpitch-slowpitch-bats | 134 | **21.4k** | 6.2 |
| /collections/baseball | 110 | **21.7k** | 2.5 |
| /collections/rawlings | 130 | 18.4k | 10.8 |

**Year over year (Jul–Oct 2026 vs 2025)**
- **/pages/fastpitch-slowpitch-bats:** clicks 429 → 138 (−68%) even though position improved 12.5 → 6.2. Investigate the SERP/CTR.
- **/collections/baseball-catchers-gear:** −30% clicks, impressions halved.
- **/collections/pitching-machines:** −28% clicks.
- **/collections/easton:** −69% clicks.
- **/collections/new-balance:** −56% clicks.
- **/collections/fastpitch-bats:** now redirects to /collections/fastpitch-softball-bats; old URL 0 impressions (was 30k). Check the new URL picked up the rankings.
- **/products/diamond-dry:** now 404 (had 96 clicks).
- **Winners:**
  - /collections/lacrosse-helmets: +152%
  - /pages/baseball-cleats: +231%
  - /collections/slowpitch-softball-bats: 3 → 168 clicks
  - homepage position: 16.5 → 8.5

**On-page (live, 2026-10-07)**
- Homepage title: "Baseball Equipment Store, Softball & Football Store in Canada | MVP". **Lacrosse is missing**, even though the client says it's their growth focus.
- Homepage H1: "Canada's premiere retailer…" ("premiere" should be "premier"; *flag before the next homepage edit*).
- **Every collection checked returns an empty description** (lacrosse, slowpitch-batting-gloves, cleats-turfshoes, bats, usssa-bats, fastpitch-softball-bats, protective-accessories, mouthguards). The long content was removed after the client complained (Sept 2026). *Confirm the intended 1–2 sentence intro isn't stored in a theme metafield instead.*
- **Andrew's question about thin homepage content** (2026-08-01): no reply found in Slack.

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-07).

**Tracking**
- Semrush project 2049385 tracks the client-approved "Final 150" list (approved 2026-03-26; a few under 150).
- A lacrosse brand / women's lacrosse revision was added later (asked 2026-04-25; Andrew updated Semrush, date *to confirm*).
- No live positions were pulled this run.

**Biggest wins** (reports)
- #1 for "slowpitch bats", "football equipment canada" and "baseball bats" (May 2026).
- New commercial rankings: "football equipment", "softball supplies", "football accessories" (Jun 2026).

**Quick wins** (GSC 90 days; page 1–2, low CTR)

| Query | Impressions | Avg position |
|---|---|---|
| "baseball cleats" | 6,547 | 11.9 |
| "rawlings canada" | 4,701 | 5.8 |
| "pitching machine" | 3,541 | 6.7 |
| "lacrosse stick" | 3,148 | 11.0 |
| "baseball bag" | 3,028 | 9.3 |
| "rawlings baseball gloves" | 3,047 | 9.0 |
| "bruce bolt batting gloves" | 2,573 | 11.0 |
| "baseball store" | 2,335 | 17.4 |
| "new balance cleats" | 2,113 | 7.7 |
| "franklin batting gloves" | 2,108 | 12.0 |

**Keyword rules**
- Commercial ("buying") terms get priority for the 150 slots over how-to terms.
- Lacrosse brands (ECD, STX, StringKing, Loading) and women's lacrosse are client priorities.
- No terms for sports or products they don't sell (pickleball, hockey and others).
- No "buy in the US" or international-shipping terms.

## 6. Current marketing programme and scope

- **SEO retainer:** monthly hours on an annual Teamwork project (renews in July). Hours and price aren't recorded in Slack. *Confirm the package and hours.*
  - **Upsell pitched 2026-02-24:** "SEO Silver", about $500/month more than current, with blogs and no keyword cap "within reason". **Outcome unknown.** Treat blogs as out of scope until confirmed.
- **Landing pages:** about 4 SEO landing pages a year.
  - In July 2025 Andrew thought only 4 of 8 owed pages (2023–25) had been delivered, and asked for keyword research on 4 more or rewrites of 3 existing pages. *Confirm what's still owed.*
  - Pages built Feb 2026 by Andrew: BC minor baseball bat rules, custom company apparel, custom sports team apparel.
- **Content approvals:** MVP now wants to **approve any substantial new content** before it goes live (2026-09-18). Drafts go in Google Docs, Andrew sends them to the client.
- **GBP posts:** Monday/Thursday for `mvp_langley` (Claude draft → Slack #gbp-post-approvals 👍 → handoff → Codex/Make publish).
- **Monthly reporting:** automated PDF report plus an "Automated Report Review" thread in #mvp that staff must confirm. Several Jul–Sep 2026 threads have unanswered follow-ups to Francis.
- **Web support:** TP handles Shopify tweaks for MVP (banners, menus, Boost filter edits, tags). These have historically come out of SEO hours ("will use up some of the December SEO hours", 2023-12-15).

## 7. PPC and Shopping overview

- **No Google Ads work found** in Slack or Drive, and no PPC team involvement. *Confirm.*
- A **Google Merchant Center** tag (`MC-JT8HVKX0ST`) is on the site, so free Shopping listings are probably active. Who manages Merchant Center isn't known. *Confirm.*
- Brittni suggested connecting GBP to Shopify for product indexing (2024-09-19). Sylvia later declined products on GBP (2025-01-09).

## 8. Content guidelines

**Collection pages (client rule, 2026-09-18)**
- Keep them to an **optimized heading plus a 1–2 sentence intro**. No long content, accordion or not. "Their main purpose is for users to quickly find things."
- Long, useful content goes on the **/pages/** guides instead. Example (Andrew, 2026-09-18):
  - Rewrite /pages/lacrosse-equipment with the "Box or Field?", "Youth and First-Time Players" and FAQ (6 Q&As) sections.
  - Move "Building a Stick" to /pages/lacrosse-sticks.
- Removed collection copy is saved in Drive docs (one doc per collection URL, folder `19AjLcAZFgMIliAKRDJqlAbFjIFopVXdN`, 2026-09-18) for reuse.

**Footwear collections:** MVP is splitting /collections/cleats-turfshoes into sport-specific collections (2026-09-29). Write Google Doc drafts for each once Andrew has the new collections ready.

**Approval:** all new or rewritten page content goes to the client as a Google Doc first. Don't publish directly.

**Voice**
- Knowledgeable, friendly, family-business tone; "treating customers and vendors like family" (About page).
- Talk like the staff who fit players for gear: practical fitting advice, league rules, sizing.
- Light wit is fine. No hype or superlatives.
- Canadian spelling.

**Content boundaries**
- No sports or products they don't stock.
- No international shipping claims.
- Don't promise stock levels or prices (online specials change often).
- Bat-rule content must cite the governing body and season.

**GBP images:** real product photos from MVP's Shopify CDN (via `/collections/<handle>/products.json`), at least 400×300. No AI imagery.

## 9. Key priorities and strategic notes

1. **Clear the September content backlog.**
   - Confirm collection pages carry the agreed 1–2 sentence intro (they currently show none).
   - Draft the /pages/lacrosse-equipment and /pages/lacrosse-sticks rewrites.
   - Move the other removed sections to suitable /pages/ guides.
   - Draft sport-specific footwear collection intros.
2. **Lacrosse growth is the client's stated focus** (2026-04-25):
   - Capture brand demand (ECD, STX, StringKing, Loading Lacrosse; Loading is a local company).
   - Build out women's lacrosse ("harder to find selection for").
   - Add "lacrosse" to the homepage title.
3. **Football refresh:** MVP planned to update its football section like the 2024 lacrosse overhaul (2026-02-26). Schutt and Vicis research was requested.
4. **Organic traffic decline in GA4** (−34% YoY sessions, Aug 2026) versus stable or growing GSC clicks.
   - Reconcile tracking (GA4 attribution) before calling it a real drop.
   - Investigate the CTR collapse on /pages/fastpitch-slowpitch-bats and the impression loss on catcher's gear.
5. **Homepage:** Andrew asked (2026-08-01) for a ranking check and possibly a Google Doc rewrite, because headings are thin. No answer was found.
6. **Competitor watch:** baseballtown.ca on baseball and softball terms.
7. **Fix redirects and 404s** from collection renames (fastpitch-bats → fastpitch-softball-bats, diamond-dry 404).

## 10. Social profiles and other channels

- **Facebook:** https://www.facebook.com/MVP-Athletic-Supplies-Ltd-134957666606202/
- **Instagram:** https://www.instagram.com/mvpathleticsupplies/
- Social is run in-house (Julia Oulton). It isn't in TP scope as far as we know.
- **Email marketing:** not in scope as far as we know. *Confirm.*

## 11. Working rules and tool IDs

**Approvals**
- Page content: Google Doc → Andrew → client (Sylvia, or *confirm* the current approver)
- GBP posts: 👍 in Slack #gbp-post-approvals
- Keyword list changes: sheet → Andrew → client approval → then Semrush (2026-02-24 process)

**Standing rules**
- Collection pages stay short.
- No products on GBP.
- Don't edit the third-party customizer.
- Keep the tracked list at 150 or fewer unless they upgrade.

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | **2049385** (position tracking, 150-keyword cap) |
| GSC | `https://www.mvpathleticsupplies.com/` (URL-prefix property; agency account has access) |
| GA4 | `G-57C9MHRFW4` |
| Merchant Center | `MC-JT8HVKX0ST` (tag on site) |
| Slack | #mvp (C019AAJKPK8) |
| Teamwork | project 1069636; tasklist 3774173 (from Jul 2026) |
| GBP automation key | `mvp_langley` |
| Shopify | shop 13813325 (`mvp-athletic-supplies.myshopify.com`) |

**Drive**
- Updated Keyword Research | MVP 2026: `10V1ZuJotAk-dunKhu8w6b4XumAG2ZonIkiE3iQwQnsI` (tabs: Final 150, COMPLETE FINAL LIST, Currently Tracked, Provided by MVP, Lacrosse Additions, Raw Data)
- MVP Worksheet (Keywords, Audits, and Other Tasks; incl. pickleball research): `1GPeOfhJn6EHIpvjhshMbF0uPo-Evqzb9KZVAFyl-hSg`
- MVP SEO Checklist (Oct 2020 onward, monthly reports): `1I1KOdILufSpk3cVhWpm8FP704Dt71CewemqEvzeEZEQ`
- Feb 2026 keyword research: `18NGNbCzmkjjqNlxkceB63esX4HiSpJTTKSEJU1G936s`
- Landing page ideas/outlines (2024): `1B0u8I7C9o-qUosu2QkirrV_14LWETpGksaUYOzEOthE`
- Removed collection content docs, folder: `19AjLcAZFgMIliAKRDJqlAbFjIFopVXdN`

## 12. Open items

- [ ] Confirm every collection page has the agreed optimized H1 + 1–2 sentence intro. The live descriptions are empty (2026-09-18 / 09-29 requests).
- [ ] Draft Google Doc rewrites: /pages/lacrosse-equipment (Box or Field?, Youth and First-Time Players, 6-question FAQ) and /pages/lacrosse-sticks ("Building a Stick") (2026-09-18).
- [ ] Draft intros for the new sport-specific footwear collections once Andrew creates them (2026-09-29).
- [ ] Reply to Andrew's homepage question: rankings, thin content, keyword headings (2026-08-01).
- [ ] Confirm the Jun, Jul and Aug 2026 Automated Report Review threads (follow-ups to Francis unanswered as of 2026-09-29).
- [ ] Reconcile the GA4 vs GSC organic discrepancy and check contact_form / email_click event tagging (Jul/Aug reports).
- [ ] Resolve Shopify access. Francis couldn't log in on 2026-09-16 ("is MVP shopify login changed recently?").
- [ ] Respond to Shawn Moore's emailed MVP issue (2026-09-24). It's tied to the third-party customizer, *confirm the issue.*
- [ ] Confirm the outcome of the SEO Silver upsell (2026-02-24) and what landing pages are still owed (2025-07-02).
- [ ] Log time in Teamwork tasklist 3774173 (logs were behind in 2025-06 and 2025-09).
- [ ] Check the fastpitch-bats redirect equity and the /products/diamond-dry 404.
- [ ] Pull the Semrush competitor list and current positions once units are restored.
- [ ] **Security:** no exposed credentials found. The Shopify Storefront API token in the page source is public by design and isn't a secret.

## 13. Gaps and conflicts

**Gaps**
- **Semrush:** no position tracking, competitors or domain overview. 4 `execute_report` calls returned 2 parameter-validation errors, "unable to charge units" and "API units balance is zero".
- **Gmail and BrightLocal** not checked, so contract, pricing, hours and the client email thread are unknown.
- **Retainer** package, hours and price not found.
- **Final 150 tab:** only the "COMPLETE FINAL LIST" tab (186 rows) could be exported as data. The exact Final 150 rows and the post-April lacrosse revision weren't readable.
- **No 2026 audit or success-track doc** found in Drive. Newest overview-type docs date from 2019–2020.
- **Merchant Center / Shopping** ownership is unknown.
- **Current keyword approver** at MVP is unknown (Sylvia vs Julia).

**Conflicts**
- **Homepage H1** says "Baseball, Softball, Football & Lacrosse", but the title tag drops lacrosse.
- **Visibility metrics** differ between reports (25.36% May, 18.68% Jun, 18.46% Aug). Likely the list change around May/June resets the baseline, so don't compare across it.
- **Client start date:** Drive has MVP ranking reports from 2011 and possibly 2005, and a 2014 "MVP Production Success Track". *Confirm.*
