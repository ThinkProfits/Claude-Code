# SPIEDR — Remediation Roadmap

**Client:** SPIEDR Ltd. (www.spiedr.com)
**Triggered by:** 6 September 2026 monthly report + follow-up investigation (17 September 2026)
**Owner:** Francis Marc Uy (SEO) · **Account lead:** Shawn Moore
**Horizon:** 18 September – 12 November 2026 (8 weeks), plus ongoing reporting hygiene
**Companion doc:** `spiedr-sept-2026-ranking-and-internal-linking-review.md` (evidence, daily rank data, full link map)

---

## What this roadmap fixes

The September report flagged Top 3 / Top 10 keyword losses and recommended internal linking work. The investigation found that most of the flagged losses were a month-boundary reporting artifact, but that the underlying diagnosis was right for the wrong reason: SPIEDR's best-performing pages receive almost no internal links, and the blog is structurally cut off from the rest of the site.

Four problems, in order of business impact:

1. **Money pages with zero internal support.** `/roof-sprinkler-system/` and `/fire-embers/` receive no in-content internal links at all, despite ranking well.
2. **A #1 position starting to slip.** `/mark-3-pump/` carries "portable fire pumps canada" — #1 until 11 September, position 16 by 16 September — on two inbound links.
3. **A dark blog.** 45 of 93 posts have no in-content inbound links, including the page that ranks for the domain's largest search volume.
4. **A reporting layer that generates false alarms.** Day-1-vs-day-31 comparison plus a keyword set that is 94% near-zero volume.

The GBP data gap flagged in the same report is tracked here as a parallel track but is not an SEO deliverable.

---

## Success measures

Measured against the 1–30 September baseline, reviewed at the 6 November and 6 December reports.

| Measure | Baseline (Sept 2026) | Target | Review point |
|---|---|---|---|
| Pages with zero in-content inbound links | 48 of 163 | Under 10 | 6 Nov report |
| Blog posts with zero in-content inbound links | 45 of 93 | Under 10 | 6 Dec report |
| `/roof-sprinkler-system/` — best position in its cluster | #12 | Top 10 | 6 Dec report |
| `/blog/…bc-fire-bans…/` — best position in its cluster | #25 | Page 2 (top 20) | 6 Dec report |
| GSC clicks (national, monthly) | 488 | Directional improvement | 6 Dec report |
| Tracked keywords with volume above 50/mo | 3 of 47 | 20 or more | 6 Oct report |

These are targets, not commitments. Rankings respond to competitor activity and Google algorithm changes that sit outside our control — the work below improves internal link equity, crawl depth and topical structure, which are the inputs we can actually influence.

---

## Phase 0 — Baseline and approvals

**Week 1 · 18–24 September · Est. 3–5 hours**

Everything downstream compares against this baseline, so it has to be captured before any edits ship.

| # | Task | Owner | Notes |
|---|---|---|---|
| 0.1 | Post the Slack thread reply on the September report | Francis | Draft ready at `slack-thread-reply-draft.md` — needs review before posting |
| 0.2 | Run a Screaming Frog crawl of spiedr.com and archive to `crawls/spiedr/` | Francis | None on file. Send a browser User-Agent — the site sits behind Mod_Security and rejects default crawler headers |
| 0.3 | Export Semrush Position Tracking daily data for 1–30 Sept as the baseline | Francis | Campaign 2084675 |
| 0.4 | Export GSC page-level performance for September | Francis | National, all devices |
| 0.5 | Confirm who ships on-page edits — SPIEDR's team or ours | Shawn | **Blocking for Phase 1.** Determines whether Phase 1 is a task list or a build |
| 0.6 | Confirm whether WordPress edits need client sign-off per page or batch approval | Shawn | Affects Phase 1 and 3 turnaround |

**Exit criteria:** crawl archived, baselines exported, edit path and approval model confirmed.

---

## Phase 1 — High-leverage internal links

**Weeks 1–2 · 18 September – 1 October · Est. 8–12 hours**

The highest return per hour on the account. Every link below has its anchor phrase already sitting in the source page's body copy, so this is editing existing sentences, not writing new content. No new pages, no design work.

### 1A. `/roof-sprinkler-system/` — from zero inbound links to six

Six commercial keywords, roughly 460 combined monthly searches, all stuck between positions 12 and 21. This page is also behind one of the two confirmed ranking declines.

