# Handoff: Adaptive GTM / GA4 conversion tracking (from session of 2026-11-18)

Start a new session in `E:\ThinkProfits\Claude-Code` and paste or point it at this file.

## Goal

Finish the "GA4 & GTM" section of the Adaptive SEO setup checklist: every Key Event (`contact_form_submit`, `calculator_quote`, `phone_click`, `email_click`) fires once, shows in GA4, and is starred as a key event. Only mark the checklist items Done after a live test in GTM Preview and GA4 DebugView.

Source: Gemini notes from the Weekly Team Check-in (2026-11-17), action item "[Francis] Set up Analytics: Perform the analytics setup and conversion tracking for the Adaptive account. Verify if the existing configuration is complete."

## Read first

1. `clients/adaptive/CARD.md`: status, hard rules, access
2. `clients/adaptive/tracking-audit-2026-11-18.md`: what is already installed and the gaps (read-only audit, nothing changed)
3. `clients/adaptive/andrew-instructions-verbatim.md`, section "GA4 & GTM": Andrew's checklist wording

## Hard rules for this task

- **Andrew signs off before any GTM change.** Adaptive is an IT firm and very technical. Andrew's rule: run every change past him first and never break their existing code. Send him the proposed changes (list below) in #adaptive and wait for his OK.
- **Never publish without Francis's explicit "yes, publish Adaptive" in chat.** Build in a new workspace and create a version, then Francis publishes by hand.
- **Don't touch Search Kings' tags.** The Google Ads conversion tags (`AW-10928700588`), the Galaxy script and their variables belong to Search Kings, who run Adaptive's Google Ads.
- **No test form submissions without Ian's OK.** The form posts to `api.beadaptive.ca/contact`, which starts a GoHighLevel workflow and reaches Ian's team. Ask Francis to arrange one real test.
- **No site code changes.** Everything below can be done in GTM. If a site change ever looks needed, it goes to Andrew and Ian.
- **Don't create a new GTM container or GA4 property.** Use the existing ones.

## Current state (verified 2026-11-18 on the live site)

| Item | Value |
|---|---|
| GTM container | `GTM-MTCXWSP`, live version 12 |
| GA4 | `G-93RZN4M2LR`. The page_view comes from the Site Kit plugin (`GT-PJSNHTT`), not from GTM. One page_view per load, so no double count. |
| Events already in GTM | `contact_form_submit` (params `form_mode`, `form_has_quote`, `form_page`), `tools_pricing_calc_engaged`, `accidental_it_calc_engaged`. All GA4 event tags use `{{Event}}` as the name and `G-93RZN4M2LR` as the measurement ID override. |
| How the form event works | The site's own JS pushes `contact_form_submit` to the dataLayer only after the API returns success. The "Let's talk" popup is the same `#adp-cf-form`; it is not a GoHighLevel iframe, so no postMessage listener is needed. |
| Phone | 5 × `tel:604-357-3456` on the homepage. CallTrackingMetrics is on the site (`__ctmid` cookie) and may swap the number, so match on `tel:` not on the number. |
| Email | No `mailto:` links on the homepage. Check /contact/ and the footer. |
| Consent mode | Site Kit sets "denied" only for EU/UK/EEA regions. Canadian traffic is not affected. |
| Not checked yet | GA4 key events, GA4 to Search Console link, Data retention, Enhanced measurement settings, which user roles seo@thinkprofits.com holds in GTM and GA4. |

## Steps

