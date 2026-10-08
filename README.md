# ThinkProfits — Claude Code

The shared workspace for ThinkProfits work done with Claude Code: client files, GBP handoffs, automations, skills, routines and the team's shared memory. Rules for Claude live in [CLAUDE.md](CLAUDE.md).

## Using it

**In the browser (claude.ai/code):** start a session and select the `ThinkProfits/Claude-Code` repo. Skills, CLAUDE.md and `memory/` load automatically. The local MCP servers (gsc, google-ads-keywords, gbp-audit) aren't available there. Claude.ai connectors (Semrush, Drive, Slack and so on) work as usual.

**On your PC:**

```
git clone https://github.com/ThinkProfits/Claude-Code
cd Claude-Code
claude
```

Each session pulls the latest changes on start (`.claude/settings.json`) and pushes when the task is done (CLAUDE.md rule).

**Setting up another PC?** Follow [SETUP-NEW-DEVICE.md](SETUP-NEW-DEVICE.md) for the full walkthrough, including a once-a-day auto-sync.

**Optional auto-sync (Windows):** catches edits made outside Claude. Run once, then it syncs every 30 minutes:

```
schtasks /Create /TN tp-repo-sync /SC MINUTE /MO 30 /TR "powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File \"<path-to-clone>\scripts\tp-sync.ps1\""
```

Log: `scripts/logs/tp-sync.log`. If a sync hits a conflict it stops without pushing. Resolve it with `git status`, or ask Claude.

## Local MCP servers

Code only. Credentials are never committed. Set each one up on your own machine:

| Server | Folder | Setup |
|---|---|---|
| gsc (Search Console) | `mcp-servers/mcp-gsc/` | see its README, run `gsc_auth.py`, then `claude mcp add` |
| google-ads-keywords | `mcp-servers/google-ads-keywords/` | see its README and `setup_auth.py` |
| gbp-audit | `mcp-servers/gbp-audit/` | see its README and `auth_helper.py` |

For each one, create a venv (`python -m venv .venv` then `.venv\Scripts\pip install -r requirements.txt`) and get the OAuth client file from the agency Google Cloud project (`gsc-claude-connection`). Don't commit that file.

## Layout

| Folder | What's in it |
|---|---|
| `clients/` | One folder per client |
| `gbp-handoffs/` | Weekly GBP handoff files for Codex + the handoff protocol |
| `automations/` | Make.com blueprints and automation docs |
| `scheduled-tasks/` | Prompts for recurring routines |
| `.claude/skills/` | Team skills (blog writer, GBP topic/post writers, Make.com, SEO/GEO) |
| `memory/` | Shared facts and standards (start at `memory/INDEX.md`) |
| `mcp-servers/` | Local MCP server code |
| `scripts/` | Repo sync script |
