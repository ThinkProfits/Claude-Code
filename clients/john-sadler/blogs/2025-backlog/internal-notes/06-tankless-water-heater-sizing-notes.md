# Internal notes: 06-tankless-water-heater-sizing

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, remove before publishing):** How-to sizing guide that walks homeowners through choosing a tankless water heater size using flow rate and temperature rise, with a worked South Surrey example, plain-language BTU explanation, recirculation, gas line and venting checks, and why a sizing visit beats an online calculator. Purely sizing; the "should I go tankless" decision is handed off to existing posts.
**Masterlist:** September 2025, Blog #2

## Image Note

*Image note: all images must be real John Sadler Plumbing & Heating photos (team, vans, completed installs). Never use AI-generated images.*

---

## GBP Post

Wondering what size tankless water heater your home needs? It comes down to how much hot water you use at once and how cold your water gets in winter. Our new guide walks through a real South Surrey example, plus the gas line and venting checks that decide whether a unit performs as rated. Call (604) 531-4355 to book a sizing visit.

**Q: How many showers can a tankless water heater run at once?**
A: It depends on the unit's output at your winter temperature rise. A unit delivering about 5 GPM in winter can usually handle two showers at once.

**Q: Do I need a bigger gas line for a tankless water heater?**
A: Often, yes. Large tankless units use far more gas than most tanks, so a licensed gas fitter checks your line size and length before installation.

CTA button: Learn more, linking to [BLOG URL]

---

## Facebook Post

Two showers and the dishwasher running at once on a cold January morning: that's the moment a tankless water heater has to be sized for. Our new guide explains flow rate, temperature rise and why we measure your incoming water before recommending a unit. [BLOG URL] #TanklessWaterHeater #SurreyBC

## Instagram Post

What size tankless water heater do you actually need? The answer comes from how much hot water you use at once and how cold your water gets in winter. Full sizing guide at the link in our bio. #TanklessWaterHeater #Navien #SouthSurrey #SurreyBC

---

## Implementation Notes

- **Schema:** FAQPage on the five FAQ Q&As; Article (BlogPosting) for the post. HowTo is optional for the 4-step section. No JSON-LD in this draft.
- **Title tag vs. H1:** H1 keeps the approved masterlist title. The title tag leads with the exact primary keyword to stay within 60 characters, so the two don't match exactly. The approved H1 also has no city; "Surrey, BC" appears in the intro instead. Editor to confirm.
- **Quick Answer:** use the WordPress "Preformatted" block.
- **Cannibalization:** this post is sizing only. "Should I go tankless" is covered by /blog/tankless-water-heater-right-for-my-home/, benefits by /blog/upgrading-to-tankless-water-heater/ and the tank vs. tankless comparison by /blog/conventional-vs-tankless-water-heaters/. Two of these are linked from the gas lines section to send readers there for the decision. /blog/upgrading-to-tankless-water-heater/ is not linked from this post. The existing "right for my home" post mentions tankless output of "about 5-6 gallons per minute"; this post gives model-specific figures at a stated temperature rise, so the two don't contradict each other. That older post could be updated later to link here. Note that the live "upgrading" post quotes FortisBC rebate amounts ($200 to $1,000) and a "98%" efficiency figure; both should be checked separately.
- **Internal links (9 distinct):** /services/plumbing/tankless-water-heaters/, /services/navien/, /services/gas-fitting/, /blog/why-choose-navien/, /blog/shower-taking-a-long-time-to-heat/, /blog/tankless-water-heater-right-for-my-home/, /blog/conventional-vs-tankless-water-heaters/, /fortisbc-rebates/, /contact-us/.
- **External links (2), both loaded and checked 2026-10-15; open in new tab with rel="noopener noreferrer":**
  - Navien Canada, "Sizing Tankless Water Heaters" (navieninc.ca): source for "use the coldest days of the year" and the 65°F example method.
  - Navien NPE-2 Series QuickFacts / spec sheet PDF (navieninc.com/downloads/npe-2-quickfacts-en/download): source for BTU input ranges (150,000 / 180,000 / 199,900 BTU/h max), the built-in buffer tank and recirculation pump, and flow at each temperature rise. Navien Canada's site redirects product and spec pages to navieninc.com, so no .ca version of the spec sheet was available. The fixture flow figures (shower 2 to 3 GPM, dishwasher 2 to 3 GPM, washer 3 to 5 GPM) come from Navien's sizing article on navieninc.com (Sept 13, 2024), which covers the same method as the Canadian article and adds the fixture figures. Swap the first external link to that .com version if the editor prefers the fixture figures directly sourced.
- **Flow figures at 75°F rise (3.9 / 4.7 / 5.2 GPM):** read from the temperature rise table in the spec sheet PDF. The PDF text came out misaligned when extracted, so the values were cross-checked against the clean 35°F, 45°F and 67°F figures on the same sheet and against the BTU formula (input × efficiency ÷ (500 × rise)). All three line up. Editor may want to glance at the PDF table to confirm.
- **Worked example assumptions (presented in the post as illustration, not as fact):** 7°C winter inlet, 49°C set point, about 40°C shower mix (gives about 79% hot share, so about 1.6 GPM hot of a 2 GPM shower). The 500 BTU per GPM per °F rule and the 57 kW electric figure (195,000 BTU/h ÷ 3,412) are standard conversions.
- **Omitted / unverifiable:**
  - Lower Mainland groundwater or municipal inlet water temperature: no credible published winter figure found (Metro Vancouver and municipal water quality reports were checked but no winter value was confirmed). The post explains the concept and says we measure it on site.
  - NRCan fixture flow rates: NRCan's showerhead and faucet pages are 2022 proposal bulletins (6.8 L/min proposed) that conflict with the reported final 2026 federal rule (7.0 L/min per IAPMO). These were not used, and Navien's published fixture ranges were used instead.
  - Specific gas pipe sizes (for example, a 3/4" minimum for about 200,000 BTU) and venting lengths (Navien US page: 2" PVC up to 75 ft): not used, because they depend on code tables and site conditions and the venting figure was only on the US page.
  - Navien cascade limits and ComfortFlow performance claims beyond "buffer tank and recirculation pump": not used.
  - No prices, rebate amounts, 24/7 or emergency claims, or superlatives.
- **NSS wording:** Navien's own page calls it "Navien Service Specialist (NSS)"; the client file says "Navien Certified Service Specialist". The post says "certified by Navien as a Navien Service Specialist (NSS)" to satisfy both.
- **Publish date:** backdated masterlist slot (September 2025, Blog #2). Confirm the publish date with the editor before scheduling.
- **Review:** run the blog-review-prompt in a fresh chat before sending to the editor.
