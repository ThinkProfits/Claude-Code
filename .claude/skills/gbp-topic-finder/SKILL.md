---
name: gbp-topic-finder
description: "Determine what a client's next Google Business Profile (GBP) post should be about, before any copy gets written. Use whenever the user asks 'what should we post to [client]'s GBP next', 'find the next GBP post topic for [client]', 'come up with GBP post topics', or when running the recurring twice-weekly GBP posting routine for any of ThinkProfits' connected client profiles and no topic has been chosen yet. Works through a fixed priority order (recent blog, real offers, review-mined topics, core services rotation, real events, keyword-gap research, seasonal relevance), checks the shared topic-tracking doc to avoid repeats, and hands off a chosen topic + real source + target keyword to gbp-post-writer for drafting. Does not write the post itself."
---

# GBP Topic Finder

Decides what a client's next GBP post should cover. This is the research/decision step only — once a topic is chosen here, hand it to `gbp-post-writer` to actually draft the post.

## When to Use

- Starting the routine for a client and no topic has been picked yet for this cycle
- Checking whether a client has enough real material to sustain the target 2x/week cadence
- Auditing whether recent topics have been too repetitive for a client

Not for: writing the actual post copy (`gbp-post-writer`), technical GBP profile data pulls (`gbp-audit` MCP), keyword volume/difficulty lookups on their own (Semrush MCP directly).

## Required Inputs

- **Client** and its `location_key`
- Access to (or a recent pull of): the client's blog/site, its live GBP listing (reviews, services, active offers/buttons), and the shared topic-tracking doc

## Priority Order

Work down this list. Use the **first** source that has real, current material — never fabricate a topic, offer, or detail to fill a gap, and never skip ahead to a lower-priority source just because it's easier.

| # | Source | What to check | Output if used |
|---|---|---|---|
| 1 | Recent blog post | Client's blog/news page for anything not yet turned into a GBP post | Blog title + URL as the topic and CTA destination |
| 2 | Real, active offer/promotion | Site banners, current promos, rebate programs actually running now | Offer details + confirmed start/end dates → flag as post type `OFFER` |
| 3 | Review-mined topics | The client's own Google Maps review tags/mentions — pick the highest-count real topic not recently used | Topic + real mention count as the demand signal |
| 4 | Core services/categories rotation | The GBP's own services list — rotate to a service not covered recently | Service name, straight from the profile |
| 5 | Real events/recognition | Awards, milestones, community involvement — genuinely true, not invented | Event/award detail + date |
| 6 | Semrush keyword-gap topic | Real search term with volume the client isn't ranking well for, still needs a genuine informational angle | Keyword + confirmed volume/intent from Semrush, not assumed |
| 7 | Seasonal relevance | Genuine seasonal service timing tied to the actual season/climate, not manufactured urgency | Seasonal angle, generic enough to be true |

**Regulated clients (legal, medical, financial):** only sources 3, 4, 6, or 7 apply, framed purely educationally. Skip 1 and 2 if either would imply a case outcome or specific result.

## Rotation Rule

Check the shared topic-tracking doc before picking. If the same topic (or same source-type) was used in the last 2-3 cycles for this client, move to the next priority source instead, even if the higher one is technically still available — variety matters more than always using source #1.

After choosing, log the topic + source + date to the shared tracking doc so the next run doesn't repeat it.

## Target Keyword + Search Intent

Every chosen topic needs a real target keyword and its search intent (informational, commercial/near-transactional, navigational) before handing off. Confirm via Semrush keyword research for that client's city + service — don't guess volume or intent. If Semrush data isn't available in the moment, hand off with keyword + intent stated as "logically derived, not yet Semrush-confirmed" rather than presenting it as verified.

## Handoff Output

Report, ready for `gbp-post-writer`:

- **Client + `location_key`**
- **Chosen topic** + which priority source it came from and why
- **Source material** (URL, review count, offer terms/dates, service name — whatever backs it)
- **Target keyword + search intent**
- **Suggested post type** (Standard/Offer/Event) based on the source

## Common Mistakes

- Defaulting to source #1 or #7 because they're easiest, skipping past a better-fitting real source in between.
- Picking a topic already used recently because the tracking doc wasn't checked.
- Presenting a guessed keyword/intent as if it were Semrush-confirmed.
- Choosing an Offer or Event topic without confirmed real dates/terms.
- For regulated clients, picking a topic that implies a specific case outcome or guaranteed result.

## Related Skills

- `gbp-post-writer`: takes the topic this skill outputs and drafts the actual post
- `agency-blog-writer`: if the chosen topic reveals a content gap worth a full blog post instead of just a GBP post
