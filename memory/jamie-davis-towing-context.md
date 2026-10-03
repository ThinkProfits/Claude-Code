---
name: jamie-davis-towing-context
description: "Jamie Davis Towing site facts, schema mess found in Sept 2026 audit, and the \"ask before changing titles/H1s/city-focus\" rule for this client"
metadata: 
  node_type: memory
  type: project
  originSessionId: f0d180ae-e2f5-4af8-8de5-72f4bdf2c42f
  modified: 2026-09-03T17:10:46.354Z
---

Jamie Davis Towing (jamiedavistowing.com) — Semrush project ID 30290458 ("Jamie Davis Towing"), only the `tracking` tool is enabled on that project, NOT `siteaudit`. Semrush Site Audit reports will fail/return nothing for this client until Site Audit is added to the project.

**Rule: get sign-off on any major H1/title/city-focus change before publishing.** Jamie Davis Towing's core service pages are active Google Ads landing pages — the account is user (francis@thinkprofits.com)'s, and it's performing well. Title/H1 rewrites and shifting a page's city focus (e.g. making a page "too Calgary-specific" when Calgary is a small part of the business) can hurt Ads landing-page relevance/Quality Score.
Why: user explicitly said this 2026-09-04 after catching several title/H1 drifts during a technical+schema audit (Calgary crept into the flatbed page title, CAA/BCAA got over-emphasized as the roadside-assistance page's main keyword instead of a trust signal, heavy-duty page's emergency-recovery angle got flattened into generic "for bigger vehicles" copy).
How to apply: before editing any `<title>`, H1, or a page's primary city/geo focus on this site, propose the change and wait for explicit approval — don't just ship it. Body copy, schema, and minor grammar fixes are lower-risk but still flag anything that could read as a positioning shift.

**Site structure**: homepage + `/towing-services/` (general automotive) + `/heavy-duty-towing-services/` + `/flatbed-towing-services/` + `/roadside-assistance/` + `/commercial-towing-services/` (redirects from old `/commercial-towing/`) + `/long-haul-international-towing/` + `/train-derailment-recovery-services/` + city pages: `/24-7-towing-calgary/`, `/golden-towing-company/`, `/langley-tow-company/`, `/towing-surrey-bc/`, `/chilliwack-towing/`, `/hope-towing/`. Physical address/HQ is Hope, BC; Calgary, AB is a satellite service area, not the main market — see [[jamie-davis-towing-context]] rule above.

User is considering splitting heavy-duty-towing-services into a dedicated emergency-recovery (crane/cliff-recovery) page vs. a general large-vehicle towing page, and possibly merging the large-vehicle angle into the commercial-towing-services page instead. Not decided as of 2026-09-04 — wants research first before restructuring.

**Schema markup is a real mess (found 2026-09-04, not yet fixed):**
- Two independent, uncoordinated JSON-LD systems stacked on every page: an auto-generated Yoast SEO graph (Organization/WebSite/WebPage, using a broken **relative** `@id` like `"/#organization"` instead of an absolute URL) and a separate hand-authored graph (LocalBusiness/Service/FAQPage, mostly using absolute `@id`s like `https://www.jamiedavistowing.com/#business`). These don't reference each other correctly, so Google can't reliably tell they're the same entity.
- The homepage's hand-authored block declares a business entity as `"@type":"TowingService"` — not a real schema.org type, so it's likely ignored entirely by validators.
- Every other service page's hand-authored block declares the business as `@id: https://www.jamiedavistowing.com/#business`, EXCEPT `/24-7-towing-calgary/`, which invents its own separate entity (`.../24-7-towing-calgary/#business`, name "Jamie Davis Towing Calgary") that isn't linked to the main business entity or to the "Jamie Davis Towing - Calgary AB" sub-location already declared as a `department` of the main business on the other pages. Same real-world Calgary location described three inconsistent ways — a NAP-consistency problem, not just a syntax nitpick.
- The `@type` array for the shared `#business` entity also isn't consistent page-to-page (e.g. `/towing-services/` adds `"AutoRepair"`, which is inaccurate — they tow vehicles, they don't repair them).
Full detail was given to the user in chat on 2026-09-04; not yet repeated in a written deliverable. If asked to fix this, the fix is: pick ONE canonical LocalBusiness/AutomotiveBusiness `@id` (the existing `https://www.jamiedavistowing.com/#business` is the best candidate since it's already used on 6 of 7 pages), reuse it everywhere including the Calgary page and the homepage, drop the invalid `TowingService` type, fix the Yoast relative `@id`s, and keep the `department` sub-entities as the one source of truth for each satellite city location.

No Screaming Frog Desktop/CLI is installed in this environment — technical crawls for this client were done via manual curl fetch + Semrush instead. If Screaming Frog access is added later, prefer it for larger crawls (this site is only ~18 URLs per the XML sitemap, so manual fetch was fully sufficient here).
