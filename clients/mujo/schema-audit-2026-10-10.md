# Mujo schema audit: FAQ, hub pages, Organization (2026-10-10)

> **Scope:** three items from Britt's email (FAQPage, hub pages as LocalBusiness, duplicate Organization).
> **Method:** crawled all 284 URLs in the Rank Math sitemaps (posts, pages, products, product categories, locations), parsed every JSON-LD block, and compared FAQ schema questions against the visible page text. Raw data: crawl scripts in the session scratchpad; re-run before fixing if more than a few weeks pass.
> **Status:** findings only. Nothing changed on the site.

## Headline findings

1. **The hand-coded schema lives inside page content** (a Custom HTML block at the bottom of each page, e.g. privacy policy, page ID 3). It is on **71 pages** and declares Mujo as a **LocalBusiness** on every one of them, and on 69 of them it says each page `isPartOf` the LocalBusiness (it should be part of the WebSite).
2. **45 of those 71 blocks contain ChatGPT leftovers** in public schema: `:contentReference[oaicite:0]{index=0}` inside descriptions. Several also have garbled characters (`â€”`, `â€™`) from a bad copy-paste. Google and AI crawlers read these. Fixing the hub/LocalBusiness issue removes most of them.
3. **FAQ schema is wrong more often than right.** Only 1 of 18 pages with FAQPage schema matches its visible FAQ. 12 blog posts have FAQ schema with no visible FAQ at all, and one product page's FAQ schema describes a different textbook.
4. **Duplicate Organization** is on 2 pages (homepage, Texas CTE funding), not site-wide. But the separate `#localbusiness` entity on 71 pages is the bigger duplication.

Context on FAQ rich results: since August 2023 Google only shows FAQ rich results for well-known government and health sites, so for Mujo FAQPage schema won't produce the expandable SERP feature. It's still worth having (accurate) for Google's understanding and AI answers, but a mismatched FAQ schema is a guidelines risk with no upside. Source: Google Search Central Blog, "Changes to HowTo and FAQ rich results", 8 August 2023. HowTo rich results were retired at the same time; 4 blog posts still carry HowTo schema (list below), which is harmless but dead weight.

---

## 1. FAQPage audit

### A. Visible FAQ, no FAQPage schema (add schema): 17 pages

| Page | Visible questions |
|---|---|
| /florida-marketing-curriculum-high-school/ | 5 |
| /high-school/ai-textbooks/foundations-artificial-intelligence/ | 4 |
| /high-school/business-textbooks/ai-for-business/ | 5 |
| /high-school/business-textbooks/entrepreneurship-fundamentals/ | 5 |
| /high-school/business-textbooks/principles-of-business/ | 5 |
| /high-school/digital-marketing-textbooks/ai-marketing-fundamentals/ | 4 |
| /high-school/digital-marketing-textbooks/creating-digital-media-content/ | 4 |
| /high-school/digital-marketing-textbooks/fashion-marketing-essentials/ | 4 |
| /high-school/digital-marketing-textbooks/foundations-of-marketing/ | 4 |
| /high-school/digital-marketing-textbooks/influencer-marketing-essentials/ | 4 |
| /high-school/digital-marketing-textbooks/online-marketing-fundamentals/ | 4 |
| /high-school/digital-marketing-textbooks/social-media-marketing/ | 4 |
| /high-school/digital-marketing-textbooks/sports-and-entertainment-marketing-essentials/ | 4 |
| /high-school/digital-marketing-textbooks/website-and-e-commerce-design-strategy/ | 4 |
| /higher-education/ai-textbooks/ (hub) | 7 |
| /higher-education/business-textbooks/ (hub) | 7 |
| /higher-education/ai-textbooks/prompt-engineering-curriculum/ | 6 |

Note: most high-school FAQs share the same 3 generic questions ("Can this material be integrated into high school curricula?", "What is the best way to learn more…"). Fine for visitors, but worth making each set more title-specific when schema is added.

### B. FAQPage schema that doesn't match the visible FAQ (rewrite from the visible Q&A): 5 pages

| Page | Schema Qs | Found on page | Problem |
|---|---|---|---|
| /higher-education/ai-textbooks/ai-literacy-healthcare/ | 5 | 0 | **Schema describes "Artificial Intelligence Accounting Principles"**, a different book (copy-paste). Page shows 7 different healthcare questions. |
| /higher-education/ai-textbooks/artificial-intelligence-literacy/ | 5 | 0 | Schema questions differ from the 5 visible ones. |
| /higher-education/business-textbooks/artificial-intelligence-accounting-principles/ | 5 | 0 | Schema questions differ from the 8 visible ones. |
| /higher-education/business-textbooks/artificial-intelligence-business-writing/ | 5 | 3 | Page shows 12 questions; schema has 5, 2 of them not on the page. |
| /higher-education/business-textbooks/artificial-intelligence-for-entrepreneurs/ | 5 | 0 | Visible FAQ is plain text (not toggles) with different wording. |

