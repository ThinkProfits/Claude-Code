# Lovable fix round: 2026-10-30

This round applies the findings in [site-audit-2026-10-29.md](site-audit-2026-10-29.md).
- **User decision (Oct 30):** keep the About page, but give it its own content and link to it from Home.
- **Blog:** take it out of the nav and footer until posts exist.

The message below was sent to Lovable word for word.

---

Fix round from our site audit. Please apply everything below. Keep all copy in src/content (pages.ts and estate.ts) as now. Keep noindex and robots Disallow. Keep SHOW_REVIEW_NOTES on. Do not change any approved copy except where it's listed here.

## A. Navigation, About and Blog
1. Blog: keep the /blog route, but remove "Blog" from the header nav, mobile menu and footer nav. It should only be reachable by URL until articles exist.
2. About: keep "About" in the nav. Give the About page its own content, replacing the copy of the Home bio. Use this copy:
   - Title: "About Geraldine Hampton | Calgary Estate Lawyer"
   - Meta description: "Geraldine Hampton has practised wills and estates exclusively since 2010. Her background, credentials and how she works with clients across Calgary."
   - H1: "About Geraldine Hampton"
   - Intro: "Geraldine Hampton is a Calgary lawyer who has practised wills and estates exclusively since 2010, when she opened Estate Options."
   - Section H2 "Why wills and estates": "Geraldine went into law to help people, and she finds wills and estates work fascinating. Choosing one area of law, rather than adding wills to a general practice, means every file she handles is a will or an estate. She has kept up with wills and estates courses throughout her career, and taught Wills & Estates at Chinook Learning (Calgary Board of Education) for 12 years."
   - Section H2 "Experience": "Over her career Geraldine has prepared thousands of wills, enduring powers of attorney and personal directives, and handled hundreds of probates." Under this paragraph add a ReviewNote: "Please confirm you're comfortable stating these numbers. We've kept them general (thousands of documents, hundreds of probates) to match what you told us."
   - Section H2 "How she works": "You meet with Geraldine herself, not with a questionnaire or an assistant. She walks you through your options in plain language and leaves the decisions with you. Many clients meet with her at their own kitchen table; home visits are available across Calgary, and older and younger clients alike appreciate them."
   - Section H2 "Mediation": "Geraldine became an ADRIC Qualified Mediator (QMed) in 2019. She mainly mediates estate disagreements, helping families talk things through before they turn into court applications."
   - Section H2 "Credentials": reuse the shared credentials list.
   - Section H2 "Outside the office": "Away from her practice, you'll find Geraldine at the piano, on the badminton court, on the golf course or at the skating rink."
   - Keep the headshot (alt text unchanged) and MeetingButtons, and end with the standard ClosingCta. CTA title: "Talk to Geraldine". CTA text: "Call or send a message, and she'll arrange a time to meet — at your home or wherever suits you."
   - Add a ReviewNote near the top: "Your notes said no About page at launch. We've added one with fuller background, so the Home page can stay short. Let us know if you'd rather hold it for later."
3. Home "Meet Geraldine" section: keep only the first bio paragraph and the credentials list. Remove the second bio paragraph (the hobbies sentence now lives on About). Below the credentials, add a link to /about with the text "More about Geraldine", styled like the other underlined links.

