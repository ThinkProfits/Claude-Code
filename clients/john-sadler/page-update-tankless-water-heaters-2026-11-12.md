# John Sadler Plumbing & Heating: Tankless Water Heater Systems page update

**Prepared and applied live:** 2026-11-12 by Francis Marc Uy (approved in chat).

**URL:** https://www.johnsadler.ca/services/plumbing/tankless-water-heaters/ (WordPress page ID 4872; rollback point: revision 8396, 2026-01-26)

**Target keyword:** tankless water heater installation (primary per keywords.md; now set as the Yoast focus keyphrase, which was empty)

**Search intent:** Commercial / local (a homeowner choosing a tankless installer)

**Scope:** Small edits within the existing sections. Layout and images unchanged. Rows not listed were kept as they are.

## Urgent fix

Why Choose item 6 had the same pasted ChatGPT citation chip ("barrie", linking to barrieheatingcooling.ca) as the hub page. It was removed first.

| # | Section | Current Content | Replacement Content |
|---|---|---|---|
| 1 | **Item 6: Quality Workmanship Guaranteed** | …peace of mind [link chip "barrie" to barrieheatingcooling.ca]. | Chip deleted |
| 2 | **Item 6 text** | We stand behind our work 100%… completed to the highest standard… we'll make it right – end of story | We stand behind our work and won't consider the job done until you're happy. Every project is completed to code, and we back our repairs and installations with solid warranties for your peace of mind. If something isn't right, we'll make it right. |
| 3 | **Meta description** | We are tankless water heater specialists. Our experienced technicians provide tankless hot water heater installation & repair services in Surrey! | Tankless water heater installation, repair and maintenance in Surrey, White Rock and Langley. Navien Certified, family-owned for 50 years. |
| 4 | **Yoast focus keyphrase** | (empty) | tankless water heater installation |
| 5 | **H2: Customer Experience** (subline) | Serving White Rock, Surrey & Langley for over 40 years! | Serving White Rock, Surrey and Langley for 50 years. |
| 6 | **H2: Why Choose John Sadler Plumbing & Heating?** (subline) | For nearly 50 years, our family-owned company has been the trusted choice for homes and businesses across Surrey and the Lower Mainland. … | For 50 years, our family-owned company has served homes across Surrey and the Lower Mainland. … |
| 7 | **Items 1, 3, 4, 7** | Shared block | Same replacements as the hub page (item 7 bullet hidden with `list-style: none`) |
| 8 | **Call button (Benefits section)** | Call Us Today for a Free Estimate:(604) 531-4355 (link `tel:(604) 531-4355`) | Call Us Today: (604) 531-4355 (link `tel:+16045314355`) |
| 9 | **H4: GET STARTED** | Contact us today to learn more about our plumbing services in Surrey, White Rock & Langley… If you have an emergency, please contact us immediately as our certified technicians can help! | [Contact us today](https://www.johnsadler.ca/contact-us/) to learn more about our tankless water heater services in Surrey, White Rock & Langley or schedule your appointment. Regardless of your problem, our experience can provide a quality solution. |
| 10 | **Button** | FREE ESTIMATE (tooltip "GIVE ME FREE QUOTE") | [BOOK SERVICE](https://www.johnsadler.ca/contact-us/) (tooltip "Book service") |

## Implementation Notes

- **Verified live 2026-11-12:** no barrieheatingcooling.ca link in the page source, the only phone link is `tel:+16045314355`, one H1, the new meta description is in the source, Kinsta cache cleared.
- **Barrie chip on other pages:** the live HTML of /services/plumbing/tankless-water-heater-repair/ and /services/heating-cooling/boiler-repair/ still has it (1 each). Both are next in the queue. /boiler-installs-replacement/ and the homepage are clean.
- **Not changed, flagged:** the eyebrow label "HEATING & COOLING" on this plumbing page; the item 5 en dash. Schema has no prices or emergency claims.
- **Colin to confirm:** "around 20 years" lifespan; "unlimited hot water"; the Bosch, GE, NTI, Rinnai and Triangle Tube logos.
- **Cannibalization watch:** keywords.md maps the same tankless installation terms to /tankless-water-heater-surrey/ as well.
