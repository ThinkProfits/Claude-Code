# SPIEDR internal links, November 2026 (roadmap Phase 1, November report commitment)

**Status: PROPOSED. Nothing is live yet. Waiting on Francis's OK before any edit on spiedr.com.**

Built 2026-11-19 from the live REST content of 99 source pages (`/roof-sprinkler-system/`, `/mark-3-pump/` and every `/blog/` post), fetched with a browser User-Agent. Each row wraps a phrase that **already sits in the source sentence** (roadmap rule: edit existing sentences, don't write new copy). Edits go through `wp-spiedr` only, one post at a time, checking the live page after each.

Targets are the four pages named in the November report as slipping (GSC avg position, Oct 2026 vs Oct 2025): fire service trailers 8.0 to 17.5, equipment rentals 11.1 to 22.1, wildfire consulting 13.8 to 26.4, sprinkler kits 11.1 (Aug) to 21.0.

| Target | URL | Content inlinks today (REST scan) |
|---|---|---|
| Fire service trailers | `/sprinkler-trailers/fire-service-trailers/` (page 5858) | 3 (one blog, site map, history) |
| Equipment rentals | `/fighting-equipment-rentals/` (page 5915) | 5 direct, plus 6 via the old `/equipment-rentals/` 301 |
| Wildfire consulting | `/services/wildfire-consulting/` (page 5809) | 33 direct, plus 12 via the old `/services/consulting/` 301 |
| Sprinkler kits | `/sprinkler-kits/` (page 5900) | 14 |

## A. New in-content links (21)

### Fire service trailers → `/sprinkler-trailers/fire-service-trailers/`

| # | Source (ID) | Anchor (existing text) | Sentence |
|---|---|---|---|
| T1 | `/mark-3-pump/` (7277) | Structure Protection Trailers | "…we have manufactured 98% of all purchased Structure Protection Trailers in Canada." |
| T2 | `/blog/b-c-wildfires-rise/` (7208) | SPIEDR sprinkler trailer | "Our SPIEDR sprinkler trailer can protect up to 50 homes." |
| T3 | `/blog/maintenance-tips-for-wildfire-protection-equipment-in-british-columbia-canada/` (8676) | sprinkler trailer | "If a firefighter relies on a sprinkler trailer but it fails…" |
| T4 | `/blog/early-wildfire-detection-in-bc-how-faster-warnings-reduce-response-time-and-damage/` (8914) | sprinkler trailers | "Structure protection units and sprinkler trailers are designed to be deployed quickly by a small crew." |
| T5 | `/blog/wildfire-preparedness-in-winter/` (8797) | structure protection trailer | "…a full off-season inspection for every structure protection trailer or sprinkler kit you operate." |
| T6 | `/blog/advanced-firefighting-equipment-in-combating-california-wildfires/` (8709) | Sprinkler trailers (body sentence, not the H-tag) | "Sprinkler trailers are designed for rapid deployment across large areas." |

### Equipment rentals → `/fighting-equipment-rentals/`

| # | Source (ID) | Anchor | Sentence |
|---|---|---|---|
| R1 | `/roof-sprinkler-system/` (8254) | fire fighting equipment rentals | "SPIEDR contributes to the safety of communities by providing fire fighting equipment rentals, wildland fire suppression training, and consulting services." |
| R2 | `/blog/firesmart-your-property-with-wildfire-mitigation/` (8724) | equipment rental services | "SPIEDR's ongoing training and equipment rental services ensure systems remain operational…" |
| R3 | `/blog/canada-wildfire-season-began-early/` (8212) | Equipment rentals | List item "Equipment rentals and deployment planning" |
| R4 | `/blog/defensible-space/` (8482) | equipment rentals | "…through wildland fire consulting, equipment rentals, and training…" |
| R5 | `/blog/double-hazard-zones/` (8017) | Wildland fire equipment rentals | List item |
| R6 | `/blog/bc-wildfire-app/` (7705) | Equipment rentals | List item "Equipment rentals" |

### Wildfire consulting → `/services/wildfire-consulting/`

| # | Source (ID) | Anchor | Sentence |
|---|---|---|---|
| C1 | `/roof-sprinkler-system/` (8254) | consulting services | Same sentence as R1 (two links in one sentence; both are genuine) |
| C2 | `/blog/wildfire-protection-orchards/` (8695) | professional wildfire consulting | "In addition to professional wildfire consulting based on FireSmart and Firewise principles…" |
| C3 | `/blog/firesmart-your-property-with-wildfire-mitigation/` (8724) | SPIEDR's consulting team | "SPIEDR's consulting team advises clients on landscaping layouts that minimize fuel near buildings." |
| C4 | `/blog/okanagan-wildfire-risks/` (8716) | property-specific wildfire risk assessments | "Conduct property-specific wildfire risk assessments with experts like SPIEDR." (the "SPIEDR" link to `/services/` stays) |
| C5 | `/blog/2025-wildfire-outlook/` (8713) | wildfire risk assessment specialists | "Work with wildfire risk assessment specialists to evaluate potential hazards specific to your property." |
| C6 | `/blog/essential-wildland-firefighting-equipment/` (7977) | Consulting and planning for wildfire readiness | List item |

### Sprinkler kits → `/sprinkler-kits/`

| # | Source (ID) | Anchor | Sentence |
|---|---|---|---|
| K1 | `/roof-sprinkler-system/` (8254) | sprinkler kits | "We carry a variety of sprinklers and sprinkler kits, including the RAINMAKER sprinkler." |
| K2 | `/blog/wildfire-preparedness-in-winter/` (8797) | sprinkler kit | Same sentence as T5 |

Only two strong kit mentions exist outside pages that already link there; the kits page is already the best-linked of the four. `/mark-3-pump/` has no unlinked kit, rental or consulting mention, so its only row is T1.

## B. Fix links that go through a 301 (same anchor, swap the URL)

These already point at the right page but take a redirect hop. Low risk, no copy change.

| Old href | New href | Pages |
|---|---|---|
| `/services/consulting/` | `/services/wildfire-consulting/` | homepage (5243), how-wildfire-consultants-help (8698, 2 links), firesmart-your-property (8724), wildfire-protection-orchards (8695), examining-the-wildfire-impact (8583), prevent-wildfire (7720), bc-wildfire-app (7705), ai-wildfire-monitoring (7690), emergency-kits (7609), specialized-suppression-tactics (7421), 6-tactics (7387), british-columbias-disaster-budget-for-2019 (7348) |
| `/equipment-rentals/` | `/fighting-equipment-rentals/` | homepage (5243), how-wildfire-consultants-help (8698), wildfire-protection-orchards (8695), emergency-kits (7609), everything-you-need-to-know-about-bc-fire-bans (7531), wildfire-consulting page (5809) |
| `/training/` | `/wildfire-fighting-training/` | how-wildfire-consultants-help (8698), plus any others found during the edit |

Homepage and WPBakery pages store some links inside encoded `vc_btn` / raw blocks (see `memory/spiedr-context.md`). Edit those by hand in wp-admin if the MCP replace can't reach them.

## Notes for Francis

- **Duplicate trailer pages:** `/sprinkler-trailers/` (5855) and `/spiedr-sprinkler-trailers/` (7118) are both indexed with self-canonicals and cover the same topic. `/sprinkler-trailers/` gets the clicks (76 in Jul–Oct GSC). Not touched here; worth a consolidation decision later.
- Roadmap Phase 1 (roof sprinkler, Mark-3, fire embers, fire pump systems) is a separate list in `spiedr-fix-roadmap-2026-q4.md`. This file covers the four pages promised in the November thread.
- After edits: re-run the REST scan and fill in the "Live" column below.

## Edit log

| # | Live? | Date | Checked on live page |
|---|---|---|---|
| (fill in after approval) | | | |
