# Aloha Life: Lovable edits from Shawn's call (2026-10-09)

Project: **Maui Luxury Spa** (`f52a47a4-163a-4052-b86a-67809f0d334c`), Shawn's workspace. Not the "Remix (Aloha Life Massage)" project (`aa57ab0f`), which is a separate lotus-logo variant.
Editor: https://lovable.dev/projects/f52a47a4-163a-4052-b86a-67809f0d334c
Not published. Preview needs a Lovable login.

## Done (each verified by diff)

| # | Task | Commit | Notes |
|---|---|---|---|
| 2 | Premium VIP moved to Massage dropdown | cde9f4d | VIP copy softened: no "late-night", same-day "possible when a massage therapist is available" |
| 3 | Couples massage removed | a4d4012, ed3861b | Page deleted, `/couples-massage-maui` redirects to `/massage-services-maui`. Couples Facial and Back Facial removed too (dropped at 2026-06-17 meeting). Couples/sunset copy on area pages rewritten. |
| 4–6 | Hot Stone + Pregnancy added to dropdown; "In-Room" wording removed | bd07430 | Pregnancy = $30 add-on (matches Acuity "Pregnancy Massage Upgrade"). Hot stones = included in Silver/Gold/Platinum. |
| 8 | Pricing matched to Acuity + deep links | b42ff04, b248158 | See pricing below. Every package card links to its own Acuity category, plus a "group options" link. |
| 9 | What to Expect page under About | b248158 | `/what-to-expect`, in About dropdown after About Us |
| 10 | Footer rebuilt | 5d8a072, e475522 | Columns: Massage, Spa, About, Service Areas, Contact. `id="footer-reviews"` slot ready for the review widget. |
| — | Excluded areas removed | 5d8a072, e475522 | Wailuku, Kahului, Hana pages removed and redirected to `/service-areas`; "all of Maui" changed to "the island of Maui" |

## Individual massage service pages (same day, second request)

One data file (`src/data/massageServices.ts`) plus one dynamic route (`/massage-services-maui/:slug`) rendered by the existing `FocusedServicePage`. Commits dddbf62, b36545b, 16b8f17. The copy is our rewrite of the live alohalifemassage.com service pages, with their medical claims (depression, immune, detox) left out.

Slugs were chosen from Google Keyword Planner US volumes (Semrush API units were at zero):
- "lomi lomi massage maui" gets 320/mo vs "lomilomi" at 10, so the slug is `lomi-lomi-massage`.
- "prenatal massage maui" gets 90/mo vs "pregnancy" at 0, so the slug is `prenatal-massage`. The nav label stays "Pregnancy Massage".
- Other volumes: deep tissue 320/mo, therapeutic 260/mo, Swedish 70/mo.

| Page | New URL | Live-site URL to 301 at cut-over | Target keyword |
|---|---|---|---|
| Deep Tissue | /massage-services-maui/deep-tissue-massage | /services/deep-tissue-mobile-massage/ | deep tissue massage maui |
| Swedish | /massage-services-maui/swedish-massage | /services/swedish-mobile-massage/ | swedish massage maui |
| Therapeutic | /massage-services-maui/therapeutic-massage | /services/therapeutic-mobile-massage/ | therapeutic massage maui |
| Lomi Lomi | /massage-services-maui/lomi-lomi-massage | /services/lomilomi-mobile-massage/ | lomi lomi massage maui |
| Sports | /massage-services-maui/sports-massage | /services/sports-mobile-massage/ | sports massage maui |
| Hot Stone | /massage-services-maui/hot-stone-massage | /services/hot-stones-mobile-massage/ | hot stone massage maui |
| Prenatal | /massage-services-maui/prenatal-massage | (none) | prenatal massage maui |
| Premium VIP | /massage-services-maui/premium-vip | /services/premium-mobile-massage-therapy-services/ | — |

Search intent for all: commercial/local (book a mobile massage). The old `/premium-mobile-massage-therapy-services` redirects to the new VIP URL. Hub cards show "Learn more" links. The nav, the footer and every old `#anchor` link point to the new pages. Two approved blog.ts edits: the sports link, and "evening sessions" changed to "your first day on the island".

## Pricing source (Acuity, pulled 2026-10-09)

Booking site: https://AlohaLifeMassageAppointmentBooking.as.me/ . Acuity shows prices including Hawaii GET (4.712%). The site shows base prices.

- Bronze: 60 $149 · 75 $175 · 90 $199 · 120 $299
- Silver: 60 $175 · 75 $205 · 90 $235 · 120 $323
- Gold: 75 $249 · 105 $299 · 120 $350
- Platinum: 120 $499 · 150 $569
- Facials: Hydrating 60 $149 · Anti-Aging 60 $149 · Microchanneling (ProCell) 60 $235. The Classic Facial isn't on Acuity, so the site says "call to book".
- Pregnancy upgrade $30. Travel fees: Lahaina/Kaanapali $25, Kapalua $30, Launiupoko $20, Ulupalakua $30.
- **Waxing is not on Acuity.** The waxing bundle prices on the site were made up by Lovable. Left as they are on purpose (Dani may remove waxing); revisit.

## Still open

- **1. Logo / brand name "Aloha Life Mobile Massage & Spa"**: blocked until the Canva connector is authorized in claude.ai connector settings. Plan: edit the plumeria logo subline "MOBILE SPA" to "MOBILE MASSAGE & SPA" in white and dark versions, upload them to Lovable as image swaps only, then update `BRAND` in `src/data/site.ts`, meta and schema.
- **7. Turn PPC back on**: needs someone with Google Ads access. No write access from Claude. Conversion tracking has been down about 90% year over year since June 2026, so fix tracking first or the campaign runs blind. Suggested budget US$5–20/day, depending on season and whether tracking is fixed. Keep the Hana/Nahiku/Wailuku/Kahului exclusions and the adult-intent negatives.
- **11. Footer GBP reviews**: decision is a free widget (e.g. Trustindex). A team member creates the widget account and connects the GBP, then gives the embed code to Lovable to place in `#footer-reviews`. The hard-coded "240+ reviews" stays until then (GBP had 257 in Aug 2026).
- Valentine's couples blog (`src/data/blog.ts`, slug `couples-massage-maui-valentines-in-room-guide`) still promotes couples and side-by-side massage and a "sunset slot". The wedding blog also says "couples massage the evening before". Needs a decision: rewrite or remove.
