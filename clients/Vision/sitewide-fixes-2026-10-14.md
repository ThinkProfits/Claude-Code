# Vision: sitewide fixes from the heat pump page feedback (2026-10-14)

**Why this exists:** feedback on the heat pump installation page edits (2026-10-14) listed six problems. This doc checks every page and post on visionplumbingandheating.com for the same problems and lists the exact fixes.

**Scan:** all 257 sitemap URLs (67 pages, 190 posts), raw HTML, crawled 2026-10-14. Customer Google reviews and the testimonials page were skipped, because we don't edit customer quotes.

**Access:** we have no WordPress connection for Vision, so each fix below needs to be made in Elementor by hand. Where we found the Elementor widget ID (`data-id`), it's included so the right block is easy to find.

**The rules behind every fix (from the feedback, plus CLIENT.md):**
1. The only phone number on the site is **250-470-9552** (`tel:2504709552`). CallRail swaps it for visitors automatically. A hard-coded tracking number breaks that and throws off call metrics.
2. Vision does **not** offer free quotes, estimates or consultations.
3. Vision does **not** do rebate paperwork. They help with information and eligibility only.
4. Heat pump installs take **1 to 3 days**, which is what the heat pump page says. Other pages must not contradict it.
5. **No em dashes** in content.
6. Put new content into the existing section on the same topic instead of adding a near-duplicate section. Keep "Why Choose" high on the page.

---

## Priority 1: hard-coded CallRail numbers (5 pages) and a wrong number (3 posts)

**Status: DONE 2026-10-14 (Francis, via the wp-vision MCP).** All 8 now show 250-470-9552, including the `tel:` links and a schema ContactPoint on the emergency furnace page. We checked the live pages and confirmed nothing else in the stored content changed. Wording was left as is: the CTA rewording and the "emergency line" phrasing still need Andrew's approval. Originals are backed up in the session scratchpad. Each page also has a WordPress revision.

