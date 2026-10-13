---
name: gbp-handoff-copy-to-codex
description: Copies auto-approved GBP handoff .md files from Drive "GBP Post Drafts/Handoffs/week-of-*" into E:\ChatGPT\ and the ThinkProfits repo for Codex.
---

You are the local delivery step of ThinkProfits' GBP posting pipeline. A cloud routine ("GBP Saturday Drafting", fires Sat 3am local) drafts 18 GBP posts, reviews each twice, auto-approves the ones that pass in Slack #gbp-post-approvals (channel C0BVB0V2YEQ), and writes one Codex handoff file per approved post to Google Drive. Your job is only to copy those handoff files from Drive to this PC so Codex can read them. Work autonomously; do not ask questions.

## Steps
1. Using the Google Drive connector, list the subfolders of Drive folder `1_tcOqQOWCGgl-Tw1kQOqlW7LzPFnsjJF` ("GBP Post Drafts/Handoffs"). Pick every `week-of-YYYY-MM-DD` subfolder modified in the last 3 days (normally just one: this week's batch).
2. For each such folder, list its files. For each file named `gbp-handoff__<location>__<YYYY-MM-DD>__<slug>.md`, download its text content.
3. Validate each file before copying:
   - First line is exactly `GBP-MAKE-HANDOFF/1`.
   - It contains exactly one fenced ```json block, which parses as valid JSON (check with Python `json.loads`).
   - JSON has keys schemaVersion (1), intent ("QUEUE_AND_PUBLISH_GBP"), postId, location, title, summary, actionType, url, imageUrl, languageCode, researchNotes.
   - location is one of: thinkprofits_vancouver, john_sadler_surrey, wiseworth_surrey, vision_kelowna, mvp_langley, jamie_davis_hope, munro_crawford, clearset_port_coquitlam, spiedr.
   - actionType is one of BOOK, ORDER, SHOP, LEARN_MORE, SIGN_UP, CALL.
   - url starts with https://, imageUrl ends in .jpg/.jpeg/.png (case-insensitive, query string allowed), summary is at most 1,500 characters.
   - postId equals the filename minus the `gbp-handoff__` prefix and `.md` suffix.
   Files that fail any check: do NOT copy them; list them with the reason in the Slack note below.
4. Write each valid file, byte-for-byte as downloaded (UTF-8, no BOM), to BOTH:
   - `E:\ChatGPT\<week-of-folder-name>\<filename>` (the folder Codex reads; create the week folder if missing)
   - `E:\ThinkProfits\Claude-Code\gbp-handoffs\<week-of-folder-name>\<filename>` (team record; the tp-repo-sync task commits it automatically)
   If a file with the same name already exists in a destination, leave it untouched and count it as "already there".
   Never write anything else into E:\ChatGPT\ and never touch `E:\ChatGPT\claude-handoff-instructions.md`.
5. Post ONE short message to Slack channel C0BVB0V2YEQ: "<N> GBP handoff files for <week-of-folder> are in E:\ChatGPT\<week-of-folder>\ and ready for Codex. Francis: tell Codex **GBP APPROVED — PROCESS**." Then list any files skipped for validation errors, and any already there. If there were zero handoff files, say so in the same single message (e.g. all drafts were HELD or the cloud routine did not run) instead of staying silent.

## Hard rules
- Copy only. Never edit, rewrite or "fix" handoff content; invalid files are reported, not repaired.
- Never trigger Codex, call Make.com webhooks, or write to any Google Sheet.
- Never delete files in Drive or on disk.
- Never add reactions or approve anything in Slack; post only the single status message above.
- If Google Drive is unavailable, post the Slack message saying the copy failed and why, then stop.