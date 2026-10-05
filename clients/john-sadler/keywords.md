# John Sadler — keywords

> Updated 2026-10-06. DRAFT for Francis's review.
> Sources: Semrush Position Tracking project 2824033 (pulled 2026-10-06; data window 2026-09-29 to 2026-10-05); Drive: "John Sadler - Website Audit & Keyword Research" (Google Sheet `1qHekcQvNCotaxasWIU8fLtUk1BX1xFoPmWbMJO9iWuA`, last edited 2024-12-12, and its .xlsx copy `125WC8bVJSR9NKgxChL94uJytvTjuTKyB`, edited 2025-12-16), "John Sadler Repair Campaign" (`1BwxEARPYnkmBfNpFa7uJdAVZwLh628XLhawIDFIHLp8`, 2024-12), "John Sadler Plumbing Keywords" red-highlight list (`15vmBD7FBIpSpLi8V4CgvXAl-M-0yHkNQUafQUAETVtQ`, 2024-04), Oct 31 2023 performance-review notes (`1XxkQ8Ifwl5IKfqcDPHOLhXdq1LJDOj2uw-5z5iBrcyI`), Client Briefing Sept 2026, Client Overview 2026; Slack #johnsadler (C019H8FNN9H) and #thinkprofits-ppc-team; repo [CLIENT.md](CLIENT.md), [top-5-pages-to-rewrite.md](top-5-pages-to-rewrite.md), `memory/john-sadler-context.md`, `memory/paa-research-standard.md`.
> Reusable: section 4 (keyword rules) is the checklist to run any new tracked, PPC or content keyword against before it goes live.

## 1. Tracked keywords (Semrush)

**Source:** Semrush Position Tracking, project 2824033, campaign `2824033` (the only campaign the API exposes), tracked mask `*.johnsadler.ca/*`. Pulled 2026-10-06.

**Campaign structure note.** The API returns **one campaign with 113 keywords**, not three per-location campaigns. The `campaigns` report came back with no targets, and the guessed per-location ID `2824033_1` returned "campaign not found". The campaign's own search location couldn't be read through the API, so the tables below are **split by the location word inside each keyword**, not by Semrush location. This doesn't match the Briefing's "Surrey 70 / Langley 130 / White Rock 116" (early 2026), which suggests the 3-market setup was either consolidated or lives somewhere the API can't see. Check in the Semrush UI before the keyword redo.

- **Volume** is Semrush's figure for the campaign (lowest level available: local or regional). Treat it as relative, not absolute.
- **7-day change** = position on 09-29 minus position on 10-05 (positive = moved up). "lost" = dropped out of the top 100 on 10-05.
- **30-day change** = Semrush `Diff30` (positive = up).
- Ranking URL is relative to the domain. For 8 terms where the homepage ranks (e.g. best plumber surrey, gas fitter surrey, boiler installation surrey), Semrush recorded the **non-www, http** homepage (`http://johnsadler.ca/`). Check the www/https redirect.

**Snapshot (10-05)**

| Group | Keywords | In top 100 | Top 10 | Top 3 |
|---|---|---|---|---|
| Surrey (incl. South Surrey) | 44 | 40 | 21 | 8 |
| White Rock | 25 | 25 | 13 | 2 |
| Langley | 37 | 21 | 4 | 2 |
| Abbotsford (not served) | 6 | 1 | 0 | 0 |
| No location word | 1 | 1 | 0 | 0 |
| **Total** | **113** | **88** | **38** | **12** |

**Biggest 7-day moves (09-29 → 10-05)**
- Up: boiler repair langley 40 → 13; air conditioner surrey 48 → 22; plumbing and heating company surrey 23 → 4; furnace installation white rock 36 → 16; plumbers in surrey bc 23 → 10; tankless water heater installation surrey 24 → 12; radiant heating white rock 7 → 1; gas line installation surrey 5 → 1.
- Down: **furnace repair surrey 13 → 31 (590/mo, the single most valuable loss)**; hot water tank services white rock 3 → 29; plumbing and heating surrey 7 → 26; furnace service white rock 16 → 37; plumbers in white rock bc 7 → 25; heating service surrey 15 → 32; furnace repair white rock 19 → 32; hot water tank services langley 4 → 14; plumber south surrey 3 → out of top 100 (on 10-05 only, so possibly a one-day blip).
- Not ranking at all (top 100) on several high-volume heads: **surrey plumbing (1,300)**, **langley plumbing (880)**, **furnace repair langley (260)**, south surrey plumbing (170), plumbing and heating langley (50).

