# Lovable brief: industry page rebuild (thinkprofits.com) (v2)

> **Status:** DRAFT v2, 2026-10-07. Replaces v1. **Phase 0 and the Phase 0 addendum are read-only and safe to send now. Phases 1–8 wait for Andrew's decisions** (audit section 11).
> **Project:** Lovable "Thinkprofits Rebuild" (`12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17`).
> **Based on:** [industry-pages-audit-2026-10-07.md](industry-pages-audit-2026-10-07.md) (v2). Keyword research is done (Google Ads Keyword Planner + GSC), so Lovable doesn't do any keyword research or write any copy.
> **Reusable:** the phase pattern below (inspect → fix the redirect basics → build empty page shells → redirects → clean up links → canonicals → paste in hand-written copy → verify) works for any Lovable site clean-up. Swap the tables to reuse it.
> **How to use:** paste one phase at a time and check the report before pasting the next. Messages already sent: v1 (audit + Phase 0) and the addendum (`lovable-message-phase0-addendum-2026-10-07.txt`).

---

## Phase 1: www redirect fix (needs Andrew's OK; independent of the rest)

```
Change the redirect from https://www.thinkprofits.com/* to https://thinkprofits.com/* so it returns HTTP 301 (permanent) instead of 302, keeping the full path and query string. Do the same for http://www.thinkprofits.com/*. Report back with the status codes of https://www.thinkprofits.com/ and https://www.thinkprofits.com/seo-services/ after the change.
```

---

## Phase 2: build the industry page shells and the hub (empty slots for hand-written copy)

```
Create 9 new industry pages under /industries/. Do NOT write marketing copy. Use the placeholders exactly as written; a person will write the final copy by hand. Do NOT publish any of these pages until I send the final copy (Phase 7). Keep them unpublished/draft, or noindex and out of the sitemap and nav, until then.

Pages (URL, then working H1 placeholder):
/industries/law-firms/ – [[H1: Law Firm SEO]]
/industries/plumbing/ – [[H1: SEO for Plumbers]]
/industries/hvac/ – [[H1: HVAC SEO]]
/industries/dental/ – [[H1: Dental SEO]]
/industries/hotels-hospitality/ – [[H1: Hotel & Hospitality Marketing]]
/industries/ecommerce/ – [[H1: Ecommerce SEO]]
/industries/manufacturing-industrial/ – [[H1: B2B, Manufacturing & Industrial SEO]]
/industries/home-services/ – [[H1: SEO for Contractors & Home Services]]
/industries/education/ – [[H1: SEO for Education]]

Each page uses this structure with placeholders:
- Hero: H1, [[SUBHEAD]], CTA to /contact/
- H2 [[What we do]]: three sub-sections: [[SEO]], [[AI search (AEO/GEO)]], [[Google Ads]]
- H2 [[Results]]: a proof block linking the case studies listed below
- H2 [[How we work]]: [[PROCESS]]
- H2 Pricing: link to the published tiers on /seo-services/, /aeo-services/ and /ppc-advertising/ (no new prices)
- H2 FAQ: [[FAQ]]
- Final CTA, contact form with Cloudflare Turnstile
- /industries/home-services/ only: add H2 sections with id anchors for #roofing, #electricians, #landscaping, #cleaning, #towing, #drainage, #fencing, #garage-door, #pest-control, #restoration, #moving, #auto-repair, each with a [[2–4 SENTENCES]] placeholder.

Case studies to link per page:
- law-firms: /case-study/thomas-associates/, /case-study/hoogbruin-company/
- plumbing: /case-study/john-sadler-plumbing-heating/, /case-study/lone-star-plumbing-heating/, /case-study/butler-plumbing-heating/
- hvac: /case-study/lone-star-plumbing-heating/, /case-study/butler-plumbing-heating/
- dental: /case-study/tsawwassen-family-dental/
- hotels-hospitality: /case-study/executive-hotels-resorts/, /case-study/liz-moore-destination-weddings/, /case-study/prestons-restaurant-lounge/
- ecommerce: /case-study/golf-ball-planet/, /case-study/mvp-athletic-supplies/
- manufacturing-industrial: /case-study/merit-kitchens/, /case-study/euro-rite-cabinets/, /case-study/qsd-inc/, /case-study/can-four-industrial/, /case-study/ccd-energy-services/
- home-services: /case-study/ultimate-fence/, /case-study/anago-of-vancouver/
- education: /case-study/sprott-shaw-college/, /case-study/mujo-learning-systems/

Internal links on every industry page: /industries/, /seo-services/, /aeo-services/, /ppc-advertising/, /contact/. Plumbing and HVAC link to each other. Ecommerce links to /ecommerce-website-design/.

Schema: Service + BreadcrumbList now; FAQPage only once real FAQ text is in.

Also rebuild /industries/ (keep URL, header, footer, design system) as the hub:
- H1 placeholder [[HUB H1]], intro [[HUB INTRO]]
- A card for each of the 9 industry pages (link + one-line placeholder)
- Section "Healthcare & clinics" [[PLACEHOLDER]] linking /industries/dental/
- Section "Professional services" [[PLACEHOLDER]] (accountants, immigration consultants)
- Keep "Don't see your industry?" with a link to /contact/
- Do not reuse any sentence from the old /aeo-services/<industry>/, /ppc-advertising/ppc-for-<industry>/ or /seo-services/local-seo/local-seo-<industry>/ pages.

Report back: the list of created pages, confirmation that none are published or indexable yet, and a screenshot of one shell.
```

