---
name: weekly-seo-report-slack-check
description: Weekly check of Slack channel D06U5NPDEQ6 for the ThinkProfits Weekly SEO Optimization report
---

Check the Slack channel/DM with ID D06U5NPDEQ6 for a message posted in the last 7 days containing the phrase "ThinkProfits Weekly SEO Optimization" (a Semrush Position Tracking report). Use slack_read_channel or slack_search_public_and_private to find it.

If no matching message is found: report that clearly as a chat message and stop.

If found:
1. Read the attached full markdown report file via slack_read_file to get the "Things to Do This Week" priority items and "Revamp" recommendations.
2. Send the report (forwarded as-is, or its priority sections) to the Lovable project "thinkprofits" (project_id: 12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17, workspace_id: rJj3ci8koRXi6ThNECB7) using the Lovable send_message tool. Ask it to implement the priority action items — typically a Vancouver SEO services page refresh, PPC/Google Ads page protection, and local signal strengthening on contact/about pages — while keeping the existing design/structure intact and not fabricating any stats, rankings, or claims not already in the report or on the site.
3. Wait for send_message to return with status "completed" and a response summary. Trust that response directly as confirmation — do NOT call get_project, get_diff, or fetch the live site to re-verify (this is intentional, to save Lovable credits, per explicit user instruction).
4. Reply in the Slack thread (thread_ts = the found message's ts, channel D06U5NPDEQ6) with "This has been implemented." followed by a short bullet summary of what changed, drawn from Lovable's response summary. Also note any recommended items from the report that are research/audit tasks (e.g. competitor SERP review, keyword-to-page mapping) rather than buildable changes, and flag those as still outstanding.

Report a brief summary of what was done as a chat message as well.