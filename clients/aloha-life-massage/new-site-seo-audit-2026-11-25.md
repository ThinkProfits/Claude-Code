# Aloha Life: new-site SEO audit, keyword research and page-by-page optimization

> **Date:** 2026-11-25 · **Author:** Claude for Francis (SEO lead) · **Status:** internal, for Francis / Andrew / Shawn. Not client-facing yet.
> **What was audited:** Lovable project "Maui Luxury Spa" (`f52a47a4-163a-4052-b86a-67809f0d334c`), latest commit `aa72304` (2026-10-13, nothing has changed since). Every route, data file, template, `index.html`, `robots.txt`, `sitemap.xml` and the JSON-LD were read from source.
> **Data sources:** Google Keyword Planner via the `google-ads-keywords` MCP (US, English, avg. monthly searches Nov 2025 to Oct 2026); Google Search Console `https://alohalifemassage.com/` (2026-08-27 to 2026-11-25); live-site Yoast sitemaps (fetched 2026-11-25); [keywords.md](keywords.md), [CLIENT.md](CLIENT.md), [lovable-edits-2026-10-09.md](lovable-edits-2026-10-09.md).
> **Not available:** Semrush. Every keyword report returned "no API units left" (`hint_url: semrush.com/mcp-access`), so there is no KD, SERP, competitor or PAA pull from Semrush in this audit. Volumes are Google's own Keyword Planner figures (rounded bands, US-wide). The Lovable preview needs a login, so page speed and Core Web Vitals were **not measured**. Run PageSpeed Insights once it is published.
> **Spelling:** the analysis is in Canadian English (agency default). Suggested on-page copy is in US English because the client is in Hawaii (CLIENT.md §8, still *confirm with Andrew*).
> **No guarantees:** nothing here promises a ranking. These are the changes most likely to improve visibility, based on the data above.

---

## 1. The short version

The new site looks great and the service-area pages are genuinely strong. **As built, though, it is not ready to launch from an SEO point of view, and launching it as-is would very likely lose most of the organic traffic the old site earns.** The five biggest problems:

1. **Search engines and AI crawlers see an empty page.** It is a client-side React app (Vite SPA). Every URL serves the same `index.html`, with the homepage title, a sitewide `noindex, nofollow` and `<div id="root"></div>`. Google can render JavaScript, but slowly and less reliably. ChatGPT, Claude and Perplexity crawlers generally do not run JavaScript (Vercel, "The rise of the AI crawler", Dec 2024), so for AEO/GEO the site is invisible. **This needs prerendering or SSR before launch.**
2. **The blog lost its content.** The 12 migrated posts are 3–4 paragraph stubs (about 60–120 words each). The live versions are full articles. The lymphatic drainage post, the best non-brand page on the old site (43 clicks, 861 impressions, average position 7.5 over the last 90 days), would drop to about 70 words. **Three live posts are missing entirely**, including the scuba post (370 impressions, position 8.8).
3. **Every lead form is fake.** The VIP NDA request, the Retreats registration, the Retreats newsletter and the Join Our Team application all show a "received" toast and **send nothing anywhere**. Any lead submitted after launch is lost.
4. **The redirects aren't real redirects.** `/meet-the-team`, `/couples-massage-maui` and the others are React `<Navigate>` calls. Google sees a 200 page, not a 301. There's also no server-side map for the ~45 live URLs (`/services/...`, `/blog/health/...`), so all their equity would go to soft 404s. Unknown URLs return 200 too (soft 404).
5. **The brand headline targets a phrase nobody searches.** "Mobile spa maui", "maui mobile spa" and "luxury spa maui" get **0–10 searches a month**. "Maui massage" / "massage maui hawaii" gets **2,900**, "massage places in maui" **2,900** and "massage kihei" **480**. The homepage H1 and title don't contain the word "massage".

