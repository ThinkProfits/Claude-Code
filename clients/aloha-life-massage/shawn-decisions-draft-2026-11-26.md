# Draft: Slack DM to Shawn, Aloha new-site decisions (2026-11-26)

> Status: DRAFT, not sent. Needs Francis's OK. Internal (Shawn only), not client-facing.

---

Hey Shawn, I ran a full SEO audit on the Aloha Lovable build. The short version: it looks fantastic, but there are a few things we need to sort out before it goes live, or we'll likely lose most of the organic traffic the old site earns.

**Already done (in Lovable, nothing published):** wording fixes ("massage therapist", never "therapist" on its own), shorter title tags, cleaned-up schema, area-page headings now say "Mobile Massage in [Area]", and missing links on the massage page. I didn't touch the homepage headline. That one's your call (see 9).

**Launch blockers on our side** (no decision needed, just time):
- Search engines and AI tools (ChatGPT, Perplexity) currently see a blank page, because the site is JavaScript-only. It needs prerendering.
- The "redirects" aren't real 301s yet, and the ~45 old URLs need mapping. The map is drafted.
- The 4 forms (VIP NDA, retreat sign-up, newsletter, job application) don't send anywhere yet.
- No analytics or tracking installed.
- The blog came over as short stubs and 3 posts are missing. It needs the full text re-imported.

**Decisions I need from you (some will need Dani):**
1. **Domain and name:** keep alohalifemassage.com (safest, keeps 7 years of rankings) or move to alohalifemobilespa.com? And is the business name "Aloha Life Massage", "Aloha Life Mobile Spa" or "Mobile Massage & Spa" (what the logo says)? It has to match the Google Business Profile exactly.
2. **Couples bookings:** can we say two massage therapists can work at the same time, if booked ahead? One review mentions exactly that. "Couples massage maui" gets ~720 searches a month, and right now we have no page for it because of the side-by-side rule.
3. **Lymphatic drainage:** is it a bookable service? The old blog on it is our best non-brand page. A service page could build on that.
4. **Paia, Haiku, Makawao:** do we serve them, and what are the travel fees? Paia and Haiku already have pages.
5. **Licensing:** Dani's (and the team's) Hawaii licence numbers, plus a check that the "570 hours / Hawaii doesn't accept the MBLEx" claims are accurate. Those claims are on every area page. Also, are estheticians allowed to do microneedling in Hawaii?
6. **Waxing:** keep or drop? It isn't on Acuity, and the prices on the site were placeholders. Some are below Dani's $150 wax-only minimum.
7. **Retreats:** OK to hide the page until there are real 2027 dates? It currently lists past 2026 dates and one retreat in Hana.
8. **Hosting:** are you OK with us deploying the build outside Lovable (e.g. Netlify or Cloudflare) if Lovable's hosting can't do prerendering and real redirects?
9. **Homepage headline:** "luxury mobile spa" gets almost no searches. "Maui massage" gets ~2,900 a month. Can we work "massage" into the main heading, e.g. "Mobile Massage & Spa in Maui, Brought to Your Door"?

The full audit has page-by-page notes and the redirect map. Happy to walk you through it in 15 minutes whenever suits.

---

**Sources for the numbers:** Google Keyword Planner, US, average monthly searches, Nov 2025 to Oct 2026. Old-site performance comes from Google Search Console, Aug 27 to Nov 25, 2026.