| Source page | Existing mentions | Suggested anchor direction |
|---|---|---|
| `/product/rainmaker/` | 6 | "roof sprinkler system" in the product description |
| `/wildfire-sprinkler-kit/` | 4 | "rooftop sprinkler protection" |
| `/fire-embers/` | 3 | "roof sprinklers" where ember ignition is discussed |
| `/blog/what-to-do-in-a-wildfire-evacuation/` | 2 | "roof sprinkler system" |
| `/blog/firesmart-your-property-with-wildfire-mitigation/` | 2 | "roof sprinkler system" |
| `/blog/does-rain-really-reduce-wildfire-risk/` | 2 | "roof sprinklers" |

### 1B. `/mark-3-pump/` — defend the slipping #1

Thirteen pump product pages already name the Mark-3 and none of them link to the hub page. This is the single cheapest defensive action on the account.

Priority order by existing mention density: `/product/mark-3-b2-10hp-mid-range/` (13), `/product/mark-3-qs-10hp-high-pressure/` (11), `/product/rancher-65-gallon/` (5), `/shop/` (4), `/product/striker3-13hp-portable/` (4), `/product/bb-4-21hp-high-pressure-portable/` (4), `/product/bb-4-18hp-high-pressure-portable/` (4), then the remaining seven pump product pages.

Vary anchors across "Mark-3 portable fire pump", "portable fire pumps in Canada", "our Mark-3 pump range" — do not repeat one string thirteen times.

### 1C. `/fire-embers/` — support the top traffic page

The site's highest-traffic organic page (#5 for "what is embers", 110/mo) receives nothing. Twenty-eight pages already mention embers. Place 8–10 links, starting with:

`/roof-sprinkler-system/` (10 mentions) · `/blog/defensible-space/` (7) · `/blog/firesmart-your-property-with-wildfire-mitigation/` (6) · `/structure-protection-sprinklers/` (5) · `/blog/preparing-for-wildfires-property-owner-guide/` (5) · `/blog/preparing-for-wildfire-evacuation/` (5) · `/blog/okanagan-wildfire-risks/` (5) · `/spiedr-wildfire-sprinkler-kit/` (4)

Note that 1A and 1C reciprocate — `/roof-sprinkler-system/` and `/fire-embers/` should link to each other. Both pages sit on the same ember-ignition topic and the relationship is genuine, not manufactured.

### 1D. `/spiedr-fire-pump-protection-systems/` — support a confirmed decline

Position 17 for "fire fighting pumps" (50/mo), one inbound link, and behind the "fire fighting pumps for sale" drop. No page currently uses the exact phrase without linking, so these need a sentence written rather than a word wrapped:

`/mark-3-pump/` · `/waterax-pumps/` · `/sprinkler-trailers/` · `/blog/history-of-wildfire-equipment/` · `/blog/essential-wildland-firefighting-equipment/` · `/blog/maintenance-tips-for-wildfire-protection-equipment-in-british-columbia-canada/`

**Exit criteria:** roughly 30 in-content links placed across four target pages; a re-crawl confirms each target's inbound count. **Ships before 1 October so the effect lands in October data and reads in the 6 November report.**

---

## Phase 2 — Reporting hygiene and the second tier of pages

**Weeks 3–4 · 2–15 October · Est. 6–9 hours**

### 2A. Rebuild the Position Tracking keyword set

Must land before the 6 October report is built, or the October report repeats September's false alarms.

- Remove or de-prioritise the near-zero-volume terms that generate the Top 3 / Top 10 churn (44 of 47 keywords sit at 0–30/mo).
- Add the terms SPIEDR genuinely ranks for at volume: the BC fire ban cluster ("fire ban bc" 5,400, "bc fire ban" 3,600, "bc burning ban" 720, "fire ban in bc" 720), the roof sprinkler cluster, the ember cluster, and "waterax" (480).
- Keep a small tagged group of the current brand and product terms so historical continuity is not lost — tag them separately rather than deleting.

### 2B. Fix how the report reads rank movement

- Report month-over-month position change using a **monthly average**, or a 7-day average at each endpoint, rather than day 1 versus day 31. This is what turned a two-day wobble into a reported -13.
- Add a note wherever Position Tracking and GSC sit side by side: Position Tracking for this campaign is **Desktop / British Columbia only**, GSC is **national**. They will never agree, and readers should know why.

### 2C. Second-tier link targets

Lower volume than Phase 1 but still unsupported: `/spiedr-sprinkler-trailers/` (0 inbound links), `/spiedr-wildfire-sprinkler-kit/` (5), `/about-us/history/` (1), `/waterax-pumps/` (add links from `/mark-3-pump/`, `/sprinkler-trailers/`, `/products/`).

