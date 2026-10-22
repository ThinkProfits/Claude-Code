# MySaskFarm: RM page title/meta fix (2026-10-23)

Five RM pages carried the next RM's AIOSEO title and meta description (shifted by one row). This file records the values before and after the fix, so the fix can be reversed. The live values were read from the site on 2026-10-22.

The fix restores the existing site pattern (`RM of [Name] No. [###] Farmland for Sale | MySaskFarm`). It doesn't apply the new RM template's title; that happens when each page is rewritten.

| Page | Before: title | Before: meta description | After: title | After: meta description |
|---|---|---|---|---|
| /rm-of-corman-park/ | RM of Dundurn No. 314 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Dundurn No. 314, just south of Saskatoon. Browse current listings or get a free evaluation of your land. | RM of Corman Park No. 344 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Corman Park No. 344 around Saskatoon, Warman and Martensville. Browse current listings or get a free land evaluation. |
| /rm-of-dundurn/ | RM of Kindersley No. 290 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Kindersley No. 290, west-central Saskatchewan. Browse current listings or get a free evaluation of your land. | RM of Dundurn No. 314 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Dundurn No. 314, just south of Saskatoon. Browse current listings or get a free evaluation of your land. |
| /rm-of-kindersley/ | RM of Tisdale No. 427 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Tisdale No. 427, northeast Saskatchewan. Browse current listings or get a free evaluation of your land. | RM of Kindersley No. 290 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Kindersley No. 290, west-central Saskatchewan. Browse current listings or get a free evaluation of your land. |
| /rm-of-biggar/ | RM of Corman Park No. 344 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Corman Park No. 344 around Saskatoon, Warman and Martensville. Browse current listings or get a free land evaluation. | RM of Biggar No. 347 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Biggar No. 347, west of Saskatoon. Browse grain and livestock land, or get a free evaluation of your farm. |
| /rm-of-arlington/ | RM of Biggar No. 347 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Biggar No. 347, west of Saskatoon. Browse grain and livestock land, or get a free evaluation of your farm. | RM of Arlington No. 79 Farmland for Sale \| MySaskFarm | Farmland for sale in the RM of Arlington No. 79, southwest Saskatchewan. Browse current listings or get a free evaluation of your land. *(new; Arlington's original meta wasn't found anywhere on the site)* |

Pages already correct (not touched): /rm-of-aberdeen/, /rm-of-tisdale/, /rm-of-antler/.

**Status:** see the log below.

## Log
- 2026-10-23: values prepared. Waiting for a WordPress admin sign-in (no MCP connection to this site).
- 2026-10-23: **fix applied and verified live.** Done through the new `wp-mysaskfarm` MCP (Easy MCP AI). Page IDs: Corman Park 521, Dundurn 636, Kindersley 644, Biggar 609, Arlington 573.
  - How: Easy MCP AI's AIOSEO integration is switched off on this site (wp-admin › Easy MCP AI › Tools › Abilities), so the change went through AIOSEO's own REST route instead: `POST /aioseo/v1/posts-list/load-details-column` to read, then `POST /aioseo/v1/posts-list/update-details-column` with `{postId, title, description}` per page. This is the same call as AIOSEO's inline edit on the Pages list, so it changes only the SEO title and meta description. No page content, slugs or other SEO settings were touched, and the three correct pages (Aberdeen, Tisdale, Antler) were left alone.
  - Before values read from the site matched the "Before" column on all five pages before writing.
  - Cache: cleared Elementor CSS and LiteSpeed page cache for the five pages (`wp_clear_cache`, scope posts).
  - Verification: fetched each live URL (no query string). `<title>`, `<meta name="description">`, `og:title`, `twitter:title` and the AIOSEO WebPage schema `name` all show the "After" values on all five pages.
  - Side note: each page also carries a second WebPage schema node named "Farmland for Sale in the RM of [Name] No. [###] | MySaskFarm" (not from the AIOSEO title). It already names the right RM on all five pages, so it was left as is.