**Out-of-scope flags in the tracked list**
- **6 Abbotsford keywords** (boiler repair abbotsford, furnace abbotsford, furnace maintenance abbotsford, furnace repair abbotsford, hot water tank abbotsford, plumber abbotsford). Abbotsford is no longer served (Client Overview, Sept 2026). Remove.
- **fortis rebates** (2,400/mo, informational): not a service. The FortisBC co-op was dropped 2025-09-02. Keep only if the rebate page is still a deliberate lead magnet; otherwise remove.
- **Generic "plumber / plumbing" terms** (about 30 of them) are fine to track, but the pages ranking for them must not promise general repairs (faucets, toilets, drains). See section 4.
- **AC repair terms** (air conditioning repair surrey / langley) were off-limits until 2026-08. They're now allowed, but the live AC and heat pump pages still say "installs only" (CLIENT.md, 2026-09-15 audit).
- **Missing from tracking:** no Navien terms, no heat pump repair terms, no boiler maintenance or strata terms, and no Cloverdale / Walnut Grove / Ocean Park / Grandview Heights terms (priority areas 3, 5, 7 and 9).

### Surrey

44 keywords · 40 ranking in top 100 · 21 in top 10 · 8 in top 3

| Keyword | Pos. 10-05 | Pos. 09-29 | 7-day change | 30-day change | Volume | Ranking URL |
|---|---|---|---|---|---|---|
| boiler services surrey | 1 | 2 | +1 | 0 | 20 | /surrey-boiler-services/ |
| gas fitter surrey | 1 | 1 | 0 | 0 | 70 | / |
| gas line installation surrey | 1 | 5 | +4 | +3 | 10 | / |
| boiler installation surrey | 2 | 3 | +1 | +3 | 10 | / |
| in floor heating surrey | 2 | 5 | +3 | -1 | 10 | /services/plumbing/radiant-in-floor-heating/ |
| best plumber surrey *Track only; no "best" in copy* | 3 | 2 | -1 | 0 | 20 | / |
| radiant heating surrey | 3 | 4 | +1 | +1 | 10 | / |
| water heater south surrey | 3 | 10 | +7 | +5 | 10 | / |
| furnace repair south surrey | 4 | 1 | -3 | -3 | 20 | /services/heating-cooling/furnace-repair/ |
| gas line installation services surrey | 4 | 2 | -2 | 0 | 10 | /services/gas-fitting/ |
| plumbing and heating company surrey | 4 | 23 | +19 | 0 | 10 | / |
| hot water tank installation surrey | 5 | 5 | 0 | 0 | 10 | /services/plumbing/hot-water-tanks/ |
| hot water tank repair surrey | 5 | 5 | 0 | 0 | 20 | /services/plumbing/hot-water-tanks/ |
| hot water tank services surrey | 5 | 5 | 0 | 0 | 10 | /services/plumbing/hot-water-tanks/ |
| tankless water heater repair surrey | 5 | 6 | +1 | +2 | 10 | /services/plumbing/tankless-water-heaters/ |
| hot water tank replacement surrey | 6 | 6 | 0 | +18 | 30 | /services/plumbing/hot-water-tanks/ |
| best plumbers in surrey *Track only; no "best" in copy* | 7 | 7 | 0 | 0 | 20 | / |
| furnace service surrey | 8 | 16 | +8 | -3 | 110 | /services/heating-cooling/furnace-repair/ |
| tankless water heater services surrey | 9 | 8 | -1 | +4 | 10 | /services/plumbing/tankless-water-heaters/ |
| plumbers in surrey bc | 10 | 23 | +13 | 0 | 210 | / |
| plumbers surrey bc | 10 | 13 | +3 | +1 | 210 | / |
| heat pump installation surrey | 11 | 7 | -4 | -2 | 30 | /services/heating-cooling/heat-pumps/ |
| tankless water heater maintenance surrey | 11 | 12 | +1 | -7 | 10 | /services/plumbing/tankless-water-heaters/ |
| plumber in surrey | 12 | 9 | -3 | -2 | 1300 | / |
| tankless water heater installation surrey | 12 | 24 | +12 | -5 | 10 | /services/plumbing/tankless-water-heaters/ |
| furnace installation surrey | 13 | 20 | +7 | +8 | 20 | /services/heating-cooling/furnace-installation/ |
| boiler repair surrey | 14 | 16 | +2 | +1 | 30 | /surrey-boiler-services/ |
| plumber surrey | 14 | 14 | 0 | +11 | 1300 | / |
| plumbers surrey | 15 | 13 | -2 | -6 | 1300 | / |
| heating services surrey | 17 | 17 | 0 | -3 | 10 | / |
| plumbing company surrey | 17 | 17 | 0 | +4 | 110 | / |
| plumbing services surrey | 17 | 27 | +10 | -4 | 90 | / |
| furnace services surrey | 19 | 17 | -2 | -4 | 110 | /services/heating-cooling/furnace-repair/ |
| air conditioner surrey | 22 | 48 | +26 | +9 | 110 | /services/heating-cooling/air-conditioning/ |
| heating installation surrey | 26 | 16 | -10 | -14 | 10 | / |
| plumbing and heating surrey | 26 | 7 | -19 | -17 | 90 | / |
| furnace repair surrey | 31 | 13 | -18 | -22 | 590 | /services/heating-cooling/furnace-repair/ |
| heating service surrey | 32 | 15 | -17 | -16 | 10 | / |
| surrey air conditioning | 41 | 36 | -5 | -8 | 110 | /services/heating-cooling/air-conditioning/ |
| air conditioning services surrey | 54 | 43 | -11 | -14 | 10 | /services/heating-cooling/air-conditioning/ |
| air conditioning repair surrey *Allowed since 2026-08 (repairs now offered)* | – | – | – | 0 | 20 | – |
| plumber south surrey *Dropped out on 10-05 only; may be a one-day blip* | – | 3 | lost | -97 | 170 | / |
| south surrey plumbing | – | – | – | -64 | 170 | – |
| surrey plumbing | – | – | – | 0 | 1300 | – |

