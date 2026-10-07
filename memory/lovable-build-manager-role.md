---
name: lovable-build-manager-role
description: Claude acts as manager and QA for Lovable page builds on the ThinkProfits rebuild; Francis delegates design calls and wants Lovable held to a high bar
metadata:
  type: feedback
---

For ThinkProfits website page builds in Lovable (project "Thinkprofits Rebuild", `12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17`), Francis wants Claude to be the manager and checker: write the briefs, own the design decisions, review every Lovable change before reporting back, and send firm, specific correction messages when Lovable's work is sloppy or doesn't follow the brief (said 2026-10-08: "be the man behind all these page builds. I trust you").

**Why:** Francis would rather review finished, checked work than relay instructions and spot problems himself. Andrew reviews the result.

**How to apply:**
- Don't just pass on Lovable's own report. Verify it: read the changed file with the Lovable MCP `read_file`, and check the rendered page visually when the preview is reachable (the preview URL needs a Lovable login in the browser pane).
- Make design calls (layout, spacing, hierarchy, consistency) without asking, within ThinkProfits' design system: dark blue (`tp-blue-deep`), orange accent, `font-display` headings, rounded-2xl cards.
- Still ask before anything outward-facing: publishing, changing live (non-draft) pages, or making new factual or client claims.
- Corrections to Lovable should be blunt and specific: name what it got wrong against the brief and say exactly what to fix. Stay professional, not abusive.
- Keep a change log per page (e.g. `clients/thinkprofits/industry-pages/plumbing/plumbing-page-v2-changes-2026-10-07.md`) with commit SHAs and credits.
- Never guarantee rankings in page copy; don't invent reviews, stats or client names.
