# 01 answer-first-content-without-faq-dumping: internal notes

**Scope:** How-to (AI category) on structuring pages so the answer comes first and each H2 stands alone, deciding which questions earn an FAQ, and trimming existing 20-question FAQ blocks. Writing and page structure only, not markup. Fills brief row #1 (week of Sep 22, 2026).

**Publish date:** 2026-09-22 (backfill, real week date per brief).

## Sources checked (all fetched 2026-11-25)

| URL | Confirmed |
|---|---|
| https://developers.google.com/search/updates#removing-faq-rich-result (linked) | Old FAQPage doc URL 301s here. Update log: deprecation notice added May 8, 2026, feature "will no longer appear in Google Search starting May 7, 2026"; FAQ rich result documentation removed June 15, 2026. |
| https://developers.google.com/search/docs/appearance/ai-features (linked; last updated 2025-12-10) | No additional requirements or special optimisations for AI Overviews / AI Mode; no special schema.org markup or AI text files needed; best practices incl. important content as text, internal links, structured data matching visible text; "Indexing and serving isn't guaranteed." |
| https://thinkprofits.com/digital-news/local-business-entity-consistency-ai-search/ and /canonical-url-qa-lovable-headless-launches/ | Voice reference: "we", dry practitioner tone, quick answer + tables, CTA "Book My Free Consultation" to /contact/, H3 for CTA box. |
| https://thinkprofits.com/sitemap.xml (301 URLs) | All internal links used are in the sitemap. |

## Claims cut / not used

- Any claim that answer-first content gets cited more by AI tools or wins featured snippets: no primary source. Post says explicitly it does not guarantee either.
- "Google still parses FAQPage markup for understanding" (made in our faq-schema-dead post): not found in Google docs. Not used.
- FAQ count benchmarks from third-party blogs (e.g. 3 to 5 per page, 7 to 10 per 2,000 words): not authoritative. The "three to five" figure is labelled in the post as our house convention, not a Google rule.
- Google Business Profile Q&A as a question source: removed because I could not confirm the feature is still live.
- No statistics used.

## Keyword data (google-ads-keywords MCP, Keyword Planner, Canada geo 2124, Nov 2025 to Oct 2026)

| Keyword | Avg monthly (CA) |
|---|---|
| answer-first content (primary; close variant "answer first content") | 10 |
| aeo | 2,900 (rising: 5,400 in Oct 2026) |
| answer engine optimization | 320 |
| ai search optimization | 140 |
| faq schema | 90 |
| aeo content | 10 |
| content structure for seo | 10 |
| inverted pyramid writing | 10 |
| featured snippet optimization | 10 |
| bluf writing / passage ranking | 10 each (not used) |
| how to write for ai overviews | 0 (dropped) |

Primary is low volume; the post is a supporting piece for the AEO cluster and /aeo-services/, not a traffic play.

**PAA-style questions folded into FAQ** (from web search on AEO page structure): is answer-first the same as inverted pyramid; do FAQs still help after FAQ rich results; how long should the opening answer be; should service pages have FAQs.

## Cannibalisation finding

No existing post targets "answer-first content". Closest neighbours checked:
- `/digital-news/how-to-make-content-quotable-by-ai/`: sentence-level quotability; "lead with the answer" is one of six patterns; recommends FAQ blocks and never warns about overuse. Differentiated (page structure + FAQ triage) and linked from the new post.
- `/digital-news/faq-schema-dead-what-gets-you-cited-by-ai/` and `/digital-news/faq-schema-ai-search-2026/`: about FAQ markup. New post is explicitly not about markup. Not linked (faq-schema-dead carries unsourced stats; flag for its own refresh).
- `/digital-news/aeo-home-services-answer-inventory/`: building an answer inventory for home services; different job.

## Internal links used (8 distinct)

/digital-news/how-to-make-content-quotable-by-ai/, /digital-news/service-page-location-page-blog-post/, /digital-news/aeo-prompt-testing-dataset/, /digital-news/content-consolidation-without-traffic-loss/, /free-seo-audit-tool/, /aeo-services/, /content-writing-services/, /contact/.

Note: the brief lists `/geo-services/`, but it 301s to `/aeo-services/geo/` and is not in the sitemap. Used `/aeo-services/` instead. Worth updating the brief.

## Image note

One hero only: `/images/blog/wp/tp-branded-placeholder.jpg`. Alt: "Answer-first content page layout with the answer at the top of each section". No AI-generated images.

## Implementation notes

- No JSON-LD in the draft; Lovable outputs Article, FAQPage and Breadcrumb from the FAQ block. Four FAQs.
- CTA box heading is H3 to match live posts; 7 H2s including the FAQ heading.
- Spelling follows the brief ("optimisations").

## GBP post (ThinkProfits Vancouver)

Is the useful answer on your service page sitting at question 14 of a FAQ accordion? Our new guide shows how to write answer-first content: put the reply at the top, make every section stand on its own, and keep only the three to five FAQs your customers actually ask. Read the guide and book a free 30-minute consultation if you want a second set of eyes. CTA: Learn more > [blog URL]

## LinkedIn

Plenty of pages we review hide their best answer in a 20-question FAQ block near the footer. Google stopped showing FAQ rich results in May 2026, so that block is no longer a shortcut to anything. Our new guide covers answer-first content: how to structure a page so each section stands alone, which questions earn an FAQ, and how to trim the ones you have. [blog URL] #AEO #ContentStrategy

## Facebook

If your website's answers live at the bottom of a long FAQ list, most visitors never see them. Here is how we restructure pages so the answer comes first and every section makes sense on its own. [blog URL] #SmallBusinessMarketing

## Review 2026-11-25 (fresh-eyes editor)

- Links: every internal link returned 200 with no redirect on thinkprofits.com (the site 301s unknown URLs, so 200 = real page); posts not in the brief list were confirmed in sitemap.xml. External Google links resolve 200.
- Spelling: -ize kept per Canadian Press (brief's -ise line ignored by instruction). No em/en dashes found.
- Meta label corrected 155 -> 153 (actual count).
- CTA heading moved from H3 to H2: as an H3 under the FAQ H2 it would be parsed into the FAQ block and FAQPage schema as a fake question.
- Rewrote the FAQ-history paragraph ("free real estate", "the blocks got longer") to a plainer, less glib version.
- H2 "What answer-first content actually means" -> dropped filler "actually".
- Facts re-verified: FAQ rich result stopped May 7, 2026, docs removed June 15, 2026 (Search Central updates); AI features page: no special optimizations or schema, structured data should match visible text, indexing and serving not guaranteed. All supported.
