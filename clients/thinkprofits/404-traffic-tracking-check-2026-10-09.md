# thinkprofits.com: 404 traffic and GA4 tracking check

> **Status:** Partial, 2026-10-09. Prepared by Francis (with Claude).
> **Why:** The monthly GA report (Sept 8 to Oct 5) showed traffic down about 43% month over month (3.0K active users). The 404 page was the #2 most-viewed page, with 149 views and a 90% bounce rate.
> **Context:** Google's September spam update was still rolling out. Hold any conclusions about lost rankings until it settles.
> **Answer:** the 404 views were bots hitting old WordPress URLs, and those URLs already 301 correctly. The traffic drop is unengaged Direct traffic falling away; real traffic is roughly flat. Details are in the GA4 section below.

## Sources (all pulled 2026-10-09)

- Google Search Console `sc-domain:thinkprofits.com`:
  - Pages, 2026-07-01 to 2026-10-07 (325 URLs).
  - Pages compared month over month: 2026-09-08 to 10-05 against 2026-08-11 to 09-07.
- HTTP status checks with curl on 50 URLs: top-traffic pages, legacy slugs, slugs with or without a trailing slash, and typo slugs.
- A browser check of the GA4 and GTM tags on 6 page templates.

## Tracking: working

- These pages load GTM container `GTM-KWN9KF`, which fires GA4 `G-BS5YJWQF03`:
  - homepage
  - `/seo-company-vancouver/` (city page)
  - `/digital-news/llms-txt-guide/` (blog post)
  - `/case-study/golf-ball-planet/` (case study)
  - `/contact/`
  - the 404 page
- On every one of those pages, the GA4 pageview hit (`g/collect`) was sent.
- The 404 page is tracked. Its title is "Page Not Found | ThinkProfits.com" and it is set to `noindex, nofollow`.
- No sign that a recent site update broke tracking.

**Side issues found:**

- GTM still loads Universal Analytics (`analytics.js`). UA stopped collecting data in 2024, so the tag is dead weight. Remove it from GTM.
- `www.thinkprofits.com` redirects to the non-www site with a **302** (temporary). It should be a **301** (permanent). The Google Business Profile link points to the www homepage with UTM tags, so it goes through this redirect.

## Broken URLs

| URL | Status | Search Console impressions (Jul–Oct) | Suggested fix |
|---|---|---|---|
| `/pcc-agency-abbotsford/` | 404 | 1 | 301 to `/ppc-agency-abbotsford/` (a "pcc" typo) |

Only 1 of the 50 URLs checked returns a real 404, so organic search is **not** what's feeding the 404 page.

How the site handles URLs that don't exist:

- **Unknown top-level paths** (for example `/something/`): return a true 404 and show the "Page Not Found" page. This is the only kind of URL that shows up as 404 views in GA4.
- **Unknown `/digital-news/<slug>/`:** 301 to `/digital-news/`.
- **Unknown `/case-study/<slug>/`:** the server returns **200**, then the browser jumps to `/portfolio/`. This is a soft 404, and Google may flag these pages in Search Console. Worth fixing so they return a real 404, or a 301 for known old slugs.
- Legacy paths already redirect correctly:
  - `/aeo-services/*` → `/geo-services/aeo/*`
  - `/case-studies/*` → `/case-study/*`
  - old blog slugs → their new slugs

**Possible lead (not confirmed):** Search Console lists spam-style referral URLs, for example `www.thinkprofits.com/?ref=littlepicturebooks922` and `/web-design-services/responsive-web-design-development/?ref=littlepicturebooks918`. If GA4 shows the 404 views coming from odd referrers, spam or bot traffic is the likely cause. That would also mean part of the 43% drop is junk traffic, not real visitors.

**Organic search context:** Search Console clicks are small on both sides. The homepage got 24 clicks against 30 the month before. Most service pages lost about 50% of their impressions month over month, for example:

- `/seo-company-vancouver/`: 39.7K → 19.1K
- `/services/`: 20.6K → 11.2K
- `/seo-services/`: 12.6K → 6.3K

Clicks barely moved, so the 3.0K-user decline is mostly coming from somewhere other than organic search.

## GA4 404 breakdown (added 2026-10-09, property `properties/253466203`)

Filtered on page title "Page Not Found | ThinkProfits.com", 2026-09-08 to 2026-10-05: **123 views** across 81 different paths. No single bad link is behind it.

**The 404 hits look like bots, not people:**

- **Source:** 117 of 123 views came from (direct) / (none) with no referrer. The only real referrers were chatgpt.com (2), wiseworth.com (2), johnsadler.ca (1) and search.google.com (1).
- **Device and visitor type:** 115 of 123 on desktop, and 117 from new users.
- **Countries:** United States (43), Singapore (36), Vietnam, China and the Philippines.
- **Timing:** views came in bursts. There were 28 on Sep 8 and 57 between Sep 16 and 19. From Sep 24 onward, almost none (1–2 a day at most).
- **Paths:**
  - Mostly old WordPress URLs, for example:
    - `/almost-everything`
    - `/case-studies/lone-star-plumbing-heating`
    - `/cloud-services`
    - `/plumber-marketing`
    - `/blog?category=...`
    - `/careers/...`
    - `/our-team`
  - Plus vulnerability probes, for example `/@fs/proc/1/environ` and `/__debug__`.

