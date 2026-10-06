# MySaskFarm.com: client profile

> **Status:** DRAFT v0.1, 2026-10-07. Pending review by Francis.
> **Sources:** Slack (#mysaskfarm C0BGPH5JSKT, full history 2026-07-11 to 2026-10-06), Drive (Client Overview Document, updated 2026-07-10/21; 90-Day Roadmap, 2026-07-23; Master Keyword Research 2026; Keyword Tracker; keywords-for-approval sheet; SEO & AEO/GEO Setup checklist; About Us questionnaire), Semrush (project 30622784, domain overview CA), GSC (URL-prefix property, 90 days), live site (2026-10-07), repo.
> **Not checked:** Gmail (connector broken), BrightLocal (tool error on the one attempt), Semrush keyword-level organic report (API units ran out), Semrush Position Tracking (no campaign exposed through the API).
> **Related files:** [keywords.md](keywords.md), `Saskatchewan-Farmland-Prices-Blog-Draft.docx` (this folder).
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Business**
- Solo farmland realtor, **Grant Ostapowich**, operating as **MySaskFarm.com**.
- Legal name: **Grant Ostapowich Realty Prof Corp**.
- Brokerage: **Century 21 Fusion**. The brokerage must stay on the website (regulatory requirement, Client Overview).
- 17 years as a realtor, 30+ years farming (47 years combined). Licensed province-wide (live homepage).
- Based in Warman, SK (about 10 km north of Saskatoon) per the Client Overview. The live footer shows **210-310 Wellman Lane, Saskatoon, SK S7T 0J1** (likely the brokerage office; *confirm which address is the NAP of record*).
- Phone: 306-227-1167. Email: mysaskhome@gmail.com.
- Website: https://mysaskfarm.com
- Timezone: Central Standard (Saskatchewan, no DST).

**Revenue context** (Client Overview, July 2026)
- 2025: $500,000 (prior 3-year average ~$275,000). 2026 to date (July): $246,000. Goal: $500,000+.
- Ideal mix: land sales 90%, appraisals 5%, residential 5%.

**Relationship**
- Estimate e-signed **2026-07-02**. Slack channel opened 2026-07-11.

**Client contact**
- **Grant Ostapowich:** owner and **sole approver**. Prefers Slack (fastest), text/call for quick items, email for detailed lists. Slack invite was planned (free plan only); *confirm he joined*.
- "Tommy" at the C21 Fusion marketing team (fusion.marketing@c21.ca) handled access handoff in July 2026. Not a day-to-day contact.

**ThinkProfits team**
- Andrew Silbernagel: lead/manager, client comms, publishing
- Francis Marc Uy: SEO lead (keywords, blogs, strategy)
- Shawn Moore, Clarissa (admin): in the channel

**Stack** (live site, 2026-10-07)
- WordPress 7.1.2 + Elementor 3.35.7
- SEO plugin: **All in One SEO (AIOSEO) 4.9.5.1**
- Listings: MLS / realtor.ca feed powering RM pages (*plugin name not confirmed*)
- Hosting: unknown host, DNS in "BlackSun" (Slack 2026-07-22). Host confirmed monthly server-level backups; Andrew asked about daily/weekly (2026-08-27).
- Domain registrar: GoDaddy (2FA tied to Grant; TP design@ account is a delegate).
- Credentials are stored in **Elepass** (team password manager). Never copy them into this repo.

## 2. Services: what they do and don't do

**What they do**
- **Farmland sales** (primary): buying and selling Saskatchewan farmland. Land types Grant wants: cropland, pasture, hunting land, irrigated land, ranches.
- **Land appraisals:** about 2% of revenue today, 5% target.
- Residential: **repeat clients only.** Grant would refer it out entirely if farmland volume allowed.

**What they don't do (never target)**
- Residential real estate, homes for sale, condos
- Urban real estate and urban lots
- Commercial property
- **Acreages:** excluded in the 90-Day Roadmap even though Shepherd's acreage cluster is easy volume. Flag only as a future scope conversation.
- Out-of-province land (e.g. Manitoba)

**Regulatory: real-estate advertising**
- Grant is a licensed salesperson under a brokerage, so the **brokerage name must appear in his advertising**, including the website. The Client Overview says C21 Fusion "must remain on website per regulatory requirement".
- Saskatchewan's regulator is the **Saskatchewan Real Estate Commission (SREC)**. *Confirm the exact SREC bylaw wording* (brokerage name prominence, team/trade-name rules) before the rebrand that demotes C21 to "regulatory minimum".
- **Live-site check, 2026-10-07:** the only brokerage reference found is the footer line "©C21 Fusion. 2026 All Rights Reserved". "Century 21 Fusion" is not written out and is not identified as the brokerage. **This may not satisfy the disclosure rule. Flag to Andrew/Grant before any further branding changes.**
- Don't promise sale prices, valuations or timelines. Blog content that touches tax (capital gains) or investment needs a "not tax/financial advice" line (already in the published farmland-prices post's FAQ).
- "Free valuation" CTAs: keep them distinct from formal **appraisals** (a paid service). *Confirm with Grant how he wants each described.*

