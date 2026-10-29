---
name: blog-fact-check-standard
description: Andrew's Oct 2026 blog review lessons that apply to every client - source every fact, verify links and client claims, match the client's tone history
metadata:
  type: feedback
---

Andrew's review of the Jamie Davis Towing drafts and Munro & Crawford's client feedback (Slack, 2026-10-28 and 2026-10-29) exposed problems that apply to every client blog, not just those two.

1. **Source every external fact, linked on first mention, and open the source to confirm it says exactly that** (right publisher, right year, right figure). Drafts had invented stats and links to pages that didn't contain the claim.
2. **Check every internal link against the live sitemap and write it as a full absolute URL.** Drafts had malformed `http:///` links and guessed slugs for pages that don't exist.
3. **Never invent client experience or capabilities.** No made-up first-person anecdotes ("every fall we tow…"), and no service, equipment or phone number that isn't confirmed by the live site or the client.
4. **No overstated absolutes, and don't trust the client's old posts as a source.** Check every claim before reusing it.
5. **Time-sensitive figures** (fines, rates, limits, dates) say "at the time of writing" and link the official source.
6. **Question headings only for the main search queries. Never repeat a heading question in the FAQ. The FAQ is always the last section.**
7. **Every deliverable lists meta title, meta description (under 155 characters), slug and primary keyword.**
8. **Match the tone the client has already approved.** Munro & Crawford rejected three casual drafts in a row after earlier, more formal posts had gone over well. Before drafting, read the client's last few *approved* posts and the voice rules in CLIENT.md section 8. Don't apply a generic conversational house style.

**Why:** Andrew had to fix all four Jamie Davis posts before sending them to the client, and Munro & Crawford rejected the Notary vs Lawyer blog for tone. Each correction costs Andrew review time and client goodwill.

**How to apply:** run this as a checklist on every client blog before handoff. Per-client detail lives in `clients/jamie-davis/CLIENT.md` and `clients/munro-crawford/CLIENT.md` section 8. Related: [[blog-topic-cannibalization-check]], [[paa-research-standard]].
