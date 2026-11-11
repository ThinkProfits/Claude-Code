# John Sadler: site crawl and GA4 review, 2026-11-11

Internal. These are the follow-ups from the 2026-11-10 check-in ([checkin-2026-11-10.md](checkin-2026-11-10.md)). Nothing on the live site was changed. Andrew asked us to hold edits until he shares how the client meeting went.

- **How the crawl was run:** the public WordPress REST API (`/wp-json/wp/v2/pages` and `/posts`), covering every published page and post, with the rendered content searched for patterns. The sitemaps return 403 to scripts, but the REST API answers.
- **Not covered:** header, footer and widget output outside `content`, Bold page builder blocks that don't render into `content`, and the live CallRail swap.

## 1. AC and heat pump repair copy

- **The blocker is cleared on the two service pages.** Andrew rebuilt both on 2026-11-09 (modified 18:51):
  - [/services/heating-cooling/air-conditioning/](https://www.johnsadler.ca/services/heating-cooling/air-conditioning/)
  - [/services/heating-cooling/heat-pumps/](https://www.johnsadler.ca/services/heating-cooling/heat-pumps/)
- Both now have a repair H2, a "repair or replace" section, repair FAQs ("Do you repair air conditioners? Yes."), and repair wording in the brand and CTA sections. No "installs only" copy is left on either page.
- **Page-update doc built 2026-11-11:** [page-update-heating-cooling-hub-2026-11-11.md](page-update-heating-cooling-hub-2026-11-11.md). It supersedes the draft table below.
- **Still says install-only:** the parent hub [/services/heating-cooling/](https://www.johnsadler.ca/services/heating-cooling/) (modified 2026-09-11). Its current text:
  > We do not: repair or service air conditioners or heat pumps; do propane, oil, or fuel conversions; do new construction; do drain cleaning (subbed to a trusted partner); install fireplaces. Why install-only for AC and heat pumps Cooling and heat pump systems are more sensitive to install quality than any other HVAC equipment. By focusing exclusively on installation for AC and heat pumps...

  This now contradicts the two child pages. Proposed edit (draft, not applied):

  | Current | Replacement |
  |---|---|
  | We do not: repair or service air conditioners or heat pumps; do propane, oil, or fuel conversions; do new construction; do drain cleaning (subbed to a trusted partner); install fireplaces. | We do not: do propane, oil, or fuel conversions; do new construction; do drain cleaning (we refer this to a trusted partner); or install fireplaces. |
  | H2/H3 "Why install-only for AC and heat pumps" plus its paragraph | **Remove.** Optionally replace it with a short "AC and heat pump repair" paragraph linking to [/services/heating-cooling/air-conditioning/](https://www.johnsadler.ca/services/heating-cooling/air-conditioning/) and [/services/heating-cooling/heat-pumps/](https://www.johnsadler.ca/services/heating-cooling/heat-pumps/). |

- **Unblocked by this:** blogs #1, #7 and #8 in `blogs/2025-backlog/`, and the Navien heat pump and AC error-code posts, can be cleared for publishing once the hub is fixed. The rest of their usual sign-off still applies.

### Things to check on Andrew's new pages (for Andrew and Colin, not fixed)

- **Price ranges are now live:**
  - "$6,000 to $15,000+" for a multi-zone mini-split
  - "$16,000 to $25,000+" for dual fuel
  - "a few hundred dollars" for common AC repairs

  Our content rules say no prices or cost figures, and price terms were pulled from PPC in April 2024. The client may well have approved these in the meeting, so confirm with Andrew rather than assuming either way.
- **Brand claims Colin needs to confirm:**
  - "dealer for American Standard"
  - Repairs "Amana, Daikin". Neither is on the serviced-brands list in CLIENT.md.
  - Fujitsu ductless installs
  - "we repair heat pumps of all types and brands, including systems we did not install"

## 2. Other live-copy issues, by priority

**High: out of scope, or contradicts the client's rules**

| Issue | Pages |
|---|---|
| Says "From leaky faucets and drain cleaning ... we do it all, residential and commercial" (out of scope three ways) | /services/plumbing/hot-water-tanks/, /services/plumbing/hot-water-tanks-installs-replacement/, /services/plumbing/tankless-water-heaters/, /services/plumbing/tankless-water-heater-repair/, /boiler-installs-replacement/, /services/heating-cooling/boiler-repair/, /services/heating-cooling/ (one shared block) |
| Faucet/toilet/clogged-drain service lists | /plumbers-near-me/, /white-rock-plumbing/, /langley-plumbing-and-heating/, /services/plumbing/ |
| Drain cleaning (snaking and hydro-jetting) listed as a strata service | /services/strata-maintenance/ |
| "We proudly serve: Langley \| Surrey \| White Rock \| Maple Ridge \| Abbotsford". Abbotsford is not served, and Maple Ridge isn't on the priority list (*confirm with client*) | /services/plumbing/hot-water-tanks/, /services/plumbing/hot-water-tanks-installs-replacement/, /boiler-installs-replacement/ |
| Abbotsford in the footer area list | /home-2-2/footer/ (sitewide footer) |
| "24/7 emergency plumbing service" (unconfirmed, and the hours are Mon–Fri 8:30–5) | /plumbers-near-me/ (FAQ), /blog/why-does-my-furnace-keep-shutting-off/ |
| "Our team is on-call ... after hours" (same shared block) | The 7 pages in the first row, plus / (homepage) |

**Medium: "50 years" rule (2026 is the 50th year)**

- **"Over 40 years" or "over 45 years" on about 20 pages**, including:
  - /services/heating-cooling/furnace-installation/ (also says Aldergrove)
  - /services/gas-fitting/
  - /services/heating-cooling/furnace-repair/
  - /services/heating-cooling/boiler-repair/
  - /services/plumbing/radiant-in-floor-heating/
  - /services/strata-maintenance/
  - /white-rock-plumbing/
  - /langley-plumbing-and-heating/
  - /plumbers-near-me/
  - /contact-us/
  - /services/
  - /surrey-boiler-services/
  - /tankless-water-heater-surrey/
  - /services/plumbing/hot-water-tanks/
  - /services/plumbing/tankless-water-heaters/
  - blogs: choosing-strata-plumber-hvac-tech, fortis-heat-pump-rebate-requirements, should-you-repair-or-replace-your-furnace, do-you-need-a-boiler-repair-or-a-replacement
- **"Nearly 50 years" on several pages and blogs.** It's acceptable, but "50 years" is the rule.

**Medium: "free estimate" / "free quote" (estimate policy unconfirmed)**

- Pages:
  - /services/plumbing/tankless-water-heater-repair/
  - /services/plumbing/tankless-water-heaters/
  - /services/heating-cooling/boiler-repair/
  - /services/heating-cooling/
  - /services/gas-fitting/
  - /combi-boiler-installation-and-repair/
  - /services/plumbing/radiant-in-floor-heating/
  - /tankless-water-heater-surrey/
  - /fortisbc-rebates/
  - / (homepage)
  - the 3 "We proudly serve" pages
- Blogs: navien-dual-fuel-promo (also an expired April 15 offer), heat-pump-rebates-info (also quotes $4,000–$5,000 rebates).

**Low: superlatives**

- "best in the industry" (Navien heat exchangers): /services/navien/, /services/navien/how-does-a-navien-combi-boiler-work/, /blog/right-boiler-system-for-me/
- "the very best service": /plumbers-near-me/
- The award lines ("Voted Best Trade Service Business ... THE NOW readers", "voted best plumber by the Peace Arch News Readers Choice Awards for 2020") quote real awards, which is fine. The 2020 one is stale.

## 3. Phone numbers / CallRail

- 36 non-blog pages show (604) 531-4355 as plain text more often than as `tel:` links, including the new AC and heat pump pages, the homepage and the footer.
- It's a rough count. The script compared phone mentions to `tel:` links in the page content, so it can't tell which ones CallRail swaps.
- **Next steps:**
  - Confirm whether John Sadler uses CallRail. It's not in CLIENT.md, and the September PPC review flagged "zero phone calls on Repairs and Remarketing".
  - If they do, run the incognito swap check from the 2026-11-10 check-in on the homepage, the AC and heat pump pages, and /contact-us/.

## 4. GA4 review (property 256434296, www.johnsadler.ca)

**Sessions by channel**

| Channel | Oct 2025 | Sep 2026 | Oct 2026 | Oct YoY |
|---|---|---|---|---|
| Organic Search | 1,025 sessions / 89 key events | 580 / 43 | 520 / 51 | -49% sessions, -43% key events |
| Direct | 774 / 17 | 586 / 15 | 656 / 16 | -15% |
| Paid Search | 102 / 13 | 303 / 21 | 292 / 26 | +186% |
| Display | 33 / 2 | 132 / 18 | 176 / 34 | +433% |
| AI Assistant | 0 | 19 / 1 | 21 / 3 | new |

**Read**

- **The organic drop is real.** -49% sessions in October lines up with GSC (-56% clicks in September). It isn't only the tracking artifact noted in CLIENT.md.
- Paid and Display now make up a much larger share of traffic.
- **Biggest organic landing-page losses, October YoY:**
  - /blog/replace-water-heater/: 241 to 66 (-73%). The site's top organic post, rewritten 2026-08-24. CLIENT.md's "already improving" note is out of date; check GSC queries and positions.
  - /blog/boiler-components/: 54 to 21
  - /services/navien/: 38 to 15 sessions, and 15 to 1 key events. The hub rewrite draft (`page-update-navien-hub-2026-10-23`) is the fix.
  - /blog/condo-boiler-requirements-2025/: 35 to 7
  - /blog/thermal-relief-valve-dripping/: 35 to 18
- **Holding steady:** homepage (209 to 183), /contact-us/ (32 to 28 sessions; key events up from 4 to 13).
- **Event counts, Jun–Oct 2026 vs Jun–Oct 2025:**
  - session_start: 25,279 to 7,242 (-71%)
  - phone_click: 1,188 to 310 (-74%)

  The session drop is bigger than organic alone explains. Last year's numbers probably include bot or spam traffic, as CLIENT.md already suspected, so **don't quote these YoY figures to the client until tracking is verified.**
- **Seasonality:** Andrew's point that the June–October drop is seasonal was made in the part of the check-in about the other client. For John Sadler, the organic loss runs year over year on the same months, so seasonality doesn't explain it.

## 5. Blog backlog (masterlist checked 2026-11-11)

**Approved old topics still not written** (all "Waiting on info from client"):

- **May 2025 #1 "Why does my furnace not start?"** Overlaps Oct 2025 #2 "What to Do if My Furnace Won't Start?", which is already written and with the client. Recommend merging them or dropping one, to avoid cannibalisation.
- **May 2025 #2 "Does my boiler need maintenance?"** Overlaps the live /blog/annual-boiler-service/ and /blog/regular-boiler-maintenance/. Better as a refresh of one of those than as a new post.
- **Jun 2025 #1 strata post** (boilers, misinformation about all-electric systems). It needs the client's input on the misinformation angle. The live /blog/condo-boiler-requirements-2025/ (which lost traffic, see section 4) is the closest page.

**Proposed topic needing a reframe:** proposed topic #12 "AC Maintenance Tips" still says "Installs-only scope respected". It can now include repair.
