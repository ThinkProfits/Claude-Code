# Estate Options site audit (pre-Andrew review)

- **Date:** 2026-10-29
- **Build:** Lovable project 69c1b714-db52-47cf-b5b5-0dc70974ab8c. The audit covers HEAD `2e0e532b`, which is commit `4b40de20` plus three later edits made directly in Lovable:
  - hero meeting buttons
  - the /blog page
  - the /about page
- **Method:** two passes.
  - Pass 1: a page-by-page read of the source.
  - Pass 2: an independent reviewer re-read all the source, the build brief, the keyword research and the Client Overview, without seeing pass 1.
  - Every item below was found or confirmed by at least one pass. Items marked **(both)** were found independently by both.
- **Not covered:** a rendered visual check. The preview needs a Lovable login, and the built-in browser isn't signed in. Desktop and 375px screenshots are still owed (see section 8).

Severity:
- **High:** fix before Andrew sees it.
- **Medium:** fix in the next round.
- **Low:** polish.

---

## 1. Summary

- No errors found against the client's rules:
  - no banned words
  - REALTOR® always carries the ®
  - no NE Calgary communities
  - Canadian spelling
  - one H1 per page
  - every fact checks out against the Client Overview
  - colour contrast passes AA
- **3 High issues:**
  - 2 legal-accuracy risks on the Executor page
  - no privacy notice or legal disclaimer anywhere on the site
- **2 new pages need a decision:**
  - /about goes against the Overview's "no About page at launch" and duplicates the Home bio word for word.
  - /blog is in the main nav but empty.
- **The gaps that matter most to the client are:**
  - schema (none yet)
  - internal linking (Probate and Executor are dead ends)
  - the intake form, which makes estate enquirers answer will-planning questions

---

## 2. High: fix before Andrew

| # | Page | Issue | Fix |
|---|---|---|---|
| H1 | Executor | The "Two roles" section offers Geraldine as **attorney under your EPA**. Alberta's Powers of Attorney Act requires a lawyer's certificate of legal advice, and the certifying lawyer can't be the named attorney. She likely can't draft *and* certify an EPA naming herself. (pass 2; needs Geraldine to confirm) | Add the question to the existing compensation ReviewNote: "Who gives the legal-advice certificate when you're named as attorney?" |
| H2 | Executor | The "Why name a lawyer" bullet reads "*carry mandatory professional liability insurance*". It suggests her executor or attorney role is insured. ALIA coverage is for legal services and may not cover acting as executor. The Overview doesn't support it. **(both)** | Remove the bullet, or ask Geraldine to confirm the coverage. |
| H3 | Sitewide | No privacy policy and no "general information, not legal advice" disclaimer. The intake form collects sensitive data (disability, litigation, marital status), so Alberta's PIPA applies. **(both)** | Add a footer disclaimer line and a /privacy page. Link the page from both forms. |
| H4 | /about (new) | The Overview says "*no About page at launch*". The page repeats the Home bio, credentials and headshot word for word, which creates duplicate content. Nothing links to it except the nav. | Decide: (a) remove it, or (b) keep it, give it its own content, and link "Meet Geraldine" on Home to it. Ask Andrew which. |
| H5 | /blog (new) | It's in the main nav but shows "*No articles have been published yet.*" An empty blog makes a new site look abandoned. The nav is also now 7 items plus the phone number and CTA, which risks crowding the desktop header at 1024px (needs a visual check). | Keep the route but take it out of the nav and footer until the first posts exist. |

---

## 3. Questions for Geraldine (add to ReviewNotes)

These are new questions from the audit. The existing open notes on compensation, LSA disclosure, REALTOR® wording, filing fees and FAQ copy stay as they are.

1. Who gives the legal-advice certificate when you're named as attorney under an EPA? (see H1)
2. Does your professional liability insurance cover you when you act as executor or attorney? (see H2)
3. Is the first wills meeting charged, or complimentary like the first estate meeting? Home step 2 only mentions estates.
4. Should Westhills sit under West Side? The Overview groups it with the SW communities; the site lists it under "Also serving".

---

## 4. Page by page

### Home `/`