### C. FAQPage schema with no visible FAQ (remove schema, or add a visible FAQ section first): 12 blog posts

- /teacher-blog/best-seo-lesson-plans/
- /teacher-blog/chatgpt-atlas/
- /teacher-blog/digital-marketing-skills-every-high-school-graduate-should-have-in-2026/
- /teacher-blog/educators-guide-to-prompt-engineering-preparing-students-for-ai-driven-marketing/
- /teacher-blog/social-media-marketing-lesson-planning-college-university/
- /teacher-blog/social-media-marketing-textbook-selection-guide-2026/
- /teacher-blog/teach-seo/
- /teacher-blog/teach-website-design/
- /teacher-blog/teaching-digital-marketing-fundamentals/
- /teacher-blog/teaching-e-commerce-resources/
- /teacher-blog/the-ethical-landscape-of-ai-education/
- /teacher-blog/what-marketing-educators-need-to-know-about-meta-ai-grok-and-the-rise-of-social-ai-chatbots/

Recommendation: these are Brittni's posts, so the better fix is adding a short visible FAQ section (the Q&A already exists in the schema), not deleting the schema. Her call.

HowTo schema (retired by Google, harmless) on: /teacher-blog/educators-guide-to-prompt-engineering-…/, /teacher-blog/teach-seo/, /teacher-blog/teach-website-design/, /teacher-blog/teaching-digital-marketing-fundamentals/.

### D. FAQPage schema that matches: 1 page

- /texas/cte-funding/ (6 of 6 match). **But the page shows its FAQ twice**: 10 visible questions, several near-duplicates ("Does the $40 entitlement expire in August?" / "…at the end of August?"). Remove one set.

---

## 2. LocalBusiness / hub-page audit

All 71 pages below have the hand-coded block declaring `LocalBusiness` (`@id …/#localbusiness`, Vancouver address only, no Lahaina office). Rank Math's own page schema appears to be off on these pages. Fix = delete the hand-coded Custom HTML block and let Rank Math output the right type, setting the page schema type in Rank Math where needed.

### A. Hub pages: should be CollectionPage only (6)

| Page | Current | Fix |
|---|---|---|
| /higher-education/ | LocalBusiness + CollectionPage (`hasPart` = generic `Thing`s) | CollectionPage |
| /higher-education/ai-textbooks/ | same | CollectionPage (+ FAQPage, see 1A) |
| /higher-education/business-textbooks/ | same | CollectionPage (+ FAQPage, see 1A) |
| /high-school/ai-textbooks/ | same | CollectionPage |
| /high-school/digital-marketing-textbooks/ | same | CollectionPage |
| /teacher-resources/ | LocalBusiness + Service | CollectionPage |

Not affected (no hand-coded block): /high-school/business-textbooks/, /higher-education/digital-marketing-textbooks/.

### B. Textbook curriculum pages: should be WebPage about the book, not LocalBusiness (19)

High school: foundations-artificial-intelligence, ai-for-business, entrepreneurship-fundamentals, principles-of-business, influencer-marketing-essentials, social-media-marketing.

Higher ed: ai-literacy-healthcare, artificial-intelligence-literacy, generative-ai-for-business, prompt-engineering-curriculum, artificial-intelligence-accounting-principles, artificial-intelligence-business-administration, artificial-intelligence-business-writing, artificial-intelligence-for-entrepreneurs, artificial-intelligence-project-management, artificial-intelligence-sales-fundamentals, business-analytics-fundamentals, digital-marketing-fundamentals, public-relations-strategy-communications.

These currently mix LocalBusiness with Service or CollectionPage. A textbook page is neither a local business nor a service. Recommended: plain WebPage (Rank Math default) plus FAQPage where a visible FAQ exists. The Book schema we drafted belongs on the matching /shop/ product pages, not here (avoids two pages claiming the same product).

### C. Teacher-resource service pages: Service is fine, LocalBusiness is not (8)

/high-school/teacher-resource-cloud/, /higher-education/teacher-resource-cloud/, /teacher-resources/applied-ai-for-business-lesson-plans/, /teacher-resources/digital-marketing-lesson-plans/, /teacher-resources/exams-tests/, /teacher-resources/lms-integration/, /teacher-resources/student-learning-outcomes/, /teacher-resources/teacher-manuals/.

Fix: keep a Service type if wanted (Rank Math can do it), with `provider` = the Organization (`/#organization`), not `/#localbusiness`.