## 3. Target market and geography

**Who they serve:** rural Saskatchewan landowners aged 55–65+, at or near retirement, thinking about selling. Skews male, land-rich. Grant believes they're more tech-savvy than peers (precision ag) and may use voice search (*confirm with our own research*). Buyers are expansion-minded producers and investors.

**Scope:** the whole province. Grant won't turn down any listing.

**Priority zone:** RMs **north of Highway 1** (better moisture, more activity). Southern RMs are lower priority but still targetable.

**Priority RMs** (Grant's questionnaire, 46 RMs)
- 399–406; 369, 371–373, 376, 377; 339–347; 310, 312, 314–317; 279–287; 429–431, 463; 434–437

**Wave 1 (Keyword Tracker, Saskatoon/Warman ring):** 401 Hoodoo, 402 Fish Creek, 403 Rosthern, 404 Laird, 371 Bayne, 372 Grant, 373 Aberdeen, 342 Colonsay, 343 Blucher, 344 Corman Park, 345 Vanscoy, 314 Dundurn.
- The 90-Day Roadmap orders Wave 1 differently (401, 402, 403, 400, 399, 404, 405, 406, 344, 371, 373, 342). **Use the Keyword Tracker order** (newer, and it moves 399 Lake Lenore to Wave 2). *Confirm with Andrew.*

**RM pages that exist** (sitemap, 2026-10-07): 8 `/rm-of-*/` pages, including Corman Park, Aberdeen, Tisdale, Biggar, Kindersley, Arlington. The Client Overview says "~400 RM-based landing pages". **Conflict: see section 13.**

**Seasonality**
- **Peak: November–March** (listings, buyers, deals). Bump publishing and outreach Oct–Feb.
- Photography window: July–August.
- **Slow: June (seeding) and September (harvest).** Expect slow replies.

## 4. Competitors

**From the brief and Semrush CA, 2026-07-23** (90-Day Roadmap)

| Domain | Organic KWs | Est. traffic/mo | Top-3 | Notes |
|---|---|---|---|---|
| hammondrealty.ca | 440 | ~4,480 | 74 | Top competitor. One /listings page ranks #1 for buyer heads (~66% of traffic) + brand (~29%). Works exclusively with Open Sale. |
| sheppardrealty.ca | 1,294 | ~2,690 | 45 | Family firm. Big acreage cluster (excluded for us). Brief spells it "Shepherd". |
| cawkwellgroup.com | 227 | ~220 | 4 | Grant's realistic solo benchmark. Brief spells it "Cockwell". |
| teamserca.com | 35 | ~150 | 2 | Research only. |
| farmboyrealty.com | 31 | ~0 | 0 | Research only. |
| **mysaskfarm.com** | 32 | ~6 | 0 | Baseline. |

**Primary tracking competitors:** Hammond, Sheppard, Cawkwell (Client Overview).

**Surfaced in research, not in the brief** (Roadmap, 2026-07-23): kentbraaten.com (monthly SK farmland market report, a direct AEO competitor for price/value content), Boyes Group / Murdoch Farm Team, Klarenbach Land & Livestock (widely cited 100-year land-value analysis), sask-farms-for-sale.com. *Not confirmed as added to tracking.*

**Content rule:** never recommend or link to competing realtors in client content.

## 5. Current SEO status

**Semrush domain overview, CA database (pulled 2026-10-07)**
- 30 organic keywords; 0 in top 3, 2 in 4–10, 10 in 11–20
- ~3 organic visits/month (estimate)
- 12 keywords trigger AI Overviews; 17 trigger People Also Ask
- Baseline (2026-07-23): 32 keywords, ~6 visits, 0 top-3. Flat, which is expected for a foundation phase.

**GSC, URL-prefix property `https://mysaskfarm.com/`, 2026-07-09 to 2026-10-07 (90 days)**
- **~14 clicks, ~1,810 impressions** across 16 pages
- Top pages:

| Page | Clicks | Impressions | Avg position |
|---|---|---|---|
| /rm-of-corman-park/ | 2 | 985 | 10.4 |
| / | 7 | 388 | 41.3 |
| /rm-of-aberdeen/ | 1 | 125 | 10.0 |
| /rm-of-kindersley/ | 0 | 91 | 13.2 |
| /listings/ | 4 | 44 | 34.5 |
| /rm-of-tisdale/ | 0 | 37 | 12.6 |
| /mortgage-calculator/ | 0 | 29 | 8.7 |
| /sell/ | 0 | 26 | 3.5 |

- **Corman Park is the only RM with real search demand right now:** "corman park sk" (145 impressions, pos 9.6), "corman park, sk" (57), "corman park rm" (40, pos 8), "corman park saskatchewan" (32). These are mostly navigational/geographic, not buyer intent, but they show RM pages can rank page 1.
- "my farm" (238 impressions, pos 49): brand-name noise, not a target.
- Money terms barely show yet: "sask farms for sale" (8 impressions, pos 44.5), "farmland for sale rm of tisdale" (12, pos 17.2), "sell my farm" (1, pos 45).
- The two new blogs (published around 2026-10-01 to 10-06) have no GSC data yet.
- `sc-domain:mysaskfarm.com` returns 403; only the URL-prefix property is accessible. GSC didn't exist at onboarding (Slack 2026-07-22), so data starts around July 2026.

**On-site status (live, 2026-10-07)**
- Homepage title "Farmland for Sale in Saskatchewan | MySaskFarm", H1 "Farmland for Sale in Saskatchewan". Already matches the master sheet's primary keyword.
- Schema present: Organization, WebSite, WebPage, BreadcrumbList, FAQPage. **No RealEstateAgent / Person schema for Grant yet** (Roadmap Month 2 item).
- Homepage FAQ includes **"Who is the best farmland realtor in Saskatchewan?"**: a superlative. The answer is generic ("the best farmland realtor for you is one who…"), but review it against the no-superlatives rule and SREC advertising rules.
- **No /about/ page.** The master sheet maps "farmland realtor saskatchewan" to a new /about/; the About Us questionnaire was sent 2026-08-18 (*answers not found*).
- **No appraisal page.** Planned: /farmland-appraisal-saskatchewan/.
- /listings/ is thin (~130 words outside the feed).
- Leftover residential-flavoured pages: /mortgage-calculator/, /mortgage-preapproval/ (*confirm whether to keep; farm mortgages are in scope, home pre-approval is not*).
- Older posts: "Feeling the weight of selling your farmland…" and "The Grass Ceiling: Why Pastureland Remains the Rancher's Stronghold".

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-07).

