# Clearset: GSC YoY drop, Aug–Oct 2026 (notes for Andrew's call with Sean, 2026-11-10)

- **Asked by:** Andrew in #clearset on 2026-11-07: "huge drop in GSC last 3 months YoY. Please investigate and let me know your findings and proposed action items."
- **Written:** 2026-11-10 by Francis (with Claude)
- **Builds on:** [gsc-yoy-drop-investigation-2026-10.md](gsc-yoy-drop-investigation-2026-10.md), which covered Jul–Sep. That reply was drafted but never posted in Slack.

**Sources**

| Data | Source | Scope |
|---|---|---|
| Clicks, impressions, average position | Google Search Console, property `https://clearsetvactruck.ca/` (web search) | Aug 1–Oct 31 2026 vs Aug 1–Oct 31 2025. Query data: all 3,360 / 3,103 query rows GSC returned for each period. |
| Search volume and cost per click | Google Ads Keyword Planner | Location British Columbia, 12 months Oct 2025–Sep 2026 |

Keyword Planner rounds volumes for low-spend accounts, so treat them as ranges, not exact counts. Query-level GSC totals are lower than page totals because GSC hides anonymised queries.

## 1. Headline numbers

| | Aug–Oct 2025 | Aug–Oct 2026 | Change |
|---|---|---|---|
| Clicks, whole site (page level) | 1,071 | 490 | **-54%** |
| RV pumping page | 555 | 54 | -90% (501 of the 581 clicks lost, 86%) |
| Homepage + GBP link | 217 | 249 | +15% |
| Other service and city pages | 299 | 187 | -37% |
| October only | ~288 | ~127 | -56% |

**Clicks by topic** (query level, Aug–Oct):

| Topic | Clicks 2025 | Clicks 2026 | Impressions 2025 | Impressions 2026 |
|---|---|---|---|---|
| RV / trailer / black tank | 145 | 12 | 9,856 | 3,877 |
| Septic | 57 | 12 | 70,972 | 43,959 |
| Grease trap | 7 | 2 | 4,056 | 3,521 |
| Portable toilets / sanitation | 11 | 4 | 1,506 | 4,346 |
| Hydrovac | 1 | 3 | 7,729 | 3,473 |
| Brand ("clearset…") | 101 | 102 | 714 | 650 |

Brand searches are flat, so people still look for Clearset by name. The loss is in non-brand service searches.

## 2. Demand didn't drop. Clearset's share did.

People are searching for these services in BC as much as they did last year. The RV numbers are close to flat across the season:

| Keyword (BC) | Avg searches / month | Oct 2025 | Sep 2026 | Top-of-page bid range (CAD) |
|---|---|---|---|---|
| rv septic tank pumping | 30 | 40 | 30 | $2.32–$8.33 |
| rv pumping service near me | 10 | 10 | 10 | n/a |
| rv tank pumping service near me | 10 | 10 | 10 | n/a |
| rv pump out service near me | 10 | 10 | 10 | $3.86–$10.54 |
| septic tank pumping | 1,300 | 1,300 | 1,000 | $3.51–$15.91 |
| portable toilet rental | 880 | 590 | 590 | $2.17–$12.64 |
| hydrovac | 590 | 720 | 590 | $2.88–$15.76 |
| septic tank pumping near me | 390 | 390 | 480 | $3.18–$16.63 |
| septic service near me | 260 | 320 | 260 | $3.23–$20.05 |
| septic tank cleaning | 210 | 320 | 140 | $4.47–$21.24 |
| grease trap cleaning | 210 | 210 | 170 | $4.52–$18.00 |
| catch basin cleaning | 70 | 90 | 50 | $6.94–$34.93 |
| septic tank pumping langley | 50 | 70 | 50 | $5.42–$22.09 |
| vacuum truck services near me | 40 | 70 | 30 | $3.73–$21.09 |

## 3. RV: the main loss

| Query | Clicks 2025 | Clicks 2026 | Impressions 2025 | Impressions 2026 | Avg position 2025 | Avg position 2026 |
|---|---|---|---|---|---|---|
| rv septic tank pumping | 10 | 0 | 157 | 29 | 12.5 | 7.0 |
| rv tank pumping service near me | 7 | 0 | 303 | 124 | 6.9 | 19.9 |
| rv pumping service near me | 6 | 0 | 85 | 29 | 10.7 | 4.7 |
| mobile rv pumping service | 6 | 0 | 103 | 11 | 11.2 | 5.6 |
| rv septic pumping | 4 | 0 | 286 | 15 | 38.0 | 12.9 |
| rv pump out | 0 | 0 | 53 | 6 | 5.9 | 7.0 |

