# Aloha Life Massage: client profile

> **Status:** DRAFT v0.1, 2026-10-06. Pending review by Francis.
> **Sources:** Slack (#aloha-life-massage C04DKPZSRUH, Andrew/Shawn/Clarissa DMs and group DMs), Drive (Jun 17 2026 meeting notes, 2023 contract, Success Track, Website Audit sheet, Blog Automation Feed, blog docs), Make (scenario 6189592 blueprint, scenario list), Semrush (project 10922418, US database), GSC (`https://alohalifemassage.com/`), live site, repo.
> **Not checked:** Gmail (connector broken), BrightLocal (tool returned a schema error), Semrush Position Tracking (API says "campaign not found" for 10922418), the Sept 2026 monthly report PDF (Slack file unreadable through the API).
> **Related files:** [keywords.md](keywords.md), [memory/blog-automation-faq-accordion-architecture.md](../../memory/blog-automation-faq-accordion-architecture.md), [memory/schema-type-nonmedical-therapy-practices.md](../../memory/schema-type-nonmedical-therapy-practices.md), `.claude/skills/blog-make-handoff/SKILL.md`.
> Facts marked *confirm* are unverified. Don't use them client-facing until checked.

**Read this first: the account is in a holding pattern.** On 2026-06-17 the client agreed to stop PPC and move the SEO and blog budget into building a new "Aloha Life Mobile Spa" website. Andrew confirmed on 2026-07-09: "we are putting all hours towards the new site build", and no new blog topics are needed. Monthly reports still arrive and still need a read-and-reply. Don't start new SEO, blog or ads work without checking with Andrew or Shawn.

## 1. Client overview

**Business**
- Mobile massage service on Maui, Hawaii. Massage therapists travel to hotels, condos, vacation rentals, homes and (per the site) yachts. No studio.
- Trading name: Aloha Life Massage. Schema and GBP-style name on the site: "Aloha Life Massage / Maui's Best Mobile Service".
- **Rebrand in progress:** "Aloha Life Mobile Spa", adding facials and waxing (meeting 2026-06-17). New domain discussed as alohalifemobilespa.com. As of 2026-10-06 that domain **301-redirects to alohalifemassage.com**, so the new site isn't live on its own domain yet.
- "Serving Maui since 2019" (agreed hero H1 for the new site).
- Website: https://alohalifemassage.com
- Phone: (808) 649-9777 (confirmed as the correct number 2026-06-17; matches the live site)
- Location: Kihei, HI 96753. The live schema publishes a full street address including a unit number. *Confirm whether that should be public for a service-area business* (section 13).
- Hours: the site's two schema blocks disagree (8:00–18:00 vs 9:00–17:00, 7 days). "7 days a week by reservation" per the 2026-06-17 notes. *Confirm.*
- Timezone: Hawaii (HST, UTC−10, no daylight saving). Maui is 3 hours behind Vancouver during Pacific daylight time and 2 hours behind in winter.

**Relationship**
- Channel created 2022-12-01. Strategy session agenda Dec 2022.
- ThinkProfits built the current WordPress site in 2023 (custom web development contract, US$9,569.90 less 5% prompt-pay discount; launch approval Aug 2023).
- Ongoing SEO, blogs and PPC since then. Current retainer and contract term not found.
- **Shawn Moore (TP President/CEO) runs the relationship directly with Dani** and makes decisions alongside her in meetings. Treat Shawn as the escalation point for scope and budget.

**Client contacts**
- **Dana "Dani" Burianova:** owner and founder. Approver. Also a working massage therapist (named in reviews). Blog author byline is "Dani" (Andrew, 2026-07-09). Her email on file is a personal address; not reproduced here.
- Other massage therapists named in public reviews: Hakem, Tiffany. *Roles not confirmed.*
- Email: Dani said 2026-06-17 she doesn't use the old aloha email address, and it was to be removed from the site. No business email is published.

**ThinkProfits team**
- Shawn Moore: President/CEO, relationship owner, leading the new-site build
- Andrew Silbernagel: account manager and PPC lead, reviews and edits all blogs
- Francis Marc Uy: SEO lead, blog writer
- Clarissa (Admin): admin, Teamwork projects
- Brittni Woodson: listed as TP lead in the channel topic and Success Track (2024). *No longer active on the account; update the channel topic.*

**Stack** (live site, 2026-10-06)
- WordPress 7.1.2, Rishi theme (rishi-pro / rishi-companion), Elementor 4.2.2, Mega Elements, Smart Slider 3, Cost Calculator Builder, Widget for Google Reviews
- Yoast SEO (per memory; Yoast fields mapped in Make)
- Bookings: Acuity (per the 2026-06-17 notes)
- Hosting: Kinsta (2023 screen captures reference "aloha-kinsta"). *Confirm still current.*
- WooCommerce leftovers in the sitemap: /shop/, /cart/, /checkout/, /my-account/, /best-deals/, /sample-page/
- New site prototype: built in Lovable by Shawn (meeting 2026-06-17)

## 2. Services: what they do and don't do

**What they do** (live site, 2026-10-06)
- Massage modalities: Swedish, Therapeutic, Deep Tissue, Lomilomi (Hawaiian), Sports, Hot Stones
- Premium / VIP mobile massage
- Couples massage and group bookings (2 to 50+ people)
- Add-ons, gift certificates
- Lymphatic drainage and prenatal massage are covered in blogs. *Confirm both are bookable services* (the lymphatic blog is the site's best non-brand organic page).
- **Packages** (homepage, 2026-10-06): Bronze $149/60 min, $199/90; Silver $175/60, $235/90; Gold $249/75, $299/105; Platinum $499/120, $569/150. All include travel and setup. Prices are in USD.
- **Coming with the rebrand** (2026-06-17): facials limited to 4 programmes (classical, hydrating, anti-aging, microneedling); waxing including Brazilian and bikini, with a **$150 minimum booking for wax-only appointments**. Retreats page "Coming Soon", January 2027, no firm dates. *None of this is on the live site yet.*

**What they don't do**
- **Side-by-side couples massage.** Dani said couples imagery implies side-by-side availability, "That's not case" (2026-06-17). Couples bookings exist, but don't promise simultaneous side-by-side treatment. *Confirm exactly what the couples offer is.*
- **Evening appointments** aren't standard. Avoid night-time imagery that implies 7 pm bookings (2026-06-17).
- Couples facials and back facials (removed from the new menu).
- Concierge / private chef services: shelved to "phase 2".
- **Areas not served:** Hana, Wailuku and Kahului (2026-06-17); Hana and Nahiku excluded since 2025-03-22. No Oahu, Big Island or other islands.
- Studio or spa visits (fully mobile).

**Regulatory**
- **This is Hawaii, not BC.** CMTBC/RMT advertising rules don't apply. Massage therapists and massage establishments in Hawaii are licensed by the Hawaii Board of Massage Therapy (HRS Chapter 452). Hawaii is understood to require the licence number in massage advertising. *Confirm the exact rule and get Dani's therapist and establishment licence numbers before writing ads or claims.*
- The site says therapists are "licensed and insured" and the homepage says "certified". *Confirm the licence and insurance claims are accurate for every contractor.*
- **Health claims:** keep benefits general and hedged ("may help", "many people find"). No treatment, cure or diagnosis claims, and nothing medical in lymphatic drainage, prenatal or post-dive content. Andrew added "proportionality context around DCS risk" to the scuba blog (2026-06-23); follow that model.
- **Never write "therapist" or "therapy" alone.** Always "massage therapist" or "massage therapy" (Andrew, 2025-11-13, repeated 2025-12-13 and 2026-05-30). Plain "therapist" reads as mental-health or physio and can confuse readers, Google and AI.
- Schema: this is a non-medical practice. Use `["LocalBusiness", "ProfessionalService"]` or `HealthAndBeautyBusiness`, never `MedicalBusiness` (memory: schema-type-nonmedical-therapy-practices). The live site currently stacks LocalBusiness and HealthAndBeautyBusiness (section 5).

## 3. Target market and geography

**Who they serve:** vacationers (couples, honeymooners, wedding parties, families, babymooners, divers, golfers, snowbirds) plus local residents. Upscale positioning; the client wants the brand to read "more upscale" (2026-06-17).

**Priority areas** (client, 2025-03-22, and audit sheet)
1. Wailea / Makena / Wailea-Makena (high spending, client priority)
2. Kapalua (high spending, client priority)
3. Kihei (home base; strongest local rankings)
4. Lahaina / Kaanapali / Napili / Kahana (West Maui)
5. Paia, Makawao and Upcountry. *Not explicitly listed; confirm.*

**Do not target:** Hana, Nahiku, Wailuku, Kahului (see section 2). The live site FAQ and schema still list Kahului and Wailuku, which needs fixing. "All of Maui" wording must change to "the island of Maui" / "the majority of Maui" (client, 2026-06-17).

**Search traffic** (GSC, 2026-07-08 to 10-05): USA 534 clicks, Canada 9, everything else negligible. Semrush database = **US**.

**Context:** Maui tourism has been down since the 2023 fires. Shawn cited a 40% drop in March 2025 (unverified; Andrew flagged it as unverified at the time). Don't quote that number client-facing without a source.

## 4. Competitors

| Domain / name | Notes | Source |
|---|---|---|
| mauideeptissuemassage.com | Near-parity visibility with Aloha in May 2026 (26.02% vs 26.73%), still gaining; held steady in July | Automated report reviews, 2026-06-25 and 08-08 |
| mauipremiermassage.com | Dani believed it outranks Aloha (Mar 2025); team doubted it. Mentioned in a Feb 2026 draft at "starting around $250" | Slack 2025-03-22, 2026-02-03 |
| "Mobile Massage Maui" (GBP) | Running sponsored Maps ads as of Jun 2026 | Meeting 2026-06-17 |
| "Maui Mobile Massage" | Named in a rejected blog draft | Slack 2026-02-03 |
| Resort spas (e.g. Four Seasons Wailea) | Positioning foil: mobile vs hotel spa | Blogs, audit sheet |

**Rule:** never list or recommend competitors in content. If competitors ever appear, it must be a deliberate "best of" piece that clearly positions Aloha first (Andrew, 2026-02-03).

Semrush competitor visibility wasn't pulled (Position Tracking API failed). *Pull it from the Semrush UI.*

## 5. Current SEO status

**GSC** (`https://alohalifemassage.com/`, 2026-07-08 to 10-05)
- 559 clicks, 17,738 impressions, 3.2% CTR, avg position 13.4
- `sc-domain:alohalifemassage.com` returns 403. Use the URL-prefix property.
- Impression spikes on 07-14, 08-12 and 09-15/16 (800–1,200/day vs ~150 normal) with low CTR. Probably bot or SERP-feature noise. *Check.*

**Top pages, 90 days**

| Page | Clicks | Impressions | Avg pos |
|---|---|---|---|
| /?utm_source=google&utm_medium=organic&utm_campaign=GMB (GBP link) | 241 | 4,500 | 7.3 |
| / | 213 | 9,073 | 13.9 |
| /blog/health/lymphatic-drainage-massage-maui-benefits/ | 62 | 933 | 6.9 |
| /services/lomilomi-mobile-massage/ | 13 | 572 | 28.1 |
| /meet-the-team/ | 6 | 1,615 | 8.2 |
| /services/ | 2 | 1,940 | 7.6 |

Service pages barely earn clicks: Deep Tissue (pos 31.4), Swedish (43.8) and Group Bookings (67.3).

**Semrush (US database, 2026-10-06):** 116 organic keywords, ~123 estimated monthly visits, 0 paid keywords. About 72% of estimated traffic is the brand query.

**Monthly report trend** (automated reviews in Slack)
- **May 2026:** visibility −10.70% MoM; "mobile massage near me" #1 → #7; 4 top-3 positions lost; Singapore bot traffic (187 users, 0 events).
- **June 2026:** "deep tissue massage" #2 → unranked; avg position 26.03.
- **July 2026:** visibility −7.6 pts; 16 keywords down vs 4 up; swedish massage, therapeutic massage, deep tissue massage maui, swedish massage therapy all fell.
- **August 2026:** avg position 27.97 → 20.00; 14 up, 3 down; 5 new top-3s; organic sessions +10.5% MoM; GSC impressions −45.6% YoY.
- **Key events down ~90% YoY in every channel** (Jun–Aug). Flagged every month as a likely tracking gap. Not investigated (all hours are on the new site).

**GBP:** 5.0 stars, 257 reviews (Aug 2026 report); 0 new reviews in August. Impressions +27.9% YoY, calls +733% YoY, direction requests −54.1% YoY. GBP is linked with GMB UTM tags.

**Live-site technical notes** (2026-10-06)
- Two H1s on the homepage ("Maui's Very Best Mobile Massage Therapists" and "Experience Ultimate Relaxation Best Mobile Massage Maui").
- Three overlapping business schema blocks: a LocalBusiness block named "Aloha Life Massage / Maui's Best Mobile Service" (8–6 hours), a HealthAndBeautyBusiness block (9–5 hours, full street address), plus Yoast's graph. Consolidate to one.
- The homepage FAQPage schema contains broken escaped HTML (a literal `<h3>` leaked into an answer).
- /service-areas/ returns 404; there are no location pages yet. Location-page keyword research exists (audit sheet, Jan 2026).
- WooCommerce and sample pages are still in the sitemap.
- The two June 2026 blogs still sit under /blog/uncategorized/ even though Andrew asked for categories and Francis marked it done (2026-08-06). *Confirm.*
- **Brand-safety issue:** the site ranks and gets some clicks for adult-intent queries (erotic, sensual, nuru, "happy ending" massage Maui). See keywords.md section 4.

### Keywords

Full detail is in [keywords.md](keywords.md) (2026-10-06).

**What's tracked:** Semrush project 10922418 has Position Tracking enabled, but the API returns "campaign not found", so the tracked list couldn't be pulled. The monthly reports show the campaign exists (local, Maui). *Export it from the Semrush UI.*

**Where we stand (Semrush US organic + GSC)**

| Keyword | Position | Note |
|---|---|---|
| maui mobile massage | 2 (Semrush) / 18.7 (GSC avg) | Core money term |
| mobile massage maui | 3 / 28.2 | Core money term, 587 impressions |
| lymphatic drainage massage maui | 2 / 5.3 | Best non-brand performer (blog) |
| maui massage (1,900/mo) | 31 | Biggest volume gap |
| couples massage maui (480/mo) | 38 | Watch the side-by-side rule |
| massage kihei / kihei massage | 12–14 (GSC) | Home-base local terms |

**Flags**
- Out-of-area: the Lomilomi page ranks for Oahu, Waikiki and Honolulu terms. Not served.
- Excluded areas: audit-sheet location research includes Kahului terms. Kahului is now excluded.
- Job terms ("massage therapist jobs") map to /join-our-team/: fine for recruiting, not for lead tracking.

## 6. Current marketing programme and scope

**Status since 2026-06-17: paused / redirected**
- **SEO and blogs:** budget moved to the new-site build. "We don't need the new topics since we're working on the new site instead" (Andrew, 2026-07-09). The blog-masterlist planning task skips Aloha ("paused"). Shawn floated pausing local SEO for Aloha on 2026-06-18.
- **PPC:** client agreed to stop paying for PPC (2026-06-17). Andrew: "Ads minorly dealt with. Pausing soon anyways" (2026-07-09). *Confirm the ads are paused.*
- **Reporting:** the automated monthly report and Slack review continue. Francis must still read each one and reply in-thread. **The Sept 2026 review (posted 2026-09-09) is still unacknowledged** after two bot follow-ups.
- **New site:** Shawn building in Lovable with SEO team support. Plan: launch on the new domain, keep the old site live until validated, protect GBP reviews and rankings.

**Before the pause** (Oct 2025 – Jun 2026)
- Blogs: about 1 per month, drafted by Francis, edited by Andrew, then client approval. Published by Francis or Andrew.
- GBP: a longer GBP post is a required deliverable for every blog (Andrew, 2026-02-03). Aloha is **not** on the Mon/Thu GBP automation (no location key in `gbp-brain-body-split`).
- On-page: FAQs and "Why Choose Us" sections added to the service pages (Jan 2026); citations added (Feb 2026); location-page keyword research (Jan 2026).

**Pricing:** retainer not found. Success Track (2022–2024) lists a starting marketing budget of $600–700 (currency and whether that's fee or ad spend unclear, *confirm*).

**Project tracking:** Teamwork project 1133313 ("ready for use again", 2026-04-29); earlier tasklist 3642852 (Oct 2025). Log time against it.

## 7. PPC overview

**Status:** being paused or paused (see section 6). No Google Ads data in the reports, and Semrush shows 0 paid keywords (2026-10-06).

**History**
- 2023: ad copy and performance doc (Oct 2023).
- 2024-10-25: PMAX approved at **$5/day** (Chris's recommendation).
- 2024-11-26 (Andrew): fixed PMAX targeting, turned off auto text, added cross-negatives, made the brand name a negative, and removed inappropriate keywords ("hot female massage therapist", "pretty massage therapist near me"). Asked whether ads should run 24/7.
- 2025-03-22: spend raised to **$600 for 30 days**; Hana excluded from ad geo.
- 2026-05: Paid Search relaunched (12 key events in May), then fell 97% YoY by June.
- 2026-07-07: Shawn asked Francis to check "what's going on with Aloha google ads".

**If ads restart:** present budget as a range with stated assumptions (e.g. US$5–20/day depending on season and conversion tracking), not a fixed promise. Exclude Hana, Nahiku, Wailuku and Kahului. Keep the adult-intent negatives. Fix conversion tracking first.

## 8. Content guidelines

**Approval flow:** Francis drafts → Andrew edits → client (Dani) approves → publish. Never publish without approval.

**Hard rules** (all from Andrew's edits unless noted)
- "Massage therapist" / "massage therapy", never "therapist" or "therapy" alone. "Therapeutic" is fine.
- Hyper-local Maui angles only. No generic global topics (Shawn, 2024-11-22; client, 2025-03-22).
- Don't name or link competitors (2026-02-03).
- Frame same-day / last-minute availability as "possible" or "likely", **never guaranteed** (2025-12-13).
- Reduce gendered wording in wedding and couples content ("wedding party", "newlyweds", "couple").
- Every blog needs: a Quick Answer paragraph after the intro (styled like the stiff-neck blog); an FAQ section with topic-specific questions; at least one service-page link and one other-blog link; a category; Dani as author; a longer standalone GBP post.
- Strip "image placement notes" before sending to the client.
- No couples-side-by-side imagery or claims, no evening/night imagery, no AI images of places that aren't Maui (2026-06-17).
- Check for duplicate topics against existing posts before pitching (Oct 2025 topic duplicated a June 2025 post).
- Use "Serving Maui since 2019" and "the island of Maui", not "all of Maui".
- US English is appropriate on client-facing copy for this US client. *Confirm with Andrew* (agency default is Canadian English).

**Voice:** warm, upscale, island-relaxed ("Aloha, E Komo Mai"), trustworthy. Wit is fine; nothing cheeky that could read as adult-adjacent.

**Pipeline formatting** (Make blog automation, see section 11): no H1 in the Doc body, exact H2 "Frequently Asked Questions" with H3 questions, SEO meta in the sheet only.

## 9. Key priorities and strategic notes

1. **New site and rebrand** (Shawn-led). The SEO risks to manage:
   - A domain move needs a full 301 map, GSC change of address and GBP website update.
   - Running two live sites risks duplicate content. Keep the new one noindexed until cut-over, or keep the old one canonical.
   - Two GBPs: Andrew recommended (2026-07-08) a second GBP named "Aloha Life Mobile Spa" with a different address, category and website, and ideally a unique phone number (shared phone = duplicate-listing risk). *Decision not recorded.*
   - Carry the "therapist" rule, area exclusions and new service list into the new site.
2. **Conversion tracking.** Key events down ~90% YoY across all channels for 3+ months. Fix before relaunching ads or judging SEO.
3. **Brand safety.** Adult-intent rankings and clicks (keywords.md §4).
4. **Fix area claims on the live site.** Remove Kahului and Wailuku from the FAQ and schema; change "all of Maui".
5. **Local pages** for Wailea/Makena, Kapalua, Kihei and Lahaina/Kaanapali once the new site exists (keyword research done Jan 2026).
6. **Strategic read:** brand and GBP drive most clicks. Non-brand rankings are thin outside "mobile massage maui". The best content asset is the lymphatic drainage blog. Leads were already down in Mar 2025 despite traffic gains; the client attributes that to tourism and pricing.

## 10. Social profiles and other channels

- Facebook: facebook.com/AlohaLifeMassage
- Instagram: @alohalifemassage. In Nov 2024 it was empty and the bio linked to an old, non-forwarding site. *Confirm fixed.*
- Reviews: Google (5.0, 257). Review widget currently a paid plugin; the client wants a free replacement on the new site (2026-06-17).
- Referral partner mentioned: a concierge service (Epicured), per the 2026-06-17 meeting. *Confirm name.*
- No email marketing known.

## 11. Working rules and tool IDs

**Approvals**
- Content: Andrew edits, Dani approves.
- Scope and budget: Shawn.
- Reports: reply in the bot thread ("read: content accurate" is enough) per Andrew, 2026-07-09.

**Standing rules**
- "Massage therapist", never "therapist"
- No Hana, Nahiku, Wailuku, Kahului
- No competitors in content
- No guaranteed same-day availability
- No side-by-side couples or evening claims
- No medical claims

**Tool IDs**

| Tool | ID |
|---|---|
| Semrush | **10922418** ("Aloha life Massage", alohalifemassage.com). Tools: Site Audit, Backlink Audit, Position Tracking, SEO Ideas, GA/GSC. Position Tracking API returns "campaign not found". |
| GSC | `https://alohalifemassage.com/` (works). `sc-domain:alohalifemassage.com` → 403. |
| Slack | #aloha-life-massage C04DKPZSRUH. Not in #gbp-post-approvals automation. |
| Teamwork | Project 1133313; tasklist 3642852 (Oct 2025) |
| GBP automation key | None (not on the Mon/Thu pipeline) |

**Make.com blog pipeline** (team 2871706, zone us2.make.com)

| Item | ID / value |
|---|---|
| Production scenario | **6189592** "Aloha Life Blog Draft Publisher": **inactive and flagged invalid** (last edit 2026-09-08). Description still says "ACTIVE PILOT", every 15 min. |
| Test scenario | 6194333 "Aloha FAQ Accordion Publisher [TEST - INACTIVE]", on-demand |
| Inspection tools (exist, not run) | s6189656 inspect_aloha_blog_sheet_results, s6193765 verify_aloha_faq_test_draft, s6193774 inspect_aloha_blog_google_doc_export |
| Feed spreadsheet | `1pn-1J7PENZD3ZYIwn_s9qZAdfBK2yS9ZcqTJg8bGqU0` "Aloha Life Massage — Blog Automation Feed". Now **shared by all pipeline clients** (tabs: Aloha, John Sadler, Vision, SPIEDR, Jamie Davis). |
| Sheet tab | Tab is now named **"Aloha"**, but scenario 6189592 still points at `sheetId: "Untitled"`. Probably why it's invalid. *Confirm.* |
| Columns (A:L) | A Post Title · B SEO Meta Title · C SEO Meta Description · D Slug · E Status detail (Processing / Draft Created / Skipped - Slug Exists) · F Blog Google Docs Link · G Image URL · H WordPress Post ID · I Draft URL · J **trigger** ("Ready to Publish" → "Drafted") · K unused · L Error Message |
| Make connections | Google 10937775; WordPress (alohalifemassage.com) 10938499 |
| Sheet rows | Row 2: scuba blog → WP draft 8075 (since published). Row 3: test post → WP **draft 8079, still in WordPress**; delete it. |
| Drive: client folder | `1vDgMjk0LvSHNz7UX-n3UVPDTcew_mNla` "Aloha Life Massage" (holds the feed sheet and audit sheet) |
| Drive: blog docs folder | `1vJR5ejj_TI5_FtaalMJRT78WUsvlWNbW` (all 2025–2026 blog docs) |
| Pipeline status | Francis to Andrew, 2026-09-09: "works well now just a little tweak on FAQs and some automation optimization". The FAQ schema phase is still deferred. |

**Drive**

| File | ID |
|---|---|
| Website Audit (KW mapping, location KWs, blog silos) | `1r1CcYLgvdJvmqGfi1E8OWz3neJJsSTpOnlQFLAqrQ9Y` |
| Meeting notes + transcript, 2026-06-17 (rebrand decisions) | `17kGFFyfUsHUlnyqjspK8laXyG_Do7Luz_eU5Uw2zQGI` |
| Client Service Contract 2023 (web build) | `1fqA7K6uuTGuSTLpQszGmQW8A67sJYfJKXReJ6xVsepg` |
| Change Order 2023-02-13 | `1_HCXnbzWFZVbPRFcaVaqThi3il0oLA51KHiJzMlOLBc` |
| Success Track (mostly blank template) | `1luy7qWBPTP3OMqxk3jTk-cegxQUzOekm01LCyxPENvE` |
| PPC keywords (2022–23, linked from Success Track) | `1KIcuOn7ed3rQzsBuhK87B1uZlF8OEb-XGuuhq0liS4I` (not read) |
| BLOG Masterlist (shared, Aloha tab) | `1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw` (not read this session) |

## 12. Open items

**Waiting on decisions**
- [ ] New-site launch plan: domain (alohalifemobilespa.com redirects to the old site today), cut-over date, redirect map, and duplicate-content handling while both run.
- [ ] Second GBP "Aloha Life Mobile Spa": decided? (Andrew recommended Option 2, 2026-07-08.)
- [ ] Confirm Google Ads are fully paused and billing stopped.
- [ ] Confirm whether SEO/blog work resumes after the build, and the retainer amount.

**Overdue for us**
- [ ] Reply to the **Sept 2026 automated report review** (posted 2026-09-09; follow-ups 09-16 and 09-29).
- [ ] Check the Oct 2026 report when it arrives (~10-07).

**Live-site fixes** (still worth doing; the old site stays live during the build)
- [ ] Remove Kahului and Wailuku from the homepage FAQ and schema; replace "all of Maui".
- [ ] Merge the duplicate business schema blocks into one; fix the broken FAQ schema HTML; one H1.
- [ ] Move the two June 2026 posts out of /uncategorized/ (or confirm the categories were set).
- [ ] Remove WooCommerce and sample pages from the sitemap.
- [ ] Delete the Make test draft (WP post 8079).

**Tracking and data**
- [ ] Audit GA4 key events (form_submit, phone_click, purchase). Down ~90% YoY across all channels since at least June 2026.
- [ ] Export the Semrush Position Tracking keyword list from the UI (API can't reach the campaign).
- [ ] Get `sc-domain:alohalifemassage.com` GSC access, or keep using the URL-prefix property.
- [ ] Fix or retire Make scenario 6189592 (`sheetId "Untitled"` vs tab "Aloha"; flagged invalid).

**Security / privacy**
- [ ] Failed WordPress login attempts were reported on 2025-10-11 for Aloha (and Vision, Munro, Spiedr), and Francis's Aloha password had changed. *Confirm it was investigated and 2FA / login limiting is on.*
- [ ] Decide whether the live schema should publish the full street address with unit number (looks residential). Service-area businesses usually hide it.
- No plain-text credentials were found in the Drive files or Make blueprint reviewed.

## 13. Gaps and conflicts

**Gaps**
- Gmail not checked.
- BrightLocal: tool error, so no rank-grid, citations or reviews data.
- Semrush Position Tracking keywords, competitors and visibility: API "campaign not found".
- Sept 2026 report PDF: the Slack file API failed.
- Retainer, current contract term, and whether a monthly SEO contract exists after the 2023 web build.
- Hawaii licence numbers (therapist / establishment) and the exact advertising rule.
- BLOG Masterlist Aloha tab not read.
- New-site build status since July 2026 (nothing in the channel since 2026-08-06 apart from the report bot).

**Conflicts**
- **Service areas:** client excluded Wailuku and Kahului (2026-06-17), but the live FAQ and schema say "We serve all of Maui, including … Kahului, and Wailuku".
- **Hours:** schema 8:00–18:00 vs 9:00–17:00.
- **Business name:** "Aloha Life Massage" vs "Aloha Life Massage / Maui's Best Mobile Service" (schema/GBP) vs "Aloha Life Mobile Spa" (new). The meeting notes contradict themselves: "officially adopted the Aloha Life Mobile Spa name" vs "retain the current business name, Aloha Life Mobile Spa, rather than changing it". *Confirm.*
- **New domain:** transcript mentions "aloha spa.com", "aloha mobilespa.com" and alohalifemobilespa.com.
- **Pricing:** Bronze was $120/60 min (Jun 2025, Slack); the live site says $149 (Oct 2026).
- **Make scenario description** says "ACTIVE PILOT" but the scenario is inactive and invalid.
- **Channel topic** lists Brittni as TP lead; Andrew and Francis actually run it.
- **Imagery:** the 2026-06-17 decision was to replace stock and AI images, but Dani also floated using AI for a daylight image. Prefer real Maui photos.
