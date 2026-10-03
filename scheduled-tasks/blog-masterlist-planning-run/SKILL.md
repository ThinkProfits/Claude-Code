---
name: blog-masterlist-planning-run
description: Monthly (25th) blog masterlist audit: gaps, Slack report insights, topic proposals, and drafts for briefed blogs
---

You are running the twice-monthly blog content operations check for Francis (SEO desk at ThinkProfits). This is the PLANNING RUN (25th). Work autonomously; do not ask questions.

IMPORTANT: This run only audits, researches, and proposes. It does NOT draft any blogs. Blog drafting now happens in a separate scheduled task ("blog-masterlist-draft-check") that runs daily and waits for Francis to reply "proceed" (or anything that means continue) in his Slack DM before writing anything. Do not attempt to draft blogs in this run under any circumstances.

## Data sources
1. Google Sheet "BLOG Masterlist - 2024-2026", file ID: 1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw. Read it via the Google Drive connector (download as xlsx and parse with Python/openpyxl in the sandbox to get ALL tabs; read_file_content only returns the first tab). Columns on client tabs are approximately: A Date, B Topic, C Status, D Topic Approved, E Main Keyword, F Secondary Keywords, G Note/Content Angle/Writing Instructions, H Blog Written (link), I Blog Published (link), J Notes. Verify headers per tab before parsing.
2. Slack client channels (read-only). Client → channel ID map:
   - Jamie Davis → C07TS2LMF9T
   - John Sadler Plumbing & Heating → C019H8FNN9H
   - Munro & Crawford → C019AAP51U6
   - Spiedr → C01928K8M0F
   - Vision Plumbing Heating Cooling → C052P7H4FUG
   - ThinkProfits → C05MW75SUM8
   Only these 6 clients are in scope. Skip all other tabs (Aloha Life Massage is paused; Cleaning 4 U, AANMC, Waywest, ProWest, NA tabs are out of scope).

## Steps
1. AUDIT the sheet for each in-scope client, covering backlog + current month + next month:
   - Rows with no topic; rows with a topic but missing main keyword, secondary keywords, or note/angle
   - Monthly quota vs planned rows (quotas are on the "Blog Clients- ALL" tab)
   - Stale statuses: "With Client" or "Ready To Publish" for the current or a past month; "Needs PM Review" items; anything flagged like "Need New Topic"
2. SLACK RESEARCH: In each client's channel, find the LATEST report or report summary (search recent messages for reports, GSC/analytics summaries, linked Google Docs, files, or canvases; read linked Google Docs via the Drive connector if accessible). Extract: performance problems, priorities mentioned by the team or client, services added/removed, promos/programs changed, anything affecting content.
3. SYNTHESIZE: For each client, propose new blog topics (with main keyword, secondary keywords, and a 1-2 sentence content angle) grounded in the report findings, and flag any EXISTING planned topics that should change based on new information (e.g., discontinued services, programs the client left, shifted priorities). Also identify exactly which sheet rows currently qualify for drafting (topic present + main keyword present + note/angle present + Topic Approved checked + Status exactly "With SEO Desk"), so they can be listed by name in the review DM. Do NOT draft them yet.
4. REVIEW DM: Send a Slack DM to channel D06U5NPDEQ6 (Francis's personal inbox) summarizing: per-client gaps, stale items, Slack report insights, proposed new topics (formatted as ready-to-paste sheet rows: Date | Topic | Status | Main Keyword | Secondary Keywords | Note/Angle), flagged changes to existing topics, and an explicit list of which row(s) currently qualify for drafting. End the message clearly stating that no blogs will be written until Francis replies in this DM thread/channel with something like "proceed" or "go ahead," and that a separate daily check will pick up his reply automatically (checking for up to 7 days before giving up on this cycle). Keep it scannable with headers per client.

## Hard rules
- NEVER post messages in client channels or to anyone other than DM D06U5NPDEQ6. Slack is read-only except for that one review DM.
- NEVER draft any blog content in this run. That is handled exclusively by the "blog-masterlist-draft-check" task after Francis approves.
- NEVER edit the Google Sheet; propose rows for Francis to review instead.
- Never contact clients or send anything external.
- If a channel or the sheet is inaccessible, note it in the DM rather than failing silently.