- **Semrush Position Tracking (project 30622784) exposes no campaign through the API** ("targets: null"; campaign lookup "not found"). Either tracking was never set up or it isn't visible to the API. **Check the Semrush UI.**
- **Approval list:** "MySaskFarm.com keywords for approval | 2026" holds **73 keywords** (2026-08-15/17). Andrew chased Grant for keyword sign-off again on 2026-08-27. **No approval found in Slack.** *Confirm status.*
- **Master Keyword Research 2026** (FINAL LIST, 244 rows, last edited 2026-09-10) maps keywords to pages with H1s and meta titles.
- Rules in brief: farmland only; no residential/urban/condo/commercial/acreage; RM terms in both name and number forms; low-volume RM terms kept for local, voice and AEO.

## 6. Current marketing programme and scope

**ThinkProfits package:** **SEO Bronze ($995/month) + AEO/GEO Bronze ($995/month)**, about $1,990/month total. Grant's comfortable ceiling is ~$2,000/month; $2,500–$3,000 is not (Client Overview).

**Recurring work**
- **Blogs:** 1 per month on Bronze (Client Overview). Andrew asked for September **and** October blogs on 2026-10-06, so expect catch-up. Topics run on a 6-month rolling roadmap that Grant approves.
- **Blog format:** duplicate and edit the two published posts (Andrew, 2026-10-06). Images: Grant's photos in the Drive Client Assets folder, resized to **1920 × 800 px** in the Canva project "MySaskFarm.com Blog Images (1920 x 800 px)".
- **On-page / RM work:** Wave 1 RMs in blocks; Bronze can't cover all RM pages (Grant knows this).
- **AEO/GEO:** entity work for Grant (not C21), FAQ/PAA content, quotable data blocks, RM land-value content.
- **Reporting:** monthly. *Confirm format and date.*

