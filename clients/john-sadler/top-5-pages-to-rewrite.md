# John Sadler Plumbing & Heating — Top 5 Pages to Rewrite

Ranked by YoY impression loss, GSC "Performance on Search" export (3 months vs. same period last
year, pulled 2026-08-28). Non-blog/service pages only, per request. See
[top-5-pages discussion](#status--next-step) below each row for current status.

| # | Page | Impressions YoY | Clicks YoY | Status |
|---|---|---|---|---|
| 1 | [johnsadler.ca/plumbers-near-me/](https://www.johnsadler.ca/plumbers-near-me/) | -84.5% (47,535 → 7,365) | -5 | Rewritten — blocked on 3 client answers |
| 2 | [johnsadler.ca/langley-plumbing-and-heating/](https://www.johnsadler.ca/langley-plumbing-and-heating/) | -47.7% (45,762 → 23,941) | -14 | Confirmed thin — HTML rebuild pilot, not started |
| 3 | [johnsadler.ca/services/heating-cooling/furnace-installation/](https://www.johnsadler.ca/services/heating-cooling/furnace-installation/) | -67.9% (32,042 → 10,297) | -1 | Not yet checked live |
| 4 | [johnsadler.ca/services/gas-fitting/](https://www.johnsadler.ca/services/gas-fitting/) | -70.3% (30,229 → 8,993) | -21 (biggest click loss of the five) | Not yet checked live |
| 5 | [johnsadler.ca/services/heating-cooling/boiler-repair/](https://www.johnsadler.ca/services/heating-cooling/boiler-repair/) | -53.5% (33,392 → 15,522) | -5 | Not yet checked live |

## 1. [Plumbers Near Me](https://www.johnsadler.ca/plumbers-near-me/)

Worst impression collapse on the site (non-blog). Rewrite already built this session:

- [plumbers-near-me.html](./plumbers-near-me.html) — full standalone page (topbar/hero/footer included)
- [plumbers-near-me-sections/](./plumbers-near-me-sections/) — same content split into 6 paste-in WordPress blocks, FAQ schema embedded
- Blocked on: estimate-fee policy, typical response time, 24/7/emergency policy — see the 3 placeholder `<span class="placeholder">` tags inside [06-faq.html](./plumbers-near-me-sections/06-faq.html)

**Internal links already in the rebuild:** → [/langley-plumbing-and-heating/](https://www.johnsadler.ca/langley-plumbing-and-heating/), → [/white-rock-plumbing/](https://www.johnsadler.ca/white-rock-plumbing/) (the only two service-area pages confirmed to exist on the live site — verified via live DOM check, not guessed)

## 2. [Langley Plumbing & Heating](https://www.johnsadler.ca/langley-plumbing-and-heating/)

Confirmed thin on live check: ~200 words of body content (443 total incl. nav/footer), generic
bullet lists, no FAQ, footer stuck at "Copyright © 2025". Selected in the Aug 26, 2026 scrum as
the team's HTML-rebuild test page.

**Should internally link to/from once rebuilt:**
- ← [/plumbers-near-me/](https://www.johnsadler.ca/plumbers-near-me/) (already links here)
- ↔ [/white-rock-plumbing/](https://www.johnsadler.ca/white-rock-plumbing/) (sibling location page — cross-link both directions once Langley is rebuilt, matching the pattern already live between the two hot-water-tank pages)
- ↔ [/services/plumbing/](https://www.johnsadler.ca/services/plumbing/) (parent service hub)

**Not yet built.** Reference [brand.md](./brand.md) for colors/fonts/tone before rebuilding — same palette used in the plumbers-near-me rebuild.

## 3. [Furnace Installation & Replacement](https://www.johnsadler.ca/services/heating-cooling/furnace-installation/)

Impressions down 67.9% YoY. **Not yet opened live this session** — flagged from GSC data alone,
content quality unconfirmed. Do not treat as "thin" until checked; could be a technical/internal-
linking issue instead (see the Discussion Queries in the earlier roadmap summary).

**Likely internal-linking neighbors once investigated:**
- ↔ [/services/heating-cooling/furnace-repair/](https://www.johnsadler.ca/services/heating-cooling/furnace-repair/) (sibling page, confirmed strong content — good internal-link source)
- ↔ [/services/heating-cooling/](https://www.johnsadler.ca/services/heating-cooling/) (parent hub)

## 4. [Gas Fitting](https://www.johnsadler.ca/services/gas-fitting/)

Impressions down 70.3% YoY *and* the biggest click loss (-21) of these five pages. **Not yet
opened live this session.**

**Likely internal-linking neighbors:**
- ↔ [/services/](https://www.johnsadler.ca/services/) (parent hub)
- ↔ [/blog/navien-dual-fuel-promo/](https://www.johnsadler.ca/blog/navien-dual-fuel-promo/) (flagged separately as an expired-offer page needing its own fix — currently dead weight, not a good link source until fixed)

## 5. [Boiler Repair](https://www.johnsadler.ca/services/heating-cooling/boiler-repair/)

Impressions down 53.5% YoY. **Not yet opened live this session.**

**Likely internal-linking neighbors:**
- ↔ [/boiler-installs-replacement/](https://www.johnsadler.ca/boiler-installs-replacement/)
- ↔ [/combi-boiler-installation-and-repair/](https://www.johnsadler.ca/combi-boiler-installation-and-repair/) (confirmed thin separately — combi is a related but distinct system type, cross-link don't merge)

## Status & next step

Pages 3-5 need the same live-page check already done for pages 1-2 before committing to a
rewrite — the drop is confirmed by data, the cause (thin content vs. technical vs. lost links)
is not yet confirmed for those three. Say the word and I'll check them the same way.

## Related files in this folder

- [brand.md](./brand.md) — colors, fonts, voice, NAP, known sitewide inconsistencies
- [plumbers-near-me.html](./plumbers-near-me.html) — full rebuilt page (page #1 above)
- [plumbers-near-me-sections/](./plumbers-near-me-sections/) — same page as pasteable WordPress blocks
