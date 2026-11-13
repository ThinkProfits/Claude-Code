# Vision: site goes unresponsive during WP MCP edits (investigation, 2026-11-12)

Internal. Not client-facing.

Site: visionplumbingandheating.com (WordPress on Kinsta, Elementor, WP Rocket, behind Cloudflare).
Connection: `wp-vision` MCP server (Easy MCP AI plugin), connected 2026-10-13.

## What happened on 2026-10-13

Times in UTC (subtract 7 h for Vancouver PDT).

| Time | What was running | Result |
|---|---|---|
| 22:29 | `wp-vision` connection added mid-session | — |
| 22:36–22:48 | Session "Heat Pump page edits review": phone-number fixes on 8 pages. Each fix rewrote the whole `_elementor_data` field (60–100K characters), deleted `_elementor_element_cache`, then re-saved the page to purge Kinsta's cache | Worked |
| 22:51–23:22 | Same session: em-dash script across 13 Elementor pages, same rewrite + cache-clear + re-save per page | Hit the MCP rate limit (error -32003) 3 times, even after spacing calls 4 s, then 9 s, then 15 s apart |
| ~23:00–23:21 | **At the same time**, session "GSC structured data issues": read about 264 sitemap URLs and wrote schema fixes through the same MCP | Also rate-limited; 3 pages fixed |
| 23:22 | Verification run | Timed out on the server handshake |
| 23:28–23:31 | Session "Vision Plumbing website access" | **504 Gateway Time-out.** Cloudflare reached the server, but it didn't answer. `/wp-json/` gave no reply within 20 s. Cloudflare Ray ID `a4a220910e0da0d8` |
| ~23:31 | — | Recovered on its own: first REST reply 13.4 s, then about 1 s |

The site had also gone down briefly on **2026-09-15**, before the MCP existed (CLIENT.md, technical history). So the server has little headroom even without us; the MCP burst pushed it over.

## Site checks (read-only through wp-vision, 2026-11-12 01:55 UTC)

**Load multipliers on every save:**
- **No persistent object cache.** Site Health recommends one, and the host supports Redis. Every request rebuilds options and queries from the database, and Easy MCP AI stores its AI sessions in the database too.
- **Database max_connections = 50.** Concurrent MCP sessions plus visitors plus cron can exhaust it.
- **Heavy plugin stack.** 41 active plugins: Elementor + Pro + 3 add-on packs (Essential Addons, Mega Elements, Dynamic Visibility), 3 separate Google-review plugins, Gravity Forms, Yoast, Simple History (logs every change), Redirection.
- **WP Rocket.** Remove Unused CSS jobs run every minute, and its preload queue shows 371 URLs pending, 0 completed (tracking disabled, so this can't be read as live). Each page save purges the cache and re-queues CSS and preload work, so 13 big saves in a row can set off a wave of background requests.
- **WP-Cron runs on page requests** (it's not disabled and moved to a server cron). Four jobs run every minute (Action Scheduler, Rocket RUCSS, two Rocket SaaS jobs), so they ride on MCP and visitor requests.

**MCP-specific:**
- **Easy MCP AI is 2.1.1; 2.4.1 is available.** Not checked whether the update helps performance.
- **Per-token rate limit is 60/min.** Two sessions together easily exceeded it.
- **Diagnostics warning (e5):** WP Rocket caches the plugin's API endpoints. Fix: exclude `/wp-json/easy-mcp-ai/`, `/.well-known/oauth-*` and `/.well-known/openid-configuration` from caching in WP Rocket.

**Other:**
- **No PHP error log** (WP_DEBUG_LOG is off). Server-side evidence for 2026-10-13 lives only in MyKinsta (analytics, PHP worker usage, logs).
- **24 plugin updates and 1 theme update pending,** including Elementor 4.2.4 → 4.4.0 and WP Rocket 3.23.4 → 3.24.

## Likely cause

These are inferences; Kinsta's logs would confirm them.

1. **Two sessions hit the same site at once.** One did big Elementor rewrites, the other a full-site crawl plus writes.
2. **Each Elementor save is expensive.** It writes 60–100K of JSON, rebuilds Elementor CSS, purges Kinsta and WP Rocket caches, re-queues RUCSS and preload jobs, and Simple History logs it.
3. **There's no object cache and only 50 DB connections, on a server that had already fallen over once (Sept 15).** PHP workers fill up, Cloudflare waits about 100 s, and returns a 504.
4. **Timed-out requests keep holding a PHP worker** for up to 300 s (max_execution_time), so retries make it worse.

It's the same pattern seen on John Sadler on 2026-11-12 (`clients/john-sadler/HANDOFF-live-page-edits-2026-11-11.md`), so this is a general risk with bulk MCP edits on our Kinsta sites, not just a Vision quirk.

## Recommended fixes

**Hosting and site (needs Andrew's OK; the first two need MyKinsta access):**
- [ ] Ask Kinsta for PHP worker limit hits and error logs around 2026-10-13 22:30–23:35 UTC (Ray ID `a4a220910e0da0d8`), and 2026-09-15. Ask whether the plan's PHP worker count is enough.
- [ ] Enable Kinsta's Redis add-on (persistent object cache). Cost to be confirmed with Kinsta.
- [ ] Exclude the Easy MCP AI endpoints from WP Rocket caching (diagnostics e5).
- [ ] Update Easy MCP AI to 2.4.1, then the other pending updates, using the safe-updates routine.
- [ ] Optional: move WP-Cron to a Kinsta server cron so it stops riding on requests.

**How we run MCP edits (all sites):**
- [ ] One session per site at a time. Never run a crawl and a write job against the same site together.
- [ ] Space writes about 20–30 s apart on Elementor pages, and stop if any response takes more than 5 s.
- [ ] Clear cache per page only, never the whole site.
- [ ] Crawl in small batches, requesting only the fields needed.
- [ ] Do bulk work off-peak.
- [ ] Use Kinsta staging for large batches where the change can be pushed after.

## Not found

No meeting note (Gemini notes Oct 13–Nov 10, the Oct 14 Vision client meeting transcript) or Slack message from Andrew mentions this outage. Granola and Google Chat weren't searchable.
