# 02 search-terms-vs-keywords-google-ads: internal notes

**Scope:** Explainer/how-to (PPC) defining search terms vs keywords in Google Ads, how match types connect them, a weekly search terms report routine, what the report hides (privacy omissions, "other search terms" in insights), negative keyword match rules, and structural fixes. Fills brief row #2 (week of Sep 29, 2026). Links to the AI Max post without repeating its match-type comparison.

**Publish date:** 2026-09-29 (backfill, real week date per brief).

## Sources checked (all fetched 2026-11-25)

| URL | Confirmed |
|---|---|
| https://support.google.com/google-ads/answer/2472708 (linked) | Search term and keyword definitions (quoted); report path Campaigns > Insights and reports > Search terms; Keyword column not shown by default; Match type labels incl. "Exact match (close variant)"; low-activity terms omitted for privacy (quoted). |
| https://support.google.com/google-ads/answer/2453972 (linked) | Negative broad/phrase/exact behaviour; negatives don't match close variants; too many negatives can reduce reach; negatives at ad group, campaign and shared-list level. |
| https://support.google.com/google-ads/answer/7478529 (mentioned, not linked, to stay at 2 external links) | Three match types, syntax, broad is default, broader types capture narrower types' queries plus more. |
| https://support.google.com/google-ads/answer/11386930 (mentioned, not linked) | Search terms insights includes terms hidden for privacy; lower-spend/uncategorised queries bundled as "other search terms"; available for Search, PMax, Shopping. |
| https://support.google.com/google-ads/answer/7102466 | Adding negatives from the report: to ad group, campaign, existing or new list; default is negative exact match. |
| https://thinkprofits.com/digital-news/ai-max-search-term-matching-vs-exact-phrase/ | Existing post compares AI Max vs exact/phrase and never defines search terms vs keywords or the weekly report routine, so no overlap. |

## Claims cut / not used

- Negative keyword list limits (5,000 per list, 20 lists): seen only in a search summary, not confirmed on a fetched page. Omitted.
- "56-day" window for search terms insights themes: not confirmed on the insights page. Omitted.
- Any claim about an "Other search terms" totals row inside the search terms report itself: not in Google's docs. Post only describes the "other" bucket in search terms insights.
- No statistics used. No client results or numbers. The Vancouver plumber is a hypothetical example, framed as "picture...".

## Keyword data (google-ads-keywords MCP, Keyword Planner, Canada geo 2124, Nov 2025 to Oct 2026)

| Keyword | Avg monthly (CA) |
|---|---|
| search terms vs keywords (primary) | 10 |
| search terms vs keywords google ads | 10 |
| negative keywords | 40 |
| search terms report | 20 |
| keyword match types | 20 |
| phrase match vs exact match | 20 |
| google ads search terms report | 10 |
| google ads negative keywords | 10 |
| google ads match types | 10 |
| negative keyword list | 10 |
| google ads wasted spend | 0 (dropped) |

Volumes are low across the cluster (Canada is a small market for PPC how-to queries); the post covers the cluster rather than one head term. Primary keyword appears 4 times in the post body plus title/meta.

**PAA-style questions folded into FAQ:** difference between search terms and keywords; how often to check the search terms report; why ads show for searches not added; why search terms are missing; negative exact vs phrase.

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml on 2026-11-25. No URL contains "search-term" except `ai-max-search-term-matching-vs-exact-phrase` (different intent: AI Max vs exact/phrase decision). No URL contains "negative" or "waste". `what-is-keyword-research` targets SEO keyword research, not Ads search terms. Clear to proceed.

## Internal links used

/digital-news/ai-max-search-term-matching-vs-exact-phrase/, /digital-news/weekly-google-ads-change-log/, /digital-news/google-ads-lead-quality-loop/, /digital-news/google-ads-location-targeting-vancouver/, /digital-news/brand-nonbrand-google-ads-budget/, /ppc-advertising/, /contact/ (7 distinct).

## Image note

Hero uses the site's `/images/blog/wp/tp-branded-placeholder.jpg`. If replaced later, use a real, client-data-free screenshot of a demo account's search terms report (no AI images, no real client names or spend visible).

## Implementation notes

- No JSON-LD in draft; Lovable layout outputs Article, FAQPage and Breadcrumb from the FAQ block.
- External links should open in a new tab with rel="noopener noreferrer".
- Google Ads UI labels (Insights and reports, Add as negative keyword) can shift; recheck before publish if the UI changes.

## GBP post (ThinkProfits, Vancouver)

Your keywords are what you bid on. Your search terms are what you actually paid for, and the two are rarely identical. Our new guide explains search terms vs keywords in Google Ads, how to read the search terms report each week, and how to use negative keywords without cutting good traffic. Read it on our blog, or book a free 30-minute consultation to review your own account.

CTA button: Learn more > [blog URL]

## LinkedIn

Ever opened a Google Ads search terms report and wondered who searched "plumbing apprenticeship" and why you paid for it? Keywords are your instructions; search terms are what happened. We wrote up the weekly routine we use to keep the two close: match types, the report columns that matter, what the report hides, and how negative match types really behave. [blog URL] #GoogleAds #PPC

## Facebook

Running Google Ads? Your keyword list and your search terms report are telling two different stories. Here is how to read the report weekly and stop paying for clicks you never wanted: [blog URL] #GoogleAds

## Review 2026-11-25 (fresh-eyes editor)

- Links: every internal link returned 200 with no redirect on thinkprofits.com (the site 301s unknown URLs, so 200 = real page); posts not in the brief list were confirmed in sitemap.xml. External Google links resolve 200.
- Spelling: -ize kept per Canadian Press (brief's -ise line ignored by instruction). No em/en dashes found.
- FACT FIX: post said negatives do not cover misspellings. Google's negative keyword page says negatives account for casing and misspellings automatically but not plurals or synonyms. Bullet corrected.
- Negative phrase examples changed from single words ("jobs", "salary", "free") to multi-word phrases; for single words negative broad and phrase behave identically, so the original advice was misleading. FAQ answer rewritten.
- Cut a repeated parallel pair of sentences in the first H2 (AI-tell).
- CTA softened: "we will show you where your budget is going" read as a free account audit, which the brief does not allow. Now a free 30-minute conversation.
- Meta label corrected 153 -> 152.
- Facts re-verified on 2472708, 2453972, 7478529, 11386930, 7102466 (definitions, report path, Keyword column default, privacy omission, other search terms, default negative exact).