---

## Phase 3: redirects (only once the new pages are live, and only if Phase 0 confirmed capacity)

```
Add permanent HTTP 301 server-side redirects (no JavaScript or meta refresh). Cover both the trailing-slash and no-slash versions of every "from" URL. Update existing rules in place where one already exists (marked "repoint"). After this, no redirect may point to another redirect.

TO /industries/law-firms/
/seo-services/local-seo/local-seo-law-firms/, /aeo-services/law-firms/, /ppc-advertising/ppc-for-law-firms/, /lawyer-seo/ (repoint)

TO /industries/plumbing/
/seo-services/local-seo/local-seo-plumbing/, /aeo-services/plumbing/, /ppc-advertising/ppc-for-plumbing/, /seo-for-plumbers (repoint), /plumbing-seo-company-toronto/ (repoint)

TO /industries/hvac/
/seo-services/local-seo/local-seo-hvac/, /aeo-services/hvac/, /ppc-advertising/ppc-for-hvac/

TO /industries/dental/
/seo-services/local-seo/local-seo-dentists/, /aeo-services/dentists/, /ppc-advertising/ppc-for-dentists/, /dentist-seo-services (repoint)

TO /industries/hotels-hospitality/
/seo-hotels-resorts/ (repoint)

TO /industries/ecommerce/
/seo-for-retail (repoint)

TO /industries/manufacturing-industrial/
/seo-for-manufacturing-companies/ (repoint)

TO /industries/education/
/seo-for-education/ (repoint)

TO /industries/home-services/
/seo-for-home-service-contractors/ (repoint)
/seo-services/local-seo/local-seo-roofing/, /aeo-services/roofing/, /ppc-advertising/ppc-for-roofing/
/seo-services/local-seo/local-seo-electricians/, /aeo-services/electricians/, /ppc-advertising/ppc-for-electrician/
/seo-services/local-seo/local-seo-landscaping/, /aeo-services/landscaping/, /ppc-advertising/ppc-for-landscaping/
/seo-services/local-seo/local-seo-cleaning/, /aeo-services/cleaning/
/seo-services/local-seo/local-seo-garage-door/, /aeo-services/garage-door/
/seo-services/local-seo/local-seo-pest-control/, /aeo-services/pest-control/
/seo-services/local-seo/local-seo-restoration/, /aeo-services/restoration/
/seo-services/local-seo/local-seo-home-remodeling/, /aeo-services/home-remodeling/
/seo-services/local-seo/local-seo-moving-companies/, /aeo-services/moving-companies/
/seo-services/local-seo/local-seo-auto-repair/, /aeo-services/auto-repair/, /ppc-advertising/ppc-for-auto-repair/

TO /industries/
/seo-services/local-seo/local-seo-med-spa/, /aeo-services/med-spa/, /ppc-advertising/ppc-for-med-spa/
/seo-services/local-seo/local-seo-dermatology/, /aeo-services/dermatology/
/seo-services/local-seo/local-seo-chiropractors/, /aeo-services/chiropractors/
/seo-services/local-seo/local-seo-physiotherapy/, /aeo-services/physiotherapy/
/seo-services/local-seo/local-seo-veterinarians/, /aeo-services/veterinarians/
/seo-services/local-seo/local-seo-accountants/, /aeo-services/accountants/

Then remove the old page entries/files for every redirected URL so they no longer render. If they share a template fed by a data list, remove the entries, not the template.

Report back: the rules added/changed, the total rule count before and after, and any chains fixed.
```

**Fallback if Phase 0 shows too little redirect capacity:** skip the 30 `/aeo-services/<industry>/` and `/ppc-advertising/ppc-for-<industry>/` rules for Tier 3 industries. Return HTTP 410 (gone) for those URLs instead, since they've earned essentially no clicks. Keep all the repoints and Tier 1 rules.

---

## Phase 4: remove every reference to the old pages

