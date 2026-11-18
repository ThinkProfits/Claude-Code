---
type: audit
client: adaptive
date: 2026-11-18
---

# Adaptive: GA4 / GTM tracking audit (2026-11-18)

Read-only audit of the live site (beadaptive.ca) from the browser. Nothing changed in GTM, GA4 or WordPress.

## What is installed

| Item | Finding |
|---|---|
| GTM | `GTM-MTCXWSP`, live version 12, installed once (inline snippet). |
| GA4 | `G-93RZN4M2LR`. The page_view hit comes from **Site Kit** (`GT-PJSNHTT`), not from GTM. Only one page_view per load, so no double counting today. GTM also holds a Google tag settings variable for the same ID. |
| Google Ads | `AW-10928700588` conversions + Search Kings "Galaxy" script, all inside GTM. Search Kings owns these; do not touch. |
| Other | Microsoft UET (`_uetsid`), CallTrackingMetrics (`__ctmid`, likely swaps the phone number). |
| Consent mode | Site Kit sets "denied" by default for EU/UK/EEA regions only. Canadian visitors are not affected. |

## Events that already exist

The site's own code (custom contact form + calculators) pushes to the dataLayer, and GTM has GA4 event tags for them:

- `contact_form_submit`, with `form_mode` (contact / estimate), `form_has_quote` (yes / no), `form_page`. Fires only after the form API returns success. Covers the "Let's talk" popup, which is the same `#adp-cf-form` (not a GoHighLevel iframe; it posts to `api.beadaptive.ca/contact`, which then triggers GHL).
- `tools_pricing_calc_engaged` (first input on /tools/managed-it-pricing-calculator/).
- `accidental_it_calc_engaged` (the second calculator).

## Gaps against Andrew's checklist

| Checklist item | Status |
|---|---|
| GA4 tag fires via GTM only | Not met: GA4 page_view comes from Site Kit. Works and is not doubled. Moving it into GTM touches their setup, so Andrew decides. |
| `calculator_quote` key event | No "quote completed" event exists. The calculators update live; the real completion is sending the quote with the form (`form_has_quote = yes` or `form_mode = estimate`). Can be built in GTM only, no site code change. |
| Form submission key event | Event exists. Still need to confirm in GA4 that it arrives and is starred. |
| `phone_click` | Missing. 5 `tel:604-357-3456` links on the homepage. GTM link-click trigger on "tel:". |
| `email_click` | No `mailto:` links on the homepage. Check /contact/ and the footer before building. |
| GA4 key events / GSC link | Not checked yet. The GA4 MCP (agency login) cannot see this property; needs the browser signed in as seo@thinkprofits.com. |

## Proposed GTM changes (not built, waiting on Andrew)

1. `phone_click`: GA4 event tag, Link Click trigger, Click URL contains `tel:`.
2. `email_click`: same with `mailto:` (only if mailto links exist).
3. `calculator_quote`: GA4 event tag on Custom Event `contact_form_submit` where `form_has_quote` equals `yes`.
4. Leave GA4 page_view on Site Kit unless Andrew wants it moved into GTM.
5. After publishing: star `contact_form_submit`, `calculator_quote`, `phone_click`, `email_click` as key events; leave the two `_engaged` events unstarred.
6. Test in GTM Preview + GA4 DebugView before marking done. No test form submission without Ian's OK (it fires their GHL workflow).
