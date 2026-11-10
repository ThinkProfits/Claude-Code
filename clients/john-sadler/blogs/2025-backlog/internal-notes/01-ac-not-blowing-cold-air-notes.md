# Internal notes: 01-ac-not-blowing-cold-air

Not client facing. Never paste into the Google Doc.

## Scope

> **EDITOR ONLY (remove before publishing):** Symptom troubleshooting guide covering why a central AC or a heat pump in cooling mode blows warm or weak air, which checks a homeowner can safely do, which fixes need a licensed technician, and when to book AC or heat pump repair with John Sadler.

## Image Note

*Image note: all images must be real John Sadler job photos. Never use AI-generated images.*

---

## GBP Post

Is your AC not blowing cold air? Before you sweat it out, check that the thermostat is on Cool with the fan on Auto, replace a dirty filter, and clear debris from around the outdoor unit. If the air is still warm, or you see ice on the lines, our licensed technicians can diagnose and repair central air conditioners and heat pumps across South Surrey, White Rock and Langley.

**Q: Should I turn off my AC if it's not blowing cold air?** Yes, if you see ice or the outdoor unit hums without starting, since running it can strain the compressor.

**Q: Can I add refrigerant myself?** No. In BC, refrigerant work must be done by an approved technician.

**CTA button:** Learn more (link: [blog URL])

---

## Facebook Post

Warm air coming out of the vents on a hot day? Our new guide walks through why your AC or heat pump might not be blowing cold air, the quick checks you can safely do yourself, and when it's time to call a licensed technician. Read it here: [blog URL] #SurreyBC #ACRepair

## Instagram Post

AC not blowing cold air? Start with the thermostat, the filter and the outdoor unit, then call us if it's still warm. Our full troubleshooting guide is at the link in our bio. #SurreyBC #WhiteRock #ACRepair #HeatPump

---

## Implementation Notes

- **BLOCKER, fix before publishing:** The live [/services/heating-cooling/air-conditioning/](https://www.johnsadler.ca/services/heating-cooling/air-conditioning/) and [/services/heating-cooling/heat-pumps/](https://www.johnsadler.ca/services/heating-cooling/heat-pumps/) pages still say John Sadler does installs only and refers repairs elsewhere. AC and heat pump repair has been offered since Aug 2026. That copy must be removed or updated before this post goes live, otherwise the post's CTA contradicts the service pages it links to.
- **Publish timing:** Seasonal topic. Best published April to May 2027, ahead of the May to August search peak, rather than now (October).
- **Cannibalization check:** Done. No existing johnsadler.ca post targets "ac not blowing cold air" or close variants. No overlap. Related posts linked instead: /blog/heat-pump-vs-ac-unit/, /blog/can-i-install-ac/, /blog/know-before-installing-heat-pump-ac/.
- **Title:** Masterlist title is "Why is My AC Not Blowing Cold Air?". Title tag and H1 were reworked to put the primary keyword first and add the city; the question form appears in the intro and FAQ.
- **Schema:** FAQPage for the four FAQs. Article (BlogPosting) for the post. HowTo is not recommended (the frozen-coil steps are a sub-section, not the whole post).
- **Internal links (8 distinct):** air-conditioning service page, heat-pumps service page, /contact-us/, /blog/comparing-different-thermostats/, /blog/furnace-filter/, /blog/heat-pump-vs-ac-unit/, /blog/can-i-install-ac/, /blog/know-before-installing-heat-pump-ac/.
- **External link (1), verified loading 2026-10-15:** BC Laws, Ozone Depleting Substances and Other Halocarbons Regulation (B.C. Reg. 387/99, s. 7(1) and the "approved person" definition in s. 1). Open in a new tab with rel="noopener noreferrer". The BC Coroners heat dome death statistics were removed in review (2026-10-16) to avoid fear-based framing under the client's no-urgency rule.
- **People Also Ask:** Search tools did not return a literal PAA box. FAQ questions were chosen from the recurring questions across the top-ranking pages for the keyword and its variants (running but not cooling, whether to turn it off, frozen coil thaw time, heat pump warm air in cooling mode). A fifth, "Can I add refrigerant myself?", was cut for length because the body already answers it; it is kept in the GBP post. Confirm against a live Google PAA check or Semrush once API units reset.
- **Omitted / not verified:** No filter replacement interval given (no Canadian source confirmed). No specific thaw time stated beyond "a few hours / most of a day" (sources vary). The "93% without air conditioning" heat dome figure appears in media coverage but was not in the government release I could verify, so it was left out. FortisBC gas emergency line not used (AC is electric; the safety line points to the breaker and 911 instead). Brands named in the CTA (Lennox, Carrier, Trane, Rheem) are from the client's serviced-brands list; confirm the new repair team covers AC/heat pump repair on all four.
- **Review:** Run the blog-review-prompt in a fresh chat before sending to the editor.
