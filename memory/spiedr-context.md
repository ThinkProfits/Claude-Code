---
name: spiedr-context
description: "SPIEDR Ltd. (www.spiedr.com) — ThinkProfits wildfire-protection client; Semrush project, tracking quirks, and the Sept 2026 internal-linking findings."
metadata: 
  node_type: memory
  type: project
  originSessionId: c61f1e88-ad2f-4d7b-bdb8-d5f894a4d639
  modified: 2026-10-01T17:08:12.710Z
---

SPIEDR Ltd. — wildfire structure protection equipment (sprinkler kits, sprinkler trailers, WATERAX/Mark-3 portable fire pumps), BC. Client contacts in reporting: Bob and Natalie. Monthly report signed by Shawn Moore. Francis is the assigned SEO lead. Client folder: `clients/spiedr/`.

**Semrush:** project ID 2084675, name "Spiedr", url `www.spiedr.com`. Position Tracking campaign_id is the same 2084675. Tracking config is **Desktop / British Columbia / Google** — it will never agree with the GSC section of the report, which is national. Say so in reports where the two sit side by side.

**Tracking campaign is badly scoped (as of Sept 2026):** 44 of 47 tracked keywords have 0–30/mo volume, so Top 3 / Top 10 counts churn on noise. "bc wildfire service" (2,900/mo) is tracked but unranked; the highest-volume terms the site actually ranks for — "fire ban bc" (5,400), "bc fire ban" (3,600) — aren't tracked at all. Refresh the keyword set before reading month-over-month tier counts as signal.

**Month-boundary artifact:** the monthly report compares day 1 vs day 31, so a two-day wobble reads as a collapse. Always pull the daily `Dt` series from `tracking_position_organic` before accepting a flagged drop. Sept 2026 example: "structural fire protection" reported as -13 (6→19) was actually 6–7 for 29 of 31 days.

**Internal linking is the standing structural problem.** In-content links only (header/nav/footer stripped), 163 sitemap URLs: `/roof-sprinkler-system/` and `/fire-embers/` have **zero** inbound in-content links despite being the best-ranking and highest-traffic pages respectively; `/mark-3-pump/` has 2; `/spiedr-fire-pump-protection-systems/` has 1. 45 of 93 blog posts have zero, reachable only via a ten-page paginated archive — including the BC fire bans post that ranks #25–31 for the site's biggest-volume terms.

**Crawling:** spiedr.com sits behind Mod_Security — plain `curl` returns "Not Acceptable!". Send a real browser User-Agent plus `Accept:` headers and it serves normally. No Screaming Frog crawl on file yet.

**Stack (checked 2026-10-02 from public HTML + /wp-json/):** WordPress 7.1.2, WPBakery Page Builder (js_composer), theme Whistle with a whistle-child child theme, WooCommerce 11.0.1, Yoast, Wordfence, Redirection, Simple History, Jetpack, Trustindex, an `eap-accordion` plugin. The homepage uses `vc_custom_*` Design Options classes plus 4 `wpb_raw_html` / `wpb_raw_code` blocks, which are stored encoded. **Easy MCP AI is already installed** (`easy-mcp-ai/v1` namespace is live), Connected 2026-10-02 as user-scope MCP server **`wp-spiedr`** (http, Bearer token) — health check shows Connected, Wordfence did not block it. Any other WordPress MCP server you have connected is a different site, never Spiedr. Double-check the server prefix is `wp-spiedr` before any write. The token was pasted in chat once, so the user was advised to rotate it (revoke in Easy MCP AI, re-run `claude mcp add`).

Related: [[blog-topic-cannibalization-check]], [[strategy-core-pages-before-niche]]