```
Using the Phase 0 link list, update every link to a URL redirected in Phase 3 so it points straight to its new destination, or remove it:
- Header/footer nav: add "Industries" → /industries/ (dropdown with the 9 industry pages if the design allows).
- /seo-services/local-seo/, /aeo-services/, /ppc-advertising/, /services/: replace the industry grids with links to the 9 /industries/ pages plus "See all industries" → /industries/.
- /sitemap/ (HTML) and sitemap.xml: remove old URLs; add /industries/ and the 9 industry pages (trailing slash).
- llms.txt: remove old URLs; add /industries/ and the 9 pages.
- Blog posts: update in-content links to point at the final destination.
- Schema: remove Service/OfferCatalog entries for removed pages.
Report back: every file changed and what changed.
```

---

## Phase 5: trailing slash and canonicals (site-wide)

```
1. Every page's canonical uses the trailing-slash URL.
2. The no-slash version of every page returns 301 to the slash version (not a 200 duplicate).
3. All internal links use the trailing-slash version.
Test and report status + canonical for: /ppc-advertising, /aeo-services/geo, /industries/plumbing, /seo-services/local-seo, /digital-news/how-long-should-blog-post-be-seo-ai-2026
```

---

## Phase 6: titles and meta descriptions (after Andrew approves)

Primary keywords come from audit section 8. Nothing here promises a result.

| URL | Title (≤60 chars) | Meta description (≤155 chars) |
|---|---|---|
| /industries/law-firms/ | Law Firm SEO & Marketing in Vancouver, BC \| ThinkProfits | SEO, AI search and Google Ads for Canadian law firms. See our family law and personal injury results. Month-to-month, Vancouver since 1996. |
| /industries/plumbing/ | SEO for Plumbers & Plumbing Marketing \| ThinkProfits | SEO, Google Ads and AI search for plumbing companies. See our John Sadler, Lone Star and Butler results. Month-to-month, Vancouver since 1996. |
| /industries/hvac/ | HVAC SEO & HVAC Marketing Agency \| ThinkProfits | HVAC SEO, Google Ads and AI search planned around heating and cooling seasons. Proven with plumbing & heating clients. Vancouver since 1996. |
| /industries/dental/ | Dental SEO & Dental Marketing \| ThinkProfits | Dental SEO, Google Ads and AI search for clinics that want more new patients. See our Tsawwassen Family Dental work. Vancouver since 1996. |
| /industries/hotels-hospitality/ | Hotel SEO & Hospitality Marketing \| ThinkProfits | SEO, Google Ads and AI search for hotels, resorts and restaurants. See our Executive Hotels & Resorts results. Vancouver agency since 1996. |
| /industries/ecommerce/ | Ecommerce SEO Agency & Shopify SEO \| ThinkProfits | Ecommerce and Shopify SEO, Google Shopping and AI search. See our Golf Ball Planet and MVP Athletic results. Vancouver agency since 1996. |
| /industries/manufacturing-industrial/ | B2B SEO for Manufacturers & Industrial \| ThinkProfits | SEO, Google Ads and AI search for manufacturers and industrial suppliers. See our Merit Kitchens and QSD results. Vancouver since 1996. |
| /industries/home-services/ | SEO for Contractors & Home Services \| ThinkProfits | SEO, Google Ads and AI search for contractors and trades: roofing, electrical, landscaping and more. Month-to-month. Vancouver since 1996. |
| /industries/education/ | SEO for Schools & Colleges \| ThinkProfits | SEO, Google Ads and AI search for colleges, schools and education providers. See our Sprott Shaw College results. Vancouver since 1996. |

Before using these: get permission to name each client. If permission isn't given, swap in a generic proof line.

```
Set these exact title tags and meta descriptions on the pages listed. Don't edit the wording.
[PASTE TABLE]
```

---

## Phase 7: paste in the final copy (once per page)

```
Here is the final approved copy for <URL>. Paste it into the placeholders exactly as written. Do not edit, shorten, expand or "improve" it, and keep the H-tags as marked. If something doesn't fit the layout, tell me instead of rewriting it. Then add FAQPage schema from the FAQ section, make the page indexable, add it to sitemap.xml and nav, and publish.

[PASTE HAND-WRITTEN COPY]
```

---

## Phase 8: verification

```
Run and report a pass/fail table:
1. Every Phase 3 "from" URL (slash and no-slash) returns 301 in one hop to its destination.
2. Each published /industries/ page returns 200, has a self-referencing trailing-slash canonical, is indexable, and is in sitemap.xml.
3. No redirected URL appears in sitemap.xml, llms.txt, nav, footer, /sitemap/ or any internal link.
4. None of these phrases appear anywhere on the site: "Failure-Mode Answer Architecture", "training and retrieval set", "Reddit threads", "Q&A seeding", "368,000".
5. https://www.thinkprofits.com/ returns 301.
6. Contact forms on the new pages submit (Turnstile present).
```

After a pass: request indexing for `/industries/` and each published page in GSC. Then check GSC Pages ("Not found (404)", "Page with redirect", "Duplicate without user-selected canonical") weekly for 6 weeks.
