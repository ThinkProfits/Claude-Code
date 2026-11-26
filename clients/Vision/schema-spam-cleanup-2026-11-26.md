# Vision: inline schema block cleanup (found 2026-11-26)

**Status: DONE 2026-11-26.** Francis approved the removal ("as long as they are necessary edits to avoid confusion from google"), and Claude made it through `wp-vision` `wp_replace_in_post`, removing only the `<script type="application/ld+json">…</script>` blocks from `post_content`.
- **24 items cleaned.** Before → after content length, for example: 16518 43,342 → 4,082 characters, 32981 43,255 → 4,129. That's 2 pages plus 22 posts, the last two with a broken empty-author Article block (16495, 1146).
- **Rollback:** each post kept its pre-edit revision, so `wp_restore_revision` undoes any one of them.
- **Origin:** on post 16518 the block arrived in the 2024-05-24 revision by site user 73 (content went from 4,065 to 43,347 characters).
- **Checks after the edit:**
  - Site search for "application/ld+json", "blogspot" and "778-403-4749" returns 0 results.
  - 8 live URLs (served fresh, `x-kinsta-cache: MISS`) show 0 blogspot links and 0 hits for the old number.
  - What remains on each page is Yoast's graph (Article, WebPage, Organization with Vision's 4 real social profiles) plus the theme's sitewide Blog/BreadcrumbList blocks.
  - Post text was untouched.
- **Still open (wording, needs Vision's OK):** the Privacy Policy page body still gives the closed Leckie Rd address ("Unit B (108), 2280 Leckie Rd Kelowna, B.C. V1X 6G6") as the privacy officer's mailing address. It should be 2600 Acland Rd Unit 8.
- **Reindexing:** on 2026-11-26 `post-sitemap.xml` and `page-sitemap.xml` were resubmitted through the GSC API. Per-URL "Request indexing" only works in the Search Console UI, not the API, and is capped at about 10–12 URLs per day per property. It needs the agency Google account signed in. Handed to Grok on 2026-11-26 (`E:\GrokBot\tasks\open\2026-11-26__vision__gsc-request-indexing.md`, 10 URLs on day 1 and 12 on day 2).

The findings below are kept for the record.

## What it is

22 items carry hand-pasted JSON-LD `<script>` blocks inside the post content (not Yoast, not a plugin, not the theme): 20 old blog posts plus the Financing and Privacy Policy pages. The blocks render on the live pages.

Example: post 16518 (/hot-temperature/) has 5 blocks in its content:
- **2 × LocalBusiness** with the **old closed Leckie Road address** ("2280 Leckie Rd Unit 108") and phone **778-403-4749**. That number isn't in our files. The main line is 250-470-9552, and CLIENT.md says to use it everywhere (CallRail swaps it).
- **2 × Corporation**, each with a `sameAs` list of about 256 URLs across about 259 domains. The list reads like an old backlink export pasted in. It includes:
  - spam and blog-network pages (dozens of blogspot posts from 2017–2021, `best-seo-domains.com`, `air-conditioning-riyadh.com`, `taplaleklanc.metropolitan.hu`)
  - competitor "best plumbers in Kelowna" lists (`ceplumbingheating.ca/top-9-highest-rated-plumbers-in-kelowna-of-2023/`, `handymanreviewed.com/best-plumbers-kelowna/`)
  - a few legitimate pages (BC Hydro, FortisBC, Vision's social profiles).
- **1 × Article** block, which duplicates what Yoast already outputs.

## Why it matters

- It publishes the **wrong NAP** (closed address, unknown phone) in structured data on 22 URLs. That conflicts with the GBP and the site, which both use 2600 Acland Rd.
- `sameAs` is meant to list the business's own official profiles. 256 unrelated URLs, many of them spam, plus a competitor's ranking list, give search engines and AI answers a confused picture of Vision. It can also look manipulative.
- The duplicate Article and LocalBusiness entries conflict with Yoast's schema graph.

It looks like an old SEO tactic, not a hack: the posts were last edited by site users, and the blocks are the same pasted snippet with small variations. The revision history wasn't checked.

## Affected URLs (WordPress IDs)

Posts: 32981 /uv-water-filtration-benefits/, 32031 /benefits-of-installing-heat-pump/, 31976 /prevent-flood-damage-this-spring/, 31846 /hydronic-heating-benefits/, 31628 /plumbing-emergency-guide/, 31103 /plumbing-heating-rebates/, 16439 /fireplace-maintenance/, 16897 /5-benefits-of-consistent-furnace-maintenance/, 16892 /5-things-to-look-for-when-hiring-a-kelowna-plumber-2/, 16855 /maximize-cooling-by-keeping-your-air-conditioner-working-properly/, 16673 /top-tips-to-extend-the-life-of-your-air-conditioner/, 16594 /8-top-tips-to-improve-your-air-conditioner-efficiency-this-summer/, 16571 /five-reasons-to-maintain-your-air-conditioner-heat-pump/, 16533 /5-hvac-mistakes/, 16518 /hot-temperature/, 16472 /finding-heat-pump-experts/, 16469 /fall-maintenance-tips/, 1223 /your-furnace-needs-regular-maintenance/, 1152 /top-notch-hot-water-heaters/, 1144 /air-conditioner-care/

Pages: 28352 /financing-rebates/financing/, 3 /privacy-policy/

Two more posts have inline JSON-LD **without** the spam list or the 778 number: 16495 /electric-or-gas-fireplace/ and 1146 /hvac-technician-vision-mechanical-does-that/. Check them in the same pass.

How this was found (repeatable): `wp-vision` search for "blogspot" (22 results), "778-403-4749" (the same 22), and "application/ld+json" (24).

## Proposed fix (for Andrew's OK)

1. Remove every inline `<script type="application/ld+json">` block from those 24 items' post content, and leave the rest of the content untouched. Yoast keeps outputting the correct sitewide schema.
2. If Andrew wants per-post Article or FAQ schema, add it through Yoast settings, not pasted scripts.
3. Edit one post first and confirm that it renders and the Yoast schema is intact. Then do the rest, paced (follow `memory\vision-wp-mcp-elementor-edits.md` for the cache steps).
4. Clear the WP Rocket and Kinsta caches, then request reindexing of the 22 URLs in Search Console.
5. Optional: check the revision history on one post to see when the block was added.

WordPress keeps a revision for each post edit, so every change can be rolled back.
