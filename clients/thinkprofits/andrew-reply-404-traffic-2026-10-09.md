**Subject: thinkprofits.com: 404 spike and traffic drop, run down**

Hi Andrew,

Short version: the 404 spike was bots hitting old WordPress URLs, and Shawn's Sept 23 redirect update already fixed most of them. Tracking is fine. Most of the 43% drop is unengaged "Direct" traffic going away, not real visitors. While checking the redirects in Lovable I found a few fixes worth making, and I've drafted the Lovable instructions for them.

**1. GA4: 404s by landing page and source (Sept 8 – Oct 5)**

- The "Page Not Found" page had **123 views at an 88% bounce rate** across **77 landing pages**. GA4 shows 123 now rather than 149, probably because data finished processing after the report was pulled. No single bad link drives it.
- The most-hit URLs were all old WordPress paths:

| Old URL | Views | Now |
|---|---|---|
| /almost-everything | 5 | 301 → /services/ |
| /careers/senior-digital-ads-specialist | 4 | 301 → /about/ |
| /case-studies/lone-star-plumbing-heating | 4 | 301 → /case-study/lone-star-plumbing-heating/ |
| /cloud-services | 4 | 301 → store.thinkprofits.com |
| /plumber-marketing | 4 | 301 → /seo-services/ |
| /blog?category=… (5 categories) | 14 | 301 → /digital-news/?category=… |
| /case-studies/sprott-shaw-college | 3 | 301 → /case-study/sprott-shaw-college/ |
| /plumber-seo | 3 | 301 → /seo-services/ |
| /plumber-marketing/plumber-pricing-packages/ | 2 | **still 404** |

- **Source:** 117 of the 123 views came in as direct traffic with no referrer. The only real referrers were ChatGPT (2), wiseworth.com (2), johnsadler.ca (1) and Google Search Console (1).
- **Why we think it's bots:**
  - 94% desktop and 95% new users, mostly from the US and Singapore.
  - The views came in two bursts (Sept 8 and Sept 16–19).
  - Some requests were security probes, like `/@fs/proc/1/environ`.
- The 404 hits drop to almost nothing after the Sept 23 redirect update.

**2. Search Console: "Not found (404)"**

- Search Console lists **106 URLs as 404**, crawled between April and Oct 4. The count jumped from 89 to 115 during Sept 15–19, the same bot bursts we see in GA4.
- Checked live today:
  - **81 now redirect** to working pages.
  - **4 have since been published**.
  - **25 still 404**. Those are mostly old WordPress month archives and category pages (e.g. `/digital-news/2015/08/`), plus a test page and an admin path.
- One oddity: `/seo-services_/local-seo_/local-seo-pest-control`, crawled Oct 4. The underscores look like internal route names that got published as a link at some point. It's covered in the Lovable fix.
- The export doesn't show which pages link to these URLs. They're old WordPress URLs that Google keeps re-checking from its own history, not links on the current site.

**3. Tracking**

- I checked six page templates: homepage, city page, blog post, case study, contact and the 404 page. All load GTM (GTM-KWN9KF) and send the GA4 pageview (G-BS5YJWQF03).
- Nothing broke tracking in a recent update.

**About the 43% drop**

| Channel | Active users (prev. 4 wks → Sept 8–Oct 5) | Engaged sessions |
|---|---|---|
| Direct | 4,976 → 2,858 | 217 → 206 |
| Organic Search | 132 → 123 | 95 → 84 |
| AI Assistant | 15 → 20 | 11 → 17 |

- The whole drop is in Direct, where fewer than 5% of visitors engage. Engaged sessions held steady, and AI assistant traffic is up.
- Agreed on holding off on ranking conclusions until the spam update finishes. Search Console impressions on the main service pages did fall about 50% month over month, so that's worth rechecking once it settles.

**Redirect fixes (from checking the redirect map in Lovable)**

I read the site's redirect setup in Lovable (797 rules) and checked it against the live site and the Search Console list:
- **Rule-order bug:** a catch-all for `/blog/` sits above 34 more specific rules, so old blog and case-study URLs all land on /services/ instead of their real pages. For example, `/blog/case-studies/golf-ball-planet/` goes to /services/.
- **Missing 301s:**
  - `/plumber-marketing/plumber-pricing-packages/`
  - the `/pcc-agency-abbotsford/` typo
  - the old WordPress blog archive, category and pagination pages
  - the underscored pest-control URL
- **Redirects pointing to pages that don't exist:**
  - the Euro-Rite case study uses the wrong slug
  - Plugbusters has a redirect but no case study
  - two old posts point to articles that were renamed
- **Broken case-study URLs return a 200, then jump to /portfolio/.** Google can flag that as a "soft 404". It should be a real server-side redirect.
- **www → non-www is a 302 (temporary), not a 301.** The redirect rule is set to 301, so the 302 is likely coming from the domain or Cloudflare settings. Our Google Business Profile link goes through this redirect.

I've drafted one Lovable message covering all of these (`clients/thinkprofits/lovable-message-redirect-fixes-2026-10-09.txt`). It's ready to send once you're happy with it.

**Also worth doing**

- Remove the old Universal Analytics tag from GTM. It stopped collecting data in 2024.
- Add a GA4 bot filter so Direct traffic doesn't inflate the monthly numbers.

Full notes and data: `clients/thinkprofits/404-traffic-tracking-check-2026-10-09.md`.
