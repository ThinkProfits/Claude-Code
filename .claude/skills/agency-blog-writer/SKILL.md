---
name: agency-blog-writer
description: "Write blog posts for agency clients with brand-safe guardrails. Use whenever the user asks to 'write a blog for [client]', 'draft a blog for [client]', 'create the next blog for [client]', 'write a blog targeting [keyword] for [client]', or any blog writing task where a client name or project instructions document is present in the conversation, project files, or memory. Use this INSTEAD OF the generic seo-content-writer skill whenever the work is for a specific agency client, even if the user only says 'write a blog': if a client context exists, this skill applies. Enforces editor-required guardrails: location accuracy (no US references for Canadian clients and vice versa), no recommending competitors, scope adherence to the brief, no AI-voice tells, 1200-2000 word cap, required deliverables (blog plus GBP post plus social posts), and no schema in client-facing drafts. Tone-matches the client's existing blogs."
---

# Agency Blog Writer

A skill for writing blog posts for agency clients while enforcing brand consistency, location accuracy, scope adherence, and the agency's required deliverables. Adapted from the agency's Master SEO/GEO Content Creation Prompt v3.2 with editor-specific guardrails baked in.

## When to Use This Skill

- Writing blog posts for any agency client where project instructions are available (in project files, attached to the conversation, or pasted in context)
- Drafting client deliverables that include a blog plus GBP post and social posts
- Any blog work where the client has specific service areas, prohibited competitors, brand voice requirements, or a content brief

Use this INSTEAD OF the generic `seo-content-writer` skill when writing for a specific agency client. This skill enforces stricter guardrails: location accuracy, competitor avoidance, scope discipline, brand voice matching, and required ancillary deliverables.

Also applies to the earlier, batch stage of this same workflow: brainstorming a list of blog topic candidates for a client (e.g. "give me blog topics for [client]," "what should we blog about," "find content gaps") before any single post is assigned or drafted.

## Topic Ideation Phase (Before Presenting a Topic List)

When the ask is a batch of topic candidates rather than one already-assigned post, run a site-wide duplicate-content check before presenting anything. This is separate from Step 2's cannibalization check below, which is a single-keyword spot check done right before drafting one already-chosen post; a topic-ideation batch needs the equivalent check run once across the whole site, first.

1. **Pull what's already indexed.** Check the client's XML sitemap for a blog/post-specific sitemap (e.g. `/blog-sitemap.xml`, `/post-sitemap.xml` on WordPress; Wix and other builders often split sitemaps by content type — check `/sitemap.xml` first, it usually indexes the others). If no blog sitemap exists, check the general pages sitemap and the site's own blog/news listing page directly. Cross-check with Semrush: `resource_organic_unique` (organic research toolkit) on the domain, sorted by `keywords_count_desc`, surfaces every URL Google has indexed and is ranking for, catching pages a sitemap might miss or that aren't labeled "blog."
2. **Cross-reference proposed topics against that list**, watching for two distinct risks:
   - **Duplicate content:** an existing page already targets the same primary keyword or covers the same core topic.
   - **Cannibalization:** two proposed topics, or a proposed topic and an existing page, target keyword clusters close enough to compete with each other for the same query (e.g. several near-identical "how to start a podcast" long-tail variants).
3. **Drop or clearly differentiate** any topic that overlaps with existing content. When two proposed topics in the same list are the overlap risk (not an existing page), note the recommended fix in the deliverable, e.g. folding overlapping long-tail variants into one pillar post as FAQ subheadings rather than shipping them as separate posts.
4. **State the finding plainly**, even when the answer is "no existing content found, clear to proceed." Don't leave the check implicit or wait for the client/user to ask.

## How to Use

### Step 1: Confirm required inputs

Confirm or ask for the following. If client project instructions are available in project files, pull what you can from them before asking:

- **Client name**
- **Client website URL**
- **Country** (US, Canada, etc.)
- **Client's exact service areas** (e.g., "Kelowna, West Kelowna, Vernon, Penticton, Lake Country, BC", never just "BC" or "the Okanagan")
- **Topic / title from content calendar**
- **Type of post** (how-to, listicle, comparison, explainer, seasonal)
- **Primary focus keyword**
- **Supporting keywords** (8–15)
- **Word count target** (default 1,200–2,000 words = 3–5 pages)
- **2–3 existing blogs from the client's site (URLs) to study for tone**
- **4–7 internal pages from the client's site available for linking**
- **Required deliverables** (default: blog + GBP post + social posts)
- **Client project instructions** (attached or pasted)

