# From The Man: memory inbox for Claude Code

This folder is a one-way memory handoff from **The Man** (Grok Bot, Francis Uy's bot manager) to **Claude Code**. Francis set it up on 2026-11-25 (16:54 PHT): "everytime you have something saved, create MD file for claude so he can read it and be able to merge your data to his".

## How it works

1. **The Man writes.** Every time The Man saves something to its own memory, it drops one new file here.
2. **Claude reads and merges.** At the start of a task (after reading `memory/INDEX.md`), Claude checks this folder for files not yet in `merged/`. For each one, oldest first, Claude merges the facts into its own memory the usual way: update or create `memory/<short-name>.md` and update `memory/INDEX.md`. If a note has `supersedes:`, Claude updates or replaces the fact it names.
3. **Claude files it.** After merging a note, Claude moves that file, unchanged, into `from-the-man/merged/`.

## File names

`YYYY-MM-DD_HHMM_<slug>.md`, with the date and time in Asia/Manila (PHT, UTC+8). Example: `2026-11-25_1655_initial-snapshot.md`.

## File format

```
---
source: the-man
date: 2026-11-25 16:55 (Asia/Manila)
type: behavior | workstream | profile | world
topic: <short topic, e.g. gbp, citations, setup>
supersedes: <optional: the file or fact this replaces>
---

Plain facts, one per bullet. Francis's exact words are quoted where he gave them,
with the date and time (PHT).
```

Types:
- `behavior`: how the bots or Claude should work (rules, approvals, process).
- `workstream`: the state of a piece of work (a client, a campaign, a plan).
- `profile`: facts about Francis, Think Profits or the team.
- `world`: outside facts (tools, platforms, Google limits).

## Rules

- The Man only adds new files here. It never edits Claude's own memory files, `memory/INDEX.md` or `CLAUDE.md`. (The one-time setup on 2026-11-25 was the exception, done at Francis's request; see the initial snapshot.)
- Claude never edits or deletes files in this inbox. The only change Claude makes here is moving a processed file into `merged/`.
- If a note conflicts with something Claude knows, the newer dated fact from Francis wins. If it is unclear, Claude asks Francis rather than guessing.
- No secrets, passwords or tokens ever go in these files. This folder is committed to the team's GitHub repo by the normal sync.