**Content**
- **M (pass 2):** The Step 2 note "*This is an introductory meeting, not legal advice*" sits under a step that also covers wills meetings, which *are* legal advice. Change it to "The complimentary estate meeting is introductory, not legal advice."
- **M (pass 2):** FAQ "Do I need a will?" says "*someone must apply to the court*", but the probate page says a grant is "Not always" needed. Change it to "someone may need to apply".
- **M (pass 2):** "*When an estate includes a home, Geraldine is also a REALTOR®.*" doesn't follow. Change it to "When an estate includes a home, it helps that Geraldine is also a REALTOR®."
- **L (both):** Two FAQs ("Do I need a will?", "How often should I update…") repeat on the Wills page with different answers. Give each page its own questions, or use one answer in both places.
- **L (pass 1):** The hero says "Home visits across Calgary", but the areas list includes High River and Okotoks. Either say "across Calgary and area" or confirm she visits those towns.
- **L (both):** Dashes are inconsistent. The hero quote uses a spaced en dash ("comfortable – often", as specified in the brief); the rest of the site uses em dashes. Serial commas are also mixed: Home step 2 has "process, what the estate requires, and her fees", while Probate has "…and her fees". Use the Probate version ("is likely to require") on both pages.
- **L (pass 1):** "Protecting what you've built" is vague and repeats the Wills card. Sharpen it or cut it.

**UX/UI and conversion**
- **M (both):** The three service cards all use "*Learn more →*" as link text. That's generic anchor text, and screen readers read the arrow aloud. Use "Wills & estate planning", "Probate & estates" and "Executor services".
- **M (both):** The short form has no required fields, so an empty submit still says "Thank you". It also lacks the "*don't send confidential documents / no lawyer-client relationship*" line that the /contact form has.
- **L (pass 1):** The Fees block doesn't mention the complimentary estate meeting, which is the strongest offer on the page.
- **L (pass 2):** The PO Box shows on Home and in the footer without the "mailing address only" note, so people may expect an office.

**Technical**
- **M (both):** The hero H1 uses `fade-up` and starts at opacity 0 for 0.7s, which delays the Largest Contentful Paint (LCP). The headshot also has no `fetchpriority="high"`. Remove the animation from the H1 and add fetchpriority.
- **L (pass 2):** The headshot appears twice with the same alt text. Set the second one to `alt=""`.
- **L (both):** The meta description is 164 characters. Trim it to about 155.

### Wills & Estate Planning `/wills-estate-planning`
- **M (pass 2):** The Signing step says "*You sign with Geraldine present, so everything is witnessed properly*". That implies one witness (Alberta requires two) and reads like an assurance. Change it to "You sign with Geraldine, and your documents are signed and witnessed as Alberta law requires."
- **M (pass 2):** "Choosing your attorney" ends "*Geraldine can act for you — see*" and the link drops onto its own line. Make the link inline, or end the sentence first.
- **M (both):** The title is 76 characters. Suggest "Wills Lawyer in Calgary | Wills, EPAs & Directives" (51). The meta description is 188 characters; cut the "Practising… since 2010." sentence.
- **L (both):** The H1 is 93 characters and wraps to about 6 uppercase lines on mobile. With the new hero buttons, the CTA now sits below the fold on phones. It's approved copy, so the option is to move "Estate Planning with Wills, Powers of Attorney & Personal Directives" into a styled subline.
- **Linking:** The page links to Executor twice but never to Probate.

### Estates & Probate `/estates-probate`
- **M (both):** The "Complimentary initial meeting" box is an H3 straight after the H1, which skips a heading level. Make it a `<p>` styled as a heading, or an H2.
- **M (both):** The page is a dead end for internal links; its only in-content link is `/#mediation`. Add links to /executor-services and /wills-estate-planning (see section 6).
- **L (both):** The title is 66 characters and the description 167. Trim both.
- Checked and correct:
  - Court of King's Bench and the Surrogate Rules
  - the filing-fee table (still has its verify note)
  - the complimentary meeting wording ("not legal advice, no obligation")

### Executor Services `/executor-services`
- **H1 and H2** (above).
- **M (both):** The page is a dead end. Its only link is to the external REALTOR® site. Add links to Wills (you name an executor in your will) and Probate (what an executor does).
- **L (pass 2):** The voice mixes "we" with "Geraldine", e.g. "*That's why we recommend naming an alternate*". Pick one.
- **L:** The description is 169 characters. Trim it.

### Contact `/contact`
- **M (both):** The intake form asks every visitor, including probate and executor enquirers, 7 will-planning questions (relationship status, children, disability, US property and so on). That's real friction for a grieving executor. Show those questions only when the service is "Wills…".
- **M (pass 2):** There's no general message field; the only free text is "Anything unusual we should know?". Add "How can Geraldine help?".
- **M (pass 2):** The confidentiality disclaimer sits *below* the Send button. Move it above.
- **M (both):** The contact-detail H3s come before the page's only H2, which skips a level. Make them H2s, or put the form first.
- **L (pass 2, opinion):** Phone is required, but the intro says "Most people email first". Consider making phone optional.

### About `/about` (new): see H4
- The title is 63 characters and the description 158. The H1 is fine.
- It reuses the hero sub-line as its intro, so a third page now opens with the same sentence.

