# 07: internal-linking-qa-checklist (internal notes)

**Scope:** How-to checklist post covering pre-publish internal link QA (orphan check, links to service pages, anchor text, broken/redirecting/non-crawlable links, navigation vs contextual links). Fills backfill row #7, week of Nov 3, 2026. Category: SEO.

## Image note

Hero uses the site's branded placeholder `/images/blog/wp/tp-branded-placeholder.jpg`, alt: "Internal linking checklist for reviewing a blog post before it goes live". No AI imagery. Optional later: a real screenshot of the checklist table or a Search Console Links report (blur any client data).

## Sources checked

- https://developers.google.com/search/docs/crawling-indexing/links-crawlable (linked in post): crawlable links need `<a href>`; Google "can't reliably extract URLs" from elements without href; anchor text should be descriptive, reasonably concise, relevant; "click here" is generic; keyword stuffing in anchors violates spam policies; "Every page you care about should have a link from at least one other page on your site"; words before/after links matter; avoid links right next to each other; image link alt text used as anchor. No numeric links-per-page target.
- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes (linked in post): update internal links to new URLs; avoid chaining redirects; Googlebot can follow up to 10 hops.
- https://developers.google.com/search/docs/crawling-indexing/http-network-errors: "By default, Google's crawlers follow up to 10 redirect hops."
- https://support.google.com/webmasters/answer/9049606 (Search Console Links report): internal links section shows which pages link to a given page; report is a sample, "isn't a comprehensive list of every link on your site".

## Claims cut or softened

- Cut: any per-post link count presented as Google guidance (Google gives none). Our "5+ on 1,200+ word posts" is framed as our own practice.
- Cut: nofollow-on-internal-links FAQ (Google's link page covers nofollow only for outbound links; also trimmed for word count).
- Cut: "3 hops max" type rules; Google's "ideally no more than 3 and fewer than 5" wording exists but was not needed.
- "10 to 15 minutes" is our own estimate, not a stat.
- Vendor blog figures (2 to 6 links per 1,000 words, etc.) from search results not used: unverified, vendor sources.

## Keyword data

Source: google-ads-keywords MCP (Keyword Planner), Canada (geo 2124), pulled 2026-11-25. Avg monthly searches:
- internal linking checklist: 0 (no data). Kept per brief as the primary; the post realistically ranks on the broader terms below.
- internal linking 70 | seo checklist 70 | internal links seo 30 (close variant: internal linking seo) | orphan pages 20 | on page seo checklist 20 | internal linking best practices 10 | anchor text seo 10 | orphan pages seo 10 | broken internal links 10 | internal link audit 10 | internal linking strategy 10 | blog post checklist 10.
- Flag for Francis: consider "Internal Linking Checklist" staying as the H1 but treat "internal linking" as the realistic target.

PAA-style questions found via web search (folded into FAQ): what is an orphan page; how many internal links per post; should internal links open in a new tab; is linking to a redirect bad. Nofollow question dropped (see above).

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml (301 URLs) on 2026-11-25 for link/anchor/orphan/internal/redirect/checklist/audit/structure terms. No existing post targets internal linking. Nearest: `5-simple-steps-to-a-successful-link-building-strategy` (external link building, different intent), `seo-url-structure`, `sitemap-hygiene-website-rebuild`, `content-consolidation-without-traffic-loss` (the latter two are linked as related reading). Clear to publish.

## Internal links used (10 distinct)

/digital-news/sitemap-hygiene-website-rebuild/, /digital-news/content-consolidation-without-traffic-loss/, /seo-services/local-seo/, /seo-audit/, /digital-news/service-page-location-page-blog-post/, /content-writing-services/, /free-seo-audit-tool/ (x2), /digital-news/city-landing-page-cannibalization-search-console/, /seo-services/, /contact/.

Practise what we preach: after publishing, add a contextual link to this post from `sitemap-hygiene-website-rebuild` and `content-consolidation-without-traffic-loss` so it is not an orphan.

## GBP post (ThinkProfits Vancouver)

Publishing a new blog post? Run a quick internal linking check first: make sure older pages link to it, it links to the right service page, every anchor describes its destination, and nothing points at a redirect. Our new checklist walks through each step in about 15 minutes. CTA button: Learn more, linking to [BLOG URL].

## LinkedIn

A new blog post with no internal links pointing at it relies on the sitemap and luck. We put together the pre-publish internal linking checklist we use on our own site and client sites: orphan checks, anchor text, service-page hand-offs and redirect clean-up. [BLOG URL] #SEO #ContentMarketing

## Facebook

Before you hit publish on your next blog post, give it 15 minutes of internal link QA. Our checklist covers what to check and why it matters: [BLOG URL] #SEO #VancouverBusiness

## Implementation notes

- No JSON-LD in draft; Lovable layout outputs Article, FAQPage (4 Qs) and Breadcrumb.
- Closing CTA heading is bold text, not an H3, so the FAQ block doesn't pick it up as a question.
- External links open in a new tab with rel="noopener noreferrer".
- Publish date: week of Nov 3, 2026 (backfill).
- Word count 1,790 (body incl. table and FAQ, excluding metadata lines).

## Review 2026-11-25

- Links: all 10 internal links 200; both developers.google.com links 200. Converted absolute https://thinkprofits.com links to root-relative paths to match the rest of the batch.
- Meta description label corrected 154 to 155 (recounted). Title 57.
- Fixed a contradiction: closing line said "four strong links rather than six weak ones" while the FAQ sets five as our minimum; now "five strong links rather than eight weak ones".
- Facts relied on the writer's fetched sources (links-crawlable, site-move, Links report); claims match those pages. No other changes; voice and offers pass.
