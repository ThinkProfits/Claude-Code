# Internal notes: 04 primary-vs-secondary-conversions-google-ads

**Scope:** Explainer plus checklist covering what primary vs secondary conversion actions do to bidding and reporting in Google Ads, common lead-gen mistakes, and a governance checklist. Fills backfill row #4 (week of Oct 13, 2026). Category: PPC.

## Sources checked (all fetched 2026-11-25)

- https://support.google.com/google-ads/answer/11461796 (About primary and secondary conversion actions): primary reported in "Conversions" and used for bidding when the campaign optimises toward its goal; secondary is observation only, in "All conv."; exception for custom goals; GA-created conversions secondary by default and only promotable to primary in Google Ads; give the system 1 to 2 conversion cycles to adapt; path Goals > Conversions > Summary > Edit goal. **Linked in post.**
- https://support.google.com/google-ads/answer/3438531 (About conversion counting options): "One" = one conversion per ad click, suits leads; "Every" suits sales; changes apply to future conversions only; "Every" is default for website actions. **Linked in post.**
- https://support.google.com/google-ads/answer/10995103 (About conversion goals): actions grouped into goals by category (e.g. "Submit lead forms", "Contacts"); account-default goals selected for new campaigns; campaign-specific goals; custom goals can mix primary and secondary and are "not recommended in most cases".
- https://support.google.com/google-ads/answer/6095882 (Measure calls from ads): call conversions use a minimum call length setting. Post mentions the setting only, no default number.

## Claims cut or softened

- Default 60-second call length: only found on an older Google page, not stated in the post.
- "Learning" status lasting up to 7 days after changes: seen in a fetch summary, not used (kept the 1 to 2 conversion cycles line, which is on the primary/secondary page).
- AI-qualified call leads (newer Google feature, answer 16913326): not covered, out of scope and not verified in depth.
- No statistics used, so no stat citations needed.

## Keyword data (google-ads-keywords MCP, Keyword Planner, Canada, 2026-11-25)

| Keyword | Avg monthly searches (CA) |
|---|---|
| google ads conversion tracking | 90 |
| google ads primary vs secondary conversions | 10 |
| secondary conversion google ads | 10 |
| primary and secondary conversions | 10 |
| google ads conversion actions | 10 |
| conversion goals google ads | 10 |
| include in conversions google ads | 10 |
| google ads conversion settings | 10 |
| primary vs secondary conversions | 0 (no data) |
| primary conversion google ads | 0 (no data) |

Low volume across the cluster in Canada. Treat this as a practitioner/trust post supporting /ppc-advertising/, not a traffic play. Kept the brief's primary keyword; the closest measurable variant is "google ads primary vs secondary conversions".

PAA-style questions found via search and folded into FAQ: do secondary conversions affect Smart Bidding; why All conv. is higher than Conversions; One vs Every for leads; can GA4 key events be primary; how long to wait after changes.

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml (17 Google Ads / conversion URLs). No post targets primary vs secondary conversions. Partial overlap:
- `google-ads-lead-quality-loop` has an FAQ "Which conversion actions should be primary?" and a stage table marking inquiry as secondary. This post links to it and defers CRM/offline import detail to it.
- `google-ads-account-handoff-checklist` mentions noting primary actions and test-firing them. Linked from step 6.
No conflict; this post owns the settings mechanics and governance.

## Image note

Hero uses the site placeholder `/images/blog/wp/tp-branded-placeholder.jpg`. If replaced later, use a real (anonymised) screenshot of a Goals > Summary page, never AI imagery, and blur account IDs.

## GBP post (ThinkProfits Vancouver)

Is your Google Ads account bidding toward real leads or toward page views? Primary vs secondary conversions decide what Smart Bidding chases, and duplicate form tracking can make one inquiry look like two. Our new checklist walks through the settings to review before your next bid strategy change. Read the guide, or book a free 30-minute consultation with our Vancouver team.
CTA button: Learn more > [blog URL]

## LinkedIn

A cost per lead that looks great in Google Ads but does not match your intake numbers usually has a boring cause: the wrong actions set as primary conversions. Page views, duplicate thank-you pages and GA4 imports all end up steering Smart Bidding. We wrote up the checklist we use to clean it up. [blog URL] #GoogleAds #PPC

## Facebook

Running Google Ads for leads? Check which conversions are set as "primary". That one setting decides what Google's bidding chases, and we often find page views and duplicate form tracking in there. Here is our quick checklist: [blog URL] #GoogleAds

## Implementation notes

- No JSON-LD in draft; Lovable layout outputs Article, FAQPage and Breadcrumb from the FAQ block.
- Publish date: week of Oct 13, 2026 (backfill).
- External links (2) should open in a new tab with rel="noopener noreferrer".
- Internal links (8 distinct): /ppc-advertising/, /digital-marketing-reporting/, /contact/, and posts target-cpa-vs-business-cpa-google-ads, google-ads-lead-quality-loop, google-ads-account-handoff-checklist, weekly-google-ads-change-log, budget-limited-vs-demand-limited-google-ads. The two not on the brief's list (target-cpa-vs-business-cpa-google-ads, google-ads-account-handoff-checklist) were confirmed in the sitemap on 2026-11-25.
- Menu paths in Google Ads (Goals > Conversions > Summary) match the help page as of 2026-11-25; UI labels can change.

## Review 2026-11-25 (fresh-eyes editor)

- Links: every internal link returned 200 with no redirect on thinkprofits.com (the site 301s unknown URLs, so 200 = real page); posts not in the brief list were confirmed in sitemap.xml. External Google links resolve 200.
- Spelling: -ize kept per Canadian Press (brief's -ise line ignored by instruction). No em/en dashes found.
- Overlap with 06 (Ads vs GA4 vs CRM) and 09 (value-based bidding): cut the CRM side-by-side reporting recommendation in "What to expect" down to one line (reconciliation belongs to 06). Counting (One/Every) and GA4-import-as-primary stay here as settings mechanics; 06 covers them only as causes of discrepancies. Offline values/VBB are not covered here and the CRM paragraph defers to lead-quality-loop. Once 06 and 09 are live, add a contextual link from 04 to each.
- "cost per lead looks half its real size" was only true if every lead double-counted; changed to "far lower than it really is".
- FAQ on waiting time was internally inconsistent (1 to 2 conversion cycles of a few days is not "a couple of weeks"); rewrote to define a conversion cycle and label the two-week minimum as our own practice.
- CTA softened: "we will look at your conversion list, counting settings and goals" was a free PPC audit, which the brief forbids. Now a free 30-minute conversation.
- Facts re-verified on 11461796 (primary/secondary, custom goal exception, GA default secondary, 1 to 2 cycles, Goals > Conversions > Summary path), 3438531 (One vs Every, Every is website default, future-only changes), 10995103 (goal categories, account-default goals, custom goals), 6095882 (minimum call duration setting).
