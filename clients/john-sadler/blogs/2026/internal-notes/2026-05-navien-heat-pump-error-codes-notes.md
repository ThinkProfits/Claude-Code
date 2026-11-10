# Internal notes: 2026-05-navien-heat-pump-error-codes

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, delete before publishing):** Error-code explainer for the Navien NAZ heat pump (outdoor unit): every code in Navien's published NAZ table, grouped by letter family, including the normal "running indication" codes like dF (defrost), plus what a homeowner can safely check and when to call a technician. It does not cover heat pump sizing, rebates or installation.
**Masterlist:** May 2026, Blog #1 (row 70), "Navien Heat Pump Error Codes Explained" (topic approved). Series: NAZ.

## Image Note

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

Heat pump stopped working, or a technician mentioned a code like dF, P2 or H5? Our new guide explains Navien NAZ heat pump error codes, which ones are normal, what you can safely check, and when to call. Q: What does dF mean on a Navien heat pump? A: It's a normal defrost cycle that melts frost off the outdoor coil, and Navien's manual says it lasts up to 8 minutes. Questions? Call our Surrey team at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

Steam coming off your heat pump in winter? That's usually defrost mode, and it's normal. Our new guide explains Navien NAZ heat pump error codes, which ones need attention, and the safe checks you can do before calling us. [blog URL] #SurreyBC #HeatPump

## Instagram Post

dF, PRH, P2, H5: what is your Navien heat pump trying to tell you? Our latest blog breaks down NAZ heat pump error codes in plain language. Link in bio. [blog URL] #Navien #HeatPump #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **BLOCKER (from CARD.md): do not publish until the "installs only / refer repairs elsewhere" copy is removed from `/services/heating-cooling/heat-pumps/`.** Checked live on 2026-10-23: the page still has a section titled "Why 'installs only' matters for heat pumps". This post links to that page and its CTA invites service calls, so publishing first would send readers to a page that says John Sadler doesn't repair heat pumps. Needs Tina/Colin approval of the page edits in `page-update-ac-heat-pump-repair-2026-10-16.md` first.
- **Also confirm with Tina/Colin:** that John Sadler is happy to promote Navien heat pump diagnosis and service (repairs are "early stage" per the brief). The CTA is worded as "we work on Navien heating and cooling equipment" and "call", without promising repair turnaround.
- **Schema:** FAQPage for the four FAQs (answers have no links and no branded language). Article/BlogPosting with author John Sadler Plumbing & Heating.
- **Publish date:** Masterlist slot is May 2026 (overdue). "navien heat pump" searches peak March to June (90/mo in March), so a February or March 2027 publish works if the blocker isn't cleared sooner.
- **Source of every code:** Navien NAZ Installation and Operation Manual (Version 2.0, July 2026), section 4.7.2 "Error Codes"; defrost figures from section 4.1; display and Multikit details from sections 5 and 6.2. Downloaded from navieninc.com on 2026-10-23. Every code in the NAZ table is in the post, except that F4 to F7, FC to FF and LB to LF are grouped in prose. The NAZ service manual (with fix procedures) is behind a login and was not used.
- **Codes not in Navien's table:** P7, PA, PB, H9, HA, HB, HD, L2 to L9 and F1 to F3 don't appear in the NAZ manual, so they aren't mentioned. (F1 "Low pressure switch error" does appear in the NAA air conditioner table, but not the NAZ one.)
- **Cannibalization check (johnsadler.ca sitemaps, pulled 2026-10-23):** no existing post covers Navien heat pump codes. Related posts (`/blog/heat-pump-vs-ac-unit/`, `/blog/heating-with-heat-pump-or-furnace/`, `/blog/know-before-installing-heat-pump-ac/`, `/blog/choosing-heat-pump-contractor/`) are buying and comparison content. The 2025-backlog draft "How Does a Heat Pump Work?" mentions defrost in general terms; this post covers Navien-specific defrost timing only, so no conflict. Link to it once it's live.
- **Internal links (6 distinct):** /services/heating-cooling/heat-pumps/, /blog/heating-with-heat-pump-or-furnace/, /blog/navien-furnace-error-codes/ and /blog/navien-air-conditioner-error-codes/ (sibling posts, not live yet), /services/navien/, /contact-us/.
- **External links (1, verified loading 2026-10-23, open in new tab with rel="noopener noreferrer"):** Navien NAZ product downloads page (lists the NAZ Installation and Operation Manual). The FortisBC number is stated in the dual-fuel note without a link; it was verified on fortisbc.com the same day.
- **Wording decisions:** "certified technician" is used for refrigerant work rather than naming a specific BC certificate, since that wasn't verified. "Flammable refrigerant" follows the NAZ manual's own safety section ("FLAMMABLE REFRIGERANTS" safety checks for R-454B work). No prices, rebates, 24/7 or emergency claims.
- **PAA research:** Semrush returned "no API units" on 2026-10-23 and Keyword Planner has no question data. FAQs follow common heat pump question patterns (where's the code, what is defrost, why does it keep shutting off, cold weather). Re-check with Semrush `phrase_questions` (database ca) once units are restored.
- **Images:** 3 placements, all must be real John Sadler photos, never AI or stock.
- **Quick Answer:** use the WordPress Preformatted block.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
