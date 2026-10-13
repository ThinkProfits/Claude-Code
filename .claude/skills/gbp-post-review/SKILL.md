---
name: gbp-post-review
description: Fresh-context review of a finished Google Business Profile post draft before approval. Use when asked to 'review this GBP post', 'check the GBP drafts', or as the review step after gbp-post-writer (the Saturday GBP routine runs it twice per draft). Returns PASS or a numbered list of required fixes tied to rubric codes.
---

# GBP post review

GBP equivalent of the blog review pass: a reviewer that did not write the draft checks it against a fixed rubric. Run it in a fresh context (a new chat or a subagent) and give it only the draft fields, not the writer's research notes.

**Input:** location_key, date, title, summary, actionType, url + where it was confirmed, imageUrl + where it came from, post type, target keyword + volume source.

**Output:** either `PASS`, or a numbered list of required fixes, each starting with its rubric code (e.g. `H2: image is .webp, swap for a JPG/PNG from the Approved Queue log`). Be specific. Do not rewrite the post yourself.

**Approval rule used by the Saturday routine:** two review passes. Any hard fail (H*) still true after pass 2 means HELD for human review: no :+1:, no Codex handoff. Q* items must be fixed but don't block approval once fixed.

### Reviewer rubric
Hard fails (any one of these means the draft cannot be auto-approved):
- H1. `url` is not confirmed (not from Semrush indexed pages, web search results, or the Approved Queue log).
- H2. Image is missing ("NEEDS PHOTO"), not confirmed real for this client, or is .webp / not JPG or PNG.
- H3. actionType is not exactly one of LEARN_MORE, BOOK, ORDER, SHOP, SIGN_UP, CALL.
- H4. A named offer, promo, price, program, award or event that cannot be verified as real and current.
- H5. Guarantee or outcome language ("guaranteed", "#1", "best results", promised rankings or savings). For Munro & Crawford (law firm): anything implying a case outcome, legal advice, or a topic source other than review-mined / core service / keyword-gap / seasonal.
- H6. Wrong geography (US references for Canadian clients, wrong city/service area for the location).
- H7. Summary over 1,500 characters, or a date-specific line that will be stale on the post date.
- H8. Same topic or source-type already used for this client in the last ~3 weeks of the channel.
Quality fixes (must be fixed, but do not block approval once fixed):
- Q1. The first ~100 characters don't carry the main point and the keyword/service + city.
- Q2. AI-voice tells: em dashes, "In today's...", "Look no further", "elevate", "seamless", stacked adjectives, generic filler.
- Q3. Not Canadian English spelling (colour, centre, neighbour, etc.).
- Q4. Tone doesn't match the client (professional, sharp, human; no sarcasm, no inside jokes).
- Q5. CTA wording doesn't match the actionType, or the post type (standard/offer/event) is wrong for the content.
- Q6. Title is vague or doesn't match the body.
