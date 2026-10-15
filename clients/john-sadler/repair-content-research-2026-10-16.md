# John Sadler: AC and heat pump repair content research, 2026-10-16

> **Status:** Research, step 1 of the scrum task in [scrum-2026-10-15.md](scrum-2026-10-15.md) item 2. No site changes made yet.
> **Task:** Add repair wording, headings and schema to the AC and heat pump pages now that the client offers repairs (since 2026-08-20). Keep it to obvious edits; don't invent process details.
> **Sources:**
> - Live pages, read 2026-10-16 in a browser (curl gets a Cloudflare 403)
> - [john-sadler-tracked-keywords-2026-10-15-v2.xlsx](john-sadler-tracked-keywords-2026-10-15-v2.xlsx): Final Tracking List, GSC Queries (16 months), GBP Search Terms
> - Google Ads Keyword Planner, 2026-10-16, locations Surrey + Langley + White Rock combined, Oct 2025 to Sep 2026
> - [keywords.md](keywords.md) sections 2, 4 and 5
> **Not pulled:** Semrush phrase questions (PAA). The Semrush API reports no API units left on the account. The FAQ list below uses GSC question queries and the questions already on file instead.

## 1. What the live pages say now

Both pages actively tell visitors that Sadler does **not** repair. Each item below has to change. Adding a "we also do repairs" line without removing these would contradict itself on the same page.

### /services/heating-cooling/heat-pumps/
Title: "Heat Pump Installation in Surrey | Navien NAZ Specialist | John Sadler". Last modified 2026-08-19, one day before repairs were approved.

| Where | Problem |
|---|---|
| H1 | "Heat Pump Installation in Surrey — Navien NAZ Specialist". Installation only, and it has an em dash (brand rule). |
| Intro paragraph (under the first H2) | Says they install heat pumps only and focus exclusively on new installs |
| H2 "Why "installs only" matters for heat pumps" | The whole section argues for installs only and ends by referring repairs to another contractor |
| FAQ "Does John Sadler repair heat pumps?" | Answers no, and says they don't offer heat pump repair or maintenance |
| "Our Experience" block | Says "We work on all brands of heat pumps". This now fits, so keep it. |
| Schema | WebPage, Breadcrumb, WebSite and Organization only. No Service or FAQPage. |
| Em dashes | Many in the body copy (brand rule: no em dashes) |
| Licence | Shows "TSBC Licence #92486". The full number is LGA0092486. |

### /services/heating-cooling/air-conditioning/
Title: "AC Installation in Surrey, White Rock, Langley & Delta | John Sadler Plumbing & Heating"

| Where | Problem |
|---|---|
| H1 | "AC Installation in Surrey / $10K in Heat Pump Rebates Available". Installation only, and it carries a fixed rebate figure. |
| H2 "AC installation across Surrey and the Lower Mainland" | Says they install both types "and only both", focusing exclusively on new installs |
| H2 "Why "installs only" is the right call for AC" | Argues for installs only, contrasts with "a service tech squeezing it between repair calls", and refers repairs elsewhere |
| FAQ "Does John Sadler repair air conditioners?" | Answers no, and says they don't offer AC repair or AC maintenance |
| Two H1s | "Frequently Asked Questions" is also an H1 on both pages. It should be an H2. |
| Schema | Has LocalBusiness and Organization blocks, but no Service or FAQPage |

**Sitewide follow-up:** other pages, such as the heating and cooling hub, the furnace pages and blogs, may also say "installs only" for AC or heat pumps. This wasn't checked. It's CLIENT.md priority 4 ("sweep for pages covering services they don't offer"), run in reverse.

## 2. Keyword demand

Keyword Planner figures are average monthly searches for Surrey + Langley + White Rock combined. "GSC" is the site's own Search Console data over 16 months (from the v2 workbook).

### Heat pump repair (small but steady, peaks in winter and spring)

