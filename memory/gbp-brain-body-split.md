---
name: gbp-brain-body-split
description: "Claude does GBP research/writing only, never touches the Google Sheet or Make webhook directly — Codex (ChatGPT) executes via a handoff file protocol"
metadata: 
  node_type: memory
  type: project
  originSessionId: bce0938f-c879-4ec3-b154-0d2b6073bcf8
  modified: 2026-10-03T21:58:34.084Z
---

As of 2026-09-08, the GBP posting pipeline was split: Claude is "the brain" (research + writing via `gbp-topic-finder`/`gbp-post-writer`), Codex/ChatGPT is "the body" (writes to the Google Sheet, triggers Make). Claude must NOT edit the GBP queue spreadsheet or call the publishing webhook directly anymore — that's Codex's job now.

Protocol, defined in `gbp-handoffs/claude-handoff-instructions.md` (written by Codex, pasted by Francis):
- After finishing a post, write one file: `gbp-handoff__<location>__<YYYY-MM-DD>__<short-slug>.md`
- File starts with literal marker `GBP-MAKE-HANDOFF/1` then one fenced ```json block with exact schema (schemaVersion, intent: QUEUE_AND_PUBLISH_GBP, postId, location, title, summary, actionType, url, imageUrl, languageCode, researchNotes).
- `location` must be one of: thinkprofits_vancouver, john_sadler_surrey, wiseworth_surrey, vision_kelowna, mvp_langley, jamie_davis_hope, munro_crawford, clearset_port_coquitlam, spiedr.
- `actionType` must be one of: BOOK, ORDER, SHOP, LEARN_MORE, SIGN_UP, CALL.
- Write the finished .md to `E:\ChatGPT\` (local shared folder Codex reads from — confirmed 2026-09-08, already held a copy of claude-handoff-instructions.md there) in addition to posting it to the Slack review channel below. Francis reviews in Slack, then manually tells Codex the file is in that folder — he is the one who triggers Codex, not an automatic folder watch, so the human-approval gate stays intact.
- Also give the .md to Francis with exactly: "Review the attached GBP handoff. If approved, upload it to Codex with the message: **GBP APPROVED — PROCESS**" (still applies for the Slack copy / chat-upload path if he prefers that route for a given post).
- Never claim the user already approved — the upload message is the approval.

**Why:** removes Claude's need for Sheet write access entirely (previously explored: Apps Script web app plan — abandoned, superseded by this). Reduces misclick/accidental-edit risk from browser-based sheet editing (see prior incident in `codex-gbp-make-sheets-migration.md` session).

**How to apply:** whenever asked to post/queue a GBP post, produce the handoff .md per this spec instead of writing to the Sheet or calling any webhook. If this file's protocol details look stale (e.g. `claude-handoff-instructions.md` has changed), re-read that file before trusting this memory.

Approval channel for GBP posts in Slack: `#` channel ID `C0BVB0V2YEQ` (the "gbp post approvals" channel).

GBP Queue artifact (the review UI + shared DB Francis approves/rejects/edits posts in): `https://claude.ai/code/artifact/a5214b7d-26a9-40a1-b5cd-0e83faf540d3` (org `a8766fb8-0468-46f6-b923-fee0aa3374ca`). Read approved rows via `Artifact action:read_db, db_op:list, collection:"posts"` filtered to `status:"approved"` — don't just read the page's static SEED array, that's only a fallback seed, not live data. If this URL ever 404s or seems stale, use `Artifact action:list` and find it by title "GBP Queue" rather than asking Francis to resend the link.

**Confirmed trigger phrase (2026-09-08):** when Francis says something like "check the artifacts for approved posts", the flow is: read the GBP Queue artifact's `posts` collection (`db_op: query`/`list`, filter `status: "approved"`), spot-check each row against the field rules above (image must be JPG/PNG — reject/flag WebP and find a real same-site substitute rather than leaving it broken; flag stale scheduled_date or date-specific copy like a holiday-closure line; flag any count mismatch against what Francis expects), write one handoff .md per approved row, upload all of them to the Slack channel above, then post one summary message in that channel listing open flags. Francis confirmed this is the right workflow going forward — don't re-ask for confirmation each time, but keep surfacing per-batch judgment calls (bad images, stale copy, count mismatches) rather than silently deciding them. Francis does the actual Codex upload + approval phrase himself — Claude has no Codex/ChatGPT connector.

