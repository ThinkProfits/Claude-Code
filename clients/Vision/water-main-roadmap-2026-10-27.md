# Vision: 90-day plan, water mains + Vernon

> **Status:** Internal draft, 2026-10-27. For Francis and Andrew. Not client-facing yet; once Andrew signs off it gets rewritten as Brent's plan (no competitor names, no em dashes).
> **Two workstreams, one plan:**
> - **A. Water main / trenchless** (Brent's 2026-10-20 email), across 7 towns.
> - **B. Vernon expansion**, all services (client meeting 2026-10-14, scrum 2026-10-15). Kelowna stays #1.
>
> They share the Vernon GBP, the Vernon pages and the review drive, so they're planned together. Each phase lists both.
> **Builds on:** [water-main-research-2026-10-27.md](water-main-research-2026-10-27.md) and [vernon-audit-2026-10-27.md](vernon-audit-2026-10-27.md). Covers organic, Maps/GBP and AI. Still separate: the technician photo/video checklist, the in-package vs add-on split (with the AEO recommendation), and Andrew's Ads section with budget ranges.
> **Scope reminder:** trenchless **water** only. Vision doesn't do trenchless sewer, so no sewer, CIPP sewer or septic content anywhere in this plan.
> **Start date assumed:** Mon 2026-11-02, if Brent approves this week. Weeks below count from there.

## The strategy in one paragraph

Vision already ranks #1 organically for the core term in Kelowna, Penticton and Vernon, but search volume is tiny and Vision is missing from every Maps 3-pack. So the plan isn't "rank for more keywords". It's: fix and deepen the one page that already ranks, give Google and AI tools real proof that Vision does this work in each town (projects, photos, reviews that say "water line"), get that proof onto the GBPs, and only then add town and material pages built from real jobs. No result can be promised; the leading indicators in section 6 tell us whether it's working.

**Vernon** follows the same logic. Organic rankings have climbed to page 2, but in Vernon the Maps packs and Google's AI answers go to companies with a Vernon address and hundreds of reviews. Vision's Vernon profile has 2 reviews, a Coldstream address, Kelowna posts and a link to the Kelowna homepage. So we fix the broken basics first (the hub's canonical loop, the expired promo, the profile link), then the profile and reviews. Only after that do we revamp the 4 Vernon pages and add new ones in demand order. The Vernon pages also carry the water line message for Vernon.

## Cannibalisation check (done 2026-10-27)

Searched the live site for water line, water main and trenchless content:
- **Only one page targets this topic:** `/trenchless-water-main-service/` (ID 32113).
- **Related pages:** `/water-leak-detection-kelowna/` (ID 28310); blog `/sewer-line-problems-in-the-okanagan/` (sewer, keep separate).
- **One blog post already exists** (missed in the first pass, found when GA4 was checked): `/trenchless-pipe-repair-explained/` (ID 36594, May 2026). It covers trenchless vs open trench, restoration cost ranges, methods (including CIPP) and warning signs. It brings in about 4 organic sessions a month and 1 call in 90 days. **No new blog repeats it.** It gets refreshed instead (Phase 1), and the hub's cost and signs sections link to it rather than duplicate it.
- **No other posts** on water line replacement price, materials, municipal ownership or Poly-B service lines.
- **Town pages already exist:** West Kelowna (33788), Penticton (33824), and 4 Vernon pages: the hub (29642), emergency plumber, hot water and furnace. **None exist** for Lake Country, Peachland or Summerland. The Vernon hub has a canonical loop and is missing from the sitemap (Vernon audit, section 2).
- **Vernon pages compete with each other** for "plumber vernon", furnace and water heater terms (Vernon audit, finding 11). Revamping them means one intent per page.
- **Poly-B:** 7 pages already compete (research section 2). Nothing new on Poly-B until those are consolidated.

## Phase 1: Fix the foundation (weeks 1–3)

Goal: make the existing page accurate and worth sending traffic to, and get tracking in place before any new work, so we can show Brent before-and-after numbers.

**Website**
- [ ] Fix the trenchless page errors (research section 5): remove the sewer claims and sewer FAQ, confirm or remove CIPP, delete the leftover condo and no-heat copy, confirm each claim (same day, 50 years, half the time).
- [ ] Expand the page into the hub for this service. Sections:
  - Signs your water service line is failing (leak between street and house, low pressure, wet patch in the yard, high bill)
  - Methods Vision uses (pipe bursting, pulling, directional boring) and when an open trench is still the right call
  - Materials Vision replaces (Poly-B, copper, galvanized, black poly), one short section each
  - What it costs and what drives the price (ranges from Vision, not guesses)
  - Who owns which part of the line (property line vs city side; check each municipality)
  - Process from first call to restored water
  - Towns served, each linking to its town page
  - FAQ written as direct answers AI tools can lift
- [ ] Refresh the trenchless blog post (ID 36594) to match: same CIPP and lifespan checks as the page, fix the "trenschlee" typo in the FAQ, and link it to the hub.
- [ ] Add Service schema with `areaServed` for all 7 towns, and FAQPage schema (through the existing FAQ schema process).
- [ ] Link to the hub from the plumbing services page, leak detection page, the 3 town pages and the main Poly-B page.

**Maps / GBP**
- [ ] Kelowna and Vernon GBPs: add "Trenchless water line replacement", "Water service line replacement" and "Water main repair" as services with descriptions.
- [ ] Check service areas on both GBPs cover all 7 towns.
- [ ] Decide whether the Vernon GBP joins the posting automation (open item in CLIENT.md section 10). Right now it carries copies of Kelowna posts.

**Vernon (workstream B): fix now, no client input needed**
- [ ] Remove the expired June 2025 FortisBC promo and "Claim Fortis Rebate" button from /furnace-repair-vernon/.
- [ ] Fix the hub canonical (self-canonical), confirm it's back in the sitemap, resubmit in GSC.
- [ ] Repoint the footer link and 11 in-content links from `/vernon-plumbing/` to `/vernon-plumbing-hvac/`.
- [ ] Point the Vernon GBP website link to `/vernon-plumbing-hvac/` (keep `utm_campaign=gmb_vernon`).
- [ ] Copy fixes on the Vernon pages: "Pluming", the duplicate H3, "ventilation systems", the zero-width space in the hot water title, "30/37 years", Fahrenheit, the furnace page schema provider.
- [ ] Send Vision the 6 decisions in Vernon audit section 11 (address, phone, travel charge, Vernon team, photos, review link).

**Tracking (needed before we can report anything per town)**
- [ ] Restore BrightLocal (invalid API key), then set up a Maps grid per town for "water line replacement" and an AI Visibility report (prompts in section 4).
- [ ] Top up Semrush API units and add per-town Position Tracking locations for the tracking additions in research section 4 (Andrew approves the list).
- [ ] Give the trenchless page and water line ads their own CallRail number or source tag, so calls can be counted separately from general plumbing.
- [ ] Confirm the CRM (Housecall Pro or ServiceM8) and ask Vision to tag water line jobs with town and lead source. This is what turns rankings into "jobs and revenue" for Brent.
- [ ] Vernon calls: confirm (236) 599-6737 is a CallRail number and report it as its own source. GA4 can't attribute most calls to a city.
- [ ] BrightLocal grids for "plumber vernon" and "furnace repair vernon" alongside the water line grids.

## Phase 2: Build proof and content (weeks 4–8)

Goal: give every town real evidence that Vision does underground water work there.

**Real-job content (the piece competitors don't have)**
- [ ] Start a case study format: town, pipe material, problem, method, how long, photos, short quote from the homeowner (with permission). One page per notable job, or a running "Recent water line projects" section on the hub.
- [ ] Target: 1–2 case studies a month, depending on how many jobs Vision does and how reliably techs capture photos ([technician checklist](water-line-job-capture-checklist.md)).
- [ ] Every case study also becomes a GBP post on the GBP closest to the job.

**Cost page (biggest organic gap)**
- [ ] New page or hub section: trenchless water line replacement cost in the Okanagan. GSC shows about 680 impressions a quarter on cost questions with no matching page. The existing blog post covers *restoration* costs saved; this one covers the *price of the job itself*. Keep them distinct and cross-linked. Needs real price ranges and cost drivers from Vision. If Vision won't publish ranges, we write the cost drivers and stop there; no invented numbers.
- [ ] Target keyword: trenchless water line replacement cost. Intent: commercial investigation.

**Blogs (from the existing 4 a month, not extra)**

Candidates, all checked against the site above. Each states its target keyword and intent when briefed.
1. Signs your main water line is leaking (water main leak; informational, symptom)
2. Poly-B water service lines in the Okanagan: what to check (poly b water line; informational). Only after Poly-B consolidation, and it must be about the underground line, not indoor repipes.
3. ~~Trenchless vs open trench~~ Dropped: `/trenchless-pipe-repair-explained/` already covers it. Refresh that post instead (Phase 1).
4. Who pays to fix a water line between the street and the house, by municipality (informational). Needs municipal sources checked per town.
5. Copper vs galvanized vs black poly service lines: how long each lasts (informational)

**Poly-B cleanup (unblocks item 2)**
- [ ] Pick one Poly-B page as the main target, merge or redirect the weak ones, and re-point internal links. Needs Andrew's sign-off on which page wins.

**Vernon (workstream B): after Vision answers the audit decisions**
- [ ] **Vernon GBP:** address decision (staffed location, or service-area with the address hidden), matching NAP on the site and in schema, Vernon-specific posts, add services (including the water line services from Phase 1).
- [ ] **Vernon review drive:** labelled Vernon link in Podium, sent to Vernon-area customers only. Not all customers: Kelowna customers reviewing the Vernon location risks removal. Honest detail ("the job and the town"), no scripts, no incentives.
- [ ] **Revamp the 4 Vernon pages** in the 2026 layout, one intent each. Andrew committed to this on Oct 14; agree who drafts.
  - Hub: owns "plumber vernon" and "plumbing and heating vernon".
  - Service pages: own their own service.
  - Real local content: the Vernon-based tech and plumber, response times, Vernon/Coldstream housing and water notes, Vernon projects and reviews.
  - Trenchless water line section on the hub (this replaces the Phase 3 Vernon row).
- [ ] **Internal links:** add Vernon links from the homepage and the ~20 service pages that already say "based in Kelowna and Vernon".
- [ ] **Align the copy** on travel charge and response time once Vision answers.
- [ ] **Blogs:** localise 2–4 of the Oct–Dec masterlist topics for Vernon (Vernon audit section 10). These use the existing quota, alongside the water line candidates above. Agree the split with Andrew; the repipe topic can serve both workstreams.

## Phase 3: Extend to every town (weeks 6–12)

Goal: town relevance for Maps, ads and AI "who serves X" answers. Order follows Brent's priorities and where Vision is weakest.

| Order | Town | Action | Why |
|---|---|---|---|
| 1 | West Kelowna | Add a water line section to the existing town page, plus a case study | Brent's #2 market; Vision not in organic top 10 or Maps |
| 2 | Vernon | Covered by the Vernon hub revamp (Phase 2, workstream B), plus a Vernon case study from the Turtle Mountain job if Brent sends the photos | Organic #1 already, but the ranking page is titled Kelowna; Maps is the gap |
| 3 | Penticton | Add a water line section to the existing town page | Organic #1; one strong local competitor page to beat |
| 4 | Lake Country | New town page, only once there's at least one real local job to show | No page today; organic #5–6 |
| 5 | Peachland | New town page, same condition | Not in organic results |
| 6 | Summerland | New town page, same condition | Organic about #3 |

- **No thin town pages.** Each new page needs local content (a real job, local water service notes, the municipality) or it risks being treated as a doorway page. If there isn't a local job yet, the town stays as a section on the hub.
- **No extra GBPs** unless Vision has a real staffed location in that town. A fake address risks suspending the main Kelowna profile, which is the one bringing in most calls. *Confirm with Andrew whether Vision has any other premises.*
- [x] Update CLIENT.md sections 3 and 12 (Penticton and Summerland are served; Vernon is an expansion market). Done 2026-10-27. Align PPC geo targeting with Andrew.

**Vernon (workstream B), weeks 6–12**
- [ ] New Vernon pages in demand order, each with real local content:
  - **Vernon AC / heat pump.** HVAC terms carry the volume: "hvac vernon" is 70/mo, and the hub currently soaks up the AC queries at page 2.
  - **Drain cleaning,** which Vision is absent from in Vernon.
  - **Water line,** once a Vernon case study exists.
- [ ] **Vernon citations,** after the NAP decision: Yelp, YellowPages, BBB, HomeStars, Vernon Chamber, Apple Business Connect, Canada411.
- [ ] **Clean up old listings:** the "Vision Mechanical" ones (YellowPages incl. the Enterprise Way address, Kelowna Chamber, Indeed) and the Cybo phone.
- [ ] **Suggest Vernon Chamber membership to Vision** (their cost).

## 4. AI search (runs across all phases)

AI tools pick up what third-party sites say about a business. Right now that's King Rooter for this category.

**On-site:** the hub FAQ, cost page and case studies are written to be quotable (direct answer first, then the detail). This is covered in Phases 1 and 2.

**Off-site:**
- [ ] **Review requests:** ask water line customers to mention what was done and where, for example "they replaced our water line in West Kelowna". Asking for honest detail is fine. Scripting reviews or offering incentives breaks Google's policy, so we don't do either. Set up through Podium.
- [ ] **HomeStars, Yelp, BBB, Facebook:** check the profiles exist, list water line replacement as a service, and include the 7 towns.
- [ ] **Local mentions:** supplier or manufacturer dealer listings, local news if Vision does a notable job, community sponsorships. Real ones only. No posting fake recommendations in Facebook groups or on Reddit.

**AI Visibility prompts to track** (BrightLocal, once the key is fixed; baseline before Phase 1 work goes live):
1. Who does trenchless water line replacement in Kelowna?
2. Best company to replace my water main in West Kelowna
3. Water line leak between street and house, Vernon, who should I call?
4. How much does trenchless water line replacement cost in the Okanagan?
5. Poly-B water service line replacement Kelowna
6. Underground water line replacement Penticton
7. Who replaces copper water lines in Lake Country?
8. Is trenchless water line replacement worth it?
9. Best plumber in Vernon BC
10. Best HVAC company in Vernon

Prompts 9 and 10 are the Vernon baseline. Google AI Mode currently names 5 to 6 Vernon companies for each, taken from their Google profiles, and Vision isn't among them.

## 5. Ads (Andrew)

Placeholder for Andrew's section. Points from the research that affect it:
- Penticton and Summerland are negatives and Peachland targeting was removed (2026-08-20); Brent now wants all three.
- Bids run about $6–44 a click (BC); volumes are about 10 searches a month per term in the Okanagan.
- "pipe bursting" needs sewer negatives.
- Landing page should be the fixed hub (Phase 1), not the current page.
- Budget as ranges with stated assumptions.
- **Vernon:** Andrew's Oct 14 actions are to rebalance ad weighting toward Vernon and evaluate a separate Vernon campaign. Vernon paid traffic fell from 315 sessions (LY quarter) to 10. "plumber vernon" bids are $20–74; "hvac vernon" $17–104. Landing pages should be the Vernon pages, not the homepage.

## 6. How we'll know it's working

No ranking or lead number is promised to Brent. We report these monthly, per town where the tool allows:

| Measure | Source | Baseline needed by |
|---|---|---|
| Maps grid position for "water line replacement" | BrightLocal grid per town | End of week 2 |
| Organic positions for the tracked water line terms | Semrush, per-town locations | End of week 2 |
| Impressions and clicks on the hub and cost page | GSC | Have it (2026-07-27 to 10-25) |
| Calls and forms from water line pages and ads | CallRail, GA4 | End of week 3 |
| Water line jobs and revenue by town and source | Housecall Pro or ServiceM8 | Depends on CRM access |
| Reviews mentioning water line work | GBP / BrightLocal Reputation Manager | End of week 2 |
| Mentions in AI answers for the 10 prompts | BrightLocal AI Visibility | End of week 2 |
| Vernon GBP review count (baseline 2) | GBP | Have it |
| Local finder position for "plumber vernon" and "furnace repair vernon" | BrightLocal grid | End of week 2 |
| Clicks on Vernon queries (baseline 7 a quarter) | GSC | Have it |
| Vernon GBP website sessions (baseline 21 a quarter) | GA4 `gmb_vernon` | Have it |
| Calls on the Vernon number | CallRail | End of week 3 |

## 7. What we need from Vision

- [ ] Confirm services: CIPP for water lines (yes or no), directional boring, which pipe materials, any job size limits.
- [ ] Confirm the claims on the current page (same day, 50 years, half the time).
- [ ] Price ranges for typical jobs, or a clear no on publishing them.
- [ ] Photos and short notes from recent water line jobs, with town (checklist coming).
- [ ] Permission process for using customer quotes and job addresses (street name only, never house numbers).
- [ ] CRM access or a monthly export of water line jobs by town and source.
- [ ] Any other staffed locations besides Kelowna and Vernon.
- [ ] **Vernon:** is 25 Midland Dr, Coldstream a staffed location or a technician's home?
- [ ] **Vernon:** confirm (236) 599-6737 is the Vernon number for the site.
- [ ] **Vernon:** what's true now on travel charge and response time?
- [ ] **Vernon:** can we name the Vernon-based tech and plumber?
- [ ] **Vernon:** the Turtle Mountain water line photos (promised Oct 14), plus vans and staff at Vernon landmarks.

## 8. Open questions for Andrew

- Which Poly-B page should win the consolidation?
- Does the Vernon GBP join the posting automation?
- Which pieces fit the current Plumbing Bundle and which need the AEO add-on: see [package split](water-main-package-split-2026-10-27.md) (recommends AEO Bronze).
- **Vernon pages:** you said on Oct 14 you'd revamp them. Do you draft, or do I draft for your edit?
- **Who is cross-posting Kelowna posts to the Vernon GBP?**
- **Should Vernon go into Brent's plan doc** or a separate note? It's in the merged draft for now, because the client raised it in the same week.
- Is Brent's 90-day expectation realistic given the volumes? Suggest framing the first 90 days as "foundation and proof", with Maps and AI movement measured from month 2.