| Page | Widget | Current | Replacement |
|---|---|---|---|
| [/residential/heating-cooling/heat-pump-installation-kelowna/](https://visionplumbingandheating.com/residential/heating-cooling/heat-pump-installation-kelowna/) | Installation process list, `data-id=8b2cea6` (still there after this week's edits) | "…by giving us a call today at [778-760-1221](tel:778-760-1221)." | "…by giving us a call today at [250-470-9552](tel:2504709552)." |
| [/residential/heating-cooling/air-conditioning-installation-kelowna/](https://visionplumbingandheating.com/residential/heating-cooling/air-conditioning-installation-kelowna/) | Closing CTA paragraph, `data-id=289cdd5` | "Call [778-946-6884](tel:778-946-6884) or contact us online to get your new AC unit across the Okanagan." | "Call [250-470-9552](tel:2504709552) or contact us online to book your new AC installation anywhere in the Okanagan." |
| [/residential/heating-cooling/air-conditioning-maintenance-kelowna/](https://visionplumbingandheating.com/residential/heating-cooling/air-conditioning-maintenance-kelowna/) | Closing CTA paragraph, `data-id=766226d` | "Call [778-946-6884](tel:778-946-6884) or contact us online to schedule your AC maintenance across the Okanagan." | "Call [250-470-9552](tel:2504709552) or contact us online to schedule your AC maintenance across the Okanagan." |
| [/residential/heating-cooling/furnace-installation-kelowna/](https://visionplumbingandheating.com/residential/heating-cooling/furnace-installation-kelowna/) | Closing CTA paragraph, `data-id=99adce3` | "Call [778-946-6884](tel:778-946-6884) or contact us online to get your new furnace across the Okanagan." | "Call [250-470-9552](tel:2504709552) or contact us online to book your new furnace installation anywhere in the Okanagan." |
| [/emergency-furnace-repair-kelowna/](https://visionplumbingandheating.com/emergency-furnace-repair-kelowna/) | H2 "Emergency Furnace Repair 24/7" body, `data-id=1785748` | "If needed, call our emergency line now at [778-402-9661](tel:778-402-9661) ." | "If needed, call us now at [250-470-9552](tel:2504709552)." |
| [/smart-thermostats-are-the-future-energy-solution/](https://visionplumbingandheating.com/smart-thermostats-are-the-future-energy-solution/) | Post sign-off | "Vision Plumbing Heating Cooling 250-479-9552" | "Vision Plumbing Heating Cooling [250-470-9552](tel:2504709552)" |
| [/when-should-you-call-a-professional-plumber/](https://visionplumbingandheating.com/when-should-you-call-a-professional-plumber/) | Post sign-off | "Vision Plumbing Heating Cooling 250-479-9552" | "Vision Plumbing Heating Cooling [250-470-9552](tel:2504709552)" |
| [/luxury-of-driveway-heating-systems/](https://visionplumbingandheating.com/luxury-of-driveway-heating-systems/) | Post sign-off | "Vision Plumbing Heating Cooling 250-479-9552" | "Vision Plumbing Heating Cooling [250-470-9552](tel:2504709552)" |

- **250-479-9552 is a typo** (479, not 470). It isn't a CallRail number, but it's the wrong number, so calls from those 3 posts go nowhere useful.
- Also fixed in the AC and furnace install rows: "get your new AC unit across the Okanagan" didn't read well.
- **Left alone:** 1-250-763-4918 on /okanagan-wildfire-resources-2026/ is the Regional District of Central Okanagan's line, not Vision's.
- **Header and footer:** clean. Every header and footer `tel:` link uses 250-470-9552.
- **Worth asking Vision:** the 778-402-9661 "emergency line" may have been given to us by Vision as a real after-hours line, not a tracking number. Check with Andrew before swapping it. If it is a CallRail number, swap it as above.

---

## Priority 2: rebate paperwork claims (2 pages)

| Page / section | Current | Replacement |
|---|---|---|
| /residential/heating-cooling/ · H2: Why Choose Vision Plumbing Heating Cooling? | "Licensed plumbers, gas fitters, HVAC technicians, and electricians on staff — no apprentices leading jobs. Multiple Best of Kelowna awards across plumbing, heating, and cooling. A+ BBB rating. Hundreds of five-star Google reviews. Set up to process FortisBC, BC Hydro, CleanBC, and federal Greener Homes rebates on your behalf." | "Licensed plumbers, gas fitters, HVAC technicians, and electricians on staff, with no apprentices leading jobs. Multiple Best of Kelowna awards across plumbing, heating, and cooling. A+ BBB rating. Hundreds of five-star Google reviews. We'll help you figure out which [available rebates](https://visionplumbingandheating.com/financing-rebates/residential-rebates/) your new system may qualify for." |
| /residential/heating-cooling/air-conditioning-installation-kelowna/ · intro paragraph, `data-id=a325573` | "We size every system to the building, walk you through the rebate paperwork, and stand behind the workmanship long after the truck leaves the driveway." | "We size every system to the building, explain which available rebates may apply, and stand behind the workmanship long after the truck leaves the driveway." |
| /residential/heating-cooling/air-conditioning-installation-kelowna/ · H2: What Does an AC Installation Actually Look Like? (`data-id=6664bcd`), "Commissioning and walkthrough" step | "Commissioning and walkthrough : we test the system, set the thermostat with you, register the warranty, and submit rebate paperwork." | "Commissioning and walkthrough: we test the system, set the thermostat with you, and register the warranty." |

- The /residential/heating-cooling/ line also names the **federal Greener Homes Grant**, which is closed. The last day to submit documents was December 31, 2025 (source: [Natural Resources Canada, Canada Greener Homes Initiative](https://natural-resources.canada.ca/energy-efficiency/home-energy-efficiency/canada-greener-homes-initiative)). The replacement drops it.
- **Fine as is:** "Permitting and rebate assistance handled by Vision installers" on the heat pump page reads as help, not paperwork. The feedback left it in. If we want it to be clearer: "Permits handled by Vision, plus help understanding which available rebates may apply."

---

## Priority 3: free consultation offers (1 page; 1 old post optional)

| Page / section | Current | Replacement |
|---|---|---|
| [/financing-rebates/residential-rebates/](https://visionplumbingandheating.com/financing-rebates/residential-rebates/) · "How to Apply" | "Homeowners interested in taking advantage of this rebate can contact us for more information and a free consultation . Our team of experts will guide you through the qualification process and help you select the best system for your home." | "Homeowners interested in taking advantage of this rebate can [contact us](https://visionplumbingandheating.com/contact/) for more information or to book an in-home assessment. Our team will explain the qualification requirements and help you choose the best system for your home." |
| [/2025-kelowna-spring-home-show/](https://visionplumbingandheating.com/2025-kelowna-spring-home-show/) (old event post) | "Plus, our team will be ready to provide free consultations on how to make your home more energy-efficient…" | Optional. This was a booth offer at a past event. If we change it: "Plus, our team will be at the booth to answer questions on how to make your home more energy-efficient…" |

- "guide you through the qualification process" was also changed to "explain the qualification requirements", so it doesn't suggest we do the paperwork.
- No other page or post mentions free quotes, estimates or no-obligation consultations. "Get a Quote" buttons (not free) are fine.

---

## Priority 4: install timeline contradiction (1 page)

| Page / section | Current | Replacement |
|---|---|---|
| /residential/heating-cooling/air-conditioning-installation-kelowna/ · H3: How long does AC installation take in Kelowna? | "…Ductless mini-split installs typically take one to two days depending on the number of indoor heads. Heat pump installations replacing a furnace can run one to [two days]…" | Keep the mini-split sentence. Change the heat pump sentence to: "Heat pump installations typically take 1 to 3 days, depending on the system type and home layout." (This matches the heat pump page.) |

- **Check first:** the scan cut this sentence off after "one to". Read the rest of the FAQ answer in Elementor before replacing it.

---

## Priority 5: em dashes on service pages (13 pages, 35 instances)

Fix pattern: a dash in a list item becomes a colon. A dash between clauses becomes a comma, a full stop or a reworded sentence.

| Page / section | Current | Replacement |
|---|---|---|
| **/residential/heating-cooling/heat-pump-installation-kelowna/** · H3: Are mini-splits efficient in Kelowna winters? | "Yes — modern cold-climate mini-splits maintain heating capacity well below freezing…" | "Yes. Modern cold-climate mini-splits maintain heating capacity well below freezing…" |
| heat pump page · H3: Can a mini-split cool an entire Kelowna home? | "Vision will recommend the configuration that matches your home — not a one-size-fits-all package." | "Vision will recommend the configuration that matches your home, not a one-size-fits-all package." |
| **/ac-repair-kelowna/** · H2: The Most Common Air Conditioner Repair Problems in Kelowna (7 list items) | "AC won't turn on — usually a tripped breaker…" / "AC running but not cooling — low refrigerant…" / "AC freezing up — restricted airflow…" / "Strange noises (grinding, buzzing, banging — failing fan motor…" / "Water leaking from indoor unit — blocked condensate drain…" / "AC short-cycling — oversized unit…" / "High hydro bills with no cooling improvement — efficiency loss…" | Swap each " — " for ": ". For example, "AC won't turn on: usually a tripped breaker, blown capacitor, faulty contactor, or thermostat issue". The noises item is also missing its closing bracket: "Strange noises (grinding, buzzing, banging): failing fan motor, loose component, or compressor wear". |
| **/residential/heating-cooling/air-conditioning-installation-kelowna/** · Why Choose, "Proper system sizing" | "Every install is sized to the building — square footage, insulation, ceiling height, and how Okanagan sun loads the space." | "Every install is sized to the building: square footage, insulation, ceiling height, and how Okanagan sun loads the space." |
| **/residential/heating-cooling/air-conditioning-maintenance-kelowna/** · H2: Do I Need Air Conditioner Maintenance or a Repair? | "Most Kelowna AC systems don't announce a problem loudly — they quietly get worse." | "Most Kelowna AC systems don't announce a problem loudly. They quietly get worse." |
| AC maintenance · H3: Does Vision service AC across the Okanagan? | "Yes — Kelowna (Glenmore, Rutland, …), West Kelowna, Lake Country, Peachland, Vernon, Coldstream, Penticton, Summerland, and Naramata." | "Yes. We cover Kelowna (Glenmore, Rutland, …), West Kelowna, Lake Country, Peachland, Vernon, Coldstream, Penticton, Summerland, and Naramata." |
| **/residential/heating-cooling/furnace-repair-kelowna/** · H2 heading | "Kelowna Furnace Repair Services — What We Fix" | "Kelowna Furnace Repair Services: What We Fix" |
| **/residential/heating-cooling/** · intro P1 | "The Okanagan's climate — long hot summers, increasingly common heat domes, cold but rarely extreme winters, and dry shoulder seasons — calls for a system matched to the home and the homeowner." | "The Okanagan's climate, with long hot summers, increasingly common heat domes, cold but rarely extreme winters, and dry shoulder seasons, calls for a system matched to the home and the homeowner." |
| /residential/heating-cooling/ · intro P2 | "…or chasing down a no-heat call in January — Vision is the family-owned, fully licensed Kelowna HVAC company that's been doing this for forty years." | "…or chasing down a no-heat call in January, Vision is the family-owned, fully licensed Kelowna HVAC company that's been doing this for forty years." |
| /residential/heating-cooling/ · Why Choose | (covered in Priority 2) | (covered in Priority 2) |
| **/indoor-air-quality/** · H3: Vision Pure Air Services, P1 | "…using SolaceAir products, manufactured by Dynamic Air Quality Solutions — a company with over 40 years of IAQ manufacturing experience…" | "…using SolaceAir products, manufactured by Dynamic Air Quality Solutions, a company with over 40 years of IAQ manufacturing experience…" |
| IAQ · "Important:" note | "The best solution starts with identifying the source — which is why Vision assesses your home before recommending anything." | "The best solution starts with identifying the source, which is why Vision assesses your home before recommending anything." |
| IAQ · H4: SolaceAir Products For Kelowna Homes (4 product names) | "AirRanger — Polarized Media Air Cleaner" / "BioForce Defender — UVC/UVV Germicidal System" / "AirSentinel — Bypass HEPA Filtration" / "EDGE — Activated Carbon Filtration" | "AirRanger: Polarized Media Air Cleaner" / "BioForce Defender: UVC/UVV Germicidal System" / "AirSentinel: Bypass HEPA Filtration" / "EDGE: Activated Carbon Filtration" |
| IAQ · AirSentinel item | "True HEPA filtration at 99.97% efficiency at 0.3 microns — equivalent to MERV 17 or higher." | "True HEPA filtration at 99.97% efficiency at 0.3 microns, equivalent to MERV 17 or higher." |
| **/financing-rebates/vision-elite-service-plan/** · intro | "…priority access to our most experienced technicians in the Okanagan—all year round." | "…priority access to our most experienced technicians in the Okanagan, all year round." |
| Elite plan · H2: The Okanagan's Preferred Home Maintenance Service Plan | "…priority scheduling for all plumbing, heating, and cooling needs—an essential advantage during the Okanagan's peak seasonal shifts." | "…priority scheduling for all plumbing, heating, and cooling needs. That's an essential advantage during the Okanagan's busiest seasons." |
| **/kelowna-boiler-services/** · H3: Are combi boilers really more energy-efficient? | "Because they only heat water on demand—rather than heating and storing a large tank of water—they virtually eliminate standby heat loss…" | "Because they only heat water on demand, rather than heating and storing a large tank of water, they virtually eliminate standby heat loss…" |
| **/residential/poly-b-plumbing-kelowna/** · H3: Poly B Plumbing Concerns & Regulatory Actions | "…began to spring leaks—often these were tiny, pinhole leaks…" | "…began to spring leaks. Often these were tiny pinhole leaks…" |
| Poly B · same section | "The oxidants in water supplies—and chemicals such as chlorine—react with the polybutylene pipes…" | "The oxidants in water supplies, and chemicals such as chlorine, react with the polybutylene pipes…" |
| Poly B · H2: How to Tell if You Have Poly B Plumbing | "The most common diameter is 1/2" or 3/4"—the same as most residential copper piping." | "The most common diameter is 1/2" or 3/4", the same as most residential copper piping." |
| **/trenchless-water-main-service/** · H2: Signs You May Need a Water Line Replacement | "…give us a call —we'll diagnose the issue quickly…" | "…give us a call. We'll diagnose the issue quickly…" |
| **/hot-water-heater-repair-vernon/** · H2: Vernon Hot Water Heater Installations | "Don't wait any longer— contact u s today…" | "Don't wait any longer. [Contact us](https://visionplumbingandheating.com/contact/) today…" (also fixes the "u s" typo) |
| **/residential/emergency-plumber-vernon-bc/** · H3: 24/7 Emergency Plumbing Services in Vernon, BC | "Don't let a plumbing emergency disrupt your life— contact us anytime…" | "Don't let a plumbing emergency disrupt your life. Contact us anytime…" |

**Blog posts:** 269 em dashes across 63 posts. These are older and lower priority, and they're mechanical fixes. The full list, with the surrounding text for each dash, is in [em-dash-blog-list-2026-10-14.md](em-dash-blog-list-2026-10-14.md). Start with the posts that get the most traffic: /quietest-air-conditioners-2026/ (2) and /is-high-efficiency-furnace-worth-it/ (1). After that, fix the posts with the most dashes.

---

## Priority 6: section structure and near-duplicates

| Page | Issue | Fix |
|---|---|---|
| /residential/heating-cooling/air-conditioning-maintenance-kelowna/ | The H2 "Serving Kelowna & Surrounding Okanagan Communities" (with a Call Us 24/7 button) appears **twice**: under the hero and again just before the FAQs. | Keep the first one. Retitle the second CTA band, for example "Book Your AC Tune-Up Before the Heat Hits", or remove it. |
| /residential/heating-cooling/air-conditioning-installation-kelowna/ | The page has an install process section (H2 "What Does an AC Installation Actually Look Like?") and also a timing answer in the FAQ. Neither duplicates the other. Only the heat pump timing conflicts (Priority 4). | No structural change needed. |
| /residential/heating-cooling/heat-pump-installation-kelowna/ | Restructured in the feedback. Mini-split content is now under H2 "Consider Getting A New Ductless Split or Mini Split Heat Pump", and Why Choose sits high on the page. | Done. Only the phone number and 2 em dashes remain (above). |
| Other 2026 rewrites (AC repair, furnace install/repair/maintenance, heat pump repair, emergency furnace, IAQ) | Checked for repeated topic sections and for Why Choose placement. Why Choose is the 3rd or 4th H2 on all of them, and no duplicate process or mini-split sections were found. | None. |

---

## Also found during the scan (not in the feedback, but against Vision's rules)

| Page | Issue | Suggested fix |
|---|---|---|
| [/trenchless-water-main-service/](https://visionplumbingandheating.com/trenchless-water-main-service/) · FAQ "Do you handle trenchless sewer line replacement too?" | The answer says "It is possible, but due to cost we often recommend alternative options…". Vision doesn't do trenchless sewer work (CLIENT.md, 2026-04-15 and 2026-08-18). | "No. Our trenchless work is for water lines only. For sewer line problems, we offer drain camera inspections and conventional sewer line repair. [Contact us](https://visionplumbingandheating.com/contact/) to discuss the best option for your property." |
| [/importance-of-hvac-maintenance/](https://visionplumbingandheating.com/importance-of-hvac-maintenance/) | Lists "Air Duct Cleaning: Prevent allergen circulation." as a maintenance item and "Regular filter and duct cleaning reduces indoor pollutants." Vision doesn't do duct cleaning. | Remove the "Air Duct Cleaning" item. Change the other line to "Regular filter changes reduce indoor pollutants." |
| [/here-comes-fall/](https://visionplumbingandheating.com/here-comes-fall/) | "Have your furnace or duct work cleaned if needed" | "Have your furnace cleaned and serviced if needed" |
| [/financing-rebates/vision-elite-service-plan/](https://visionplumbingandheating.com/financing-rebates/vision-elite-service-plan/) · FAQ on combining discounts | "But they are typically eligible for financing and More Rewards points!" Vision left More Rewards on 2026-07-07. | "But they are typically eligible for financing." |
| Furnace repair, furnace maintenance and emergency furnace pages | The banner "Get Up To $150 Off When We Service Your Gas Appliances / Claim Fortis Rebate" may refer to a FortisBC program that ended June 2025 (already flagged in CLIENT.md). The Why Choose copy also says "over 660 reviews", but the widget now shows 712. | Confirm with Vision whether the FortisBC rebate is still running. Update the review count, or say "over 700". |
| /ac-repair-kelowna/ · H2 | Typo: "Strata, Condo & Townhouse AC Repair in the Okangan" | "…in the Okanagan" |

More Rewards mentions on past promo posts (/5x-more-rewards-2026/, /40-years-of-vision/, /air-ease-buy-back-promo-2026/, /penticton-fall-homeshow-2025/) can stay, per CLIENT.md ("past-dated blogs can stay").
