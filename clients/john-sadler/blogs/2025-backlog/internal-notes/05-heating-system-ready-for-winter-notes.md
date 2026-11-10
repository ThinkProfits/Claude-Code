# Internal notes: 05-heating-system-ready-for-winter

Not client facing. Never paste into the Google Doc.

## Scope

**Draft 05 (Sep 2025 slot):** How to Get Your Home Heating System Ready for Winter
**Scope line (editor review only, remove before publishing):** How-to checklist that walks Surrey-area homeowners through winter prep one heating system at a time (gas furnace, boiler/combi/radiant in-floor, heat pump, Navien tankless), then a short "every home" section that links to the existing fall-prep post instead of repeating it.
**Masterlist row:** September 2025, Blog #1 (topic approved). Drafted 2026-10-15.

## Image Note

**Image note:** All images must be real John Sadler photos (technicians, vans, real installs). Never use AI-generated images. Three placements are marked above; a fourth can be added near the "Every Home" section (suggested: technician testing a CO alarm, file: carbon-monoxide-alarm-test.jpg, alt: Technician testing a carbon monoxide alarm near a bedroom).

---

## GBP Post

Is your home ready for winter? The checklist depends on your system: furnaces need fresh filters and a gas safety inspection, boilers need a pressure check, heat pumps need clear space around the outdoor unit, and Navien tankless units need annual descaling. Our new guide breaks it down by system so you can get your heating system ready for winter in one afternoon, then book the tune-up with our licensed gas fitters.

Q: How often should a furnace be tuned up? A: Once a year, ideally in early fall before the heating season starts.

Q: Is frost on my heat pump normal? A: A light layer is normal, and the unit clears it with a short defrost cycle. Thick ice that stays is not.

CTA button: Learn more (link to blog URL). Alternate: Call now.

---

## Facebook Post

Furnace, boiler, heat pump or Navien tankless? Each one needs a different pre-winter checklist, and our new guide walks through all four so you know exactly what to check yourself and what to leave to a licensed technician. Read it here: [BLOG URL] #SurreyBC #HomeHeating

---

## Instagram Post

Not every home runs on a furnace. Our new winter checklist is organised by system type (gas furnace, boiler and radiant in-floor, heat pump and Navien tankless) so you can get your heating system ready in one afternoon. Link in bio. #SurreyBC #WhiteRockBC #FurnaceTuneUp #HeatPump

---

## Implementation Notes

- **Publish timing:** This is a September 2025 masterlist row being drafted mid-October 2026. Publish as soon as approved; the topic is most useful before the first sustained cold weather and the peak tune-up booking period. Set the publish date to the actual go-live date, not a back-dated September 2025 date.
- **Schema:** FAQPage (four Q&As above, written link-free and brand-free for schema). Article (BlogPosting). HowTo is optional; the post is a checklist by system rather than a single linear procedure, so FAQPage + Article is enough.
- **Cannibalization:** Existing posts already cover generic fall prep (/blog/prep-plumbing-heating-for-fall/: hoses, sprinklers, pipe insulation, CO detectors, filters, registers) and furnace tips (/blog/home-furnace-maintenance-tips/, /blog/furnace-maintenance/). This post is differentiated by structuring around each system type the client services. It does not repeat hoses, sprinklers or pipe insulation; it links to /blog/winterize-your-plumbing/ and /blog/prep-plumbing-heating-for-fall/ instead. The furnace section is kept short and links out to /blog/furnace-service-frequency/ rather than re-covering existing furnace content.
- **Consolidation recommendation (later):** /blog/furnace-maintenance/ (about 250 words) and /blog/home-furnace-maintenance-tips/ (about 450 words) are thin and overlap each other and this post's furnace section. Consider merging them into one stronger "furnace maintenance checklist" post (target: furnace maintenance checklist, 110/mo) and 301-redirecting the other. Not urgent; revisit after this post is indexed.
- **Internal links (9 distinct, trimmed from 13 in review on 2026-10-15; removed furnace filter, furnace shutting off, radiant boiler care and heat pump vs furnace blog links):** Current list: /blog/winterize-your-plumbing/, /blog/furnace-service-frequency/, /blog/annual-boiler-service/, /services/heating-cooling/boiler-repair/ (twice: body and CTA), /services/heating-cooling/heat-pumps/, /services/navien/, /blog/prep-plumbing-heating-for-fall/, /services/heating-cooling/furnace-repair/, /contact-us/. Sentences that referred to the removed posts were rewritten in review on 2026-10-16.
- **External links (2, both verified loading 2026-10-15):** Natural Resources Canada, Heating and cooling with a heat pump (defrost behaviour, 3-month filter, annual contractor service). Technical Safety BC, Carbon Monoxide Safety (CO alarms every floor and near bedrooms, test monthly, replace every 7 to 10 years, annual gas appliance inspections, rental Gas Safety Regulation requirement). Open both in a new tab with rel="noopener noreferrer".
- **Verified but not linked:** FortisBC emergency line 1-800-663-9911 (24 hours) or 911, and the stop / go outside / call steps, confirmed on fortisbc.com "Gas leaks and odour" page. Navien annual maintenance guidance (flush heat exchanger; clean water screens, air filter and condensate trap) confirmed on navieninc.com maintenance blog posts.
- **Omitted or unverifiable:**
  - Heat pump outdoor clearance of 30 to 60 cm: the only source found was a Quebec contractor blog, not NRCan or a manufacturer. Replaced with "the minimum clearance listed in your installation manual."
  - Lower Mainland weather claims (wet, mild winters, arctic outflow frequency): not verified with Environment Canada, so no specific weather claims are made beyond "the first cold snap."
  - Health Canada CO alarm placement guidance: the Health Canada CO page found does not give placement or replacement guidance (the "preventing exposure" subpage URL returned 404). Technical Safety BC was used instead as the BC authority.
  - Specific boiler pressure numbers: ranges vary by system, so readers are pointed to their manual and gauge markings instead.
  - BC proposal to make CO alarms mandatory in existing homes: status unconfirmed, so not mentioned.
- **Title tag vs H1:** Title tag uses "Get Your Heating System Ready for Winter" (fits 54 characters with brand); H1 keeps the approved masterlist title "How to Get Your Home Heating System Ready for Winter." Editor can align them if strict matching is required.
- **Service areas:** Surrey, White Rock and Langley mentioned once in the intro; South Surrey and Langley appear only in image alt/descriptions. No Abbotsford.
- **Review step:** Run the blog-review-prompt on this draft in a fresh conversation before sending to the editor.
