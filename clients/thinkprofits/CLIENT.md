# ThinkProfits: agency profile

> **Status:** DRAFT v0.1, 2026-10-07. Pending review by Francis.
> **What this is:** the "who we are / how we work / our own site" reference for any team member or Claude session. It is not a normal client brief. For client work, read the client's own `clients/<client>/CLIENT.md` too.
> **Sources:** repo (`CLAUDE.md`, `README.md`, `memory/*`, `scheduled-tasks/*`, `automations/*`, `gbp-handoffs/*`, every `clients/*/CLIENT.md`, this folder's `data/` and GSC xlsx), Slack (#tpmarketing, #thinkprofits-ppc-team, #seo, #team-chat, #gbp-post-approvals, #thinkprofits-site-forms, Francis's DM, group DM, channel list), Drive (search for pricing/proposal/contract files), live GSC (`sc-domain:thinkprofits.com`, 90 days to 2026-10-07), live site via curl (2026-10-07).
> **Not checked:** Semrush (API units balance at zero on 2026-10-07, so no calls), Gmail (connector broken), BrightLocal, Flowlu, Teamwork (no connector).
> **Related:** [keywords.md](keywords.md), `data/` (blog triage, old sitemap, 2026-08-25 meeting notes, AEO/GEO topic template).
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

## 1. Agency overview

**Business**
- Legal name: **ThinkProfits.com Inc.** (brand: ThinkProfits / Think Profits). Founded **1996** in Vancouver by Shawn Moore.
- Office: **#602-1388 Homer Street, Vancouver, BC V6B 6A7**. Hours Mon–Fri 9am–5pm Pacific.
- Phones (business lines on the site): toll-free 1-877-597-7888 (sales), local (604) 638-1188.
- Emails on the site: `clientcare@thinkprofits.com` (schema, form notifications) and `info@thinkprofits.com` (About page). *Confirm which is primary.*
- Sister brands (same founder): **Mujo Learning Systems** (mujo.com, digital marketing textbooks; also a client channel) and **AI Savvy** (aisavvyceo.com / aisavvy.io / aivy.io; AI consulting and speaking). Online store: `store.thinkprofits.com`.
- Positioning (site, 2026-10-07): "Vancouver's longest-running digital marketing agency", AI search + SEO + PPC + web design for established businesses (site says **$3M+** revenue on the homepage/footer, **$2M+** on About; conflict). Month-to-month, no long-term contracts; clients own all accounts. 5.0 Google rating, 48 reviews. Google Partner. **Certified Lovable partner agency** since 2026-08-13.
- Timezone: business runs on **Pacific time**. Francis works from the Philippines (PHT, UTC+8); scheduled routines are set in PHT or UTC, so check each one.

**Team (as seen in Slack and the repo)**

| Person | Role |
|---|---|
| Shawn Moore | Owner, President & CEO. Billing, contracts, pricing, final say on account holds. Signs reports on some accounts. |
| Andrew Silbernagel | Manager / account manager on most clients; **PPC lead**; web dev and security (Lovable site, WordPress fixes); builds Teamwork projects; approves blogs on some accounts (e.g. SPIEDR); posts the Automated Report Reviews. |
| Francis Marc Uy | **SEO desk**: SEO, blogs, GBP drafting and handoffs, schema, site edits, the Claude/Codex automations. Assigned SEO lead on report reviews. |
| Clarissa | Admin / operations: billing records, Teamwork, reports. |
| Brittni Woodson | Listed as "TP Lead" in several older channel topics (Wiseworth, MVP, AANMC, John Sadler, Aloha, Cleaning4U). Current client profiles name Andrew instead. *Confirm whether these topics are stale.* |
| Hubert ("Hubee") | Listed as SEO lead in the #cleaning4u topic. *Confirm current role.* |

**Tools of record** (from repo `CLAUDE.md`)
- **Semrush** (MCP) for SEO/traffic/competitive data, first choice when it can answer.
- **Google Workspace / Gmail / Drive** for docs and comms.
- **BrightLocal** (MCP): local rank, reputation, citations, AI visibility.
- **Make.com** (MCP `make-token`): blog and GBP publishing scenarios.
- **gbp-audit**, **gsc**, **google-ads-keywords**: local MCP servers (code in `mcp-servers/`), PC-only, not in cloud sessions.
- **Teamwork** (`thinkprofitscom.teamwork.com`): tasks and time logging per client. **Flowlu**: CRM. **Lovable**: our own site and new client builds. **CallRail**, **Cloudflare**, **Kinsta** (legacy hosting), **Elepass/password manager** for shared logins. Canva connector installed, not authorised.
- Search Atlas was trialled and **not recommended** (Andrew, 2026-08-07: inaccurate data and broken features).

