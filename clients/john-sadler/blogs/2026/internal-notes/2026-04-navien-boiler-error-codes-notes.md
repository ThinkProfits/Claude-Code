# Internal notes: 2026-04-navien-boiler-error-codes

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, delete before publishing):** Error-code explainer for Navien NFB-H and NHB-H condensing boilers: every code in Navien's published code tables, grouped by type, with what each one means, what a homeowner can safely check (reset, power, gas valve, condensate, pressure reading) and when to call a licensed technician. It does not cover combi boilers (NCB), tankless water heaters or annual maintenance (the June Navien maintenance post covers that).
**Masterlist:** April 2026, Blog #1 (row 67), "Navien Boiler Error Codes Explained" (topic approved). Series: NFB-H, NHB-H.

## Image Note

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

Seeing an E003, E012 or E302 on your Navien boiler? Our new guide explains the error codes for Navien NFB-H and NHB-H boilers, what you can safely check yourself, and when it's time to call a licensed technician. Q: How do I reset a Navien boiler? A: Press the Back button on the front panel; if the code returns, the boiler needs service. As a Navien Certified Service Specialist in Surrey, we're here to help at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

A code on your Navien boiler's display doesn't have to be a mystery. Our new guide breaks down the NFB-H and NHB-H error codes, from ignition and venting codes to low water pressure, with the safe checks you can do and the signs it's time to call us. [blog URL] #SurreyBC #Navien

## Instagram Post

E003? E302? E110? Our latest blog explains what Navien boiler error codes mean and what you can safely check before calling a technician. Link in bio. [blog URL] #Navien #BoilerRepair #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **Schema:** FAQPage for the four FAQs (answers have no links and no branded language). Article/BlogPosting with author John Sadler Plumbing & Heating. No HowTo schema.
- **Publish date:** Masterlist slot is April 2026 (overdue). Publish with the current date rather than backdating, unless the team prefers to fill the April archive slot. Boiler error-code searches peak December to March (navien boiler repair: 880/mo in Dec and Jan), so publishing before December is the priority.
- **Source of every code:** Navien NFB-H User's Information Manual (Version 1.0, April 2024, section 5.2) and NFB-H Installation & Operation Manual (Version 1.0, February 2024, section 11.7); Navien NHB-H User's Information Manual (Version 1.0, April 2024, section 5.2) and NHB-H Installation & Operational Manual (Version 1.0, April 2026, section 11.14). All downloaded from navieninc.com on 2026-10-23. The two series share the same table, except E031 (Burner Overheat), which appears in the NFB-H tables only. Code names in the table are quoted as Navien prints them.
- **Codes deliberately not given extra detail:** E762's insertion depth is printed differently across manuals (NFB-H user manual "2-?" (garbled), NFB-H I&O "3 inches", NHB-H I&O "2-3/4 in (70 mm)"), so the post says "not fully seated" without a measurement. It's an installer fix either way.
- **Service manuals:** the NFB-H and NHB-H service manuals on navieninc.com are behind a login, so the post relies on the user and installation manuals only. Colin may want to add detail on E302/E352 from field experience.
- **Cannibalization check (johnsadler.ca post and page sitemaps, pulled 2026-10-23):** no existing post covers Navien error codes. Closest pages: `/blog/new-boiler-not-working-surrey-bc/` (general new-boiler troubleshooting, mentions "an error code on the display" generically), `/blog/whats-wrong-with-my-boiler/` (general symptoms), `/services/heating-cooling/boiler-repair/` (service page). This post is Navien-model-specific and code-level, so it complements them. Recommend adding a link from `/blog/new-boiler-not-working-surrey-bc/` ("error code on the display") to this post. Per CLIENT.md keyword routing, Navien commercial queries still go to `/services/navien/`; this post links there and the hub rewrite should link back.
- **Internal links (5 distinct, meets the 5 minimum):** /services/heating-cooling/boiler-repair/ (intro), /blog/radiant-floor-heating-boiler-care/, /services/navien/, /blog/navien-furnace-error-codes/ (sibling post, not live yet: publish together or hold the link until it's live), /contact-us/. If the sibling link has to come out, add /blog/annual-boiler-service/ to keep five.
- **External links (3, all verified loading 2026-10-23, open in new tab with rel="noopener noreferrer"):** FortisBC gas leaks and odour page (emergency line "1-800-663-9911 (24 hours)" confirmed on page), Navien NFB-H downloads page (lists both NFB-H manuals). The skill target is 1 to 2; the FortisBC safety link is kept because the brief requires the verified emergency number. Drop the Navien link if the editor wants 2 max.
- **Facts to confirm with Colin:**
  - That the NHB-H models John Sadler services are the current NHB-55H/80H/110H/150H line (the post names NHB-110H as an example).
  - Whether John Sadler wants to tell homeowners how to top up pressure themselves. The post currently says not to open fill or relief valves unless the installer has shown them how.
- **Wording decisions / omitted claims:** no prices, rebates, 24/7 or emergency-service claims. "Licensed gas fitter under Technical Safety BC rules" is kept general rather than citing a specific regulation. Navien's warranty labour/parts terms were not quoted.
- **PAA research:** Semrush returned "no API units" on 2026-10-23, and Keyword Planner returns no question data. FAQs use the question patterns implied by the code-level searches (navien e003, navien e302, navien boiler low water pressure) plus the reset step every manual leads with. Re-check with Semrush `phrase_questions` (database ca) once units are restored.
- **Images:** 3 placements, all must be real John Sadler photos, never AI or stock.
- **Quick Answer:** use the WordPress Preformatted block.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
