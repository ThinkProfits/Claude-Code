# Slack → Lovable Approval Relay — Claude Code Setup Guide

**What this is:** step-by-step instructions for recreating, in Claude Code (the CLI), the same automated relay that currently runs as a scheduled task in Cowork for Francis. The relay watches a Slack DM for ChatGPT-drafted content briefs tagged `@Claude`, and once Francis replies "approved" in the thread, forwards the instruction verbatim to a Lovable project. It never forwards anything twice, and a "rejected" reply permanently kills that instruction.

**Reusable template:** the logic in Step 4 (the prompt) is generic — only the IDs in the "Configuration values" section are ThinkProfits/Francis-specific. Anyone on the team can copy this doc, swap the IDs for their own Slack DM and Lovable project, and get the same relay for their own workflow. Please don't fork this file per-person — update the config table instead so we're all working from one copy (see the note at the bottom on where to keep it).

---

## 1. Prerequisites

- Claude Code CLI installed and authenticated (`claude` on PATH; run `claude --version` to confirm).
- A Slack MCP server connected, with permission to read and post in the target DM.
- A Lovable MCP server connected, with access to the target workspace/project.
- Ability to schedule a recurring job on the machine that will run this (cron on macOS/Linux, Task Scheduler on Windows, or a CI runner) — Claude Code itself has no built-in scheduler, unlike Cowork's scheduled tasks.

## 2. Connect the MCP servers

Run these once (adjust server names/args to match whatever Slack and Lovable MCP packages your org uses — check with whoever set up the Cowork connectors, since the same underlying integrations can usually be reused):

```bash
claude mcp add slack -- <slack-mcp-server-command-and-args>
claude mcp add lovable -- <lovable-mcp-server-command-and-args>
```

Verify both are connected and list their tools:

```bash
claude mcp list
```

