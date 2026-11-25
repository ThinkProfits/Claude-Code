# ThinkProfits blog backfill, November 2026: shared brief

**Why:** the last post on thinkprofits.com/digital-news/ is dated 2026-09-21. The ChatGPT daily packages after that never reached Lovable (summary only, copy stuck in ChatGPT). Francis chose on 2026-11-25: **one post per missing week (10 posts, weeks of Sep 22 to Nov 24), real publish dates, released a few per week.** Topics are picked from ChatGPT's planned list, keeping evergreen ones and dropping unverifiable "news" items and anything that overlaps existing posts.

**Reusable:** this brief is the template for any future ThinkProfits blog batch. Change the topic table, keep the rules.

## Site facts (thinkprofits.com, our own site)

- ThinkProfits, Vancouver, BC digital marketing agency: SEO, AEO, GEO, PPC (Google Ads), web design (incl. Lovable builds), content, reporting, fractional marketing.
- Blog lives at `/digital-news/<slug>/`. Built in Lovable (React). 138 posts, last one Sep 21, 2026.
- Voice (study `/digital-news/local-business-entity-consistency-ai-search/` and `/digital-news/canonical-url-qa-lovable-headless-launches/`): first-person plural "we", plain and direct, practitioner tone, honest about limits ("this will not guarantee..."), tables and step lists welcome, no hype.
- Offers you may mention: **free 30-minute consultation** ("Book My Free Consultation" CTA to `/contact/`), the **free SEO audit tool** at `/free-seo-audit-tool/`. Do NOT offer free audits of any other kind (no free PPC/Google Ads audit, no free SEO audit by a person). No prices.

## Internal link targets (use real ones only)

