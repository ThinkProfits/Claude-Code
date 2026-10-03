---
name: aanmc-context
description: "AANMC (aanmc.org) ThinkProfits client — GSC access, Oct 2026 naturopathic-doctor click-loss diagnosis, deliverable location, open questions"
metadata:
  node_type: memory
  type: project
  originSessionId: a11c04dc-34ed-4ebe-a8c9-98b42f76d16a
  modified: 2026-10-01T16:51:26.679Z
---

AANMC (Association of Accredited Naturopathic Medical Colleges, aanmc.org) is a ThinkProfits client. Its audience is prospective ND students, not patients. GSC property is `sc-domain:aanmc.org` on the agency gsc MCP (siteOwner). Working folder: `clients\ThinkProfitsClients\aanmc\`.

Oct 2026 diagnosis (deliverable `AANMC_Naturopathic-Doctor-Click-Recovery_2026-10.md/.docx`):
- "naturopathic doctor" clicks fell 275 → 42 (Jul–Sep 2025 vs 2026).
- Cause 1: cannibalization across 5+ URLs, with no "what is a naturopathic doctor" page. The proposed fix is a new `/what-is-a-naturopathic-doctor/` page.
- Cause 2: a local pack of 3 clinics sits above organic results (patient intent).
- Cause 3: weak or missing metas. The traditional-vs-licensed article has no meta. /naturopathic-medicine/ meta is off-topic and was last modified 2023-11-30.
- Cause 4: AI answers and demand softening.
- Don't repurpose /comparing-nd-md-curricula/. It ranks #2–3 for ND-vs-MD queries.

**Why:** I need the baseline numbers to measure the recovery later, and the open client questions are still pending.

**How to apply:** Before follow-up work, check what AANMC answered on these open questions:
- Who the ND medical reviewer is
- Whether newer salary data exists than the 2020 study
- Whether a patient-facing "verify an ND" section is acceptable
- US vs Canadian spelling for page copy
- Whether to merge /naturopathic-schools-usa/ into /naturopathic-schools/

aanmc.org returns 403 to rapid curl requests. Space requests out or use WebFetch.

Related: [[page-update-doc-format]], [[paa-research-standard]], [[strategy-core-pages-before-niche]]