### White Rock

25 keywords · 25 ranking in top 100 · 13 in top 10 · 2 in top 3

| Keyword | Pos. 10-05 | Pos. 09-29 | 7-day change | 30-day change | Volume | Ranking URL |
|---|---|---|---|---|---|---|
| radiant heating white rock | 1 | 7 | +6 | 0 | 10 | /services/plumbing/radiant-in-floor-heating/ |
| plumbing and heating white rock | 3 | 3 | 0 | +2 | 20 | / |
| in floor heating white rock | 4 | 5 | +1 | -3 | 10 | /services/plumbing/radiant-in-floor-heating/ |
| boiler repair white rock | 5 | 5 | 0 | 0 | 10 | /white-rock-plumbing/ |
| plumber white rock | 6 | 6 | 0 | +2 | 390 | /white-rock-plumbing/ |
| plumbing services white rock | 6 | 6 | 0 | +1 | 10 | /white-rock-plumbing/ |
| white rock plumbing | 6 | 3 | -3 | 0 | 390 | /white-rock-plumbing/ |
| plumbers white rock bc | 7 | 7 | 0 | 0 | 20 | /white-rock-plumbing/ |
| heat pump installation white rock | 8 | 8 | 0 | 0 | 10 | /services/heating-cooling/heat-pumps/ |
| gas fitter white rock | 9 | 7 | -2 | 0 | 10 | /white-rock-plumbing/ |
| hot water tank replacement white rock | 9 | 8 | -1 | 0 | 10 | /services/plumbing/hot-water-tanks/ |
| plumber in white rock | 9 | 11 | +2 | -1 | 390 | /white-rock-plumbing/ |
| plumbers white rock | 9 | 9 | 0 | -2 | 390 | /white-rock-plumbing/ |
| gas line installation white rock | 11 | 11 | 0 | -7 | 10 | /services/gas-fitting/ |
| tankless water heater services white rock | 12 | 10 | -2 | 0 | 10 | /white-rock-plumbing/ |
| boiler installation white rock | 15 | 14 | -1 | -8 | 10 | /white-rock-plumbing/ |
| furnace installation white rock | 16 | 36 | +20 | +22 | 10 | /services/heating-cooling/furnace-installation/ |
| hot water tank repair white rock | 20 | 24 | +4 | -10 | 10 | /white-rock-plumbing/ |
| heating installation white rock | 24 | 28 | +4 | -6 | 10 | /white-rock-plumbing/ |
| heating service white rock | 25 | 14 | -11 | -18 | 10 | /white-rock-plumbing/ |
| plumbers in white rock bc | 25 | 7 | -18 | -18 | 20 | /white-rock-plumbing/ |
| hot water tank services white rock | 29 | 3 | -26 | -26 | 10 | /white-rock-plumbing/ |
| furnace repair white rock | 32 | 19 | -13 | -15 | 90 | /white-rock-plumbing/ |
| air conditioner white rock | 37 | 19 | -18 | -33 | 10 | /services/heating-cooling/air-conditioning/ |
| furnace service white rock | 37 | 16 | -21 | -34 | 10 | /white-rock-plumbing/ |

### Langley

37 keywords · 21 ranking in top 100 · 4 in top 10 · 2 in top 3