1. **Confirm access** in the browser signed in as seo@thinkprofits.com: Publish access in GTM (`GTM-MTCXWSP`), Editor in GA4 (`G-93RZN4M2LR`). Request it if missing. The `ga4` MCP is signed in as the agency account and does **not** see Adaptive's property, so use the browser for GA4.
2. **Check GA4 (read only):** Admin > Events: is `contact_form_submit` arriving, and is it a key event? Admin > Product links > Search Console: linked to `sc-domain:beadaptive.ca`? Note what you find in the audit file.
3. **Send Andrew the proposal** in #adaptive (draft it for Francis to send, don't post it yourself):
   - Add `phone_click`: GA4 event tag, Link Click trigger (Just Links), Click URL contains `tel:`.
   - Add `email_click`: same with `mailto:`, only if mailto links exist on the site.
   - Add `calculator_quote`: GA4 event tag on Custom Event `contact_form_submit` with condition Data Layer Variable `form_has_quote` equals `yes`. Uses the existing dataLayer variables, so no site code change.
   - Keep GA4 page_view on Site Kit (works, not doubled). This is the one checklist item ("GA4 fires via GTM only") we recommend not doing; Andrew decides.
   - Key events to star: `contact_form_submit`, `calculator_quote`, `phone_click`, `email_click`. Leave the two `_engaged` calculator events unstarred.
4. **After Andrew's OK, build** in a new GTM workspace named `TP conversion tracking 2026-11`. Reuse the existing `G-93RZN4M2LR` constant variable and the `form_has_quote` dataLayer variable. Enable the built-in Click URL variable if it's off. Use tag and trigger IDs that don't clash.
5. **Test in Preview** (Tag Assistant): click a phone link once with a capture-phase `preventDefault()` so nothing dials; confirm `phone_click` "Fired 1 time" and the hit in GA4 DebugView. `calculator_quote` and `contact_form_submit` need one real form send with a quote attached, which needs Ian's OK (see rules).
6. **Create a version** with notes and ask Francis: "yes, publish Adaptive?" Francis publishes in the GTM UI. Confirm by fetching `https://www.googletagmanager.com/gtm.js?id=GTM-MTCXWSP` and grepping `phone_click` / `calculator_quote`.
7. **Next day:** star the key events in GA4 (Admin > Events). An event shows there only after GA4 has received it, which can take hours to a day.
8. **Close out:** update `CARD.md` (Now / Last activity), the audit file, this handoff (log below), and the checklist sheet [SEO Setup Checklist | Adaptive](https://docs.google.com/spreadsheets/d/1ep8ZhqAo8ERoui-ItkGnhXAFPrdGWQ-3HLZlDcNRzUI/edit). Post a short summary in #adaptive with what's live and what's still unverified.

## Tools

- **Browser** (built-in pane or Claude in Chrome) signed in as seo@thinkprofits.com, for GTM and GA4 admin.
- **`gtm` MCP server** (local, `E:\Claude\mcp-servers\gtm`, user-scope in `~/.claude.json`): list/find containers, workspaces, create/update tags, triggers and variables, create versions. It does **not** publish, by design. Signed in 2026-11-18 as the agency account (same as the GSC server); token at `%LOCALAPPDATA%\mcp-gtm\token.json`; re-auth with `gtm_auth.py`. It sees 89 GTM accounts but **not** `GTM-MTCXWSP` (see Log). The GTM API quota is a few queries per minute, so pass `account_name_hint` to `find_container`. Fallback: build in the GTM UI (Import Container > **Merge**, never Overwrite; the preview must read `0 Deleted`).
- The `gtm-event-tracking` skill describes the same method for Adapting Social clients. Its steps for Preview testing and starring key events apply here, but its file locations and Wix/Elementor rules don't.

## Log

- 2026-11-18: read-only audit done (`tracking-audit-2026-11-18.md`). Nothing changed in GTM, GA4 or WordPress. Waiting on Andrew's OK for the proposal in step 3.
- 2026-11-18 (later): `gtm` MCP signed in as the agency account. Step 1 finding: the agency account's GTM account "Adaptive Technical Inc." (`accounts/4319822099`) holds only `GTM-K82P6LX` ("www.beadaptive.ca"), which is **not** on the live site. The live homepage loads `GTM-MTCXWSP` (3 refs) and `GT-PJSNHTT`, nothing else. So the agency account has no access to the live container yet. Ask Adaptive (Andrew/Ian) who owns `GTM-MTCXWSP` and for Publish access for the agency account. `GTM-K82P6LX` looks like an old, unused container: leave it alone.
