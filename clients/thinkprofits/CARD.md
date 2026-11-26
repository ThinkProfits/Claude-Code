---
type: card
client: thinkprofits
updated: 2026-11-19
---

# ThinkProfits (our own account): card

**Status:** Internal account for thinkprofits.com on Lovable. The plumbing industry page went live on 2026-10-14, and the redirect fixes for the September 404 spike are drafted but not yet sent to Lovable.

**Next step:** Get Andrew's OK on the redirect-fix message and send it to Lovable (missing 301s, the soft 404 on case-study URLs, and the www 302 that our GBP link passes through).

**Blogs stalled since September (found 2026-11-25).** The ChatGPT daily "Lovable-ready blog package" posts in DM `D06U5NPDEQ6` hold only summaries; the article copy sits in a ZIP inside each ChatGPT run. The Slack-to-Lovable relay (Cowork routine `trig_012ThbYzzU6FgYRGxjzRRv3p`) sent 6 approved packages (12 articles, Nov 4 and Nov 11), Lovable replied "package missing, nothing changed" every time, and the relay still posted "forwarded to Lovable". None of those URLs are live. Relay routine **disabled** 2026-11-25; Francis is moving that task to Grok. Backfill instead: 10 new posts (one per missing week) written, reviewed and revised by Claude in [blog-backfill-2026-11/](blog-backfill-2026-11/); batch 1 (3 posts) built in Lovable 2026-11-25, commit `90f0dce`, awaiting Francis's Publish. Remaining batches and the reusable send process: [RELEASE-PLAN.md](blog-backfill-2026-11/RELEASE-PLAN.md). Two older live posts (`faq-schema-dead...`, `maps-pack-still-wins-local-ai-overviews-8-percent`) quote unsourced stats; Grok drafted the refresh (TP-3), Francis approved it 2026-11-26 but it is held, not live (see memory/thinkprofits-site-drafts-grok.md).

**New (2026-11-18): Vancouver digital marketing agency page.** Shawn sent an AI-answer fix doc ([data/2026-11-14-vancouver-agency-fix-from-shawn.docx](data/2026-11-14-vancouver-agency-fix-from-shawn.docx)) asking for a standalone /digital-marketing-agency-vancouver/ page (today it 301s to /seo-company-vancouver/). Facts checked against the live site on 2026-11-18. The Lovable message was sent on 2026-11-18 with Francis's OK (message `main:user#00000000001669#usr:C3RCBQBH`). Lovable finished the build on 2026-11-18 (commit `2791a38`, 6.3 credits) and the diff was reviewed on 2026-11-19: redirect removed (only that rule), copy word for word, FAQPage + BreadcrumbList + Service schema (Service points to the existing `#localbusiness`), self canonical, sitemap entry, links from the homepage services area and /services/. Nothing is published yet, so the live URL still 301s. Before or right after publishing: the "Last updated" date is hard-coded to 18 November 2026, the /services/ link sits alone on its own line with no sentence around it, and the GBP link is a Maps search URL rather than the profile's own link. Message: [lovable-message-digital-marketing-agency-vancouver-2026-11-18.txt](lovable-message-digital-marketing-agency-vancouver-2026-11-18.txt). Changes from Shawn's draft: the meta description was cut to 155 characters, the sentence naming Major Tom, Brandcamp, dNOVO and 1UP was removed, and an FAQ was added. PAA wasn't pulled because Semrush units are at zero. GSC (90 days): "digital marketing agency vancouver", "marketing agency vancouver" and "best digital marketing agency vancouver" rank at positions 1–4 through the homepage GBP URL (`?utm_source=gmb_listing`). /seo-company-vancouver/ doesn't rank for them, so removing the redirect carries no cannibalisation risk. Keep the GBP website URL on the homepage. Still open for Shawn: Clutch profile, a single PPC starting price, and the EY/Mujo proof items.

**Also open from the 2026-10-13 team check-in:** make sure the published plumbing page leads with the ~$3,995+/month bundles, not $399 PPC; Andrew is updating the bundle deliverables. Full list: CLIENT.md section 12; exact instructions in [team-check-in-2026-10-13-francis-tasks.md](team-check-in-2026-10-13-francis-tasks.md).

**Open from Andrew (Slack DM, bot still following up as of 2026-11-04):** Andrew forwarded an email from Shawn with questions about the TP site and asked Francis to handle it. Find that email, answer it, and reply in the DM.

**Blocked on:** Andrew: OK on the redirect message, decisions for industry-page Phases 1 to 8, updated plumbing bundles, and a review of the plumbing page FAQs. Shawn (away until 2026-10-23): text edits on the plumbing page, sign-off on the family timeline years and the 1998 "12×" wording. Semrush API units are at zero, which blocks the Site Audit rerun.

**Last activity:** Plumbing industry page published at /industries/plumbing/ (2026-10-14). GBP posts for 2026-10-12 and 2026-10-15 handed off (week-of-2026-10-12).

## Where things live

| What | Where |
|---|---|
| Agency profile (team, services, workflows, open items) | [CLIENT.md](CLIENT.md) |
| Keywords and GSC detail for our site | [keywords.md](keywords.md) |
| Industry page audit and keyword research | [industry-pages-audit-2026-10-07.md](industry-pages-audit-2026-10-07.md) |
| Lovable brief for the industry page rebuild | [lovable-brief-industry-pages-2026-10-07.md](lovable-brief-industry-pages-2026-10-07.md) |
| Industry page template and plumbing page files | [industry-pages/](industry-pages/) |
| 2026-10-13 team check-in: Francis's tasks (verbatim quotes), Grockbot notes, Claude-artifacts feasibility | [team-check-in-2026-10-13-francis-tasks.md](team-check-in-2026-10-13-francis-tasks.md) |
| 404 spike and traffic drop check | [404-traffic-tracking-check-2026-10-09.md](404-traffic-tracking-check-2026-10-09.md) · reply to Andrew: [andrew-reply-404-traffic-2026-10-09.md](andrew-reply-404-traffic-2026-10-09.md) |
| Other working files | `lovable-message-*.txt` (Lovable messages), `thinkprofits.com-*.xlsx` (GSC exports), [data/](data/) (blog triage, sitemap, industry research) |
| GBP handoffs | `gbp-handoffs/week-of-*/gbp-handoff__thinkprofits_vancouver__*` |
| Semrush | project 2029236 (from the brief, not verified) |
| Slack | #tpmarketing · GBP approvals: #gbp-post-approvals |
| Lovable | "Thinkprofits Rebuild" `12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17` |

**Before any task, read CLIENT.md sections 7 (standards) and 11 (working rules).** This card only gives status and pointers. It deliberately repeats no rules.