**Published so far** (Slack 2026-10-06)
- /saskatchewan-farmland-prices/ (title "Saskatchewan Farmland Prices: Still Climbing? | MySaskFarm")
- /best-time-sell-farmland-saskatchewan/ (dated 2026-10-01 on the page)
- Both drafted by Francis 2026-09-12; Grant "really liked" them and added a couple of edits.
- Repo copy: `Saskatchewan-Farmland-Prices-Blog-Draft.docx` (pre-edit draft; target keyword "saskatchewan farmland prices", 40/mo, mixed informational/commercial intent).

**Existing marketing outside TP:** newspaper ads; automated RM-based listing emails to a large contact list (tool unknown); trade-show booths at Agribition (Regina), Crop Production Show (Saskatoon) and Ag in Motion.

**Project tracking:** Teamwork project linked in the Slack channel bookmarks (*ID not captured*).

## 7. PPC overview

- **No PPC in scope.** Budget is fully committed to SEO + AEO (90-Day Roadmap, 2026-07-23).
- No Google Ads account details found. If PPC is ever pitched, present spend as a range with assumptions and keep Grant's ~$2,000/month total ceiling in mind.

## 8. Content guidelines

**Approval flow**
- **New or majorly revised content** (blogs, new pages): send the draft to Grant first. He wants to add his own voice and expertise.
- **Minor keyword-level rewording** of existing copy: no approval needed; TP proceeds.
- Andrew publishes after approval (current pattern).