| Keyword | Pos. 10-05 | Pos. 09-29 | 7-day change | 30-day change | Volume | Ranking URL |
|---|---|---|---|---|---|---|
| radiant heating langley | 1 | 2 | +1 | 0 | 10 | /services/plumbing/radiant-in-floor-heating/ |
| in floor heating langley | 2 | 2 | 0 | -1 | 10 | /services/plumbing/radiant-in-floor-heating/ |
| hot water tank repair langley | 5 | 12 | +7 | +6 | 20 | /services/plumbing/hot-water-tanks/ |
| hot water tank replacement langley | 10 | 12 | +2 | -3 | 20 | /services/plumbing/hot-water-tanks/ |
| gas fitter langley | 12 | 15 | +3 | +2 | 40 | /services/gas-fitting/ |
| boiler repair langley | 13 | 40 | +27 | +16 | 10 | /services/heating-cooling/langley-boiler-repair/ |
| hot water tank services langley | 14 | 4 | -10 | -9 | 10 | /services/plumbing/hot-water-tanks/ |
| hot water tank installation langley | 17 | 16 | -1 | -4 | 10 | /services/plumbing/hot-water-tanks/ |
| best plumber langley *Track only; no "best" in copy* | 21 | 19 | -2 | -4 | 10 | /langley-plumbing-and-heating/ |
| plumbers langley bc | 32 | 31 | -1 | 0 | 70 | /langley-plumbing-and-heating/ |
| tankless water heater maintenance langley | 34 | 33 | -1 | -20 | 10 | /services/plumbing/hot-water-tanks/ |
| plumber in langley | 44 | 34 | -10 | -15 | 880 | /langley-plumbing-and-heating/ |
| plumbers langley | 49 | 45 | -4 | -13 | 880 | /langley-plumbing-and-heating/ |
| plumber langley | 50 | 44 | -6 | +50 | 880 | /langley-plumbing-and-heating/ |
| boiler services langley | 59 | 48 | -11 | -29 | 10 | /langley-plumbing-and-heating/ |
| plumbers in langley bc | 59 | 44 | -15 | -58 | 70 | /langley-plumbing-and-heating/ |
| boiler installation langley | 62 | 54 | -8 | -26 | 10 | /langley-plumbing-and-heating/ |
| plumbing company langley | 65 | 61 | -4 | -21 | 10 | /langley-plumbing-and-heating/ |
| plumbing services langley | 65 | 56 | -9 | -27 | 10 | /langley-plumbing-and-heating/ |
| heating services langley | 66 | 62 | -4 | -18 | 10 | /langley-plumbing-and-heating/ |
| heating service langley | 85 | 80 | -5 | -43 | 10 | /langley-plumbing-and-heating/ |
| air conditioner langley | – | – | – | 0 | 90 | – |
| air conditioning repair langley *Allowed since 2026-08 (repairs now offered)* | – | – | – | 0 | 20 | – |
| air conditioning services langley | – | – | – | 0 | 10 | – |
| furnace installation langley | – | – | – | 0 | 20 | – |
| furnace repair langley | – | – | – | -41 | 260 | – |
| furnace service langley | – | – | – | 0 | 40 | – |
| furnace services langley | – | – | – | 0 | 40 | – |
| gas line installation langley | – | – | – | -67 | 10 | – |
| heat pump installation langley | – | – | – | 0 | 10 | – |
| heating installation langley | – | – | – | -64 | 10 | – |
| langley plumbing | – | – | – | -55 | 880 | – |
| plumbing and heating company langley | – | – | – | -67 | 10 | – |
| plumbing and heating langley | – | – | – | -69 | 50 | – |
| tankless water heater installation langley | – | – | – | 0 | 10 | – |
| tankless water heater repair langley | – | – | – | -60 | 10 | – |
| tankless water heater services langley | – | – | – | -65 | 10 | – |

### Abbotsford

6 keywords · 1 ranking in top 100 · 0 in top 10 · 0 in top 3

| Keyword | Pos. 10-05 | Pos. 09-29 | 7-day change | 30-day change | Volume | Ranking URL |
|---|---|---|---|---|---|---|
| boiler repair abbotsford **FLAG: Abbotsford not served** | 46 | 35 | -11 | +54 | 10 | /services/heating-cooling/boiler-repair/ |
| furnace abbotsford **FLAG: Abbotsford not served** | – | – | – | 0 | 20 | – |
| furnace maintenance abbotsford **FLAG: Abbotsford not served** | – | – | – | 0 | 10 | – |
| furnace repair abbotsford **FLAG: Abbotsford not served** | – | – | – | 0 | 170 | – |
| hot water tank abbotsford **FLAG: Abbotsford not served** | – | – | – | 0 | 20 | – |
| plumber abbotsford **FLAG: Abbotsford not served** | – | – | – | 0 | 720 | – |

### No location modifier

1 keywords · 1 ranking in top 100 · 0 in top 10 · 0 in top 3

| Keyword | Pos. 10-05 | Pos. 09-29 | 7-day change | 30-day change | Volume | Ranking URL |
|---|---|---|---|---|---|---|
| fortis rebates *Review: informational; FortisBC co-op dropped 2025-09* | 59 | 47 | -12 | -11 | 2400 | /fortisbc-rebates/ |

## 2. Priority targets by page

**Sources:** "Keyword Research" and "Keyword Mapping 2024" tabs of the Website Audit & KW Research sheet (2024-08 to 2024-12; volumes are Semrush CA national from that time); Client Briefing / Overview (Sept 2026); Semrush tracking (2026-10-05); Slack 2024-12-12 (client asked for furnace repair focus across all 3 markets). Volumes are 2024 figures unless marked (T), meaning tracked volume from 2026-10.

