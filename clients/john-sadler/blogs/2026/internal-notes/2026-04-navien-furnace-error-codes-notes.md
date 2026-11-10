# Internal notes: 2026-04-navien-furnace-error-codes

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, delete before publishing):** Error-code explainer for Navien furnaces in two parts: the NPF hydro furnace (hydronic, "E" codes on the front control panel) and the NDF gas furnace (flashing status-light codes on the control board). Covers every code in Navien's published tables, what each one means, what a homeowner can safely check, and when to call a licensed technician. It does not cover installation, sizing or maintenance schedules.
**Masterlist:** April 2026, Blog #2 (row 68), "Navien Furnace Error Codes Explained" (topic approved). Series: NPF (hydronic) and NDF (gas).

## Image Note

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

Is your Navien furnace showing a code or a flashing light? Our new guide explains Navien furnace error codes for both the NPF hydro furnace and the NDF gas furnace, what you can safely check, and when to call a licensed technician. Q: How do I reset a Navien hydro furnace? A: Press the Back button on the front panel; if the code returns, the furnace needs service. Call our Surrey team at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

Navien's hydro furnace and gas furnace report problems in different ways: one shows E codes, the other flashes a status light. Our new guide explains both, with the safe checks you can do and the signs it's time to call us. [blog URL] #SurreyBC #Navien

## Instagram Post

E302 on your hydro furnace? Four flashes on your gas furnace? Our latest blog explains Navien furnace error codes and what to do about them. Link in bio. [blog URL] #Navien #FurnaceRepair #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **Schema:** FAQPage for the four FAQs (answers have no links and no branded language). Article/BlogPosting with author John Sadler Plumbing & Heating. No HowTo schema.
- **Publish date:** Masterlist slot is April 2026 (overdue). Publish with the current date. "navien hydro furnace" peaks in January (390/mo CA), so publishing before December matters.
- **Source of every code:** Navien NPF Installation and Operation Manual (Version 1.1, June 2026, section 5.15 "Understanding Error Codes") and Navien NDF Installation & Operation Manual (Version 1.0, September 2026, sections 18.5 "Diagnostic Codes for Status LED" and 18.6 "Fault Code History"). Both downloaded from navieninc.com on 2026-10-23. Code names are quoted as Navien prints them. The NPF service manual is behind a login and was not used.
- **NPF table reading note for Colin:** the E740 to E788 rows in the NPF PDF are laid out in a way that makes column alignment hard to read. The mapping used (E740 outdoor sensor, E762 vent pipe, E774/E775 external safety system 1 and 2, E782 controller-panel communication, E786 front panel connection, E788 gas type settings) follows the order of the reasons column. Please confirm against a unit or the service manual. Same for E810 vs E811 (both "abnormal circulator operation"; the filter/duct checks are printed beside E810).
- **Omitted on purpose:** the NPF E003 entry also tells propane customers to check their tank. John Sadler doesn't do propane, so that line was left out. NDF "9 flashes: not used" is left out of the table.
- **NDF "status light" location:** Navien's manual doesn't say whether the LED is visible through a door window. The post tells homeowners to count flashes only if they can see the light without removing a panel (the manual says not to run heating with doors off). Colin to confirm whether the NDF has a sight window.
- **Cannibalization check (johnsadler.ca sitemaps, pulled 2026-10-23):** no existing post covers Navien furnace codes. `/services/heating-cooling/furnace-repair/` has a generic "Error Codes on the Furnace Display" section and an FAQ "My furnace is showing an error code. What should I do?"; this post is Navien-model-specific and links to that page, so they support each other. `/blog/navien-hydro-furnace-case-study/` is an install story and is linked, not repeated. `/blog/why-does-my-furnace-keep-shutting-off/` overlaps loosely but was not linked because it still has the 24/7 line flagged in the 2025 backlog README. Recommend adding a link from the furnace-repair FAQ answer area (body copy, not the FAQ answer) to this post.
- **Internal links (6 distinct):** /services/heating-cooling/furnace-repair/, /blog/navien-hydro-furnace-case-study/, /blog/furnace-filter/, /services/navien/, /blog/navien-boiler-error-codes/ (sibling post, not live yet: publish together or hold the link), /contact-us/.
- **External links (3 Navien + 1 FortisBC, all verified loading 2026-10-23, open in new tab with rel="noopener noreferrer"):** FortisBC gas leaks and odour page (emergency line confirmed), Navien NPF downloads page, Navien NDF downloads page. That's above the skill's 1 to 2 target; the two Navien source links sit under the reference tables as citations. If the editor wants 2 max, keep FortisBC and fold the Navien citations into plain-text source lines.
- **Facts to confirm with Colin:** example model number NPF700-080H; whether John Sadler services NDF furnaces yet (the NDF manual is dated September 2026, so the line may be new in Canada).
- **Wording decisions:** no prices, rebates, 24/7 or emergency-service claims.
- **PAA research:** Semrush returned "no API units" on 2026-10-23 and Keyword Planner has no question data. FAQs follow the reset step every manual leads with, the code-level searches seen in Keyword Planner (E302 is a shared Navien code) and the "flashing lights" pattern common to gas furnace searches. Re-check with Semrush `phrase_questions` (database ca) once units are restored.
- **Images:** 3 placements, all must be real John Sadler photos, never AI or stock.
- **Quick Answer:** use the WordPress Preformatted block.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
