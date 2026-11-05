---
name: munro-blog-html
description: Turn an approved Munro & Crawford (munrocrawford.ca) blog draft into copy-and-paste-ready HTML for the WordPress Text/Code editor, matching the style of the firm's live posts. Use when the user says 'make the code for the Munro blog', 'HTML for posting', 'paste-ready code for Munro', 'get this Munro blog ready to post', or points at a .md draft in clients/munro-crawford/blogs/. This skill does not write or review content. Use agency-blog-writer for drafting.
---

# Munro & Crawford blog → paste-ready HTML

Converts an approved `.md` draft into one HTML file that can be pasted straight into the WordPress **Text** (Code) tab on munrocrawford.ca. The house pattern comes from the live posts published from July 2026 onward (business-succession-planning, how-to-contest-will-bc, avoiding-probate-bc), pulled from `https://munrocrawford.ca/wp-json/wp/v2/posts`.

## Run it

```bash
python -I .claude/skills/munro-blog-html/scripts/md_to_wp_html.py clients/munro-crawford/blogs/2026/<draft>.md
```

This writes `<draft>-wp-paste.html` next to the draft. Several drafts can go in one call.

## What the draft must look like

The output depends on the draft following the agency-blog-writer format:
- `**Title tag:**`, `**Meta description:**` and `**URL slug:**` lines above the article.
- One `# ` H1 (the post title), then `##` sections and `###` subsections.
- A `> **Quick Answer:** ...` blockquote.
- Images written as `[IMAGE: what it shows | alt: alt text | file: name.jpg]`. The first one is treated as the hero image.
- `## Frequently Asked Questions` with `###` questions. The article ends at the first `---` after the FAQ, so GBP/social posts and implementation notes are left out automatically.
- Markdown links, `**bold**`, `*italic*`, `-` bullets and pipe tables are all supported.

## House pattern (what the script produces)

1. An HTML comment at the top with the title tag, meta description, slug, author `munro_admin`, hero file and alt text. WordPress hides it. The values go into the WordPress/Yoast fields.
2. The post title as `<h2>`, because the theme prints the real H1 from the Title field.
3. `<!-- Insert hero image here: file.jpg -->`, then the Quick Answer `<blockquote>`.
4. Section headings as `<h2><strong>…</strong></h2>` and subsections as `<h3><strong>…</strong></h3>`.
5. Bullets as `<li><strong>Term:</strong> explanation</li>`.
6. Internal links open in the same tab. External links (bclaws, CRA, SCC) get `target="_blank" rel="noopener noreferrer"`.
7. Remaining images become `<!-- Insert image here: file | alt: … | shows: … -->` placeholders.
8. FAQ questions as `<h3><a href="#">Question</a></h3>`, the same look as the live posts, followed by the answer.
9. A closing `<p><a href="https://munrocrawford.ca/contact/">Contact a Lawyer</a></p>`.
10. Typographic quotes and every non-ASCII character are written as numeric entities (`&#8217;`, `&#8220;`), so nothing turns into a "�" character when pasted.

## FAQ schema: microdata, not JSON-LD

**The site strips anything inside square brackets from post content.** The live posts that carry a JSON-LD `<script>` show `"mainEntity": ` with the array gone (checked 2026-11-05 on how-to-contest-will-bc, avoiding-probate-bc and business-succession-planning). Their FAQ schema is therefore broken. This matches the CLIENT.md note that the "page builder breaks custom code".

To get around this, the script wraps the FAQ in schema.org **microdata** (`itemscope` / `itemprop` attributes on the HTML). Microdata needs no brackets, so it survives intact. Never add a JSON-LD block to the body.

The client standard is still **Easy Accordion with schema turned on** (CLIENT.md, section 8). If the team uses Easy Accordion for this post:
- delete the FAQ `<div itemscope …>` block from the paste file
- paste the questions and answers into a duplicated accordion
- check that the schema toggle is on

Use only one of the two methods, or Google gets duplicate FAQ markup.

## Posting checklist (give this to the user with the file)

1. In the WordPress editor, open the **Text** tab (not Visual) and paste the whole file. Do not switch to the Visual tab afterwards, because it can drop the microdata attributes.
2. Copy the title, slug, meta description and focus keyword from the top comment into the WordPress and Yoast fields. Set the author to `munro_admin`.
3. Upload the images, set the featured image and replace each `<!-- Insert … -->` placeholder with the real image and its alt text.
4. Preview the post: check the table (if any), the links and the FAQ.
5. After publishing, run the URL through Google's Rich Results Test or the Schema Markup Validator and confirm the FAQPage is detected.

## Rules

- Do not change the wording. The draft has already been through review and Andrew's approval. If something reads wrong, flag it instead of editing.
- Canadian spelling, no outcome promises, no "expert" or "specialist" claims (LSBC Code ch. 4). These are already enforced at the writing stage. Flag anything that slipped through.
- Keep the `.md` as the source of truth. Re-run the script after any edit to the draft instead of hand-editing the HTML.
