# Internal notes: 2026-06-navien-tankless-maintenance

Not client facing. Never paste into the Google Doc.

## Scope

**Scope (editor review only, remove before publishing):** Practical explainer on Navien tankless water heater maintenance: how often Navien says to service it, what a professional service visit involves step by step, what Surrey's water means for descaling, what owners can do between visits, how annual servicing differs for Navien combi boilers, boilers and the NPF hydro-furnace, and how maintenance ties to the Navien warranty. Every interval comes from Navien's own manuals or Navien's published guidance.
**Masterlist:** June 2026, Blog #1 (row 73)

## Image Note

All images must be real John Sadler photos, never AI-generated or stock.

---

## GBP Post

**Navien tankless water heater maintenance: once a year keeps it running right.** Navien recommends descaling your tankless water heater at least once a year, plus cleaning the air intake filter every 3 to 4 months. Our latest post walks through what a full service involves, from flushing the heat exchanger to checking the venting, and why soft Surrey water does not mean skipping it.

Q: How often should a Navien tankless be serviced? A: Navien recommends annual maintenance, including descaling at least once a year.

Q: What does error code E760 mean? A: It is Navien's flushing and service alarm, a reminder that routine service is due.

As a Navien Certified Service Specialist, we service Navien tankless water heaters, combi boilers and boilers across Surrey, White Rock and Langley. Book your annual service today.

CTA button: Learn more (link: blog URL)

## Facebook Post

Is your Navien tankless water heater due for its yearly service? Navien recommends descaling at least once a year, even with our soft Surrey water. Here's what a service visit actually involves, step by step: [blog URL] #NavienTankless #SurreyBC

## Instagram Post

Once a year, your Navien tankless needs a proper flush, a filter clean and a venting check. Our new guide breaks down what's involved and how often, straight from Navien's own manuals. Link in bio. #Navien #TanklessWaterHeater #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **Schema:** Article + FAQPage (FAQ answers already contain no links and no branded language).
- **Quick Answer:** put it in the WordPress Preformatted block.
- **Images:** real John Sadler photos only, never AI or stock. Only two confirmed real photos are on file (`clients/john-sadler/images/technician-working.jpeg`, `work-vans.jpeg`); ask Tina for a Navien service photo and an inlet filter close-up.
- **Links marked "link once published":** /blog/navien-boiler-error-codes/ and /blog/navien-furnace-error-codes/ are being written in parallel. Add the hyperlinks only when they are live; otherwise remove the two sentences.
- **Internal links (distinct):** /services/plumbing/tankless-water-heater-repair/, /combi-boiler/, /blog/annual-boiler-service/, /blog/furnace-service-frequency/, /blog/why-choose-navien/, /services/navien/, /contact-us/, plus the two error-code posts once live.
- **External links (4):** Navien descaling page, NPE-2 manual, NCB-H manual, Metro Vancouver 2025 water quality report. This is above the skill's 1 to 2 target because every interval is sourced; the editor can drop the NCB-H link if needed (the fact is still in the manual).
- **Publish timing:** the primary keyword peaks December to February and again in July (Keyword Planner). Publishing before December is ideal.
- **Cannibalization check (2026-10-23, WordPress REST post/page list):** no existing post covers Navien tankless flushing, descaling or inlet filters (zero mentions of "flush" or "descal" on any related page). Boiler and furnace servicing is already covered generically by /blog/annual-boiler-service/, /blog/regular-boiler-maintenance/, /blog/boiler-furnace-maintenance/ and /blog/furnace-service-frequency/, so this post keeps those sections short, Navien-specific, and links out rather than repeating them.
- **Removed or not claimed:** no maintenance plan, price, response time or 24/7 claim. No lifespan figure (no Navien source found). Warranty years left out of the blog (they differ by model and are in the hub page draft).

### Sources used for fact-check (for Colin)

| Fact | Source |
|---|---|
| Descale at least once a year; frequency rises with mineral content and set temperature; Navien recommends a professional | [Navien: How to descale tankless water heaters](https://www.navieninc.com/blog/notice/how-to-descale-tankless-water-heaters) |
| Annual maintenance recommended; hard water may need more frequent maintenance; failure to maintain may void warranty | [Navien: Tankless water heater maintenance](https://www.navieninc.com/blog/notice/tankless-water-heater-maintenance) |
| Verify operation, including gas pressure; o-ring on condensate trap; inlet screens on all tankless units | [Navien: Simple tips for maintaining your Navien unit](https://www.navieninc.com/blog/notice/simple-tips-for-maintaining-your-navien-unit) |
| Air intake filter every 3 to 4 months (E110); vent and intake inspected annually; drain first; flush 45 minutes; "somewhat complicated procedure"; A2 recirculation filter; E016/E030/E760; freeze damage not covered; warranty void for failure to maintain; hard water damage excluded; claims via original installer | [Navien NPE-2 User's Information Manual](https://www.navieninc.com/downloads/npe-2-user-s-information-manual-en/download), pages 5, 11 to 15, 17 to 19 |
| Combi boiler inspected annually at start of heating season by a qualified technician; annual start-up checklist; monthly owner checks | [Navien NCB-H User's Information Manual](https://www.navieninc.com/downloads/ncb-h-user-s-information-manual-en/download), pages 18 to 20 |
| NHB-H and NFB-H boilers inspected annually by a qualified technician | [NHB-H manual](https://www.navieninc.com/downloads/nhb-h-user-s-information-manual-en/download), [NFB-H manual](https://www.navieninc.com/downloads/nfb-h-user-s-information-manual-en/download) |
| NPF: monthly air filter; seasonal blower, combustion, intake, water level, venting checks; annual neutralizer pH test | [Navien NPF Installation & Operation Manual](https://www.navieninc.com/downloads/npf-installation-and-operation-manual-en/download), pages 42 and 130 |
| Treated water hardness 2025: Capilano 20.5, Seymour 20.2, Coquitlam 2.4 mg/L as CaCO3 | [Metro Vancouver 2025 Water Quality Annual Report, Vol. 1](https://metrovancouver.org/services/water/Documents/water-quality-annual-report-volume-1-2025.pdf), pages 37 to 39 |
| Gas smell: go outside, call 1-800-663-9911 (24 hours) or 911 | [FortisBC: Gas leaks and odours](https://www.fortisbc.com/safety-outages/energy-safety/natural-gas-safety/gas-leaks-and-odour) |

Note: the Navien manuals are hosted on navieninc.com and state the units are approved for the USA and Canada. Colin should confirm nothing differs for the Canadian versions.

### Research gaps

- Semrush API units were exhausted on 2026-10-23 (both `keyword_research` and `organic_research` returned "no_api_units"), so no live People Also Ask pull. Volumes are Google Ads Keyword Planner, Canada. FAQs are built from Keyword Planner question-form terms (how to flush navien tankless water heater 50, how long do navien tankless water heaters last 10, how often should a navien tankless water heater be serviced 0) and Navien's own topics. Re-check with Semrush `phrase_questions` (database "ca") once units are restored.
