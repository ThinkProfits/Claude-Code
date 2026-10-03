# SPIEDR — September 2026 report follow-up

**Scope:** the two items flagged in the automated review of the 6 Sep 2026 report — (1) Top 3 / Top 10 keyword drop-offs, and (2) internal linking around newly #1-ranking pages.

**Prepared:** 17 September 2026 · Francis Marc Uy (SEO)

**Data sources:** Semrush Position Tracking (project 2084675, campaign `www.spiedr.com`, Desktop / British Columbia / Google), Semrush Organic Research (`ca` database), and a full link crawl of the 163 URLs in spiedr.com's XML sitemaps (39 pages, 93 posts, 31 products; 162 fetched successfully).

**Not covered here:** the Google Business Profile zeroed reviews/call clicks. That is a separate action item and has not been investigated.

---

## 1. The Top 3 / Top 10 drop-offs

### Short version

Most of the flagged erosion is a month-boundary snapshot artifact, not a trend. Two keywords are genuine declines. And a third issue — one the report could not have seen — opened up around 11–12 September and is worth raising with the client now.

### The headline "collapse" did not happen

The summary singled out **"structural fire protection"** falling 13 spots, from position 6 to 19. The daily series tells a different story:

```
Aug 01–15   6 5 5 6 6 6 4 6 6 6 6 6 6 6 6
Aug 16–29   12 12 12 12 12 12 12 11 7 7 7 7 7 7
Aug 30–31   19 19
```

The keyword held position 6–7 for 29 of 31 days and only touched 19 on the final two days of the month. Because the report compares 1 Aug against 31 Aug, a two-day wobble is rendered as a -13 collapse.

September confirms it: the keyword sat at 6–7 for most of the month and is at **7** as of 16 September.

**"structural fire protections systems"** is the same story — position 1–3 for most of August, 7 on the last day, back to 3–6 through September.

Both keywords point at the same page, `/structural-protection-unit/`, which is not weakly linked (22 in-content inbound links). There is no underlying problem to fix here.

### Two genuine declines

| Keyword | Aug 1 | Aug 31 | Sept 16 | Landing page | Verdict |
|---|---|---|---|---|---|
| top wildfire sprinkler protection | 3 | 9 | 14 | `/structure-protection-sprinklers/` | **Real.** Has not recovered; drifting further. |
| fire protection roof sprinkler system | 8 | 13 | 14 | `/roof-sprinkler-system/` | **Real.** Flat at 13–14 since mid-August. |
| fire fighting pumps for sale | 9 | 12 | 18 | `/spiedr-fire-pump-protection-systems/` | **Real but noisy.** Swings 8–18 daily. |

All three land on pages with weak or no internal link support — see section 2. That is the most plausible common cause and the cheapest thing to test.

### Noise, not signal

- **wildland sprinkler kits** (3 → 4) and **wildfire protection systems** (15 → 16): within normal daily variance.
- **wildland fire pumps**: swung between 1, 3, 16, 19 and unranked within August alone. This SERP is unstable; do not read a trend into it.

### New since the report — worth flagging to the client

Three keywords that were stable or #1 through the reporting period moved sharply around **11–12 September**:

| Keyword | Through Sept 11 | Sept 16 | Landing page |
|---|---|---|---|
| portable fire pumps canada | 1 | 16 | `/mark-3-pump/` |
| wildland fire structure protection | 1 | 7 | `/structure-protection-sprinklers/` |
| wildland fire pumps | 3 (Sept 1) | 21 for most of Sept | `/mark-3-pump/` |

Three unrelated keywords moving on the same two days points to a SERP-side event rather than anything on the site. It should be monitored and reported next cycle rather than chased, but the client should hear it from us first.

### One caveat on the whole keyword set

44 of the 47 tracked keywords have a monthly search volume of 0–30. A ±5 position swing on a 10-searches-per-month keyword carries almost no business meaning, and it is what produces most of the Top 3 / Top 10 churn in these reports. Meanwhile **"bc wildfire service" (2,900/mo)** is tracked and unranked, and the highest-volume terms SPIEDR actually ranks for nationally — "fire ban bc" (5,400), "bc fire ban" (3,600) — are not in the campaign at all.

**Recommendation:** refresh the Position Tracking keyword set before the next report so the Top 3 / Top 10 counts track terms that move the business.

---

## 2. Internal linking

The report's recommendation — build internal links around the newly #1 pages — is right, but understates the problem. Several of SPIEDR's best-ranking pages currently receive no in-content internal links at all.

### Method

All 163 sitemap URLs were fetched and parsed. `<header>`, `<nav>` and `<footer>` were stripped before counting, so the figures below are **in-content contextual links only** — not menu or template links. Links from `/site-map/` are excluded as they carry no editorial signal.

### Pages that rank well and get no internal support

| Page | Contextual inlinks | Ranks for (Semrush, `ca`) |
|---|---|---|
| `/roof-sprinkler-system/` | **0** | roof fire sprinklers (90) #12 · roof fire sprinkler system (70) #14 · roof sprinkler system (90) #17 · roof sprinklers fire (90) #19 · roof sprinklers (110) #20 · roof sprinkler (50) #21 |
| `/fire-embers/` | **0** | what is embers (110) #5 · embers in the fire (110) #7 · fire ember (140) #12 · fire embers (140) #13 · ember fire (70) #14 — **the site's top organic traffic page** |
| `/spiedr-sprinkler-trailers/` | **0** | — |
| `/spiedr-fire-pump-protection-systems/` | **1** | fire fighting pumps (50) #17 |
| `/mark-3-pump/` | **2** | wildland fire pumps (140) #14 · wajax pump (70) #20 · portable fire pump (70) #20 · mark 3 pump (170) #23 |
| `/about-us/history/` | **1** | — |
| `/spiedr-wildfire-sprinkler-kit/` | **5** | — |

