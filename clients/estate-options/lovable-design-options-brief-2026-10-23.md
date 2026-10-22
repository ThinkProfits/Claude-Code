# Estate Options: Lovable design options brief (v1)

> **Status:** DRAFT v1, 2026-10-23. Built from the Oct 22 scrum, where Andrew asked Francis to build the Estate Options demos.
> **Goal:** 2 to 3 visually distinct style options, about 80% polished, for Geraldine to pick from. **This round is about look and layout, not final copy.** Working forms aren't needed.
> **Lovable:** a new project in **Shawn's Lovable** (business workspace, `rJj3ci8koRXi6ThNECB7`), named "Estate Options – Design Options". It stays in our workspace until the site is paid for and signed off. No handoff, domain, GA4, Search Console or tracking work yet.
> **Reusable:** this brief's pattern works for any "show the client 3 looks before we build" Lovable job. Swap the inputs and the three directions.

## Inputs (sources)

| Input | Where |
|---|---|
| Client overview (services, likes/dislikes, compliance) | Drive: Estate_Options_Client_Overview (`1P3xEXfWEROi7c13clV6R1HNkL29WN5-KKmC7NfT6urw`) |
| Approved keywords + page names | Drive: "Estate Options \| Initial Keyword Research FOR APPROVAL" (`1CoFEJMVF16O91ynVU6ueYz0H6ZOGagmla_ltOuJl-6A`). Geraldine approved this lawyer list (Oct 22 scrum). |
| Research draft (must-have sections per page) | [keyword-research-draft-2026-10.md](keyword-research-draft-2026-10.md), section 3 |
| Logo | Her current Estate Options logo, taken from estateoptions.ca (432×261 JPG): black condensed "ESTATE", lowercase "options", a light-blue wedge and a red wedge. "Final Logos.zip" (Oct 6 email) isn't in Drive yet. **Swap in the original files before launch.** |
| Headshot | Drive Client Assets: "Headshots _Web Only_ - Geraldine-1.jpg" (768×768, grey background) |

## Rules every option must follow

**Compliance (Law Society of Alberta + her wishes):**
- Never "specialist", "specializes", "specialty", "expert" or "best". Use "practises wills and estates exclusively".
- No testimonials, reviews, star ratings or client stories.
- Never promise "peace of mind", "easy", "simple" or "stress-free". No low or flat fees.
- The complimentary initial meeting (for estates) must not read as free legal advice.
- No "only NW Calgary estate lawyer" claim (not verified).
- No tax planning or trusts. Asset protection is worded so it doesn't imply them.
- REALTOR® always carries the ®.
- No stock photos of older people. Use only her headshot plus abstract or architectural Calgary imagery (or none).

**Must haves:**
- Her photo, prominent.
- The phone number visible in the header on every page: 403-483-2020 (calls only).
- Estate Options is the brand, with her name featured prominently next to it.
- Contact details: geraldine@estateoptions.ca, info@estateoptions.ca, PO Box 31069, RPO Bridgeland, Calgary, AB T2E 9A3. Hours: Mon to Fri 9 am to 5 pm, with evenings and weekends by appointment. Home visits across Calgary.
- Credentials: Alberta Bar 2007; ADRIC Mediator QMed 2019; Law Society of Alberta; LLB, University of Alberta; BA, University of Calgary; 12 years teaching Wills & Estates at Chinook Learning. Practising wills and estates exclusively since 2010.

**Her taste:**
- **Likes:** gkthomaslaw.ca, hoogbruin.com and especially munrocrawford.ca. Clean, easy to navigate, services shown clearly, simple and elegant.
- **Dislikes:**
  - willsandestates.ca: busy, huge graphics, stock seniors, forced "peace of mind"
  - macdonaldlawnorth.ca: amateur look
  - Glossy realtor sites
  - Dark, sombre sites that "look like undertakers"
- Tone: professional, friendly, experienced, non-judgmental. Style should suit the classic logo.

