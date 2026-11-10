# Internal notes: 04-common-hot-water-tank-problems

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, delete before publishing):** Symptom-by-symptom troubleshooting guide covering the most common gas and electric hot water tank problems (no hot water, running out fast, pilot going out, leaks, dripping relief valve, noise, rotten egg smell, rusty water, water too hot), each with the likely cause, what a homeowner can safely do, and when to call; it deliberately does not cover replacement signs or tank lifespan (those live on /blog/replace-water-heater/).
**Masterlist:** August 2025, Blog #2, "Common Hot Water Tank Issues & What to Do About Them" (topic approved)

## Image Note

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

Cold shower, puddle by the tank, or a strange rumble from the basement? Our new guide covers the most common hot water tank problems in gas and electric tanks, what you can safely check yourself, and when it's time to call a licensed technician. Q: Can I use my hot water tank if it's leaking? A: Turn off the cold supply and the gas or breaker first, then find the source; a fitting or drain valve leak is usually repairable, but a leak from the tank body means the tank has failed. Read the full guide or call our Surrey team at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

No hot water, a leaking tank, or water that smells like rotten eggs? We've put together a symptom-by-symptom guide to the most common hot water tank problems, with the safe checks you can do yourself and the signs it's time to call us. [blog URL] #SurreyBC #HotWaterTank

## Instagram Post

Rumbling, popping, leaking or no hot water at all? Our latest blog breaks down common hot water tank problems and what to do about each one, from checking the pilot light to knowing when to call a licensed technician. Link in bio. [blog URL] #HotWaterTank #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **Schema:** FAQPage for the four FAQs (answers contain no links or branded language, per brief). Article/BlogPosting with author John Sadler Plumbing & Heating. No HowTo schema (this is diagnostic, not a single procedure).
- **Publish date:** Masterlist slot is August 2025 (backlog). Publish with the current date rather than backdating, unless the team prefers to fill the August 2025 archive slot.
- **Cannibalization / differentiation from /blog/replace-water-heater/ (site's top organic post):** That post owns "signs it's time to replace," lifespan, tank age, repair vs replace and tankless upgrade. This post deliberately has no replacement-signs list, no lifespan or age section, and no repair-vs-replace FAQs. It targets the symptom/diagnosis query cluster (hot water tank problems/issues, no hot water, leaking, noise, pilot going out, rotten egg smell). Where replacement is the honest answer (tank-body leak, internal rust), it links to /blog/replace-water-heater/ with descriptive anchors (2 links, the skill's cap for one destination: "when to replace a hot water tank" in the intro and "replacing a hot water tank" in the tank-body leak H3; the rusty water H3 mentions replacement without a third link). Recommend adding a reciprocal link from replace-water-heater's leak and noise bullets to this post ("common hot water tank problems") so the two posts read as a pair.
- **Overlap with /blog/water-heater-replace-repair/:** older thin repair-vs-replace post; no conflict with this troubleshooting angle, but it competes with replace-water-heater, so consider consolidating it into that post separately.
- **Internal links (6 distinct):** /blog/replace-water-heater/, /blog/shower-taking-a-long-time-to-heat/, /blog/thermal-relief-valve-dripping/, /services/plumbing/tankless-water-heaters/, /services/plumbing/hot-water-tanks/ (main CTA), /contact-us/.
- **External links (2, both verified loading 2026-10-15, open in new tab with rel="noopener noreferrer"):** FortisBC gas leaks and odour page (emergency line 1-800-663-9911 confirmed on page), canada.ca Public Health Agency of Canada water temperature page (60°C / 49°C figures quoted from page).
- **Facts to confirm with client:**
  - "Text a photo of your tank to (604) 531-4355" is taken from the live replace-water-heater post; confirm the number still accepts texts.
  - Anti-scald mixing valves are mentioned as general safety guidance only, not as a John Sadler service; confirm whether the client installs them before adding any service language.
  - Brands listed in the CTA are from the brief's serviced-brands list.
- **Wording decisions / omitted or unverifiable facts:**
  - The brief said "Health Canada" for the 49°C guidance; the current canada.ca page is from the Public Health Agency of Canada, so the post attributes it to PHAC. The guidance is 60°C at the tank plus 49°C at the tap via mixing valves (not "set the tank to 49°C"), and the post reflects that.
  - Licensing: the post says gas parts, venting and wiring are "a job for a licensed gas fitter or technician" rather than stating a legal requirement, since Technical Safety BC has homeowner permit provisions for some gas work in a person's own home. Flagged rather than overstated.
  - Flushing frequency ("at least once a year") is framed as manufacturer guidance (consistent with AO Smith's published advice and the client's own replace-water-heater post) and points readers to their manual; no statistic cited.
  - No prices, rebates, discounts, 24/7 or emergency-service claims used. Business hours stated as Mon to Fri 8:30 to 5:00 per brief.
- **Images:** 4 placements, all must be real John Sadler photos, never AI or stock.
- **PAA research:** FAQ questions chosen from People Also Ask-style queries (leaking tank use, flushing frequency, relighting pilot, rotten egg smell in hot water only); a tank-temperature question was dropped because the body already answers it and the post was at the word cap. Lifespan, age and repair-vs-replace questions excluded because they are already in the replace-water-heater FAQ.
- **Quick Answer:** use the WordPress Preformatted block.
- **H1 vs title tag:** H1 keeps the approved masterlist wording, keyword-first ("Hot Water Tank Problems and What to Do About Them"); the title tag uses "& Fixes in Surrey, BC" for the local signal within 60 characters. If the editor wants a strict H1/title match, use "Hot Water Tank Problems & Fixes in Surrey, BC" as the H1.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
