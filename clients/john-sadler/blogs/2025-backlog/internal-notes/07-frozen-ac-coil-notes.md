# Internal notes: 07-frozen-ac-coil

Not client facing. Never paste into the Google Doc.

## Scope

> **EDITOR ONLY (remove before publishing):** How-to guide covering why an air conditioner or heat pump coil freezes in cooling mode, how a homeowner can safely thaw it, how to tell whether the cause is a simple fix or a technician repair, how to prevent it, and how winter frost on a heat pump differs from a summer freeze-up.

## Image Note

*Image note: all images must be real John Sadler job photos. Never use AI-generated images.*

---

## GBP Post

Seeing ice on your AC lines? A frozen AC coil usually means low airflow or low refrigerant. Turn cooling off, set the fan to On to melt the ice, and replace a dirty filter. If it freezes again, our licensed technicians can find the cause and repair central air conditioners and heat pumps across South Surrey, White Rock and Langley.

**Q: Can I run my AC while the coil is frozen?** No. Turn cooling off and run the fan until the ice melts, since running it can damage the compressor.

**Q: Why does my AC keep freezing up?** A dirty filter or closed vents are the usual cause. If it keeps happening with a clean filter, call a technician to check the refrigerant and blower.

**CTA button:** Learn more (link: [blog URL])

---

## Facebook Post

Ice on your air conditioner in the middle of summer? A frozen AC coil is more common than you'd think, and the first fix is something you can do yourself. Our new guide walks through how to thaw it safely, why it happens and when to call a technician: [blog URL] #SurreyBC #ACRepair

## Instagram Post

Frozen AC coil? Turn cooling off, run the fan and check your filter. If it freezes again, give us a call. Full guide at the link in our bio. #SurreyBC #WhiteRock #ACRepair #HeatPump

---

## Implementation Notes

- **BLOCKER, fix before publishing:** Same as the AC post (#1). The live [/services/heating-cooling/air-conditioning/](https://www.johnsadler.ca/services/heating-cooling/air-conditioning/) and [/services/heating-cooling/heat-pumps/](https://www.johnsadler.ca/services/heating-cooling/heat-pumps/) pages still say installs only and refer repairs elsewhere. Remove that copy before this post goes live.
- **Publish order:** Publish after `/blog/ac-not-blowing-cold-air/` (#1 in this folder), because this post links to it. If #1 isn't live yet, remove that link until it is.
- **Publish timing:** Seasonal. Keyword Planner shows the peak runs May to August (July is roughly 3 to 4 times the yearly average). Best published April to May 2027.
- **Cannibalization check:** No existing johnsadler.ca post targets frozen AC coils (checked against the post list gathered for this backlog on 2026-10-15; the sitemap returned 403 to a direct fetch on 2026-11-10). The only overlap is internal: draft #1 (AC not blowing cold air) has a short "Frozen Evaporator Coil" section and a thaw-time FAQ. This post goes deeper (signs, full thaw steps, causes, prevention, winter heat pump frost). **Recommended:** in #1, keep section 6 short and add a link to this post from it ("our full guide to fixing a frozen AC coil"), and consider dropping #1's "How long does it take a frozen AC coil to thaw?" FAQ so the two pages don't compete for that question.
- **Title:** Masterlist title is "How to Fix Frozen AC Coils?". The title tag and H1 lead with the higher-volume "frozen ac coil" (210) instead of "how to fix frozen ac coils" (10); the how-to phrasing sits in the intro and the step-by-step H2.
- **Schema:** FAQPage for the four FAQs. Article (BlogPosting) for the post. HowTo is optional for the six-step thaw section.
- **Internal links (8 distinct):** /blog/ac-not-blowing-cold-air/ (draft, see publish order), /blog/furnace-filter/, /blog/furnace-service-frequency/, /blog/heat-pump-vs-ac-unit/, /services/heating-cooling/heat-pumps/, /services/heating-cooling/air-conditioning/, /contact-us/, plus the phone link.
- **External links (2), both verified loading 2026-11-10:** BC Laws, Ozone Depleting Substances and Other Halocarbons Regulation (B.C. Reg. 387/99, s. 7(1)); Natural Resources Canada, "Heating and cooling with a heat pump" (defrost cycle section). Open in a new tab with rel="noopener noreferrer".
- **People Also Ask:** No live PAA pull (Semrush units). FAQs chosen from the recurring questions across the top-ranking pages for the keyword and its variants (thaw time, running while frozen, repeat freezing, heat pump frost in winter). Re-check with Semrush `phrase_questions` when units are restored.
- **Omitted / not verified:** No specific outdoor temperature below which an AC shouldn't run (manufacturer figures vary, no Canadian source). No filter replacement interval beyond "check monthly in cooling season". No prices. Brands in the CTA come from the client's serviced-brands list; confirm the repair team covers AC/heat pump repair on all four.
- **Colin to confirm:** the "emergency or auxiliary heat" advice for an iced-over heat pump fits the systems they install, and the six thaw steps match what the office tells callers.
- **Review:** Run the blog-review-prompt in a fresh chat before sending to the editor.