## 2. Services we sell

Published on thinkprofits.com (checked 2026-10-07). These are list prices; real contracts vary (loyalty discounts, bundles, older rates). Figures are CAD, plus GST, management fees only (ad spend is billed separately by the platform).

| Service | Tiers (monthly fee + one-time setup) | Notes |
|---|---|---|
| **Think SEO** | Bronze $995 + $1,680 · Silver $1,895 + $1,950 · Gold $3,495 + $3,040 · Platinum $4,995 + $3,800 | Bronze covers up to 2 products/services. |
| **Think AEO** (includes GEO) | Same four tiers and prices as SEO | Newest line. Jamie Davis is the first AEO/GEO client (April 2026). Shawn also introduced an hourly "AEO – AI Engine Optimization" line at the SEO rate (Feb 2026). |
| **Think PPC** | Bronze $399 + $1,000 (up to $1K/mo spend) · Silver $699 + $1,200 (up to $5K) · Gold $999 + $1,500 · Platinum $1,499 + $2,000 | Clients own their Ads accounts. |
| **Think Web Leads** (websites) | Bronze $3,999 · Silver $6,999 · Gold $9,999 · Platinum $14,999 (one-time) | A "Web Sales Platinum" quote for SPIEDR was $19,999; custom AI lead qualification added at $2,000 on one quote. Lovable hosting ~US$50/month. |
| **AI Growth Audit** | $9,995 (one-time) | Mentioned on site FAQ. *Confirm scope.* |
| **Website support** | $249/month | Plugin/theme updates, monitoring, SSL. |
| **Web services retainer** | $1,500 minimum, time-tracked | "Web Services Retainer (Time Tracking Contract)" template in Drive. |
| Also listed | Content development, reporting dashboards, fractional marketing management, strategy consulting ("Parthenon Strategy" framework), e-commerce web design, domain registration | No published price found. |