**IMPORTANT correction (2026-09-15): the GBP Queue artifact (`a5214b7d-26a9-40a1-b5cd-0e83faf540d3`) is STALE/DEMO data, not the live drafting system.** The real source of truth for current-week drafts is the Slack channel `#gbp-post-approvals` (`C0BVB0V2YEQ`) itself — individual per-draft messages (one per client per scheduled date), each with a "React :+1: to approve / :-1: to reject" footer, corrections/photo-assignments posted as **thread replies** on each draft (not new channel messages). Always read the channel + thread replies directly for current content before creating handoff files — do not reuse Artifact DB content, it caused a real mistake once (wrong topics/images handed off). The Artifact's own `write_db` path (Approve/Reject buttons) is a separate, disconnected UI that nobody is currently feeding — treat it as dead unless told otherwise.

**Weekly folder convention (started 2026-09-15):** handoff `.md` files go in a subfolder per week, named `week-of-<Monday's-date>` (e.g. `week-of-2026-09-14`), created under both `gbp-handoffs/` in this repo and `E:\ChatGPT\` on Francis's PC (Codex confirmed it pulls recursively from `E:\ChatGPT\`, subfolders are fine — no flat-folder requirement). `claude-handoff-instructions.md` lives at `E:\ChatGPT\` root (the copy Codex reads) and at `gbp-handoffs/claude-handoff-instructions.md` in this repo, never inside a week folder.

**Real-photo sourcing trick:** when a client's site can't be browsed directly (true for the cloud routine — network egress to arbitrary domains is blocked there; true sometimes in interactive sessions too), check Google Drive for a file/sheet that looks like an "Approved Queue" log — it records real image URLs previously published to each location's live GBP, which is a legitimate real-photo source without guessing or browsing.

**Valid Google actionType values, reconfirmed 2026-09-15:** `LEARN_MORE`, `BOOK`, `ORDER`, `SHOP`, `SIGN_UP`, `CALL` only. `"GET_OFFER"`/`"Get Offer"` is NOT valid despite repeatedly showing up in drafts — remap to `LEARN_MORE` or `SHOP` and flag the swap in `researchNotes`.

**CALL posts still need a `url`:** Slack drafts with a CALL action often say "no URL needed", but the handoff spec requires a verified public HTTPS `url` and every prior CALL handoff carried one. Fill it in with a verified client page, such as the homepage (first done 2026-09-25 for Jamie Davis).

**Link/image checking (2026-10-01):** most client sites (Clearset, Vision, Jamie Davis, John Sadler, Wiseworth) sit behind Cloudflare and return 403 to curl's default or short user agents, and to a spoofed "Googlebot/2.1" sent from a non-Google IP. Use a full Chrome user-agent string for pages and `Googlebot-Image/1.0` for images; both return 200. A 403 there does not mean the link is broken. Also check image dimensions: several "approved" images were below GBP's 400x300 minimum (Vision's `Vision-*.png` files are all 396x325, SPIEDR `sprinkler-tower.jpg` is 384x336), and Munro Crawford's banners (2200x597, 2000x450) crop badly. Vision's WP media API (`/wp-json/wp/v2/media?search=`) and MVP's Shopify `/collections/<handle>/products.json` are quick sources for real, bigger images.

**Automation status (2026-09-15):** the only real cron-scheduled GBP routine is `trig_01XS9XYk3kACsnCPgvH4wNCb`, renamed "GBP Saturday Drafting (all 9 locations)", cron `0 19 * * 5` UTC (= Sat 3am Philippines time), `enabled: true`. It now does ONLY the research+draft+post-to-Slack step for all 9 locations (Mon + Thu date, 18 drafts/run) — it no longer sends anything or calls the Make webhook (that behavior was removed; it was the old pre-handoff-file approach anyway). Sending to Codex is still a fully manual step: a human/Claude session reads the channel, creates handoff `.md` files, and Francis uploads them to Codex with "GBP APPROVED — PROCESS". Before this date, the Saturday drafting step had never actually been automated — both prior batches (Sept 5, Sept 14) were manual chat-triggered runs, which is why a "scheduled" Saturday run silently never happened.