| Keyword | KP avg/mo | GSC impressions | GSC avg pos. | Note |
|---|---|---|---|---|
| heat pump repair | 30 | 2,406 | 15.1 | Peaks Jan, Apr–Jun (50/mo) |
| heat pump repair surrey | 10 (workbook: 30) | 2,726 | 4.9 | **Already ranks ~5 while the page says "no repairs"**. Easiest win. |
| heat pump repair near me | 10 | 1,259 | 13.8 | Dropped from tracking as a "near me" variant |
| heat pump service near me | 10 | 1,892 | 19.8 | Dropped from tracking |
| heat pump maintenance | 20 | n/a | n/a | Only if the client offers maintenance (see section 5) |
| heat pump service / service surrey | 10 / 10 | 93 ("servicing") | 13 | High CPC ($17–50), so buyer intent |
| heat pump repair langley | 10 | n/a | n/a | |
| heat pump not heating | 10 | n/a | n/a | Symptom term. Good as an FAQ or blog, not an H1. |
| mini split repair | 10 | n/a | n/a | They install mini-splits. Confirm they repair them. |
| heat pump repair white rock | 0 | n/a | n/a | Mention White Rock in body copy only |

### AC repair (bigger, but very seasonal)

| Keyword | KP avg/mo | GSC impressions | GSC avg pos. | Note |
|---|---|---|---|---|
| ac repair / air conditioner repair | 260 | n/a | n/a | Apr–Aug 320–590/mo, Nov–Feb 40–140/mo |
| ac repair near me | 110 | n/a | n/a | |
| air conditioning repair surrey (= ac repair surrey) | 40 (workbook: 110) | 3,038 / 1,705 | 30.7 / 53.5 | July–Aug 110/mo, Sep 20/mo. CPC $9–50. |
| ac repairs surrey | n/a | 2,014 | 27.1 | Workbook marked it "not a tracking term" |
| hvac repair | 40 | n/a | n/a | |
| hvac repair surrey | 10 (workbook: 20) | n/a | n/a | |
| ac repair langley / air conditioning repair langley | 10 | n/a | n/a | |
| ac maintenance / ac service | 40 / 50 | n/a | n/a | Only if they offer maintenance |
| ac not cooling | 10 | n/a | n/a | Symptom / FAQ |
| ac repair white rock | 0 | n/a | n/a | |

**Read:** Andrew's call holds up. AC repair search collapsed after August (480 to 90 in September for "ac repair"), so a dedicated AC repair page can wait until spring. Heat pump repair has year-round demand that climbs from December, and the page already ranks about #5 for "heat pump repair surrey" without saying they do it. That's the edit with the fastest payoff.

## 3. Keyword-to-page map (same-page edits now)

| Page | Primary (keep) | Add as repair secondary | Where it goes |
|---|---|---|---|
| /heat-pumps/ | heat pump installation surrey | heat pump repair surrey; heat pump repair; heat pump repair langley; heat pump service (only if offered) | H1, title, meta, a new H2 section, FAQ answer, Service schema |
| /air-conditioning/ | air conditioning installation surrey; air conditioner surrey | air conditioning repair surrey; ac repair surrey; ac repair langley; hvac repair surrey | H1 subline, title, meta, a new H2 section, FAQ answer, Service schema |

No cannibalization risk: no other page targets AC or heat pump repair. Furnace repair stays on /furnace-repair/; the AC page already links to it.

## 4. Proposed edits (draft for Andrew's review before anything goes live)

Every edit follows the brand rules: no em dashes, no "best" or "#1", "we/our" voice, 50 years, no fake urgency.

