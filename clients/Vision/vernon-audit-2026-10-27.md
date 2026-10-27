# Vision: Vernon site-wide audit

> **Status:** Internal audit, 2026-10-27. For Francis and Andrew. Not client-facing (it names competitors).
> **Why:** the Oct 14 client meeting and the Oct 15 scrum made Vernon an expansion market (Kelowna stays #1; don't rework the whole site). Brent also named Vernon as a water main market on Oct 20. This audit covers everything Vernon across the site and every platform we can reach. Its actions are merged into [water-main-roadmap-2026-10-27.md](water-main-roadmap-2026-10-27.md).
> **Sources:**
> - Website: all 263 sitemap URLs crawled, plus wp-vision.
> - GSC (URL-prefix property) and GA4 (property 363625322).
> - Google Ads Keyword Planner, Vernon geo 1001972.
> - Live Google and Bing results, Google AI Mode and the public Vernon GBP listing, checked in the browser.
> - Directory searches.
> - The blog masterlist sheet (Vision tab).
> - Meeting notes: [meeting-2026-10-14-index.md](meeting-2026-10-14-index.md), [scrum-2026-10-15.md](scrum-2026-10-15.md).
>
> **Periods:**
> - Current: 2026-07-27 to 10-25.
> - Previous: the 90 days before that.
> - Last year (LY): 2025-07-27 to 10-25.
> - Keyword Planner: Oct 2025 to Sep 2026.
>
> **Not available:**
> - **Semrush:** no API units.
> - **BrightLocal:** invalid key, so no grids and no GBP Insights.
> - **gbp-audit API:** quota 0, so the GBP Q&A, services, secondary categories and service areas couldn't be read.
> - **CallRail native reports:** not accessible.
> - **Google Ads account:** not read.
> - **Apple Maps:** not checked.
>
> **Live results** were checked from outside the Okanagan with "vernon" in the query, so treat them as indicative. Google showed a CAPTCHA near the end of the competitor checks. It wasn't bypassed, and the remaining checks used Bing and direct site visits.
> **Spot-checked by hand:**
> - The canonical loop, the sitemap exclusion and the expired furnace promo are confirmed.
> - The 778-946-6884 number seen on the homepage is **not** an error. The raw HTML has only 250-470-9552. CallRail swaps the number for each visitor.

## Scorecard

| Area | State | One-line verdict |
|---|---|---|
| Google Maps (Vernon packs) | Poor | Not in any top-3 pack; Vernon GBP has **2 reviews** vs 247 to 2,900 for pack winners |
| Vernon GBP setup | Poor | Coldstream residential address, links to the Kelowna homepage, posts are Kelowna copy |
| Organic rankings | Fair, improving | Average position 31.5 to 17.6 YoY, but mostly page 2; 7 clicks in 90 days |
| Vernon pages (content) | Weak | 4 pages, generic copy, one stale with an expired promo; no AC, heat pump, drain or water line page |
| Technical | Broken in one key place | The Vernon hub canonicalises to a URL that redirects back to it and is missing from the sitemap |
| Internal linking | Weak | Footer and 11 links go through a redirect; about 20 service pages mention Vernon without linking |
| Citations | Missing | No Vernon listing on Yelp, BBB, YellowPages, HomeStars, Facebook or the Vernon Chamber; old "Vision Mechanical" listings live |
| AI answers | Absent | Google AI Mode names 5 to 6 Vernon companies, all from GBPs with lots of reviews; Vision isn't one |
| Measurement | Blind | GA4 can't attribute most calls to a city; Vernon GBP traffic is 21 sessions a quarter |
| Demand | Small but real | "plumber vernon" cluster about 260/mo (480 in Oct); Vernon demand is about 25–35% of Kelowna's |

## 1. Top findings, ranked by impact

| # | Finding | Fix | Owner | Fits package? |
|---|---|---|---|---|
| 1 | **The Vernon GBP is nearly invisible.** It has 2 reviews (5.0) against 727 on Kelowna. Google labels it "Plumber in British Columbia", not Vernon. It appears in the 20-result local finder for only 5 of 10 queries (#8 to #16), and never in a top-3 pack. The lowest review count among pack winners was 247. | Vernon review drive (section 5), fix the address, link and posts (findings 2 and 4) | Vision (reviews), TP (GBP) | Yes |
| 2 | **The Vernon GBP address is 25 Midland Dr, Coldstream V1B 3B7**, which looks like a residential street in Coldstream, a separate municipality. If it's a technician's home and customers aren't served there, Google's rules require a service-area listing with the address hidden. | Client decision: staffed location, or switch to service-area with the address hidden and Vernon plus nearby areas as service areas | Vision decides, TP updates | Yes |
| 3 | **Canonical loop on the Vernon hub.** `/vernon-plumbing-hvac/` sets its canonical to `/vernon-plumbing/`, which 301s back to the hub. Yoast leaves the hub out of `page-sitemap.xml`. Confirmed by hand. | Set the hub canonical to itself (Yoast advanced field) and confirm it's back in the sitemap | TP | Yes |
| 4 | **The Vernon GBP website link goes to the Kelowna-titled homepage** (`/?utm_campaign=gmb_vernon…`). All Vernon GBP visits land there: 21 sessions in 90 days, 0 tracked calls. | Point it to `/vernon-plumbing-hvac/` and keep the UTM | TP | Yes |
| 5 | **Vernon GBP posts are Kelowna posts.** The 4 posts from Oct 13 mention "Kelowna homes" and "Kelowna cold snaps", and the Aug 17 post is about Kelowna. The description says "over 30 years" while the brand now says 40. | Vernon-specific posts. Decide whether the Vernon profile gets its own slot in the posting automation (CLIENT.md section 10 open item) | TP | Yes, at a basic level. More volume is an add-on |
| 6 | **Visible NAP on the Vernon pages is Kelowna.** The pages show 250-470-9552, the Acland Rd Kelowna address and Kelowna reviews. The schema on 3 of 4 pages declares the Coldstream address and +1-236-599-6737, which **matches the GBP**, but neither appears anywhere a person can see it. | After decision 2: show the Vernon phone (GBP number, probably a CallRail number) and the address or service-area wording on the Vernon pages | TP after Vision decides | Yes |
| 7 | **Only 4 Vernon pages** (hub, emergency plumber, hot water, furnace). Nothing for AC, heat pump, drains, trenchless water line, Poly-B, boiler, gas, water treatment or leak detection. Competitors Fox, Vernon Air Conditioning and Air Tech have 30 to 70 Vernon-titled service pages. | Revamp the 4, then add Vernon pages in demand order (section 8) | Andrew committed to revamping the 3–4 pages (Oct 14); TP | Revamp yes; new pages partly add-on |
| 8 | **`/furnace-repair-vernon/` is stale** (last modified 2025-03-28). It still shows "Until June 30th 2025, Get Up To $150 Off When We Service Your Gas Appliances" with a "Claim Fortis Rebate" button, in heating season. Its schema provider points to an undefined @id, and it doesn't link to the hub. | Remove the promo now; rewrite in the 2026 furnace page layout | TP | Yes |
| 9 | **Internal links go through a redirect.** The sitewide footer "Vernon" link and 11 in-content links point to `/vernon-plumbing/` (a 301). About 20 Kelowna service pages say "We are based in Kelowna and Vernon" with no link. These include all the AC, heat pump, boiler, IAQ and trenchless pages. The homepage mentions Vernon twice with no link. | Repoint all links to the hub; add Vernon links from the matching service pages and the homepage | TP | Yes (internal links need no approval) |
| 10 | **The site contradicts itself about Vernon.** The FAQ says "Any outer areas do incur a travel charge such as Myra, Summerland, Vernon, Penticton…". The AC repair page says Vernon is "typically next-day". About 10 pages say Vision is "based in Kelowna and Vernon". | Client decision on travel charge and response time, then align the copy | Vision decides | Yes |
| 11 | **The Vernon pages compete with each other:** "plumber vernon" (the 260/mo head term) is split between the hub (#26) and the emergency page (#23). The hub outranks the furnace page on furnace queries. "Water heater repair vernon bc" is spread over 3 pages, and its average position fell from 12.8 to 27.6. | One page per intent: the hub targets "plumber vernon" / "plumbing and heating vernon"; service pages own their service; trim the hub's service paragraphs and link out instead | TP | Yes |
| 12 | **No Vernon citations.** None on Yelp, BBB, YellowPages, HomeStars, Facebook, Canada411 or the Vernon Chamber. Bing Places matches the GBP. Old "Vision Mechanical" listings are live on YellowPages (one at the outdated 310-2076 Enterprise Way address), the Kelowna Chamber (phone 250-861-3627) and Indeed. The Kelowna Yelp listing is 2.3 stars from 4 reviews and shows in Vernon Yelp categories. Cybo lists the Vernon location with (778) 404-3100. | Build Vernon citations once the NAP is settled; clean up the Vision Mechanical listings | TP | AEO add-on (off-site work) |

## 2. Technical

| Issue | Where | Detail | Fix |
|---|---|---|---|
| Canonical loop | /vernon-plumbing-hvac/ | Canonical `https://visionplumbingandheating.com/vernon-plumbing/` → that URL 301s to the hub. Probably a Yoast advanced-field override (not REST-visible, check in wp-admin) | Self-canonical |
| Hub missing from sitemap | page-sitemap.xml | Side effect of the canonical | Recheck after the fix; resubmit sitemap in GSC |
| Links through redirects | Footer + 11 pages | `/vernon-plumbing/` and `/vernon/` both 301 to the hub | Repoint to `/vernon-plumbing-hvac/` |
| Undefined schema reference | /furnace-repair-vernon/ | `provider` @id `/vernon-plumbing/#vernon-business` is defined nowhere; other Vernon pages use `/#vernon` | Use the `/#vernon` node |
| Zero-width space in title | /hot-water-heater-repair-vernon/ | "Hot Water Heater Repair Vernon[U+200B] \| …" | Retype the title |
| Old URL | /vernon-plumbing/ | Was the main Vernon URL in 2025 (11,111 impressions LY); now a redirect. Fine once nothing links to it | None beyond the link repoint |

## 3. The four Vernon pages

| Page | Words | Modified | Ranking highlights (GSC, current) | Problems |
|---|---|---|---|---|
| **/vernon-plumbing-hvac/** (hub, 29642) | ~670 | 2026-10-19 | 12 clicks in 90 days. "hvac company vernon" #12.6, "plumber vernon" #25.9, "vernon plumbing and heating" #6.1 (3 clicks). Gets "plumbing company" #5.9 and "plumbing services" #4.6 from people near Vernon | Canonical loop. Duplicated H3 "Vernon HVAC Services" and paragraph. IAQ copy lists "ventilation systems" (Vision doesn't do ventilation). Lists water mains but doesn't link to the trenchless page. Links only to the 3 Vernon child pages. Local content is a neighbourhood list only. Kelowna reviews widget |
| **/residential/emergency-plumber-vernon-bc/** (29444) | ~1,030 | 2026-10-19 | 5 clicks. "emergency plumber vernon" #5.7, "emergency plumber" #4.9 (near Vernon). Live check: #3 | About 23% copied word for word from the Kelowna emergency page. H3 typo "Will My Insurance Cover **Pluming** Repairs?". "over 37 years" (now 40). Grammar: "Vision Plumbing Heating Cooling prioritize". Two en dashes used as dashes. Links to the hub through the redirect |
| **/hot-water-heater-repair-vernon/** (29687) | ~695 | 2026-10-19 | 2 clicks. "water heater replacement vernon" #4.1. Live check: #4 for "hot water tank replacement vernon" | Zero-width space in title. Title says "Hot Water Heater Repair", H1 says "Hot Water Tank Repair". No tankless coverage. "over 30 years". Links to the hub through the redirect |
| **/furnace-repair-vernon/** (29631) | ~1,050 | **2025-03-28** | 2 clicks. "furnace repair vernon" #13.5. Hub outranks it on "furnace service" and "heating services" | **Expired June 2025 FortisBC promo.** 2023-era copy, Fahrenheit in the FAQ ("65F to 68F"), "over 30 years", H2 about maintenance over copy about repair, no heat pump or dual-fuel section, no link to the hub, broken schema provider |

**Kelowna comparison:** the 2026 Kelowna furnace repair page is ~2,010 words; the West Kelowna and Penticton town pages are ~1,130 to 1,155 words. The Vernon hub is ~670.

**What's missing everywhere:** a real local signal. There's no Vernon team or technician, no Vernon response time, no Vernon projects or reviews, nothing on Vernon or Coldstream water, climate or housing stock. The client said on Oct 14 that an HVAC tech and a plumber live in Vernon. That's the most credible local content available.

## 4. Internal linking

| Target | Links in today |
|---|---|
| Hub (direct URL) | 2 (/indoor-air-quality/, /sitemap/) |
| Hub (via the `/vernon-plumbing/` redirect) | Footer sitewide + 11 pages |
| /furnace-repair-vernon/ | 8 (3 Kelowna furnace pages, emergency furnace, furnace brands, hub, 1 blog, sitemap) |
| Emergency Vernon | 4 |
| Hot water Vernon | 3 |

**Pages that mention Vernon but link to no Vernon page:**
- The homepage.
- All AC pages (repair, install, maintenance) and both heat pump pages.
- The heating and cooling hub and the boiler page.
- Trenchless water main (6 mentions), leak detection, Poly-B, Kitec, drains, gas lines and water treatment.
- All commercial pages and the FAQ.
- 42 of 43 blog posts that mention Vernon.

**Main nav:** no town links, only About > Service Areas.

## 5. Google Business Profile and reviews

| Field | Vernon GBP | Kelowna GBP |
|---|---|---|
| Address | 25 Midland Dr, **Coldstream** V1B 3B7 | 2600 Acland Rd Unit 8, Kelowna |
| Phone | (236) 599-6737 (likely a CallRail number; confirm) | (778) 760-2926 (CallRail, per the Feb 2026 swap) |
| Website link | Homepage + `utm_campaign=gmb_vernon` | Homepage + `gmb` |
| Panel label | "Plumber in British Columbia" | "Plumber in Kelowna, British Columbia" |
| Rating / reviews | **5.0 / 2.** Most recent about 2 months ago; neither mentions Vernon or a service | 4.9 / 727 |
| Photos | 15 | n/a |
| Posts | Active, but all Kelowna copy (4 on Oct 13, offer Oct 9, Aug 17) | Same posts |
| Description | "…over 30 years…" | Mentions formerly Vision Mechanical |
| Website traffic (GA4, 90 days) | 21 sessions, 0 tracked calls | 588 sessions, 25 first-time calls |
| Not readable | Q&A, services list, secondary categories, service areas, Insights | |

**Review plan (from the Oct 14 meeting, checked against Google's rules):**
- **OK:** Ask Vernon-area customers to review the Vernon profile. Use the labelled Vernon link Brandi is setting up in Podium. Ask for honest detail ("mention the job and the town").
- **OK:** Past Vernon customers can be asked too.
- **Not OK:** Sending *all* review links to the Vernon profile for a while. That would get Kelowna customers reviewing a location they didn't use, which Google can treat as misleading and remove. Ask Vernon customers only.
- **Not OK:** Copy-pasted review text, or incentives (already ruled out in the meeting).
- **Target:** a review band, not a promise. Pack winners start around 250 reviews, which is a long-term goal. Getting into the local finder top 10 for the core terms is a realistic first marker.

## 6. Citations

| Platform | Vernon listing | Notes |
|---|---|---|
| Google | Yes | See section 5 |
| Bing Places | Yes, matches the GBP | Likely synced |
| Apple Maps | Unknown | Apple Business Connect was claimed Feb 2026 via clientcare@; check for a Vernon location |
| Yelp | No | Kelowna listing 2.3 stars / 4 reviews shows in Vernon categories |
| BBB | No | Kelowna A+ profile shows in Vernon categories |
| YellowPages.ca | No | Three "Vision Mechanical" listings, one at the outdated 310-2076 Enterprise Way |
| HomeStars | No (BC) | |
| Facebook | No Vernon page | Main page 7.9K followers |
| Vernon Chamber | No | Competitor Bee's Knees is a member |
| Kelowna Chamber | Kelowna | "Vision Mechanical Ltd.", phone 250-861-3627 |
| Cybo (aggregator) | Yes | Phone (778) 404-3100, mismatched |

Fix the NAP decision first (section 5, finding 2), then build listings, or the same mismatches get copied everywhere. BrightLocal Citation Tracker would speed this up once the API key works.

## 7. Search data

**GSC, queries containing "vernon"**

| Period | Clicks | Impressions | Avg position |
|---|---|---|---|
| Current | 7 | 6,503 | 17.6 |
| Previous | 4 | 8,022 | 17.6 |
| LY | 0 | 13,376 | 31.5 |

- **Rankings have improved but traffic hasn't followed.** AC/HVAC Vernon terms went from about #50–80 to #13–25. That's page 2, which in this market gets almost no clicks.
- **Impressions on Vernon AC/HVAC terms look inflated.** "hvac company vernon" shows 518 impressions a quarter against about 10 searches a month in Keyword Planner, and 68% of impressions are desktop. Likely rank trackers. Judge by clicks and positions.
- **Kelowna pages ranking for Vernon terms:** about 2,600 impressions LY, about 30 now. Fixed.
- **Implicit-local wins:** people near Vernon searching without the town see the Vernon pages high for "emergency plumber" (#4.9), "plumbing services" (#4.6), "plumbing company" (#5.9) and "water heater repair" (#8.1). The Vernon GBP URL ranks #1–3 in the local pack for "plumbing and heating", "furnace repair" and "heat pump installation" near Vernon. Those clicks go to the Kelowna homepage.

**GA4**

| | Vernon area, current | Previous | LY |
|---|---|---|---|
| Sessions | 89 | 95 | 366 |
| Organic search sessions | 64 | 63 | 40 |
| Paid (search + display + video) | 10 | 17 | 315 |
| Attributable calls | 1 | 5 | 7 |

- **Vernon is 2.4% of Canadian sessions,** against Kelowna 37.6% and West Kelowna 7.0%.
- **The drop since LY is paid traffic,** not organic. Organic from Vernon is up 60%.
- **Calls can't be counted by city in GA4.** About 1,010 of roughly 1,220 call events have no source or city. Counting Vernon calls needs CallRail itself or the Vernon GBP number tracked as its own source.
- **Most Vernon visitors land on the homepage** (39 of 89). The four Vernon pages together got about 24 sessions from all cities in 90 days.

**Keyword Planner, Vernon geo (avg monthly)**

| Keyword | Searches | Top-of-page bid |
|---|---|---|
| plumber vernon (cluster) | 260 (480 in Oct) | $20–74 |
| plumber (no town) | 90 | $6–35 |
| hvac vernon | 70 | $17–104 |
| plumbers near me | 70 | $12–58 |
| plumbing and heating vernon | 50 | $17–60 |
| furnace repair vernon | 30 (70 in Oct) | $12–72 |
| hot water tank (no town) | 30 | $4–18 |
| emergency plumber vernon, air conditioning vernon, ac repair vernon | 10 each | |
| heat pump, hot water tank, drain cleaning, boiler, gas fitter, Poly-B, water line + vernon | 0 | |

- **Vernon is about 25–35% of Kelowna's demand** on core terms ("plumber kelowna" is about 1,000/mo).
- "Duct cleaning vernon" gets 70/mo, but Vision doesn't do ducts. Skip it.
- "Vernon air conditioning" (140/mo) is mostly a competitor's brand name.

## 8. Competitors

| Competitor | GBP | Vernon address | Site | What wins for them |
|---|---|---|---|---|
| Vernon Air Conditioning, Plumbing & Electrical | 5.0 / 818, plus a 2nd GBP 5.0 / 41 | Kalamalka Lake Rd | ~30 Vernon service pages | Exact-match name, #1 in almost every pack, first in AI Mode answers |
| Fox Plumbing Heating Cooling Electrical | 4.7 / 2.9K | Kosmina Rd (also Kamloops, Kelowna) | Very granular repair/install/maintain pages per service, "[Service] in Vernon, BC" titles | Ranks organically for nearly every service; has a water line page |
| Bee's Knees | 4.6 / 750 | Vernon | ~30 service pages incl. water main, Poly-B repiping | #1 pack for "water line replacement vernon"; Vernon Chamber member |
| TruFinity | 4.9 / 247 | Vernon | Hubs + city pages incl. /service-areas/vernon/ | Multi-city like Vision, yet in 4 of 10 packs with 247 reviews |
| Air Tech | 4.9 / 410 | 25 Ave, Vernon | ~70 service pages | Vernon firm that expanded into Kelowna, the mirror image of Vision; in both AI Mode answers |
| Applewood | 4.8 / 696 | Kalamalka Lake Rd | Thin | #1 organic for furnace and AC queries anyway |
| Xced, Eagle Rock (Armstrong) | 78 / 103 reviews | Vernon / Armstrong | Very thin | Named in AI Mode and Facebook "Vernon Rant and Rave" threads |

**Pattern:** in Vernon, reviews and a real local address beat content depth. Thin sites with Vernon addresses and hundreds of reviews outrank deep sites. Content still matters for organic, where Fox and Vernon AC win with one page per service.

## 9. AI answers

- **No classic AI Overview rendered** for any of the 12 queries.
- **Google AI Mode:**
  - "Best plumber in vernon bc": Vernon Air Conditioning, Xced, Fox, Air Tech, S.P. Seymour, Bertelsen.
  - "Best hvac company vernon": Vernon AC, Air Tech, Applewood, Double J, Fox.
  - Every source was a Google business profile. Vision isn't named.
- **What it means:** AI visibility in Vernon runs through the Vernon GBP (reviews, rating, a Vernon label). With 2 reviews and a Coldstream label, Vision doesn't qualify yet. The review drive and the GBP fixes are also the AI fixes.

## 10. Blog plan: topics to localise for Vernon

The Oct–Dec rows on the masterlist are all "Needs PM Review" and none is live yet.

| Month | Topic | Suggestion |
|---|---|---|
| Oct | Signs It's Time to Repipe Your Kelowna Home | Make it Vernon. Same 1980s–90s Poly-B housing stock; ties into the water line work |
| Nov | How to Lower Your Gas Bill This Winter in the Okanagan | "Kelowna and Vernon" framing; Vernon is colder. No rebate paperwork, no More Rewards |
| Dec | Winterizing a Vacant or Seasonal Okanagan Property | Strong Vernon fit: Predator Ridge, Silver Star, Okanagan Landing second homes |
| Dec | Keep Your Gas Meter and Appliance Vents Clear This Winter | North Okanagan snow angle |

The parked topics "AC Repair in Vernon" and "Emergency Plumber in Vernon" stay parked. They belong on Vernon service pages, not in the blog.

## 11. Decisions needed from Vision

1. **25 Midland Dr, Coldstream:** a staffed location customers can visit, or a technician's home? If it's a home, the GBP becomes a service-area business with the address hidden.
2. **Vernon phone number:** confirm (236) 599-6737 is the CallRail number for the Vernon GBP and can go on the Vernon pages.
3. **Travel charge and response time for Vernon:** the FAQ says there's a travel charge; the AC page says next-day. What's true now?
4. **Vernon team:** can we name the Vernon-based HVAC tech and plumber (first names, photos optional) on the Vernon pages?
5. **Photos:** Brent's Turtle Mountain water line photos (promised Oct 14), plus vans and staff at recognisable Vernon spots.
6. **Reviews:** confirm the labelled Vernon review link in Podium goes to Vernon customers only.

## 12. Prioritised actions

**Fix now (no client input needed, technical or factual):**
- [ ] Remove the expired June 2025 promo and button from /furnace-repair-vernon/
- [ ] Fix the hub canonical; confirm the hub returns to the sitemap; resubmit in GSC
- [ ] Repoint the footer and the 11 in-content links from `/vernon-plumbing/` to `/vernon-plumbing-hvac/`
- [ ] Point the Vernon GBP website link to `/vernon-plumbing-hvac/` (keep the UTM)
- [ ] Fix the typos and errors: "Pluming", the duplicate H3, "ventilation systems", the zero-width space, "30/37 years" to match the 40-year line, Fahrenheit, the furnace schema provider

**Next 30 days (after Vision answers section 11):**
- [ ] GBP address decision and NAP alignment (GBP, site visible NAP, schema)
- [ ] Vernon-specific GBP posts; decide on Vernon in the posting automation
- [ ] Vernon review drive (Vernon customers only)
- [ ] Revamp the 4 Vernon pages in the 2026 layout, with real local content, one intent per page, and links to every matching service page
- [ ] Add Vernon links from the homepage and the ~20 service pages that already mention Vernon
- [ ] Align the travel charge and response time copy
- [ ] Localise 2–4 upcoming blogs (section 10)
- [ ] Andrew: Vernon ad targeting and the separate Vernon campaign decision (Oct 14 action)

**30 to 90 days:**
- [ ] New Vernon pages in demand order: Vernon AC / heat pump (HVAC terms have the volume), then drain cleaning, then trenchless water line once a Vernon case study exists
- [ ] Vernon citations (Yelp, YellowPages, BBB, HomeStars, Vernon Chamber, Apple, Canada411); clean up the "Vision Mechanical" and Enterprise Way listings
- [ ] Vernon Chamber membership (client cost; competitor Bee's Knees is a member)
- [ ] Measurement: Vernon calls tracked as their own source in CallRail; BrightLocal grids for "plumber vernon" and "furnace repair vernon"; AI Mode prompts for Vernon added to AI Visibility tracking

**How we'll know it's working** (no promised positions):
- Vernon GBP review count
- Local finder position for "plumber vernon" and "furnace repair vernon"
- Clicks on Vernon queries
- Vernon GBP website sessions
- Calls on the Vernon number

## Raw data

The three working reports (website, search data, Maps/competitors) are in the session scratchpad, not the repo. Everything decision-relevant is in this file. Re-run the competitor ranks and grids once Semrush units and BrightLocal are restored.
