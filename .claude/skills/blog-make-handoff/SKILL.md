---
name: blog-make-handoff
description: "Prepare an already-approved blog post for ThinkProfits' Make.com Google-Doc-to-WordPress publishing pipeline. Use whenever the user pastes a Google Doc link and says something like 'here's the approved blog', 'send this to the sheet', 'get this ready for Make', 'this one's approved, set it up for [client]', or hands over a finished/reviewed article that now needs to go into a client's Make.com blog-automation spreadsheet. This skill does NOT write or approve blog content — that's agency-blog-writer's job — it only handles the handoff step immediately after approval: reading the approved doc, reformatting it to the pipeline's required structure, creating the clean production copy in the client's Drive folder, and handing back the exact values the user needs to paste into that client's spreadsheet. Always use this instead of manually explaining the Make.com column layout from scratch, since the conventions here were worked out and locked in across a real client rollout (Aloha Life Massage) and should stay consistent for every client on this pipeline."
---

# Blog → Make.com Handoff

Turns an approved blog (a Google Doc someone has already reviewed and signed off on) into the exact inputs ThinkProfits' Make.com scenario needs to create a WordPress draft — a clean production Doc plus the spreadsheet row values. This is the "brain" half of a brain/body split: Claude prepares content and metadata, the human pastes it into the sheet, and Make/Codex on the other end actually publishes. Same shape as the GBP pipeline's brain/body split (see `gbp-brain-body-split` memory) — the reasoning there applies here too: keeping a human-approval gate between "content is ready" and "it actually goes live" is the point, not a limitation to work around.

## When to Use

- User pastes a Google Doc link for a blog that's already been approved and says it's ready for Make/WordPress
- User asks "what goes in the sheet for this one" about a finished article
- Setting up a new client on this same Make.com pipeline (same conventions apply, different Drive folder/sheet)

Not for: writing the blog itself (`agency-blog-writer`, `seo-content-writer`), choosing what to write about, editing the Make.com scenario, or touching the spreadsheet directly (no tool exists for that — see Hard Constraints below).

## Step 1: Confirm which client, and read the approved Doc

If the client isn't already obvious from context, ask. The client determines which Drive folder the production copy goes into and which sheet the values are meant for — don't assume every client's sheet looks like Aloha's.

Read the approved Doc's content via the Drive connector. This is the source of truth for the article body — don't ask the user to paste the text in chat.

## Step 2: Reformat to the pipeline's required structure

Make exports this Doc as HTML and feeds it straight to WordPress, so the Doc's structure IS the published post's structure. Check/fix:

- **No H1 in the body.** WordPress renders the post title (from the spreadsheet, not the Doc) as the page's H1. An H1 inside the Doc would create a duplicate, visually-wrong second title.
- **Opens with an intro paragraph**, then H2 sections, H3 subsections where a section needs them.
- **Normal paragraphs, lists, bold text, and hyperlinks are all fine** — Make preserves them through the export. Don't flatten them to plain text.
- **FAQ section, if present, needs an exact structure**: an H2 reading exactly "Frequently Asked Questions", each question as an H3, and everything after that H3 up to the next H3 or H2 counts as the answer — not assumed to be a single paragraph. An answer can legitimately span multiple paragraphs, a list, bold text, or a link. (The Make scenario converts this into a native `<details>/<summary>` accordion — see `blog-automation-faq-accordion-architecture` memory for why that approach was chosen over a plugin, and why FAQ schema is intentionally not part of this yet.)
- **No SEO metadata inside the body.** Post title, SEO meta title, SEO meta description, slug, and excerpt live only in the spreadsheet. If the approved Doc has these written at the top (common when a writer drafts title/meta alongside the article), pull them out for Step 3 and don't carry them into the production copy — leaving them in would publish them as visible text in the article.

If the approved Doc already matches this structure, don't rewrite it just to rewrite it — the goal is a correct production copy, not a stylistic pass.

## Step 3: Create the production Doc

Find the client's Drive folder (search Drive by client name — don't guess an ID or create a stray file at the root). Create a new Google Doc there containing just the cleaned article body, using HTML content so headings/bold/lists/links convert properly rather than landing as plain text.

Name it something identifiable (e.g. `<Client> — <Post Title>`), matching how the client's other content files are named.

## Step 4: Hand back the paste-ready values — nothing else

Reply with only what the user needs to manually paste into the sheet, clearly labeled, plus the new Doc's link. Do not paste the full article text back into the chat — the whole point of Step 3 was to avoid that.

```
Post Title:            <post title>
SEO Meta Title:         <SEO title tag>
SEO Meta Description:   <meta description>
Slug:                   <url-slug>
Excerpt:                <1-2 sentence excerpt>
Blog Google Docs Link:  <link to the new production Doc>
```

Column names and order vary by client (Aloha Life Massage's sheet, for example, is A:L with column E used for detailed processing status and a separate column J as the actual publish trigger — the user sets it to `ready to publish`, Make flips it to `drafted` once the draft is created). Present the values labeled like above so they map cleanly onto whichever columns that client's sheet actually has, rather than assuming Aloha's layout is universal. If this is a new client's first time through this pipeline and you don't know their column layout, ask rather than guessing.

## Hard Constraints

- **Never write to the spreadsheet directly, and never claim to have.** There is no tool that edits an existing sheet's cells/rows — only whole-file creation exists, which would destroy the rest of the sheet's data. Sheet population is always a manual paste by the human. If asked to "just put it in the sheet," explain this limit rather than attempting it.
- **Never touch the Make.com scenario itself** — that's Codex's side of this split.
- **FAQ schema (FAQPage JSON-LD) is out of scope.** It was deliberately deferred to a later phase — see the memory file referenced above. Don't add it unprompted.
- **WordPress Post ID / Draft URL / Error Message columns are Make's to fill, not yours** — leave those blank in whatever you hand back; they get written after Make actually runs.

## Related Skills

- `agency-blog-writer`: writes and gets the blog approved in the first place — run before this skill, not instead of it
- `gbp-post-writer` / `gbp-topic-finder`: the equivalent brain-half skills for the GBP posting pipeline, same brain/body philosophy