If critical inputs are missing (topic, primary keyword, country/service area), ask before proceeding. Do not invent values.

### Step 2: Pre-write research

Before writing a single word:

1. Read the client project instructions in full. Note: service list, what the client does NOT do, tone preferences, named competitors to avoid, differentiators, slogan, active promotions, prohibited CTA language.
2. Visit the client's website and read 2–3 of their existing blog posts. Note sentence length, paragraph length, voice (formal vs. conversational), use of contractions, CTA style, how they refer to themselves.
3. Search the primary keyword on Google. Review the top 3–5 ranking pages for depth and content gaps.
4. **Cannibalization check:** search the client's site for the primary keyword (`site:clientdomain.com [keyword]`). If a similar post exists, flag it before writing. Options are consolidate, write a clearly differentiated angle, or update the existing post.
5. Identify 3–5 internal linking opportunities from the URLs provided. Note specific anchor text and where each link will sit.
6. Verify every statistic, rebate amount, regulation reference, and program detail with a primary source. If you cannot confirm within 2 minutes, omit. Never fabricate.

## Hard Rules: Non-Negotiable

These override every other instruction. Violating any of them means the draft will be rejected by the editor.

### Location accuracy

- Every regulatory reference, rebate program, statistic, code, and example must apply to the client's actual country and service area.
- For Canadian clients: reference relevant Canadian/provincial bodies only (FortisBC, CleanBC, NRCan, Health Canada, provincial licensing boards). Verify the program is real and current. Do NOT reference US federal programs (DOE, EPA, Inflation Reduction Act, IRS tax credits), US enforcement bodies, or US-specific statistics.
- For US clients: do not reference Canadian programs. Same rule in reverse.
- Use the client's actual service-area names. Do not invent neighbourhoods or claim coverage in cities not on the project instructions.

### Competitor handling

- Never name, list, or recommend the client's competitors as good options, premium-tier, top-rated, or in any positive framing.
- Never write content that helps a reader pick a competitor, including "how to choose the best [X] in [city]" if it leads to recommending other companies. Reframe to "what to look for in a [service] company," using the client's own credentials as the worked example.
- Do not link out to competitor websites.
- If a topic structurally requires brand or vendor comparison and one happens to be a competitor, name them only neutrally if absolutely required and never with a positive recommendation. Default to omitting.

### Scope adherence

- Deliver exactly what the brief asked for. If the brief says "multi-brand listicle of the quietest ACs," include 4+ brands with comparable depth, not a single-brand deep dive. If the brief says "how-to," write a how-to. If the brief says "comparison," write a comparison.
- State the post type and what it will cover in one sentence at the very top of the draft (above the H1) so the editor can verify scope at a glance. Note that this line is for editor review and should be removed before publishing.

### Tone: no AI-voice tells

The following are immediate red flags. Avoid all of them:

- Anthropomorphism of inanimate objects ("the gasket has given up on life," "the pipes are tired," "the furnace is sulking")
- Abrupt one-word or one-line standalone sentences for dramatic effect ("Hold on." "Wait." "But here's the thing.")
- "It's not just X, it's Y" constructions
- Stock openers: "In today's fast-paced world," "Let's dive in," "Buckle up," "When it comes to," "We've all been there"
- Filler transitions used more than once per post: "That said," "All in all," "At the end of the day"
- Em dashes (—). NEVER use them anywhere in client blog content. The em dash is one of the strongest reader signals of AI-written content, and that impression alone is disqualifying for agency client work. Replace em dashes with commas, colons, parentheses, or by splitting the sentence in two. Regular hyphens (-) in compound words (high-efficiency, cold-climate) and as dash markers in bullet lists are fine; en dashes and em dashes are not.
- Three-item parallel constructions stacked on each other ("clean, fast, and reliable"; "trusted, experienced, and local") more than once per post
- Bullet fragments without context (see Depth Rules)

Before drafting, read the 2–3 reference blogs the user provided. Match sentence rhythm, paragraph length, formality level, contractions, how the client refers to itself, and CTA style. The reader should not be able to tell this post was written by a different author than the others on the site.

### No schema in client-facing drafts

- Do NOT include JSON-LD, structured data code blocks, or schema markup in the draft.
- Schema is implementation, not deliverable. If FAQPage, Article, or HowTo schema would help, add a one-line note in the implementation section at the bottom.

### Length discipline

- Default cap: 1,200–2,000 words (3–5 pages). Do not exceed unless the brief explicitly authorizes more.
- Pad-detection test: if a section exists only to hit a word count, cut it.

## Blog Anatomy