**Voice**
- "Professional, informative, and fun" (Grant's words).
- First-person Grant / "we" is fine; lead with **30 years farming + 17 years selling farmland**. Content should read like a farmer talking to farmers, not generic real-estate copy.
- Canadian spelling. Saskatchewan terms: RM (rural municipality), quarter section, soil zone, SAMA assessment.

**Hard rules**
- Farmland only. No residential, urban, condo, commercial or acreage angles.
- **Grant and MySaskFarm.com are the primary entity.** C21 Fusion appears at the regulatory minimum only, but it **must** appear (section 2).
- No ranking, price or sale guarantees. Market forecasts get sourced and hedged (e.g. FCC Farmland Values Report, cited by year).
- No "best" / "#1" claims in copy (tracking such keywords is fine).
- Tax, estate and investment topics carry a "not tax/financial advice; talk to your accountant" line.
- Never recommend or link to competing realtors.
- Cite sources for all land-value statistics (FCC, SAMA, Western Producer, etc.).

**Images**
- Use Grant's Drive photos (Client Assets) or licensed stock.
- **Photos of farm equipment on private property need permission**, even without faces or plates. Default to stock or confirmed-owned images.
- Some Client Assets files look like stock with foreign captions ("Alberta, Canada" combines; "Swedish countryside" canola). Don't caption them as Saskatchewan.

**Priority content topics** (Grant's top client FAQs)
1. Are land prices still going up? (**done**: /saskatchewan-farmland-prices/)
2. How much is land worth in my area / my RM?
3. Is there any land for sale in my area?
4. How much did [neighbouring parcel] sell for?
5. What do we need to offer to buy that land?

## 9. Key priorities and strategic notes

**90-Day Roadmap (Aug–Oct 2026)**
- **Month 1 (Aug), foundation:** fix the broken RM search; GA4/GTM + conversion tracking; rebrand hierarchy (Grant primary, C21 minimum); backlink/plugin audit; keyword sign-off; 6-month blog roadmap; flagship land-values blog.
- **Month 2 (Sept), money pages:** "Sell Your Farmland in Saskatchewan" seller page; "Hire a Farmland Realtor" (Grant) service page; blog on capital gains on inherited farmland; homepage video optimisation; RealEstateAgent/FAQ/Article schema.
- **Month 3 (Oct), scale + AEO:** buyer pillar by land type (crop/pasture/hunting/irrigated); "How much is farmland worth in my RM?" blog and RM value data blocks (the Hammond gap); Wave 1 RM content, block 1.

**Where things actually stand (2026-10-07)**
- Blogs: 2 published (land prices, best time to sell). The capital-gains blog isn't published yet.
- /sell/ exists (title "Sell Farmland in Saskatchewan | Free Evaluation"). *Confirm whether it's been rewritten as the seller money page.*
- No /about/ (Grant service page) yet; questionnaire sent 2026-08-18.
- RM search fix, GA4/GTM, video optimisation, rebrand: **status not confirmed in Slack.**
- On-site edits were on hold until backups were sorted (Andrew, 2026-07-22). Monthly server backups confirmed 2026-08-27.

**Strategic read**
- Hammond wins with one listings hub + brand, not a content library. Grant's edge is the **RM structure + farming credibility**, so RM land-value content and seller-intent pages are the fastest path.
- Corman Park already earns page-1 impressions. Make it the model RM page and replicate it.
- We're heading into the Nov–Mar peak. Seller and value content needs to be indexed **now**.
- **Entity risk:** AI engines may credit C21 Fusion, not Grant. Person/RealEstateAgent schema, an About page and consistent NAP are AEO priorities.
- Set expectations honestly: Months 1–3 are foundation; payoff compounds through the winter season. No guarantees.

## 10. Social profiles and other channels

- Facebook: facebook.com/profile.php?id=100091515696350 (C21-branded; access unknown)
- Instagram: @saskatoon_realtor (C21-branded; Grant has access)
- X/Twitter is linked in the site footer (*handle not captured*).
- **TP doesn't manage social.** Andrew suggested Grant create MySaskFarm-branded profiles for NAP consistency (2026-07-22).
- **GBP:** an existing profile uses **C21 branding, is a sub-profile on the C21 listing, and has bad reviews**; nobody knows who has access. Andrew proposed creating a new MySaskFarm-specific GBP (2026-07-22). *Outcome not found.* Check SREC/brokerage rules before creating it.

## 11. Working rules and tool IDs

**Approvals**
- Grant approves all new and major content. Minor keyword edits don't need approval.
- Andrew publishes; Francis writes.

**Standing rules**
- Farmland only (no residential/urban/condo/commercial/acreage)
- Brokerage name must stay on the site
- Grant is the primary entity, not C21
- No guarantees, no superlatives
- Preserve the RM-search functionality and the homepage video (optimise, don't remove)
- Back up before on-site edits

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | Project **30622784**. No Position Tracking campaign visible via API (2026-10-07). |
| GSC | `https://mysaskfarm.com/` (URL-prefix, works). `sc-domain:mysaskfarm.com` = 403. |
| Slack | #mysaskfarm **C0BGPH5JSKT** |
| GA4 / GTM | *Not confirmed* (existed per contact; TP access pending as of 2026-07-22) |
| Passwords | Elepass (never in repo) |

**Drive**

| File | ID |
|---|---|
| Client folder "Mysaskfarm" | `1fqkekIxA-3mEt7V1o6Y_yKfqPa22st_S` |
| Client Assets (photos) | `13fwk53i1AOpj6zWqpKaQcezGq5XBceBH` |
| SEO & AEO 2026 folder | `15DkkTKVrnB5vNhbBbOGi3Tcn_d6jgG9i` |
| Blogs folder | `1b7yveD-heNkCwIHVqh1oVnm0epAQrRk-` |
| Client Overview Document | `1AOYKril_Q5suww-AHUW3Y8p638M2Azi2oqqQitXfnYA` |
| Onboarding questionnaire (Form) | `1T2gc16qtKCqmFuoFBP2etTd0HRZWoXsKfGw7N7cuPj4` |
| 90-Day Roadmap | `10wV0T5_r-SbxSRQ1GJv0Cq2qqpIfUK1eWtzKLg2k7rA` |
| Master Keyword Research 2026 | `1GNRXa9jvbJOWZ3MTPBJy6ficT4UbnI8Z4DZbQOfhU30` |
| Keyword Tracker (Francis, Slack 2026-07-31) | `1cxQz5KFeRoztOJEq9ix8__JRVu5lbWW_m8P0Fhgm2_A` |
| Keywords for approval (73 kw) | `1qr8epymVB4CgT3du4W3vfoqPBWHI7NZhTeBbqtoAtm8` |
| Initial Keyword Research | `1DEPiwS_eVywyyxogiFWqmcN3ccVQubw6BoTRXbQQPaE` |
| SEO & AEO/GEO Setup checklist | `1oiF1MvE9LWEX1gxdY0Yms-H-Y3gB6cDTdleAUiOJpow` |
| About Us questionnaire | `1cmvIJl4E5gJVFG9PtmImThmiXn0ifaJX` |
| Blog doc: Farmland Prices | `1QkdLQNro1IYdc1eSLbsBaCkCg8npwB4fYlyPTtyHmW8` |
| Blog doc: Best Time to Sell | `144GwJpIjMCTttTP552SDz6dUCgE011Fodl5e-fX9QJ4` |

## 12. Open items

**Waiting on the client**
- [ ] Keyword list sign-off (73-keyword approval sheet; chased 2026-08-27).
- [ ] 6-month blog roadmap approval. *Confirm whether sent.*
- [ ] About Us questionnaire answers (sent 2026-08-18).
- [ ] Hi-res MySaskFarm.com logo (reminded at least twice).
- [ ] phpMyAdmin / cPanel invite from the old team (Slack 2026-08-27).
- [ ] GA4 access; who controls Facebook; who owns the existing C21 GBP.
- [ ] Which address is the NAP of record (Warman vs 210-310 Wellman Lane, Saskatoon)?
- [ ] What tool sends the RM listing emails?

**Compliance**
- [ ] **Brokerage disclosure:** footer only says "©C21 Fusion". Confirm SREC requirements and show "Century 21 Fusion" clearly as the brokerage before demoting C21 further.
- [ ] Review the homepage FAQ "Who is the best farmland realtor in Saskatchewan?" (superlative).
- [ ] Decide on a new MySaskFarm GBP vs the C21 sub-profile (check brokerage rules first).

**Content and site**
- [ ] Write the September/October catch-up blogs (Andrew, 2026-10-06). Candidates: capital gains on inherited farmland; "How much is farmland worth in my RM?"
- [ ] Build /about/ (Grant, "farmland realtor saskatchewan") with RealEstateAgent/Person schema.
- [ ] Build /farmland-appraisal-saskatchewan/.
- [ ] Rewrite Wave 1 RM pages (templates ~85–95% duplicated per the tracker); start with Corman Park and Aberdeen.
- [ ] Confirm status of: RM search fix, GA4/GTM conversion tracking, homepage video optimisation, rebrand.
- [ ] Decide on /mortgage-calculator/ and /mortgage-preapproval/.

**Ops**
- [ ] Set up (or confirm) the Semrush Position Tracking campaign in project 30622784 with the approved list.
- [ ] Get `sc-domain:mysaskfarm.com` access, or keep using the URL-prefix property.
- [ ] Add kentbraaten.com, Klarenbach, Boyes/Murdoch, sask-farms-for-sale.com to competitor tracking.
- [ ] Ask about daily/weekly backups (asked 2026-08-27; no answer found).

**Security:** no exposed credentials were found in Slack or the Drive files read. Logins are referenced as stored in Elepass. Keep it that way.

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked (connector broken).
- BrightLocal: one attempt, tool error. No review/citation data.
- Semrush: no Position Tracking data (no campaign via API); keyword-level organic report failed (API units balance zero).
- GSC: domain property 403; URL-prefix data only from ~July 2026.
- Onboarding questionnaire (Google Form) responses not read.
- Teamwork project ID, monthly report format, and GA4/GTM status not found.
- Slack has no message between 2026-09-12 and 2026-10-06 about the technical items (search, video, tracking, rebrand).

**Conflicts**
- **RM page count:** Client Overview says ~400 RM landing pages; the live sitemap lists **8** `/rm-of-*/` pages. The rest may be generated by the MLS plugin and not in the sitemap, or may not exist. *Confirm before planning Wave 1 "create" vs "rewrite".*
- **Address:** Warman (Client Overview) vs Saskatoon Wellman Lane (live footer).
- **Wave 1 RM list:** Roadmap and Keyword Tracker differ (section 3).
- **Blog cadence:** Bronze = 1/month (Client Overview), but Andrew asked for September and October posts in one week (2026-10-06); likely catch-up, not a scope change. *Confirm.*
- **Competitor names:** brief spells "Shepherd" / "Cockwell"; the domains are sheppardrealty.ca / cawkwellgroup.com.
- **Blog URL:** the Initial Blog Topics tab planned `/blog/saskatchewan-farmland-prices-guide/`; it went live at `/saskatchewan-farmland-prices/`. Use the live URL.
- **Primary keyword volume:** "saskatchewan farmland prices" is 50/mo in the Roadmap (July), 40/mo in the draft and tracker (Sept). Use 40 (newer).
