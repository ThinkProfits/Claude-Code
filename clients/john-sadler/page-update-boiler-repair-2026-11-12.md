# John Sadler Plumbing & Heating: Boiler Repair & Maintenance page update

**Prepared and applied live:** 2026-11-12 by Francis Marc Uy (approved in chat).

**URL:** https://www.johnsadler.ca/services/heating-cooling/boiler-repair/ (WordPress page ID 4155; rollback point: revision 8388, 2025-12-16)

**Target keyword:** boiler repair (primary per keywords.md; now set as the Yoast focus keyphrase, which was empty)

**Search intent:** Commercial / local (a homeowner whose boiler needs repair or service)

**Scope:** Small edits within the existing sections. Layout and images unchanged. Rows not listed were kept as they are.

## Urgent fix

Why Choose item 6 had the pasted ChatGPT citation chip ("barrie", linking to barrieheatingcooling.ca). It was removed first. This was the last live page found with it.

| # | Section | Current Content | Replacement Content |
|---|---|---|---|
| 1 | **Item 6: Quality Workmanship Guaranteed** | …peace of mind [link chip "barrie" to barrieheatingcooling.ca]. | Chip deleted |
| 2 | **Item 6 text** | We stand behind our work 100%… highest standard… – end of story | We stand behind our work and won't consider the job done until you're happy. Every project is completed to code, and we back our repairs and installations with solid warranties for your peace of mind. If something isn't right, we'll make it right. |
| 3 | **Meta description** | Expert boiler repair and maintenance in Surrey and surrounding areas. Trust John Sadler Plumbing & Heating with over 40 years of quality service. Call us today! | Boiler repair and maintenance in Surrey, White Rock and Langley. Licensed technicians and gas fitters, family-owned for 50 years. Call (604) 531-4355. |
| 4 | **Yoast focus keyphrase** | (empty) | boiler repair |
| 5 | **Intro link "boiler replacement"** | https://www.johnsadler.ca/boiler-replacement/ (301 redirect) | https://www.johnsadler.ca/boiler-installs-replacement/ |
| 6 | **Experience paragraph** | …serving the Lower Mainland for over 40 years… | …serving the Lower Mainland for 50 years… |
| 7 | **"Our expert plumbers" paragraph** | Our expert plumbers offer the best repair services for your boiler… experts in all aspects of plumbing, gas fitting, boiler repairs, and boiler maintenance. | Our licensed technicians repair boilers of all makes and models. Locally owned and operated, John Sadler Plumbing & Heating has a team of skilled, experienced tradespeople who specialize in gas fitting, boiler repair and boiler maintenance. |
| 8 | **H2: Contact Us Today for Tankless Water Heater Repairs** (pasted onto the boiler page) | Tankless copy; unlinked 604.531.4355; "We'll have your system up and running in no time." | H2: Contact Us Today for Boiler Repairs<br><br>Don't let a malfunctioning boiler disrupt your day! Call John Sadler Plumbing & Heating at [(604) 531-4355](tel:+16045314355) or fill out our [online contact form](https://www.johnsadler.ca/contact-us/) to schedule your boiler repair. We'll diagnose the problem and explain your options before any work begins. |
| 9 | **Button (Contact section)** | Get a Free Quote Today! | Book Your Repair Today |
| 10 | **H2: Why Choose John Sadler Plumbing & Heating?** subline + items 1, 3, 4, 7 | Shared block | Same replacements as the hub page (item 7 bullet hidden with `list-style: none`) |
| 11 | **H4: GET STARTED** | …our plumbing services… If you have an emergency, please contact us immediately… | [Contact us today](https://www.johnsadler.ca/contact-us/) to learn more about our boiler repair services in Surrey, White Rock & Langley or schedule your appointment. Regardless of your problem, our experience can provide a quality solution. |
| 12 | **Button** | FREE ESTIMATE (tooltip "GIVE ME FREE QUOTE") | [BOOK SERVICE](https://www.johnsadler.ca/contact-us/) (tooltip "Book service") |
| 13 | **H2: Expert Boiler Repair for All Major Brands** | …We carry top industry brands, including: | …We service many boiler brands, including: |
| 14 | **Closing paragraph** | …provide the best products and services… | …provide the right products and services… |

## Implementation Notes

- **Verified live 2026-11-12:** no barrieheatingcooling.ca in the source, the only phone link is `tel:+16045314355`, no `/boiler-replacement/` links left, one H1, the new meta description is in the source, Kinsta cache cleared.
- **Colin to fix (factual error):** "As the central nervous system of your water heating system, your boiler is responsible for providing hot water to your taps. The boiler heats water in the storage tank…" describes a hot water tank, not a hydronic boiler.
- **Not changed, flagged:** the JSON-LD schema says "over 40 years" and claims a "Peace Arch News Readers Choice Award – Best Plumber (2020)", which isn't on record in CLIENT.md; Aldergrove in the intro and schema (client to confirm); the "HEATING & COOLING" eyebrow; the item 5 en dash.
