# Lovable brief: industry page clean-up (thinkprofits.com)

> **Status:** DRAFT v0.1, 2026-10-07. **Don't paste into Lovable until Andrew has approved the decisions in section 4 of the audit.**
> **Project:** Lovable "Thinkprofits Rebuild" (`12fc0c4c-0a7a-4dbb-ae43-0ad0e1c21a17`).
> **Based on:** [industry-pages-audit-2026-10-07.md](industry-pages-audit-2026-10-07.md). Keyword research is already done (Google Ads Keyword Planner + GSC), so Lovable doesn't need to do any.
> **Reusable:** the prompt structure below (inventory → safety checks → hub → redirects → clean-up → slots for hand-written copy → verification) works for any Lovable site clean-up. Swap the tables to reuse it.
> **How to use:** paste one phase at a time. Each phase ends with a "report back" step. Check the report before pasting the next phase.

---

## Phase 0: check before you change anything (paste first)

```
We are cleaning up the industry service pages on thinkprofits.com. Before changing anything, inspect the project and report back. Do NOT edit any files in this phase.

1. REDIRECTS: Tell me exactly how redirects are served on this site today (Encited, a redirects file, TanStack/SSR route config, Cloudflare, or something else). Show me the file or config that holds them and count how many redirect rules exist. Tell me whether the site returns a real HTTP 301 status or a client-side redirect.
2. INVENTORY: List every route/file that renders these pages, and whether each is a separate file or one shared template fed by data:
   - /aeo-services/<industry>/ (21 industries)
   - /ppc-advertising/ppc-for-<industry>/ (10 industries)
   - /industries/
3. REFERENCES: For each of the 31 industry URLs, list every place it is linked from: header/footer nav, /industries/, /aeo-services/, /ppc-advertising/, /services/, the HTML sitemap page (/sitemap/), sitemap.xml, llms.txt, blog posts, schema/JSON-LD.
4. TRAILING SLASH: Fetch /ppc-advertising/ppc-for-landscaping and /ppc-advertising/ppc-for-landscaping/ (no slash and slash). Report the HTTP status and the <link rel="canonical"> of each. Do the same for /aeo-services/accountants and /aeo-services/accountants/.
5. BACKUP: Confirm the current version is saved in Lovable history so we can roll back, and tell me the version/commit name.

Report back with all five answers. Don't fix anything yet.
```

---

## Phase 1: build the industries hub (paste after Phase 0 checks out)

```
Update the /industries/ page into the single hub for all industries. Keep the existing URL, header, footer and design system. Do NOT generate new marketing copy. Use the placeholder text exactly as written below so that a person can write the final copy by hand.

Structure:
- H1: "Industries We Work With" (placeholder; final H1 to be supplied)
- Short intro paragraph: [[HUB INTRO: written by Francis]]
- Section "Industries with dedicated pages". One card per industry below, linking to its pages:
  - Plumbing: /aeo-services/plumbing/ and /ppc-advertising/ppc-for-plumbing/
  - HVAC: /aeo-services/hvac/ and /ppc-advertising/ppc-for-hvac/
  - Dentists: /aeo-services/dentists/ and /ppc-advertising/ppc-for-dentists/
  - Electricians: /aeo-services/electricians/ and /ppc-advertising/ppc-for-electrician/
  - Landscaping: /ppc-advertising/ppc-for-landscaping/
  - [ROOFING and LAW FIRMS go here ONLY if I confirm they are kept. Otherwise they go in the next section.]
- Section "Other industries we support". One short block per industry, each with its own H3 and an id anchor (e.g. id="garage-door"). Each block body is the placeholder [[2–4 SENTENCES: written by hand]] plus a link to the case study where one is listed:
  - Cleaning (link /case-study/anago-of-vancouver/)
  - Home Remodeling (link /case-study/merit-kitchens/ and /case-study/euro-rite-cabinets/)
  - Accountants
  - Moving Companies
  - Restoration
  - Pest Control
  - Garage Door
  - Auto Repair
  - Med Spas
  - Dermatology
  - Chiropractors
  - Physiotherapy
  - Veterinarians
- Each block links to /aeo-services/, /seo-services/ and /ppc-advertising/ with one line: "Ask us about SEO, AI search or PPC for your business" linking to /contact/.
- Section "Don't see your industry?" Keep the existing section.

Rules:
- Do NOT reuse any sentences from the old /aeo-services/<industry>/ pages.
- Do NOT add FAQ schema to the hub unless I supply real FAQ text.
- Keep the existing Organization/ProfessionalService schema. Add a BreadcrumbList.
- Make sure the hub is in sitemap.xml with a self-referencing canonical (with trailing slash).

Report back: a screenshot of the page and the list of anchors created.
```

---

## Phase 2: redirects (paste only after Phase 0 confirms how redirects work and that there's room)

