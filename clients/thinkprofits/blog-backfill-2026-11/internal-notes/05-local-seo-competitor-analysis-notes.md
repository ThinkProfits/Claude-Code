# 05 local-seo-competitor-analysis: internal notes

**Scope:** How-to guide (six steps) for running a local SEO competitor analysis in Vancouver: find who actually ranks for money terms by location, then compare GBP categories, reviews, service/location pages, links and citations, and turn gaps into a ranked fix list. Fills backfill topic #5, week of Oct 20, 2026. No real competitors named; all examples generic.

## Sources checked

| URL | What it confirmed |
|---|---|
| https://support.google.com/business/answer/7091 (Tips to improve your local ranking) | Local results mainly based on relevance, distance, prominence; more reviews and positive ratings can help local ranking; helpful replies help a business stand out; prominence includes how many websites link to a business; no way to request or pay for better local ranking. **Linked in post.** |
| https://support.google.com/business/answer/7249669 (Manage your business category) | Primary category should be the most specific that describes the business; additional categories for departments/services; "The categories you select affect your local ranking on Google"; avoid a category for every service. **Linked in post.** |
| https://support.google.com/business/answer/3038177 (Guidelines for representing your business) | Business name must reflect real-world name; unnecessary info in name not permitted; use as few categories as possible; categories not to be used as keywords. Referenced by name, not linked (2-external-link cap). |
| https://support.google.com/contributionpolicy/answer/7400114 + Google transparency report (search result summaries) | Paid/incentivised reviews prohibited; repeated fake engagement can lead to restrictions on a Business Profile. Stated generally in post, not linked. Policy page notes a recent update; re-check wording before reuse. |

Voice references read: `/digital-news/local-business-entity-consistency-ai-search/`, `/digital-news/canonical-url-qa-lovable-headless-launches/`. Neither has an FAQ block; brief requires one, so FAQ kept.

## Claims cut or softened

- Cut: description of where the primary category appears on the profile (UI detail not verified on a Google page).
- Cut: specific statistic from Google transparency report (188M reviews removed in 2024): seen only in search summary, not fetched from the primary page, and not needed.
- Softened: claims about ThinkProfits' own process ("the method we use", "our team runs competitor reviews", "most businesses we review") to avoid unverifiable service/case claims. Kept "local SEO work usually starts with existing core pages" (matches the agency's core-pages-before-niche strategy).
- Softened free SEO audit tool description to "a quick read on technical and on-page issues" (did not verify tool's runtime or exact checks).
- Cut a FAQ ("Do I need paid tools?") for length.

## Keyword data (google-ads-keywords MCP, Canada, geo 2124, Nov 2025 to Oct 2026)

| Keyword | Avg monthly (CA) |
|---|---|
| local seo competitor analysis | 10 |
| seo competitor analysis (close variant: competitor analysis seo) | 110 |
| local competitor analysis | 10 |
| local seo analysis | 20 |
| local seo audit | 30 |
| local pack ranking | 10 |
| google business profile categories | 10 |
| google business profile reviews | 70 |
| local citations | 50 |
| local seo vancouver | 320 |
| how to rank higher on google maps | 20 |
| google maps ranking factors | 10 |

Primary keyword is low volume; the post's value is topical support for `/seo-services/local-seo/` and long-tail capture. PAA: no reliable PAA scrape available via web search; FAQ questions are PAA-style questions inferred from top-ranking guides and common query patterns (finding competitors, frequency, fewer-reviews-ranks-higher, copying categories).

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml (301 URLs) on 2026-11-25 for "compet", "rival", "benchmark", "gap", "local", "audit", "rank". No existing post targets "local seo competitor analysis" or competitor analysis generally. Closest neighbours (linked or differentiated, not overlapping): `local-seo-geo-grid-report-vancouver` (how to read grid reports; linked from Step 1), `reviews-local-entity-signals-vancouver` (linked from Step 3), `how-to-do-an-seo-audit-in-2026` and `marketing-audit-vs-seo-audit-vancouver` (audit scope, not competitor comparison). Clear to publish.

## Internal links used (9 distinct)

`/seo-services/local-seo/`, `/seo-audit/`, `/free-seo-audit-tool/`, `/contact/`, `/digital-news/local-seo-geo-grid-report-vancouver/`, `/digital-news/reviews-local-entity-signals-vancouver/`, `/digital-news/service-page-location-page-blog-post/`, `/digital-news/city-landing-page-cannibalization-search-console/`, `/digital-news/local-business-entity-consistency-ai-search/`.

## Image note

One hero image only: site placeholder `/images/blog/wp/tp-branded-placeholder.jpg`, alt "Local SEO competitor analysis worksheet comparing Vancouver map pack results". If replaced later, use a real screenshot of a (blurred/anonymised) worksheet or map pack; never show a real competitor's name, never AI imagery.

## Implementation notes

- No JSON-LD in draft; Lovable layout outputs Article, FAQPage and Breadcrumb from the FAQ block.
- Publish date: Oct 20, 2026 (backfill week).
- External links open in new tab (`target="_blank" rel="noopener noreferrer"`).
- Semrush is mentioned as a tool for referring-domain research (agency tool of record); no specific Semrush feature claims made.

## GBP post (ThinkProfits Vancouver)

Who shows up when Vancouver customers search for what you sell? It is often not the competitor you have in mind. Our new guide walks through a local SEO competitor analysis step by step: find who Google actually shows for your money terms, then compare categories, reviews, service pages and links so you know which gaps to close first. Read the guide or book a free 30-minute consultation.

CTA button: Learn more → [blog URL]

## LinkedIn

The businesses you lose quotes to are not always the ones beating you in the map pack. We put together a six-step local SEO competitor analysis for Vancouver businesses: start with who Google actually shows from your customers' locations, then compare categories, reviews, pages and links, and rank the fixes by effort. [blog URL] #LocalSEO #VancouverBusiness

## Facebook

Ever wonder why another business keeps showing up above you on Google Maps? Our latest guide walks through a simple local SEO competitor analysis you can run with a spreadsheet and an afternoon. [blog URL] #LocalSEO

## Review 2026-11-25 (fresh-eyes editor)

- Links: every internal link returned 200 with no redirect on thinkprofits.com (the site 301s unknown URLs, so 200 = real page); posts not in the brief list were confirmed in sitemap.xml. External Google links resolve 200.
- Spelling: -ize kept per Canadian Press (brief's -ise line ignored by instruction). No em/en dashes found.
- Category example "Emergency locksmith service" vs "Locksmith" replaced with Google's own documented example ("Nail salon" vs "Salon"); could not confirm the locksmith category name exists.
- Fake-review consequence reworded to match the policy page: prohibited, incentivized reviews removed, account privileges can be restricted for violations (the original "profile can face restrictions" overstated what the fetched page says).
- Image line fixed: file now points to /images/blog/wp/tp-branded-placeholder.jpg (was an invented filename).
- "## FAQ" renamed "Frequently asked questions" for consistency; CTA moved from H3 to H2 so it is not parsed as a FAQ question.
- Meta was 150 (bottom edge); extended to 159.
- Facts re-verified on 7091, 7249669 ("The categories you select affect your local ranking", pick a specific category, not one per service), 3038177 (real-world name, as few categories as possible), contributionpolicy 7400114.
