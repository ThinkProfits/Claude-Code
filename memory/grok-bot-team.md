---
name: grok-bot-team
description: Francis's Grok Bot team ("The Man" plus GBP Manager, Citations Builder, QA Reviewer, Local SEO Strategist, Analytics & Search Data, SEO & AI Briefing, Task Tracker, Sales Contract Bot), its publishing chain, the daily digest to Claude, and the plan to take over all clients later.
metadata:
  node_type: memory
  type: reference
  modified: 2026-11-26
---

Francis runs Grok Bot. He calls its manager **"The Man"**, and The Man manages these bots:
- Citations Builder
- GBP Manager (handles GBP for all clients: drafts each change and waits for Francis's OK)
- QA Reviewer
- Local SEO Strategist (content and strategy)
- Analytics & Search Data (added 2026-11-26): the bot for GSC, GA4 and Semrush data (traffic and ranking drops, indexing, URL Inspection, report numbers). Read-only by default; requests indexing only once approved, through the normal chain. Briefs about GSC or GA4 can name `Bot: Analytics & Search Data`.
- SEO & AI Briefing (added 2026-11-26): sends Francis a daily SEO, Google-update and AI-tools briefing at about 14:00 PHT.
- Task Tracker (added 2026-11-26): read-only. Keeps one deduplicated backlog from `E:\GrokBot\` (tasks, BACKLOG.md, briefings, handoffs), this `from-the-man/` folder, Slack, Gmail and meeting notes. Sweeps at 17:00, 23:00 and 05:00 PHT and reports changes to The Man, who updates the Task Dashboard. It never writes to `E:\GrokBot`.
- the shared Sales Contract Bot

The team is organised by job, not one bot per tool: Citations Builder also covers BrightLocal, GBP Manager covers Business Profiles, QA Reviewer does checks.

**Golden rule (Francis, 2026-11-26):** the Grok Bot account handles only ThinkProfits and ThinkProfits' clients. No other agency, and no other agency's clients, may appear in any bot's work, files or memory. Briefs and anything Claude gives Grok follow the same rule.

**Publishing chain:** the creating bot makes the item, then QA Reviewer checks it, then The Man does a final check for quality, readability and credibility, then Francis approves, then the publishing bot acts. Nothing is published without every step.

**Questions Board:** The Man keeps every open question for Francis, Shawn and others on its Questions Board, a cursor.com canvas (link in `from-the-man/merged/2026-11-25_1655_initial-snapshot.md`).

**Reports to Claude:** The Man drops a note into [`from-the-man/`](from-the-man/README.md) every time it saves a memory. It also writes a daily digest around **06:00 PHT**, `YYYY-MM-DD_0600_daily-digest.md`, covering the previous 24 hours. Francis asked for the digest on 2026-11-26 at 02:18 PHT and moved it from 23:30 to 06:00 at 02:37: "thats usually the time when I head off". Claude merges each file, then moves it into `merged/`.

**Work from Claude to Grok:** Claude does the research and writes task briefs in `E:\GrokBot\tasks\open\` (exists since 2026-11-26; Grok suggests names like `YYYY-MM-DD__client__task.md` with `Bot:` and `Status:` lines). Grok drafts the work in `E:\GrokBot\work\`. Francis approves. Grok's client walkthrough is in `E:\GrokBot\briefings\thinkprofits.md`.

**Taking over all clients is a later plan, not a current one.** Francis, 2026-11-25 16:56 PHT: "I want you to handle everything from writing QA reviews and posting for all clients now. but after the thinkprofits posting is 110% successful. lets talk about this later." Until Francis says otherwise, every client except ThinkProfits keeps the current pipeline: Saturday drafting, Slack approvals, Codex handoff files (see [GBP brain/body split](gbp-brain-body-split.md)).

**Current Grok work (2026-11-26):** Francis said "go" at 05:03 PHT for the ThinkProfits-own website drafts only (see [ThinkProfits site drafts by Grok](thinkprofits-site-drafts-grok.md)); other clients' tasks stay on hold. The Man accepted every correction in `E:\GrokBot\handoffs\_early-2026-11\CLAUDE-REVIEW.md` (client industries come from each CARD.md).

**Why:** Grok's first reports (2026-11-24/25) got client industries and dates wrong. Check facts in its notes before merging them, and the newer dated fact from Francis wins.