`/roof-sprinkler-system/` is the clearest opportunity on the site: six commercial keywords, roughly 460 combined monthly searches, all sitting between positions 12 and 21, on a page with zero internal link equity. It is also the page behind one of the two genuine ranking declines.

`/mark-3-pump/` matters for a different reason — it is the page behind "portable fire pumps canada", which held #1 until 11 September and has since slipped to 16. Two inbound links is thin support for a position-1 page.

### The blog is effectively dark

45 of 93 blog posts have **zero** in-content inbound links. They are reachable only through a ten-page paginated archive, which puts most of them several clicks from the home page with almost no internal equity flowing to them.

The most expensive case: `/blog/everything-you-need-to-know-about-bc-fire-bans-and-restrictions/` ranks positions 25–31 for **"fire ban bc" (5,400/mo)**, **"bc fire ban" (3,600/mo)**, "bc burning ban" (720), "fire ban in bc" (720), "fireban bc" (720) and roughly fifteen more BC fire-ban variants. That is by far the largest impression pool on the domain, and nothing on the site links to it. Moving that page from the bottom of page 3 to page 2 is a realistic near-term target and would not require new content — only links and a refresh.

### Ready-to-place links (the text is already on the page)

These are pages that already use the target phrase in body copy and do not currently link to the target.

**→ `/roof-sprinkler-system/`**
- `/product/rainmaker/` (6 mentions)
- `/wildfire-sprinkler-kit/` (4)
- `/fire-embers/` (3)
- `/blog/what-to-do-in-a-wildfire-evacuation/`
- `/blog/firesmart-your-property-with-wildfire-mitigation/`
- `/blog/does-rain-really-reduce-wildfire-risk/`

**→ `/fire-embers/`** (28 pages qualify; strongest first)
- `/roof-sprinkler-system/` (10 mentions)
- `/blog/defensible-space/` (7)
- `/blog/firesmart-your-property-with-wildfire-mitigation/` (6)
- `/structure-protection-sprinklers/` (5)
- `/blog/preparing-for-wildfires-property-owner-guide/` (5)
- `/blog/preparing-for-wildfire-evacuation/` (5)
- `/blog/okanagan-wildfire-risks/` (5)

**→ `/mark-3-pump/`** (14 pages qualify)
- `/product/mark-3-b2-10hp-mid-range/` (13 mentions)
- `/product/mark-3-qs-10hp-high-pressure/` (11)
- `/product/rancher-65-gallon/` (5)
- `/shop/` (4)
- plus eight more pump product pages

**→ `/waterax-pumps/`**
- `/mark-3-pump/` (7), `/sprinkler-trailers/` (4), `/products/` (2)

**→ `/structural-protection-unit/`** — 31 pages qualify, mostly product pages. This page already has 22 inlinks and is holding #1, so treat as lower priority.

### Anchor text note

Current internal anchors are dominated by repeated template strings — "Wildland Sprinkler Kits" appears 63 times, "WATERAX Pumps" 61 times, "SPIEDR Sprinkler Trailers — Mobile Structure…" 70 times. New links should use varied, descriptive in-content anchors rather than repeating the menu label.

---

## 3. Recommended order of work

1. **`/roof-sprinkler-system/`** — add 6–8 in-content inbound links from the pages listed above. Addresses a confirmed ranking decline and a ~460/mo national cluster stuck on page 2.
2. **`/mark-3-pump/`** — link from the 13 pump product pages that already name the Mark-3. Defends a #1 position that started slipping on 11 September.
3. **`/fire-embers/`** — 8–10 links from the wildfire-preparedness blog cluster. Highest-traffic page on the site, currently unsupported.
4. **`/spiedr-fire-pump-protection-systems/`** — supports the "fire fighting pumps for sale" decline.
5. **Blog architecture** — replace or supplement the ten-page paginated archive with topic hubs (Wildfire Preparedness, BC Fire Bans & Regulations, Equipment & Pumps) so the 45 unlinked posts receive contextual links. Prioritise linking the BC fire bans post from a prominent resources block.
6. **Refresh the Position Tracking keyword set** so future Top 3 / Top 10 counts reflect commercially meaningful terms.

Items 1–4 are on-page edits with no new content required and can ship inside one sprint.

---

## 4. Limitations

- Semrush Position Tracking for this campaign is **Desktop / British Columbia only**. The Google Search Console figures in the report are national. The two data sets will not agree, and the report should say so where they are placed side by side.
- The crawl covered URLs present in spiedr.com's XML sitemaps. Any page excluded from the sitemaps is not reflected in the inlink counts.
- No Screaming Frog crawl exists on file for spiedr.com. One should be run before the next audit cycle so crawl depth and orphan status can be confirmed independently.
- Ranking movement is influenced by factors outside our control, including competitor activity and Google algorithm updates. The actions above are expected to improve internal link equity and crawl depth; no specific position outcome is being promised.