**Technical (set now so we don't redo it later):**
- Every page `noindex, nofollow` until launch.
- Semantic headings: one H1 per page.
- Mobile-first and responsive.
- WCAG AA colour contrast.
- Alt text on images.
- Canadian English.

## Site map (same in all options)

Home, Wills & Estate Planning, Estates & Probate, Executor Services, Contact. **No About page.** Home holds the bio.

| Page | H1 (draft, from the approved sheet) | Target keyword |
|---|---|---|
| Home | Estate Lawyer in Calgary (with her name) | estate lawyer calgary |
| Planning | Wills Lawyer in Calgary: Estate Planning with Wills, Powers of Attorney & Personal Directives | wills lawyer calgary |
| Estates & Probate | Probate Lawyer in Calgary: Estate Administration & Support for Executors | probate lawyer calgary |
| Executor Services | A Lawyer to Act as Your Executor or Attorney in Calgary | professional executor |
| Contact | Contact Estate Options | branded |

## What this round builds

**Only the Home page gets fully styled, in 3 versions.** Interior pages are full content only after she picks a style.

- `/` is an internal chooser page with three cards ("Option 1 / 2 / 3", a one-line description each, links). It's noindex and not part of the final site.
- `/option-1`, `/option-2` and `/option-3` are each a complete Home page in that style, with its own header (logo, nav, phone, CTA) and footer.
- The nav links point to `#` placeholders so we don't build interior pages 3 times.
- A small fixed "Design option X of 3 · draft content" label in the corner of each option.

Home sections, in order (each option styles them differently):
1. **Header:** logo, nav (Wills & Estate Planning · Estates & Probate · Executor Services · Contact), phone 403-483-2020, "Book a meeting" button.
2. **Hero:**
   - H1 "Estate Lawyer in Calgary"
   - Subhead: "Geraldine Hampton practises wills and estates exclusively, and has since 2010. Home visits across Calgary."
   - Two CTAs: call, and email or request a meeting
   - Her photo
3. **Services:** three cards linking to Planning, Estates & Probate and Executor Services. Executor Services gets a "few Calgary lawyers offer this" style emphasis, worded factually and without comparative claims.
4. **Other ways she helps:** estate mediation (ADRIC QMed); when a loved one is losing capacity; protecting your assets (no tax or trust implication); estate transitions, with a short REALTOR® bridge to geraldinehampton.com.
5. **Meet Geraldine:** photo, short bio, credentials list.
6. **How it works:** 1) Call or email, 2) Personal meeting with Geraldine (complimentary initial meeting for estates, explained as covering her process, what the estate needs and fees, *not legal advice*), 3) Engagement letter, then the work begins.
7. **Areas served:** Calgary-wide. Name Varsity, Edgemont, Scenic Acres, Dalhousie, Silver Springs, Brentwood, Charleswood, Collingwood, Foothills Estates, Hawkwood, Briar Hill, Capitol Hill, Mount Pleasant, Lake Bonavista, Signal Hill, Westhills, Coach Hill, Glamorgan, Christie Estates, plus High River and Okotoks. **No NE Calgary listings.**
8. **Fees:** "Fees depend on the work involved. Many planning services are fixed-fee; contact us for the current schedule." This follows the Munro & Crawford pattern.
9. **FAQ (4):**
   - Do I need a will?
   - What is probate, and do I need it?
   - How often should I update my documents?
   - Is it a conflict for my lawyer to also be a REALTOR®? (No: both regulators confirmed.)
10. **Contact strip:** short form (name, phone, email, short message), phone, emails, hours. The form only needs to look right.
11. **Footer:** contact details, PO Box, hours, nav, "Website by ThinkProfits" *not* shown (she isn't a portfolio piece).

Copy: write draft copy from the facts above. Keep it short and plain, with no invented facts, statistics, awards or claims.

## The three directions

| | Option 1: Classic Counsel | Option 2: Bold Modern | Option 3: Warm & Personal |
|---|---|---|---|
| Idea | Closest to Munro & Crawford and Thomas: calm, established, traditional law-firm polish. | Leans into her logo: confident condensed type and the wedge shape as a graphic motif. | Approachable and human: built around her photo and home visits. |
| Palette | White and warm off-white, deep navy text, logo blue as the accent, red only as a hairline accent | White, near-black, logo blue as the dominant colour block, red for small highlights | Soft stone/ivory, charcoal text, muted logo blue, a little red |
| Type | Serif headings (e.g. Libre Baskerville or Lora), clean sans body | Condensed sans headings echoing the logo (e.g. Oswald), neutral sans body | Soft serif headings (e.g. Fraunces), friendly sans body |
| Layout | Split hero: text left, photo right; service cards with thin borders; generous whitespace | Big hero type over a diagonal blue wedge; photo cut into the wedge; angled section dividers | Hero leads with the large photo and a personal greeting line; rounded cards; more breathing room |
| Avoid | Feeling stuffy or dark | Feeling loud, busy or glossy | Feeling casual or "lifestyle" |

All three: no stock photos of people, no heavy gradients, no dark full-page backgrounds, and no carousels or sliders.

## Review checklist (Claude checks before anything goes to Andrew)

- [ ] 3 options look clearly different, not just recoloured
- [ ] Logo is crisp and placed well, phone visible in the header on mobile and desktop
- [ ] Banned words search: specialist, specializ, specialty, expert, best, peace of mind, easy, simple, stress-free, testimonial
- [ ] No NE Calgary areas; no "only lawyer" claim; complimentary-meeting wording isn't legal advice
- [ ] REALTOR® with ®; Canadian spelling (practise as a verb, neighbourhood)
- [ ] noindex on every page; one H1 per page; alt text; AA contrast
- [ ] Mobile layout checked at 375px
- [ ] Credits used recorded in the change log

## Change log

| Date | What | Credits |
|---|---|---|
| 2026-10-23 | Brief v1 written | 0 |