### Blog `/blog` (new): see H5
- The description is generic. Fine once posts exist.

### 404
- **L (both):** It's Lovable's default page, outside the site layout: no header, footer, phone number or service links. Brand it, and confirm the server returns a 404 status.

---

## 5. Sitewide technical SEO

| Item | Status | Fix |
|---|---|---|
| noindex + robots `Disallow: /` | Correct for the draft | Remove at launch |
| Canonical tags | Missing | Add a self-referencing canonical per page |
| og:url, og:image, og:site_name, og:locale | Missing | Add them; use the logo or headshot as og:image |
| sitemap.xml | Missing | Add at launch |
| `lang="en"` | Should be `en-CA` | Change in `__root.tsx` |
| Google Fonts | Loads 6 families; only Oswald and Inter are used (Fraunces, Libre Baskerville, Nunito Sans and Source Sans 3 are left over from design options 1 and 3) | Load only Oswald 500–700 and Inter 400–600 |
| Root head | Declares its own title, description and robots tags | Confirm the rendered HTML has no duplicates |
| Internal content links | Use `<a>`, which reloads the full page | Use the router's `<Link>` |
| Skip link | Missing | Add "Skip to content" |
| Table captions | Missing on both tables | Add `<caption>` (can be visually hidden) |
| Banned-word test | No automated check | Add one to `review-rules.test.tsx` |
| Leftover class | `design-selector` on the draft label | Remove at launch |

## 5b. Schema (none in place yet)

| Page | Schema |
|---|---|
| Home | `LegalService`:<br>• name, url, telephone, email<br>• `areaServed`: Calgary plus the listed communities<br>• `openingHoursSpecification`: Mo–Fr 09:00–17:00<br>• no street address; she's a service-area business, so don't present the PO Box as a location<br>• `founder` → `Person` (Geraldine Hampton: jobTitle, alumniOf U of A and U of C, hasCredential QMed, memberOf Law Society of Alberta)<br>Also `WebSite`. |
| Wills, Probate, Executor | `Service` with `provider` → the LegalService; `BreadcrumbList`; `FAQPage` |
| About (if kept) | `ProfilePage` → `Person` |
| Contact | `ContactPage` |

