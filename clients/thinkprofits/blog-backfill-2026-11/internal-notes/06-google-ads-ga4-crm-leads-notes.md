# Internal notes: 06-google-ads-ga4-crm-leads

**Scope:** Analytics explainer plus how-to (topic #6, week of Oct 27): why Google Ads, GA4 and a CRM report different form-lead counts (attribution/creditable channels, click date vs event date, counting method, windows, modelled and view-through conversions, CRM spam/duplicates/offline leads) and a monthly reconciliation routine. Links `google-ads-lead-quality-loop` without repeating its CRM import build.

## Sources checked (all fetched 2026-11-25)

- https://support.google.com/analytics/answer/13965727 (Conversions vs key events): conversions are for ad measurement, key events for behaviour analysis; attribution, windows, counting method can differ; "Google Ads conversions don't appear in standard Google Analytics reports in the Reports or Explore sections." Cited in post.
- https://support.google.com/google-ads/answer/3438531 (Counting options): Every vs One; One recommended for leads. Cited in post.
- https://support.google.com/google-ads/answer/6270625 (Understand conversion tracking data): Conversions/All conv. reported by click time; "by conv. time" columns exist; view-through only in All conv.; Conversions = primary actions.
- https://support.google.com/google-ads/answer/6259715 (Attribution models): data-driven is default for most conversion actions; first click/linear/time decay/position-based retired; last click still supported.
- https://support.google.com/google-ads/answer/10081327 (Modelled online conversions): Conversions column includes modelled + observed; reasons (browser cookie limits, consent, cross-device).
- https://support.google.com/google-ads/answer/3123169 (Conversion windows, via search result summary): 30-day default click-through, up to 90 days.
- https://support.google.com/analytics/answer/10597962 (GA4 attribution settings): key event lookback default 90 days (30/60 options); 30 days for first_open/first_visit.
- https://support.google.com/analytics/answer/13366706 (GA4 counting method): Once per event recommended/default; once per session legacy.

## Claims cut or softened

- "Discrepancies often up to 20% are expected" (surfaced on 6270625 fetch): cut; FAQ says Google publishes no single acceptable range.
- "24 to 48 hour reporting lag" and "Ads data within 3 hours vs imported GA4 within 9 hours": cut (could not confirm on a current page); replaced with "wait at least a week after month end", which is our own process advice.
- GA4 default "paid and organic" creditable channels: only in a search summary, not confirmed on the fetched page; post phrases it as GA4 crediting organic/email/direct in standard reports without naming the setting default.
- June 15, 2026 Consent Mode change (from 13965727): left out as too granular for this post; candidate for its own news item.
- Third-party "10 to 30% gap is normal": excluded (vendor blog, not primary).

## Keyword data (google-ads-keywords MCP, Canada, Nov 2025 to Oct 2026)

- Primary "google ads vs ga4 conversions" and variants (don't match, discrepancy): 0 recorded volume. Topic is driven by the brief; title leads with the phrase because it matches how people describe the problem.
- google ads conversion tracking 90/mo; ga4 conversions 10; ga4 key events 10; data-driven attribution 10; google ads attribution model 10; enhanced conversions for leads 10; offline conversion tracking google ads 10; crm lead tracking 10; import ga4 conversions to google ads 10; google ads conversion tracking ga4 10.
- PAA-style questions found via web search and folded into FAQ: why Google Ads shows more conversions than GA4; import GA4 vs Google Ads tag; what gap is normal; fewer CRM leads than Google Ads.

## Cannibalisation

Checked https://thinkprofits.com/sitemap.xml. Nearest posts: `ga4-custom-conversion-windows-long-sales-cycles` (window selection only; mentions quarterly CRM reconciliation but not the causes of the gap) and `google-ads-lead-quality-loop` (CRM to Ads import and match rate; no GA4, no attribution). No existing post targets "google ads vs ga4 conversions". Both linked as supporting posts. Batch post #4 (`primary-vs-secondary-conversions-google-ads`) is a natural link once live; add it in step 2 of the routine after it publishes.

## Image note

Hero only: `/images/blog/wp/tp-branded-placeholder.jpg`, alt "Google Ads, GA4 and CRM lead counts compared side by side in a monthly report". No AI images.

## Implementation

No JSON-LD in draft; Lovable layout outputs Article, FAQPage and Breadcrumb from the FAQ block. Publish date: week of Oct 27, 2026. External links open in new tab. The 48/41/33/20 figures in the intro are labelled illustrative in the post.

## GBP post (ThinkProfits Vancouver)

Google Ads says 48 leads, GA4 says 41 and your CRM says 33? That is normal, and it is fixable. Our new guide explains the settings behind Google Ads vs GA4 conversions, why the CRM differs again, and the monthly routine we use to reconcile them. CTA: Learn more (blog URL).

## LinkedIn

Three tools, three lead counts, one tense meeting. Google Ads, GA4 and your CRM each count a form lead differently: different dates, different attribution, different counting rules. Our latest guide walks through each gap and a monthly reconciliation routine so you know which number to use for bidding, channel mix and budget. [blog URL] #GoogleAds #GA4

## Facebook

Ever noticed Google Ads, Google Analytics and your CRM never agree on how many leads you got? We break down why, and how to check which gaps are normal and which are real tracking errors. [blog URL] #DigitalMarketing

## Review 2026-11-25

- Links: all internal links 200 with trailing slash; both external Google links 200.
- Verified on Google pages: 30-day default click-through window, settable to 90 (answer/3123169, "If you don't customize the click-through conversion window... the default window is 30 days"); Conversions column reported by click time and view-through only in All conv. (6270625); DDA default and retired models (6259715); GA4 key event lookback 90 days default and GA4 reports default to Paid and Organic attribution (analytics 10597962). Window sentence kept, tightened to "can be set as long as 90 days".
- "Conversions and All conv. are reported by click time" narrowed to the Conversions column (page states it directly only for Conversions).
- GA4 creditable-channels sentence now states the verified Paid and Organic default.
- Overlap with 04: counting-method section trimmed to the GA4 contrast and now links to 04; routine step 2 no longer repeats 04's duplicate-action check, links to it instead; FAQ on GA4 import vs Ads tag reframed around cross-tool comparison. **04 must be live before this post publishes** (/digital-news/primary-vs-secondary-conversions-google-ads/ currently 301s to /digital-news/ because it is unpublished).
- Voice: rewrote the stock scenario opener and "meeting goes downhill" line; merged the one-line "Aim for gaps..." paragraph; replaced "pays for itself".
