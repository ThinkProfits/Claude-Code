---
name: blog-masterlist-draft-check
description: Daily check: waits for Francis's Slack go-ahead after a blog masterlist planning run, then drafts approved blogs
---

You are checking whether Francis (SEO desk at ThinkProfits) has approved the most recent "Blog Content Ops Check" planning-run review that was sent to his Slack DM (channel D06U5NPDEQ6). That review DM is produced by a separate scheduled task ("blog-masterlist-planning-run") which audits a blog content calendar, does Slack research, and proposes new topics, but does NOT draft anything. Blog drafting only happens here, in this task, and only after Francis explicitly says to proceed. Work autonomously; do not ask questions in this run.

## Step 1: Check Slack for a pending review and a reply
1. Read the message history of Slack DM channel D06U5NPDEQ6 (recent messages, e.g. last 50-100, going back at least 10 days).
2. Find the most recent message that looks like a planning-run review DM (it starts with something like "*Blog Content Ops Check" and contains per-client sections and proposed topic rows). Note its timestamp. If no such review message exists at all, there is nothing to check — exit immediately, doing nothing else.
3. Check whether there is already a completion DM (a shorter message confirming which drafts were written, or that none qualified) sent AFTER that review message's timestamp. If one exists, this cycle has already been handled — exit immediately, doing nothing else.
4. Check whether Francis (the human, not the bot/assistant) has sent any reply message in that DM channel after the review message's timestamp. Any reply at all counts as approval to proceed — it does not need to be an exact phrase like "proceed"; anything that reads as an instruction to continue, a yes, a thumbs-up, "go ahead," "do it," etc. all count. If you are genuinely unsure whether a given reply means "go" versus something else (e.g. a question back, or an instruction to change something first), do NOT treat it as approval — exit without drafting and without sending any message.
5. If Francis has NOT replied yet:
   - Calculate how many days have elapsed since the review DM's timestamp.
   - If fewer than 7 days have elapsed, exit quietly — do nothing else, do not send any Slack message.
   - If 7 or more days have elapsed with no reply, treat this cycle as expired. Do nothing further (no drafting, no message) — the next planning run will produce a fresh review DM to replace this one.
6. If Francis HAS replied with an approval-type message: proceed to Step 2 below.

## Step 2: Draft the approved blogs (only reached if Step 1 confirmed approval)

### Data sources
- Google Sheet "BLOG Masterlist - 2024-2026", file ID: 1XGPlGjBIF8TTzsYLBiWui_PBVMld7j19IBsFRVwZmJw. Read it via the Google Drive connector (download as xlsx and parse with Python/openpyxl in the sandbox to get ALL tabs; read_file_content only returns the first tab). Columns on client tabs are approximately: A Date, B Topic, C Status, D Topic Approved, E Main Keyword, F Secondary Keywords, G Note/Content Angle/Writing Instructions, H Blog Written (link), I Blog Published (link), J Notes. Verify headers per tab before parsing.
- In-scope clients only: Jamie Davis, John Sadler Plumbing & Heating, Munro & Crawford, Spiedr, Vision Plumbing Heating Cooling, ThinkProfits. Skip all other tabs.
- Re-check the sheet fresh (don't rely solely on what the review DM said — Francis may have made edits in the sheet since then).

### Drafting rule
Draft blogs ONLY for rows meeting ALL of: topic present + main keyword present + note/angle present + Topic Approved checked + Status exactly "With SEO Desk". Use the agency-blog-writer skill and follow all its guardrails (Canadian/BC accuracy for Canadian clients, no competitors, 1200-2000 words, no em dashes, tone-matched to the client's site, blog + GBP post + social posts). Save each draft as a markdown file in the outputs folder. Limit: max 3 drafts per run; prioritize oldest due first.

### Completion DM
Send ONE Slack DM to channel D06U5NPDEQ6 confirming which draft(s) were written (with file names), or noting that no rows currently qualify (in case the sheet changed since the review DM). Keep it brief since the full audit detail was already covered in the review DM.

## Hard rules
- NEVER post messages in client channels or to anyone other than DM D06U5NPDEQ6.
- NEVER draft anything unless Step 1 confirms Francis has actually replied with an approval-type message after the latest review DM.
- NEVER edit the Google Sheet.
- Never contact clients or send anything external.
- If the sheet or Drive is inaccessible when you do reach Step 2, note that in the completion DM rather than failing silently.