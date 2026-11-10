---
name: client-facing-blog-drafts
description: Client blog drafts and their Google Docs hold only title tag, meta, slug, keywords/intent and the post; scope line, masterlist row, image note, GBP/social posts and implementation notes go in a separate internal notes file
metadata:
  type: feedback
---

Every client blog draft is client facing. The `.md`/`.docx` and the Google Doc contain only: title tag, meta description, URL slug, primary + secondary keywords and search intent, then the post (H1 through FAQ, with inline `[IMAGE: ...]` placements).

Never put these in the client file: a scope line or "editor only" note, the masterlist row / draft number / drafted-on date, an image-sourcing note ("all images must be real photos..."), the GBP post, Facebook/Instagram posts, or implementation notes. They go in `internal-notes/<slug>-notes.md` next to the draft, which is never uploaded to the client doc.

**Why:** Francis, 2026-11-10: the files are client facing, so internal editor notes don't belong in them.

**How to apply:** Built into `.claude/skills/agency-blog-writer/SKILL.md` (Required Deliverables) and `clients/john-sadler/blogs/2025-backlog/_BRIEF.md`. Applies to every ThinkProfits client blog. All existing John Sadler drafts (2025-backlog 01-08, 2026 Navien x5) and their Google Docs were converted on 2026-11-10. Related: [[blog-fact-check-standard]], [[page-update-doc-format]].
