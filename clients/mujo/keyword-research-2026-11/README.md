# Mujo: AI and business keywords for Semrush tracking (2026-11-21)

**Request:** Brittni, #mujo, 2026-11-07: "change the tracked keywords in SemRush to reflect the keywords we want to target? I noticed the current ones don't include any of the AI or business titles for either higher ed or hs." Andrew confirmed; Francis's Nov report reply committed to doing it this week.

**Deliverable:** [mujo-ai-business-tracked-keywords-2026-11.xlsx](mujo-ai-business-tracked-keywords-2026-11.xlsx) · [Google Sheet in Drive](https://docs.google.com/spreadsheets/d/1D5wwNqckDnYZI_6G9xUyM5gFsl9riC-KIH3WOWpMAgM/edit). Status: **DRAFT for Francis's review, then Brittni's sign-off. Nothing has been changed in Semrush** (API units at zero on 2026-11-21, and keyword choices need Brittni's approval first).

## What we found

- **Current tracking is almost all digital marketing.** USA has 81 keywords and Canada 70. Only 6 touch AI or business (textbooks on artificial intelligence, foundations of artificial intelligence, ai textbooks, generative ai textbooks, applied ai for business, accounting principles textbook), all in the USA campaign. **Canada has none.** Source: Semrush pages of the 2026-11-06 monthly report.
- **There's real demand Semrush can't see.** GSC shows 1,621 non-brand queries hitting the AI and business pages over 16 months. Keyword Planner returns 0 for most of these educator phrases, because it buckets niche volumes, so GSC impressions are the better demand signal here.
- **Mujo already wins many title-level searches**, so tracking them shows real strength. Live SERP check (US, 2026-11-21), Mujo #1 for:
  - ai in accounting textbook
  - ai business writing textbook
  - generative ai for business textbook
  - ai business analytics textbook
  - applied ai for business curriculum
  - ai textbook for high school
  - ai for business high school curriculum
  - entrepreneurship textbook high school
  - #2 for ai business administration textbook and business communication textbook with ai
- **The head terms are where the work is.** Mujo is absent from the live top 10 for:
  - ai textbooks
  - ai curriculum for high school
  - foundations of artificial intelligence
  - high school entrepreneurship curriculum
  - principles of business textbook
  - ai project management textbook
  - prompt engineering textbook
- **Several big-volume terms have the wrong intent.** These are on the "Not recommended" tab:
  - "ai lesson plans" = AI lesson-plan generators
  - "ai in accounting course" = CPA continuing education
  - "prompt engineering course" = individual learners
- **Competitors:** businessu.org now redirects to Stukent, so that competitor slot is wasted. Replace it with g-w.com (Goodheart-Willcox, strong on HS business terms) and/or routledge.com (top 10 on 9 of the AI business textbook SERPs). McGraw Hill is the head-to-head rival: "AI in Business" (HE) and "Foundations of AI" (HS).
- **On-page bonus:** 23 HE target pages lack "Higher Education" in the title tag, and 8 HS pages lack "High School". This matches Andrew's 2026-06-24 title rule, still pending Brittni's pattern choice.

## The proposal

- **58 keywords:** 34 Tier 1 (core) and 24 Tier 2 (watch).
- **New keywords per campaign:** 53 for USA, 29 for Canada.
  - High school terms stay USA-only, matching where HS is sold.
  - "turnkey ai curriculum" is Canada-only.
- **Optional:** remove 6 off-target or duplicate keywords from each campaign.
- **Campaign sizes afterwards:** about 128 (USA) and 93 (Canada). Check the account's position tracking keyword limit before adding.
- **Tag everything** (HE-AI, HE-Business, HS-AI, HS-Business, title, T1/T2) so AI/business visibility can be reported separately.

**Warn Brittni first:** overall visibility will drop the month these go in, because many start outside the top 20. That drop is a new baseline, not a ranking loss.

## Files

| File | What |
|---|---|
| `mujo-ai-business-tracked-keywords-2026-11.xlsx` | The workbook. Tabs: Read me, Proposed keywords, Paste lists for USA and Canada, Current tracked set, Not recommended, SERP check, Competitors |
| `slack-draft-brittni.md` | Draft reply for #mujo (not sent) |
| `build_workbook.py` | Regenerates the workbook. The SERP notes and current tracked set are typed in it, with sources |
| `candidates.py` | The 213-keyword candidate universe |
| `gsc_ai_business.py` + `gsc-ai-business-queries.csv` | GSC aggregation for the AI/business pages (reusable for other page families) |
| `kp-*.json` | Raw Keyword Planner outputs (US geo 2840, Canada) |

**Reusable:** the method transfers to any client: GSC page-family export, Keyword Planner volume, live SERP intent check, then tier and tag. Swap the inputs in the three scripts.

## Gaps

- No Semrush data (API units at zero), so no Semrush volume, KD or current-position export. Positions in the workbook are a one-off manual SERP check from outside the US with gl=us.
- No PAA pull from Semrush. The SERP PAA questions seen are mostly generic ("What is the 30% rule for AI?") and weren't useful for these commercial terms.
- Unconfirmed: whether "Principles of Business: In An AI World" is aligned to Texas PBMF or Georgia standards (the pages claim neither), and whether nursing programmes are a target for AI Literacy for Healthcare.
