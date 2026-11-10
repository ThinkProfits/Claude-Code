# Internal notes: 02-how-does-a-heat-pump-work

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, remove before publishing):** Beginner explainer covering how a heat pump works mechanically (refrigerant cycle, heating vs cooling mode, winter operation, defrost, COP, backup heat, ducted vs ductless, air-source vs ground-source), with no heat pump vs furnace or heat pump vs AC comparison sections.
**Masterlist row:** July 2025 Blog #2, "How Does a Heat Pump System Work? A Beginner's Guide to Understanding the Technology" (topic approved)

## Image Note

All images must be real John Sadler job photos, never AI-generated.

---

## GBP Post

How does a heat pump work? It moves heat instead of making it: refrigerant pulls warmth from the outdoor air, a compressor concentrates it, and an indoor coil releases it into your home. In winter, the outdoor unit may give off a cloud of steam during its defrost cycle, which is completely normal. Our new guide explains the refrigerant cycle, efficiency and backup heat in plain language.

Q: Does a heat pump work below freezing? A: Yes. Standard models may need backup heat somewhere between -10°C and -15°C, and cold-climate models can operate down to about -30°C.

Q: Why is my heat pump steaming? A: It's usually the defrost cycle melting frost off the outdoor coil.

CTA button: Learn more (link to blog URL)

## Facebook Post

Ever wondered how a heat pump can heat your home when it's cold and damp outside? It's all about moving heat, not making it, and that cloud of steam from the outdoor unit on a frosty morning is usually just the defrost cycle doing its job. Our new beginner's guide explains it in plain language: [BLOG URL] #HeatPump #SurreyBC

## Instagram Post

Heat pumps don't make heat, they move it. Refrigerant collects warmth from outdoor air (yes, even in a Lower Mainland January), and a compressor turns it into cozy indoor heat. Seeing steam from your outdoor unit? That's the defrost cycle, and it's normal. Read the full guide at the link in our bio. [BLOG URL]

#HeatPump #SurreyBC #WhiteRock #LangleyBC #HomeHeating #JohnSadlerPlumbing

---

## Implementation Notes

- **Schema:** Article schema on the post (one line). FAQPage schema on the five FAQs (answers are link-free and unbranded for this reason).
- **Publish date:** Masterlist slot is July 2025 (backlog). Publish with the current date; a "how it works" explainer is evergreen, but the winter and defrost sections make a fall/winter publish timely.
- **Title:** The masterlist working title ("How Does a Heat Pump System Work? A Beginner's Guide to Understanding the Technology") is too long for a title tag and the skill requires the H1 to match the title tag, so both use "How Does a Heat Pump Work? A Surrey, BC Guide." The "beginner's guide" framing is kept in the intro and social copy. Swap the H1 back to the masterlist title if the editor prefers.
- **Cannibalization:** Overlap checked against /blog/heating-with-heat-pump-or-furnace/ (has a short "How Heat Pumps Work" H2), /blog/heat-pump-vs-ac-unit/, /blog/ac-heat-pump-ductless-split/ and /blog/know-before-installing-heat-pump-ac/. This post stays on the mechanism (refrigerant cycle, reversing valve, winter operation, defrost, COP, backup heat types) and contains no heat pump vs furnace or heat pump vs AC comparison section; it links out to each of those four posts for the decision content instead. None of the existing posts covers defrost, COP or the step-by-step refrigerant cycle.
- **Recommended update to existing post:** In /blog/heating-with-heat-pump-or-furnace/, add a link at the end of the short "How Heat Pumps Work" section, e.g. "For a step-by-step look at the refrigerant cycle, defrost mode and efficiency, see [how does a heat pump work?](https://www.johnsadler.ca/blog/how-does-a-heat-pump-work/)". That makes the new post the canonical "how it works" page and keeps the older post focused on the furnace decision. That section's description (heat "transferred into water via pipes, allowing for radiators") is also loose and could be trimmed once it links here.
- **Side note on existing content (not changed):** /blog/heat-pump-vs-ac-unit/ still quotes "a rebate of up to $10,000", which conflicts with the brief's no-amounts rule and FortisBC's Dec 2025 program changes. Worth a refresh.
- **Internal links (8 distinct):** /services/heating-cooling/heat-pumps/ (CTA), /blog/heat-pump-vs-ac-unit/, /blog/afue-ratings-explained/, /blog/heating-with-heat-pump-or-furnace/, /blog/ac-heat-pump-ductless-split/, /blog/know-before-installing-heat-pump-ac/, /fortisbc-rebates/, /contact-us/. First internal link appears in the "Heating Mode vs Cooling Mode" section, within the first half.
- **External links (2, both verified loading 2026-10-15, open in new tab with rel="noopener noreferrer"):** NRCan "Heating and cooling with a heat pump" (https://natural-resources.canada.ca/energy-efficiency/energy-star-canada/about/energy-star-announcements/publications/heating-and-cooling-heat-pump/6817, page modified 2025-12-24): source for the "moves heat" definition, refrigerant cycle, defrost every 30/60/90 minutes with outdoor fan off, COP ranges, hybrid system operation, ground-source no defrost and COP around 3, and 15 to 20 year service life. NRCan "Heat pumps" (https://natural-resources.canada.ca/energy-efficiency/home-energy-efficiency/canada-greener-homes-initiative/heat-pumps): source for supplemental heat at -10°C to -15°C and cold-climate operation to -30°C.
- **Claims kept general on purpose:** Steam during defrost is standard HVAC knowledge but is not stated in the NRCan guide, so it's explained as meltwater evaporating rather than cited. Lower Mainland climate is described qualitatively (mild, wet, short cold snaps) with no temperature statistics. "Dual-fuel suits the many Lower Mainland homes with gas and ductwork" is framed as fit, not as a statistic.
- **Omitted:** No rebate amounts or prices (brief rule). NRCan's "up to 2.5/3/3.5 times more efficient than an oil furnace" figures were left out because oil heat is not relevant to the client's market and the client does not service oil. Ground-source installation is described but not offered as a John Sadler service, since the brief doesn't confirm the client installs geothermal; confirm before adding it. Navien is not mentioned. Navien does make heat pumps (NAZ series, covered in the planned Navien heat pump error codes post), but whether John Sadler installs them isn't confirmed; add a Navien line if the client confirms. No 24/7 or emergency language.
- **Heat pump repairs:** The client has offered heat pump repairs only since Aug 2026 (early stage). Copy says "installation and service" per the brief, with no repair-specific claims; confirm the client is comfortable promoting heat pump service at this stage.
- **Images:** Three placements suggested; all must be real John Sadler job photos, never AI-generated.
- **Review:** Run the blog-review-prompt in a fresh chat before sending to the editor.
