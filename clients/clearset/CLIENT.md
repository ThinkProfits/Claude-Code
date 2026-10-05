# Clearset VAC Truck Services: client profile

> **Status:** DRAFT v0.1, 2026-10-06. Pending review by Francis.
> **Sources:** Slack (#clearset C04BXUMV0ES read back to 2024-05, #gbp-post-approvals, #thinkprofits-ppc-team, DMs), Drive (Success Track, Clearset Services doc, Website Audit sheet, Master Keyword sheet, City DKI Data, PPC checklist), Semrush (project 10336170 + CA organic), GSC (`https://clearsetvactruck.ca/`), live site (curl, 2026-10-06), repo (`clients/clearset/` drafts, `gbp-handoffs/`, `scheduled-tasks/`).
> **Not checked:** Gmail (connector auth error), BrightLocal (tool returned a malformed-result error). Semrush Position Tracking keyword data could not be pulled (see section 5).
> **Related files:** [keywords.md](keywords.md); drafts in this folder: `Clearset - Page Updates - Portable Sanitation.docx` (2026-10-06), `Clearset - New Pages - Coquitlam and Pitt Meadows.docx` (2026-09-04), `Clearset - Blog - Septic Repair Warning Signs.docx` (2026-09).
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Business**
- Legal name: Clearset Enterprises Ltd. Trading as **Clearset VAC Truck Services**.
- Family-owned vacuum truck company: septic, liquid waste, hydrovac, water hauling and rentals. "20+ years" in the industry (site and Success Track).
- Founder story (Success Track): Sean drove for Maple Leaf Disposal, bought his own truck, landed his old employer as his biggest contract, then branched out into residential and commercial work.
- Website: https://clearsetvactruck.ca (non-www, https). `clearset.ca` and `www.` redirect to it.
- Old domain: septictankpumpingservices.net. **It no longer resolves** (curl, 2026-10-06), so any old redirects are gone. *Confirm whether the domain lapsed.*
- Address: 880 Lougheed Hwy, Port Coquitlam, BC V3C 0B7 (new as of 2025-09-11). Service-area business; no public storefront.
- Phone: (778) 825-1032 (main; also the GBP number per Andrew, 2025-11-22). Email: info@clearset.ca
- Hours (live footer): Mon–Fri 8:30–7:00, Sat 10:00–5:00, Sun call. Site advertises a 24/7 emergency line.
- Timezone: Pacific

**Relationship**
- Client since **December 2022** (SEO and PPC both started Dec 2022; Slack channel created 2022-11-23).
- Triggers for joining: unresponsiveness from the previous agency, CT21 Analytics (Success Track).
- Pitched a blog package (2025-09-11) and an AEO package (2026-08). *Neither confirmed signed.*

**Client contacts**
- **Sean:** owner and client lead (sean@clearset.ca). Active and detail-oriented: he spots wrong images, wrong services and AI-answer gaps himself, and asks about results.

**ThinkProfits team**
- Andrew Silbernagel: TP lead (channel topic), account manager and PPC lead
- Francis Marc Uy: SEO lead
- Clarissa: admin (landing page drafts, reporting emails)

**Stack**
- WordPress on Kinsta, **Divi** builder, Yoast SEO
- FAQ schema: a header script turns any Divi accordion with the CSS class `tp-faq-accordion` into FAQPage schema automatically (Andrew, 2025-04-11). Use the class; don't hand-code FAQ schema.
- CallRail since 2025-11 (tracked numbers on GBP, site and ads differ)
- GA4 key event `footer_form_submission` (split from the contact form 2024-09-13 to fix double-counting)
- Instagram feed plugin
- CRM: QuickBooks (Success Track, 2022). *Confirm.*

## 2. Services: what they do and don't do

**What they do** (residential and commercial)
- **Septic:** septic tank pumping and cleaning, holding tank cleaning, pump chamber cleaning, septic system maintenance
- **Drain field / leach field rejuvenation:** line jetting, back flushing, hydrogen peroxide treatment and camera inspection. **If a physical replacement is needed they refer it to another company** (Slack, 2025-03-20).
- **Hydro flushing** = hydro jetting = line jetting. Top revenue generator (Success Track).
- **Hydrovac** = hydro excavation = daylighting. Also trenching, slot trenching, potholing, non-destructive digging (Slack, 2024-12-06 and 2025-05-21). Hot water services sit on the same page.
- **Line scoping / sewer camera inspection** (page built 2025)
- **Storm drain and catch basin cleaning**
- **Grease trap cleaning**
- **Lift station cleaning**
- **Trailer and RV pumping** (white, grey and black water; on-site)
- **Car wash pump-outs** (priced 2025-09)
- **Water hauling: NON-POTABLE ONLY** (pools, hot tubs, construction, cisterns, agriculture)
- **Water tote / IBC tank rentals** (1,000 L, water only; minimum 1 day, no maximum)
- **Portable toilet rentals** (construction-grade, mainly job sites; minimum 1 day, no maximum; weekly service included)
- **Well cleaning:** client asked to add it 2025-03-26 (removing sediment from underperforming wells). *Not on the site. Confirm status before writing about it.*

**Portable toilet specifics** (client, 2025-03-15)
- No sinks. Hand sanitizer dispenser included.
- ADA units and add-ons were removed from the page in April 2025 because they aren't offered.
- Toilet service area is narrower than the rest of the business: Port Coquitlam, Coquitlam, Anmore, Belcarra, Pitt Meadows, Maple Ridge, Surrey, Langley, Walnut Grove, Port Kells, Port Moody. *Confirm whether it has grown since March 2025.*

**What they don't do**
- **Potable (drinking) water.** Never. Raised 2024-09-18 and again 2026-09-11, when content we added was flagged by the client and had to be removed sitewide.
- **Septic inspections.** Only licensed plumbers / registered onsite wastewater practitioners can do these in BC (Slack, 2024-12-06; live FAQ).
- **Septic repairs and drain field replacement.** They pump and maintain; physical repairs go to another company.
- **Alberta.** They get calls from Alberta (2025-05-06) but don't serve it.
- Anything outside Chilliwack–Squamish (not "all of BC", corrected 2024-12-06).

**Starting prices** (client, 2025-09-11; *confirm current before quoting*)

| Service | Starting price | Live site (2026-10-06) |
|---|---|---|
| Septic tank pumping / cleaning | $530 | — |
| Portable toilet, per month with weekly cleaning | $140 | **$165/month** (conflict) |
| Hydrovac excavation | $230/hr | — |
| Storm drains / catch basins | $388 | — |
| RV servicing | $130 | — |
| Grease traps | $317 | — |
| Water delivery | $329 | $329 |
| Car wash pump-out | $189 | — |

**Regulatory**
- Waste handled "following Health Canada's guidelines" (client's own copy). No licence number requirement found.
- Don't cite a BC-mandated pumping interval; there isn't one. Use HealthLink BC's 2–5 year guidance (blog draft research, 2026-09).

## 3. Target market and geography

**Who they serve:** homeowners and business owners; also partners with plumbing companies (Success Track). Commercial: restaurants (grease traps), stratas, construction sites, municipalities and industrial (hydrovac).

**Service area:** Chilliwack to Squamish (Metro Vancouver and the Fraser Valley).

**Priority areas, in order** (Success Track; matches the live homepage)
1. Port Coquitlam (HQ)
2. Coquitlam
3. Port Moody (incl. Anmore and Belcarra)
4. Pitt Meadows
5. Annacis Island
6. Langley
7. Surrey
8. Maple Ridge
9. Richmond
10. Vancouver
11. Burnaby
12. New Westminster
13. Delta / Ladner / Tsawwassen
14. North Vancouver / West Vancouver
15. Aldergrove, Abbotsford, Mission
16. Squamish (*priority not confirmed*)

The Google Ads city customizer sheet (2026-03) also lists Chilliwack, Lions Bay and White Rock.

**Location pages live:** Port Coquitlam, Port Moody, Burnaby, Surrey, Richmond. **Drafted, not live:** Coquitlam and Pitt Meadows (2026-09-04 doc in this folder).

**Calls by area** (client call log, Jul → Aug 2025): biggest drops Abbotsford (-10), Surrey (-7), Port Coquitlam (-6), Delta (-6), Aldergrove (-6); gains in Vancouver, Burnaby, West Vancouver, Deroche, Pitt Meadows.

## 4. Competitors

**Named by the client** (Success Track, 2022)
- Ace Septic Pumping (acesepticpumping.ca)
- McRae's Environmental Services (mcraesenviro.com). Clearset ranks #30 for "mcrae's environmental services ltd"; don't target competitor brand terms.
- Mainland Tank Service (mainlandtank.com)

**septictankcleaninglangleybc.ca.** A lead-gen site **Clearset is also paying for** (Andrew, 2026-01-21).
- It outranks Clearset on Langley terms: Langley in the domain and GBP, plus a location page for every service (Francis, 2026-01-29).
- Clearset dominates Port Coquitlam/Coquitlam for "septic tank cleaning" and most map-grid pins for "septic tank clean up".
- Andrew's goal: a factual case for the client to drop it and move that spend to us, without losing leads. **Outcome not recorded.**
- Its ranking keywords sit in the "Sheet12" tab of the Website Audit sheet.

**Not pulled this run:** Semrush competitor visibility for the tracking campaigns (API couldn't reach them, see section 5).

## 5. Current SEO status

**GSC** (`https://clearsetvactruck.ca/`, 2026-07-08 to 10-05)
- 571 clicks, 132.6K impressions, CTR 0.43%, avg position 19.8
- 538 clicks / 123K impressions from Canada; US 17 clicks
- Brand queries ("clearset vac truck services", "clearset", "clearset enterprises ltd") are about 20% of clicks
- **Impressions fell from about 1,500–2,900/day (Jul–Aug) to 500–1,100/day (late Sept)**, while average position improved from ~20 to ~12–16. Fewer broad national impressions, not lost rankings. *Worth checking before the client asks.*

**Pages with the biggest gaps** (90 days)

| Page | Clicks | Impressions | Avg pos |
|---|---|---|---|
| /septic-system-service-burnaby/ | 5 | 37,659 | 22.8 |
| /services/sewer-camera-inspection-port-coquitlam/ | 4 | 11,611 | 32.0 |
| /services/water-hauling/ | 56 | 10,232 | 18.1 |
| /septic-tank-cleaning-surrey/ | 7 | 5,725 | 31.0 |
| /septic-tank-service-port-coquitlam/ | 3 | 5,508 | 11.2 |
| /services/septic-tank-cleaning/ | 6 | 4,040 | 25.9 |

**The Burnaby city page is acting as the national septic hub.** It ranks for "septic tank pumping (near me)" (5,400/mo CA) and "septic tank cleaning near me" (4,400/mo CA) at #14–18, while the actual hub /services/septic-tank-cleaning/ gets a tenth of the impressions. Cannibalization to sort out.

**Best performers:** homepage (160 clicks plus 117 via the GBP UTM link), RV pumping (67), water hauling (56), IBC tank rentals (42, CTR 2.5%), portable toilets (39).

**Monthly report trend** (automated reviews in #clearset)
- May 2026: key events +126% YoY; Port Coquitlam visibility -13.7% MoM; GSC avg rank 20.08 (-45.6% YoY)
- June 2026: organic = 29.7% of key events (+380% YoY); Port Coquitlam visibility +11.7 pts to 47.44%
- July 2026: GSC clicks -47.3% YoY, -22.6% MoM. **Andrew asked Francis to investigate the YoY drop (2026-08-07); five follow-ups, no findings posted.**
- Aug 2026: GSC clicks -26% MoM / -58.4% YoY; Coquitlam visibility -19.47% (13 up / 27 down); Port Moody avg position -6.93; Pitt Meadows the only gain; **zero new GBP reviews**.

**Technical history**
- A 3 MB, 20,000 px wide footer/schema logo was crashing GSC's crawler for months; fixed 2025-12-18. Watch for heavy images.
- Some content was built hidden on mobile (2025-04-11). Mobile-first indexing means nothing important should be hidden.
- Andrew says many service-page images were AI-generated; most were replaced with real Instagram/WordPress photos (2025-10-31). *Confirm none remain.*
- Real job photos are in Drive, uploaded 2025-09-24 (hydrovac, water delivery, portable toilets).

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-06).

**Tracking:** Semrush project 10336170 tracks **4 location campaigns**: Port Coquitlam, Coquitlam, Port Moody and Pitt Meadows (named in the monthly reports). The API exposed no campaign IDs, so **position data, volumes and competitor visibility couldn't be pulled. Check the Semrush UI.** The Dec 2024 brief was 3–5 locations with 30–50 keywords each, under a 150-keyword plan cap.

**Organic footprint** (Semrush CA, 2026-10-06)
- Strong on brand and "vac truck" terms: #1 "vac truck service" (480/mo), #3–4 "vacuum truck service(s)"
- Weak on the big septic heads: #14–18 for "septic tank pumping (near me)" (5,400) and "septic tank cleaning near me" (4,400)

**Out-of-scope rankings to watch:** "potable water truck" (#5) and "potable water delivery" (#14) still rank on the water hauling page; "lift station cleaning calgary" (#5, Alberta); "leach line repair" (#5). Don't build on any of these. See keywords.md section 5.

**Keyword rules**
- No potable/drinking water
- No septic inspection
- No septic or drain field repair as a service; rejuvenation and maintenance only
- No Alberta or out-of-area terms
- No competitor brand names
- Portable toilets: no sinks, ADA or add-on terms, and respect the narrower toilet service area

## 6. Current marketing programme and scope

**Package** (Success Track, since Dec 2022; *confirm still current*)
- **SEO Silver:** 150 keywords tracked, 8 hours of optimization a month, 2 landing pages a year
- **PPC Bronze:** 1 ad platform, third-party spend up to $1,500/month. Actual Google Ads spend was about CA$3.08K/month in Aug 2026, so the budget has changed. *Confirm the current contract.*

**Recurring work**
- **GBP posts:** Mon/Thu via the #gbp-post-approvals pipeline (`clearset_port_coquitlam`). Handoffs since 2026-09-14 cover RV pump-outs, grease traps, catch basins, sewer camera, hydro jetting and pre-winter septic.
- **Citations:** monthly (Francis' weekly logs, 2026-01 and 02). Cylex listing request handled 2025-10.
- **Reporting:** monthly PDF report around the 7th with an automated Slack review. Sean said in 2025-09 that he wasn't receiving Semrush emails; Clarissa sent six months manually.
- **Maintenance:** plugin updates, page edits, GSC indexing requests.

**Landing pages built in 2025:** portable toilet rentals, line scoping / sewer camera, drain field rejuvenation, water tote / IBC tank rentals. Homepage rewrite approved 2025-01, built 2025-03.

**Blogs:** none in the original scope. A first blog was drafted in Sept 2026 ("5 Warning Signs You Need Septic Repair", this folder); the site has no /blog/ yet. *Confirm blogs are in scope or covered by SEO hours.*

**Project tracking:** Teamwork project 1141193 (new 2026-01-21). **Log time monthly.** Andrew has chased time logs twice (2025-05-30, 2025-09-11).

**Pricing / retainer:** not found.

## 7. PPC overview

**Google Ads** (Andrew manages; from automated report reviews)
- Campaigns: Residential Septic, Commercial Liquid Waste, Hydrovac & Excavation, Rentals & Water
- Ad groups mentioned: Hydro Jetting & Line Flushing, Water Hauling, Toilet Rentals, Hydrovac & Excavation

| Report (data month) | Conversions | Cost / conversion | Notes |
|---|---|---|---|
| June 7 (May) | 128 (+30.6%) | CA$20.44 | Hydrovac CA$56.10 / conversion; CallRail 138 qualified leads |
| July 7 (June) | 175.5 (+33.5%) | CA$17.42 | Commercial Liquid Waste cost / conversion +104% |
| Aug 7 (July) | -25% | +33.4% | Hydro Jetting ad group cost / conversion +330% |
| Sept 7 (Aug) | -17.6% | CA$27.49 (+22.2%) | Spend CA$3.08K; qualified calls -45.1% |

- Ads use dynamic city insertion from the "Clearset City DKI Data" sheet (24 BC cities, 2026-03).
- **No city exclusivity** in the contract (2023-12), so ads can run across the Lower Mainland.
- Potable water keywords and ads were removed 2024-09-18. Keep them out.
- Ads don't target Alberta.
- GBP/Ads linking needed owner-level access from the client (2024-03). *Confirm it's done.*

## 8. Content guidelines

**Accuracy is the hard rule.** Andrew, 2026-09-11 and 2026-10-06: never add content about services the client doesn't offer; ask Andrew when unsure. The client reads the site closely and has caught us twice.

**Log every major site change in #clearset.** It gives the client and Andrew an easy change log (Andrew, 2026-10-06; applies to all clients).

**Review sliders sit right after the hero** on the home and service pages. New content must not push them down (Andrew, 2026-10-06; applies to all clients).

**Voice:** direct, second person, plain language, minimal fluff (the blog draft matched the service-page tone). Practical and trustworthy rather than salesy. Light, sensible humour is fine (see the GBP drafts).

**Terminology**
- Use both "vac truck" and "vacuum truck". Vacuum-truck terms had more volume (2025-01).
- "Hydro flushing / hydro jetting / line jetting" and "hydrovac / hydro excavation / daylighting" are synonyms. Use the client's terms in headings.
- "Portable sanitation" is now wanted as a category label alongside "portable toilet rental" (client and Andrew, 2026-10-06).

**Images**
- Real Clearset photos only (Drive folder, WordPress media, Instagram).
- No AI-generated images. Francis flagged existing ones in 2025-10.
- GBP images must be at least 400×300.

**Service areas:** describe Clearset as *serving* a city, never as *based in* it (except Port Coquitlam).

**Prices:** don't quote them unless reconfirmed. GBP drafts have left prices out since 2026-09 because of the $140 vs $165 conflict and grease trap figures that don't reconcile.

**Approval:** Andrew relays to Sean. Major copy (homepage, new pages) needs client sign-off. Small SEO tweaks can go live and get logged in Slack.

## 9. Key priorities and strategic notes

**Open asks from Andrew (2026-10-06)**
1. Fix the portable toilet page. The client flagged content covering the wrong service, likely the "What Our Customers Say About Clearset's **Hydrovac** Services" review heading, which also appears on the homepage and About page. Then **review every service page and the homepage** for similar mismatches.
2. Work **"portable sanitation"** into the toilet rental page, homepage and menu (the draft doc in this folder covers it). The homepage H1 change is undecided: Andrew is unsure and the draft keeps the H1 as is.
3. Move review sliders back up under the hero on the toilet page and homepage.

**Outstanding investigation:** the July/Aug GSC YoY click drop (asked 2026-08-07). The client is asking about AI rankings and will likely ask about declines next.

**Strategic read**
- **Location pages are the growth lever** (Francis, 2026-01-29). The Langley lead-gen site wins on page count and Langley-named assets. Coquitlam and Pitt Meadows drafts are ready; Langley, Maple Ridge, Abbotsford and others are gaps.
- **Fix septic cannibalization:** the Burnaby city page is soaking up national septic impressions. Strengthen /services/septic-tank-cleaning/ as the hub and keep city pages local.
- **AI visibility:** Sean tests ChatGPT answers himself ("septic pumping Langley", "portable sanitation" lists). AEO was pitched (2026-08). Schema, GBP categories and citations carry most of this.
- **Hydrovac and hydro jetting:** the client keeps raising them (2025-05, 2025-12). Hydrovac is a top revenue line, but the hydrovac page sits at avg position 36.5 and hydro-flushing at 45.7. Daylighting and potholing H2s were suggested in 2024-12 and 2025-05.
- **Reviews:** zero new GBP reviews in Aug 2026. Suggest a review-request cadence.

## 10. Social profiles and other channels

- Facebook: facebook.com/clearsetseptic
- Instagram: @clearsetvactruckservices. The best source of real job photos. Feed is embedded on the site.
- GBP: Port Coquitlam location (`clearset_port_coquitlam`). Categories expanded 2025-09 and services cleaned up 2026-02.
  - Categories per the "Clearset Services" doc (2026-02): Septic system service, Drainage service, Water pump supplier, Excavating contractor, Water utility company, Sewage disposal service, Portable toilet supplier, Waste management service, Water jet cutting service, Water tank cleaning service.
  - *Check "Water pump supplier", "Water utility company" and "Water jet cutting service". They don't match services Clearset offers.*
- AI referrals: a small amount from ChatGPT in GA4 (2025-09). No AI Overview mentions per Semrush at that time.

## 11. Working rules and tool IDs

**Approvals**
- Content: Andrew relays to Sean
- GBP: 👍 in #gbp-post-approvals

**Standing rules**
- No potable water
- No septic inspections or repairs
- No Alberta
- Real photos only
- Log site changes in Slack
- Reviews under the hero
- Ask Andrew when unsure about a service

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | **10336170** "Clearset - Current" (site audit, backlink audit, tracking, SEO ideas, GA). 10067027 "Clearset - old": consider archiving. |
| GSC | `https://clearsetvactruck.ca/` (agency has owner access). `https://clearset.ca/` property also exists. |
| Slack | #clearset C04BXUMV0ES. GBP source of truth: #gbp-post-approvals. |
| GBP automation key | `clearset_port_coquitlam` |
| Teamwork | project 1141193 |
| Scheduled tasks | `seo-report-roadmap` (scans C04BXUMV0ES) |

**Drive**

| File | ID |
|---|---|
| Client folder "Clearset Enterprises" | `1VvcnBKdlANCoCVFPtouNCkIWT3cqU9YG` |
| Success Track | `1OjURPkwstSpxLXe08eN9qrWZtQVW-y72hzirCJo5t1k` |
| Clearset Services (GBP categories) | `1dhzL0Fks6Rgas3RVLruSOrGuTl-kg-AmNskK6dLjads` |
| Website Audit (keyword tabs, crawls) | `1ADc8RO6p9GboX8ErZwagvQJ3o0dPZqGXS7Cx43Nyit0` |
| Master Keyword sheet (2024) | `1l0B4iNqP3rd7tcW7-IjXFBb3xC5S7Uo6XSwjdTjyrYA` |
| Master Keywords 2024 (copy) | `1WvFfhuWJxee1IEAvxowtgD6oB6n89SXxIBhUf-oH80s` |
| Landing Page Ideas KW Research | `1YQbIsLpyqwRoQyISztugDQcz0UhFEMbV4_FnROJB8xo` |
| City DKI Data (Ads) | `1j6PMBEzgr4kvVsaUwimYWBRIUi55cHX-WYiQT0fHPyk` |
| PPC Monthly Checklist | `12a2d9Ya9Wi57R43cWWxFMaN5_BnTnLnU-cSHAlkj4qs` |
| SEO Monthly Checklist (2022) | `1gPYNbMTloI5jaOLKOq9c5OBomUY3tOk72Mo9JJaIo3A` |
| Homepage copy (approved 2025-01) | `1r6kvy2RSlNP-HzNMxEzPrpwuQzD0CTrVHqoMLZZMqfg` |
| LP docs 2025 | Toilet `1jY0W1BwaeGVDnJ9y4YzRi75rp0BmuA_2HHJDUl8Xo4A`; Water Tote `1e4hBUL-vgIMYonKW73-O2A9WZfXQS2sGF_13JyWVnNs`; Sewer Camera `1X8opAYXKQ1LEvUYYZTOKhVlr-_IPp8QLiDZmm9qjPSc`; Drain Field `1oXZcGi-xQl0pSPSasZiST3WBB8VmlFDt7dTvLzzp5w4` |
| Old domain redirects (2024) | `1xIol2xFjWkPAGn8_u9KUe1moRgewk_kflcxsL33xo3k` |

## 12. Open items

**Due now (2026-10-06)**
- [ ] Fix the wrong-service content on /services/portable-toilet-rentals/ and review all service pages and the homepage for the same issue. Report back in #clearset.
- [ ] Get Andrew's and the client's sign-off on the portable sanitation edits doc, then implement. Settle the homepage H1 question.
- [ ] Move review sliders back under the hero (toilet page, homepage).

**Waiting on us**
- [ ] The GSC YoY click drop investigation (asked 2026-08-07, five follow-ups). Acknowledge the Sept automated report review (two follow-ups).
- [ ] Publish the Coquitlam and Pitt Meadows location pages (drafted 2026-09-04). Plan Langley next.
- [ ] Fix septic cannibalization (Burnaby page vs the septic hub).
- [ ] Refresh the Semrush tracked keywords: drop low-volume terms, add terms from page research (Andrew, 2025-05-21). *Check whether it was done.*
- [ ] Remove "Leach Field **Repair**" wording on the homepage (H3). They do rejuvenation and refer repairs out. *Confirm with Andrew.*

**Waiting on the client / confirm**
- [ ] Current prices (toilets $140 vs $165 live; grease trap figures).
- [ ] Which phone to publish. The site shows (778) 825-1032 and (778) 652-6317; the blog draft uses (778) 907-9875.
- [ ] Current portable toilet service area.
- [ ] Well cleaning: add as a service or not?
- [ ] Whether blogs and AEO are in scope. Approval of the first blog draft.
- [ ] Outcome of the septictankcleaninglangleybc.ca recommendation (Jan 2026).
- [ ] Real photos for the Oct 8 portable-toilet GBP draft (NEEDS PHOTO) and fresh septic truck photos (the current one has been used 3 times).
- [ ] Review the GBP categories that look wrong (section 10).

**Ops**
- [ ] Old domain septictankpumpingservices.net doesn't resolve. Check whether it lapsed and whether backlinks need reclaiming.
- [ ] Make sure Sean receives the monthly reports.
- [ ] Log monthly hours in Teamwork 1141193.

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked.
- BrightLocal: no reviews, citation or rank-grid data.
- **Semrush Position Tracking:** project 10336170 has tracking enabled, but the API returned no campaign targets and "campaign not found" for the project ID. No tracked-keyword positions, volumes or competitor visibility this run.
- Current retainer, contract and PPC budget not found. The Success Track is from 2022.
- Drive sheets were read as samples only: the full keyword tabs weren't returned.
- The client's 2026-10-06 screenshot (F0C3B3PLH7Z) couldn't be opened, so the "wrong service" item is inferred.

**Conflicts**
- **Toilet price:** $140 (client, 2025-09) vs $165/month (live page).
- **Toilet service area:** client list (2025-03, no Abbotsford/Chilliwack/Squamish) vs the live page (lists Abbotsford, Chilliwack, Squamish).
- **Toilet add-ons:** removed April 2025, but the live page has an "Optional Outhouse Add-ons & Portable Toilet Unit Types" section.
- **Phones:** three different numbers in use (CallRail adds more). Citations should use (778) 825-1032.
- **Repair language:** the homepage H3 says "Leach Field Repair", while the client refers repairs out. The blog draft targets "septic repair" signs but funnels to pumping (acceptable, but its title and keyword lean on repair).
- **Abbotsford:** in the service area and Ads cities, and a call source, but not in the toilet area.
- **Success Track** still lists the old domain and "all of BC". It's out of date.