**The 404s are already fixed.** All 14 top paths I re-checked now return a 301 to the right new page. The bursts stop around Sep 23–24, which fits redirects added around then. **No new 301s are needed from this data.** The one exception is the `/pcc-agency-abbotsford/` typo above.

**The 43% traffic drop is mostly bot traffic leaving, not real visitors.** Active users by channel, Aug 11–Sep 7 compared with Sep 8–Oct 5:

| Channel | Active users | Engaged sessions |
|---|---|---|
| Direct | 4,976 → 2,858 | 217 → 206 |
| Organic Search | 132 → 123 | 95 → 84 |
| Referral | 45 → 38 | 45 → 38 |
| AI Assistant | 15 → 20 | 11 → 17 |
| Email | 9 → 7 | 7 → 5 |

The whole drop is in Direct, and engaged sessions there held steady. Fewer than 5% of Direct "users" engage, which suggests bot or spam traffic. Real, engaged traffic is roughly flat, and AI Assistant traffic is up. Consider a GA4 bot or internal-traffic filter so monthly reports aren't inflated by Direct traffic.

## Lovable redirect map check (added 2026-10-09)

Source: Lovable project `12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17` ("Thinkprofits Rebuild - shawn"). I only read the code and changed nothing. I then checked the findings against the live site.

**How redirects work on the site:**
- The redirect list lives in `vercel.json`: 797 rules, all marked permanent (301).
- Vercel isn't what applies them. The app's own server code reads the list on every request (`src/lib/redirects.ts`, run from `src/server.ts`).
- Matching ignores letter case, works with or without a trailing slash, and keeps any query string.
- When two rules could match, the first one in the list wins.
- The redirect list was most likely last changed in the Lovable edit "Added missing 404 redirects" on 2026-09-23. That fits the 404 hits stopping around Sept 23–24.

**The 404 URLs from GA4:** 22 of the 24 top 404 paths have a working 301. Two have no rule and still return a 404:
- `/plumber-marketing/plumber-pricing-packages/`
- `/pcc-agency-abbotsford/`

**Problems in the redirect map (all confirmed on the live site):**

1. **`/blog/:path+` catches 34 more specific rules.** The `/blog/:path+` catch-all is rule #30 and sends everything to `/services/`. The 34 rules after it for specific `/blog/...` pages never get a chance to run, including:
   - every `/blog/case-studies/*` and `/blog/testimonial/*` rule
   - old blog posts that should land on their `/digital-news/` articles

   Example: `/blog/case-studies/golf-ball-planet/` goes to `/services/`, not to the Golf Ball Planet case study. **Fix:** move `/blog/:path+` below the specific `/blog/` rules.
2. **Redirects that point to case studies that don't exist.** These end on a soft 404 that jumps to `/portfolio/`:
   - `/case-studies/eurorite-cabinets/` points to `/case-study/eurorite-cabinets/`, but the real slug is `euro-rite-cabinets`.
   - `/case-studies/plugbusters/` points to `/case-study/plugbusters/`, but there is no Plugbusters case study, even though a hero image for it exists. Search Console shows 13 impressions for `/case-study/plugbusters/`.
3. **Redirects that point to blog posts that don't exist.** They take two redirects and end on the `/digital-news/` blog index:
   - `/digital-news/canonicalization/`
   - `/digital-news/what-is-the-difference-between-google-webmaster-tools-and-analytics/`
4. **Missing trailing slash.** Three cyber-monday rules point to `/ecommerce-website-design` without the slash, which adds a second redirect.
5. **www to non-www goes live as a 302, not a 301.** Rule #0 in the redirect list says 301, but the live site answers with a 302. So the www redirect is being applied before the app runs, most likely in the Lovable domain settings or Cloudflare. It also means `www.../our-team` takes two redirects: 302, then 301.
6. **Weak destinations.** Many old pages land on general hub pages when a closer page exists. Example: `/plumber-marketing/` goes to `/seo-services/` even though `/seo-services/local-seo/local-seo-plumbing/` exists. The `/hosting-services/*` pages go to store.thinkprofits.com.
7. **Soft 404 for unknown case studies.** An unknown `/case-study/<slug>` returns a 200, then the browser jumps to `/portfolio/` (`<Navigate>` in `src/pages/CaseStudy.tsx`). Unknown `/digital-news/<slug>` pages correctly send a server-side 301.

No redirect loops found.

## Not done yet

1. ~~GA4 404 breakdown~~: done, see above. GA4 is now connected to Claude Code through the `ga4` MCP server (`mcp-servers/ga4/`).
2. **Search Console "Not found (404)" report and the pages linking to those URLs.** The Search Console API doesn't provide this report. Export it from the Search Console UI under Pages → Not found (404).
3. **Semrush Site Audit for broken internal links.** Blocked on 2026-10-09: the account doesn't have enough Semrush API units. Rerun once units are added.

## Next decisions

- Which URLs get 301s, once items 1 and 2 above are in.
- Change the www → non-www redirect from 302 to 301.
- Make unknown `/case-study/` slugs return a real 404 instead of the soft 404.
- Remove the dead UA tag from GTM.