| Element | Requirement |
|---|---|
| Title (H1) | One per post. Exact match to title tag. Includes primary keyword. |
| Quick Answer box | Exactly one per post, placed directly after the H1 and before the introduction. 2–3 sentences giving a direct answer to the post's core question, in a visually distinct callout (blockquote). Must include the primary keyword. This is the ONLY answer box in the post; do not repeat the format in any section. |
| Introduction | 100–150 words. State what the post covers and why it matters in the client's service area. Primary keyword in the first 100 words. Do not restate the Quick Answer box verbatim; the intro expands on it. |
| H2 sections | 4–8 per post. Each = a major subtopic. Lead each with a one-sentence summary, then expand. |
| H3 subsections | Optional. 2–4 per H2 when used. Never skip from H2 to H4. |
| Body paragraphs | 3–5 sentences each. Max 6. |
| Bullets | 1–2 full sentences with context. Never bare fragments (exception: simple reference lists like county names or payment methods). |
| Conclusion / CTA | 100–150 words. Summarize key takeaways with a clear, client-specific next step. Never use "free estimate" unless the client offers one. |
| FAQ block | Recommended. 3–5 Q&As with specific answers (numbers, timeframes, named programs). |

### Title tag

- 50–60 characters (target 55)
- Primary keyword first; never start with brand name
- Include city and province/state on local-SEO posts
- Brand at the end with `|` (e.g. `Topic Keyword in City, Province | Brand`)
- Formula: `[Topic Keyword] in [City, Province] | [Brand]`

### Meta description

- 150–160 characters
- Front-load info, since mobile clips around 120 characters
- Include the primary keyword and a soft CTA
- Formula: `[What you do] + [for whom/where] + [key benefit] + [call to action]`

### URL slug

- 3–5 words, under 60 characters
- Lowercase, hyphenated, no stop words ("a," "the," "in" unless part of the keyword), no dates, no special characters

## Depth Rules

These override default formatting tendencies. Apply them to every bulleted list, numbered process, and differentiator section.

### Bullets must be 1–2 sentences

Each bullet must explain why the point matters and how it affects the reader. Test: would a reader respond "okay, but what does that actually mean for me?" If yes, expand it.

- BAD: "Regular maintenance"
- GOOD: "Regular maintenance: a yearly furnace tune-up clears dust from the burners and verifies the heat exchanger is intact, which prevents the small efficiency losses that compound into larger repair bills."

Exception: simple reference lists where items need no explanation (counties served, payment methods, brand names).

### Process steps must be 2–3 sentences

Every numbered step must describe what happens, what the customer's role is, and what the business does. The reader should be able to picture the interaction.

### Differentiator claims need evidence

If the post says the client is "fast" or "trusted" or "local experts," back it with a specific number, credential, or mechanism. No bare marketing claims.

### Anti-generic test

Read the opening three paragraphs. Could a competitor paste them onto their own site with only a name change? If yes, rewrite with specifics: the client's actual process, named credentials, real service area, or a specific local program.

## Local SEO Without Stuffing

- Mention service areas 1–2 times in the body, not in every section.
- Do not create "Serving [city list]" sections that just list place names.
- Demonstrate local knowledge through: relevant local regulations, regional climate or geography, area-specific programs, community context, or known regional issues.
- For local-SEO posts, include the client's NAP (name, address, phone) at least once. Must match the Google Business Profile exactly.
- Include "City, Province" naturally in the H1 and within the first 100 words for local posts.

## Linking

### Internal links

| Word count | Minimum | Target |
|---|---|---|
| Under 800 | 2 | 2–3 |
| 800–1,199 | 3 | 3–5 |
| 1,200–1,500 | 5 | 5–7 |
| 1,500–3,000 | 5 | 5–7 |

- Descriptive, keyword-relevant anchor text. Never "click here" or "read more"
- At least one internal link in the first half of the post
- Don't link to the same page more than twice. A single distinct destination counts once toward the minimum even if linked twice, so reach the minimum with distinct pages.
- Only link where it genuinely helps the reader. The minimum is a floor, not a licence to stuff: if a post can't reach 5 genuinely useful internal links, that's a signal the client needs more linkable pages, not that you should force weak links. Flag it in implementation notes rather than padding.
- Since most client posts run 1,200+ words, plan internal linking up front: identify 5+ relevant destination pages (service pages, related blogs) from the sitemap during pre-write research, before drafting.

### External links

Target: 1–2 per post, regardless of length. Use the second only when a second authoritative source genuinely strengthens the post (e.g. a statistic and a separate regulatory reference). One strong, relevant external link beats several weak ones.

