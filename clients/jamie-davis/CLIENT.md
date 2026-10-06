# Jamie Davis Towing: client profile

> **Status:** DRAFT v0.1, 2026-10-06. Pending review by Francis.
> **Sources:** Slack (#jamiedavistowing C07TS2LMF9T, #gbp-post-approvals, Francis/Andrew DMs, Blog Masterlist run DMs), Drive (SEO+GEO contract April 2026, PPC change order April 2026, 3-Month SEO Roadmap, Keyword Tracking Research 2026, Wikidata & Wikipedia Questions, PPC Monthlies), Semrush (project metadata only), live site (curl, 2026-10-06), repo.
> **Not checked:** Gmail (connector broken), GSC (403, no agency permission on `sc-domain:jamiedavistowing.com`), BrightLocal (tool error), Semrush Position Tracking (campaign not found via API; see section 5).
> **Related files:** [memory/jamie-davis-towing-context.md](../../memory/jamie-davis-towing-context.md) (site structure, Sept 2026 schema audit, sign-off rule), [keywords.md](keywords.md), GBP handoffs in `gbp-handoffs/week-of-*/gbp-handoff__jamie_davis_hope__*`.
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Business**
- Towing, heavy recovery and transport company headquartered in **Hope, BC**. Best known from Discovery's **Highway Thru Hell** (first aired 2012), which follows Jamie Davis's heavy-recovery operation on BC mountain highways.
- Legal name: the contract says **Jamie Davis Towing & Storage Ltd.**; BBB and the site's 404 page say **Jamie Davis Motor Truck & Auto Ltd.** *Confirm which is current and whether they are the same entity* (Wiki intake doc, question A1).
- Owner: Jamie Davis. Inducted into the International Towing & Recovery Hall of Fame, Class of 2019 (inductee #334 per Andrew; *confirm number*).
- Website: https://www.jamiedavistowing.com
- Head office (per site): 63011 Flood Hope Rd, Hope, BC V0X 1L2. **The Wiki intake doc says this property was sold in 2024.** *Confirm the current Hope address before any NAP or schema work.*
- Golden office: 920 King Crescent, Golden, BC V0A 1H2 (acquired Columbia Towing, Golden; date *confirm*).
- Phones (live site, 2026-10-06):

| Location | Number |
|---|---|
| 24/7 emergencies (sitewide) | 1-877-869-8440 |
| Hope | 604-869-8440 |
| Chilliwack | 604-793-8440 |
| Langley | 604-546-2222 |
| Golden | 250-344-6690 |
| Calgary, AB | 403-475-3737 |

- Email: info@jamiedavistowing.com
- Hours: dispatch 24/7; office Mon–Fri 9:00–5:00 (contact page).
- Timezone: Pacific (Calgary is Mountain).

**Relationship**
- Website build + PPC since late 2024 (Web Services Retainer signed 2024; PPC start date 2024-11-01 per PPC Monthlies). New site launched ~2025-01-04.
- **SEO + GEO/AEO bundle signed April 2026.** Jamie Davis is ThinkProfits' **first AEO/GEO client**, so the AEO playbook is being built on this account (Andrew, 2026-05-01).

**Client contacts**
- **Sherry Davis:** primary contact, contract signer and approver. Business email on the contract: ar@jamiedavistowing.com.
- **Jamie Davis:** owner. Historically reluctant to be associated with the show on the site; Sherry approved adding Highway Thru Hell branding (2024-12-19).

**ThinkProfits team**
- Andrew Silbernagel: account manager and PPC lead. **Approves all heading/title/city-focus changes.**
- Francis Marc Uy: SEO + AEO lead
- Clarissa (Admin): admin, reports
- Shawn Moore: account setup (confirmed SEO + GEO set up, 2026-04-29)
- Past: Brittni Woodson (account lead during the 2024 build), Ian Yin (developer, 2024 build)

**Stack**
- WordPress 7.1.2, Elementor 4.2.2, child theme (created by Andrew 2025-01-04), Yoast SEO, Gravity Forms
- Hosting: Kinsta (staging was `jamiedavis.kinsta.cloud`)
- Tracking: GA4, Google Tag Manager, **CallRail** (location number pools)
- Domain registrar: GoDaddy (access was a launch blocker in Dec 2024)

## 2. Services: what they do and don't do

**What they do** (Success Track list quoted in the Wiki intake doc; *client asked to confirm each is still active*)
- Light-duty automotive towing (`/towing-services/`)
- Flatbed towing, including motorcycles, classic and AWD vehicles. **Fleet uses LCG carriers, not rollback/tilt-bed trucks** (Andrew, 2026-07-10)
- **Heavy-duty towing and 24/7 emergency recovery**: rotators, cranes, air-cushion recovery, heavy lift (up to 130 tons, *confirm equipment*)
- Commercial / semi / fleet towing
- Roadside assistance: boosts, lockouts, flat-tire changes, fuel delivery
- Long-haul and international (Canada / USA, cross-border) towing
- Railway wrecker / train derailment recovery
- Transport: tractor towing, tridem tilt trailer, tandem tilt deck
- **Official BCAA contractor** (bills BCAA directly)

**What they don't do**
- **Impound / vehicle storage lots.** Andrew cut the "My car got towed, how do I get it back?" topic because they don't run impound or storage (2026-07-10), even though "Storage" is in the legal name. *Confirm with client.*
- Vehicle repair (the old `AutoRepair` schema type was inaccurate, Sept 2026 audit)
- Mobile tire **repair** is not a listed service, although "mobile tire repair" converts in Ads (keyword sheet). *Confirm whether this means flat-tire changes only.*

**Regulatory / factual**
- BC towing rates: ICBC publishes a towing rate schedule; the cost blog uses the Dec 15, 2025 schedule and a 22% fuel surcharge effective 2026-01-01 (Andrew's edits, 2026-07-10). Re-verify rates before any republish.
- AEO/Wiki work must be factual and sourced: no "award-winning", "industry-leading" or "best" (Andrew's AEO SOP, 2026-05-01).

## 3. Target market and geography

**Who they serve:** stranded drivers on BC highways (especially the Coquihalla / Hwy 5, Hwy 1, Hwy 3, Fraser Canyon, Rogers Pass / Kicking Horse), commercial fleets and truckers, rail operators, BCAA members, and long-haul customers. Andrew's steer (2026-07-10): favour the higher-value commercial and highway audience over low-value passenger-car callers.

**Locations**

| Location | Role | Page | GBP |
|---|---|---|---|
| Hope, BC | HQ, core market | /hope-towing/ | Yes (`jamie_davis_hope` in GBP pipeline) |
| Golden, BC | Operating yard | /golden-towing-company/ | Yes (not in the GBP posting pipeline) |
| Chilliwack, BC | Service area; client says most calls now come from Chilliwack, not Hope (2025-03-27) | /chilliwack-towing/ | *confirm* |
| Langley, BC | Expansion market; Langley PPC campaign added April 2026 | /langley-tow-company/ | *confirm* |
| Surrey, BC | Service area | /towing-surrey-bc/ | No |
| Calgary, AB | **Small satellite only** | /24-7-towing-calgary/ | No |

**Rules**
- **Keyword volume, research and tracking are BC-wide** (client confirmed, Andrew 2026-05-30). Main service pages target BC; city pages and GBPs target their city.
- **Calgary only on the Calgary page.** Don't let Calgary creep into other titles (Andrew, 2026-07-04).
- Instagram bio lists only Hope, Langley and Golden; old Alberta yards (Lac La Biche, Edson, Fort McMurray) closed years ago. *Confirm the definitive operating list* (Wiki intake doc, contradiction #6).

## 4. Competitors

No Semrush competitor pull this session (campaign not reachable via API). Known names from Slack and Drive:
- **Highway Thru Hell co-stars** (also benefit from the show): Quiring Towing, Aggressive Auto Towing (owned by Jamie's brother, *confirm*), MSA Towing, Mission Towing, Reliable Towing (Chilliwack).
- **Hope Towing Ltd.** (Hope): reportedly a government-approved impound operator. Shares the "hope towing" search term.
- **Columbia Towing** (Revelstoke / Sicamous): legacy brand after the Golden acquisition.
- Roadmap Decision #1 notes Calgary local emergency towing is "unwinnable" without a Calgary GBP/depot (3-Month Roadmap, 2026-05).

**Action:** pull `tracking_competitors_organic` from the Semrush UI (Andrew loaded competitors into the project on 2026-07-04).

## 5. Current SEO status

**September 2026 monthly report** (automated review, posted 2026-09-07)
- Organic sessions +8.2% MoM, key events +14.5% MoM, both slightly down YoY.
- Position tracking: **visibility down 4.98 points to 15.27%**; 46 keywords down vs 38 up.
- GSC: MoM clicks up, but **average position 41.7% worse YoY**.
- GBP: Golden and Hope both got **0 new reviews**; Hope GBP interactions -20.5% YoY and website clicks -26.2% YoY.
- AI assistants: 33 sessions (0.7%); ChatGPT +383%, Gemini +300% MoM, **0 conversions**.
- The Aug 2026 (and July) report PDF couldn't be parsed by the review bot; Francis reviewed manually.

**GSC top queries** (from the "From GSC" tab of the Keyword Tracking Research sheet, pulled ~2026-07-03; live GSC is 403)

| Query | Clicks | Impressions | Avg pos. |
|---|---|---|---|
| hope towing | 100 | 5,553 | 4.5 |
| langley towing | 64 | 430 | 4.8 |
| railway wrecker | 45 | 250 | 2.6 |
| tow truck | 31 | 17,548 | 12.1 |
| chilliwack towing | 26 | 2,269 | 7.1 |
| golden towing | 26 | 665 | 5.4 |
| long haul towing | 22 | 1,820 | 8.8 |
| tow truck surrey | 12 | 10,788 | 10.2 |
| towing service | 7 | 12,611 | 21.3 |
| towing company | 7 | 11,579 | 29.7 |

High-impression head terms (tow truck, towing service, towing company, tow truck surrey) sit at positions 10–30 with CTRs under 0.2%.

**Site and technical** (live curl 2026-10-06 plus memory file)
- ~18 URLs. All core and city pages return 200. Titles/H1s match Andrew's 2026-07-04 corrections.
- **`/blog/` returns 404** and no blog posts appear in the sitemap. Every GBP drafting run since Sept 2026 has flagged this. None of the 2026 blogs appear to be live.
- `/contact/` (old Edmonton address) now 301s to `/contact-us/`. Roadmap task M1-T01 looks done.
- **`/llms.txt` returns the HTML homepage, not an llms.txt file**, even though AEO notes say llms.txt is handled. *Confirm.*
- **Schema:** the 2026-10-06 fetch shows only the Yoast graph (Organization/WebSite/WebPage/Breadcrumb), plus FAQPage on `/langley-tow-company/`. The hand-authored LocalBusiness/Service graph and the invalid `TowingService` type described in the Sept 2026 audit (memory file) **were not found**. Either they were removed or they load client-side. *Re-check before planning the schema fix*, because the memory file may be stale.
- Semrush project 30290458 now has **both `tracking` and `siteaudit` enabled** (2026-10-06). The memory file's "no Site Audit" note is out of date.

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-06).

**What's tracked:** Andrew finalised **175 tracked keywords** on 2026-07-04 (from Francis's 200-keyword list, cross-checked with Ads, GBP and GSC) and built the Semrush project the same day. Sheet: "Jamie Davis SEO Keyword Tracking Research | 2026", `FINAL LIST` tab. Categories include Chilliwack, Commercial & Semi Towing, Coquihalla & Highway Corridor and Emergency & 24-Hour.

**Semrush API status:** project 30290458 is reachable, but its Position Tracking campaign returned "campaign not found" and the `campaigns` report listed no targets. **No live positions were pulled this session.** Check the campaign in the Semrush UI.

**Flags**
- "reliable towing chilliwack" (210/mo) is in the final list. **Reliable Towing is a Chilliwack competitor** (and a Highway Thru Hell co-star). Review.
- "hope towing" is a top query but overlaps with the competitor brand Hope Towing Ltd. Fine to track; don't write copy that implies affiliation.
- Mobile tire repair / tire repair terms appear in the research tabs. Only track them if the service is confirmed.

## 6. Current marketing programme and scope

**SEO + GEO Bronze bundle** (contract, April 2026)
- Monthly: **$1,490 + GST** ($500 loyalty discount from $1,990).
- One-time setup: $1,680 + GST (50% loyalty discount from $3,360).
- Hours: **4 SEO + 4 GEO/AEO hours a month, plus 1 blog a month** (Andrew, 2026-05-01). Log SEO and AEO time separately in Teamwork (SEO tasklist 3743195, AEO tasklist 3743210).
- The contract's payment line says "commencing November 1, 2024", which looks carried over from the 2024 contract. *Confirm the SEO+GEO start date* (Shawn confirmed setup on 2026-04-29).

**Recurring work**
- **Blogs:** 1 a month. Client approves topics. Workflow: Francis drafts, Andrew edits, client approves.
- **GBP posts:** Mon/Thu through #gbp-post-approvals (`jamie_davis_hope`). Golden GBP isn't in the pipeline.
- **AEO / entity building:** Wikidata (company + Jamie) → Highway Thru Hell Wikipedia edits → standalone Wikipedia page only with 5–10 independent sources → `sameAs` links in schema. The client intake questionnaire was sent; a one-page short version was requested (2026-05-29) and an updated first batch sent 2026-06-06.
- **Reporting:** monthly PDF plus an automated Slack review around the 7th.
- **3-Month SEO Roadmap** (2026-05): Month 1 Foundation Reset (NAP, technical, Golden GBP, sitewide schema, no keyword-stuffed H2s), Month 2 Depth & Trust (de-templatise pages, fix cannibalisation, surface BCAA + Highway Thru Hell), Month 3 Golden service × location matrix plus a corridor page. Task status in the sheet: mostly "Not Started" *(confirm)*.

## 7. PPC overview

**Programme**
- Google Ads, managed by Andrew. Account owned through francis@thinkprofits.com's MCC access per memory *(confirm owner)*. **Performing well**, so landing pages are protected (see section 11).
- **Upgraded from PPC Silver ($699/mo) to PPC Gold ($999/mo + GST), adding a Langley campaign** (change order, April 2026). Ad spend is billed separately by Google; budget not found.

**September 2026 report**
- Spend -18% MoM, conversions +~30%, **cost per conversion CA$28.25 (-36.8%)**.
- **Phone calls, phone impressions and phone-through rate all show "No data"** and every campaign shows 0 calls. Phone is the main lead type, so **call-conversion tracking needs fixing** (High urgency).
- Clicks -12.5%, impressions -2% MoM.

**Tracking history** (Andrew, 2025-01-04)
- GTM events: tp-short-contact-form-submission, tp-map-click-golden, tp-map-click-hope, tp-tv-show-link-clicks.
- tel: links standardised to the `tel:1.877.869.8440` format. Locations share overlapping numbers, so call tracking depends on the link format.
- CallRail: Hope GBP and Hope/Golden Ad assets were set up. A full website number pool needed ~15 more numbers (~$45/month). *Confirm whether the pool was ever approved.*

**Top converting Ads search terms** (keyword sheet "From Ads" tab, mid-2026): tow truck near me (19 conv), hope towing (14), towing near me (10.5), golden tow truck (10), towing golden bc (8.7), mobile tire repair (8). See [keywords.md](keywords.md) section 3.

## 8. Content guidelines

**Approval flow**
- Francis drafts, Andrew edits, then the client approves. **Never publish without client sign-off.**
- The client is slow to approve. May/June 2026 blogs have been "With Client" since June. Andrew said on 2026-08-19 to keep writing July/August drafts while waiting.

**Brand and accuracy rules** (from Andrew's edits, 2026-07-10)
- No em dashes.
- Position Jamie Davis as the expert deciding on the caller's behalf. Don't frame damage as the caller's problem.
- Use **LCG carriers**, not "rollback", for their flatbeds.
- Dispatcher checklists include passengers, animals and hazardous materials.
- Sitewide phone in content: **1-877-869-8440** (not the Hope local number).
- No impound/storage topics. No ICBC-only framing; cover ICBC, BCAA and private-pay.
- **BCAA is a trust signal, not a main keyword.** Organic targets people without a roadside membership. BCAA works as a blog topic.
- **"Heavy duty" means emergency recovery** (cranes, rotators, cliff/ditch recoveries), not just "bigger vehicles".
- Dropdown menu labels stay short. No keyword padding or "you can rely on".
- AEO/Wiki copy: factual, sourced, no superlatives.

**Content plan (Blog Masterlist, Jamie Davis tab)**

| Month (2026) | Topic | Status (per 2026-09-25 run) |
|---|---|---|
| May | Flatbed vs. Regular Tow Truck | With Client since June |
| Jun | How Much Does a Tow Truck Cost in BC? | With Client since June |
| Jul | Motorcycle Towing | Drafted (docx), Needs PM Review |
| Aug | What to Do After a Breakdown on a BC Highway | Drafted (docx), Needs PM Review |
| Sep | Winter Tires & Chains (Oct 1 rule) | Drafted (docx), Needs PM Review |
| Oct | Car Stuck in Snow or a Snowbank | Not approved |
| Nov | The Coquihalla in Winter | Not approved |
| Dec | Wrecker Truck explainer | Not approved |
| Jan–Apr 2027 | tbd (proposed: BCAA vs calling direct, heavy-duty recovery, winch-out, tow arrival time) | Proposed 2026-09-25 |

**Photos:** the image library is thin. Two site photos (`roadside-services.jpg`, `IMG_0546-scaled.jpg`) have each been reused 4+ times in GBP posts. Ask the client for fresh fleet photos.

## 9. Key priorities and strategic notes

1. **Get the blog live.** `/blog/` 404s, so 8+ written blogs aren't reaching search, and the GBP pipeline has no source material.
2. **Fix Ads call tracking** (September report, High urgency).
3. **Keyword decline:** visibility down to 15.27% in September; audit the losing keywords.
4. **GBP reviews:** zero new reviews on both profiles in September. Check that review requests are running. Investigate Hope's YoY drop.
5. **AEO entity work:** waiting on the client's answers to the Wiki intake. Nothing can be published to Wikidata until contradictions are resolved (company name, founding date, locations, inductee number).
6. **Schema / NAP:** re-audit (the hand-authored graph may be gone), then implement one canonical `#business` entity per the memory file. Resolve the Hope address first.
7. **Heavy-duty page split** (emergency recovery vs large-vehicle/commercial): undecided, research first (Andrew, 2026-07-04).
8. **Calgary positioning** (Roadmap Decision #1): recommendation is to reframe it as a BC–Calgary corridor / heavy-duty / commercial page. No decision recorded. Any change needs Andrew's sign-off.

**Strategic read**
- The Highway Thru Hell authority is the differentiator; competitors on the show share it, though.
- Highway corridor terms (Coquihalla, Fraser Canyon, Rogers Pass) are low volume but uncontested and fit the AEO angle.
- AI-referred traffic is growing but not converting, so AEO pages need clear calls to dispatch.

## 10. Social profiles and other channels

- Instagram: @jamiedavistowingoffical (spelling as on the profile; *confirm*)
- YouTube: "Jamie Davis Towing Official" (*confirm URL*)
- TikTok: has a "full fleet" clip (per GBP research notes); handle *confirm*
- Facebook, LinkedIn, X: not confirmed (Wiki intake section K)
- IMDb (Jamie): nm5266867
- Highway Thru Hell: Wikidata Q5759935; Wikipedia "Highway_Thru_Hell"
- Site footer shows "As Seen On" Highway Thru Hell linking to CTV (added Dec 2024)

## 11. Working rules and tool IDs

**Approvals**
- **Any change to a `<title>`, H1, menu label or a page's city focus needs Andrew's sign-off first.** Core pages are live Google Ads landing pages and Ads is performing well (Andrew, 2026-05-29 and 2026-07-04). See the memory file.
- Content: client approves (via Andrew).
- GBP: 👍 in #gbp-post-approvals.
- Wikidata/Wikipedia: Andrew reviews before anything is pushed.

**Standing rules**
- BC-wide targeting; city pages for cities
- Calgary only on the Calgary page
- BCAA = trust signal, not a head keyword
- Heavy duty = emergency recovery
- No impound/storage content
- No em dashes
- No superlatives in AEO/Wiki content

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | **30290458** ("Jamie Davis Towing", `www.jamiedavistowing.com`). Tools enabled: tracking, siteaudit (2026-10-06). Position Tracking campaign not reachable via API. |
| GSC | `sc-domain:jamiedavistowing.com`. **The agency account currently gets 403** (memory says it was visible earlier). Re-check access. |
| Slack | #jamiedavistowing C07TS2LMF9T. GBP source of truth: #gbp-post-approvals. |
| GBP automation key | `jamie_davis_hope` (Golden not in pipeline) |
| Teamwork | Project tasklist 3743194; SEO 3743195; AEO 3743210 |
| Blog automation | Jamie Davis tab in the shared feed sheet `1pn-1J7PENZD3ZYIwn_s9qZAdfBK2yS9ZcqTJg8bGqU0` |
| Scheduled tasks | blog-masterlist-planning-run, blog-masterlist-draft-check, seo-report-roadmap |

**Drive**

| File | ID |
|---|---|
| SEO+GEO contract (April 2026) | `17FibtF_Lb4FCv_wKLRlXZUxXgsuXirUeO703jpnigS8` |
| PPC change order 2026 (Silver → Gold) | `1_ep1OmEE4TzWBY6etxJbQGldSR0EIlYGFzuc6SZtbRc` (signed PDF `15tIwDmuVDB4mILx0L5WiU_i6zbfrYTc_`) |
| Keyword Tracking Research 2026 | `1n18x9dm4a1Xs-tlc4hdJIPP3_l-gll9CHOrRlDcpzXw` |
| 3-Month SEO Roadmap | `1CwED_5ysmrtPg6Yf2S2LYBIEH9bU6ilFzGokaK4IPJo` |
| Wikidata & Wikipedia Questions | `1FqYPQ5Qas3iPkVZtzPsVa1uPobn44dBfqM95drXSdtA` |
| PPC Monthlies | `1zaGae1HhwIGe35YYUOq4KXLR5XZ-E8NgzwRyfCpAsJg` |
| BLOG Masterlist (shared) | `1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw` |
| Blog: Tow Truck Cost in BC | `1xWPQjNA2FdK4LUIJ6xyJBMg_F8mCTeYchiL551B_Oho` |
| PPC Onboarding Questionnaire 2024 (form) | `1hYgLCPhleWFIfQPJvEZhLqR-k7ydveIn0lyPVGecRXE` |

## 12. Open items

**Waiting on the client**
- [ ] Approve the May/June blogs (With Client since June) and the Jul–Dec topics.
- [ ] Answer the Wiki intake (short version first), especially the six contradictions.
- [ ] Confirm the current Hope address (the Flood Hope Rd property was reportedly sold in 2024).
- [ ] Confirm the operating locations list, legal entity name, and whether mobile tire repair / storage are offered.
- [ ] Send fresh fleet and yard photos.

**Live site fixes** (title/H1 changes need Andrew's sign-off)
- [ ] `/blog/` 404s. Publish the approved blogs and link the blog in navigation.
- [ ] `/llms.txt` serves the homepage HTML. Add a real llms.txt.
- [ ] Re-audit schema: the hand-authored LocalBusiness graph wasn't found on 2026-10-06. Rebuild around one `#business` entity with `department`s for satellite locations, and add Wikidata `sameAs` once live.
- [ ] Commercial page H1 "Fast, Reliable 24/7 Commercial Towing Solutions" doesn't match its title. Propose a fix to Andrew; don't ship it unapproved.

**Ops**
- [ ] Fix Google Ads call-conversion tracking (0 calls recorded, September report).
- [ ] Check GBP review-request workflows (0 new reviews in September on both profiles).
- [ ] Restore GSC access for the agency account (403 on 2026-10-06).
- [ ] Check the Semrush Position Tracking campaign in the UI (API: "campaign not found"). Update the memory file: Site Audit is now enabled.
- [ ] Decide on the Calgary positioning (Roadmap Decision #1) and the heavy-duty page split.
- [ ] Add the Golden GBP to the posting pipeline (Roadmap Month 1 "GBP for Golden").
- [ ] Review "reliable towing chilliwack" (competitor brand) in tracking.
- [ ] Fix the recurring report-PDF parse failure (Jul and Aug 2026).
- [ ] **Security:** none found. No credentials were exposed in the Slack, Drive or site sources read on 2026-10-06. Domain access in Dec 2024 went through a password manager (Elepass), not plain text.

**Note:** #jamiedavistowing has had no human messages since 2026-08-19. Recent activity is in #gbp-post-approvals and the automated planning DMs.

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked.
- GSC: 403, no live data. Figures above come from the July keyword sheet and the September report.
- Semrush: no live positions, competitors or visibility (campaign not reachable via API).
- BrightLocal: tool error, no review data.
- Google Ads budget/spend and current keyword lists not found.
- Roadmap task statuses and the 2024 PPC onboarding answers weren't fully readable.
- The client's Wiki intake answers weren't found.

**Conflicts**
- **Legal name:** "Jamie Davis Towing & Storage Ltd." (contract) vs "Jamie Davis Motor Truck & Auto Ltd." (BBB, site).
- **Storage:** "Storage" is in the legal name, but Andrew says they don't run impound or storage.
- **Hope address:** the site lists 63011 Flood Hope Rd as head office; the Wiki intake says the property sold in 2024.
- **Service areas:** the site lists Hope, Golden, Chilliwack, Langley, Surrey and Calgary; Instagram lists Hope, Langley and Golden; meta descriptions say "BC & Alberta".
- **Schema:** the memory file (2026-09-04) describes a hand-authored LocalBusiness graph; the 2026-10-06 fetch shows only Yoast.
- **Semrush tools:** the memory file says tracking only; the API now shows tracking + siteaudit.
- **GSC access:** the memory file lists jamiedavistowing.com among visible properties; it returned 403 today.
- **Founding date:** BBB says 2005-02-02; the 2024 onboarding form implies ~2002.
- **Phone in content:** blogs use 1-877-869-8440, while the Hope page/GBP use 604-869-8440. Both are valid; keep the toll-free number sitewide and local numbers on city pages.
