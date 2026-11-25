# 03 map-pack-vs-organic-rankings: internal notes

**Scope:** Explainer/how-to comparing map pack and organic results: what drives each (per Google's local ranking factors), how to attribute calls and forms to each (GBP performance, UTM-tagged profile link in GA4, Search Console), and what to fix when either side is weak. Fills backfill row #3 (week of Oct 6, 2026).

**H1 note:** H1 shortened from the brief's working title ("...How Vancouver Leads Actually Arrive") to match the 56-char title tag exactly ("Actually" pushed the tag past 60).

## Sources checked

| URL | What it confirmed |
|---|---|
| https://support.google.com/business/answer/7091 | Local results based mainly on relevance, distance, prominence; prominence includes links and reviews/ratings ("More reviews and positive ratings can help"); no way to request or pay for better local ranking. (External link 1) |
| https://support.google.com/business/answer/9918094 | Performance metrics: calls (taps on call button), website clicks, directions, messages, bookings, searches; covers Search and Maps; searches metric updates at start of each month (up to 5 days); performance data only for verified profiles. (External link 2) |
| https://support.google.com/analytics/answer/10917952 | GA4 manual UTMs; should always use utm_source, utm_medium, utm_campaign; parameter values are case sensitive. (Not linked, cited in notes only to stay at 2 external links.) |
| Live posts: local-business-entity-consistency-ai-search, canonical-url-qa-lovable-headless-launches | Voice reference. |

## Claims cut or softened (unverifiable)

- Any statement on whether Search Console counts clicks from local pack / GBP website links. Google's docs are not explicit and secondary sources disagree, so the post only says GSC covers organic queries/pages and UTMs separate profile visits in GA4.
- "Map pack gets X% more clicks/actions than organic" type stats (seen on vendor blogs, no primary source).
- GBP call history (feature retired; not mentioned).
- Advice on using a tracking number as the GBP primary number (policy detail not re-verified; post recommends call tracking on the website only).
- "Ads are labelled sponsored" detail removed; kept only Google's "no way to pay for local ranking".
- Organic ranking column in the table kept generic (no claimed Google factor list).
- "Organic is less sensitive to searcher position" framed as "in our experience".

## Keyword data (google-ads-keywords MCP, Canada, Nov 2026)

| Keyword | Avg monthly (CA) |
|---|---|
| map pack vs organic | 0 (no data) |
| local pack vs organic | 0 |
| google map pack | 50 |
| google maps ranking | 30 |
| local pack | 20 |
| google business profile insights | 20 |
| map pack seo | 10 |
| local seo vs organic seo | 10 |
| google 3 pack | 10 |
| local search ranking factors | 10 |
| how to rank in google map pack | 10 |

Primary keyword kept per brief despite near-zero measured volume; the post's value is topical/AEO coverage and the secondaries. Consider "google map pack" as an editor's alternative focus.

**PAA-style questions folded into FAQ:** Is the map pack the same as organic? Does my website affect map pack ranking? How do I know if a lead came from Maps or organic? Why do I rank near my office but not across town? Can I pay to rank higher?

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml. No post targets "map pack vs organic". Adjacent posts, differentiated and linked rather than repeated:
- `maps-pack-still-wins-local-ai-overviews-8-percent` (AI Overviews vs maps pack; no ranking-factor or attribution comparison). Not linked: it carries an unsourced 8% stat; recommend sourcing or revising that post.
- `utm-parameters-canonicals-local-seo-reporting` (UTM naming incl. GBP tagging; linked for the how-to, not repeated).
- `local-seo-geo-grid-report-vancouver`, `vancouver-local-seo-report` (reporting; geo-grid linked).

## Internal links used (10 distinct)

/seo-services/local-seo/, /digital-marketing-reporting/, /free-seo-audit-tool/, /contact/, /digital-news/local-seo-geo-grid-report-vancouver/, /digital-news/utm-parameters-canonicals-local-seo-reporting/ (confirmed in sitemap), /digital-news/reviews-local-entity-signals-vancouver/, /digital-news/google-business-profile-posts-local-seo/, /digital-news/service-page-location-page-blog-post/, /digital-news/city-landing-page-cannibalization-search-console/

## Image note

Hero only: `/images/blog/wp/tp-branded-placeholder.jpg`, alt "Google search results page showing a local map pack above organic website listings". No AI or stock screenshots of real competitors' listings.

## GBP post (ThinkProfits Vancouver)

Is your Vancouver business getting calls from the map pack, from organic search, or both? They rank on different signals, and most reports blend them into one number. Our new guide explains how to separate map pack vs organic leads using your Business Profile performance, a UTM-tagged website link and Search Console, plus what to fix on each side. Read the guide and book a free 30-minute consultation if you want a second set of eyes. [CTA: Learn more > blog URL]

## LinkedIn

"Our Google ranking" is usually two rankings: the map pack ranks your Business Profile on relevance, distance and prominence, while organic results rank your web pages. We wrote up how Vancouver businesses can tell which one is actually sending calls and forms, and what to fix when one side lags. [blog URL] #LocalSEO #Vancouver

## Facebook

Ranking on Google Maps but not in the regular results, or the other way round? They run on different rules. Here is how to see which one brings your leads and where to focus first. [blog URL] #LocalSEO #VancouverBusiness

## Implementation notes

- Schema: Lovable layout outputs Article, FAQPage and Breadcrumb from the FAQ block; no JSON-LD in draft.
- Publish date: backfill for week of Oct 6, 2026.
- The closing CTA sits below a horizontal rule rather than its own H2 to keep H2 count at 7 (6 body + FAQ).
- Word count ~1,770 (body, excl. metadata and image note).

## Review 2026-11-25 (fresh-eyes editor)

- Links: every internal link returned 200 with no redirect on thinkprofits.com (the site 301s unknown URLs, so 200 = real page); posts not in the brief list were confirmed in sitemap.xml. External Google links resolve 200.
- Spelling: -ize kept per Canadian Press (brief's -ise line ignored by instruction). No em/en dashes found.
- Internal links converted from absolute https://thinkprofits.com/ URLs to relative paths to match the rest of the batch.
- Meta rewritten (153): removed "Book a free call", which is not one of the two approved offer phrasings.
- Closing section had no heading (only a rule); added H2 "Measure first, then fix" and removed the "is not a contest you pick a side in" construction (it's-not-X tell).
- CTA softened ("walk through where your leads are coming from" implied a free audit) and the free SEO audit tool mention now links to /free-seo-audit-tool/.
- "Contradictions make it harder for Google to trust..." was unsourced; now tied to Google's stated line that complete and accurate info helps local visibility.
- "most of those visits blend into google / organic" hedged to "typically" (behaviour of untagged GBP clicks is not documented by Google).
- Facts re-verified on 7091 (relevance/distance/prominence, links and reviews, no paying), 9918094 (metrics, Search and Maps, monthly searches update, verified only), 10917952 (utm_source/medium/campaign, case sensitive).
- Human decision: primary keyword "map pack vs organic" shows 0 CA volume; consider "google map pack" (50).
