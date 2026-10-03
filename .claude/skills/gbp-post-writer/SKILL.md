---
name: gbp-post-writer
description: "Write the actual copy for a Google Business Profile (GBP) post for ThinkProfits agency clients, once a topic has already been chosen (see gbp-topic-finder). Use whenever the user asks to 'write a GBP post for [client]', 'draft a Google Business Profile post', 'turn this topic into a GBP post', or when a topic has come out of the GBP posting routine for any of the 9 connected client profiles and needs to become sendable copy for the Make.com webhook pipeline. Also use to expand a blog's required GBP post deliverable (see agency-blog-writer) from a short 2-3 sentence summary into a fully-formed standalone post. Enforces GBP-specific constraints: front-loaded copy for the ~100-character truncation point, CTA button selection matched to what the profile actually supports, real (non-stock) image sourcing, and correct post-type selection (Standard/Offer/Event)."
---

# GBP Post Writer

Turns an already-chosen topic into actual Google Business Profile post copy, ready for the Make.com webhook pipeline (one `location_key` per client, routed to that client's real GBP location). This skill does NOT decide what to post about — run `gbp-topic-finder` first if no topic has been chosen yet. Companion to `agency-blog-writer`, which only asks for a short 2-3 sentence GBP post as one of its deliverables — use this skill instead whenever the post needs to carry real weight on its own (no blog behind it) or was sourced from `gbp-topic-finder`.

## When to Use

- Drafting the actual post copy (title, summary, CTA, URL, post type) from a topic that's already been chosen
- Reviewing/fixing a draft post before it goes live on a real client profile

Not for: deciding what topic to post about (`gbp-topic-finder`), writing the blog itself (`agency-blog-writer`, `seo-content-writer`), technical GBP profile edits like categories/services/hours (`gbp-audit` MCP tools), or citation/reputation work (BrightLocal).

## Step 1: Confirm required inputs

Expect these to already be settled by `gbp-topic-finder` — if any are missing, go run that first rather than guessing here:

- **Client** and its `location_key` (from the shared location-key reference doc — never guess or reuse another client's key)
- **Chosen topic** + real source material backing it
- **Target keyword + search intent** for this specific post
- **Suggested post type** (Standard/Offer/Event)

Still need to confirm here, since these are drafting-specific, not topic-specific:

- **CTA type** the profile actually supports (check if "Book Online" or another action button is active on the live listing before defaulting to Learn More)
- **Real image URL** — a live photo already hosted on the client's own site (gallery/portfolio/service page), not stock, not a downloaded local copy
- **Destination URL** for the CTA (see routing rule below)

**Regulated clients (legal, medical, financial):** keep copy purely educational. Never write anything implying a case outcome, guaranteed result, or specific advice. When in doubt, cut the claim.

## Post Anatomy

| Field | Rule |
|---|---|
| Title | Short, front-loaded — GBP truncates at roughly the first 75-100 characters before "Read more," so the value has to land before that cutoff. |
| Summary/body | Up to 1,500 characters max, but treat that as a ceiling, not a target. Specific, local, action-oriented beats generic. State what's happening, why it matters, what to do next. |
| CTA type | One of Google's actual supported values: Learn More, Book, Order, Shop, Sign Up, Call. (Note: "Get Offer" is NOT a real Google actionType despite being commonly assumed — a post using it will fail validation. An `OFFER` post_type with real terms/dates is still valid; just pick a real CTA action like Learn More or Book for it.) Match to the business (see table below), and to whatever action button the live profile actually supports. |
| CTA URL | Blog source → the blog URL. No blog / general topic → the closest relevant service page, or the homepage if nothing closer fits. Never a guessed or unverified URL. |
| Image | Real photo, live URL from the client's own site. Recommended 720×540 (4:3), 400×300 minimum, JPG/PNG, under 5MB. Never skip the image — text-only posts underperform. |
| Post type | `STANDARD` (general update), `OFFER` (needs terms + start/end dates), `EVENT` (needs event dates). Match to what's actually true; don't force an Offer or Event that isn't real. |
| Keyword | Include the target keyword naturally, once. Google indexes post content, but stuffing reads as spam and helps nothing. |

### CTA type by business type (starting point, not a rule)

| Business type | Likely best CTA |
|---|---|
| Trade/service business (plumbing, HVAC, towing, septic) | Call Now, or Learn More if no urgency |
| Retail (sporting goods, product-based) | Learn More, or Shop/Order Online if the profile supports it |
| Professional services (legal, financial) | Learn More — avoid Call Now framing that could read as soliciting urgent legal need |
| Any profile with an active "Book Online" button | Book |
| 24-hour / emergency service | Call Now |

## Common Mistakes

- Using a generic Learn More when the profile already has a stronger native action button (Book, Order Online) configured — check the live listing first.
- Reusing the exact same photo across consecutive posts for the same client — rotate through the client's real photo set.
- Writing an Offer post without real terms/dates, or an Event post for something that isn't a scheduled event — downgrade to Standard instead.
- Front-loading the post with a generic opener ("We're excited to announce...") instead of the actual value, wasting the ~100 characters before truncation.
- Linking to a guessed URL instead of confirming the real closest-match page.
- For regulated clients, implying a specific outcome, result, or guarantee — reframe to purely educational.
- Drafting without a topic from `gbp-topic-finder` first — this skill doesn't decide what to post about.

## Self-Check Before Sending

- [ ] `location_key` confirmed against the shared reference doc, not guessed
- [ ] Topic and target keyword came from `gbp-topic-finder`, not invented here
- [ ] CTA type matches what the live profile actually supports
- [ ] CTA URL is a real, confirmed page (blog, service page, or homepage — never guessed)
- [ ] Image is a real photo from the client's own site, not stock, not reused from the last post
- [ ] Post type matches reality (no fabricated Offer/Event)
- [ ] Regulated-client copy (legal/medical/financial) is factual only, no outcome or result implied
- [ ] Copy front-loads the value within the first ~100 characters

## Related Skills

- `gbp-topic-finder`: run this FIRST if no topic has been chosen yet — decides what to post about, this skill only writes it
- `agency-blog-writer`: use when the deliverable is a full blog post (its own short GBP post requirement is a summary only — use this skill instead when the GBP post needs to stand on its own)
- `seo-content-writer`: generic SEO content, non-agency work