### Heat pump page
- **Title:** Heat Pump Installation & Repair in Surrey | John Sadler
- **Meta:** Heat pump installation and repair in Surrey, White Rock and Langley. Navien Service Specialist with 50 years in the Lower Mainland. Book a visit today.
- **H1:** Heat Pump Installation & Repair in Surrey
- **Intro:** replace the "installs only / exclusively new installs" sentence with: we install and repair heat pumps across Surrey, White Rock, Langley, Delta and Aldergrove.
- **Replace the "Why installs only matters" H2** with "Heat pump repair in Surrey and Langley". Keep the true part (install quality matters, sizing and refrigerant charge cause problems two winters later) and turn it into the repair angle: those same issues are what we diagnose and fix. Close with a call/book CTA. Don't list steps, response times or pricing.
- **FAQ "Does John Sadler repair heat pumps?":** change to yes. We repair heat pumps (including ducted and ductless/mini-split, if confirmed) as well as boilers, furnaces and hot water tanks. No links and no branded language in the FAQ answer (FAQ schema rule).
- **New FAQ:** Why is my heat pump not heating? Give a short, general answer (thermostat mode, filter, outdoor unit iced or blocked, defrost cycle) that ends with "call us if it persists". Keep it general so it doesn't need client facts.
- **Fix:** the FAQ heading should be an H2, not an H1. Remove em dashes. Show the licence as LGA0092486.

### AC page
- **Title:** AC Installation & Repair in Surrey, White Rock & Langley | John Sadler
- **Meta:** Central AC and ductless mini-split installation and repair across Surrey, White Rock, Langley, Delta and Aldergrove. Navien dual-fuel systems available.
- **H1:** AC Installation & Repair in Surrey. Consider dropping the "$10K in Heat Pump Rebates" subline: CLIENT.md already asks for the rebate button to come off, and a fixed dollar figure is a claim to check.
- **H2 "AC installation across Surrey...":** remove "and only both / exclusively new installs".
- **Replace the "Why installs only is the right call" H2** with "AC repair in Surrey and Langley". Keep the existing repair-or-replace sentence (an ageing unit needing regular repairs means it's worth a replacement assessment), because it already bridges repair and install.
- **FAQ "Does John Sadler repair air conditioners?":** change to yes.
- **Fix:** the FAQ heading should be an H2.

### Schema (both pages)
- Add a `Service` node on each page: `serviceType` "Heat pump installation" plus "Heat pump repair" (and the AC equivalents), with `provider` → the existing Organization @id and `areaServed` Surrey, White Rock, Langley, Delta, Aldergrove. No Abbotsford.
- Add `FAQPage` for the FAQ blocks, after the answers are updated. Answers carry no links and no branded language.
- How it's added depends on the site's schema plugin; check the existing LocalBusiness block on the AC page to see where it comes from.

## 5. Questions for the client (Andrew said he'd raise item 1 at his 2026-10-15 client meeting; check what came back)

These block anything beyond the "obvious" edits above:
1. The repair process and its steps (Andrew's item). This means no process section until we have it.
2. Do they **maintain / service** heat pumps and AC (tune-ups), or only repair? Both old FAQs say "no repair **or maintenance**". Only change the maintenance half if they confirm.
3. Ductless mini-split repair: yes or no?
4. Which brands do they repair? The "all brands" list is on the page now. Confirm it applies to repairs.
5. Service area for repairs: same as installs?
6. Any repair warranty, diagnostic fee or response-time claim? Don't publish any until confirmed. The same rule applies to the existing 24/7 conflict.

## 6. Separate repair pages (later)

- **Heat pump repair page:** worth drafting. Demand runs year-round, the page already ranks about #5 on a page that says "no", and this winter is the season for it. Draft it in Google Docs for client approval once the section 5 answers are in. It needs a URL decision, for example /services/heating-cooling/heat-pump-repair/.
- **AC repair page:** park until about March 2027. Demand climbs from March and peaks April to August. The same-page edit covers it until then.
- Both new pages need the client's content approval (Colin checks the facts, then Tina approves).

## 7. Next steps

- [ ] Andrew: review section 4 and approve or adjust the wording
- [ ] Francis: make the approved same-page edits. Note there's no wp MCP for johnsadler.ca in this setup, so edits happen in the WordPress admin.
- [ ] Francis: add the Service schema, and the FAQPage schema once the FAQ answers are updated
- [ ] Francis: sweep the rest of the site for "installs only / refer repairs" copy on AC or heat pumps
- [ ] Andrew: get the section 5 answers from the client
- [ ] Francis: draft the heat pump repair page in Google Docs once the answers are in
- [ ] Re-run the Semrush PAA pull (`phrase_questions`) once API units are topped up, and fold the results into the FAQs
