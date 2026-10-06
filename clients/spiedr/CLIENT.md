# SPIEDR: client profile

> **Status:** DRAFT v0.1, 2026-10-06. Pending review by Francis.
> **Sources:** Slack (#firestorm_spiedr C01928K8M0F, #gbp-post-approvals, group DM with Shawn/Andrew/Clarissa, Francis's planning-run DMs), Drive (SEO/AEO/GEO Roadmap Sept 2026, Success Track 2023, Post-Performance Review 2023-01-18, Audit & Keyword Research sheet, 2026 contracts), GSC (`sc-domain:spiedr.com`, 90 days to 2026-10-05), Semrush (organic research, `ca` database), `wp-spiedr` MCP (read-only), live site, repo.
> **Not checked:** Gmail (connector broken), BrightLocal (tool returned a schema error), Semrush Position Tracking (API: "unable to charge units").
> **Related files:** [memory/spiedr-context.md](../../memory/spiedr-context.md) (tracking quirks, crawl workaround, stack), [keywords.md](keywords.md), [spiedr-fix-roadmap-2026-q4.md](spiedr-fix-roadmap-2026-q4.md), [spiedr-sept-2026-ranking-and-internal-linking-review.md](spiedr-sept-2026-ranking-and-internal-linking-review.md), [slack-thread-reply-draft.md](slack-thread-reply-draft.md).
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Client overview

**Business**
- SPIEDR Ltd. ("SPIEDR™", tagline "We Protect Structures™", tag line on About page "Wet Fuel Won't Burn!"). Designs and manufactures wildfire structure-protection equipment in BC.
- Pioneered sprinkler trailers and sprinkler kits; manufacturing since 2004. About page claims SPIEDR built "98% of all purchased Structure Protection Trailers in Canada" (*confirm before reusing; client claim, no source*).
- Website: https://www.spiedr.com (WordPress + WooCommerce shop)
- Sister brand: **Firestorm / wildlandequipment.com**. Billed together as "Spiedr (Firestorm)", but TP's SEO work has only ever been for spiedr.com (Andrew, 2026-02-18).
- Phone: +1 604-812-3473 (site header and schema)
- Address (site schema / GBP): 2952 Long Lake Rd, Knutsford, BC V0E 2A0. Contracts use a mailing address: Box 63, 6849 Old Nicola Trail, Quilchena, BC V0E 2R0. GBP drafts label the location "Knutsford/Kamloops".
- Public email: none on the site (contact form only). Schema still has `[CONFIRM-EMAIL]`.
- Timezone: Pacific

**Relationship**
- Long-standing client: SEO reports on file from 2017; PPC Bronze ran in 2017 and was cancelled (Success Track 2023).
- January 2023 Post-Performance Review: owner is moving toward retirement and a consulting focus; TP recommended merging spiedr.com and wildlandequipment.com ($20,000 web + $6,500 migration). Not taken up then. Sites were moved from Kinsta to HostGator around then.

**Client contacts** (business addresses only)
- **Bob Swart:** President (bob@spiedr.com). Original structure-protection specialist; the consulting expertise is his.
- **Natalie Smolinski:** natalie@spiedr.com. Named on the 2026 Spiedr web contract; the 2026 Firestorm contract references "Natalie's time" on hiring/government submissions.
- Note (2023): "with their operation, they may not be able to attend to our requests (like signing off documents)". Slow sign-off is normal.

**ThinkProfits team**
- Shawn Moore: account lead, signs the monthly report, owns billing/contracts
- Andrew Silbernagel: manager; reviews and approves blogs
- Francis Marc Uy: SEO lead
- Clarissa: admin (Teamwork / billing records)
- Brittni Woodson: former TP lead (2023 Success Track)

**Stack** (checked 2026-10-06 via `wp-spiedr` MCP; detail in memory)
- WordPress 7.1.2, WooCommerce 11.0.1, WPBakery 7.9 + Classic Editor, DesignThemes "Whistle" theme (Unyson framework)
- Yoast SEO 28.2, Redirection, Autoptimize, Easy Accordion (FAQ schema), Gravity Forms + Contact Form DB, Trustindex Google Reviews widget
- Security: Wordfence 9.0, Limit Login Attempts, WPS Hide Login (`/tp-login/`)
- Automation: Make Connector, Easy MCP AI (`wp-spiedr` server), WPCode Lite, Simple Custom CSS/JS
- Also active: WP File Manager, Search & Replace, WP Migrate Lite, UpdraftPlus, Duplicate Page (see section 12, security)

## 2. Services: what they do and don't do

**What they do**
- **Sprinkler trailers / Structure Protection Units (SPU):** Fire Service Trailers, Industry Wildfire Protection Trailer, 1 KM WETLINE™ trailer, community wet-line trailers
- **Sprinkler kits:** wildland sprinkler kits, Deluge (protects 4 structures), RAINMAKER™ sprinkler, roof sprinkler systems, structure protection sprinklers
- **Fire pumps:** WATERAX pumps (Mark-3, BB-4, Striker, Rancher, B2X etc.), sold through the WooCommerce shop. SPIEDR is a WATERAX reseller, not the manufacturer.
- **Wildfire consulting** (`/services/wildfire-consulting/`): FireSmart/FIREWISE assessments, fuel management, community protection systems, land development. Client says FireSmart/FIREWISE accredited (*confirm accreditation detail*).
- **Fire-fighting equipment rentals** (`/fighting-equipment-rentals/`)
- **Wildfire firefighting training in BC** (`/wildfire-fighting-training/`; Semrush also shows `/training/` ranking for "wrts")

**What they don't do / de-prioritised** (Post-Performance Review and Success Track, January 2023)
- **Film production consulting:** client asked to remove it. **Still listed** on the live consulting page (2026-10-06).
- **WIDGET™ Water Thief:** client asked to remove it from the site. **Still in the main menu** (2026-10-06). *Confirm whether the product is back on sale.*
- Trailer manufacturing: "not pursuing as much as before" (2023). *Confirm current position; the 2026 homepage leads with trailers.*
- Government work won through bidding: lower priority.
- Small homeowner jobs: lower priority (still acknowledged in content, never the lead).
- WATERAX: client wanted to stop selling some WATERAX products but stay associated with the brand (2023). The pumps are still sold in the shop. *Confirm.*

**Regulatory / claims**
- No licence-number rule found (unlike John Sadler).
- Product claims ("one trailer can protect about 50 homes", "98% of trailers in Canada") are client claims; don't put them in new content without a source or client confirmation.

## 3. Target market and geography

**Who they sell to** (Success Track 2023; reinforced by Andrew 2026-06-16)
- **Commercial first:** oil and gas camps, industrial sites, municipalities and community fire committees, resorts, camps, land developers, wineries and agricultural operations with their own water source, critical infrastructure.
- Buyers care about **how soon** (delivery timeline), not how much.
- Business goal (2023): "3–4 big fish clients" a year, e.g. clients spending around $400K, rather than "people fishing around the internet" for ideas.
- Homeowners: acknowledge briefly; never drive the structure of a post.

**Geography**
- Primary: **British Columbia**, especially the Interior (Kamloops, Okanagan, Cariboo). Content should name BC places (Kamloops, Okanagan, Kelowna) where it fits (Andrew, 2026-02-03).
- Secondary: Western Canada (Alberta, Saskatchewan per schema).
- The US is a minor market. Content must not be US-led (March and April 2026 blogs were rewritten for being too US/California-focused).
- GSC, 90 days: Canada 604 clicks, US 336 clicks (US has more impressions: 41.8K vs 35.0K).

## 4. Competitors

**Organic** (SEO/AEO/GEO Roadmap, Sept 2026, Semrush `ca`)

| Domain | Note |
|---|---|
| flashwildfireservices.ca | ~880 ranking keywords, ~1,156 est. monthly visits. The organic competitor to watch |
| waterax.com | Spiedr's own pump supplier. ~175 keywords / ~648 visits. Treat as a co-marketing/backlink partner, not a rival |

**Tracked-campaign competitors:** not pulled (Position Tracking API failed 2026-10-06). The July 2026 roadmap noted a competitor lost ground on "wildfire protection" in the same SERP move.

**Brand association:** wildlandequipment.com is the client's own sister site (Firestorm), not a competitor. It currently appears in a `sameAs` field on spiedr.com's homepage schema, which wrongly merges the two entities (section 5).

## 5. Current SEO status

**Snapshot** (Semrush `ca`, 2026-10-06): 149 organic keywords, ~17 est. visits/month, Semrush Rank 1,613,851. Authority Score 7/100 (Sept 2026 roadmap).

**GSC, 2026-07-09 to 2026-10-05 (national, all countries)**
- 1,089 clicks, 96,946 impressions, CTR 1.1%, avg position 16.1
- Clear seasonal fade: daily clicks of 15–30 in late July/early August fell to 3–10 by late September (fire season ending).
- Top pages by clicks: homepage (114), /sprinkler-trailers/ (76), /mark-3-pump/ (59), Mark-3 QS product (56), /blog/does-rain-really-reduce-wildfire-risk/ (54, 7.7K impressions), /sprinkler-kits/ (51), fire service trailers (51), /wildfire-sprinkler-kit/ (48, 7.4K impressions at pos 20.7), true-cost-of-wildfires blog (47), /roof-sprinkler-system/ (39, 4.1K impressions at pos 18.3).
- Top queries: "spiedr" (48 clicks), mark 3 pump (12), wajax fire pumps for sale, wildland fire trailer, wildland fire sprinkler kit.
- **Note:** neither /fire-embers/ nor the BC fire-bans blog is in GSC's top 20 pages for this window, although Semrush estimates /fire-embers/ as a top traffic page. Check page-level GSC before calling /fire-embers/ "the top traffic page" to the client.

**Monthly report trend** (automated reviews in #firestorm_spiedr)
- June 2026 (May data): 2 key events (-87.5% YoY), organic sessions -64.1% YoY, Singapore = 49% of users (likely bots), GSC clicks -70.1% YoY.
- August 2026 (July data): sessions +42.4% MoM, GSC clicks +115% MoM, but key events -50% MoM. Review mentions a "Maui campaign", which looks like an error in the automated review.
- September 2026 (August data): GSC clicks +9.7% MoM / +37.1% YoY, CTR +18%, visibility +4.35 pts; new #1s for "wildland fire structure protection", "portable fire pumps for sale", "structure protection unit trailer". GBP shows 0 reviews / 0 call clicks.
- No October report in Slack yet (September's arrived on the 7th).

**Ranking review and roadmap** (summaries; full detail in the linked files)
- [Sept 2026 ranking & internal-linking review](spiedr-sept-2026-ranking-and-internal-linking-review.md) (2026-09-17): most flagged Top 3/10 losses were a day-1-vs-day-31 reporting artifact. Real declines: "top wildfire sprinkler protection", "fire protection roof sprinkler system", "fire fighting pumps for sale". Three terms moved together on 11–12 Sept (SERP-side). Internal linking is the core problem: /roof-sprinkler-system/ and /fire-embers/ have zero in-content inlinks; 45 of 93 blog posts are orphaned.
- [Q4 fix roadmap](spiedr-fix-roadmap-2026-q4.md) (18 Sept–12 Nov 2026): Phase 0 baseline + approvals; Phase 1 ~30 internal links to 4 pages (due before 1 Oct); Phase 2 keyword-set rebuild + report fix (due before the 6 Oct report); Phase 3 blog topic hubs. Targets are directional, not commitments.
- [Slack reply draft](slack-thread-reply-draft.md): our answer to the Sept report review. **Not posted**: the 2026-09-07 thread still has no reply from Francis, and Andrew followed up on 09-16, 09-17 and 09-30.

**SEO/AEO/GEO audit** (Drive, Sept 2026)
- Homepage ships three JSON-LD blocks, two conflicting Organization entities, live placeholders `[CONFIRM-EMAIL]`, `[CONFIRM-LAT]`, `[CONFIRM-LNG]`, `[CONFIRM-CHANNEL-HANDLE]`, and a `sameAs` pointing to wildlandequipment.com. **All still live on 2026-10-06.**
- llms.txt had scaffolding comments and typo'd slugs. **Appears rebuilt**: the 2026-10-06 copy has no placeholder comments or "zobie" typo.
- Semrush Site Audit: 34 errors, 11,815 warnings; ~267 pages 302 through `/tp-login/?action=register`; 85 missing meta descriptions; 40 pages with multiple H1s; 30 duplicate titles; 88 low-word-count pages.
- Cannibalization: six URLs compete for "wildfire sprinkler system" (best is #11); "controlled burn" splits across three blog URLs.
- Commercial terms are very low volume in Canada (10–30/mo). Growth lever = authority + AEO + routing blog traffic into product/service pages.

**Indexing:** Andrew found `/services/wildfire-consulting/` missing from the XML sitemaps (2026-09-16). Francis fixed its canonical (it pointed at `/services/consulting/`, which redirected back) and fixed 3 other services-hub URLs; all now in the sitemap (2026-09-17). *Confirm the GSC resubmission and the wider indexing check Andrew asked for.*

**Yoast** (15 most recently modified posts, 2026-10-06): 5 have no focus keyphrase ("na"), including the two September 2026 blogs and "Early Wildfire Detection in BC".

**GBP:** location key `spiedr` in the GBP pipeline. Reports show **0 reviews, 0 rating, 0 call clicks** against ~1.3K impressions since at least May 2026. Treated as a sync/tracking gap until proven otherwise.

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-06).

**What's tracked:** Semrush project 2084675, Position Tracking campaign 2084675 (Desktop / British Columbia / Google). 47 keywords as of Sept 2026, **44 of them at 0–30 searches/month**. The live list couldn't be pulled on 2026-10-06 (API "unable to charge units"), so *confirm in the Semrush UI whether the Phase 2A refresh was done before the 6 Oct report.*

**Where the volume is** (Semrush `ca`, 2026-10-06)
- BC fire-ban cluster on one blog post: fire ban bc (5,400) #36, fire ban (6,600) #56, bc burning ban (720) #30. Was #25–31 in mid-September, so it has slipped.
- Fire-whirl blog: tornado and fire / fire whirlwind (1,600 each) #24–28.
- Product terms that actually convert: mark 3 pump (170) #5, waterax (480) #25, roof fire sprinkler system (70) #14, wildfire sprinkler system (70) #11.

**Clean-up**
- Replace the near-zero tracked terms with ranked, higher-volume terms (roadmap Phase 2A).
- Resolve "wildfire sprinkler system" cannibalization (6 URLs).
- Seasonal: fire-ban queries peak July–August. Refresh that post before May 2027.

**Keyword rules**
- Commercial buyers first; BC/Canada first.
- Don't target film production, government tender/bid terms, or US-first terms.
- Keep consulting/FireSmart terms in scope: consulting is the 2023 strategic priority.

## 6. Current marketing programme and scope

**Recurring work**
- **SEO Silver:** 8 hours/month per Teamwork (Andrew, 2026-02-18). Internal linking, technical fixes, reporting follow-ups.
- **Blogs:** 1 per month. **No client approval needed**; Andrew reviews and approves (planning run 2026-09-25). Andrew approved the 2026 schedule on 2026-01-22.
- **GBP:** Mon/Thu posts through #gbp-post-approvals (`spiedr`). Every blog also gets a GBP post; Andrew wants these long (up to ~1,500 characters, 2026-02-03).
- **Reporting:** automated monthly report around the 7th, with an automated review thread. Staff must reply confirming they've read it.

**Pricing** (*confirm current figures with Shawn*)
- Teamwork record: **SEO Silver $1,499/month (8 h) + 1 blog $150**, since about June 2024 (Andrew, 2026-02-18).
- Shawn said in the same thread "we are charging them 999 month plus blog". The Jan 2023 review shows Silver at $999 (6 h, 150 keywords) + blog $150 + reputation software $64 = $1,213 + tax. **The two figures conflict.**
- Feb 2026: Shawn introduced an hourly "AEO - AI Engine Optimization" item at the SEO rate, with standardised pricing messaging. *Confirm whether it was added for Spiedr.*

**Proposed/2026 contracts in Drive (March 2026; signature status unknown, *confirm*)**
- "Spiedr Think Web Sales Platinum Contract 2026": new spiedr.com website, $19,999, hosted on Lovable (~$50 USD/month), addressed to Natalie.
- "Firestorm Think Web Leads Gold Contract 2026": wildlandequipment.com, $9,999 + $2,000 custom AI lead-qualification, Lovable hosting, addressed to Bob.
- If the Spiedr rebuild is going ahead, it changes the Q4 roadmap: hub templates, schema and internal-link work should be specced for the new build rather than WPBakery.

**Project tracking:** Teamwork SPIEDR SEO tasklist 3723885; SPIEDR Blogs project 1146978 (Andrew, 2026-03-20).

## 7. PPC overview

- No active PPC. PPC Bronze ran in 2017 and was cancelled (Success Track 2023).
- Semrush `ca` shows 0 paid keywords (2026-10-06).
- Any PPC proposal would need a fresh scope; budgets presented as ranges with assumptions.

## 8. Content guidelines

**Approval flow**
- Francis drafts; **Andrew reviews and approves**; no client sign-off needed for blogs. Andrew sometimes rewrites and hands back "ready to publish".
- After publishing: set the author to the client's account (admin), add blog categories, and match the "Quick Answer" block styling to /blog/wildfire-insurance-coverage-commercial-properties/ (Andrew, 2025-12-13 and 2026-07-09).
- Watch scheduled dates: one post missed its schedule in Dec 2025.

**Standing rules from Andrew**
- **Lead with BC and Canada** (2026-06-16). Use BC Wildfire Service, Natural Resources Canada, CIFFC, Canadian Drought Monitor and the BC River Forecast Centre first. US data (NIFC, NIDIS, CPC) is supporting context only.
- **Write for commercial users first** (2026-06-16): site managers, operations leads, community fire-protection committees.
- **Every factual claim links to the exact source page**, not an organisation's homepage. No source, no figure (2026-06-16 and 2026-07-09).
- **Length: 3–5 pages.** The 10–14 page March/April 2026 drafts were rejected (2026-04-01, 2026-05-05).
- **FAQ schema on every post with FAQs**, using the Easy Accordion plugin with schema switched on (2026-02-03). Older posts still need it backfilled.
- Add internal links to services and related blogs; Andrew's edits usually add them.
- Images: Andrew asked where images come from (2025-12-13). Use the client's own media library; GBP images must be at least 400x300 (`sprinkler-tower.jpg` is 384x336 and fails).

**Voice:** expert, practical, calm. Wildfire is serious; no hype, no fear-mongering. Canadian English.

**Topics to avoid or reframe:** homeowner-first and campground angles (backlog ideas r42–47 need reframing), US-led stories, film production.

## 9. Key priorities and strategic notes

**Open asks from Andrew**
1. Reply in the 2026-09-07 report thread on the Top 3/10 drop-offs and internal linking (draft ready, not posted; three follow-ups).
2. Check other pages/blogs missing from the sitemap and resubmit to GSC (2026-09-16).
3. The June 2026 "significant drop in GSC YoY" investigation (2026-06-16): Francis acknowledged the report on 07-23 but no cause/fix write-up was found.
4. Backfill FAQ schema on older blogs (2026-02-03).

**Q4 roadmap phases** (see [spiedr-fix-roadmap-2026-q4.md](spiedr-fix-roadmap-2026-q4.md))
- Phase 1 internal links (due before 1 Oct) and Phase 2A keyword refresh (due before the 6 Oct report): **no evidence either shipped.** *Confirm.*
- Blocking question 0.5: who ships on-page edits, us or SPIEDR. Now partly answered: we have WordPress access through `wp-spiedr`, and Francis has already edited canonicals/sitemap.

**Sept 2026 SEO/AEO/GEO roadmap (Drive), Phase 1 quick wins**
- Fix the schema placeholders and collapse the three JSON-LD blocks
- Kill the sitewide 302 to `/tp-login/?action=register`
- Batch the 85 missing meta descriptions; fix multiple H1s

**Strategic read**
- This is a low-volume B2B/B2G niche: a single good-fit lead matters more than traffic. Measure leads (forms, calls, PDF downloads), not just rankings.
- The blog brings most impressions (fire bans, fire whirls, rain), but it's informational and seasonal. Route it into product and consulting pages.
- Consulting is the stated strategic focus (2023), yet the consulting page still carries "Film Production" and lacks proof. Worth a rewrite.
- Lead tracking looks unreliable: key events swing wildly, and Singapore/Tehran traffic suggests bots. Fix GA4 filtering before quoting conversion trends.

## 10. Social profiles and other channels

- Facebook: facebook.com/wetfuelwontburn
- X/Twitter: @wetfuelwontburn (schema; *confirm active*)
- LinkedIn: linkedin.com/company/spiedr
- YouTube: referenced in schema with a placeholder handle. *Confirm the channel URL.*
- No TP social management in scope.
- Sister site: wildlandequipment.com (Firestorm).

## 11. Working rules and tool IDs

**Approvals**
- Blogs: Andrew approves; no client approval.
- GBP: 👍 in #gbp-post-approvals.
- Site edits: low-risk SEO edits (links, meta, canonicals) have been made directly. *Confirm whether larger changes need client sign-off (roadmap task 0.6).*

**Standing rules**
- BC/Canada first; commercial buyers first; source every stat to the exact page
- Blogs 3–5 pages; FAQ schema via Easy Accordion
- Author = client admin account; add categories; Quick Answer styling
- Check the server prefix is `wp-spiedr` before any WordPress write
- Send a Chrome User-Agent plus `Accept` headers when crawling (Mod_Security)
- Position Tracking is Desktop/BC; GSC is national. Say so wherever they sit side by side.

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | Project **2084675** ("Spiedr", `www.spiedr.com`); Position Tracking campaign 2084675 (Desktop / BC / Google) |
| GSC | `sc-domain:spiedr.com` (agency account has access) |
| WordPress MCP | `wp-spiedr` (Easy MCP AI, user scope) |
| Slack | #firestorm_spiedr C01928K8M0F (renamed from #firestorm 2026-04-01). GBP: #gbp-post-approvals |
| GBP automation key | `spiedr` |
| Teamwork | SEO tasklist 3723885; Blogs project 1146978 |
| Scheduled tasks | blog-masterlist-planning-run, blog-masterlist-draft-check, seo-report-roadmap |

**Drive**

| File | ID |
|---|---|
| SPIEDR SEO/AEO/GEO Roadmap, Sept 2026 | `1VthMeqqe2t2dvJFsKVIWQomfjxRiiaNZSfte9V2MdU4` |
| Spiedr - Audit & Keyword Research (crawl + keywords, edited 2025-12-09) | `1Zbq_8qnLwpzj7mOlGc4-oM0kPXxaugfubmPSn5R34bs` |
| SPIEDR Success Track 2023 | `1_T5hF3mR9nsQ24f06TO3rDdg9GrlU4leB6BiPOcyjvE` |
| Post-Performance Review 2023-01-18 | `1wy44ShGwfCHzBGK6iikUWytQJZr3ObqN9WMkAhFCQBU` |
| BLOG Masterlist (Spiedr tab) | `1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw` |
| Spiedr SEO Keyword Acceptance Form 2021 | `1M3KX5-rgRSIMGACm8tl1VMUOokyLNr1L8AUj9Hk-2sM` |
| Spiedr Think Web Sales Platinum Contract 2026 (PDF) | `1pgtMlZTsX4OMH9zLSRguOiFjJ-GFRvsL` |
| Firestorm Think Web Leads Gold Contract 2026 (PDF) | `1gbckP-GwZOXCcV2XQEsqaS_DDvEplDAb` |
| Blog automation feed (shared, SPIEDR tab) | `1pn-1J7PENZD3ZYIwn_s9qZAdfBK2yS9ZcqTJg8bGqU0` |

## 12. Open items

**Waiting on us**
- [ ] Post the reply in the 2026-09-07 report thread ([draft](slack-thread-reply-draft.md)). Update its numbers first: "fire ban bc" is now #36, not #25–31.
- [ ] Ship roadmap Phase 1 internal links (roof sprinkler, Mark-3, fire embers, fire pump systems). Due 1 Oct; no evidence it's done.
- [ ] Refresh the Position Tracking keyword set (Phase 2A) and switch reports to averaged rank change (2B).
- [ ] Run a Screaming Frog crawl (none on file).
- [ ] Write up the June 2026 GSC YoY drop investigation.
- [ ] Finish the sitemap/indexing sweep and GSC resubmission (Andrew, 2026-09-16).
- [ ] Backfill FAQ schema on older posts.
- [ ] Add Yoast focus keyphrases to the 5 recent posts with none.

**Live site fixes**
- [ ] Remove the schema placeholders (`[CONFIRM-EMAIL]`, `[CONFIRM-LAT/LNG]`, `[CONFIRM-CHANNEL-HANDLE]`) and the wildlandequipment.com `sameAs`; merge three JSON-LD blocks into one entity. Needs the real email and YouTube handle from the client.
- [ ] Stop the sitewide 302 via `/tp-login/?action=register`.
- [ ] Remove "Film Production" from the consulting page (client request, 2023).
- [ ] Decide on WIDGET™ Water Thief (client asked to remove it in 2023; still in the menu).
- [ ] Consolidate the six "wildfire sprinkler system" URLs and the three "controlled burn" posts.

**Blog backlog** (planning run 2026-09-25)
- [ ] Oct–Dec 2026 rows (r31–33) are approved but lack angles and secondary keywords (secondaries sit in backlog r69–71).
- [ ] Nothing planned from Jan 2027. Proposed: structural fire protection for commercial sites (Jan), roof sprinkler systems for commercial properties (Feb), choosing a portable fire pump (Mar).
- [ ] Aug and Sept 2026 rows say "Published" with no URL. Add the links.

**Waiting on the client / account**
- [ ] Confirm whether the 2026 Platinum (spiedr.com rebuild on Lovable) and Gold (wildlandequipment.com) contracts were signed.
- [ ] Confirm the current retainer ($1,499 vs $999 + blog).
- [ ] GBP: confirm the profile is connected to reporting and why reviews/calls show 0. If reviews really are zero, raise a review programme with Bob and Natalie.
- [ ] GA4: filter Singapore/Tehran bot traffic; audit key events (forms, calls, pdf_download).

**Security**
- [ ] **Rotate the `wp-spiedr` Easy MCP AI bearer token.** It was pasted in chat once (memory, 2026-10-02). *Confirm it was rotated.*
- [ ] **WP File Manager is active** on production. This plugin type has a history of critical exploits. Recommend removing it, plus deactivating Search & Replace and WP Migrate Lite when they're not in use.
- [ ] Failed WordPress login attempts were reported on 2025-10-11 (Spiedr among four sites). *Confirm follow-up.* Limit Login Attempts and Wordfence are now active.
- [ ] Public registration appears enabled (`/tp-login/?action=register` linked sitewide). *Confirm it's needed (WooCommerce accounts?) or close it.*

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked.
- Semrush Position Tracking not readable (API "unable to charge units"); tracked list, competitors and current tier counts not pulled.
- BrightLocal: tool error; no review or citation data.
- No GA4 data pulled directly.
- Current retainer and the 2026 contract signature status not confirmed.
- No Sept 2026 keyword-set refresh found in Drive or Slack.
- The automated Aug 2026 review references a "Maui campaign"; unclear whether the report pulled the wrong campaign.

**Conflicts**
- **Retainer:** $1,499 Silver (Teamwork, Andrew) vs "$999 plus blog" (Shawn), both 2026-02-18.
- **Top traffic page:** the Sept review calls /fire-embers/ the top organic traffic page (Semrush estimate); GSC's 90-day top 20 doesn't include it.
- **Fire-ban post position:** #25–31 in the Sept review; #28–56 in Semrush on 2026-10-06 (main term "fire ban bc" #36).
- **Roadmap Phase 9** ("set up Position Tracking, not yet configured") conflicts with memory and the Sept review, which show a 47-keyword campaign. The roadmap line is out of date.
- **Removed services still live:** Film Production and Water Thief (client asked to remove both in 2023).
- **Address:** Knutsford street address (site/GBP) vs Quilchena mailing address (contracts). Use Knutsford for NAP; *confirm.*
- **Positioning:** 2023 said trailer manufacturing was winding down and consulting was the focus; the 2026 homepage leads with trailers for industrial sites. *Confirm current priority with Bob.*