You're looking for tools equivalent to:
- `slack_read_channel`, `slack_read_thread`, `slack_send_message` (Slack)
- `send_message` (Lovable — sends a chat message to a Lovable project's AI agent)

Unlike the Cowork session this was copied from, Claude Code doesn't require a separate "load tool schema" step (no `ToolSearch`) — once an MCP server is connected, its tools are just available.

## 3. Configuration values (ThinkProfits / Francis's current setup)

| Item | Value |
|---|---|
| Slack DM channel ID (Francis's DM with the relay bot) | `D06U5NPDEQ6` |
| Francis's Slack user ID | `U06UERMAAHJ` |
| "Claude" Slack app/user ID (the tag the relay watches for) | `U0ATBMCHVE1` |
| "ChatGPT" Slack app/user ID (the footer the relay requires) | `U0BLJPPRAAF` |
| Lovable project ID | `12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17` |
| Lovable project name | Thinkprofits Rebuild |

If you're adapting this for a different Slack DM or Lovable project, replace these six values everywhere they appear in Step 4's prompt and nowhere else needs to change.

## 4. The relay prompt

Save this as a file, e.g. `slack-lovable-relay-prompt.md`, in whatever directory you'll run Claude Code from. This is the literal instruction Claude Code should receive on every scheduled run — it is a relay only, not a drafting or research task.

```
You are running a weekday Slack-to-Lovable instruction relay with a human approval gate. Do NOT do any research, planning, or content generation of your own. Your only job is to forward APPROVED instruction messages, verbatim, to a Lovable project — never before they are approved, never if they are rejected, and never twice. Follow these steps exactly.

STEP 1 — Read the Slack DM.
Call the Slack "read channel" tool with channel_id = "D06U5NPDEQ6", limit = 100, response_format = "detailed".
This DM is Francis Marc Uy's conversation. Bot messages end with a footer like "Sent using @SomeBot". Genuine human comments typed by Francis have NO "Sent using" footer. Note each message's "Message TS" value — you need it for the thread read and any reply.
Do NOT filter by message age. Approval or rejection may arrive days after a message was posted, so evaluate all qualifying messages regardless of age. The thread replies described below decide what to do — not recency.

STEP 2 — Filter to qualifying instruction messages. A message qualifies if BOTH are true:
  (a) It was sent using ChatGPT — footer indicates "Sent using" ChatGPT / @ChatGPT (NOT "Sent using @Claude"). Ignore messages sent using Claude.
  (b) It tags Claude — the text contains the token "<@U0ATBMCHVE1" (renders as @Claude).

STEP 3 — For EACH qualifying message, read its thread and classify.
Call the Slack "read thread" tool with channel_id = "D06U5NPDEQ6", message_ts = that message's TS, response_format = "detailed".
Definitions of a GENUINE Francis reply: a thread reply whose text is his own typed comment, i.e. it has NO "Sent using" bot footer.
Classify in THIS ORDER (first match wins):

  1. ALREADY FORWARDED — any reply contains the phrase "forwarded to Lovable" (case-insensitive):
       → SKIP completely. Do nothing.

  2. REJECTED — no "forwarded to Lovable" reply exists, AND there is a genuine Francis reply whose text contains the word "rejected" (case-insensitive, no bot footer):
       → This instruction is killed. Do NOT forward it, now or ever. Rejection overrides any "approved" reply that may also be present.
       → Acknowledge ONCE: if the thread does NOT already contain a reply with the phrase "acknowledged as rejected", post "🚫 Acknowledged as rejected — this instruction will not be forwarded to Lovable." as a reply in that thread. If that acknowledgement reply already exists, post nothing and move on.

  3. APPROVED AND NOT YET FORWARDED — no "forwarded to Lovable" reply and no genuine "rejected" reply, AND there is a genuine Francis reply whose text contains the word "approved" (case-insensitive, no bot footer):
       → Ready to forward. Handle in STEP 4.

  4. PENDING — none of the above (tagged but neither approved nor rejected):
       → SKIP for now. Do not forward, do not post anything. Leave it so a future run can pick it up once Francis approves (or rejects) it.

STEP 4 — Forward each APPROVED, NOT-YET-FORWARDED, NOT-REJECTED message to Lovable (oldest first):
  - Extract the instruction text: take the full original message body, strip the "Sent using..." footer and the leading @Claude mention token, keep the rest verbatim. Do not summarize, rewrite, improve, or add to it.
  - Call the Lovable "send message" tool with:
        project_id = "12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17"  (Thinkprofits Rebuild)
        message = the extracted instruction text, prefixed with: "Relayed from Slack (Francis / ChatGPT, approved): "
    Leave plan mode off (false).
  - Immediately AFTER the Lovable send succeeds, reply in that message's thread via the Slack "send message" tool:
        channel_id = "D06U5NPDEQ6"
        thread_ts  = that message's TS
        message    = "✅ This has been forwarded to Lovable (Thinkprofits Rebuild)."
    This MUST contain the phrase "forwarded to Lovable" so the message is never forwarded again.

STEP 5 — End quietly.
The only Slack writes you make are: the "✅ ... forwarded to Lovable ..." confirmations (Step 4) and the one-time "🚫 Acknowledged as rejected ..." notes (Step 3.2). Post no summary. If there is nothing to forward and nothing new to acknowledge, make no Slack posts and no Lovable calls.

Important guardrails:
- NEVER forward a message that lacks a genuine "approved" reply from Francis (no bot footer).
- NEVER forward a message that has a genuine "rejected" reply from Francis — rejection is permanent and overrides approval.
- NEVER forward a message that already has a "forwarded to Lovable" reply.
- NEVER treat a bot post (one with a "Sent using" footer) as an approval or rejection, even if it contains the word "approved" or "rejected". This includes your own confirmation/acknowledgement replies.
- Never forward a message sent using Claude, or one that does not tag @Claude (<@U0ATBMCHVE1).
- Do not create new Lovable projects or send to any project other than 12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17.
- Pass instructions through verbatim; you are a relay, not an author.
```

## 5. Run it once by hand

Before scheduling anything, do a dry run so you can see it behave correctly:

```bash
cd /path/to/wherever/you/keep/this
claude -p "$(cat slack-lovable-relay-prompt.md)" --permission-mode acceptEdits
```

Watch the output. On a normal day with nothing new to approve, it should make no Slack or Lovable tool calls at all and just end. Confirm that against the actual Slack DM before trusting the schedule.

## 6. Schedule it (weekdays)

Claude Code has no built-in scheduler — use your OS's, running the same non-interactive command. Example for macOS/Linux `cron`, weekdays at 7:45pm local time (adjust the hour to whenever ChatGPT usually posts the day's package — Francis's briefs typically land around 7:20–7:35pm):

```cron
45 19 * * 1-5 cd /path/to/wherever/you/keep/this && /usr/local/bin/claude -p "$(cat slack-lovable-relay-prompt.md)" --permission-mode acceptEdits >> relay.log 2>&1
```

Notes:
- `--permission-mode acceptEdits` (or your org's equivalent flag for unattended runs) is needed so the scheduled run doesn't stall waiting for a human to approve tool calls — there's no one there to click "yes."
- Log output somewhere (`relay.log` above) so you can audit what a given run did without re-reading Slack.
- If you'd rather trigger this from CI (e.g., a GitHub Actions scheduled workflow) instead of a local cron job, the same `claude -p` invocation works there — just make sure the runner has the Slack/Lovable MCP credentials available as secrets.

## 7. What "identical" means here

This setup reproduces the exact behaviour verified in the current Cowork scheduled task: strict verbatim relay, no drafting, no forwarding without a genuine (non-bot) "approved" reply, no double-forwarding, and permanent rejection. It does not reproduce Cowork's own scheduling UI or its notification system — those are Cowork-specific, so plan on checking `relay.log` (or your CI run history) periodically instead of expecting a push notification.

---

*This file is meant to be the one shared copy for anyone recreating the relay — please keep edits here rather than copying it into a personal folder, and update the config table in Section 3 for your own Slack DM / Lovable project rather than rewriting Step 4's prompt.*
