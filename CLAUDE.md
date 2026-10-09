# ThinkProfits — Claude Code workspace

Vancouver, BC digital marketing agency. AEO, GEO, SEO, PPC, web design/dev, email marketing, content.

This repo holds **ThinkProfits work only**. Work for any other agency or any personal project does not belong here. Don't copy it in, link to it or mention it.

## Start of every task

1. The SessionStart hook pulls the latest from GitHub automatically. If it reports a conflict, stop and tell the user before editing.
2. Read `memory/INDEX.md` and the files for the client you're working on.

## End of every task

Commit and push before finishing:

```
git add -A
git commit -m "<what changed, in plain words>"
git push
```

A background job also syncs every 30 minutes on Francis's PC (once a day on other devices, see SETUP-NEW-DEVICE.md). Still push yourself so teammates and cloud sessions see the work right away. Never commit secrets (API keys, OAuth `client_secret*.json`, `token.json`, `google-ads.yaml`). `.gitignore` blocks the usual names, so check before forcing anything.

## Memory

Save durable ThinkProfits facts (client quirks, approvals, standing rules, tool setup) to `memory/<short-name>.md` and add a line to `memory/INDEX.md`. Don't use personal auto-memory. The repo is the team's memory, and it travels to every machine and cloud session.

## Tools of record

- **Semrush MCP** for SEO/traffic/competitive data. Never substitute other tools when Semrush can answer it.
- **Google Workspace / Gmail** (Drive MCP connected) for docs and comms.
- **BrightLocal MCP**: local rank tracking, reputation, citations, AI visibility.
- **Make.com MCP** (`.mcp.json`, `make-token`): blog and GBP publishing scenarios.
- **gbp-audit MCP**: Google Business Profile audits (see `memory/gbp-audit-quota-blocked.md`).
- **gsc**, **ga4** and **google-ads-keywords** MCPs: local servers (code in `mcp-servers/`). They run only on a PC where they've been installed and authenticated, **not in claude.ai cloud sessions**.
- Canva connector installed but not authorized (auth via claude.ai connector settings when needed).

## Writing standards

- Canadian English spelling and conventions.
- Client-facing copy: conversational but professional, sharp wit welcome, no sarcasm or inside jokes.
- Avoid jargon unless the client is technical.
- SEO/content deliverables: state target keyword and search intent.
- Proposals/reports: headers and bullets, not dense paragraphs.
- Never guarantee specific rankings or results. Flag such language for revision instead of writing it.
- Budget/ad spend: present as ranges with stated assumptions, never fixed promises.
- Cite sources for marketing/SEO statistics.

## Collaboration

Work openly. Reusable prompts, templates and skills go in this repo (or shared Drive), not in one-off personal files. Note reusable components clearly.

## Layout

- `clients/<client>/`: per-client working files (aanmc, clearset, john-sadler, mujo, mysaskfarm, spiedr, thinkprofits, Vision). New client = new folder.
- `gbp-handoffs/week-of-<Monday>/`: weekly GBP handoff `.md` files for Codex. The protocol is `gbp-handoffs/claude-handoff-instructions.md`.
- `automations/`: Make.com blueprints and automation setup docs.
- `scheduled-tasks/<name>/SKILL.md`: prompts for recurring routines (blog masterlist, SEO report roadmap, Slack relay, weekly report check).
- `mcp-servers/`: code for the local gsc, ga4, google-ads-keywords and gbp-audit servers. **No credentials.** Each person authenticates their own copy.
- `memory/`: shared facts and standards, indexed in `memory/INDEX.md`.
- `scripts/tp-sync.ps1`: the pull/commit/push sync used by the background job.

## Skills (`.claude/skills/`)

- `agency-blog-writer`: client blogs with brand-safe guardrails (blog + GBP post + social posts)
- `gbp-topic-finder` → `gbp-post-writer`: choose, then write, GBP posts
- `blog-make-handoff`: prep an approved Google Doc for the Make.com → WordPress pipeline
- `seo-content-writer`, `geo-content-optimizer`: general SEO content and AI-citation optimization
- `make-scenario-building`, `make-module-configuring`, `make-mcp-reference`, `make-api-shell-connection-workflow`: building Make.com scenarios
