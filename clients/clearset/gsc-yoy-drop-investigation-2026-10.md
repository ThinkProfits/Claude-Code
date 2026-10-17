# Clearset: GSC year-over-year click drop investigation

- **Asked by:** Andrew, in the July 2026 report review thread (#clearset, 2026-08-07): "look into the large YoY drops (GSC clicks -47%) and let me know what you find"
- **Written:** 2026-10-18 by Francis (with Claude)
- **Data:** Google Search Console, property `https://clearsetvactruck.ca/`. GSC keeps 16 months, so the earliest day available is 2025-06-05.
- **Not checked:** live Google results for the RV queries (Semrush API units are at zero, and a manual search from the Philippines would show the wrong location). The live page returns 403 to non-browser requests, so the on-page comparison uses Wayback Machine copies.

## Short answer

The site didn't lose traffic across the board. **One page, `/services/trailers-and-rvs-pumping/`, explains almost the whole drop.** If you take that page out, clicks are flat year over year.

| Period | All clicks, 2025 | All clicks, 2026 | Change | RV page, 2025 | RV page, 2026 | Rest of site, 2025 | Rest of site, 2026 | Change, rest of site |
|---|---|---|---|---|---|---|---|---|
| July | 482 | 254 | -47% | 281 | 39 | 201 | 215 | **+7%** |
| August | 452 | 188 | -58% | 281 | 23 | 171 | 165 | **-4%** |
| Jul–Sep | 1,259 | 610 | -52% | 706 | 74 | 553 | 536 | **-3%** |

The RV page lost 632 of the 649 clicks the site lost in Q3, or 97%.

## 1. What happened to the RV page

Monthly clicks (impressions in brackets):

| 2025 | Jun 220 (8,963) | Jul 281 (14,252) | Aug 281 (16,072) | Sep 144 (11,260) | Oct 130 (7,022) | Nov 57 (5,898) | Dec 34 (4,617) |
|---|---|---|---|---|---|---|---|
| **2026** | Jan 27 (3,813) · Feb 45 · Mar 62 · Apr 51 | May 85 (3,978) | Jun 66 (2,995) | Jul 39 (2,393) | Aug 23 (2,328) | Sep 12 (1,417) | Oct 1–15: 3 (629) |

- **When:** the page was steady at 55 to 80 clicks a week through August 2025. It dropped to about 35 a week from the week of 2025-09-01, then to about 10 a week by mid-November. Summer 2026 never recovered, so this isn't just RV seasonality.
- **What it lost:** the whole "RV pump-out near me" query family. Each of these had clicks in Q3 2025 at positions 6 to 15, and the whole site has **0 impressions** for them in Q3 2026: "rv tank pumping service near me" (15 clicks, pos 6.5), "rv septic tank pumping", "rv septic pumping", "rv pumping service near me", "rv black tank cleaning service", "mobile rv pumping service", "rv pump out" and about 20 more.
- **It's not an indexing problem.** URL Inspection (2026-10-18) shows it "Submitted and indexed" and crawled 2026-10-17. The canonical is self-referencing, there's no noindex, and the rich results (breadcrumbs, review snippets) pass.
- **No on-page change caused it.** The Wayback copies from 2025-07-31 and 2025-10-08 have the same title, meta description, H1, H2s and length (about 1,550 words). The decline started between those two dates.

**Likely causes**, in order of confidence:

1. **Google's August 2025 spam update** ran from 2025-08-26 to 2025-09-22, with a second wave around 2025-09-09 ([Search Engine Land](https://searchengineland.com/google-august-2025-spam-update-done-rolling-out-461560), [Search Engine Journal](https://www.searchenginejournal.com/google-confirms-august-spam-update-is-complete/556465/)). The RV decline lines up with that window. There was no manual action check in this pass. *Check GSC > Security & Manual Actions.*
2. **Local intent moved to the map pack.** These are "near me" queries. Clicks from the GBP listing (homepage with the `utm_source=gmb_listing` link) went from 14 to 120 year over year, and impressions from 4,229 to 22,142. Some of that demand is now reaching Clearset through the GBP instead of the RV page. Organic clicks don't show it.
3. **Weak page signals that make it easy to outrank.**
   - The H1 has a typo, "Trailer & RVTank Pumping Services" (no space).
   - The title and meta are generic, with no service area.
   - The page is written like an article rather than a service page.
   - A "DIY Septic Pumping Instructions" section was added between 2025-10 and 2026-01. On a service page that sends the wrong signal, and it tells the customer how to skip the service.

## 2. The rest of the site

- **Homepage plus the GBP link combined:** 249 clicks to 291 (+17%). Plain homepage clicks fell (235 to 171) while GBP-link clicks grew (14 to 120). It's the same page; Google is sending more of those visits through the map listing.
- **Small real losses:** pump chambers (13 to 2 clicks), grease trap cleaning (21 to 8), septic tank cleaning hub (12 to 6), Port Moody septic page (6 to 1). Together they lost about 30 clicks. These match the septic cannibalization already noted in CLIENT.md (the Burnaby page takes the national septic impressions).
- **Gains:** portable toilet rentals (24 to 37 clicks), storm drains (11 to 17), plus new queries like "septic tank cleaning near me" (10,704 impressions) and "septic tank pumping" (position 61 to 17).
- **Brand searches are stable:** "clearset vac truck services" 67 to 69 clicks, "clearset" 28 to 35.

## 3. What isn't a real problem

- **Impressions and average position.** Site average position "improved" from about 38 to about 19, and impressions on deep-ranking pages fell 50% to 85%. In mid-September 2025 Google stopped supporting the `&num=100` results parameter. That removed a lot of deep-position impressions from GSC sitewide, and most sites saw the same reporting drop ([Noble Studios](https://noblestudios.com/seo/google-retires-num100-seo-reporting-change/), [AdPushup](https://www.adpushup.com/blog/google-num100-parameter-removal/)). Treat 2025 vs 2026 impressions and position comparisons as unreliable, and judge on clicks.
- **Countries and devices.** Canada is 95% of clicks in both years. US impressions fell 58%, but it was only 23 clicks to begin with. Mobile clicks fell more than desktop (-58% vs -40%), which fits RV owners searching on phones.

## 4. Recommended next steps

1. **Rework the RV page as a service page** (it's still a real, popular service):
   - Fix the H1 typo.
   - Give it a local title and meta (Lower Mainland / Fraser Valley, mobile, on-site).
   - Remove or shorten the DIY section.
   - Add the starting price only if the client reconfirms it ($130 from 2025-09).
   - Add an FAQ with the `tp-faq-accordion` class.
   - Link to it from the homepage and the services page.
   - Real photos only.
2. **Check the live results** for "rv pumping near me", "rv pump out" and "mobile rv septic pumping" in Port Coquitlam / Surrey / Langley, once Semrush units are back or via a Canadian-location check. That shows who took the spots: directories, competitors or the map pack.
3. **GBP:** make sure "RV / trailer pump-out" is a listed service, and keep posting about it from May to September, before the season.
4. **Manual actions / security:** quick check in GSC to rule out a penalty.
5. **Reporting:** add a note to the monthly report that impressions and position before September 2025 aren't comparable. Report the RV page separately so one seasonal page doesn't swing the whole SEO story.
6. **Septic cannibalization fix** (already on the open list) to win back the pump chamber, septic hub and Port Moody losses.

None of the above guarantees a ranking recovery. It removes the obvious weak points and tells us who we're up against.