**Exit criteria:** refreshed keyword set live in Semrush before the October report is assembled; reporting template updated; second-tier links placed.

---

## Phase 3 — Blog architecture

**Weeks 5–8 · 16 October – 12 November · Est. 14–20 hours**

The structural fix. Forty-five posts currently sit behind a ten-page paginated archive with no contextual links reaching them — including the page carrying the largest search volume on the domain.

| # | Task | Owner | Effort |
|---|---|---|---|
| 3.1 | Group the 93 posts into three or four topic hubs — Wildfire Preparedness, BC Fire Bans & Regulations, Equipment & Pumps, Wildfire Science | Francis | 3–4 h |
| 3.2 | Build hub landing pages that link every post in their cluster | Dev + Content | 6–8 h |
| 3.3 | Link the hubs from the main navigation or a resources block so they are not themselves orphaned | Dev | 1–2 h |
| 3.4 | Add a "related reading" block of 3–4 contextual links to the 20 highest-potential posts | Content | 4–6 h |
| 3.5 | Refresh and prominently link `/blog/…bc-fire-bans-and-restrictions/` | Content + Francis | Folded into 3.4 |

**On the BC fire bans post specifically:** it ranks #25–31 across roughly twenty BC fire ban variants totalling well over 15,000 monthly searches. Moving it to page 2 needs no new page — a content freshness pass (the regulations change annually) plus real internal links. It is the highest-ceiling single item in this roadmap and the slowest to pay off, which is why it sits in Phase 3 rather than Phase 1.

**Exit criteria:** every blog post reachable in two clicks from the home page with at least one contextual inbound link; hubs indexed.

---

## Parallel track — Google Business Profile data gap

**Week 1 onward · Owner: whoever holds GBP access · Not an SEO deliverable**

The report shows 0 reviews, 0 average rating and 0 call clicks against 1.32K impressions. That reads as a tracking or sync failure rather than a true zero.

- Confirm the GBP listing is still connected to the reporting integration and that the correct location is mapped.
- Check whether call-click tracking is enabled on the listing.
- If reviews genuinely are zero, that is a separate conversation with Bob and Natalie about a review generation programme — worth raising either way.

Note for whoever picks this up: the `gbp-audit` MCP tool is currently hard-blocked at 0 requests/minute and needs a Cloud Console fix before it can be used. BrightLocal is the working alternative.

---

## Sequence and dependencies

```
Week 1   [Phase 0: baseline + approvals] ──┐
Week 1-2 [Phase 1: 30 links, 4 pages] ─────┤ must ship before Oct 1
Week 3-4 [Phase 2: keyword set + template] ┤ must land before Oct 6 report
Week 5-8 [Phase 3: blog architecture] ─────┘ payoff visible Dec report
         [GBP track: parallel, independent]
```

**Hard dependencies**

- Phase 1 cannot start until task 0.5 confirms who ships the edits.
- Phase 2A must complete before the 6 October report is assembled, or October repeats September's false alarms.
- Phase 3.2 depends on the WordPress theme supporting hub templates — confirm with the dev team in Week 1 so it is not discovered in Week 5.

**Effort envelope:** roughly 31–46 hours total across eight weeks, assuming our team ships the edits. If SPIEDR's team ships them instead, our side drops to roughly 18–25 hours and the schedule extends by their turnaround. These are estimates based on the page counts above, not a fixed quote.

---

## Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Client approval per page slows Phase 1 past 1 October | Medium | Seek batch approval for internal link edits in Week 1 (task 0.6) — these do not change page copy meaningfully |
| The 11–12 September SERP movement continues and masks our gains | Medium | Baseline captured in Phase 0; report our changes against page-level GSC impressions, not position alone |
| Theme cannot support hub templates without dev work | Medium | Confirmed in Week 1, before Phase 3 is scheduled |
| Internal linking alone does not move page-2 rankings | Medium | Phase 3 pairs links with content refresh; if the December review shows no movement, escalate to a content depth and backlink assessment |
| Report continues to generate false alarms if 2A slips | Low | Owner and hard date assigned; single Semrush change |

---

## Review points

- **6 October 2026** — September report. Phase 1 complete, Phase 2A live. Expect no ranking change yet; report the work shipped and the corrected reading of the August drop-offs.
- **6 November 2026** — October report. First data reflecting Phase 1. Check `/roof-sprinkler-system/` and `/mark-3-pump/` movement and the orphan-page count.
- **6 December 2026** — November report. Phase 3 complete. Full assessment against the success measures table above.
