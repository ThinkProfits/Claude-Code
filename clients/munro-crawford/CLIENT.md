# Munro & Crawford: client profile

> **Status:** DRAFT v0.1, 2026-10-06. Pending review by Francis.
> **Sources:** Slack (#munrocrawford C019AAP51U6, #gbp-post-approvals, #thinkprofits-ppc-team, Francis's planning/roadmap DMs), Drive (Website Audit sheet, Keyword Analysis July 2023, Recommendations doc, PPC Monthlies #2, ad groups + LPS, blog docs), GSC (`sc-domain:munrocrawford.ca`, 90 days to 2026-10-07), live site (curl, 2026-10-07), repo (GBP handoffs, scheduled-task skills).
> **Not checked:** Gmail (connector broken), Semrush (project 3545954 returned "unable to charge units"; organic fallback returned "API units balance is zero"), BrightLocal (tool returned a malformed result; one attempt only).
> **Related files:** [keywords.md](keywords.md), `gbp-handoffs/week-of-2026-09-*/gbp-handoff__munro_crawford__*`.
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Business**
- Multidisciplinary law firm (barristers and solicitors) in Kerrisdale, Vancouver. **Established 1952** by William (Bill) Munro; Peter Crawford joined in 1973; in the brick building at 5670 Yew Street since 1978 (live homepage FAQ). Site copy uses "Over 70 Years" and "Since 1952".
- Website: https://munrocrawford.ca (non-www; www 301s to it)
- Address: 5670 Yew Street, Vancouver, BC V6M 3Y3
- Phone: 604.266.7174. Fax: 604.266.7998. Email: info@munrocrawford.ca
- Hours: weekdays 9:00–5:00; closed Sat/Sun (live contact page)
- Offers house and hospital visits; office is wheelchair accessible.
- Timezone: Pacific

**Relationship**
- ThinkProfits built and maintains the site (footer credit "Web Development Vancouver by ThinkProfits.com Inc."). Slack channel created 2020-08-26; "Success Track 2020" doc dates from 2020-02, so the relationship started around early 2020. *Confirm start date.* The site was relaunched around Sept 2022 (Redirection Document and Website QC, Sept 2022).

**Client team** (business emails from the live /our-team/ page)
- **Katarina Tagliafero:** Managing Partner / Paralegal / **non-lawyer** partner, 20+ years at the firm. ktagliafero@munrocrawford.ca. Likely the approver ("she" approves blogs, Slack 2025-11-13). *Confirm who approves.*
- **Andrew Beesley:** Partner / Lawyer. abeesley@munrocrawford.ca. Branded searches for his name must rank top (Andrew S., 2026-07).
- **Peter Crawford:** Partner / Lawyer, 40+ years practising in Vancouver. pcrawford@munrocrawford.ca
- **Sabina Beesley:** Lawyer. sabina@munrocrawford.ca
- **Cecelia Cheung:** Lawyer. cecelia@munrocrawford.ca
- **Winnie Tang:** Lawyer (articled at the firm): civil litigation, corporate, real estate, wills and estates. wtang@munrocrawford.ca

**ThinkProfits team**
- Andrew Silbernagel: TP lead (channel topic), PPC, reviews all blogs before they go to the client
- Francis Marc Uy: SEO lead
- Clarissa: admin; has written Munro blogs (2025)

**Stack** (live site, 2026-10-07)
- WordPress with Yoast SEO 25.5, Gravity Forms, Smart Slider 3, Booked (appointments), Easy Accordion (FAQ schema), Trustindex Google reviews widget
- Page builder breaks custom code, so **FAQ schema must go through Easy Accordion** (Slack 2025-12-13)
- **Backups:** UpdraftPlus to the seo@thinkprofits.com Drive (latest set 2026-10-02, folder `1KP33mcXPmhZs4uI2bEmkqQdHpuiM7XSf`). Not opened.
- Hosting: not confirmed. Kinsta migration was recommended Nov 2023 – Jan 2024 with no recorded answer. *Confirm.*

## 2. Services: what they do and don't do

**Priority practice areas** (Andrew, Slack 2026-07: "estate, probate, wills, etc." come first)
- **Wills and estate planning:** wills, trusts (trust agreements, living / inter vivos trusts, alter ego trusts *confirm offered as a service, not just a blog*), succession planning, incapacity planning (power of attorney, representation agreements), tax concerns
- **Probate and estate administration:** after a death, probate applications, post-probate administration
- **Professional executor services**
- **Estate litigation:** wills variation, undue influence
- **Elder care:** financial management, home management, health and companionship, POA documents (led by Katarina)

**Secondary practice areas** (lower priority; work them only when estate work is covered)
- Business law: incorporation, contracts, buying/selling a business
- Real estate: residential, recreational, commercial conveyancing and mortgages; landlord/tenancy

**What they don't do (or no longer do)**
- **Co-op law: dropped 2026-09-17.** Andrew removed it from the home, about, service and real estate pages and redirected the page. Francis was asked to sweep everything else (other pages, schema, GBP). Thread followed up 2026-09-29 with no completion note. Live check 2026-10-07: no "co-op" text on the home, about, contact, team or legal-services pages. *Confirm GBP services/categories and blog posts are clean.*
- **Family law / divorce and personal injury:** the /our-team/ intro still lists "family law and divorce" and "litigation in support of personal injury claims". Neither appears in the menu or legal-services page. *Confirm whether still offered; if not, remove.* (Estate-focused blogs on separation agreements are fine.)

**Regulatory**
- Lawyers are regulated by the **Law Society of BC**. Marketing must follow the LSBC *Code of Professional Conduct for BC*, section 4.2 (marketing): no false or misleading claims, and no "specialist" / "expert" claims except as the Code allows. *Confirm current wording with the source:* https://www.lawsociety.bc.ca/support-and-resources-for-lawyers/act-rules-and-code/code-of-professional-conduct-for-british-columbia/chapter-4-%E2%80%93-marketing-legal-services/
- **Live copy to review against that rule:** homepage "Expert advice", "Looking for the 'best lawyer near me'? … the 5/5 rated law firm", and "Comprehensive Legal Solutions … virtually all of your legal needs". Flag for the client, don't silently rewrite.
- Katarina is a non-lawyer partner. Don't describe her as a lawyer anywhere.
- GBP and blog content: **education only, no outcome or result implied**, end with "general information, not legal advice" (GBP pipeline standard, Sept 2026).

## 3. Target market and geography

**Who they serve:** individuals and families planning estates, executors, older adults and their families, small-business owners. Referral-heavy (Andrew Beesley bio). *Confirm age/income profile; no documented persona found.*

**Service areas** (live homepage, 2026-10-07)
1. Kerrisdale (home base)
2. Vancouver (west side)
3. Richmond
4. "Surrounding Lower Mainland"

**Neighbourhood keywords**
- Kerrisdale, Kitsilano and "west side" are in the 2023 tracked list.
- **UBC keywords were recommended for removal in July 2023** but still showed in the July 2026 report (wills lawyer ubc, probate lawyer ubc). *Confirm whether they're still tracked and whether the client wants UBC.*
- Feb 2026: Francis proposed spending remaining landing-page budget on **location pages** (ranking only on "Vancouver" was holding them back locally) and added locations to the GBP. No reply from Andrew found. *Confirm.*

## 4. Competitors

- **westcoastwills.com:** the primary local competitor in Position Tracking; pulling ahead in visibility (Automated Report Review, 2026-07-07). Andrew endorsed a content + backlink review of it. Not done yet as far as Slack shows.
- No other competitors are documented. Semrush competitor data couldn't be pulled (units). *Pull from project 3545954 once units are restored.*

## 5. Current SEO status

**Position Tracking (from Automated Report Reviews, not pulled live)**
- June 2026 report (reviewed 2026-07-07): local visibility **34.20%** (-2.80 pts MoM), avg position -0.26. Five keywords hit #1. Drops: business lawyer vancouver -20, business law firm vancouver -20, wills lawyer vancouver -11, probate lawyer kitsilano -4.
- July 2026 report (reviewed 2026-08-08): local visibility -4.21%, avg position worse by 1.17; net -3 in top 3, -2 in top 10. **UBC/administration cluster fell from #1** (wills lawyer ubc, probate lawyer ubc, estate and trust administration vancouver).
- **No Sept or Oct 2026 report review** appears in #munrocrawford (last one 2026-08-07). *Confirm the August/September reports were sent.*

**Organic traffic (report reviews)**
- June 2026: GSC clicks +7.7% MoM, +212% YoY.
- July 2026: sessions +128% YoY, GSC clicks +168% YoY, key events +12% MoM; sessions -8.8% MoM.

**GSC, live** (`sc-domain:munrocrawford.ca`, 2026-07-09 to 2026-10-07)
- Traffic is **blog-led**. Top pages by clicks:

| Page | Clicks | Impressions | Avg pos. |
|---|---|---|---|
| /blog/gifting-property-to-children-in-bc-how-why-it-helps-with-your-estate/ | 639 | 27,632 | 5.4 |
| /blog/avoid-estate-tax-in-canada/ | 615 | 32,612 | 7.1 |
| /blog/what-to-bring-to-an-estate-planning-meeting/ | 403 | 14,690 | 6.7 |
| / (plus 266 clicks on the GBP-tagged URL) | 372 | 18,364 | 13.1 |
| /blog/joint-tenants-vs-tenants-in-common-bc/ | 294 | 29,930 | 6.0 |
| /our-team/ | 266 | 5,161 | 23.4 |
| /blog/what-is-an-alter-ego-trust/ | 217 | 10,072 | 5.3 |
| /blog/inheritance-tax-canada-terminal-return/ | 163 | 54,678 | 8.7 |

- **Service pages are weak:** /probate-estate-admin/ 27 clicks at avg position 18.3; /professional-executor-vancouver/ 52 clicks at 12.1; living trust page 38 clicks at 10.4.
- **Low-CTR, high-impression pages** (title/meta candidates): inheritance-tax-canada-terminal-return (0.3% CTR), what-is-a-power-of-attorney-in-bc (31K impressions, 0.25%), settling-an-estate-timeline (0.5%), how-much-does-probate-cost (0.3%).
- /blog/disinherit-your-child/ was dropping (Andrew, 2026-08-18). Francis delivered a rewrite doc (`1fB3uTbv3HQtqshc4Qk2_976EZl9EtPV95t6cb4OcPAU`); publish status unknown. *Confirm.*

**Schema and on-page (live, 2026-10-07)**
- LegalService + Organization schema on the home, about, contact and team pages. The homepage carries **two LegalService blocks** (likely duplicate). FAQPage on the homepage.
- **Person schema for all 6 staff is live on /our-team/** (requested 2026-07; Francis confirmed done).
- **The fake "London, UK / 10 Firs Avenue, Muswell Hill / hello@lawyers.com" template block is still in the global footer** on every page checked. Francis listed it for removal in July 2026; Andrew fixed wrong homepage contact info on 2026-07-25 but this block survived.
- The contact page still has COVID-19 remote-service copy.
- `http://munrocrawford.ca/` answered 200 without redirecting to https in a curl check. *Confirm the https redirect.*

**GBP:** location key `munro_crawford`. Twice-weekly posts via #gbp-post-approvals (education only). Reviews widget says 5/5. *Review count not pulled (BrightLocal down).*

**AI tracking:** "Top AI Platforms" tables show no data despite AI Assistant traffic (July 2026 review). Check GA4.

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-06).

**What's tracked:** Semrush project **3545954**. The keyword list couldn't be pulled this session ("unable to charge units"). The last documented list is the **July 2023 Keyword Analysis** (35 terms: wills / probate / estate / estate litigation / business law × Vancouver, Kerrisdale, Kitsilano, west side). The 2026 report reviews confirm terms like wills lawyer vancouver, probate lawyer kitsilano, business lawyer vancouver and the UBC set are still tracked.

**GSC highlights (90 days)**
- Branded: "munro and crawford" 140 clicks (pos 2.2); partner names (andrew beesley, peter crawford, winnie tang) rank 1–4.
- Informational wins: how to avoid estate tax in canada (pos 1.5), alter ego trust bc (2.0), co executor of will (2.7).
- Commercial gaps: probate lawyer vancouver (920 impressions, pos 7.4), estate lawyer vancouver (836, 6.9), probate lawyer (1,472, 16.4), wills lawyer vancouver (241, 20.1), estate planning lawyer vancouver (196, 14.8).

**Keyword rules**
- Estate, probate and wills first; business law and real estate are lower priority (2026-07).
- **No co-op law** (2026-09-17).
- No UBC terms unless the client confirms (2023 removal recommendation).
- Branded partner-name terms must stay top.

## 6. Current marketing programme and scope

**Recurring work**
- **Blogs: 1 per month** (Blog Masterlist quota). Topics go to the client in batches (Feb–July 2026 approved 2026-01-22; next list sent 2026-08-18).
- **Blog rewrites** of declining posts come out of SEO hours, not a blog slot (2026-08-18).
- **Landing pages:** some landing-page budget remained as of 2026-02-25. *Confirm balance.*
- **GBP:** Mon/Thu posts via #gbp-post-approvals.
- **Reporting:** monthly PDF report with an automated Slack review (~7th of the month).
- **Maintenance:** site edits (TP built the site), UpdraftPlus backups.
- **PPC:** Google Ads (section 7).

**Pricing**
- Google Ads budget: **$900/month** with 4 management hours (PPC Monthlies checklist, revised 2024-12-16). *Confirm current.*
- SEO retainer: not found.

**Project tracking:** new Teamwork SEO tasklist created 2026-07-03 (`3774206`). Time per blog is logged against the task linked in the Blog Masterlist.

## 7. PPC overview

**Google Ads** (from report reviews and PPC Monthlies)
- Campaigns seen: **Estate - TP**, a **General** campaign (ad groups General Lawyer, Wills & Estate Planning, Probate & Estate Administration), **Remarketing**.
- June 2026: cost/conv up 20.3% to **CA$74.73**; Estate campaign spend +45.1%, conversions -7.2%; Remarketing CA$31.03, 0 conversions for the second month. General Lawyer was the best ad group (6 conv, CA$38.90).
- July 2026: **14 conversions** (+7.7%), cost/conv **CA$63.71** (-7.6%). General Lawyer (CA$164) and Wills & Estate Planning (CA$158) had 0 conversions; Probate & Estate Administration CA$10.18/conv.
- **Phone call tracking returns no data across all campaigns** (flagged High in both June and July reviews). Andrew said he handled the ads side (July); *confirm call tracking was fixed.*
- Oct 2025: created the **"TP - Not Main Services"** negative keyword list (budget too small for non-core services); estate-planning final URLs moved to /estate-lawyers-vancouver/.
- Daily placement-exclusion bot runs on the account (#thinkprofits-ppc-team).

**Ad rules:** follow LSBC marketing rules (section 2). No "best", "expert" or outcome claims in ad copy unless the client confirms they're compliant.

## 8. Content guidelines

**Approval flow**
- Francis drafts → **Andrew reviews/edits** → client approves → TP publishes → resubmit to GSC.
- Never publish without client approval. Approvals can sit for months (May–July 2026 blogs sat "Ready To Publish"; Aug/Sept topics "Needs PM Review").

**Blog format (hard rules)**
- **Length: 1,000–1,500 words, 3–5 pages (4-page max).** Andrew cut 12- and 14-page drafts (2026-04-01, 2026-05-05). No table of contents.
- Use the **Munro blog template**: copy the last blog doc and **save it in the shared Drive folder, not personally** (Clarissa, 2025-10-16).
- **Every blog needs an FAQ section**, built with **Easy Accordion with schema turned on** (duplicate an existing one), added by shortcode. Check the schema toggle before publishing (missed twice, 2026-04-01).
- **Double-check the body text after publishing** (a duplicate body went live, 2026-04-01).
- **Hyperlink every service or topic that has a page on the site** (2026-06-16).
- **External citations link to the exact source page**, not the organisation's homepage (2026-06-16).

**Voice:** friendly, down-to-earth, plain language ("no stuffy legal jargon"). Educational, BC-specific. Canadian spelling. No outcome promises.

**Topics to avoid:** co-op law; non-BC law (except Canada-wide tax context); family-law advice beyond estate impact.

**Photos:** use real images from the site. The 2200×597 firm banner crops badly on GBP; prefer each page's own featured image (GBP handoffs, Sept 2026).

## 9. Key priorities and strategic notes

**Open priorities (Slack, Jul–Sept 2026)**
1. Finish the **co-op law removal sweep** (pages, schema, GBP, blogs).
2. **westcoastwills.com** content and backlink review.
3. Investigate the **UBC/administration keyword drop** and the business-law drops (business law is lower priority).
4. Keep **Andrew Beesley** (and other partner names) ranking top. Person schema is now live.
5. Publish the **disinherit-your-child rewrite** once approved.
6. Confirm Google Ads **call tracking**.

**Strategic read**
- Blogs drive almost all organic clicks; service pages sit at positions 7–18 for commercial "lawyer vancouver" terms. Converting blog authority into service-page rankings (internal links from top blogs to probate, wills and executor pages) is the highest-leverage work.
- Several blogs earn huge impressions at under 1% CTR. Title/meta refreshes are cheap wins.
- Location pages (Kerrisdale, Kitsilano, Richmond) are proposed but unapproved.
- The fake London footer block is a trust and NAP problem on a law firm site. Fix it first.

## 10. Social profiles and other channels

- No social profiles found in the live header/footer or in Slack. *Confirm whether any exist.*
- Andrew Beesley's LinkedIn and Instagram compete with the site on his name (2026-07).
- GBP is active (`munro_crawford`).

## 11. Working rules and tool IDs

**Approvals**
- Content: Andrew reviews, then the client approves.
- GBP: 👍 in #gbp-post-approvals.

**Standing rules**
- Estate / probate / wills first
- No co-op law
- 1,000–1,500-word blogs with Easy Accordion FAQ schema
- Education only, no outcome claims (LSBC)
- Katarina is a non-lawyer partner

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | **3545954** (Position Tracking; units exhausted 2026-10-07) |
| GSC | `sc-domain:munrocrawford.ca` (agency access works) |
| Slack | #munrocrawford C019AAP51U6. GBP source of truth: #gbp-post-approvals |
| GBP automation key | `munro_crawford` |
| Teamwork | SEO tasklist 3774206 |
| Scheduled tasks | blog-masterlist-planning-run, blog-masterlist-draft-check, seo-report-roadmap |

**Drive**

| File | ID |
|---|---|
| UpdraftPlus backups (seo@ Drive) | folder `1KP33mcXPmhZs4uI2bEmkqQdHpuiM7XSf` |
| Website Audit – Munro & Crawford (edited 2026-01-20) | `1cs9JDR1yMU5x2tqmiXLMtaQXYBO4wYdnWUB0VgSkiEk` |
| Keyword Analysis July 2023 | `1JT7Ic0m-J3Wbrgh0kmn_ZAJMHa_COdJxvvZnM9rsi0k` |
| Recommendations doc (to Jan 2024) | `17ExJ9LEceB2yPQtFcEUOaoz_QQko_XRNzxWQIeAuiss` |
| PPC Monthlies #2 (Oct 2025 on) | `13m_PnDCZuTskMF9SgAXDXDe_79JDCkjrfe69BzusD5Y` |
| SEO Monthlies (to Nov 2024) | `1nh7y0Ce0c2CtN6Jek0kz2FdOouEpGdPELMSQvFxhKq0` |
| BLOG Masterlist 2024–2026 (Munro tab gid 1670015287) | `1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw` |
| Blog Internal Links (2024) | `1x1EHlOeYLbZs1Wn7ZhU7JN5SJLr9WnqmFhdUSk-dpac` |
| Disinherit-your-child rewrite | `1fB3uTbv3HQtqshc4Qk2_976EZl9EtPV95t6cb4OcPAU` |

## 12. Open items

**Waiting on the client**
- [ ] Approval of the blogs sent 2026-09-17 (Notary vs Lawyer for Your Will in BC; BC Property Transfer Tax Exemptions).
- [ ] Approval of the topic list sent 2026-08-18.
- [ ] Confirm whether family law / divorce and personal injury are still offered.
- [ ] Confirm UBC targeting and the location-page idea (Kerrisdale, Kitsilano, Richmond).
- [ ] Sign-off on homepage "best lawyer near me" / "5/5 rated" / "Expert advice" wording against LSBC rules.

**Live site fixes**
- [ ] Remove the **London, UK / hello@lawyers.com** footer block (sitewide).
- [ ] Remove "family law and divorce" / "personal injury" from the /our-team/ intro if not offered.
- [ ] Remove or update the COVID-19 copy on the contact page.
- [ ] De-duplicate the two LegalService blocks on the homepage.
- [ ] Check the http → https redirect.
- [ ] Finish the co-op law sweep (blogs, schema, GBP services). Find the redirected URL and confirm the 301.

**Blog backlog**
- [ ] May–July 2026 blogs were stuck "Ready To Publish" (2026-07-27). *Confirm they're live.*
- [ ] Publish the disinherit-your-child rewrite once approved.

**Ops**
- [ ] Restore Semrush API units and pull project 3545954 (keywords, competitors, visibility).
- [ ] westcoastwills.com content and backlink review.
- [ ] Verify Google Ads call tracking and the GA4 AI-platform reports.
- [ ] Confirm the Aug/Sept 2026 monthly reports went out (no Slack review after 2026-08-07).
- [ ] Confirm the hosting provider and UpdraftPlus retention.
- [ ] **Security:** Drive has a sheet titled "Munro & Crawford Login Details" (`1RaCgnBBbzOW5u1X_IvIxrlqsZR6ToQPusTP1598gxl4`, 2020). Not opened. If it holds credentials, move them to a password manager and delete the sheet.
- [ ] **Security:** failed WordPress login attempts were reported for Munro on 2025-10-11 (see aloha-life-massage CLIENT.md). Confirm 2FA / login limiting is on.
- [ ] **Security:** UpdraftPlus database backups in the seo@ Drive contain user data and password hashes. Confirm that folder isn't shared widely.

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked (connector broken).
- Semrush: no live tracked list, visibility or competitor data (units exhausted).
- BrightLocal: no reviews or citation data.
- SEO retainer and current Ads budget not confirmed.
- Blog Masterlist Munro tab not read row by row (topic plan Oct 2026 – Feb 2027 is there).
- Client approver and full contact roles not confirmed.

**Conflicts**
- **UBC keywords:** removal recommended July 2023, still tracked in 2026 reports.
- **Services:** /our-team/ lists family law, divorce and personal injury; the menu and legal-services page don't.
- **Footer:** fake London block vs the real Yew Street NAP on the same pages.
- **Blog length:** 2025 guidance said "closer to 1,000–1,500 words"; 2026 says 3–5 pages / 4-page max. Use 1,000–1,500 words.
- **Elder care keywords:** 2023 list recommended adding "elder care lawyer" terms; the elder-care page exists, but no current tracking data confirms them.
