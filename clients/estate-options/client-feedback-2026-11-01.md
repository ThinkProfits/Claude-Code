# Geraldine's feedback on the Estate Options site draft: 2026-11-01

**Source:** Geraldine's email "RE: Websites for Review" (Sun 2026-11-01, cc Grace Mendoza), plus her comments in the Lovable editor. Andrew forwarded it to Francis on 2026-11-03, and they went over it in the 2026-11-03 scrum. Andrew's preview link for this site: https://lovable.dev/preview/cvqIAa3L29ivDJfcTh1DmcD7XiIMGs3N (Lovable project `69c1b714-db52-47cf-b5b5-0dc70974ab8c`).

The same email covers the realtor site too. Those notes are in [../geraldine-hampton-realtor/client-feedback-2026-11-01.md](../geraldine-hampton-realtor/client-feedback-2026-11-01.md). Keep the two separate.

**Deadline:** next version of both sites goes to Geraldine by end of week (Fri 2026-11-06), per the scrum.

## What she asked for

- [ ] **No fees on the law site.** Take out the fee ranges we added. (We had told her a range plus "contact for details" helps with Google. She has decided against it, which is her call.)
- [ ] **Remove technical and legal content.** In her words, she doesn't want "to practice law on the website." Some of our questions and answers were wrong or raise too many issues. She marked what to delete in the Lovable editor comments. Work through every comment.
- [x] **Mediator: change it to "since 2018" everywhere** (done 2026-11-04, see below). **Conflict:** our copy and research say ADRIC QMed **2019** (About page, credentials list, fix round 2026-10-30). Confirm with her whether 2018 refers to the QMed credential or to when she started mediating, then update every mention, schema included.
- [ ] **Brochures and business card** (her 2026-10-31 email, forwarded 2026-11-03): `Estate_Options_Wills_Pamphlet_June24.pdf`, `Flyer_Printers_Estate_Options_Pamphlet_June24.pdf`, `Estate_Options_Wills_Pamphlet_May27.pdf`, `Estate_Options_Pamphlet_May27.pdf`, `Estate_Options_Business_Card_May27.pdf`, plus `image001.jpg`. They're out of date (address and years of experience), so don't use them as a source for facts. She offered to send a photo of them standing on a desk instead. Andrew thinks they're of limited use, but they could work as staged images.

## Andrew's rules for this round (2026-11-03 scrum)

- If she asks for something to be removed, remove it.
- If a removal would really hurt SEO, flag it first and suggest other wording that Andrew can pitch to her. Either way it's her call, but she should make it knowing the tradeoff.

## Lovable preview comments (pulled 2026-11-04)

44 comments from Geraldine and 2 from Grace, all still open in the share preview. They were pulled with each one's page and the element it's pinned to, and sent to Lovable as one edit round on 2026-11-04 (message `umsg_01m6harkgyff0a01k08x53yf46`). What changed:

- **Sitewide:** mediator year changed to 2018. Every legal-fee figure removed (the court filing fee table stays; she liked it). "No one to appoint" softened to "a suitable person isn't available".
- **Home:** executor card softened, and "out of town" added (Grace). Card note font size fixed (Grace). Wording changed in "losing capacity" ("duties and responsibilities") and "protecting" ("wishes for your family"). Estate transitions expanded (she advises PRs and attorneys on selling a home: court timing, Land Titles). Bio: "changes in the law ... reviewing case law", and Chinook teaching was "pro bono". The will-meeting ReviewNote is removed (no complimentary meeting for wills). Joint assets removed from the probate FAQ. New FAQ: what happens without an EPA/PD (her wording).
- **Wills:** added that a guardian takes a year or more through the courts, plus a trustee for minors' trust funds. New "What happens without an EPA or personal directive" block in her wording. The cost section keeps its H2 but drops the ranges, and the fee FAQ drops its ranges.
- **Probate:** button relabelled "Contact Geraldine" (she asked why it said "a Calgary probate lawyer"). New first-steps line: talk to Geraldine before acting on funeral home or bank advice (with a ReviewNote, since she said to leave it out if it reads as negative). "Jointly owned property" removed. Bullets now include "serving beneficiaries" and "reviewing the estate accounting". "Potential claimants" replaces "disputes". Legal-fee range replaced with her line about electronic filing. "Challenging family dynamics" replaces "family disagreements". Added the 2.5-year litigation wait. New grant timing: 3 to 5 weeks, 6 months to a year to administer. "Qualifying family member" caveat added to the claims FAQ.
- **Executor:** intro now adds "many people don't have children, or their children live in another jurisdiction". The duties list ends with "account ... and distribute". "Best interests" added. The alternate bullet is replaced with "ask Geraldine how she makes sure an alternate is in place". **Removed "Your options compared"** (trust companies refer clients to her). **Removed "Executor compensation in Alberta"** ("a can of worms"). Percentages removed from the pay FAQ. "Family member alongside a lawyer" removed (she will never take that appointment). CTA heading "No one to name as executor?" deleted.

**Owed to Geraldine:** she asked for the removed "Your options compared" section in Word so she can look into it. The original text is in [lovable-fix-round-2026-10-30.md](lovable-fix-round-2026-10-30.md) and in Lovable git history before this round. Build the .docx and send it via Andrew.

## SEO flag list (for Andrew to pitch alternatives)

We made every removal she asked for. These are the ones with a real SEO cost:

| Page / section | She wanted | SEO cost | Alternative wording to pitch |
|---|---|---|---|
| Wills: "Cost of a will in Calgary" + FAQ | No fee ranges | "Cost of a will Calgary" and "how much does a will cost in Alberta" are high-intent searches, and AI answers favour pages with a figure. Without one, the answer gets pulled from competitors. | We kept the H2 and the fixed-fee explanation. Pitch: "Fixed fees, quoted before you commit", or one "starting from $X" figure that she sets. |
| Probate: legal fees block + FAQ | No fee ranges | Same for "probate lawyer cost Calgary". | Kept the hourly explanation and the filing fee table. Pitch: "most straightforward grant applications are quoted as a flat fee" if true, without a number. |
| Executor: "Executor compensation in Alberta" (removed) | Remove section | "Executor fees Alberta" / "executor compensation Alberta" is the page's biggest informational query. Now only one FAQ covers it, without percentages. | A short neutral paragraph that cites the Surrogate Rules factors and says compensation is agreed in writing, with no percentages. |
| Executor: "Your options compared" (removed) | Remove section (trust companies refer clients to her) | Comparison content ("lawyer vs trust company as executor") is good for AI answers. Moderate loss. | A version that leaves trust companies out: "Family member or friend vs a lawyer". She wants the Word copy first anyway. |
| Probate: joint property sentence (removed) | Remove | Minor. "Does joint property go through probate Alberta" is a PAA question. | A one-line referral: "Jointly owned assets can be complex. Get a legal opinion before transferring them." That matches her own reasoning without giving advice. |

## Mediator year

Her email says "global change to 'since 2018'". The realtor preview has a comment, "global update: 2018 not 2019", and one law-site comment says "since 2019". The email was sent last (01:14 UTC Nov 2, after the 2019 comment), so we used **2018** on both sites. A ReviewNote on the law site asks her to confirm. Our earlier research had QMed 2019, so the source needs checking.
