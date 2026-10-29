# Estate Options: full site build brief (v1)

> **Status:** v1, 2026-10-29. Geraldine picked **design option 2 (Bold Modern)** on Oct 29 (Slack #estate-options, Andrew 9:58 am CST). Andrew asked for the site to be fleshed out for her content review.
> **Lovable project:** Estate Options Design Studio (`69c1b714-db52-47cf-b5b5-0dc70974ab8c`), Shawn's workspace. Before this build, HEAD was `b253bb72f6e17e37a49703d0519f1e96834774e0`. Options 1 and 3 can be recovered from that commit.
> **Sources:** Client Overview (Drive `1P3xEXfWEROi7c13clV6R1HNkL29WN5-KKmC7NfT6urw`, includes the Oct 29 West Side note); **APPROVED** keyword sheet (Drive `1CoFEJMVF16O91ynVU6ueYz0H6ZOGagmla_ltOuJl-6A`); must-have sections in [keyword-research-draft-2026-10.md](keyword-research-draft-2026-10.md), section 3; the design brief in [lovable-design-options-brief-2026-10-23.md](lovable-design-options-brief-2026-10-23.md).
> **Reusable:** the "chosen option becomes the site, plus a review-note component" pattern below works for any Lovable build where the client picked from design options.

## Changes from the approved sheet vs our draft (check before writing)
- The Executor Services H1 is now **"Professional Executor Services in Calgary"**. Our draft had "A Lawyer to Act as Your Executor or Attorney in Calgary".
- The approved sheet adds broad secondaries: **executor** (260), **executor of will** (140), **power of attorney** (590), **wills** (1,000). These are tracked only, used naturally, and not targeted as primaries.
- "best wills and estate lawyers calgary" is tracked only. Never put "best" in the copy.

## Geraldine's Oct 29 feedback
- Add the line from option 3, *"I'll meet you where you're comfortable – often at your kitchen table."*, to option 2.
- Keep the fees treatment as it is in option 2.
- Name the **West Side** as well as NW Calgary. West Side districts: Coach Hill, Strathcona Park, Christie Park, Signal Hill, Aspen Woods, Wentworth, Westsprings, Spring Bank Hill, Crestmont, Artists View Park West, Cougar Ridge, Glamorgan.

## Open items shown as review notes on the site (in a visible "Note for Geraldine" box)
1. Executor compensation: percentage or hourly? This is still open from our Oct 16 question 2.
2. Law Society of Alberta disclosure when a lawyer drafts a will that names herself as executor. Also open from question 2.
3. Wording for the REALTOR® bridge on the Executor page. She acts as executor and may also be the listing agent, so she needs to confirm the wording.
4. The Alberta probate filing fee table needs checking against the current Surrogate Rules before launch.
5. Area list: "Christie Estates" was dropped because Christie Park covers it. Foothills Estates is kept under NW, as her overview lists it.
6. All FAQ and explainer answers are draft legal copy for her review.

---

## Message sent to Lovable

The text below was sent verbatim.

```
FULL SITE BUILD — Estate Options. Geraldine chose Design Option 2 (Bold Modern). Turn option 2 into the real 5-page site for her content review. Keep option 2's look exactly (Oswald-style condensed uppercase headings, logo blue wedge hero, angled section dividers, red ticks, black buttons, brand palette tokens already in styles.css). Do not redesign.

STRUCTURE
- Routes: "/" (Home), "/wills-estate-planning", "/estates-probate", "/executor-services", "/contact".
- Delete the chooser page and the option-1 and option-3 routes, and the option-2 route once its design is moved to "/". Remove the "Design option X of 3" DraftLabel and the section-number toggle. Replace with a small fixed corner label: "Draft for review · not live".
- Move option 2's header and footer into shared layout components used by every page. Nav links go to the real routes (header, mobile menu, footer). Active page gets an underline/red accent. Logo links to "/".
- Header CTA text changes from "Book a meeting" to "Request a meeting" (there is no booking calendar) and links to /contact.
- Every page: its own <title>, meta description, robots "noindex, nofollow", og tags; exactly one H1; Canadian English. Keep robots.txt Disallow: /.
- Interior pages use option 2's styling: a blue wedge hero band with the H1 (black text on brand blue) and a short intro, then content sections alternating white / surface, the angle-top dividers, RedTick above H2s, FAQ accordion (reuse Faq component but make it accept a list of items per page), and a closing CTA band (phone + "Request a meeting" → /contact).
- Add a ReviewNote component: a dashed 2px border box in a soft yellow (#FFF6D6 bg, #8A6D00 text, AA contrast), label "Note for Geraldine:". Controlled by one constant SHOW_REVIEW_NOTES = true in src/content so we can switch all of them off before launch.
- Put all copy in src/content (one file per page is fine). Copy below is final draft wording — use it as written; don't add claims, stats, testimonials or awards.

COMPLIANCE (hard rules — scan for these before finishing): never use "specialist", "specialize/specializes/specializing", "specialty", "expert", "best", "peace of mind", "easy", "simple", "simply", "stress-free", "guarantee". REALTOR® always with ®. No testimonials or reviews. No NE Calgary.

============ HOME ("/") ============
Title: Estate Lawyer in Calgary | Geraldine Hampton | Estate Options
Description: Geraldine Hampton has practised wills and estates exclusively since 2010. Wills, powers of attorney, probate and executor services, with home visits across Calgary.
Keep option 2's home sections and order. Changes:
1. Hero: keep H1 "Estate Lawyer in Calgary" and the subhead. Under the subhead, before the buttons, add a pull quote styled for option 2 (red tick or left red bar, larger italic-free medium weight):
   "I'll meet you where you're comfortable – often at your kitchen table."  — Geraldine Hampton
   Hero buttons: "Call 403-483-2020" (tel:) and "Request a meeting" (/contact).
2. Services cards: each card links to its page with a "Learn more →" link (Wills & Estate Planning → /wills-estate-planning, Estates & Probate → /estates-probate, Executor Services → /executor-services). Keep the featured black Executor card. Add one line to the Executor card: "A dedicated service for people with no one to appoint."
3. "Other ways Geraldine helps": give the mediation item id="mediation" (other pages link to /#mediation). Keep the four items and the REALTOR® link (https://geraldinehampton.com, new tab).
4. Meet Geraldine bio (replace):
   "Geraldine has practised wills and estates exclusively since 2010, when she opened Estate Options. Clients meet with her personally — not with a questionnaire or an assistant — and she walks them through their options in plain language, often at their own kitchen table.
   She was called to the Alberta Bar in 2007, is an ADRIC Qualified Mediator, and taught Wills & Estates at Chinook Learning for 12 years. Away from her practice, you'll find her at the piano, on the badminton court, on the golf course or at the skating rink."
   Keep the credentials list.
5. Areas we serve (replace content, keep option 2 chip styling, three labelled groups):
   Intro: "Estate Options started on Calgary's West Side in 2010, and many of Geraldine's clients still live there. Today she works with clients across Calgary, with home visits throughout the city."
   Group "Northwest Calgary": Varsity, Edgemont, Scenic Acres, Dalhousie, Silver Springs, Brentwood, Charleswood, Collingwood, Foothills Estates, Hawkwood, Briar Hill, Capitol Hill, Mount Pleasant
   Group "West Side": Coach Hill, Strathcona Park, Christie Park, Signal Hill, Aspen Woods, Wentworth, Westsprings, Spring Bank Hill, Crestmont, Artists View Park West, Cougar Ridge, Glamorgan
   Group "Also serving": Westhills, Lake Bonavista, High River, Okotoks
   ReviewNote: "We removed 'Christie Estates' because Christie Park covers it, and kept Foothills Estates under Northwest as listed in your notes. Let us know if either should move."
6. Fees: keep exactly: "Fees depend on the work involved. Many planning services are fixed-fee — contact us for the current schedule."
7. FAQ: keep the four existing Q&As; add a link at the end of the first answer "Read more about wills" → /wills-estate-planning and at the end of the probate answer "Read more about probate" → /estates-probate.
8. Contact strip: keep the short form; add a line under it: "Prefer a longer intake form? Visit the contact page." linking /contact.

============ WILLS & ESTATE PLANNING ("/wills-estate-planning") ============
Title: Wills Lawyer in Calgary | Wills, EPAs & Personal Directives | Estate Options
Description: Calgary wills lawyer Geraldine Hampton prepares wills, enduring powers of attorney and personal directives in person, with home visits. Practising wills and estates exclusively since 2010.
H1: Wills Lawyer in Calgary: Estate Planning with Wills, Powers of Attorney & Personal Directives
Intro: Your will, enduring power of attorney and personal directive work together. They say who receives what, who looks after your finances and personal care if you can't, and who would raise your children if you're not there. Geraldine prepares all three with you in person — often in your own home.
Clarifier box (bordered, right after intro): "A note on estate planning: here, estate planning means wills, powers of attorney and personal directives. Estate Options doesn't provide tax planning or trusts, and Geraldine is happy to work alongside your accountant or tax lawyer."

H2: Wills
 H3: Why you need a will
 A will names who receives your estate, who manages it (your executor) and who you'd want to raise your minor children. Without one, those decisions are made for you.
 H3: What happens in Alberta without a will
 If you die without a will, Alberta's Wills and Succession Act decides who inherits, using a set formula based on your spouse or adult interdependent partner and your children. Someone has to apply to the court to be appointed administrator, and no one has been chosen in advance to care for minor children. The result can be quite different from what you would have wanted.
 H3: What we'll talk about
 - What you own, and whether any of it is outside Alberta — including property in the United States
 - Who you'd like to benefit, and how
 - Who should act as your executor, and an alternate
 - Guardians for your minor children
 - Support for a dependant with a disability
 - Anything unusual about your family or your assets

H2: Enduring power of attorney
 An enduring power of attorney (EPA) names someone — your attorney — to manage your finances and property. "Enduring" means it keeps working if you lose the capacity to make decisions yourself, which is exactly when it's needed.
 H3: Immediate or springing
 An immediate EPA takes effect as soon as it's signed. A springing EPA takes effect only when a specified event happens, usually a written declaration that you no longer have capacity. Geraldine will explain which suits your situation.
 H3: Choosing your attorney
 Choose someone you trust with money, who is organized and willing to keep records. You can name more than one person, and an alternate. If there's no one suitable, Geraldine can act for you — see Executor Services (link /executor-services).

H2: Personal directive
 A personal directive — sometimes called a medical directive or living will — names an agent to make personal decisions for you if you can't, such as health care and where you live. It can also record your wishes about treatment, so your agent and your care team know what you'd want.

H2: Choosing an executor
 Your executor gathers your assets, pays your debts and distributes your estate. It's real work, often over many months. Many people choose a family member. If you have no one suitable, or would rather not ask, Geraldine can be named as your executor. (Link: "About executor services" → /executor-services)

H2: When to update your documents
 - Marriage, or a new adult interdependent relationship
 - Separation or divorce
 - A new child or grandchild
 - The death of a beneficiary, executor, attorney or guardian you named
 - A move to or from Alberta, or buying property outside the province
 - A big change in what you own
 Even without a big change, a review every few years keeps your documents current.

H2: How it works (numbered, option 2 big-number style)
 1. Meet with Geraldine — You meet with Geraldine herself, often at your kitchen table. No questionnaire handed off to staff.
 2. Drafting — Geraldine prepares your documents and reviews them with you, so you understand every part.
 3. Signing — You sign with Geraldine present, so everything is witnessed properly.

H2: Fees
 Many planning services are fixed-fee. Contact us for the current schedule. Your fee is set out in your engagement letter before work begins.

H2: Common questions (accordion)
 Q: Do I need a will?
 A: If you have children, own property or have clear wishes about who should receive what, yes. A will keeps those decisions with you rather than leaving them to Alberta's default rules.
 Q: What does a will set cost?
 A: A will set is usually a will, an enduring power of attorney and a personal directive. Many planning services are fixed-fee; contact us for the current schedule.
 Q: What's the difference between an enduring power of attorney and a personal directive?
 A: An enduring power of attorney covers money and property. A personal directive covers personal decisions, such as health care and where you live. Most people need both.
 Q: How often should I update my documents?
 A: After any major life change — marriage, separation, a new child, a death or a move — and otherwise every few years.
 Q: Is an online will kit enough?
 A: A kit can work for some situations, but small mistakes are common: signing or witnessing done incorrectly, unclear wording, no alternate executor, or assets outside Alberta that aren't dealt with. Those can lead to delays, court applications or a will that doesn't do what you meant. Working with a lawyer also helps if the will is ever questioned.
 ReviewNote after FAQ: "These answers are draft wording for your review — please edit anything that doesn't match how you advise clients."

Closing CTA band: H2 "Ready to start your will?" text "Call Geraldine or send a message, and she'll arrange a time to meet — at your home or wherever suits you." buttons Call / Request a meeting.

============ ESTATES & PROBATE ("/estates-probate") ============
Title: Probate Lawyer in Calgary | Estate Administration | Estate Options
Description: Calgary probate and estate administration with Geraldine Hampton. Help for executors with the courts, banks and Land Titles. Complimentary initial meeting for estates.
H1: Probate Lawyer in Calgary: Estate Administration & Support for Executors
Intro: When someone dies, the person named in the will — the executor, also called the personal representative — has a lot to do, often while grieving. Geraldine guides executors and families through probate and estate administration, and deals with the courts, banks, Land Titles and other agencies on your behalf.
Highlight box (black featured style like the Executor card): H3 "Complimentary initial meeting" — "For estates, your first meeting with Geraldine is complimentary. She'll explain her process, what the estate is likely to require and her fees, so you can decide whether to go ahead. It's an introductory meeting, not legal advice, and there's no obligation."

H2: First steps after a death
 - Get copies of the death certificate or funeral home's proof of death
 - Find the original will, if there is one
 - Secure the home, vehicles and valuables
 - Keep receipts for funeral and other expenses
 - Hold off on giving away belongings or money until the executor's authority is confirmed
 - Call Geraldine to talk through what the estate will need

H2: What is probate?
 Probate is the court process that confirms a will is valid and confirms the executor's authority to deal with the estate. In Alberta, applications go to the Court of King's Bench under the Surrogate Rules.
 H3: Do you need it?
 Not always — it depends on what the person owned and how it was held. Banks, investment firms and Land Titles often ask for a grant before they'll release or transfer assets. Jointly owned property and assets with a named beneficiary often pass outside the estate. Geraldine will review the estate and tell you what applies.

H2: Grant of probate or grant of administration
 If there's a will, the executor applies for a grant of probate. If there's no will, a family member or other eligible person applies for a grant of administration (often called letters of administration) and becomes the administrator. Either way, the grant gives the personal representative legal authority to act.

H2: An executor's duties, step by step (numbered list)
 1. Secure and protect the estate's assets
 2. Notify beneficiaries and family members as Alberta's rules require
 3. Apply to the court for the grant
 4. List and value the assets and debts
 5. Pay debts and file the final tax returns
 6. Get a clearance certificate from the Canada Revenue Agency
 7. Distribute the estate and account to the beneficiaries

H2: Working with banks, Land Titles, the courts and family
 Much of estate work is paperwork and phone calls with institutions that each have their own requirements. Geraldine handles these on your behalf, and keeps family members informed so everyone knows where things stand.

H2: How long does probate take?
 Simpler estates commonly take several months from start to finish; estates with real estate, disputes or tax questions take longer. What affects the timeline:
 - Whether there's a clear, valid will
 - The number and type of assets, including real estate
 - Court processing times
 - Tax filings and the clearance certificate
 - Whether beneficiaries agree

H2: What does probate cost?
 H3: Court filing fees
 Alberta's probate filing fees are set by the Surrogate Rules and depend on the net value of the estate in Alberta:
 Table: Net value of estate | Filing fee
  $10,000 or less | $35
  Over $10,000 to $25,000 | $135
  Over $25,000 to $125,000 | $275
  Over $125,000 to $250,000 | $400
  Over $250,000 | $525
 Small source line under table: "Source: Alberta Surrogate Rules (Alta Reg 130/1995), Schedule 2."
 ReviewNote: "Please confirm these filing fees are current before launch."
 H3: Legal fees
 Geraldine's estate work is billed hourly, and the total depends on the size and complexity of the estate. She'll explain what to expect at your first meeting. Probate and legal fees for administering an estate are normally paid from the estate, not out of the executor's own pocket.

H2: Doing some of the work yourself
 Some executors want to handle parts of the estate themselves. Geraldine can advise on specific steps, prepare the court documents, and be there for the parts that need a lawyer.

H2: When family members disagree
 Disagreements over an estate are common and stressful. As an ADRIC Qualified Mediator, Geraldine can help families talk things through before they turn into court applications. (Link "About estate mediation" → /#mediation)

H2: Common questions (accordion)
 Q: Do I need probate? — A: It depends on what the person owned and how. Banks and Land Titles often require a grant before releasing or transferring assets; jointly held assets and those with a named beneficiary often don't. Geraldine can review the estate and tell you.
 Q: How long does probate take in Alberta? — A: Simpler estates commonly take several months. Real estate, disputes, tax filings and court processing times can extend that.
 Q: What does probate cost in Alberta? — A: Court filing fees range from $35 to $525 depending on the estate's net value. Legal fees depend on the work involved and are usually paid from the estate.
 Q: My spouse or parent died. What do I do next? — A: Find the will, secure the home and valuables, keep receipts, and hold off on distributing anything. Then call Geraldine — the first meeting for estates is complimentary.
 ReviewNote after FAQ: "These answers are draft wording for your review."

Closing CTA band: H2 "Named as an executor?" text "Talk to Geraldine about what the estate needs. Your first meeting for an estate is complimentary." buttons.

============ EXECUTOR SERVICES ("/executor-services") ============
Title: Professional Executor Services in Calgary | Estate Options
Description: No one to name as your executor or attorney? Calgary lawyer Geraldine Hampton can act as the executor of your will, or as attorney under your enduring power of attorney.
H1: Professional Executor Services in Calgary
Intro: Not everyone has someone to name as executor. Geraldine can be named as the executor of your will, or as your attorney under an enduring power of attorney — so the people and causes you care about are looked after by someone who does this work every day.

H2: Who this is for
 - You have no one you'd want to appoint
 - You'd rather not place the work on family
 - Your family lives out of province or overseas
 - Family relationships make a neutral person the better choice
 - Your estate includes property that needs careful handling

H2: Two roles Geraldine can take on (two cards)
 Card "Executor of your will": After your death, Geraldine gathers your assets, pays debts and taxes, deals with the courts and Land Titles, and distributes your estate as your will directs.
 Card "Attorney under your enduring power of attorney": During your lifetime, if you can no longer manage your own affairs, Geraldine manages your finances and property on your behalf, keeping records and acting in your interests.

H2: Why name a lawyer
 - Geraldine has practised wills and estates exclusively since 2010 and has guided executors through hundreds of estates
 - Lawyers are regulated by the Law Society of Alberta and carry mandatory professional liability insurance
 - A neutral person can help keep family relationships out of the paperwork
 - You can name an alternate, so there's always a backup plan

H2: Your options compared (simple 2-column table: Option | What to consider)
 A family member or friend | Knows you well and usually charges little or nothing, but may find the work time-consuming, especially from out of province.
 A trust company | Professional and ongoing, though many have minimum estate sizes and set fee schedules.
 Alberta's Office of the Public Guardian and Trustee | Can act in some situations, generally when no one else is able or willing.
 A lawyer like Geraldine | Brings legal knowledge and a personal relationship, and is accountable to the Law Society of Alberta.

H2: How compensation works
 Executor compensation in Alberta is guided by the Surrogate Rules and must be reasonable for the work done. Beneficiaries are entitled to see it in the estate accounts. Geraldine will explain how her compensation is set and put it in writing before you name her.
 ReviewNote: "Two questions before this section is final: (1) Do you charge executor compensation as a percentage of the estate or hourly? (2) Are there Law Society of Alberta disclosure requirements when you draft a will that names you as executor? We'll update the wording once we hear back."

H2: When the estate includes a home
 Many estates include a house. Geraldine is also a REALTOR®, so she understands what's involved in preparing and selling an estate home. (Link "Learn about her REALTOR® services" → https://geraldinehampton.com, new tab)
 ReviewNote: "Please confirm you're comfortable with this wording, given the roles of executor and listing agent."

H2: Common questions (accordion)
 Q: Can my lawyer be my executor? — A: Yes. You can name any adult you trust, including a lawyer. Geraldine will discuss what the role involves and how compensation works before you decide.
 Q: What if my executor dies before me? — A: That's why we recommend naming an alternate. If no named executor can act, someone has to apply to the court to administer the estate, which adds time and cost.
 Q: Can I change my executor later? — A: Yes. You can update your will at any time while you have capacity.
 Q: Can Geraldine act alongside a family member? — A: Yes. You can name co-executors, which some families find a good balance.
 ReviewNote after FAQ: "These answers are draft wording for your review."

Closing CTA band: H2 "No one to name as executor?" text "Let's talk about whether naming Geraldine is right for you." buttons.

============ CONTACT ("/contact") ============
Title: Contact Estate Options | Geraldine Hampton, Calgary Estate Lawyer
Description: Call 403-483-2020 or email Geraldine Hampton at Estate Options. Wills, powers of attorney, probate and executor services, with home visits across Calgary.
H1: Contact Estate Options
Intro: Call or email Geraldine directly. Most people email first; if you'd rather talk, please call — this line doesn't take texts.
Two columns:
 Left: Contact details (reuse ContactDetails): Phone 403-483-2020 (calls only, no texts); Email geraldine@estateoptions.ca and info@estateoptions.ca; Mailing address PO Box 31069, RPO Bridgeland, Calgary, AB T2E 9A3 with note "Mailing address only — Geraldine meets clients in their homes or by arrangement."; Hours Monday to Friday, 9 am–5 pm, evenings and weekends by appointment; Home visits across Calgary.
 Right: H2 "Tell us a little about what you need" — intake form, short (under 2 minutes):
  - Your name(s) (required)
  - Phone (required)
  - Email (required)
  - What can Geraldine help with? (select: Wills, powers of attorney & personal directives / An estate or probate / Executor services / Mediation / Something else)
  - Relationship status (select: Single / Married / Adult interdependent partner / Separated / Divorced / Widowed)
  - Children (select: None / Minor children / Adult children / Both)
  - Do you have a dependant with a disability? (Yes / No)
  - Are all your assets in Alberta? (Yes / No / Not sure)
  - Do you own property in the United States? (Yes / No)
  - Is any litigation underway or expected? (Yes / No / Not sure)
  - Anything unusual we should know? (textarea, optional)
  - Button "Send"
  Small print under button: "Please don't send confidential documents through this form. Sending a message doesn't create a lawyer-client relationship."
  On submit (still a review draft): show "Thank you — this is a review draft, so your message wasn't sent." Do not wire email yet.
  Use proper labels, required markers, and keyboard-accessible selects.

FINISH: run a text search across src for the banned words list and fix any hits; check every page has exactly one H1 and noindex; check mobile at 375px (phone visible in header, no horizontal scroll). Reply with the list of routes and anything you couldn't do.
```

## Change log

| Date | What | Credits |
|---|---|---|
| 2026-10-29 | Brief v1 written; build message sent to Lovable | see below |
