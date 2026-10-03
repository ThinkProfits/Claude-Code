# John Sadler Plumbing & Heating — Brand Reference

Extracted directly from the live site (johnsadler.ca) on 2026-08-28 via computed styles.
Use this file as the source of truth when building new HTML pages for this client — keeps
new pages visually consistent with the existing site instead of guessing colors/fonts each time.

## Company facts (NAP + credentials)

- **Legal/trade name:** John Sadler Plumbing & Heating
- **Established:** 1976 (50 years in business as of 2026 — site copy is inconsistent, some
  pages still say "45 years"; use 50 and flag the rest for correction)
- **Phone:** (604) 531-4355
- **Email:** service@johnsadler.ca
- **Hours:** Monday–Friday, 8:30 AM–5:00 PM (footer-stated; confirm before claiming any
  24/7/emergency availability — one service page claims 24/7, footer contradicts it)
- **TSBC Licences:** #LGA0092486 (gas) & #LBP0207908 (plumbing) — must be displayed per
  BC regulation (effective 2023)
- **Certifications:** Navien Certified Service Specialist (NSS)
- **Brands serviced:** Navien, Lennox, Carrier, Trane, Rheem, American Standard, Napoleon,
  Continental, Goodman, Keeprite, Bradford White, AO Smith, Giant, John Wood
- **Service area (in site's own order):** Surrey, Langley, White Rock, North Delta,
  Cloverdale, Ocean Park, Panorama Ridge, Fleetwood, Whalley, Fort Langley, Brookswood,
  Murrayville, Clayton, South Surrey, Morgan Creek, Guildford, Newton, Fraser Heights,
  Walnut Grove, Willoughby, Aldergrove, Abbotsford

## Logo & favicon

- **Primary logo (transparent PNG):** `https://www.johnsadler.ca/wp-content/uploads/2021/09/JOHN-SADLER-transparent-300.png`
- **Favicon:** `https://www.johnsadler.ca/wp-content/uploads/2019/07/cropped-jsphlogo-2017-1-32x32.png`
- Logo alt text used sitewide: "John Sadler Plumbing & Heating"

## Colour palette

| Swatch | Hex | RGB | Usage |
|---|---|---|---|
| Brand red | `#DD1515` | rgb(221,21,21) | Primary CTA button background ("CONTACT US", "GIVE ME FREE QUOTE") |
| Charcoal (body text) | `#252525` | rgb(37,37,37) | Default body text, dark section backgrounds |
| Near-black | `#2D2D2D` | rgb(45,45,45) | Secondary dark text/background variant |
| Pure white | `#FFFFFF` | rgb(255,255,255) | Page background, text-on-dark |
| Link/accent blue | `#005394` | rgb(0,83,148) | Inline text links within body copy |
| Deep teal-blue | `#005A78` | rgb(0,90,120) | Occasional icon/accent color |
| Navy (secondary bg) | `#005299` | rgb(0,82,153) | Section background accent (used sparingly) |
| Deep navy | `#001E38` | rgb(0,30,56) | Dark section/footer background variant |
| Light gray | `#D0D0D0` | rgb(208,208,208) | Divider/background fill |
| Mid gray | `#CCCCCC` | rgb(204,204,204) | Divider/background fill |
| Muted gray text | `#AAAAAA` | rgb(170,170,170) | De-emphasized text (fine print) |

**Pattern:** white and charcoal-on-white sections alternate with dark charcoal/navy full-bleed
sections (classic contractor-site banding). Red is reserved almost exclusively for CTAs —
don't use it for body text, headings, or decoration; it's a "click here" signal only.

## Typography

- **Headings (H1/H2/H3):** `Montserrat` — bold (700) for major headings (H1 ~28.8px on
  page banners, up to 40-60px for big stat/trust callouts), medium (500) for smaller
  sub-headings (~20.8px, e.g. service category labels)
- **Body text:** `Roboto`, falling back to `Arial, sans-serif` — regular weight, ~19.2px
  with generous line-height (~32.6px / ~1.7 ratio) — site favours airy, readable paragraphs,
  not dense text blocks
- **Buttons:** `Montserrat`, uppercase (e.g. "CONTACT US", "CONTACT JOHN SADLER TODAY!"),
  white text on red background, ~4px border-radius (soft, not sharp, not pill-shaped)

## Voice & tone

- First-person plural ("we/our"), direct, plain-language — roughly grade 8-9 reading level,
  no jargon without explanation
- Local-family-business framing used often: "locally-owned," "family business," "since 1976"
- Reassurance-driven copy: emphasizes licensing, upfront pricing, "no hidden fees," honest
  advice — trust signals over hype
- Avoid unverifiable superlatives ("#1," "best") — found and flagged one instance
  (`/plumbers-near-me/` title tag said "#1 Plumber Surrey BC"); house style otherwise leans
  on verifiable facts (licence numbers, years in business, named brands serviced) rather
  than ranking claims
- CTA phrasing patterns: "Contact Us Today," "Book Our [Service] Now!," "Call Today and
  Make an Appointment," "Get a Free Quote Today!"
- Canadian spelling used inconsistently on-site ("Licence" on TSBC references, standard
  American spelling elsewhere) — default to Canadian spelling in new copy per agency standard

## Structural/component patterns to reuse

- Every service/location page opens with a full-width banner: dark background, white
  H1, white sub-line stating the service area ("Serving White Rock, South Surrey, Surrey,
  Langley & Aldergrove"), phone number + "CONTACT US" button top-right
- "Why Choose John Sadler" numbered trust-point section appears across multiple pages
  (numbered 1-7: Decades of Local Experience, Licensed & Certified Experts, etc.) — treat
  as a reusable component/block, not something to rewrite per-page
- Footer is identical across all pages: NAP, full service-area list repeated, hours,
  payment methods, both TSBC licence numbers, copyright line (currently stale — says
  "Copyright © 2025," needs updating to 2026)

## Known inconsistencies to fix opportunistically (not blockers, just flag when touching a page)

- "45 years" vs "50 years" (business age) — standardize to 50
- Footer copyright year stuck at 2025
- 24/7 emergency claim on one page contradicts Mon–Fri footer hours — confirm real policy