### D. Forms, thank-you, legal and other utility pages (38): just remove the block

/, /about/team/, /contact-rep/, /contact-us/thank-enquiring-mujo-learning-systems/, /contact-us/thank-you-texas/, /email-request-cte-examination-copies/, /email-request-high-school-examination-copies/, /email-request-higher-ed-examination-copies/, /email-schedule-content-and-pricing-review-meeting/, /free-instructor-sample/, /high-school-conference-request-copies-form/, /high-school-learning-outcomes-request/, /higher-ed-conference-request-copies-form/, /higher-ed-product-catalog/, /higher-education-curriculum/, /higher-education-learning-outcomes-request/, /nacc-ai-programs/, /new-release-email-request-higher-ed-examination-copies/, /new-release-email-request-higher-ed-learning-outcomes/, /new-release-high-school-examination-request/, /popular-adoptions-for-higher-ed-website-request/, /privacy-policy/, /purchase-order/, /qualified-high-school-discount-application/, /request-learning-outcome/, /schedule-call-alex/, /schedule-call-lexi/, /schedule-call-matt/, /schedule-content-and-pricing-program-review-meeting/, /schedule-demo/high-school/, /schedule-demo/higher-education/, /teacher-appreciation-week-giveaway-legal/, /teacher-resources/events-webinars/, /teacher-resources/request-learning-outcomes/, /terms-and-conditions/, /thank-enquiring-mujo-learning-systems/, /webinar-sign-up/, /website-link-newsletter-sign-up/.

Several of these (thank-you pages, form pages) arguably shouldn't be indexed at all; check their Rank Math robots setting while in there. The homepage and /about/team/ need the Organization fix in section 3 rather than a plain delete.

---

## 3. Duplicate Organization audit

### Pages where `/#organization` is defined twice (2)

| Page | Definition 1 | Definition 2 |
|---|---|---|
| / (homepage) | Rank Math: Organization, logo, 4 sameAs, legalName | Hand-coded: Organization + PostalAddress (Vancouver) + **LocalBusiness** (`/#localbusiness`) + **Person** Shawn Moore ("President, CEO, and Lead Author") + 7 sameAs incl. Pinterest, Instagram, Google Maps |
| /texas/cte-funding/ | Rank Math Organization | Hand-coded Organization (inside the page's own schema) |

The two homepage definitions disagree: different sameAs lists (Rank Math is missing Instagram and Pinterest; hand-coded is missing nothing but uses an old `ca.linkedin.com` URL), different URLs (`https://www.mujo.com` vs `…/`), and only the hand-coded one has the phone and address.

### Sitewide picture

- 154 pages: Rank Math Organization only (blog posts, products, categories). Fine once its details are completed.
- 71 pages: no Rank Math Organization, hand-coded `#localbusiness` instead (section 2). These are effectively a second, conflicting Mujo entity.
- 57 pages: no Organization at all (mostly pages with breadcrumbs only).

### Fix (one place, Rank Math)

1. Rank Math > Titles & Meta > Local SEO (or Knowledge Graph): name **Mujo Learning Systems**, legal name **Mujo Learning Systems Inc.**, logo, phone +1-888-536-6856, email, both addresses (Vancouver #602-1388 Homer St, BC V6B 6A7; Lahaina #A13-5295 Lower Honoapiilani Rd, HI 96761), founder Shawn Moore, and the full sameAs list (Facebook, Instagram, LinkedIn `www.linkedin.com/company/mujo-learning-systems/`, YouTube, X, Pinterest; drop the Google Maps link from sameAs).
2. Delete the hand-coded block on the homepage and the Organization node inside /texas/cte-funding/'s custom schema.
3. Delete the 71 LocalBusiness blocks (section 2). After that, every page points at one Organization.
4. Person schema for Shawn Moore: keep it on /about/ or /about/team/ only, referenced as `founder` from the Organization.

Rank Math's `/locations/` pages (Canada and USA offices) already carry Place/LocalBusiness-style schema with opening hours; those are the right home for office-level details and should stay.

---

## Effort and order (suggested)

1. Organization in Rank Math settings (once, via `wp-mujo`): small.
2. Delete hand-coded blocks: 71 page edits via `wp-mujo` (each is removing one Custom HTML block); set Rank Math schema type to CollectionPage on the 6 hubs and Service on the 8 resource pages. Medium. Do 2–3 pages first, check in Rich Results Test, then batch.
3. FAQ: rewrite the 5 mismatched schemas (B), add schema to the 17 pages (A) from their visible Q&A, de-duplicate Texas (D), and get Brittni's decision on the 12 blog posts (C). Medium.

All page-content changes go to Brittni for approval first (her standing rule).