Notes:
- **Don't** put geraldinehampton.com in `sameAs`; keep the two businesses separate.
- Google has shown FAQ rich results only for government and health sites since August 2023 ([Google Search Central, "Changes to HowTo and FAQ rich results"](https://developers.google.com/search/blog/2023/08/howto-faq-changes)). FAQPage markup still helps AI answers.

## 5c. Alt text

| Image | Alt | Verdict |
|---|---|---|
| Logo (header, footer) | "Estate Options" | OK. Inside the home link; "Estate Options home" would be slightly better. |
| Headshot, Home hero | "Geraldine Hampton, estate lawyer in Calgary" | Good |
| Headshot, Home "Meet Geraldine" | same | Set to `alt=""` (duplicate) |
| Headshot, About | same | Good |
| Decorative wedges, ticks, icons | `aria-hidden` | Correct |

---

## 6. Internal linking

**Current map:**
- **Global:** logo → /; nav (now 7 items); tel; Request a meeting → /contact; footer repeats the nav plus tel and mailto.
- **Home:** 3 "Learn more" links to the services; FAQ → Wills and Probate; external REALTOR® link; /contact ×2. Nothing links to /about.
- **Wills:** Executor ×2.
- **Probate:** /#mediation only.
- **Executor:** external REALTOR® link only.
- **Contact:** none.

**Add:**

| From | To | Anchor idea |
|---|---|---|
| Probate, "Choosing an executor" duties | /executor-services | "No one to name in your own will? See executor services" |
| Probate, closing section | /wills-estate-planning | "Make sure your own will is up to date" |
| Executor, "Who this is for" | /wills-estate-planning | "Naming an executor happens in your will" |
| Executor, "Two roles" | /estates-probate | "What an executor does" |
| Home, "Losing capacity" card | /wills-estate-planning (EPA section) | "Enduring powers of attorney" |
| Home, "Estate mediation" card | /contact | "Ask about mediation" |
| Home, "Meet Geraldine" | /about (if kept) | "More about Geraldine" |
| Home, 3 service cards | the 3 services | Descriptive anchors instead of "Learn more →" |

---

## 7. Checked and correct (both passes)

- **Copy and compliance**
  - Approved copy matches the brief, apart from the logged changes.
  - No banned words; REALTOR® carries the ® every time; no NE communities.
  - "Practises wills and estates exclusively" is used throughout.
- **Facts against the Client Overview**
  - Bar call 2007; practising since 2010; QMed 2019; LLB (U of A); BA (U of C); 12 years teaching at Chinook Learning.
  - Phone (calls only), both emails, the PO Box and hours.
  - Estates billed hourly; the regulator "no conflict" statement.
  - West Side list matches Geraldine's Oct 29 feedback.
- **Alberta terms**
  - Wills and Succession Act, adult interdependent partner, Court of King's Bench, Surrogate Rules (Alta Reg 130/1995).
  - CRA clearance certificate, personal representative, agent/attorney.
- **Structure and accessibility**
  - One H1 per page.
  - Contrast passes AA: black on brand blue 6.3:1; #555 on surface 6.8:1; red text 5.6:1; blue text 6.3:1.
  - FAQ accordion and mobile menu are accessible (aria-expanded, Escape returns focus).
  - New-tab hint on external links; intake labels and autocomplete are correct; reduced-motion is respected.
- **Forms** don't transmit anything (by design for the draft).
- **New interior hero buttons** (Call and Request a meeting): a good conversion addition.

---

## 8. Proposed fix round (Lovable, est. 2–4 credits)

1. **Copy:**
   - H2
   - Home step note, Home FAQ "may", REALTOR® line, Wills signing step, dangling "see", Executor "we" voice
   - punctuation consistency
   - new ReviewNotes (H1, Q3, Q4)
2. **About/Blog:** apply Andrew's decision (H4, H5).
3. **Compliance:**
   - footer disclaimer
   - /privacy placeholder page with a ReviewNote (Geraldine supplies or approves the text)
   - disclaimer on the Home form and above Send on Contact
4. **Forms:** required fields on the Home form; conditional will questions; "How can Geraldine help?" field.
5. **Linking:** everything in the section 6 table.
6. **Technical:**
   - fonts, `en-CA`, canonical/OG tags, skip link, LCP fix, heading levels, `<Link>`, table captions, branded 404
   - title and description trims
   - schema JSON-LD
   - banned-word test
7. **Then:** desktop and 375px visual check, either in Chrome where Lovable is signed in or from screenshots supplied by the user.

## Change log

| Date | Change |
|---|---|
| 2026-10-29 | Audit written: two passes plus a review of the new About/Blog pages. No fixes applied yet. |
| 2026-10-30 | Visual check through the Lovable share link (commit `9f1e606e`), at 1440px and 375px, on all 9 routes (including /privacy, /blog and a 404). See section 9. |
| 2026-10-30 | Fix round sent ([lovable-fix-round-2026-10-30.md](lovable-fix-round-2026-10-30.md)). Lovable commits: `5b1af7de` (full nav moved to the xl breakpoint, hamburger menu below 1280px) and `9f1e606e` (all 35 items). Verified from the diff: every item applied as specified, copy word for word, with no unrequested copy changes. Not verified: test run output, credits used, rendered visual check. |

---

## 9. Visual check (2026-10-30, share link, commit 9f1e606e)

The site was checked in a real browser at 1440px and 375px. Every page loaded.

**Passed**
- All 9 routes return HTTP 200; the unknown page returns a real 404, and the branded 404 renders.
- No horizontal scrolling at either width.
- One H1 on each page; one robots meta tag on each page.
- Canonical tags are correct.
- The JSON-LD parses on every page: LegalService, WebSite and FAQPage on Home; Service, BreadcrumbList and FAQPage on each service page; ProfilePage on About; ContactPage on Contact.
- The desktop header fits 6 nav items, the phone number and the CTA. On mobile, the hamburger menu opens correctly and includes the Request a meeting button.
- Contact form: picking Wills shows the 5 household questions (7 fields become 12); picking an estate hides them again.
- The only console errors are the 404s from the deliberate test URL.

**New findings**

| Severity | Page | Issue | Fix |
|---|---|---|---|
| M | Executor | At 375px, the "Your options compared" table is cramped: two narrow columns, with rows up to about 8 lines tall. | Below the sm breakpoint, show each row as a stacked card (option as the heading, consideration below it). |
| L | Wills, Probate | At 375px the H1 wraps to 6 and 5 lines. The first CTA lands at about 685px and 669px, so it's below the fold on short phones (667px tall). | Consider a smaller H1 size on mobile (text-3xl). The H1 copy is approved. |
| L | Home | In the Wills service card, the tax and trusts note sits below the "About wills & estate planning" link, so it reads after the call to action. | Move the note above the link. |
| L | Footer | Footer nav and email links are 21px tall. That passes WCAG 2.5.8 through spacing, but it's small for older users. | Add py-1.5 to footer links. |
| — | Preview only | The "Draft for review" label and the Lovable badge cover the bottom-left corner. | Both disappear at launch. |
