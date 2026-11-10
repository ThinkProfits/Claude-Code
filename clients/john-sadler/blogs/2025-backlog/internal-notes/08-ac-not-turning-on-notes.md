# Internal notes: 08-ac-not-turning-on

Not client facing. Never paste into the Google Doc.

## Scope

> **EDITOR ONLY (remove before publishing):** Troubleshooting guide for a central air conditioner or heat pump that won't start at all in cooling mode (as opposed to running and blowing warm air), covering the thermostat, power, safety-switch and outdoor-unit checks a homeowner can safely make, and when to book AC or heat pump repair with John Sadler.

## Image Note

*Image note: all images must be real John Sadler job photos. Never use AI-generated images.*

---

## GBP Post

AC not turning on? Before you call, check the thermostat batteries and setting, the breakers, the disconnect box beside the outdoor unit and the power switch near your furnace. If it still won't start, or the outdoor unit hums without running, our licensed technicians repair central air conditioners and heat pumps across South Surrey, White Rock and Langley.

**Q: Why won't my AC turn on after a power outage?** Most systems wait a few minutes before restarting. If it still won't start, check the breakers and thermostat.

**Q: Should I keep resetting the breaker?** No. Reset it once. If it trips again, leave it off and call a technician.

**CTA button:** Learn more (link: [blog URL])

---

## Facebook Post

Switched your AC on for the first warm day and nothing happened? Before you book a service call, there are a few quick checks worth making. Our new guide walks through the thermostat, breaker and safety-switch checks, and when it's time to call a technician: [blog URL] #SurreyBC #ACRepair

## Instagram Post

AC not turning on? Check the thermostat, the breakers and the disconnect beside the outdoor unit first. Still nothing? We can help. Full guide at the link in our bio. #SurreyBC #WhiteRock #ACRepair #HeatPump

---

## Implementation Notes

- **BLOCKER, fix before publishing:** Same as the other AC posts. The live [/services/heating-cooling/air-conditioning/](https://www.johnsadler.ca/services/heating-cooling/air-conditioning/) and [/services/heating-cooling/heat-pumps/](https://www.johnsadler.ca/services/heating-cooling/heat-pumps/) pages still say installs only and refer repairs elsewhere. Remove that copy before this post goes live.
- **Publish order:** Publish after `/blog/ac-not-blowing-cold-air/` (#1), because this post links to it. If #1 isn't live yet, remove that link until it is.
- **Publish timing:** Seasonal. Keyword Planner shows searches climb from April and peak in May (about 2.5 times the yearly average). Best published March to April 2027, earlier than the other AC posts, because "won't turn on" peaks at first start-up.
- **Cannibalization check:** No existing johnsadler.ca post targets "ac not turning on" (checked against the post list gathered for this backlog on 2026-10-15). Internal overlap with draft #1 (AC not blowing cold air): #1 has short "thermostat set wrong" and "tripped breaker" sections. This post is scoped to a system that won't start at all, and links to #1 for the warm-air case. **Recommended:** add a link from #1's breaker section to this post ("If the AC won't start at all, see our guide to an AC not turning on").
- **Title:** Masterlist title is "Why Won't My AC Turn On?". The title tag and H1 lead with "ac not turning on" (390) instead of "why won't my ac turn on" (50); the question form is the first FAQ.
- **Schema:** FAQPage for the four FAQs. Article (BlogPosting) for the post.
- **Internal links (6 distinct pages):** /blog/ac-not-blowing-cold-air/ (draft, see publish order), /blog/comparing-different-thermostats/, /services/heating-cooling/air-conditioning/, /services/heating-cooling/heat-pumps/, /contact-us/, plus the phone link. Only 5 live destinations exist for this topic until #1 publishes; the site has no other AC troubleshooting posts to link to.
- **External link (1 source, cited twice), verified loading 2026-11-10:** Natural Resources Canada, "Air Conditioning Your Home" (22 to 25°C thermostat range; power to the central unit shut off when the cooling season ends). Open in a new tab with rel="noopener noreferrer".
- **People Also Ask:** No live PAA pull (Semrush units). FAQs chosen from the recurring questions across the top-ranking pages for the keyword and its variants (thermostat set to cool, outside unit not starting, after a power outage, breaker resets). Re-check with Semrush `phrase_questions` when units are restored.
- **Omitted / not verified:** No exact compressor delay time (varies by model; "a few minutes" used). No prices. Brands in the CTA come from the client's serviced-brands list.
- **Colin to confirm:** that their crews commonly shut off central AC disconnects in the fall (the post frames it as something "many homeowners and technicians" do), and that float switches are common on the systems they service.
- **Review:** Run the blog-review-prompt in a fresh chat before sending to the editor.