- The number of RV queries with at least one click fell from **71 to 12**.
- The number of RV queries Clearset shows up for at all fell from **403 to 249**.
- Clearset now appears only occasionally for these searches: a handful of impressions against steady demand. Some average positions look better, but they're based on so few impressions that they don't mean much.
- The timing matches Google's August 2025 spam update (Aug 26 – Sep 22, 2025) ([Search Engine Land](https://searchengineland.com/google-august-2025-spam-update-done-rolling-out-461560)). The page is still indexed, and its content didn't change before the drop.
- The RV page rework recommended in October hasn't been started. The H1 typo ("RVTank") and the DIY pumping section are still on the page.

## 4. The money keywords: Clearset is on page 2, so almost nobody clicks

| Query | BC searches / month | Impressions Aug–Oct 2026 | Avg position 2026 | Clicks 2026 |
|---|---|---|---|---|
| septic tank pumping | 1,300 | 4,689 | 16.1 | 3 |
| septic tank cleaning | 210 | 7,698 | 19.6 | 0 |
| septic tank cleaning near me | 40 | 5,568 | 23.4 | 2 |
| septic tank pumping near me | 390 | 3,089 | 23.1 | 2 |
| vacuum truck services near me | 40 | 1,526 | 10.6 | 1 |
| grease trap cleaning | 210 | 1,554 | 7.8 | 1 |
| catch basin cleaning | 70 | 761 | 20.8 | 0 |
| portable toilet rental | 880 | 338 | 9.4 | 0 |
| hydrovac services | 40 | 457 | 1.5 | 0 |

- Clearset gets seen for these searches (over 23,000 impressions on the four septic terms alone) but sits around positions 16–23, on page 2, so it gets almost no clicks.
- Moving the septic terms onto page 1 is the biggest lever on the site. These are also the terms where advertisers pay $3–$21 a click in BC.
- The Burnaby city page still takes the national septic searches (27,385 impressions, 5 clicks) instead of the septic hub page. This is the cannibalization issue already on the open list.

**Why average position "improved" while clicks fell.** In Sept 2025 Google stopped supporting the `num=100` results parameter. That removed a lot of deep-position impressions from GSC reports for most sites ([Noble Studios](https://noblestudios.com/seo/google-retires-num100-seo-reporting-change/)). So year-over-year position and impression comparisons aren't reliable. Clicks are the honest measure.

## 5. What's going right

- **GBP / map pack clicks are up.** Clicks through the GBP website link went from **41 to 108** (average position 3.6). Part of the "near me" demand now reaches Clearset through the map listing instead of the service pages. GBP calls and direction requests will show this better than GSC clicks.
- **Water queries are growing.** "water truck services" went from 0 to 4 clicks (impressions 333 to 691, position 20.4 to 9.6).

## 6. Proposed action items

1. **Rework the RV page as a service page before the 2027 RV season** (aim for March):
   - Fix the H1 typo.
   - Give it a local title and meta.
   - Remove the DIY section.
   - Add an FAQ.
   - Link to it from the homepage and the services page.
   - Changes go to Andrew in a doc first.
2. **Push the septic hub page onto page 1.** "septic tank pumping" (1,300/mo) and "septic tank pumping near me" (390/mo) sit at positions 16–23 today. Make /services/septic-tank-cleaning/ the clear hub, keep the Burnaby page local, and link the city pages back to the hub.
3. **Refresh the slipping service pages:** grease trap (210/mo, position 7.8, 1 click), catch basin (70/mo) and portable toilets (880/mo, position 9.4). Add only services Clearset actually offers.
4. **Publish the Coquitlam and Pitt Meadows location pages.** They've been drafted since September.
5. **Rule out a manual action.** Check GSC > Security & Manual Actions. The connected GSC tool can't read it, so this is a manual check.
6. **Check who now ranks for the RV and septic terms.** Use Semrush once API units are back, or a Canadian-location check.
7. **Reporting:**
   - Report the RV page separately.
   - Add GBP calls and clicks next to GSC clicks.
   - Note that impressions and position before Sept 2025 aren't comparable.

None of these guarantees a recovery. They fix the clear weak points and show us who took the spots.