```
Add permanent (HTTP 301) redirects for the following URLs. Add BOTH the trailing-slash and no-trailing-slash version of each "from" URL. Use whatever redirect mechanism you identified in Phase 0. Do NOT use a client-side/JavaScript redirect or a meta refresh.

From → To
/aeo-services/garage-door/ → /industries/
/aeo-services/auto-repair/ → /industries/
/ppc-advertising/ppc-for-auto-repair/ → /ppc-advertising/
/aeo-services/med-spa/ → /industries/
/ppc-advertising/ppc-for-med-spa/ → /ppc-advertising/
/aeo-services/moving-companies/ → /industries/
/aeo-services/pest-control/ → /industries/
/aeo-services/restoration/ → /industries/
/aeo-services/dermatology/ → /industries/
/aeo-services/chiropractors/ → /industries/
/aeo-services/physiotherapy/ → /industries/
/aeo-services/veterinarians/ → /industries/
/aeo-services/accountants/ → /industries/
/aeo-services/cleaning/ → /industries/
/aeo-services/home-remodeling/ → /industries/
/aeo-services/landscaping/ → /ppc-advertising/ppc-for-landscaping/
[ONLY IF I CONFIRM ROOFING GOES TO THE HUB]
/aeo-services/roofing/ → /industries/
/ppc-advertising/ppc-for-roofing/ → /ppc-advertising/
[ONLY IF I CONFIRM LAW FIRMS GO TO THE HUB]
/aeo-services/law-firms/ → /industries/
/ppc-advertising/ppc-for-law-firms/ → /ppc-advertising/

Then:
1. Delete the page content/data entries for those industries so they no longer render at their old URLs. If one shared template is driven by a data list, remove those entries from the list. Don't delete the template, because the kept pages use it.
2. Make sure no redirect points to another redirect (no chains). If an older redirect points TO any of these URLs, update it to point straight to the new destination.

Report back: the redirect rules you added, the total redirect count before and after, and any chains you fixed.
```

---

## Phase 3: remove every reference to the removed pages

```
Using the reference list from Phase 0, remove or update every link to the URLs redirected in Phase 2:
- Header and footer navigation: remove them.
- /aeo-services/ and /ppc-advertising/ industry grids: remove the removed industries and keep only the kept ones. Add one link "See all industries we work with" pointing to /industries/.
- /services/ and the HTML sitemap page (/sitemap/): remove them.
- sitemap.xml: remove them. Kept pages must be listed with the trailing slash only.
- llms.txt: remove them and add /industries/ if it's missing.
- Blog posts: point any in-content link to the new destination from the Phase 2 table (don't leave links that go through a redirect).
- Schema/JSON-LD: remove any OfferCatalog/Service entries for removed industries.

Report back: a list of every file changed and what changed in it.
```

---

## Phase 4: trailing slash and canonicals (site-wide)

```
Make trailing slashes consistent across the whole site:
1. Every page's canonical URL uses the trailing-slash version (e.g. https://thinkprofits.com/ppc-advertising/ppc-for-landscaping/).
2. The no-slash version of every page returns a 301 to the slash version (not a 200 with the same content).
3. All internal links use the trailing-slash version.

Test and report the status code and canonical for these:
/ppc-advertising/ppc-for-landscaping
/ppc-advertising/ppc-for-dentists
/ppc-advertising/ppc-for-auto-repair
/ppc-advertising/ppc-for-hvac
/aeo-services/accountants
/aeo-services/landscaping
/aeo-services/cleaning
/digital-news/how-long-should-blog-post-be-seo-ai-2026
```

---

## Phase 5: prepare the kept pages for hand-written copy

Kept pages (adjust if roofing/law are confirmed):
`/aeo-services/plumbing/`, `/aeo-services/hvac/`, `/aeo-services/dentists/`, `/aeo-services/electricians/`, `/ppc-advertising/ppc-for-plumbing/`, `/ppc-advertising/ppc-for-hvac/`, `/ppc-advertising/ppc-for-dentists/`, `/ppc-advertising/ppc-for-electrician/`, `/ppc-advertising/ppc-for-landscaping/`.