- Link only to authoritative sources: .gov, .edu, established industry bodies, manufacturer documentation, peer-reviewed research, recognized publications
- Cite every statistic with a source link (if a post has more than 2 statistics needing citation, prioritise the load-bearing ones; don't let citations push the external count well past 2)
- Open external links in a new tab (`target="_blank"` with `rel="noopener noreferrer"`)
- Never link to competitors

## Images

- 1 image per 400–500 words (a 1,500-word blog gets 3–4 images)
- File names: hyphenated, descriptive, keyword-inclusive (e.g., `furnace-repair-kelowna.jpg`)
- Alt text: under 125 characters, one clear sentence describing the image. Include keyword or location naturally if it fits. Never stuff multiple keywords.
- Provide image **placement suggestions** in the draft (description + alt text + suggested filename), not the actual images.

## FAQ Quality

- Only include FAQs if they add value beyond what's in the body
- 3–5 questions; each answer 2–4 sentences with at least one specific detail (number, timeframe, named program, concrete example)
- Never write "costs vary" or "it depends" without context
- Format compatible with FAQPage schema: clean Q + clean A, no nested formatting

## Required Deliverables

The draft must include all of the following, in this order:

1. **Scope confirmation line**: one sentence stating the post type and what it covers (above the H1, for editor review only; note that it should be removed before publishing)
2. **Title tag** with character count
3. **Meta description** with character count
4. **URL slug**
5. **Full blog post**: H1 through CTA, FAQ if included, with image placement notes
6. **GBP post**: 2–3 sentences, 1,500 characters max, includes a CTA. Tied to blog topic. Primary keyword used naturally.
7. **Social posts**: at least one for each platform the client uses (default: Facebook + Instagram). 1–3 sentences each. Includes a placeholder for the blog URL, at least one hashtag, no emojis unless the client's existing posts use them.
8. **Implementation notes**: schema recommendations (one line per type), publish-date note, any flagged cannibalization or duplicate-content issues, any unverifiable claims removed during research.

## Self-Check Before Outputting

Run this checklist on the draft. If anything fails, fix it before outputting.

**Location and client fit**
- [ ] Every regulatory body, rebate, statistic, and example is relevant to the client's actual country and service area
- [ ] Service areas mentioned match the client project instructions exactly
- [ ] No services mentioned that the client does not offer
- [ ] No CTA language references a promotion the client doesn't offer

**Competitors and scope**
- [ ] No competitors named, listed, or recommended
- [ ] No external links to competitor websites
- [ ] The post matches the brief's scope

**Tone and voice**
- [ ] No anthropomorphism, AI-voice tells, or filler phrases
- [ ] Matches rhythm and voice of the 2–3 reference blogs
- [ ] Zero em dashes (—) anywhere in the post (commas/colons/parentheses/split sentences used instead)

**Structure and depth**
- [ ] Within 1,200–2,000 words (unless authorized)
- [ ] Intro 100–150 words with primary keyword in first 100
- [ ] 4–8 H2s, body paragraphs 3–5 sentences each
- [ ] Every bullet has 1–2 sentences of context (or is a justified simple reference list)
- [ ] Process steps each have 2–3 sentences
- [ ] Anti-generic test passed on opening 3 paragraphs

**SEO and AEO**
- [ ] Title tag 50–60 chars, primary keyword first
- [ ] Meta description 150–160 chars
- [ ] URL slug clean
- [ ] Primary keyword used 5–7 times max
- [ ] Internal links meet the minimum for word count (5 for 1,200+ word posts); external links are 1–2
- [ ] Every statistic has a source link
- [ ] Intro answers the post's main question in one sentence (AEO)
- [ ] Cannibalization check completed

**Deliverables**
- [ ] Blog + GBP post + social posts all included
- [ ] No JSON-LD or schema in the draft
- [ ] Implementation notes section at the bottom

## After Drafting: Recommend Review

After producing the draft, remind the user that the editor's process requires running a separate review pass in a fresh Claude conversation. Suggest:

> "Once you're happy with this draft, open a fresh chat and run the **blog-review-prompt** on it. The fresh-context review catches blind spots that an in-thread review misses. Repeat the review until it returns no significant issues, then do your own human pass before sending to the editor."

## Related Skills

- `seo-content-writer`: generic SEO content writing (use for non-agency or non-client work)
- `client-project-instructions`: generates client project instructions docs (run this first if a client doesn't have one yet)
- `content-refresher`: for updating existing blog posts rather than writing new ones
- `internal-linking-optimizer`: deeper internal linking analysis if needed