Services: `/seo-services/`, `/seo-services/local-seo/`, `/seo-audit/`, `/aeo-services/` (note: `/geo-services/` 301s to `/aeo-services/geo/`; don't use it), `/ppc-advertising/`, `/content-writing-services/`, `/digital-marketing-reporting/`, `/digital-marketing-strategy/`, `/web-design-services/`, `/lovable-partner-agency/`, `/fractional-marketing-services/`, `/free-seo-audit-tool/`, `/word-counter/`, `/contact/`, `/about/`.
Related posts (all live, `/digital-news/<slug>/`): `local-business-entity-consistency-ai-search`, `google-business-profile-posts-local-seo`, `reviews-local-entity-signals-vancouver`, `canonical-url-qa-lovable-headless-launches`, `marketing-case-study-evidence-checklist`, `service-page-location-page-blog-post`, `brand-nonbrand-google-ads-budget`, `google-ads-location-targeting-vancouver`, `google-ads-lead-quality-loop`, `weekly-google-ads-change-log`, `ai-max-search-term-matching-vs-exact-phrase`, `local-seo-geo-grid-report-vancouver`, `city-landing-page-cannibalization-search-console`, `content-consolidation-without-traffic-loss`, `sitemap-hygiene-website-rebuild`, `aeo-prompt-testing-dataset`, `technical-seo-services-vs-audit`, `budget-limited-vs-demand-limited-google-ads`, `wikidata-business-eligibility`, `google-business-profile-post-views-test`. Before linking any other post, confirm it exists in https://thinkprofits.com/sitemap.xml.

## Hard rules

1. Canadian English (optimise, colour, centre, behaviour, licence as noun). Canadian examples only; no US programs or US-only stats.
2. **Never guarantee rankings, leads, citations or results.** No "will rank", "guaranteed", "#1".
3. **Every statistic and every claim about how a Google product works must be verified against a current primary source** (Google Search Central, Google Ads Help, Google Business Profile Help, GA4 Help, schema.org). Use WebSearch / web-fetch to confirm. If you can't confirm it, cut it. Cite the source with an external link (1–2 per post). Do not invent numbers, case results, client names or quotes. Do not describe product features you can't confirm are current.
4. No em dashes or en dashes anywhere. No AI tells (see agency-blog-writer skill list). No competitor agencies named.
5. 1,200–1,800 words. One H1, a Quick Answer (2–3 sentences, includes primary keyword), intro 100–150 words, 4–7 H2s, 3–5 FAQs with specific answers, closing CTA (free consultation and/or free SEO audit tool).
6. At least 5 distinct internal links (from the list above), 1–2 external authoritative links.
7. Title tag 50–60 chars, keyword first, may end "| ThinkProfits". Meta description 150–160 chars. Slug as given.
8. No JSON-LD in the draft (Lovable's layout already outputs Article, FAQPage and Breadcrumb schema from the FAQ block).
9. One image: hero placeholder note only (the site uses `/images/blog/wp/tp-branded-placeholder.jpg`); give alt text.

## Topics (release order)

| # | Week filled | Slug | Working title | Primary keyword | Category | Angle / must cover |
|---|---|---|---|---|---|---|
| 1 | Sep 22 | `answer-first-content-without-faq-dumping` | Answer-First Content Without FAQ Dumping: An AEO Guide | answer-first content | AI | How to structure pages so the answer comes first and sections stand alone, without bolting 20 FAQs on. Differentiate from existing FAQ-schema posts: this is about writing and page structure, not markup. |
| 2 | Sep 29 | `search-terms-vs-keywords-google-ads` | Search Terms vs Keywords in Google Ads: A Waste-Control Guide | search terms vs keywords | PPC | Difference between keywords and the search terms report, match types, how to read the report weekly, negatives, what "other search terms" hides. Link `ai-max-search-term-matching-vs-exact-phrase` without repeating it. |
| 3 | Oct 6 | `map-pack-vs-organic-rankings` | Map Pack vs Organic Rankings: How Vancouver Leads Actually Arrive | map pack vs organic | SEO | How local pack and organic results differ in what drives them, how to see which one sends calls/forms (GBP insights, UTM on GBP website link, GSC), what to fix for each. |
| 4 | Oct 13 | `primary-vs-secondary-conversions-google-ads` | Primary vs Secondary Conversions in Google Ads: A Lead-Gen Checklist | primary vs secondary conversions | PPC | What primary/secondary means for bidding vs reporting, common mistakes (page views as primary, duplicate form + thank-you), a governance checklist. |
| 5 | Oct 20 | `local-seo-competitor-analysis` | Local SEO Competitor Analysis: A Vancouver Step-by-Step | local seo competitor analysis | SEO | Identify who actually shows in your map pack/organic for money terms, compare categories, reviews, service pages, links, citations. Never name real competitors; use generic examples. |
| 6 | Oct 27 | `google-ads-ga4-crm-leads` | Why Google Ads, GA4 and Your CRM Disagree on Form Leads | google ads vs ga4 conversions | Analytics | Attribution models, counting settings, conversion dates, consent/ad blockers, spam leads; a reconciliation routine. Link `google-ads-lead-quality-loop`. |
| 7 | Nov 3 | `internal-linking-qa-checklist` | Internal Linking QA Checklist Before a Post Goes Live | internal linking checklist | SEO | Pre-publish QA: orphan check, anchor text, links to/from money pages, broken/redirecting links, nav vs contextual. |
| 8 | Nov 10 | `google-business-profile-suspension` | Google Business Profile Suspended? An Evidence Kit for Canadian Businesses | google business profile suspended | SEO | What suspensions are, common triggers per Google's guidelines, the documents to gather (business licence, utility bill, signage photos, etc. per Google's reinstatement guidance), how to file the reinstatement request. Verify every step against GBP Help. |
| 9 | Nov 17 | `value-based-bidding-service-businesses` | Value-Based Bidding for Service Businesses: When It Makes Sense | value-based bidding | PPC | Conversion values for lead gen, offline values, data minimums per Google docs, when Maximize Conversion Value/tROAS fits a service business and when it doesn't. |
| 10 | Nov 24 | `local-seo-office-move-checklist` | Moving Offices? A 30-Day Local SEO Checklist for Vancouver Businesses | local seo office move | SEO | GBP address change process, verification, website NAP + schema, citations, redirects for location pages, ads location extensions, what to expect. |

## Output per post (write to this folder)

- `NN-<slug>.md`: title tag (with char count), meta (with char count), slug, primary + secondary keywords, search intent, category, then the full post in Markdown (H1, `> **Quick answer:**` block, body, FAQ as `### Q` + answer, CTA). Inline links as Markdown with full paths.
- `internal-notes/NN-<slug>-notes.md`: scope line, sources checked (URL + what it confirmed), claims cut because unverifiable, keyword data source, cannibalisation finding, GBP post (for ThinkProfits Vancouver), one LinkedIn + one Facebook post.