| Page URL | Primary keyword | Secondary keywords | Intent | Source |
|---|---|---|---|---|
| / (homepage) | plumber surrey (720; T 1,300) | plumbers in surrey bc (260), surrey plumber (170), surrey plumbing (140), plumbing companies in surrey (110), plumbers surrey bc, plumbing and heating surrey | Commercial / local | KW Research sheet; tracking |
| /plumbers-near-me/ | plumbers near me | plumber service (1,300), plumbing services (2,400); **no** drain/faucet/toilet terms | Commercial / local | Sheet notes "cannibalizing the home page"; rewrite drafted ([top-5-pages-to-rewrite.md](top-5-pages-to-rewrite.md)) |
| /langley-plumbing-and-heating/ | plumber langley (590; T 880) | plumbing langley (140), langley plumbing (110; T 880), langley plumber (90), plumber langley bc (70), langley plumbing and heating (40) | Commercial / local | KW Research sheet. Drop "plumbing supplies langley" (retail intent) and "langley emergency plumber" until 24/7 is confirmed |
| /white-rock-plumbing/ | plumber white rock (T 390) | white rock plumbing (T 390), plumbers white rock (T 390), plumber in white rock (T 390), plumbing and heating white rock | Commercial / local | Tracking; /white-rock-plumber/ is canonicalised to this page (sheet note) |
| /services/heating-cooling/furnace-repair/ | furnace repair surrey (210 in 2024; T 590) | surrey bc furnace repair (110), furnace repair surrey bc (90), furnace service surrey, furnace repair south surrey, furnace maintenance (3,600), furnace repair services (780) | Commercial / transactional | KW Research sheet (mapped to /services/heating-cooling/furnaces/); Slack 2024-12-12 |
| /services/heating-cooling/furnace-installation/ | furnace installation surrey (40) | furnace installation (5,400), furnace replacement (3,600), replace a furnace (590), furnace installers (320) | Commercial | KW Research sheet (mapped then to /furnace-repair-surrey/); top-5 rewrite #3 |
| /furnace-repair-langley/ (Langley furnace page; exact live URL to confirm) | furnace repair langley (T 260) | langley furnace repair, furnace repair langley bc, furnace installation langley, gas furnace repair langley, lennox furnace repair langley bc | Commercial / local | KW Research sheet. **Drop "mobile home furnace replacement langley bc"**: mobile homes are excluded (2023-10-18) |
| /services/heating-cooling/boiler-repair/ | boiler repair (1,600) | repair a boiler (480), gas boiler repair (110), boiler repair surrey (30), boiler maintenance (110), annual boiler maintenance | Commercial | KW Research sheet; top-5 rewrite #5 |
| /boiler-replacement/ (and /surrey-boiler-services/) | boiler replacement (1,000) | hot water boiler replacement (110, H1), boiler installation (590), new boiler installation (210), boiler replacement cost (50) | Commercial / informational | KW Research sheet. Cannibalization: 4 boiler pages (CLIENT.md, 2026-09-15) |
| /combi-boiler/ | combi boiler (720) | combi boiler canada (110), best combi boiler canada (40), combi boiler installation | Commercial / informational | KW Research sheet |
| /services/navien/ (hub) | navien combi boiler (720) | navien boilers (320), navien tankless repair (720, CA), navien tankless water heater repair (720, CA), navien error codes (category level) | Commercial / informational | KW Research sheet; memory (Sept 2026 audit); Briefing Navien plan |
| /services/plumbing/hot-water-tanks/ | hot water tank installation (590) | hot water tank repair (880), hot water heater repair (480), installation of hot water tank (320), hot water tank replacement surrey | Commercial | KW Research sheet. Legacy /water-heater-repair/ duplicates this page |
| /services/plumbing/tankless-water-heaters/ and /tankless-water-heater-surrey/ | tankless water heater installation (260) | tankless water heater repair (590), tankless hot water heater installation (170), tankless heater installers (110) | Commercial | KW Research sheet. Head terms "tankless water heater" (12,100) and "electric tankless water heater" (1,600) are product-research intent; secondary only |
| /services/gas-fitting/ | gas fitter surrey (T 70, ranks #1) | gas fitters (320), gas fitting (170), gas line installation (260), gas line installer (170), install gas line for stove (90) | Commercial | KW Research sheet; tracking. **Drop "propane gas fittings"** (no propane work). Top-5 rewrite #4 |
| /services/heating-cooling/air-conditioning/ | air conditioner installation (4,400) | ac installation (2,400), air conditioner installer (320), ac replacement (170), air conditioner surrey (T 110), **ac repair surrey (new)** | Commercial | KW Research sheet; Slack 2026-08-20 (repairs now offered) |
| /services/heating-cooling/heat-pumps/ | heat pump installation (1,900) | heat pump installers (720), heat pump install (390), heat pump repair (590), heat pump repair surrey (20) | Commercial | KW Research sheet. Repair terms were mapped in 2024, banned 2024-07 to 2026-08, now allowed again |
| /services/plumbing/radiant-in-floor-heating/ | radiant floor heating (880) | radiant floor heat (320), hydronic heating system (480), in floor radiant heat (210), hydronic radiant floor heating (170) | Commercial / informational | KW Research sheet; ranks #1 to 7 in all 3 markets |
| /services/strata-maintenance/ | strata building maintenance (volume not pulled) | strata boiler specialists, strata building boiler repair | Commercial (B2B residential) | Oct 31 2023 meeting notes |
| /fortisbc-rebates/ | fortisbc rebates (1,000; T 2,400) | fortisbc furnace rebate (90), fortisbc heat pump rebates (70) | Informational | KW Research sheet. Review relevance (section 1 flag) |

## 3. PPC keywords

**Current Google Ads campaigns** (Client Briefing / CLIENT.md, Sept 2026): TP - Hot Water Installs (Tankless & Tanks), TP - Heating Installs, TP - HVAC & Hot Water Repairs, TP - Remarketing, TP - AC Installs. The live keyword lists for these weren't readable from Drive; pull them from the Google Ads account.

**Top paid search terms** (Briefing, early 2026): hot water tank replacement, heater service, heating plumber, navien tankless water heater, navien installation, heat and plumbing.

### TP - Heating & Hot Water Repairs (Focus Areas), built 2024-12-18
Source: Drive `1BwxEARPYnkmBfNpFa7uJdAVZwLh628XLhawIDFIHLp8` (the Ad Copy tab only; per Slack 2024-12-18, keywords and cross-negatives were set up directly in the account, not in the sheet). Launch budget $34.47/day (Slack 2024-12-19). Likely the predecessor of today's "HVAC & Hot Water Repairs".

| Ad group | Final URL | Keyword themes (from paths/headlines) |
|---|---|---|
| Furnace Repair & Maintenance | /services/heating-cooling/furnace-repair/ | furnace repairs, tune-ups, maintenance, gas / hydro / electric furnaces |
| Conventional & Combi Boiler Repair & Maintenance | /services/heating-cooling/boiler-repair/ | boiler repairs, tune-ups, conventional and combi boilers |
| Tankless Heater Repairs & Maintenance | /services/plumbing/tankless-water-heater-repair/ | tankless water heater repair, tune-ups, maintenance |

Ad copy flags: "40+ Years" should become "50 years"; "{LOCATION(City):Surrey}'s Best Hot Water Pros" uses "best" (brand rule: no superlatives). Every ad carries TSBC #LGA0092486 (good: gas licence rule).

### Legacy campaigns, April 2024 export (583 keywords, all phrase match)
Source: Drive `15vmBD7FBIpSpLi8V4CgvXAl-M-0yHkNQUafQUAETVtQ` ("John Sadler Plumbing Keywords"). Campaigns: Surrey | Langley - Leads - Tankless; Surrey | Langley - Leads - Combi Boilers; Surrey | Langley - Navien. The **130 rows highlighted red** are the removal list.

**Red (removed) keywords, 2024-04.** The pattern is price/cost research, broad one-word heads, out-of-area terms and competitor brands:
- **Price / cost:** average cost to replace hot water tank, cost to install hot water tank, hot water tank cost, hot water tank replacement cost (incl. bc / surrey bc), tankless water heater cost / price, tankless heater(s) cost / price / prices, cost of tankless water heaters, hot water on demand cost / price, combi boilers cost / prices, how much to install combi boiler, boiler cost canada, boiler installation cost, cost of boiler replacement, boiler replacement cost (near me), residential boiler prices canada, heat pump cost, heat pump prices (installed), heat pump installation cost, heat pump system cost, navien boiler price, navien water heater price, navien ncb 240 cost to install, navien 240a tankless water heater cost to install, tankless water heater deals
- **Too broad:** boiler, furnace, heating, hvac, water heater, hot water heater, hot water tank(s), heating and cooling, plumbing and heating, home heating options, heater electric, heat saving, pump heat, residential pump, hvac pump, heatpumps
- **Wrong product / not offered:** oil on demand water heater, shower heater, hybrid water heater, hot water pump, hot water storage tank
- **Wrong location:** hot water tank toronto
- **Competitor brands:** viessmann boiler, viessmann boiler price canada, reliance tankless water heater
- **Rebate research:** tankless water heater rebate bc, hot water tank rebates bc
- **Other:** hot water tank leaking (repair ad group), navien canada, broad-match-modifier Navien variants (+navien +tankless etc.)

### Negatives and standing exclusions
- **Brand:** "John Sadler" is a negative in all campaigns (Slack 2024-06-17).
- **Cross-negatives** between ad groups in the Repairs campaign (Slack 2024-12-18; list lives in the account).
- **"Don'ts" list** sent to PPC on 2023-10-18 (Slack, Tim Serrano; Wyatt confirmed "will add all these as negative keywords"): new construction; mobile / manufactured homes; drain cleaning; fire installations; sump pumps; drain tile; pools / pool heaters; commercial and industrial.
- **2024-07-06:** 93 "repair" keywords paused, then narrowed to **heat pump and AC repair only** (Slack thread). Superseded on 2026-08-20 (section 4).
- **Repair ads paused** until late May / early June 2027 (Briefing).
- **Placement exclusions:** daily bot on #thinkprofits-ppc-team (display junk / TLD domains).
- **Navien Specific Tankless** ad group: CA$220.93 spent, 0 conversions; pause was recommended (May 2026, CLIENT.md).

## 4. Keyword rules

Run every new tracked, PPC or content keyword against this list.

| Rule | Status | Date | Source |
|---|---|---|---|
| **Heat pump / AC repair** | **Allowed** (early stage, not pushed hard). The live AC and heat pump pages still say "installs only" and need fixing first | 2026-08-20 | Slack #johnsadler (Andrew); Client Overview |
| Heat pump / AC repair (superseded) | Banned in ads; "they do repair pipes, boilers, hot water tanks, furnaces" | 2024-07-06 | Slack thread (Brittni / Chelsea) |
| Briefing says to drop "AC repairs, heat pump repairs" from tracking | **Stale.** Conflicts with the 2026-08-20 change; keep AC and heat pump repair in the redo | early 2026 | Client Briefing |
| Furnace "service" / "tune up" in ads | Asked by Andrew 2024-12-18; no written answer found. The Repairs campaign launched with "Repairs, Tune-Ups, Services" and "Book Your Annual Maintenance", so treat it as allowed | 2024-12-18 | Slack; Repair Campaign sheet |
| Furnace repair is the #1 keyword focus (Surrey, White Rock, Langley) | Client request | 2024-12-12 | Slack (Brittni, after client meeting) |
| Boiler repair / replacement focus ("customers call these furnace repairs") | Client request | 2023-10-31 | Meeting notes |
| **Navien**: track at category level ("navien error codes", "navien boiler error codes"), not per code or per city. Navien queries route to /services/navien/ | Active | Sept 2026 | Briefing; Client Overview |
| "Navien water tanks" are tankless water heaters; align keywords and ad groups | Active | 2023-10-31 | Meeting notes |
| **Not offered (don't track, bid or write):** general plumbing repairs (faucets, toilets), drain cleaning, new construction, propane / oil (incl. conversions), fire installations, commercial (stratas excepted) | Active | Sept 2026 | Client Overview |
| Also excluded: mobile / manufactured homes, sump pumps, drain tile, pools / pool heaters, industrial | Active | 2023-10-18 | Slack (PPC don'ts) |
| **Abbotsford**: no longer served | Active | Sept 2026 | Client Overview |
| Guildford added to locations | Active | 2023-10-31 | Meeting notes |
| Social / senior housing keywords: OK for SEO, no ad spend (lowest-bid contracts) | Active | 2023-10-31 | Meeting notes |
| Price / cost / "how much" terms excluded from PPC | Active | 2024-04 | Red list |
| Gas ads must show TSBC LGA0092486 | Legal requirement | Sept 2026 | Client Overview |
| No "best" / "#1" in copy (tracking "best plumber surrey" is fine) | Brand rule | 2026 | CLIENT.md section 8 |
| Zero-volume niche terms count as an AEO opportunity, not a reason to drop | Active | Sept 2026 | Client Overview |
| Redo spec: the **same keyword set** across all 3 locations (barring local terms); note each keyword's source (GSC / GBP / competitors); remove low-volume or bad terms; output = final list + add / remove list for Semrush; model on Vision's sheet | Assigned to Francis | 2026-09-04 | Slack (Andrew; followed up twice, no reply in thread) |

## 5. Opportunities

**Hilltop gap (Semrush, same campaign, 2026-10-05).** hilltopplumbing.com outranks Sadler on 34 of the 113 tracked terms, almost all **White Rock** terms, where Hilltop holds #1 on 18:
- High volume: plumber white rock (H 1 vs S 6, 390/mo), plumbers white rock (2 vs 9), plumber in white rock (2 vs 9), white rock plumbing (2 vs 6), furnace repair white rock (1 vs 32, 90/mo).
- South Surrey, where Sadler is based: plumber south surrey (H 7 vs S out of top 100, 170/mo), south surrey plumbing (6 vs not ranking, 170/mo).
- White Rock service terms where Hilltop is #1: boiler repair, furnace installation, furnace service, gas fitter, gas line installation, heat pump installation, heating installation, heating service, hot water tank repair / replacement / services, in floor heating, plumbing services, tankless water heater services, air conditioner.
- This supports the 2026-09-15 audit finding: White Rock has one location page, while Langley has dedicated boiler and furnace pages. Build White Rock boiler-repair and furnace pages.

**Gap keywords (not tracked, worth adding in the redo)**
- Navien: navien tankless repair (720 CA), navien tankless water heater repair (720 CA). Both already rank about #10 to 14 organically on /services/navien/ (memory, Sept 2026). Add navien error codes (category level).
- Repair: heat pump repair (590), heat pumps repair (210), heat pump repair surrey, ac repair surrey / white rock / langley, furnace blowing cold air, heat pump not heating.
- Maintenance: furnace maintenance (3,600 / 4,400 in 2024), boiler maintenance (110), annual boiler maintenance.
- Geography: the priority areas with no tracked terms (Cloverdale, Walnut Grove, Ocean Park, Grandview Heights, Morgan Creek, Crescent Beach), plus Guildford (2023 add).
- Strata: strata building maintenance, strata boiler repair (2023 meeting).
- Older boiler brands for repair content (2023 meeting): Burnham, Slant/Fin, Weil-McLain, Viessmann, Triangle Tube, HTP, Hydrotherm, Laars, Rinnai, IBC, Raypak, SuperHot. Keep Viessmann for SEO repair content only; it's a red PPC term as a product search.
- 2024 "Keyword Opportunities" tab (41 near-me terms): water heater repair (near me), furnace replacement near me, furnace service near me, heating repair near me, heat pump servicing near me, gas line installation, water heater replacement near me, navien tankless water heater. **Exclude** the fireplace / fire installation and gas barbecue terms on that tab (fire installations not offered; gas BBQ lines may be gas fitting, so *confirm with Colin*).

**PAA / FAQ questions already on file** (no new PAA pull was run this session; the PAA standard in `memory/paa-research-standard.md` applies to the redo)
- Boiler repair (Drive, "FAQ Boiler Repair" tab): Does repairing a boiler affect its efficiency? How often should I service my boiler to prevent repairs? What are the signs my boiler needs repair? How can I prevent boiler issues? Should I repair or replace my boiler?
- Navien (Drive, "Blog Topic Ideas" tab): how often to service a Navien tankless water heater; how long Navien tankless water heaters last.
- Plumbers-near-me / Langley rebuild FAQs (repo): are your plumbers licensed; what areas do you cover; do you charge for estimates; typical response time; emergency / after-hours; brands; Navien certification; tankless installs; strata maintenance plans; Fort Langley / Willoughby coverage. Estimate, response-time and 24/7 answers are still blocked on the client.
- Tina's idea (2023-10-31): a plain-language "what heating system is right for me" section.

**Sept 2026 keyword-redo status**
- 2026-08-20: Andrew flagged that the tracked list needs redoing (AC / heat pump repairs now offered).
- 2026-09-04: spec sent (section 4). Andrew followed up twice in the thread; no reply or sheet link found in Slack.
- Drive search found **no Sept/Oct 2026 tracked-keyword sheet**. Memory mentions a "Keyword Tracking Review (Sept 2026)" sheet (2026-09-07) owned by francis@thinkprofits.com, but no search returned it (also noted in CLIENT.md section 13). Find it or rebuild it.
- Suggested redo moves, based on this file: drop 6 Abbotsford terms; review fortis rebates; add AC / heat pump repair, Navien category, maintenance and priority-area terms; mirror one keyword set across Surrey / White Rock / Langley.

## 6. Gaps

- **Per-location Semrush campaigns not resolved.** The API exposes one 113-keyword campaign; its search location and the Briefing's 70 / 130 / 116 split couldn't be confirmed. Check the Semrush UI.
- **Semrush volume level** (local vs regional vs national) not confirmed for the campaign.
- **Live Google Ads keyword and negative lists** not pulled (no Ads access in this session; the 2024-12 sheet holds ad copy only).
- **Sept 2026 "Keyword Tracking Review" sheet** and Vision's model sheet (`1wldjAsTudm_KWKUf2F83iGPFf-tuXBzXIUQ-MvbHl08`) not found / not read.
- **No fresh PAA pull** (Semrush `phrase_questions`) and **no GSC query data** (no agency access to `sc-domain:johnsadler.ca`).
- **2024-12-18 "furnace service / tune up" question:** no written reply found in Slack.
- Drive `125WC8bVJSR9NKgxChL94uJytvTjuTKyB` is an .xlsx copy of the audit workbook. The text read was truncated, so only its notes columns were checked; the keyword tabs were read from the Google Sheet version.
- **Security note:** the Website Audit sheet's "Citation" tab stores a directory-site username and password in plain text. Consider moving it to a password manager.
