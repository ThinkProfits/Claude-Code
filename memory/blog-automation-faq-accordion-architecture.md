---
name: blog-automation-faq-accordion-architecture
description: "Make.com blog-posting pipeline (Google Doc -> WordPress) — FAQ handling uses native <details>/<summary> accordion, not a plugin; schema deferred to phase 2; HTML cleanup must preserve bold/italic/links before stripping spans."
metadata: 
  node_type: memory
  type: project
  originSessionId: 30dfad55-8be4-4833-866c-3a17aeefeb5c
  modified: 2026-09-08T07:15:34.664Z
---

Blog automation pipeline (Google Doc → Make.com → WordPress draft) settled on this architecture after review, first built/tested on the Aloha Life Massage client:

**HTML cleanup order (Google Docs export → WordPress), must run in this order, not a blanket strip:**
1. Extract only `<body>` content.
2. Convert bold styled spans (`style="font-weight:700"`) to `<strong>`.
3. Convert italic styled spans to `<em>`.
4. Preserve hyperlinks and their `href` values.
5. Normalize Google Docs lists.
6. Remove remaining `<span>` wrappers.
7. Remove unwanted `style`, `class`, `id` attributes.
8. Convert only the FAQ section to accordion markup.

**Why:** Google Docs HTML export wraps every run in inline-styled `<span>` tags that override theme typography (this is what caused Aloha's first draft to render with tiny unstyled body text). A naive "strip all spans/styles" pass also destroys bold/italic meaning that only exists as inline style, not semantic tags — so styled-span-to-semantic-tag conversion must happen BEFORE the strip step.

**FAQ accordion — native `<details>`/`<summary>`, not a plugin:**
```html
<section class="blog-faq">
  <h2>Frequently Asked Questions</h2>
  <details name="blog-faq">
    <summary>Question text</summary>
    <p>Answer text...</p>
  </details>
</section>
```
Shared `name="blog-faq"` on every `<details>` gives true one-open-at-a-time accordion behavior natively (no JS, no plugin). Site-wide CSS added once to the theme (not per-article) handles the visual toggle styling.

**Why no FAQ plugin (e.g. Ultimate FAQs):** adds REST-endpoint/CPT/shortcode unknowns that need per-site verification, separates FAQ content from its parent article, and is more moving parts for the same visual result. Native accordion has fewer dependencies and won't break if a plugin updates.

**Schema:** FAQPage JSON-LD is explicitly a phase 2 decision, not part of the first rollout. Yoast (active on Aloha) only emits FAQ schema from its own FAQ block, not from headings or native accordion HTML — so schema has to be added deliberately later (small WP integration hooking into Yoast's schema graph, or a verified plugin with its own schema enabled) rather than assumed to "just work." Also worth noting: Google's FAQ rich results now show mostly for authoritative gov/health sites, so visible rich-result payoff for a business blog is uncertain even once schema is added — treat it as a "nice for machine understanding" item, not an urgent SEO lever.

**FAQ writing convention for docs (unchanged, already followed):** exact H2 "Frequently Asked Questions" → each question as H3 → everything until the next H3 or H2 is that answer (can span multiple paragraphs, lists, bold, links — not assumed to be a single `<p>`).

**Rollout safety pattern used:** duplicate the live Make scenario into a disabled test copy, run cleanup + accordion conversion against an existing draft, compare against source doc (headings/bold/lists/links/mobile/keyboard nav), only swap into the active scenario after it passes — don't edit the working scenario directly.

See also [[gbp-brain-body-split]] for the related principle of Claude not touching live automation/webhook configs directly.

**Known gaps found 2026-10-28 (SPIEDR Blog Draft Publisher, Make scenario 6209700):**
- The cleanup chain (modules 14–22) keeps Google Docs' `https://www.google.com/url?q=…&sa=D…` redirect wrappers and the empty `&nbsp;` anchors Docs splits links into. Every internal and source link on the two Sept 2026 SPIEDR posts shipped as a google.com redirect. Unwrapping has to be added to the chain (after body extraction, before attribute stripping).
- No Quick Answer handling: the doc's "Quick answer:" paragraph goes through as plain text. Clients with a styled Quick Answer block (SPIEDR) need a conversion step.
- **Per-client FAQ exception:** SPIEDR does not use the native `<details>` accordion. It needs Easy Accordion groups (schema comes from the plugin). The group's questions sit in non-REST post meta (`sp_eap_upload_options`), so neither Make nor the `wp-spiedr` MCP can create one today. See `clients/spiedr/CLIENT.md` section 8 publishing checklist.