```
For the kept industry pages listed below, convert each page from the shared template into an individual page that takes its own copy. Do NOT write or rewrite any marketing copy yourself. A person will write it by hand and send it to you.

For each kept page:
1. Keep the URL, design system, header, footer, contact form (with Cloudflare Turnstile) and pricing-tier link.
2. Replace the body with this section structure, each with a placeholder:
   - Hero: H1 [[H1]], subhead [[SUBHEAD]], CTA button to /contact/
   - "What we do for <industry> businesses": [[WHAT WE DO]]
   - "Proof": [[PROOF BLOCK: client, what we did, sourced result]]
   - "How it works": [[PROCESS]]
   - "Pricing": link to the relevant pricing section on /aeo-services/ or /ppc-advertising/
   - FAQ: [[FAQ: unique questions per page]]
   - Final CTA
3. Remove from these pages: the shared "What We Do" six-block section, the shared FAQ, the "Related Reading" block (the Lovable canonical QA and entity checklist posts) and any text that mentions Reddit, "training set" or conversion claims.
4. Internal links on each page: the parent service page (/aeo-services/ or /ppc-advertising/), the sibling page for the same industry (AEO↔PPC), /industries/, and the case study when I supply it.
5. Set the title and meta description to the values below, exactly as given.
6. FAQPage schema: only output it once real FAQ text is in place. No schema for placeholder text.
7. Do not publish a page while it still shows placeholders. Keep the current live version until I send the final copy (Phase 6), then publish both changes together.

Title / meta description values:
[PASTE FROM THE TABLE BELOW AFTER ANDREW APPROVES]

Report back: a screenshot of one converted page and confirmation that no template text remains on any kept page.
```

**Title and meta drafts (for Andrew to approve).** Primary keyword is from the audit's section 6; intent is commercial (hiring an agency).

| Page | Title (≤60 chars) | Meta description (≤155 chars) |
|---|---|---|
| /aeo-services/plumbing/ | SEO & AI Search for Plumbers \| ThinkProfits | Local SEO and AI search for plumbing companies, from the Vancouver agency behind John Sadler and Vision Plumbing's marketing. Month-to-month. |
| /ppc-advertising/ppc-for-plumbing/ | Google Ads for Plumbers \| ThinkProfits | Google Ads and Local Services Ads for plumbing companies. Calls tracked, no ad-spend markup, month-to-month. Vancouver agency since 1996. |
| /aeo-services/hvac/ | SEO for HVAC Companies & AI Search \| ThinkProfits | SEO and AI search for HVAC contractors, built around heat-pump, furnace and rebate searches. Vancouver agency since 1996. Month-to-month. |
| /ppc-advertising/ppc-for-hvac/ | HVAC Marketing: Google Ads & LSA \| ThinkProfits | Google Ads and LSA for HVAC companies, planned around seasonal demand. Calls tracked, no ad-spend markup. Vancouver agency since 1996. |
| /aeo-services/dentists/ | SEO for Dentists & AI Search \| ThinkProfits | Dental SEO and AI search for clinics that want more new-patient calls. See our Tsawwassen Family Dental work. Vancouver agency since 1996. |
| /ppc-advertising/ppc-for-dentists/ | Dental Google Ads Management \| ThinkProfits | Google Ads for dental clinics: new-patient campaigns, call tracking, no ad-spend markup. Month-to-month. Vancouver agency since 1996. |
| /aeo-services/electricians/ | SEO for Electricians & AI Search \| ThinkProfits | SEO and AI search for electrical contractors. Local rankings, Google Business Profile and AI answers. Vancouver agency since 1996. |
| /ppc-advertising/ppc-for-electrician/ | Electrician Marketing: Google Ads \| ThinkProfits | Google Ads and LSA for electrical contractors. Calls tracked, no ad-spend markup, month-to-month. Vancouver agency since 1996. |
| /ppc-advertising/ppc-for-landscaping/ | Landscaping Marketing: Google Ads \| ThinkProfits | Google Ads for landscaping and hardscaping companies, planned around the season. Calls tracked, month-to-month. Vancouver agency since 1996. |

Before using these: confirm we may name John Sadler, Vision and Tsawwassen Family Dental. If not, swap in a generic proof line. No meta promises a result.

---

## Phase 6: paste in the final copy (repeat once per page)

```
Here is the final, approved copy for <URL>. Paste it into the placeholders exactly as written. Don't edit, shorten, expand or "improve" the wording. Keep the H-tags I've marked. If anything doesn't fit the layout, tell me instead of rewriting it. Once it's in, output FAQPage schema from the FAQ section and publish.

[PASTE HAND-WRITTEN COPY]
```

---

## Phase 7: final verification (paste last)

```
Run these checks and report a pass/fail table:
1. Each redirected URL (slash and no-slash) returns HTTP 301 in one hop to its destination.
2. Each kept page returns 200, has a self-referencing trailing-slash canonical, is indexable (no noindex), and appears in sitemap.xml.
3. No removed URL appears in sitemap.xml, llms.txt, nav, footer, the /sitemap/ page or any internal link.
4. No page on the site still contains the shared template phrases "Failure-Mode Answer Architecture", "Speakable Schema" blocks copied per industry, "training and retrieval set", or "Reddit threads".
5. /industries/ renders every anchor from Phase 1.
6. Contact forms on kept pages still submit (Turnstile present).
```

After Lovable reports a pass: request indexing for `/industries/` and each kept page in GSC, then check GSC Pages → "Not found (404)" and "Page with redirect" weekly for 4–6 weeks.