## B. Copy fixes (exact)
4. Home "How it works", step 2 note: change it to "The complimentary estate meeting is introductory, not legal advice." Add a ReviewNote under the steps: "Is the first meeting for a will also complimentary, or is it billed? We've only said complimentary for estates."
5. Home FAQ 1: change the question to "What happens if I don't have a will?" In its answer, change "someone must apply to the court" to "someone may need to apply to the court".
6. Home FAQ "How often should I update my documents?": replace it with Q "What happens at the first meeting?" and A "For an estate, your first meeting is complimentary: Geraldine explains her process, what the estate is likely to require and her fees, so you can decide whether to go ahead. It's an introductory meeting, not legal advice. For wills and powers of attorney, she meets with you in person, often at your home, to talk through your family, what you own and your wishes."
7. Home step 2 body: change "what the estate requires, and her fees" to "what the estate is likely to require and her fees".
8. Home "Other ways", Estate transitions: change it to "When an estate includes a home, it helps that Geraldine is also a REALTOR®."
9. Home areasNote: append "Also: do you do home visits in High River and Okotoks? And should Westhills sit under West Side rather than Also serving?"
10. Wills page, "How it works", Signing step: change it to "You sign with Geraldine, and your documents are signed and witnessed as Alberta law requires."
11. Wills page, "Choosing your attorney": end the text with "If there's no one suitable, Geraldine can act for you." and make the link label "Learn about executor and attorney services" so it reads as its own line, not a dangling "see".
12. Executor page, "Why name a lawyer", bullet 2: change it to "Lawyers are regulated by the Law Society of Alberta". Remove the insurance wording.
13. Executor page compensation ReviewNote: append "(3) When you're named as attorney under an enduring power of attorney, who gives the lawyer's certificate of legal advice, since the certifying lawyer generally can't be the named attorney? (4) Does your professional liability insurance cover you when you act as executor or attorney? We've removed the insurance line until we hear back."
14. Executor FAQ "What if my executor dies before me?": change "That's why we recommend naming an alternate." to "That's why Geraldine recommends naming an alternate."
15. Home service cards: replace the three "Learn more →" links with descriptive text: "About wills & estate planning", "About estates & probate", "About executor services".

## C. Internal links (inline, as styled text links using the router Link)
16. Probate page, section "An executor's duties, step by step": after the list, add a link "No one to name as executor in your own will? See executor services" pointing to /executor-services.
17. Probate page, "Doing some of the work yourself" section: add a link "Make sure your own will is up to date" pointing to /wills-estate-planning.
18. Executor page, "Who this is for": after the bullets, add the link "You name your executor in your will — see wills & estate planning", pointing to /wills-estate-planning.
19. Executor page, "Two roles" section: add the link "What an executor does, step by step", pointing to /estates-probate.
20. Home "Other ways" cards:
    - "When a loved one is losing capacity": add a link "About enduring powers of attorney", pointing to /wills-estate-planning.
    - "Estate mediation": add a link "Ask about mediation", pointing to /contact.
21. Change internal links rendered in service-page.tsx Block to use the router's <Link> for internal hrefs. Keep <a target="_blank"> for external ones.

## D. Compliance
22. Footer: add a small line on every page: "The information on this website is general information, not legal advice. Contacting Estate Options doesn't create a lawyer-client relationship." Add a "Privacy" link to /privacy. Change the copyright to "© {current year} Estate Options".
23. Create /privacy using SiteLayout and InteriorHero, with noindex. Title "Privacy | Estate Options". H1 "Privacy". Body:
    - "Estate Options collects the personal information you choose to send through this website — such as your name, phone number, email and details about your situation — only to respond to your enquiry and to provide legal services you ask for."
    - "We don't sell or share your information for marketing. We keep it confidential and secure, and only as long as we need it for these purposes or as the law and Law Society of Alberta rules require."
    - "You can ask to see or correct the personal information we hold about you, or ask questions about how it's handled, by contacting Geraldine at geraldine@estateoptions.ca. Alberta's Personal Information Protection Act (PIPA) applies."
    - Add a ReviewNote: "This is placeholder privacy wording for your review. Please replace it with your own policy or approve this version before launch."
    Do not add /privacy to the main nav; footer link only.
24. Home short contact form:
    - make name and email required (with "(required)" text like on the Contact form)
    - add the same disclaimer as the Contact form, above the Send button
    - add "By sending, you agree to our privacy policy", linked to /privacy
25. Contact intake form:
    - Move the disclaimer above the Send button and add the same privacy line.
    - Add a textarea "How can Geraldine help?" (optional) right after the service select.
    - Show the relationship status, children, dependant with a disability, all assets in Alberta, and US property questions ONLY when the service is "Wills, powers of attorney & personal directives". Hide them for every other choice and when nothing is selected. Keep the litigation question visible for everyone.

## E. Technical SEO and accessibility
26. __root.tsx:
    - Set lang="en-CA".
    - Load Google Fonts for Oswald (500;600;700) and Inter (400;500;600) only; remove Fraunces, Libre Baskerville, Nunito Sans and Source Sans 3.
    - Remove the root-level title, description and robots meta if the child routes already provide them, so there are no duplicate tags in the rendered head.
27. Add a SITE_URL constant "https://estateoptions.ca" in src/content. In siteHead, add:
    - a canonical link (SITE_URL + path) per page
    - og:url, og:site_name "Estate Options" and og:locale "en_CA"
    - og:image and twitter:image pointing to the headshot as an absolute URL; twitter:card "summary_large_image"
    Pass the path into siteHead from each route.
