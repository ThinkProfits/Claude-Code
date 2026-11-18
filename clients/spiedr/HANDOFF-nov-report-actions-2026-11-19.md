# Handoff: Spiedr November report follow-through (from session of 2026-11-19)

Start a new session in `E:\ThinkProfits\Claude-Code` and point it at this file.

## Goal

Ship the four next steps Francis committed to in the November report reply, then report back in the same Slack thread. The reply is public to the team, so these are promises with dates.

- Reply posted 2026-11-19: [Slack link](https://thinkprofitscom.slack.com/archives/C01928K8M0F/p1795021542087579?thread_ts=1793991764.756459&cid=C01928K8M0F)
- Channel `#firestorm_spiedr` (ID `C01928K8M0F`), thread ts `1793991764.756459`
- Reply text: [slack-reply-draft-2026-11-report.md](slack-reply-draft-2026-11-report.md)

## Read first

1. [CARD.md](CARD.md) (status) and [CLIENT.md](CLIENT.md) sections 5, 8 and 11 (rules)
2. [memory/spiedr-context.md](../../memory/spiedr-context.md): Semrush quirks, crawl workaround (Mod_Security: send a browser User-Agent + Accept headers), stack (WPBakery, Yoast), `wp-spiedr` MCP
3. [spiedr-fix-roadmap-2026-q4.md](spiedr-fix-roadmap-2026-q4.md), Phase 1 tables (source page, existing mentions, anchor direction)

## Before you start

- **`wp-spiedr` MCP failed to connect on 2026-11-19** (HTTP 401, auth header rejected). The Bearer token was likely rotated or revoked. Francis needs to issue a new token in Easy MCP AI on spiedr.com and re-run `claude mcp add` before any WordPress edit. Do not use any other `wp-*` server: none of them is Spiedr.
- Semrush MCP was out of API units in November. Check before step 4; if still out, say so in the thread instead of guessing.

## The four commitments

| # | Task | Promised timing | Done when |
|---|---|---|---|
| 1 | Internal links to fire service trailers, equipment rentals, wildfire consulting and sprinkler kits from the roof sprinkler, Mark 3 and blog content (roadmap Phase 1) | end of Nov 2026 | Links live; list of source page → target → anchor logged in a new `internal-links-2026-11.md` |
| 2 | Confirm the Sep 17 URL fixes (consulting, rentals: canonical had pointed at a redirect, URLs missing from the sitemap) are indexed under the right URL | week of 2026-11-23 | GSC URL Inspection result for each URL recorded; request indexing if not |
| 3 | Verify `contact_form` and `pdf_download` GA4 events fire, then add phone and email click tracking | Nov 2026 | Events seen in GA4 DebugView/Realtime; GTM changes noted (GTM MCP can edit but not publish; Andrew or Francis publishes) |
| 4 | Pull the Semrush keywords that left the top 20 and check what waspwildfire.com is gaining | once Semrush units are back | Short list in the thread; check the daily `Dt` series first (month-boundary artifact) |

### Progress (2026-11-19, follow-up session)

- [x] **1. Internal links live (Francis approved 2026-11-19).** 20 new links + redirect-hop swaps for the old consulting, rentals and training URLs. Log and before/after counts in [internal-links-2026-11.md](internal-links-2026-11.md). All swaps done; homepage verified live.
- [x] **2. Indexing confirmed.** `/services/wildfire-consulting/`: Submitted and indexed, Google canonical = user canonical, crawled 2026-11-08. Rentals page is `/fighting-equipment-rentals/` (not under /services/): indexed, canonical correct, crawled 2026-11-06. `/services/consulting/` = "Page with redirect" (expected). No reindex request needed.
- [x] **3. Events verified; GTM change prepared, not published.** GA4 property 274454704, 2026-10-23 to 2026-11-19: contact_form 3, pdf_download 1, phone_click 3 (phone tracking already existed, tag 20). No mailto links on the site. GTM container GTM-MH3WNL2 (`accounts/6004069871/containers/46323771`), new workspace 16 "2026-11 email click + phone trigger fix (ThinkProfits)": added trigger 32 "Email click Trigger" (Click URL starts with mailto:) + tag 33 "GA4 Event - email_click"; changed trigger 19 from "contains tel" to "starts with tel:". **Andrew or Francis: Preview, then publish.**
- [ ] **4. Blocked: Semrush has no API units** (checked 2026-11-19, every Position Tracking report unavailable). Retry when units return.
- [x] Slack follow-up posted 2026-11-19 ([link](https://thinkprofitscom.slack.com/archives/C01928K8M0F/p1795040251320219?thread_ts=1793991764.756459&cid=C01928K8M0F)).

Notes:
- Step 1: edit existing sentences where the anchor already appears (roadmap rule). WPBakery raw blocks are stored encoded; read the memory before editing. Show Francis the link list before writing anything live.
- Step 1 targets: trailers page (`/spiedr-sprinkler-trailers/` or `/sprinkler-trailers/`, confirm which is canonical), rentals, `/services/wildfire-consulting/`, `/spiedr-wildfire-sprinkler-kit/`. Sources: `/roof-sprinkler-system/`, `/mark-3-pump/`, relevant blog posts.
- Step 3: tools are `ga4` and `gtm` MCPs (agency account). Spiedr's forms were broken by reCAPTCHA until Andrew's fix on Oct 23; November is the first clean month.

## When done

1. Draft a short follow-up in the same thread ("Update on the November items: …", done / still open), **show Francis and wait for his OK** before posting.
2. Update CARD.md (next steps) and CLIENT.md (section 5 if findings change the picture).
3. Tick the items in this file.

## Not in scope here

- The other 11 November report replies: see `automations/HANDOFF-monthly-report-replies-2026-11-19.md` and `automations/monthly-report-replies-2026-11-drafts.md`.
- Other open Spiedr threads (non-indexed pages spike from 2026-10-28, blog fixes, October blog FAQ schema): listed on CARD.md.