There are also **~70 uses of "therapist" on its own** (the client's #1 copy rule), **no analytics or GTM installed**, and several claims that break existing client rules: a "guaranteed" heading, a retreat in Hana, waxing prices under the $150 wax-only minimum, couples side-by-side copy and medical "detox" claims in the blog.

---

## 2. Launch blockers (P0): fix before the domain goes live

| # | Issue | Where | Fix |
|---|---|---|---|
| P0-1 | **No prerender / SSR.** Crawlers get an empty `#root` and the homepage `<head>` on every URL until JS runs. | `index.html`, `vite.config.ts` | Add build-time prerendering for every route in `sitemap.xml` (e.g. `vite-plugin-prerender`/`vite-ssg`, or Lovable's SSR option if the plan supports it). **Confirm with Lovable whether its hosting serves prerendered HTML.** If not, deploy the build to Netlify / Cloudflare Pages / Vercel. Success test: `curl -A Googlebot <url>` returns that page's own title, H1, body copy and JSON-LD. |
| P0-2 | **Sitewide `noindex, nofollow`** hard-coded in `index.html`. That's correct pre-launch, but `Seo.tsx` deliberately never overrides it, so if nobody removes it, the whole site launches de-indexed. | `index.html:10` | Put it on the launch checklist: remove it on cut-over day and keep it on the lovable.app preview only (an env-based flag is best). |
| P0-3 | **Domain is still `maui-zen-on-demand.lovable.app`** in `SITE_URL`, all canonicals, og:url, JSON-LD `@id`s, `robots.txt` and `sitemap.xml`. | `src/data/site.ts`, `public/robots.txt`, `public/sitemap.xml`, `index.html` | Decide the production domain (alohalifemassage.com vs alohalifemobilespa.com; see §8), then swap `SITE_URL` plus the hard-coded og/twitter URLs in `index.html`. Regenerate the sitemap. |
| P0-4 | **No server-side 301s.** All "redirects" are client-side `<Navigate>` (200 status). There's no map for the live site's ~45 URLs. | `src/App.tsx` | Implement host-level 301s from the full map in §7 (`_redirects`/`netlify.toml`/Cloudflare rules or Lovable's equivalent). Then submit the change of address in GSC and update the GBP website URL. |
| P0-5 | **Soft 404s.** `NotFound` renders on a 200 response with no `noindex`. | `src/pages/NotFound.tsx` | Return a real 404 from the host for unknown paths (the prerender step or a host rule), and add `<meta name="robots" content="noindex">` to NotFound as a backstop. |
| P0-6 | **Four forms submit nowhere** (toast only). | `PremiumVip.tsx` (NDA), `Retreats.tsx` (registration + newsletter), `JoinOurTeam.tsx` (application) | Wire each one to a real endpoint (Supabase table + email notification, or a form service), or replace it with a `mailto:`/`tel:` link until wired. Test every form end-to-end before launch. |
| P0-7 | **No analytics or tag manager.** No GA4, GTM or Clarity in the codebase. Conversion tracking on the old site is already down ~90% YoY. | `index.html` | Install GTM, then GA4 with key events: Acuity outbound click (`as.me`), `tel:` click and each form submit. Add cross-domain measurement for Acuity if it supports the GA4 tag. Don't launch blind. |
| P0-8 | **Blog content is truncated** (see §5.6) and **3 ranking posts are missing.** | `src/data/blog.ts` | Migrate the full approved text of all 15 live posts, with H2s and FAQs. Restore lomi-lomi-vs-swedish, prenatal-babymoon and scuba. |
| P0-9 | **Waxing booking is broken.** Waxing isn't on Acuity (lovable-edits log), but every waxing "Book" button goes to the generic Acuity page. The bundle prices were invented by Lovable, and Bronze ($45/$75) and Silver ($135) are **below the client's $150 wax-only minimum**. | `src/data/services.ts` `waxingPage`, `BrazilianWaxing.tsx` | Either set waxing to "Call to book" (like Classic Facial) with prices Dani confirms, or remove the price cards. Add the $150 wax-only minimum. Drop the standalone "Underarm Wax" item (keyword rule: no single-service wax terms). |
| P0-10 | **Retreats page is stale and off-rule.** All four retreat dates are 2026 and three have passed. The "Gratitude" retreat is in **Hana, an excluded area**, and lists a "Plant Medicine Talk Circle". The headline says "across the Hawaiian Islands". The client's position is "Coming Soon, January 2027, no firm dates". | `src/data/retreats.ts`, `Retreats.tsx` | Replace it with a short "Coming soon" page and a working interest form, `noindex` until dates are real. Remove Hana and the plant-medicine item. |

---

## 3. Sitewide technical and schema findings (P1)

**Rendering and head**
- `index.html` ships a static `DaySpa` JSON-LD block (address "Maui", reviewCount 240) on **every** URL, while each page also injects a `HealthAndBeautyBusiness` with the same `@id`. That's two conflicting business entities. **Fix:** delete the static block and keep one business node in `Seo.tsx`.
- `index.html` has a `<meta name="keywords">` tag. Google ignores it. Remove it (harmless, but it advertises the keyword list to competitors).
- Favicon is declared `type="image/png"` but points to `.ico`. Fix the type and add a 180×180 apple-touch-icon.
- The `og-image.jpg` is the same on every page. Fine for launch; later, give the service and area pages their own.

**Schema (JSON-LD)**
- **Name, address, phone (NAP) mismatch with GBP.** Schema says `name: "Aloha Life Mobile Spa"`, `addressLocality: "Wailea"`, 96753. The GBP is "Aloha Life Massage" in Kihei (CLIENT.md §1). The logo says "Mobile Massage & Spa". Pick one legal/trading name and make the GBP, schema, logo, title tags and footer match exactly. A Wailea locality with the Kihei ZIP will read as inconsistent.
- **`aggregateRating` on the business** (home, `/service-areas`, `/reviews`, and the `index.html` block). Google doesn't show star snippets for self-serving reviews on LocalBusiness/Organization (Google Search Central, Review snippet guidelines), and the `/reviews` page marks up Google reviews as first-party `Review` objects. **Remove both.** Let the GBP carry the stars.
- **Review count is inconsistent:** 238 (area pages), 240 (schema), 240+ (copy). GBP had 257 in Aug 2026. Use one source (ideally the live widget planned for `#footer-reviews`) or say "250+".
- **Massage and facial bundles are marked up as `Product`** with Offers (`ServicePageTemplate.tsx`). These are services, so Product markup is the wrong type and may be flagged. Use `Service` + `Offer` (or `OfferCatalog`) instead.
- **`ServiceAreaDetail.tsx` and `ServiceAreas.tsx` define their own `businessLd`** instead of importing it from `Seo.tsx`, so it has already drifted (ServiceAreas adds `aggregateRating` 238). Use the shared one.
- **FAQPage duplication:** the homepage and `/faq` emit the identical 8-question FAQPage. Give `/faq` the full set and the homepage a short, different set (or no FAQ schema).
- **Blog `BlogPosting.author` is the Organization.** The client rule is a Dani byline. Use a `Person` (Dani, with a link to `/about#team`) for E-E-A-T, and set a real `dateModified` when posts are updated.
- **Missing:** `sameAs` (Facebook, Instagram, GBP CID URL), `openingHoursSpecification` (decide 8–6 vs 9–5; CLIENT.md conflict), `geo`, `hasMap`, `logo`. Add them to the single business node. For a service-area business, leave out the street address.

**Crawl and indexation**
- `sitemap.xml` has no `<lastmod>`. Add it (the generator script already exists). It also lists the Valentine's couples post that needs rewriting, and `/retreats` (noindex it until it's real).
- Missing pages compared with the live site: **contact, privacy policy, terms, gift certificates, group bookings, add-ons, testimonials**. A privacy policy is required once the forms collect personal data. Gift certificates earned clicks (13% CTR). See §7.
- Hash links (`#in-room`, `#bundles`, `#bikini`, `#full-body`) are fine for UX but can't rank. "Mobile Massage" in the nav points to `#in-room`, an anchor with no unique content.

**On-page templates**
- **Title tags are too long.** 22 of 26 measured titles run 63–85 characters because the " | Aloha Life Mobile Spa" suffix adds 22. Google truncates at roughly 580 px (~60 characters). Shorten the suffix to " | Aloha Life" or drop it where the title already names the brand (About repeats it twice).
- **Meta descriptions run 155–167 characters** and lean on "Maui's top-rated" / "5.0 stars" superlatives. Keep them to ≤155 characters and verifiable.
- **Every hero image has `alt=""`** (PageHero, BlogPost). That's acceptable for decorative backgrounds, but then the pages have **no descriptive image at all**. Add at least one real in-content photo with alt text per service and area page (and Dani's real photos fix the imagery-rule problem at the same time).
- **The same boilerplate blocks repeat on most pages:** the same 6 reviews, the same 9-area grid with the VIP blurb, the same FAQ. Thin-template risk. Rotate service-relevant reviews per page and drop the generic FAQ where the page has its own.
- Footer headings skip levels (h4 with no h3). Minor accessibility issue.
- `tel:` links use `8086499777` without `+1` in the footer. Use `tel:+18086499777` everywhere (the area pages already do).
- The homepage hero image is a **sunset**, which breaks the "no evening imagery" rule (CLIENT.md §8). The site-wide imagery problem is already logged and is waiting on Dani's photos.

**Copy-rule violations (sitewide)**
- **"Therapist" used on its own: ~70 instances across 13 files** (customer review quotes excluded). Main offenders: `serviceAreaDetails.ts` (~29), `ServiceAreas.tsx` (7), `blog.ts` (7), `site.ts` FAQ (5), `Index.tsx` (5), `About.tsx` (4), `PremiumVip.tsx` (4), `ServiceAreaDetail.tsx` (4), `index.html` meta (3). One Lovable instruction can fix them all: replace "therapist(s)" with "massage therapist(s)", or "esthetician" where facials or waxing are meant.
- **Guarantee language:** About H2 "The best massage of your trip — guaranteed". Remove (agency rule and client rule).
- **Unverifiable superlatives:** "Maui's top-rated", "Maui's most-loved", "Best VIP…", "Industry-leading pay", "Top split in the Hawaiian mobile spa space", "Trusted by prominent guests across the world". Soften or source them.
- **Out-of-scope geography:** "every corner of Maui" (`/service-areas` meta + FAQ "If you're staying on island, we'll come to you"), VIP "around the world", "off-island", "jet". The rule is "the island of Maui" and no Hana, Nahiku, Wailuku or Kahului.
- **Unverified licensing facts presented as fact:** "570+ training hours", "Hawai'i does not accept the national MBLEx", "every therapist holds an active Hawai'i LMT license", "licensed Hawai'i estheticians", "background-cleared". These may be right, but nobody has confirmed them, and they sit on every area page. Verify with the Hawaii Board of Massage Therapy (HRS ch. 452) and Dani before launch. Also confirm microneedling/microchanneling is within a Hawaii esthetician's scope of practice.

---

## 4. Keyword research

**Source:** Google Keyword Planner, US, English, average monthly searches (Nov 2025 to Oct 2026). Tourists search before they fly, so US-wide is the right base. Keyword Planner merges close variants: "maui massage" and "massage maui hawaii" share one 2,900 bucket, so don't add those numbers together.

### 4a. Head and core terms

| Keyword | Avg/mo | Comp. | Intent | Notes |
|---|---|---|---|---|
| maui massage / massage maui hawaii | 2,900 | High | Commercial, local | Biggest relevant term. Old site ranks ~22–24 (GSC). **Homepage primary.** |
| massage places in maui | 2,900 | High | Commercial, local | Same cluster. Homepage secondary. |
| maui spa / spas in maui hawaii | 2,400 | Medium | Commercial, mostly resort spas | Hard to win against resort spas. Secondary for homepage and facial hub only. |
| best spa in maui / best spa in maui hawaii | 720 | High | Commercial investigation | Listicle-dominated SERP. Blog angle, not a page. |
| best massage in maui / best massage maui | 480 / 140 | Low–Med | Commercial investigation | Homepage secondary; reviews page. |
| maui spa massage / maui spa and massage / maui spa and wellness | 320 each | Low | Commercial | **Fits the rebrand.** Use "massage & spa" phrasing, not "mobile spa". |
| maui day spa / day spa maui hawaii | 320 | High | Commercial | Secondary; facial hub. |
| massage therapist maui | 260 | Low | Commercial | About/team and massage hub. |
| massage therapy maui | 260 | Low | Commercial | Massage hub. |
| mobile massage maui | 210 | Low | Commercial, high fit | Old site 27.6 avg (GSC, 610 impressions, 32 clicks). Homepage + hub. |
| mobile spa maui / maui mobile spa / luxury spa maui | 0–10 | — | — | **Current homepage positioning. No demand.** Keep it as a brand line, not the SEO target. |
| in room massage maui / hotel massage maui / in home massage maui | 0 | — | — | Zero Maui-modified volume. National "massage at hotel room" (480) and "in room massage" (480) are worth a section, not a page. |

### 4b. Services

| Keyword | Avg/mo | Comp. | Page |
|---|---|---|---|
| couples massage maui / couples massage maui hawaii | 720 / 720 | High | **No page** (removed). See decision D2. |
| babymoon maui | 590 | Low | Prenatal page + restore the babymoon blog |
| deep tissue massage maui | 260 | Low | Deep tissue page |
| lomi lomi massage maui / lomi massage maui | 260 / 260 | Med | Lomi lomi page |
| lomi lomi massage (national, informational) | 22,200 | Low | Lomi lomi page "What is lomi lomi" section + restore the lomi-vs-swedish blog |
| swedish vs deep tissue (national) | 1,300 | Low | Existing blog (currently a stub) |
| facial maui | 140 | Med | Facial hub |
| prenatal massage maui | 90 | Low | Prenatal page |
| lymphatic drainage massage maui / lymphatic massage maui | 90 / 30 | Med | **Not a service on the new site.** The blog ranks 6.4 today. See D3. |
| waxing maui / brazilian wax maui | 70 / 70 | Low | Waxing hub / Brazilian page |
| microneedling maui | 50 | Med | Microneedling page |
| hydrafacial maui | 40 | Med | Not offered. Don't target. |
| swedish massage maui | 30 | Low | Swedish page |
| massage after scuba diving | 30 | Low | Restore the scuba blog (GSC 370 impressions) |
| lomi lomi vs swedish | 30 | Low | Restore the blog |
| sports massage maui | 20 | Med | Sports page |
| hot stone massage maui | 10 | — | Hot stone page (low demand; keep it for completeness) |
| therapeutic massage maui | not returned | — | Low. Keep the page; it supports the package menu. |

### 4c. Areas

| Keyword | Avg/mo | Page | Old-site GSC |
|---|---|---|---|
| massage kihei / massage kihei hawaii | 480 / 480 | /service-areas/kihei | "massage kihei" pos 12.2, "massage kihei maui" 9.9, "best massage kihei" 4.0 |
| kihei massage / massage kihei maui | 210 / 110 | /service-areas/kihei | "kihei massage" 9.3 |
| lahaina massage / massage lahaina hawaii | 390 / 390 | /service-areas/lahaina | — (handle with fire-recovery sensitivity) |
| kaanapali massage | 260 | /service-areas/kaanapali | — |
| paia massage | 170 | /service-areas/paia | — |
| wailea massage / massage wailea maui / massage wailea | 140 / 140 / 90 | /service-areas/wailea | "massage wailea maui" 16.8 |
| makawao massage | 90 | **No page.** Upcountry. *Confirm served* (CLIENT.md §3) | — |
| massage kapalua / massage napili | 30 / 30 | Kapalua / Napili pages | — |
| makena massage / haiku massage | 10 / 10 | Makena / Haiku pages | — |
| massage kahului | 320 | **Do not build.** Kahului excluded 2026-06-17 | — |

**Excluded on purpose:** "exotic massage maui" (880) and the sensual, happy-ending and body-rub terms the old site still gets clicks on (GSC: "sensual massage maui" 5 clicks, "happy ending massage maui" 3). Hotel-brand terms (Grand Wailea, Westin and so on, up to 60k) are navigational for the resorts. Mention properties in copy (the area pages already do), but never target them in titles.

**PAA / question research:** not pulled (Semrush `phrase_questions` had no units). The PAA standard (`memory/paa-research-standard.md`) still applies. Pull it before rewriting the FAQs in §5, or have someone run the questions manually in an incognito US SERP.

---

## 5. Page-by-page audit and optimization

Format per page: what's there → issues → recommended title (≤60 chars), H1 and meta (≤155 chars), plus content and linking changes. **Target keyword and search intent are stated for every page.**

### 5.1 Homepage `/`
**Target:** maui massage · **Secondary:** massage maui hawaii, massage places in maui, mobile massage maui, maui spa massage · **Intent:** commercial / local

*Current:* title "Luxury Mobile Spa in Maui — Massage, Facials & Waxing | Aloha Life Mobile Spa" (77 characters). H1 "Maui's luxury mobile spa, delivered with aloha." The body has a 4-tier package grid, how-it-works, reviews, areas and FAQ. ~600 words of unique copy.

*Issues*
- H1 and title lead with "luxury mobile spa" (0 searches). The word "massage" is not in the H1.
- Sunset hero breaks the imagery rule. "Licensed therapists" appears 4 times. "Certified Maui therapists" (certified vs licensed; pick the accurate one).
- No mention of the priority areas above the fold. No "Serving Maui since 2019" (the agreed hero line).
- "No hotel mark-ups" is a comparative claim. Fine, but keep it factual.
- Service cards link to the hubs only. No direct links to the 7 massage pages or the top area pages from the homepage body (the nav handles it, but in-content links carry more weight).

*Recommend*
- **Title:** `Maui Massage & Mobile Spa | In-Room | Aloha Life` (50)
- **H1:** "Mobile Massage & Spa in Maui, Brought to Your Door" with the eyebrow "Serving Maui since 2019".
- **Meta:** "Licensed massage therapists bring massage, facials and waxing to your Maui villa, condo or resort suite. Serving Kihei, Wailea, Kaanapali and more." (149)
- Add a ~150-word "Massage in Maui, without leaving your room" section that answers the query directly (who, where, what's included, price from $149, how to book). It's an AEO-friendly answer block.
- Add a "Popular massage styles" row linking to deep tissue, lomi lomi, Swedish and prenatal, plus a "Where we travel" line linking Kihei, Wailea, Kaanapali and Lahaina.
- Swap the hero to a daytime photo once Dani supplies one.

### 5.2 Massage hub `/massage-services-maui`
**Target:** massage therapy maui · **Secondary:** massage therapist maui, maui spa massage · **Intent:** commercial

*Issues*
- Title 83 characters. It competes with the homepage for "mobile massage maui". Differentiate: the hub sells the menu and packages; the homepage sells the brand and areas.
- **The Deep Tissue card has no "Learn more" link** (missing `href`) even though the page exists. "Mobile Massage" (#in-room) and "Premium & Executive" cards also have no link (VIP has a page).
- Card durations don't match the packages: Swedish says "60 / 90 / 120" but the packages are 60/75/90/120; Sports says "60 / 90".
- "Speeds recovery, restores range of motion, prevents soreness" is an unhedged health claim. "Maui's most-loved", "therapists".
- Bundles are marked up as `Product` (see §3).

*Recommend*
- **Title:** `Massage Therapy in Maui | Mobile Massage Menu & Prices` (55)
- **H1:** "Massage Therapy in Maui, Delivered to You"
- **Meta:** "Deep tissue, lomi lomi, Swedish, hot stone and prenatal massage at your Maui villa or condo. Packages from $149 for 60 minutes, before tax." (139)
- Add `href` for deep tissue, `/massage-services-maui/premium-vip` for the Premium card, and either a real in-room page or remove the in-room card.
- Add a comparison table (style · pressure · best for · link) for snippet and AEO value.

### 5.3 Massage detail pages (7) `/massage-services-maui/<slug>`
Shared template `FocusedServicePage`. Copy is clean, hedged and follows the "massage therapist" rule (the best-written pages on the site). **Shared issues:** ~300–350 words of unique copy per page versus ~1,300–1,400 on the live equivalents (rough count, 2026-11-25), so these are thinner than the pages they replace. Titles run 71–75 characters. Hero alt is empty. No price on the page except in some FAQs. No links to related blog posts or area pages beyond the generic grid. All link "Book" to the Bronze category, even where Silver would fit.

**Template fix (one Lovable change for all 7):** add a "Pricing" block that pulls the package prices, a "Where we offer it" block linking 4 priority areas, a "Related reading" block (1–2 blog posts), and 2–3 extra FAQs per page from PAA research. Target 600–900 words per page.

| Page | Target keyword (vol) | Intent | Recommended title | Page-specific changes |
|---|---|---|---|---|
| deep-tissue-massage | deep tissue massage maui (260) | Commercial | `Deep Tissue Massage in Maui \| Mobile, From $149` (47) | Link to the swedish-vs-deep-tissue blog. Add a "deep tissue vs sports" FAQ. The old lymphatic blog outranked the old deep tissue page; internal-link from the restored lymphatic post with "deep tissue massage in Maui" anchor text. |
| swedish-massage | swedish massage maui (30) | Commercial | `Swedish Massage in Maui \| In-Room Relaxation` (44) | Link to both swedish-vs blogs. Low volume; keep the page lean. |
| therapeutic-massage | therapeutic massage maui (low) | Commercial | `Therapeutic Massage in Maui \| Mobile & Licensed` (47) | Good "not medical massage" FAQ; keep it. |
| lomi-lomi-massage | lomi lomi massage maui (260) + lomi massage maui (260); "lomi lomi massage" 22,200 national | Commercial + informational | `Lomi Lomi Massage in Maui \| Traditional Hawaiian` (48) | **Highest-upside service page.** Expand "What is lomi lomi" into 250–300 words (history, technique, what to expect), add "lomi lomi vs Swedish" FAQ, link the restored comparison blog. Uses a `sunrise.jpg` that reads as sunset; swap. Keep "Maui" signals strong so it stops ranking for Oahu terms. |
| sports-massage | sports massage maui (20) | Commercial | `Sports Massage in Maui \| Surf, Hike & Golf Recovery` (51) | Link the sports-recovery and scuba blogs. Remove "cupping" from the sports blog unless it's offered. |
| hot-stone-massage | hot stone massage maui (10) | Commercial | `Hot Stone Massage in Maui \| Included From $175` (46) | Book button should go to Silver (it does). Fine. |
| prenatal-massage | prenatal massage maui (90) + **babymoon maui (590)** | Commercial | `Prenatal & Babymoon Massage in Maui \| Mobile` (45) | Add "babymoon" to the H1/intro ("Planning a babymoon on Maui?") and a babymoon FAQ. Restore and link the babymoon blog. Nav label "Pregnancy Massage" is fine. |

### 5.4 Premium VIP `/massage-services-maui/premium-vip`
**Target:** VIP / luxury in-room massage Maui (0–10 measurable; brand/positioning page) · **Intent:** commercial, high value

*Issues:* **The NDA form sends nothing (P0-6).** H1 "Best VIP Mobile Massage Therapy Services in Maui" ("Best" is an unverifiable superlative). "Around the world", "off-island", "jet" contradict Maui-only. "Therapists" ×4. "Background-cleared", "Trusted by prominent guests across the world" are unverified. Title 79 characters.

*Recommend:* **Title** `Private VIP Massage in Maui \| Discreet In-Suite Service` (55). **H1** "Private VIP Massage in Maui". Fix the form. Keep it as a conversion page; don't expect search volume.

### 5.5 Facial hub + 4 facial pages
**Hub target:** facial maui (140) · **secondary:** maui day spa (320), maui spa (2,400, long shot) · **Intent:** commercial

*Issues:* "Clinical-grade products", "Advanced collagen-induction therapy that … fades pigment", and "Most Requested" / "Signature Service" badges are unverified claims. Hub title 82 characters. The "what's included" details are still waiting on Dani (already logged).
- `classic-facial`: "Call to book" works. Fine.
- `hydrating-facial`, `anti-aging-facial`: individual terms ≈ 0 volume. Keep them as menu pages, but point the internal "facial maui" anchors at the hub.
- `microneedling`: target "microneedling maui" (50). Copy is responsibly hedged. **Confirm esthetician scope of practice in Hawaii for microneedling/microchanneling** before launch.

*Recommend:* **Hub title** `Facials in Maui \| Mobile Facials From $149` (42). **H1** "Facials in Maui, in the Privacy of Your Suite". Replace "clinical-grade" with the actual brands used (Eminence, Knesko and ProCell appear elsewhere on the site), which is stronger for E-E-A-T anyway.

### 5.6 Waxing hub + Brazilian page
**Target:** waxing maui (70) / brazilian wax maui (70) · **Intent:** commercial

*Issues:* P0-9 (booking and pricing). Brazilian page `pairWith` links "Vacation Glow Bundle" to `/` (broken intent). The `#hydrating` anchor on the facial hub does exist. "A quick refresh before dinner" implies evenings. Titles 77–79 characters. Note Dani wanted waxing kept for now (CLIENT.md §12).

*Recommend:* **Hub title** `Waxing in Maui \| Private, In-Suite Hard Wax` (43). **Brazilian title** `Brazilian Wax in Maui \| Private & In-Suite` (42). State the $150 wax-only minimum clearly (it reduces bad-fit enquiries).

### 5.7 Service areas hub `/service-areas`
**Target:** mobile massage maui areas / "massage near me" support (GBP proximity) · **Intent:** navigational / commercial

*Issues:* "Every corner of Maui" (meta) and "If you're staying on island, we'll come to you" contradict the exclusions. It carries its own `businessLd` with `aggregateRating` 238. Unverified licensing paragraph. Title 70 characters.

*Recommend:* **Title** `Maui Mobile Massage Service Areas \| Aloha Life` (46). Add an explicit "Areas we don't currently serve: Hana, Kahului, Wailuku" line (honest, and it filters out bad leads). Add Makawao/Upcountry only if Dani confirms.

### 5.8 Area pages (9) `/service-areas/<slug>`
**The strongest pages on the site:** 600–800 words of real local detail per page (resorts, logistics, landmarks, area FAQs, nearby links). They need targeting, not rewriting.

**Shared issues**
- **H1 and title lead with "Mobile Spa", but searchers type "massage <area>".** H1 is "Mobile Spa Service in Kihei". Change the pattern to **H1 "Mobile Massage in <Area>, Maui"** and **title `<Area> Massage | In-Room Mobile Massage | Aloha Life`** (Kihei = 51 characters). Mention spa and facials in the intro.
- "Therapist" appears ~29 times in this data file.
- The travel-fee sentence is identical on all 9 pages, and the Wailea and Kihei FAQs say "no travel fee". Make it area-specific using the Acuity fees (Lahaina/Kaanapali $25, Kapalua $30; Paia/Haiku: confirm).
- `serviceLd` → `provider` repeats a local `businessLd` copy. Use the shared one.
- Kihei and Haiku FAQs promise "simultaneous sessions" / "multiple therapists working simultaneously". Check against the side-by-side rule (D2).

| Page | Target (vol) | Specific fixes |
|---|---|---|
| kihei | massage kihei (480) + massage kihei hawaii (480) + kihei massage (210) | **Priority #1 area page.** The old site already ranks 4–12 for Kihei terms. Page says "Kihei is just north of our Wailea home base", but CLIENT.md says Kihei *is* the home base. Fix to match the GBP. |
| lahaina | lahaina massage (390) + massage lahaina hawaii (390) | Sensitive copy is handled well. "Lahaina Shores reopened July 2025" and "local resident pricing options" are unverified; confirm or remove. Title: `Lahaina Massage \| Mobile Massage in West Maui` (45). |
| kaanapali | kaanapali massage (260) | Good. "Book 3–5 days ahead" vs Kihei's "48+ hours": make the lead times consistent. |
| paia | paia massage (170) | Good. Confirm Paia is served (not on the client's explicit list). |
| wailea | wailea massage (140) + massage wailea maui (140) + massage wailea (90) | "Home base" claim (see Kihei). "In-suite facials before dinner reservations" implies evening bookings; change to "before a celebration or photo session". |
| kapalua | massage kapalua (30) | Client priority despite low volume (high spend). Keep. Add the $30 travel fee. |
| napili | massage napili (30) | "Ask about our bundle pricing" / "multi-day wellness packages": confirm they exist. |
| makena | makena massage (10) | "Polo Beach Club" appears under both Wailea and Makena; pick one. Verify the "Maui Prince closed 2016" fact. |
| haiku | haiku massage (10) | Borders the Road to Hana. Copy says "along the road to Hana" repeatedly, which flirts with the excluded area. Confirm it's served. |

**New area pages (after launch, if Dani confirms coverage):** Makawao/Upcountry (makawao massage 90). Don't build Kahului (320/mo, excluded).

### 5.9 About `/about` (absorbs `/meet-the-team`)
**Target:** massage therapist maui (260), "Dani massage therapist" (brand) · **Intent:** navigational / trust

*Issues:* **H2 "The best massage of your trip — guaranteed"** (remove). "Maui's top-rated mobile massage provider" (unverifiable). Title repeats the brand twice (78 characters). Team bios name the Ritz-Carlton, Grand Wailea and "Spa Grande" (confirm each affiliation). Tiffany's bio says "rotator cuff recovery", which reads as clinical; soften it. No `Person` schema for the team.

*Recommend:* **Title** `About Us & Our Maui Massage Therapists \| Aloha Life` (51). Add `Person` schema for Dani (founder, licence number once confirmed) and link the blog byline here. On the old site `/meet-the-team/` gets 1,552 impressions (position 7.4) and `/about-us/` gets 1,416 (position 5.0). Both need server 301s to `/about`.

### 5.10 What to Expect `/what-to-expect`
**Target:** what to expect mobile massage (informational, supports conversions) · Clean, rule-compliant copy (uses "massage therapist" correctly). Add `HowTo`-style structure (the steps are already an `<ol>`) and an FAQ block (cancellation, tipping, pets, what to wear) built from PAA. Title is 68 characters; cut to `What to Expect From a Mobile Massage in Maui` (44, no suffix).

### 5.11 FAQ `/faq`
Identical to the homepage FAQ (same 8 questions, same FAQPage schema). Expand it to 15–20 questions grouped by Booking / Services / Areas / Policies, using PAA data and the questions on the area pages. Fix "every therapist is fully licensed in Hawai'i" to cover estheticians and use "massage therapist". Title: `Mobile Massage FAQ \| Booking, Areas & Prices \| Maui` (51).

### 5.12 Reviews `/reviews`
Thin page: 6 reviews, the same 6 shown on ~10 other pages, plus self-serving Review schema (§3). Recommend embedding the live GBP review widget here (the free widget decision is already made) and removing the Review/AggregateRating markup. Title is fine at 65 characters; trim to `Reviews \| 5.0 Stars on Google \| Aloha Life Maui` (47).

### 5.13 Retreats `/retreats`
See P0-10. Noindex until there are real 2027 dates. "Maui wellness retreat" terms weren't measured.

### 5.14 Join Our Team `/join-our-team`
**Target:** massage therapist jobs maui (recruiting) · Fix the form (P0-6). Add `JobPosting` schema only if there are real, current openings with pay ranges. Verify "industry-leading pay" / "top split" / "same-week payouts" or remove them. **Exclude this page's events from lead reporting.**

### 5.15 Blog index + 12 posts `/blog/<slug>`
*Issues (all posts)*
- **Truncated content.** Posts render 3–4 plain `<p>` paragraphs with **no H2s, no Quick Answer, no FAQ**, against the client's blog standard (CLIENT.md §8). Example: the lymphatic post is ~70 words on the new site.
- **Medical claims** the old copy had been edited to avoid: "encourage natural detoxification", "Detox & Relax with Maui's Best" (lymphatic title), "drain travel inflammation", "reduced inflammation", "lower cortisol", "research-backed" (no sources), "restores range of motion in a single session", "full recovery within 24 hours".
- **Rule breaks:** Valentine's post promises "Two therapists, two tables, side-by-side" and a "sunset slot". The wedding post has "couples massage the evening before". The snowbird post offers a "snowbird package" with discounts (unverified). The sports post mentions "cupping" (unverified). The group post claims "two to fifteen therapists".
- **Slugs dropped the category folder** (`/blog/health/…` → `/blog/…`). Fine, but each needs a 301 (§7).
- Author is the Organization (should be Dani). There's no visible date or byline. "Keep reading" just shows the first 3 posts, not related ones.

*Fix:* re-import the full approved text of all 15 live posts (Drive blog folder `1vJR5ejj_TI5_FtaalMJRT78WUsvlWNbW`), change `body: string[]` to support headings and FAQ blocks, show a byline and date, and pick related posts by category. Then:

| Post | Target keyword (vol) | Action |
|---|---|---|
| lymphatic-drainage-massage-maui-benefits | lymphatic drainage massage maui (90) | **Restore the full text first.** Retitle without "Detox … Maui's Best". Old GSC: 43 clicks, position 7.5. |
| swedish-vs-deep-tissue-massage-which-one-is-right-for-you | swedish vs deep tissue (1,300 national) | Restore full text. Add a comparison table. |
| couples-massage-maui-valentines-in-room-guide | couples massage maui (720) | Rewrite to the side-by-side rule (decision D2), or 301 it to the massage hub. |
| mobile-massage-pre-wedding-gift-maui | wedding massage maui (0; supports group) | Remove "the evening before". |
| benefits-of-booking-a-mobile-full-body-massage-in-maui | full body massage maui (GSC 48 impressions) | Restore. 551 impressions on the old site. |
| 7-surprising-health-benefits… | — | Restore and hedge every benefit. Cite sources or drop "research-backed". |
| sports-recovery-massage-maui, jet-lag, stiff-neck, snowbirds, group-massage-planning, mobile-massage-vs-hotel-spa | — | Restore full text, strip unverified offers and claims. |
| **lomi-lomi-vs-swedish-massage** (missing) | lomi lomi vs swedish (30) + supports lomi lomi (22,200) | **Re-add.** |
| **prenatal-massage-maui-babymoon-guide** (missing) | babymoon maui (590) | **Re-add.** Link from the prenatal page. |
| **massage-after-scuba-diving-maui** (missing) | massage after scuba diving (30); old GSC 370 impressions, position 8.8 | **Re-add** with Andrew's DCS-proportionality edits. |

Blog index title is 80 characters; cut to `Maui Massage & Wellness Blog \| Aloha Life` (41). Drop "Maui's top-rated" from the meta.

---

## 6. Content gaps worth building (after the P0s)

Ordered by measured demand × fit. All need Dani/Andrew sign-off before writing.

1. **Couples & group massage page** (couples massage maui 720 + couples massage maui hawaii 720). The old site has `/services/group-bookings/`, which isn't in the new IA. Needs decision D2 on how couples is worded.
2. **Lymphatic drainage massage page** (90 + 30, plus near-me demand), only if it's a bookable service (D3).
3. **Gift certificates page.** The old page converts at 13% CTR. Low volume, high intent.
4. **Contact page** with phone, hours, areas and the booking link (a NAP anchor for local SEO).
5. **"Best spa in Maui" style guide content** (720) as a blog post, positioned honestly (mobile vs resort spa) without naming competitors.
6. **Makawao / Upcountry area page** (90), if served.

---

## 7. Redirect map (server-side 301s at cut-over)

Old live URLs from the Yoast sitemaps (fetched 2026-11-25), mapped to the new routes. Paths are relative. Keep trailing-slash variants.

| Old URL | New URL | Note |
|---|---|---|
| / (incl. `?utm_…GMB`) | / | Keep the GBP UTM link working |
| /services/ | /massage-services-maui | 1,790 impressions |
| /services/swedish-mobile-massage/ | /massage-services-maui/swedish-massage | |
| /services/deep-tissue-mobile-massage/ | /massage-services-maui/deep-tissue-massage | |
| /services/therapeutic-mobile-massage/ | /massage-services-maui/therapeutic-massage | |
| /services/lomilomi-mobile-massage/ | /massage-services-maui/lomi-lomi-massage | 585 impressions |
| /services/sports-mobile-massage/ | /massage-services-maui/sports-massage | |
| /services/hot-stones-mobile-massage/ | /massage-services-maui/hot-stone-massage | |
| /services/premium-mobile-massage-therapy-services/ | /massage-services-maui/premium-vip | |
| /services/group-bookings/ | new couples/group page, else /massage-services-maui#bundles | See §6 |
| /services/mobile-massage-add-ons/ | /massage-services-maui#bundles | |
| /services/gift-certificates/ | new gift page, else / | See §6 |
| /services/benefits-of-massage/ | /blog/7-surprising-health-benefits-of-booking-a-mobile-massage-in-maui | |
| /about-us/, /our-team/, /meet-the-team/ | /about | 1,416 + 1,552 impressions |
| /meet-the-team/join-our-team/ | /join-our-team | |
| /testimonials/ | /reviews | |
| /contact/, /appointments/ | new /contact (else /) | |
| /privacy-policy/, /terms-conditions/ | new pages | Required |
| /blog/ | /blog | |
| /blog/<category>/<slug>/ (15 posts) | /blog/<slug> | Same slug for all 15 once the 3 missing posts are restored |
| /shop/, /cart/, /checkout/, /my-account/, /best-deals/, /sample-page/ | 410 or / | WooCommerce leftovers |
| /couples-massage-maui, /microneedling-maui, /microchanneling-maui, /service-areas/{kahului,wailuku,hana}, /premium-mobile-massage-therapy-services | as in App.tsx | Convert from `<Navigate>` to real 301s |

After launch: GSC change of address (if the domain changes), resubmit the sitemap, update the GBP website and the Acuity "return to site" link, and check the 301s with a crawl.

---

## 8. Decisions needed (from Shawn / Dani)

| # | Decision | Why it matters |
|---|---|---|
| D1 | **Domain and business name.** alohalifemassage.com (keeps 7 years of equity, simplest) vs alohalifemobilespa.com (needs a full move). And "Aloha Life Massage" vs "Aloha Life Mobile Spa" vs "Aloha Life Mobile Massage & Spa" (the logo). | NAP must match the GBP exactly. Keeping the current domain carries far less risk. |
| D2 | **How do we describe couples bookings?** A review says "my husband and I both got massaged by two lovely therapists", so two massage therapists at once does happen. The 2026-06-17 note says side-by-side "is not the case". | Unlocks a 720–1,440/mo keyword cluster. Fixes the Valentine's/wedding posts and the area-page FAQs. |
| D3 | Is **lymphatic drainage** a bookable service? | The best non-brand asset on the old site. It may deserve a service page. |
| D4 | Are **Paia, Haiku, Makawao/Upcountry** served, and what are their travel fees? | Area pages exist (Paia, Haiku) or are worth building (Makawao). |
| D5 | **Licence facts:** Dani's and each contractor's Hawaii licence numbers, whether "570 hours / no MBLEx" is accurate, esthetician licences, and microneedling scope. | These claims appear sitewide. Hawaii may require licence numbers in massage advertising (CLIENT.md §2, *confirm*). |
| D6 | **Waxing:** keep or remove, real prices, and the booking method. | P0-9 |
| D7 | **Retreats:** hide until dates are real? | P0-10 |
| D8 | **Hosting:** can Lovable serve prerendered HTML and server 301s, or do we deploy elsewhere? | P0-1, P0-4 |

---

## 9. Suggested order of work

1. **Before launch (P0):** prerender/SSR → 301 map → real 404s → forms wired → GTM/GA4 → full blog migration (15 posts) → waxing/retreats fixes → "therapist" sweep → remove "guaranteed" and unverified claims → domain/NAP swap → remove `noindex`.
2. **Launch week:** GSC (sitemap, change of address if any, URL inspection of the top 20 pages), GBP website update, crawl to verify the 301s, PageSpeed check.
3. **First 30 days (P1):** retarget the homepage and area-page titles/H1s (§5.1, §5.8), shorten every title to ≤60 characters, schema clean-up (§3), expand the 7 massage pages (§5.3), lomi lomi and prenatal/babymoon upgrades.
4. **30–90 days:** couples/group page (after D2), gift certificates, contact, lymphatic page (after D3), PAA-driven FAQ expansion (top up Semrush units first), real photos sitewide.

**Reusable component:** §3's "copy-rule violations" list and §7's redirect table are templates for any Lovable/SPA migration. Copy them into the next client migration checklist.
