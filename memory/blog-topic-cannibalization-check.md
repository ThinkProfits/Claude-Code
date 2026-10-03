---
name: blog-topic-cannibalization-check
description: "Always check existing site content before presenting a blog topic list, to avoid duplicate/cannibalizing content"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ac02c2dd-7b4c-4abf-9586-0c47a4486371
  modified: 2026-09-10T17:16:32.602Z
---

Before presenting a batch of blog topic ideas (not yet a single assigned post), check the client's existing indexed content for overlap. Pull the blog/post sitemap (or general pages sitemap if no dedicated one exists) and cross-check with Semrush `resource_organic_unique` sorted by keywords_count, since that catches indexed pages a sitemap misses. Flag any proposed topic that duplicates or would cannibalize an existing page, and state the finding even when the answer is "no overlap found."

**Why:** Francis (francis@thinkprofits.com) asked directly whether existing content had been checked, after a topic list was already delivered without that check being surfaced. The check should happen up front and be stated proactively, not only when asked.

**How to apply:** Applies to any client blog-topic-ideation task, not just when the `agency-blog-writer` skill is explicitly invoked. It's baked into that skill's "Topic Ideation Phase" section (`.claude/skills/agency-blog-writer/SKILL.md`), but apply it by habit even for quick manual research.