**What clients actually pay (from client profiles, for context only)**
- SEO retainers seen: about **$999–$1,499/month** for Silver-level work (older 2023–2024 rates; SPIEDR's records conflict), Jamie Davis SEO + GEO Bronze bundle **$1,490/month** after a $500 loyalty discount, Wiseworth ~6 hours/month.
- PPC management seen: **$699–$999/month** (Jamie Davis Silver → Gold). Ad spend ranges seen: **~$900/month** (Munro & Crawford) up to **~$5,000–$7,500/month** (John Sadler, Vision).
- Bundles appear in channel purposes (e.g. "Plumbing Bundle": SEO Gold 10 h + PPC Silver + 1 blog/month + $249 support).
- Assumption when quoting: tier pricing above is the starting point; scope, discounts and ad spend change the total. Always present totals as ranges and confirm current rates with Shawn before quoting. Never promise results.

**Contract templates in Drive:** "Think Profits Client Service Contract" (e.g. Magellan Immigration, PPC Silver + SEO Audit, 2026-03-10; Onguard Solutions 2026), "Web Services Retainer (Time Tracking Contract) 2025", "Success Track" docs (per-client strategy docs, e.g. Vision Mechanical Success Track 2023). No standalone pricing sheet or proposal template was found in Drive search. *Confirm where the master versions live.*

## 3. Who we serve

- **Client types:** established small-to-midsize businesses, mostly **home and trade services** (plumbing/HVAC, towing, vac trucks, electrical, drainage, kitchens), plus professional services (law, immigration, accounting, dental), education/associations (AANMC, Mujo), B2B/industrial (Wiseworth, SPIEDR wildfire protection), e-commerce (MVP Athletic Supplies, Golf Ball Planet) and hospitality.
- **Geography:** headquartered in Vancouver; most clients are in **BC** (Lower Mainland, Fraser Valley, Okanagan, Interior), with others in Alberta/Saskatchewan and the US (AANMC is US/Canada; site says about 40% of work is national or cross-border).
- Site claims 3,500+ businesses served since 1996.

## 4. Competitors (our own SEO competitors)

Not pulled from Semrush this run (units at zero). From the "ThinkProfits Weekly SEO Optimization" reports:
- **Thrive** (Thrive Internet Marketing): 49 top-10 keywords vs our 14 in Semrush tracking (2026-10-05).
- Qualitative SERP competitors (2026-09-14 audit): **Vancouver SEO Agency, Digital Handshake Media, The Status Bureau, SEOh!, SAZ Consulting**.
- Their visible strengths: tracking-first PPC, geo-grid local reporting, recognisable brand proof, low-price AI positioning, executive GEO/AEO messaging. Our angle: proof discipline, published pricing, 30-year history, integrated SEO/PPC/local/AI measurement.
- *Action:* pull the competitor list from Semrush project 2029236 when units are back.

## 5. Our own site: SEO status

**Platform:** thinkprofits.com moved from WordPress on Kinsta to **Lovable** (served through Cloudflare) in 2026. Pre-rendering was handled by **Encited** (300-redirect plan limit vs 672 redirects in use, July 2026); Lovable added server-side rendering in Aug 2026 and the team planned a TanStack Start migration for true 301s (2026-08-19). *Confirm whether the TanStack migration is done and whether Encited is still needed.*

**What's on the site (sitemap, 2026-10-07):** 300 URLs: 181 blog posts (`/digital-news/`), 22 case studies, 22 AEO industry pages, 10 PPC industry pages, 20 `/seo-company-<city>/` and 20 `/ppc-agency-<city>/` pages, core service pages, a free SEO audit tool and a word counter. `llms.txt` is live (updated 2026-10-03); `robots.txt` explicitly allows AI crawlers. Schema: Organization, ProfessionalService, FAQPage, WebSite, Speakable.

**Search Console (live, 90 days to 2026-10-07):** 242 clicks, 374,131 impressions, CTR 0.06%, avg position 29.7. Avg position improved from ~38 (July) to ~20–28 (late Sept). Clicks are mostly branded or from the GBP link. `/seo-company-vancouver/` has 96K impressions and 15 clicks. Full detail: **[keywords.md](keywords.md)**.

**Semrush (weekly reports, project 2029236):** visibility 4.53% (2026-10-05, up 1.12 pts); 168 tracked keywords, 44 in the top 100, 14 in the top 10. Several PPC terms reached #1 in Sept. GBP: impressions -78% and website clicks -95% in one weekly comparison (2026-09-21). *Confirm against the Semrush UI.*

**Lead situation:** Shawn flagged a lack of inbound leads as the top company priority (meeting 2026-08-25) and said fixing the website is the most critical task.

**Site issues to know**
- Lost content after migration: blog posts and testimonials that weren't migrated lost impressions from mid-August. Plan: restore them on their original URLs (meeting 2026-08-25). Triage list: `data/_blog_triage.csv`.
- Cannibalisation and slash conflicts on SEO/web-design hub pages (see keywords.md section 6).
- `/pricing/` returns **404** but the homepage says "We publish all of our pricing". Prices live on each service page.
- Contact-form email broke on 2026-09-25; fixed 2026-10-03 with a daily Lovable watchdog posting to #thinkprofits-site-forms. A new alert on **2026-10-04** reported `notify.thinkprofits.com` as an unverified sending domain (3 emails refused). *Confirm resolved.*
- Spam/hack clean-up (July 2026): Cloudflare Turnstile, disposable-email blocklist, timing checks, tighter CORS on forms. Add Turnstile to any new form.

**Claims on our own site to review** (our standards say no guarantees and cite stats)
- Homepage FAQ: "Most clients see their first AI citations within 60–90 days" reads as a promised result. **Flag for revision.**
- "the longest in the market — our next-oldest competitor was founded in 2006" and "the only Vancouver agency whose work is taught in 250+ schools": need a source or softer wording.
- About page says the team "earned recognition from Ernst & Young's Entrepreneur of the Year program"; Shawn's bio says "nominee". Make them match.
- "$3M+" vs "$2M+" target-client revenue (see section 1).

## 6. Delivery workflows

| Workflow | How it works | Read |
|---|---|---|
| **GBP posts (brain/body)** | Saturday cloud routine drafts Mon + Thu posts for all 9 GBP locations and posts them to **#gbp-post-approvals** (`C0BVB0V2YEQ`). Team approves/corrects in threads. A Claude session turns approved drafts into `GBP-MAKE-HANDOFF/1` .md files in `gbp-handoffs/week-of-<Monday>/` (and `E:\ChatGPT\`); Francis uploads to Codex with "GBP APPROVED — PROCESS"; Codex writes to the Sheet and Make publishes. Claude never touches the Sheet or webhook. Our own location key: `thinkprofits_vancouver` (6 handoffs so far, Sept 14 – Oct 1). | `memory/gbp-brain-body-split.md`, `gbp-handoffs/claude-handoff-instructions.md`, `automations/codex-gbp-make-sheets-migration.md` |
| **Blog pipeline (Make.com)** | Approved Google Doc → Make cleans the HTML (order matters: bold/italic/links first, then strip spans) → WordPress draft with a native `<details>` FAQ accordion. FAQ schema is phase 2. Prep step uses the `blog-make-handoff` skill. Built on Aloha Life Massage. | `memory/blog-automation-faq-accordion-architecture.md`, `automations/Vision Blog Draft Publisher [TEST - INACTIVE].blueprint.json` |
| **Blog masterlist routines** | Planning run on the 25th audits the "BLOG Masterlist - 2024-2026" sheet, reads client Slack reports and DMs Francis proposed topics. A daily check drafts only after Francis replies "proceed" (expires after 7 days). ThinkProfits is in scope (quota 2/month, mostly inactive since 2024). | `scheduled-tasks/blog-masterlist-planning-run/SKILL.md`, `scheduled-tasks/blog-masterlist-draft-check/SKILL.md` |
| **Automated monthly report reviews** | Around the 9th, "🤖 Automated Report Review" posts land in each client channel (cc Andrew as manager, assigned SEO/PPC leads). The `seo-report-roadmap` routine finds new ones (dedupe file), and DMs Francis a per-client SEO roadmap. `slack_read_file` has been failing on the report attachments. | `scheduled-tasks/seo-report-roadmap/SKILL.md` |
| **Our own site: weekly SEO report** | A ChatGPT scheduled run posts "ThinkProfits Weekly SEO Optimization" (Semrush Position Tracking) to Francis's DM. The `weekly-seo-report-slack-check` routine forwards priority items to the Lovable project "thinkprofits". Daily content handoffs from ChatGPT ("Lovable-ready blog package") arrive in the same DM tagged @Claude. | `scheduled-tasks/weekly-seo-report-slack-check/SKILL.md` |
| **Slack → Lovable relay** | Weekday relay: ChatGPT-written instructions tagged @Claude in Francis's DM are forwarded to the "Thinkprofits Rebuild" Lovable project only after Francis replies "approved"; "rejected" kills them. Never forwards twice. | `scheduled-tasks/slack-to-lovable-relay/SKILL.md`, `automations/claude-code-slack-lovable-relay-setup.md` |
| **PPC hygiene bot** | "ThinkProfits Google Ads Bot" posts daily placement syncs and junk/TLD placement exclusions across the MCC to #thinkprofits-ppc-team. | Slack `C06MKQFTV50` |
| **Site monitoring** | Lovable daily check (9am Pacific) posts to #thinkprofits-site-forms only when form emails fail, enquiries go missing, the contact page fails, or a week passes with no enquiries. Plan to copy this for client Lovable sites. | Slack `C0990N9V3GV` |
| **Teamwork** | Each client has a Teamwork project/tasklist; log SEO, AEO, blog, PPC and support hours there. Since Sept 2026 Andrew uses a "combined" project per client (SEO, blogs, PPC, pages, support in one). | Links in each client's channel bookmarks |
| **Weekly team check-in** | Shawn, Andrew, Francis. Gemini notes + transcript land in Drive (example: `data/_doc_content.txt`, 2026-08-25). | Drive |

## 7. Standards (all clients)

Writing rules come from repo `CLAUDE.md`: Canadian English; conversational but professional, sharp wit welcome, no sarcasm or inside jokes; no jargon unless the client is technical; state target keyword and search intent on SEO deliverables; headers and bullets in proposals/reports; **never guarantee rankings or results** (flag such language); ad spend as ranges with assumptions; cite sources for stats.

- [Page-update doc format](../../memory/page-update-doc-format.md): Current | Replacement side by side, Keep/New Section labels, exact H-tags, internal links spelled out.
- [People Also Ask research](../../memory/paa-research-standard.md): always pull PAA questions into keyword research and FAQs.
- [Service page vs blog format](../../memory/service-page-vs-blog-format.md): service pages are scannable conversion layouts; build the docx with `--kind Page`.
- [Blog topic cannibalisation check](../../memory/blog-topic-cannibalization-check.md): check existing site content before proposing topics.
- [Core pages before niche pages](../../memory/strategy-core-pages-before-niche.md): low-authority domains fix core pages first.
- [Schema for non-medical therapy practices](../../memory/schema-type-nonmedical-therapy-practices.md): LocalBusiness + ProfessionalService, not MedicalBusiness.
- GBP image rules (in `memory/gbp-brain-body-split.md`): real client photos only, JPG/PNG, at least 400x300; use a full Chrome UA when checking Cloudflare-protected client sites.
- AEO/Wikidata work is factual and sourced only: no "award-winning", "industry-leading", "best" (Andrew's AEO SOP, see `clients/jamie-davis/CLIENT.md`).

## 8. Client roster

From `clients/*/CLIENT.md` (all DRAFT v0.1, Oct 2026) and the Slack channel list.

| Client | Folder | Domain | Semrush project | Slack channel | Status |
|---|---|---|---|---|---|
| AANMC | [aanmc](../aanmc/CLIENT.md) | aanmc.org | 3439424 | #aanmc `C019H89BB8T` | Active (paused Nov 2025 for non-payment, resumed Feb 2026; payments behind again per Aug 2026 meeting, *confirm*) |
| Aloha Life Massage | [aloha-life-massage](../aloha-life-massage/CLIENT.md) | alohalifemassage.com | 10922418 | #aloha-life-massage `C04DKPZSRUH` | SEO/blogs paused since 2026-06-17 (budget moved to new site build) |
| Clearset VAC Truck | [clearset](../clearset/CLIENT.md) | clearsetvactruck.ca | 10336170 | #clearset `C04BXUMV0ES` | Active (SEO Silver + PPC Bronze) |
| Jamie Davis Towing | [jamie-davis](../jamie-davis/CLIENT.md) | jamiedavistowing.com | 30290458 | #jamiedavistowing `C07TS2LMF9T` | Active (SEO + GEO Bronze, PPC Gold) |
| John Sadler Plumbing & Heating | [john-sadler](../john-sadler/CLIENT.md) | johnsadler.ca | 2824033 | #johnsadler `C019H8FNN9H` | Active (SEO, PPC, 2 blogs/month) |
| Munro & Crawford | [munro-crawford](../munro-crawford/CLIENT.md) | munrocrawford.ca | 3545954 | #munrocrawford `C019AAP51U6` | Active (SEO + PPC) |
| SPIEDR | [spiedr](../spiedr/CLIENT.md) | spiedr.com | 2084675 | #firestorm_spiedr `C01928K8M0F` | Active (SEO Silver, 1 blog/month) |
| Vision Plumbing Heating Cooling | [Vision](../Vision/CLIENT.md) | visionplumbingandheating.com | 11470309 | #vision-plumbing `C052P7H4FUG` | Active (Plumbing Bundle: SEO + PPC) |
| Wiseworth Canada Industries | [wiseworth](../wiseworth/CLIENT.md) | wiseworth.com | 2049406 | #wiseworth `C019E04B2AZ` | Active (SEO ~6 h/month) |
| MySaskFarm | [mysaskfarm](../mysaskfarm/CLIENT.md) | mysaskfarm.com | 30622784 (no live tracking campaign) | #mysaskfarm `C0BGPH5JSKT` | Active (new July 2026) |
| Mujo Learning Systems | [mujo](../mujo/CLIENT.md) | mujo.com | 2160205 (dupes 24450287, 14590131) | #mujo `C019H2Q5HS6`, #think-mujo `C07QWJWGSLD` | Active (sister company / client) |
| MVP Athletic Supplies | [mvp](../mvp/CLIENT.md) | mvpathleticsupplies.com | 2049385 | #mvp `C019AAJKPK8` | Active (Shopify; SEO + GBP) |
| ThinkProfits (us) | [thinkprofits](CLIENT.md) | thinkprofits.com | 2029236 | #tpmarketing `C019H9PQ9BM` | Internal |

**Other client channels in Slack (no repo profile, status unknown):** #golfballplanet, #overseas5 (canadaintercambio.com), #tsawwassenfamilydental, #nam (musicschoolmississauga.com), #mcmullen-plumbing, #hoh-kitchens, #aglonsite-hireair, #waywest-mechanical (private; active PPC per the Ads bot), #cleaning4u (active PPC per the Ads bot), #nova-hypnosis, #arbor-green-tree, #prowest-heating-and-air-conditioning, #zone-west, #inspira-lifestyles, #magellan-immigration, #drainage-pro, #powerup-electric, #on-guard (Onguard Solutions, PPC report review). Waywest, ProWest and Cleaning 4 U are out of scope for the blog routines.

**GBP pipeline location keys (9):** `thinkprofits_vancouver`, `john_sadler_surrey`, `wiseworth_surrey`, `vision_kelowna`, `mvp_langley`, `jamie_davis_hope`, `munro_crawford`, `clearset_port_coquitlam`, `spiedr`.

## 9. Known tool issues (as of 2026-10-07)

- **Semrush API units balance hit zero on 2026-10-07.** Earlier runs (2026-10-06) already returned "unable to charge units". Don't call `execute_report`; use repo exports and the Semrush UI until topped up. Position Tracking via API also returns "campaign not found" for some projects (Aloha, Jamie Davis).
- **Gmail connector:** broken / needs re-auth; client emails and approvals in Gmail haven't been checked by any profile run.
- **BrightLocal MCP:** returns a schema error on every call tried; Vision's rank tracker also stalled since July 2025.
- **gbp-audit MCP:** hard-blocked at 0 requests/min (Google Cloud quota). Needs GBP API access approval. See `memory/gbp-audit-quota-blocked.md`.
- **GSC access gaps:** the `gsc` MCP is signed in as the agency account (96 properties). Gaps found: `sc-domain:jamiedavistowing.com` returns 403. Local only, not in cloud sessions. Re-auth steps: `memory/gsc-mcp-thinkprofits-auth.md`. The ChatGPT "GSC Wizard" connector returns `payment_required`.
- **Slack:** `slack_read_file` fails on report attachments (invalid_union); ChatGPT's scheduled runs can't upload files to Slack.
- **Encited redirect cap** (300 on current plan vs 672 redirects).
- Local servers (`gsc`, `google-ads-keywords`, `gbp-audit`) only run on Francis's PC. Google Ads Keyword Planner MCP works (Basic access approved 2026-09-30; see `memory/google-ads-keyword-planner-mcp.md`).

## 10. Social profiles and channels

- Facebook: facebook.com/ThinkProfits
- Instagram: instagram.com/thinkprofits
- LinkedIn: linkedin.com/company/think-profits-com-inc/
- YouTube: youtube.com/@thinkprofits
- Google Business Profile: Vancouver location (5.0, 48 reviews per site); GBP link carries `?utm_campaign=gmb&utm_medium=organic&utm_source=gmb_listing`.
- Blog: thinkprofits.com/digital-news/
- Shawn asked for the Lovable partner announcement to go out on LinkedIn and Facebook (2026-08-15). *Confirm posted.*

## 11. Working rules and IDs

| Item | Value |
|---|---|
| Semrush project (our site) | **2029236** (from brief; not verified this run) |
| GSC property | `sc-domain:thinkprofits.com` |
| Google Ads MCC | Think Profits MCC 362-716-7231; self account 2916941762 |
| Lovable project | "thinkprofits" / "Thinkprofits Rebuild", `12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17` |
| Blog masterlist sheet | `1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw` (ThinkProfits tab) |
| GBP queue sheet | `1MFFDsfa4aVvVqqR1wpfNrRsQ-EzhSwZ10QjaD87-Nto` (Codex/Make only; don't edit) |
| GBP location key | `thinkprofits_vancouver` |

**Slack channel map (internal)**

| Channel | ID | Use |
|---|---|---|
| #tpmarketing | `C019H9PQ9BM` | Our own site and marketing (Lovable, redirects, forms, partner badges) |
| #seo | `C05MW75SUM8` | SEO team chat; weekly Slackbot checklist reminders |
| #thinkprofits-ppc-team | `C06MKQFTV50` | Google Ads bot (placement syncs/exclusions) |
| #gbp-post-approvals | `C0BVB0V2YEQ` | GBP drafts and approvals (source of truth) |
| #thinkprofits-site-forms | `C0990N9V3GV` | Site enquiries and watchdog alerts |
| #team-chat | `C016T5AJSM9` | Company-wide (quiet in last 3 months) |
| #automation-innovation | `C092P0Z8W2X` | Automation ideas |
| #n8n-keywords, #seo-keyword-research, #local-keyword-data | `C092J29B23G`, `C092KSD918Q`, `C09AWTCDGAX` | Keyword data feeds |
| #aisavvy | `C0AKA9KJGG3` | AI Savvy sister brand |
| Francis's DM | `D06U5NPDEQ6` | Routine output, weekly SEO reports, relay instructions |

**Rules**
- ThinkProfits work lives in this repo only; no other agency or personal content.
- Pull before work, commit and push after (repo `CLAUDE.md`). Never commit secrets.
- Claude never edits the GBP Sheet or calls Make webhooks directly.
- Client approvals and billing holds follow each client's CLIENT.md; Shawn decides account holds.

## 12. Open items

**Security (business accounts)**
- [ ] **A staging-site password is written in plain text in the #aglonsite-hireair channel topic.** Remove it from the topic and rotate it.
- [ ] Two Google Workspace accounts had **no 2FA** (`admin@thinkprofits.com`, `shawn@thinkprofits.net`) and 2FA isn't enforced org-wide (Andrew, 2026-08-14). *Confirm fixed.*
- [ ] `notify.thinkprofits.com` unverified sending domain (watchdog alert 2026-10-04). Finish DNS verification.
- [ ] Opt out of Lovable's model-training data collection on every team account (terms changed 2026-09-09; Francis confirmed his is off). *Confirm Shawn and Andrew.*
- No credentials were found in the repo files read for this profile.

**Our site**
- [ ] Fix `/seo-company-vancouver/` (96K impressions, 15 clicks): title/snippet, page ownership vs `/seo-services/` and `/services/`.
- [ ] Restore lost blog posts/testimonials on original URLs (`data/_blog_triage.csv`: 45 KEEP, 119 MAYBE).
- [ ] Resolve `/pricing/` 404 (redirect to a pricing hub or remove the claim).
- [ ] Revise the "first AI citations within 60–90 days" FAQ line and source the "longest-running"/"only agency" claims.
- [ ] Decide on the TanStack Start migration and Encited.
- [ ] Pull Semrush competitors and PAA once units are restored.
- [ ] ThinkProfits blog masterlist tab is mostly inactive since 2024 (2/month quota); the Sept 25 planning run proposed 4 AEO/Wikidata/schema topics awaiting "proceed".

**Agency**
- [ ] Top up Semrush API units; re-auth Gmail; fix BrightLocal MCP; get GBP API quota raised.
- [ ] Build profiles for MVP and Mujo; add Semrush IDs for MySaskFarm, Mujo, MVP.
- [ ] Update stale "TP Lead" channel topics (Brittni) if she's no longer on those accounts.

## 13. Gaps and conflicts

- **Blog-masterlist routine maps "ThinkProfits" to `C05MW75SUM8` (#seo)**, but our site channel is #tpmarketing `C019H9PQ9BM`. Reports for our own site actually arrive in Francis's DM.
- **Target client revenue:** $3M+ (homepage, footer) vs $2M+ (About).
- **Primary email:** clientcare@ (schema, forms) vs info@ (About page).
- **EY:** "recognition" vs "nominee".
- **SPIEDR retainer:** $1,499 Silver (Teamwork) vs "$999 plus blog" (Shawn); list price for SEO Silver is now $1,895. Older clients are on legacy rates.
- **Clearset PPC Bronze** caps spend at $1,500 in the contract, but the published Bronze tier caps at $1,000 and actual spend was ~$3.08K/month.
- **Semrush project 2029236** comes from the brief only; not verified in the repo or via API.
- **AEO/GEO topics xlsx** (`data/AEO & GEO Blogs and PR Topics.xlsx`, 90 blog + 56 PR topics) is a generic `[Company Name]` template written for a direct-marketing/customer-acquisition company, not for ThinkProfits. Treat it as a reusable reputation/AEO topic template; confirm which client it was built for.
- **Client status** for the ~18 channel-only clients is unknown; Flowlu (CRM) wasn't checked.
- No pricing sheet, proposal template or Success Track template was found in Drive search; contract PDFs exist per client.
