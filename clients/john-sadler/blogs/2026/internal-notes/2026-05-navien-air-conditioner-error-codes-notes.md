# Internal notes: 2026-05-navien-air-conditioner-error-codes

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, delete before publishing):** Error-code explainer for Navien central air conditioners: the NAA series (letter codes such as F0, P2, H5) and the NAE series (numbered alarm and error codes such as 251 and 201), with a short section on how faults on the paired NAS air handler and NAM cased coil show up. Covers what the codes mean, what a homeowner can safely check, and when to call a technician. It does not cover AC sizing, rebates or installation.
**Masterlist:** May 2026, Blog #2 (row 71), "Navien Air Conditioner Error Codes Explained" (topic approved). Series: NAA, NAE (plus NAS and NAM context).

## Image Note

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

AC stopped cooling? Navien air conditioners record a code that points to the cause. Our new guide explains Navien NAA and NAE error codes, which ones reset on their own, what you can safely check, and when to call. Q: Can a dirty filter cause an AC error code? A: Yes, a clogged filter cuts airflow and can trigger a low pressure code, so check it first. Questions? Call our Surrey team at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

Warm air from the vents on a hot day? Before you sweat it, check our new guide to Navien air conditioner error codes. It explains what the NAA and NAE codes mean, the safe checks you can do yourself, and when it's time to call us. [blog URL] #SurreyBC #AirConditioning

## Instagram Post

P2, H5, 251, 201: what is your Navien AC trying to tell you? Our latest blog explains Navien air conditioner error codes in plain language. Link in bio. [blog URL] #Navien #AirConditioning #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **BLOCKER (from CARD.md): do not publish until the "installs only / refer repairs elsewhere" copy is removed from `/services/heating-cooling/air-conditioning/`.** Checked live on 2026-10-23: the page still says "Why 'installs only' is the right call for AC" and "If you need an AC repair, we'll happily refer you to a trusted local repair contractor." This post links to that page in the intro and invites service calls, which contradicts it. Needs Tina/Colin approval of the edits in `page-update-ac-heat-pump-repair-2026-10-16.md` first.
- **Also confirm with Tina/Colin:** that John Sadler services Navien NAA and NAE units (AC repair is "early stage"). The CTA avoids promising repair turnaround. Best publish window is April to May 2027, ahead of the summer peak ("navien air conditioner" peaks May to July at 50/mo CA).
- **Schema:** FAQPage for the four FAQs (answers have no links and no branded language). Article/BlogPosting with author John Sadler Plumbing & Heating.
- **Source of every code:** Navien NAA Air Conditioner Installation and Operation Manual (Version 1.0, January 2026, section 4.5.2); Navien NAE Series Installation and Operation Manual (Version 1.0, July 2025, sections 3.2 and 7.1 to 7.2); Navien NAM Installation and Operation Manual (Version 1.0, December 2024, "Refrigerant Leak Detection System"); Navien NAS Installation and Operation Manual (Version 1.0, December 2024). All downloaded from navieninc.com on 2026-10-23. The NAA, NAS and NAE service manuals are behind a login and were not used.
- **NAS/NAM claim (masterlist note says faults "surface on paired NAA/NAE display"):** verified only partly. Neither the NAS nor NAM manual has an error code table (confirmed by text search). The NAE manual lists low indoor airflow and a dirty indoor filter as causes of low pressure codes 252/202, which supports "indoor problems show up as outdoor pressure codes". The leak mitigation behaviour (indoor blower on, outdoor unit disabled) is quoted from the NAM manual; the NAS manual references the same refrigerant leak sensor. Colin to confirm whether the NAS/NAM leak alarm also produces a code on the outdoor display (not documented in the manuals reviewed).
- **NAE table reading note for Colin:** the NAE error table PDF prints the codes and names in separate columns, so the pairing in the post (201 to 210 = alarms 251 to 260 repeated; 501/505/506/507 = T_a, TD, TS, T_cond sensors; 561/562 = PD/PS pressure sensors; 702 = outdoor unit to inverter driver communication; 801 to 824 = alarms 851 to 874 repeated; 999 = unknown) follows the order of the names column. Reading the reset column line by line gives 201 to 210 = Manual, 501 to 702 = Auto, 801 to 999 = Manual, which is what the table shows ("Automatic once the fault clears" is our plain-language reading of Navien's "A = Auto" for error codes). Please confirm against a unit.
- **NAE homeowner steps:** "clean the air intake filter with the unit off" and "check the main water valve" come from Navien's own E201/E203 troubleshooting flowcharts in the I&O manual. Nozzle replacement is described there as a service-centre job and is not suggested to homeowners.
- **Cannibalization check (johnsadler.ca sitemaps, pulled 2026-10-23):** no existing post covers Navien AC codes. `/blog/heat-pump-vs-ac-unit/`, `/blog/can-i-install-ac/` and `/blog/know-before-installing-heat-pump-ac/` are buying content. The 2025-backlog draft "AC Not Blowing Cold Air?" covers general symptoms for any AC brand; this post is Navien code-specific. Link the two to each other once both are live.
- **Internal links (5 distinct, meets the 5 minimum):** /services/heating-cooling/air-conditioning/, /blog/heat-pump-vs-ac-unit/, /services/navien/, /blog/navien-heat-pump-error-codes/ (sibling post, not live yet: publish together or hold the link), /contact-us/. If the sibling link has to wait, add /blog/can-i-install-ac/ or /blog/furnace-filter/ (filter section) to keep five. Note: /blog/heat-pump-vs-ac-unit/ still quotes an outdated "$10,000" rebate (flagged in the 2025 backlog README); fix that before linking traffic to it, or swap the link for /blog/ac-heat-pump-ductless-split/.
- **External links (2 Navien downloads pages, both verified loading 2026-10-23, open in new tab with rel="noopener noreferrer"):** NAA and NAE product downloads pages, placed under the reference tables as citations. No gas safety link is needed (electric cooling equipment).
- **Wording decisions:** "certified technician" for refrigerant work rather than naming a specific BC certificate (not verified). No prices, rebates, 24/7 or emergency claims.
- **PAA research:** Semrush returned "no API units" on 2026-10-23 and Keyword Planner has no question data. FAQs follow common AC troubleshooting question patterns (where is the code, alarm vs error, fan running but not cooling, dirty filter). Re-check with Semrush `phrase_questions` (database ca) once units are restored.
- **Images:** 3 placements, all must be real John Sadler photos, never AI or stock.
- **Quick Answer:** use the WordPress Preformatted block.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