28. Titles and descriptions:
    - Home description: "Geraldine Hampton has practised wills and estates exclusively since 2010. Wills, powers of attorney, probate and executor services, with home visits."
    - Wills title: "Wills Lawyer in Calgary | Wills, EPAs & Directives"
    - Wills description: "Calgary wills lawyer Geraldine Hampton prepares wills, enduring powers of attorney and personal directives in person, with home visits across Calgary."
    - Probate title: "Probate Lawyer in Calgary | Estate Administration"
    - Probate description: "Calgary probate and estate administration with Geraldine Hampton. Help for executors with courts, banks and Land Titles. Complimentary first estate meeting."
    - Executor description: "No one to name as executor? Calgary lawyer Geraldine Hampton can act as executor of your will or as attorney under your enduring power of attorney."
    - Contact title: "Contact Estate Options | Calgary Estate Lawyer"
    - Do not change any H1.
29. Home hero:
    - Remove the fade-up animation from the hero text block (it delays the main heading).
    - Add fetchPriority="high" to the hero headshot.
    - On the second "Meet Geraldine" headshot, set alt="" and loading="lazy".
30. Heading order:
    - Probate "Complimentary initial meeting" box: render the title as a styled <p> (same look), not an h3.
    - Contact page: render the ContactDetails headings as h2 there (same visual size), so the page doesn't skip from h1 to h3.
31. Add a visually hidden "Skip to content" link as the first focusable element, targeting <main id="main">.
32. Add a visually hidden <caption> to both tables: "Alberta probate court filing fees by estate value" and "Options for who can act as your executor".
33. 404 page: render it inside SiteLayout. H1 "Page not found". Text: "The page you're looking for isn't here. Try one of these instead:". Links to the three service pages and /contact, plus the phone number.
34. Schema JSON-LD (as head script tags of type application/ld+json, built from src/content):
    - Home: a LegalService with name "Estate Options", url SITE_URL, telephone "+1-403-483-2020", email geraldine@estateoptions.ca, and areaServed: City Calgary plus the community names from areaGroups. Also openingHoursSpecification Monday–Friday 09:00–17:00, priceRange omitted, and NO street address. Add founder: Person "Geraldine Hampton", jobTitle "Lawyer", alumniOf University of Alberta and University of Calgary, memberOf Law Society of Alberta, hasCredential "ADRIC Qualified Mediator (QMed)". Also add a WebSite object.
    - Wills, Probate, Executor: a Service (name = page H1, provider referencing the LegalService @id, areaServed Calgary), a BreadcrumbList (Home > page) and a FAQPage built from that page's FAQs.
    - Home: a FAQPage from the home FAQs.
    - About: a ProfilePage whose mainEntity is the Person.
    - Contact: a ContactPage.
    - Do not include geraldinehampton.com anywhere in the schema.
35. Tests: in review-rules.test.tsx, add a test that fails if any string in src/content contains these banned words (case-insensitive, whole words): specialist, specialize, specialty, expert, best, "peace of mind", easy, simple, simply, stress-free, guarantee, testimonial. Also add a test that "REALTOR" never appears without "®". Make sure all tests pass.

When done, list every file you changed and confirm each numbered item.

---

## Result (2026-10-30)

- **Commits:**
  - `5b1af7de`: header switches to the hamburger menu below 1280px, so 6 nav items fit.
  - `9f1e606e`: all 35 items.
- **Verified against the diff:** all 35 items applied, and the copy matches word for word. No other approved copy changed. Blog is removed from the nav and footer, but the route still exists. /privacy has noindex. The schema has no street address and no geraldinehampton.com. The intake form shows the will questions only when "Wills, powers of attorney & personal directives" is selected.
- **New tests:** a banned-word check across all content, a REALTOR® check, and a check for the conditional intake fields.
- **Not verified:**
  - Whether the tests pass. Lovable's run output wasn't captured.
  - Credits used.
  - The rendered look on desktop and at 375px.
  - The 404 HTTP status.
- **Known limitation:** the canonical tags, og:image and schema URLs point to https://estateoptions.ca. They resolve only once the site is live on that domain. That's expected, and the pages stay noindex for now.
