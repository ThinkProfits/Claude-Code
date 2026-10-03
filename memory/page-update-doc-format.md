---
name: page-update-doc-format
description: "Required layout for any website page-update deliverable doc — Current vs Replacement side-by-side, Keep/New Section labels, exact H-tags, internal links"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 43b112ef-76c7-48b2-b591-a1c6641dd650
  modified: 2026-09-25T18:30:29.586Z
---

When a deliverable doc proposes edits to an existing web page, lay it out as a side-by-side table:
**Current Content | Replacement Content**, one row per section, in live page order.

- Section not changing: mark the replacement cell **"Keep Section"**.
- Section being added: mark it **"New Section"** (current cell empty) and state where it goes (after which existing heading).
- Label every row with its exact H-tag and heading text as it appears live (e.g. `H2: Online Therapy & Counseling`) so the developer can find the exact block on the page.
- Current Content must be **verbatim** live text, never a summary ("five bullets…" failed the check), including accordion FAQ answers (Wix loads them client-side — grab via browser). One row per FAQ H3, never grouped.
- Put links INSIDE the replacement copy as real clickable hyperlinks on the anchor text (URL shown beside it), and buttons as linked button lines — not as a separate "suggested links" list (Francis, 2026-09-26). A per-page link table at the end is fine as a QA checklist.
- Always spell out internal links: anchor text + target URL, per section. Never leave linking implicit.

**Why:** Francis (2026-09-25): devs need to see exactly which on-page section is replaced and what the edit is. Internal linking is the thing most often forgotten.

**How to apply:** any page-update doc for any client. The side-by-side table is for UPDATES only. **Brand-new pages** use the standard content-writing layout instead (Francis, 2026-09-26): write standard deliverable markdown (scope note, title/meta/slug/keyword, H1 + flowing copy with inline links and "Button:" lines, `## Implementation Notes` with dev notes + open questions + link list), then build the .docx in portrait, no tables. Related: [[service-page-vs-blog-format]].
