# Internal notes: 09 value-based-bidding-service-businesses

**Scope:** Decision-focused explainer (PPC) on value-based bidding for lead-gen service businesses: how Maximize Conversion Value / Target ROAS differ from count-based bidding, Google's documented prerequisites, three ways to set lead values (static, form answers, offline CRM), when it fits vs when to stay on Target CPA, and our rollout sequence. Fills backfill row #9, week of Nov 17, 2026.

**Word count:** ~1,780 (post body incl. H1, quick answer, table, FAQ, CTA). Primary keyword used 7 times.

## Sources checked (2026-11-25)

- https://support.google.com/google-ads/answer/15099424 (About Smart Bidding using value-based bidding for Search and Shopping): confirmed the two strategies; June 2026 label change ("Maximize conversion value with a Target ROAS" shown as "Target ROAS", bidding unchanged); 15 conversions in last 30 days for Target ROAS; 2+ distinct values, proxy values such as lead score allowed; conversion delay ideally under 7 days; one funnel stage; ramp-up of 3 weeks or 1 to 2 conversion cycles (whichever longer); initial ROAS target from historical 30-day ROAS; daily uploads optimal. **Linked in post.**
- https://support.google.com/google-ads/answer/13489421 (Best practices for generating high-quality leads): confirmed Target CPA recommended for qualified/converted leads when distinct values can't be assigned; enhanced conversions for leads recommended over offline conversion import (GCLID); upload ideally daily; 15 conversions in 30 days at account level; conversion value rules by location, device, audience. **Linked in post.**
- https://support.google.com/google-ads/answer/14792795 (Value-based Bidding Best Practices): confirmed avoid zero-value conversions; daily uploads; lead form answers as a way to differentiate values; keep budgets unconstrained with ROAS targets. Not linked (external cap of 2). Note: this page says 4 weeks or 3 conversion cycles of upload history, while 15099424 says 3 weeks or 1 to 2 cycles. Post quotes the 15099424 figure only, since that is the linked source.
- Voice references read: /digital-news/local-business-entity-consistency-ai-search/ and /digital-news/canonical-url-qa-lovable-headless-launches/.

## Claims cut or softened

- Dropped "Maximize Conversion Value has no minimum conversion requirement" (third-party claim only, not confirmed on Google Help).
- Did not state Display or Performance Max thresholds (vary by campaign type; out of scope).
- Proxy value example ($3,000 job, 1 in 10 close) is labelled in-copy as an illustration, not a benchmark. No client results or stats used.
- No promise of lift; "Results vary... we do not promise a lift" kept deliberately.
- Product names keep Google's US spelling ("Maximize Conversion Value") because they are UI labels; all other copy is Canadian spelling.

## Keyword data (google-ads-keywords MCP, Keyword Planner, Canada, Nov 2025 to Oct 2026)

| Keyword | Avg monthly searches (CA) |
|---|---|
| value based bidding (close variant: value-based bidding) | 30 |
| troas | 140 |
| maximize conversion value | 20 |
| target roas | 20 |
| value based bidding google ads | 10 |
| conversion value rules | 10 |
| offline conversion import | 10 |
| google ads conversion value | 10 |
| enhanced conversions for leads | 10 |
| maximize conversion value vs maximize conversions | 10 |
| target roas google ads | 10 |
| value based bidding lead generation | 0 (no data) |

Low volume, practitioner audience; value is topical authority for /ppc-advertising/ rather than traffic.

**PAA-style questions folded into the FAQ** (from web search of lead-gen VBB queries): can VBB work for lead gen without ecommerce; conversions needed for Target ROAS; Maximize Conversion Value vs Maximize Conversions; offline conversions first; how long to judge.

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml (301 URLs) for bid/value/roas/conversion/ads slugs. No post targets value-based bidding. Closest: `target-cpa-vs-business-cpa-google-ads` (Target CPA; mentions tROAS once) and `google-ads-target-overperformance-audit` (Aug 2026 rollout audit; has a tROAS section but no VBB setup or Maximize Conversion Value). Distinct angle; this post links to the Target CPA post as the step before. Clear to proceed.

## Internal links used (7 distinct)

/digital-news/target-cpa-vs-business-cpa-google-ads/ (confirmed in sitemap), /digital-news/google-ads-lead-quality-loop/, /digital-news/budget-limited-vs-demand-limited-google-ads/, /digital-marketing-reporting/, /digital-news/weekly-google-ads-change-log/, /ppc-advertising/, /contact/.

## Implementation

- Hero: `/images/blog/wp/tp-branded-placeholder.jpg`, alt "Value-based bidding for service businesses in Google Ads". Branded placeholder only, no AI imagery.
- No JSON-LD in draft; Lovable layout outputs Article, FAQPage and Breadcrumb from the FAQ block.
- Publish date: 2026-11-17 (backfill week). Category: PPC.
- External links: open in new tab with rel="noopener noreferrer".
- Reviewer to confirm: the June 2026 "Target ROAS" relabel matches what the ThinkProfits ad accounts show today.

## GBP post (ThinkProfits Vancouver)

Not every lead is worth the same, so should your Google Ads bid as if they are? Value-based bidding lets Smart Bidding favour the enquiries that tend to become bigger jobs, but only when your CRM can send back honest values and you have enough conversions for it to learn. Our new guide covers Google's prerequisites, how to set lead values, and when Target CPA is still the smarter choice. Read it on our blog. CTA button: Learn more → [blog URL]

## LinkedIn

Value-based bidding is one of those Google Ads settings that looks like an obvious upgrade for service businesses. Sometimes it is. Sometimes it teaches Smart Bidding the wrong lesson with very confident numbers. We wrote up what Google's documentation asks for before you switch (two or more distinct values, 15 conversions in 30 days for Target ROAS, short conversion delays) and how we roll it out on one campaign before touching the rest. [blog URL] #GoogleAds #PPC

## Facebook

Does your Google Ads account treat a small repair enquiry and a major project request as the same lead? Value-based bidding can fix that, if your data is ready. Here is how to tell, and what to do if it is not. [blog URL] #GoogleAds

## Review 2026-11-25

- Links: all internal links 200; converted absolute thinkprofits.com links to root-relative. Both Google links 200.
- Re-verified 15099424 (15 conversions/30 days for tROAS, 2+ values, <7-day delay, single stage, 3 weeks or 1-2 cycles ramp-up, historical ROAS benchmark, June 2026 relabel, proxy values), 13489421 (tCPA when distinct values can't be assigned, ECL over GCLID import, daily uploads) and 14792795 (avoid zero-value conversions, lead form answers, unconstrained budgets).
- Fixed a conflict with Google's guidance: "spam should carry no value at all" now says exclude junk rather than send it as $0, since Google advises against zero-value conversions.
- Overlap with 04: rollout step 1 no longer re-describes the primary/duplicate audit (that is 04's checklist); it now picks the funnel stage. The "fix duplicates first" line links to 04. No overlap with 06 found. **04 must be live first** (currently unpublished, 301s).
- Voice: removed "not a toggle you flip on a Friday afternoon" (not-X-but-Y construction) and the repeated "confident" phrasing.
- Body now ~1,820 words (within 1,850).
