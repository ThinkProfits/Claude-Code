# Adaptive: initial research (keywords, competitors, blog topics)

Prepared 2026-11-17 by Francis for Andrew. **Internal draft.** Nothing here has gone to Ian, and nothing on the site has been changed.

## Data sources and gaps

| Source | What it gave | Notes |
|---|---|---|
| Google Search Console (`sc-domain:beadaptive.ca`, last 90 days) | Real queries, impressions and positions | Access through seo@ works |
| Google Keyword Planner (Vancouver geo, plus Canada for blog topics) | Search volumes | Small terms floor at "10" and many long-tail terms show 0, so treat those as "unknown/very low", not zero |
| Ian's Market Intelligence report (Oct 9, 2026) | Competitor metrics, AI visibility | Third-party, Semrush-based; per the checklist we update it, not redo it |
| Site sitemaps + YouTube RSS | Content inventory, video performance | 80 posts, 76 city pages, 55 videos |
| Client FAQ doc | Real sales-call questions | Used in place of People Also Ask (see below) |

**Update (same day):** Semrush keyword difficulty and rankings were pulled through the Semrush web app. See section 8. The keyword gap tool and the Questions filter still couldn't be run, because another Chrome extension blocked clicks on those forms.

**Blocked:** the Semrush MCP is out of API units (every report returns "no API units left"). That means no keyword difficulty, no Semrush keyword gap, no `phrase_questions` (our usual People Also Ask source) and no fresh competitor pulls yet. Ian's FAQ doc stands in for PAA this round because it holds real sales-call questions, which are better evidence of intent anyway. The gap analysis and difficulty scores still need to be run once units are topped up, or done in the Semrush UI.

---

## 1. What Search Console says (Aug 19 to Nov 17, 2026)

**Traffic today is mostly brand and the AI comparison post.**
- `/latest/copilot-vs-chatgpt-vs-gemini-vs-claude-for-business/`: 252 clicks, 27,761 impressions, average position 6.4. This is the site's biggest page.
- Homepage: 175 clicks, mostly brand queries ("adaptive", "adaptive technical", "adaptive it").

**Core commercial pages are visible but stuck on page 2 or 3.** This is the biggest lever, and it matches our core-pages-first approach for a low-authority domain (Authority Score 14).

| Query | Impressions | Avg position | Ranking page |
|---|---|---|---|
| managed it services vancouver | 2,007 | 24 | /managed-it-services-vancouver/ |
| it services vancouver | 1,026 | 21 | /managed-it-services-vancouver/ |
| it company burnaby | 60 | 11.8 | /managed-it-services-burnaby/ |
| it services burnaby | 46 | 27 | /managed-it-services-burnaby/ |
| it support burnaby | 41 | 23.8 | /managed-it-services-burnaby/ |
| it support for accounting firms | 64 | 7.7 | accounting page |
| automated cloud backup vancouver | 67 | 12.1 | /cloud-services-vancouver/ |

Page-level impressions (all queries, 90 days):

| Page | Impressions | Avg position |
|---|---|---|
| /managed-it-services-vancouver/ | 20,963 | 25.5 |
| /managed-it-services-west-vancouver/ | 5,761 | 37.5 |
| /cloud-services-vancouver/ | 4,509 | 18.7 |
| /cybersecurity-services-in-vancouver/ | 3,065 | 27 |
| /microsoft-365-consulting-vancouver/ | 2,723 | 22.9 |
| /areas-we-serve/ | 2,666 | 41.3 |
| /managed-it-services-burnaby/ | 674 | 12.4 |

**Note:** the Burnaby page sits at position 12 to 24 in GSC. The client overview says "page one for managed it services burnaby" (from the market report's live check, where it was 4th). Rankings differ by searcher location, so the BrightLocal Burnaby grid baseline will settle this. Until then, treat Burnaby as protected.

---

## 2. Keyword list (draft for Ian's approval)

Volumes are Google Keyword Planner averages for **Vancouver**. Everything below excludes Google Workspace, residential IT, copiers, cameras, door access, SAP, phone systems and one-off project work.

### A. Core commercial: managed IT and IT support, Vancouver

| Keyword | Vancouver vol. | GSC today | Map to |
|---|---|---|---|
| msp vancouver | 260 | not seen | /managed-it-services-vancouver/ |
| managed it services vancouver | 170 | pos 24 | /managed-it-services-vancouver/ |
| managed service provider vancouver | 170 | not seen | /managed-it-services-vancouver/ |
| it support vancouver | 140 | not seen | /it-support-vancouver/ (check for cannibalization with the managed IT page) |
| it services vancouver | 90 | pos 21 | /managed-it-services-vancouver/ |
| it company vancouver | 50 | not seen | homepage or managed IT page |
| it consulting vancouver | 40 | not seen | /it-consulting-vancouver/ |
| it outsourcing vancouver / outsourced it vancouver | 20 each | not seen | managed IT page |
| managed it vancouver, it service provider vancouver | 10 each | n/a | managed IT page |

### B. Service lines (priority order from the overview)

| Keyword | Vancouver vol. | Map to |
|---|---|---|
| cyber security vancouver | 70 | /cybersecurity-services-in-vancouver/ |
| cybersecurity services vancouver | 10 | same |
| ai consulting vancouver | 10 | /ai-for-business/ |
| cloud services vancouver | 20 | /cloud-services-vancouver/ |
| microsoft partner vancouver | 10 | M365 consulting page |
| microsoft 365 consulting vancouver | 0 to 10 | /microsoft-365-consulting-vancouver/ |

### C. Burnaby (protect) and other cities

| Keyword | Vol. | Note |
|---|---|---|
| it company burnaby / it services burnaby / it support burnaby / managed it services burnaby | 10 each (floor) | Protect. Baseline before any change |
| it support surrey, richmond, north vancouver, coquitlam, langley, new westminster | 10 each | Existing city pages |
| it support abbotsford / managed it services abbotsford | 0 to 10 | **No page yet.** Fraser Valley gap (8 competitors have pages) |

### D. Verticals

Keyword Planner shows 10 or less for all of these. They are still worth tracking because buyers are high value and AI tools already name Adaptive for some of them.

- it support for law firms / managed it services for law firms: Adaptive **is not named** by AI tools for law firms. This is the biggest vertical gap.
- it support for accounting firms / managed it services for accounting firms: Adaptive is named (1st in Perplexity, 5th in ChatGPT). GSC position 7.7.
- managed it services for nonprofits
- managed it services long term care bc / it support for long term care homes bc: 1st in BrightLocal's live check (Oct).

### E. Switching-provider intent (Ian's main success measure)

Keyword Planner returns 0 to 10 for all of these ("switching it providers", "msp contract" 70 in Canada, "how to switch msp", "signs you need a new it provider"). Low measured volume, but this is exactly what Ian says converts. Track a small set and cover it with content, not just pages.

### Tracking recommendation (Silver = 1 area, Vancouver)

Start with about 25 keywords: all of A, the cyber/AI/cloud terms from B, the four Burnaby terms, the vertical terms in D, plus "msp contract" and "switching it providers". Add the chosen competitors once the gap analysis is done.

---

## 3. Competitors (from Ian's Oct 2026 report; Semrush refresh pending)

| Competitor | Authority Score | Organic visits/mo | Why it matters |
|---|---|---|---|
| Revotech (revotech-networks.com) | 24 | 2,669 | #1 local firm on organic traffic; closest messaging to Adaptive |
| Nucleus (yournucleus.ca) | 27 | 2,037 | Only 41 pages, no blog: authority does the work. Named by Ian |
| Clearbridge (clearbridge.ca) | 9 | 1,889 | Strong traffic despite low authority; Fraser Valley and Okanagan city pages |
| Cloud9 (c9s.ca) | 18 | 1,049 | 186 city pages incl. Fraser Valley. Named by Ian |
| Sea to Sky (seatosky.com) | 21 | 556 | Named by Ian |
| F12.net | 34 | 6,527 (national) | National, PE-backed. Named by Ian |
| ActiveCo (activeco.com) | 22 | 377 | PE roll-up partner. Named by Ian |
| **Adaptive** | **14** | **57** | 19th of 23 on visits despite 81 commercial pages |

**Suggested gap-analysis set** (matches the checklist): Revotech, Sea to Sky, Nucleus, plus Tenecom for Vancouver head terms. Clearbridge is worth adding for Fraser Valley.

**AI visibility (from the report):** Adaptive is named for accounting firms, long-term care and "a real person answers". It is **not named** for law firms, Fraser Valley, Burnaby (in Perplexity) or "publishes pricing per user". The last one is odd, because Adaptive does publish pricing.

---

## 4. Existing content check (cannibalization)

I checked all 80 posts and 90+ pages in the sitemaps before picking topics.

- **AI comparisons are already saturated.** There are four posts, and two of them (`chatgpt-vs-gemini-vs-copilot-for-business` and `copilot-vs-chatgpt-vs-gemini-vs-claude-for-business`) are near-duplicates. **No new AI comparison posts.** Consolidating these two is a monthly-work item.
- **Already covered, so refresh instead of writing new:**
  - EDR: `antivirus-edr` ("what is edr" has 260 searches/mo in Canada)
  - MSP cost: `how-much-does-an-msp-cost`
  - Hiring an MSP: `what-questions-should-you-ask-before-hiring-an-msp`
  - In-house vs outsourced: `in-house-it-or-outsource`
  - Cyber insurance: `do-you-need-cyber-insurance`, `why-cyber-insurance-premiums-are-so-high`
  - Passkeys and MFA: 8 posts between them
  - Long-term care: 3 posts
- **Gaps (nothing on the site yet):**
  - law and accounting posts
  - nonprofit posts
  - Microsoft 365 backup
  - private equity roll-ups (also confirmed in Ian's FAQ doc)
  - Fraser Valley
  - general (non-LTC) switching guide

---

## 5. YouTube patterns (for scripts)

- Weekly, 6 to 12 minutes. Ian explains one tool or change for business owners. Hook titles include "X vs Y", "5 things", "what's free and what isn't" and "before [deadline]".
- **Best performers:**
  - Copilot Notebooks, free now: 14,608 views
  - Microsoft's new login policy: 4,179
  - Copilot runs Claude: 1,550
- **Weakest:**
  - Company and culture videos
  - Shorts
  - The care-home switching video: 217 views
- **Takeaway:** "a feature you already pay for" and "a change you must act on" do best. Business-buying topics (switching, contracts) make weak videos but are strong for SEO and sales. That is exactly why Andrew wants each topic labelled.
- Blog and video are already 1:1 on the site (Ian's own pipeline turns transcripts into posts). Our scripts should fit that pipeline rather than compete with it. **Question for Andrew:** do we write the script and Ian records it, with our post built from the same outline?

---

## 6. Blog topic candidates (labelled per Andrew)

Labels: **Video** = good for a YouTube episode. **SEO** = has search demand or supports a money page. Volumes are Canada-wide (Keyword Planner) unless noted.

| # | Working title | Target keyword (vol.) | Intent | Label | Overlap check |
|---|---|---|---|---|---|
| 1 | Does Microsoft back up your 365 data? What it keeps, what it doesn't, and for how long | microsoft 365 backup (140) | Informational, leads to cloud and security pages | **Video + SEO** | None. Answers FAQ #7 (backup and data residency in Canada) |
| 2 | Switching IT providers: what the 90-day handover actually looks like | switching it providers (10); msp contract (70) | Commercial investigation (switching intent) | **SEO, weak video** | Partial: `switching-it-providers-long-term-care` is care-home only. This is the general version; link the two. Also backs up the "about 90 days" fix Ian asked for |
| 3 | Microsoft 365 for nonprofits: the grants, the free licences, and the catch | microsoft 365 nonprofit (210); microsoft nonprofit grant (20) | Informational, leads to nonprofit page | **Video + SEO** | None. Seasonal: publish by January (nonprofit year ends March 31) |
| 4 | How private equity roll-ups work in managed IT, and what changes after the sale | msp private equity (10) | Commercial investigation, differentiation | **Video, low search** | None. Ian's own idea and FAQ #11. Strong for AI answers and switching prospects |
| 5 | Microsoft 365 Business Premium: the security features most offices pay for and never switch on | microsoft 365 business premium (880) | Informational / commercial | **Video + SEO** | Partial: `microsoft-365-business-plans-apps` is about unused apps. This angle is the security stack (Defender, Intune, Conditional Access). Keep them distinct |
| 6 | What to check in an IT support contract before you sign | msp contract (70); it support contract (10) | Commercial investigation | **SEO, OK video** | Partial: `what-questions-should-you-ask-before-hiring-an-msp`. This is about contract terms (term length, notice, what's billed extra). Link both |
| 7 | IT for BC law firms: what the Law Society and your insurer now expect | law firm cybersecurity (10) | Commercial, vertical | **SEO / AI visibility** | None. Targets the law-firm AI gap. Supports /managed-it-for-legal/ |
| 8 | Your office's AI use policy: what to put in it (with a template) | ai policy template (40) | Informational | **Video + SEO** | Partial: `ai-training-for-employees-8-rules`. Policy document vs training rules. Ian writes these for clients (FAQ #6) |
| 9 | Phishing simulations: do they actually change staff behaviour? | phishing simulation (70) | Informational | **Video + SEO** | Partial overlap with the "human hack" posts. New angle: testing, not awareness |
| 10 | IT for accounting firms before tax season: a January checklist | accounting firm technology (10) | Commercial, vertical | **SEO / AI visibility** | None. Reinforces where AI already names Adaptive. Seasonal |

**Refresh instead of new (monthly work, not blog slots):**
- `antivirus-edr`: retarget at "what is edr" (260) and "edr vs antivirus"
- `how-much-does-an-msp-cost`: align with all-in pricing (FAQ #1, the top sales question)
- Merge the two near-duplicate AI comparison posts
- `in-house-it-or-outsource`

**My recommendation for December's 2 slots:** #2 (switching guide, Ian's main measure) and #3 (nonprofits, seasonal). Then January: #1 and #10.

---

## 7. Next steps

1. Top up Semrush API units, or run the keyword gap and difficulty in the Semrush UI. Then refresh competitor metrics and PAA questions.
2. Run the BrightLocal Burnaby grid baseline and export the GSC Burnaby baseline before any page changes.
3. Andrew reviews this list. Then one clear keyword recommendation goes to Ian for approval (no tiered options).
4. Set up Vancouver position tracking once Ian approves.

---

## 8. Semrush web app data (Canada database, Nov 15, 2026 snapshot)

Pulled from Semrush Organic Rankings for beadaptive.ca and revotech-networks.com. "Pos" is Adaptive's current organic position.

| Keyword | CA volume | KD % | Adaptive pos | Adaptive URL ranking |
|---|---|---|---|---|
| managed it services vancouver | 1,300 | 12 | 33 | **/managed-it-services-west-vancouver/** |
| it services vancouver | 1,300 | 14 | 26 | /managed-it-services-vancouver/ |
| vancouver managed it services | 1,000 | 18 | 32 | **/managed-it-services-west-vancouver/** |
| managed service provider vancouver | 880 | 18 | 42 | /managed-it-services-vancouver/ |
| it support vancouver | 880 | 17 | not in top 50 | n/a |
| it company vancouver | 880 | 17 | not in top 50 | n/a |
| managed services vancouver | 480 | 13 | 35 | **/managed-it-services-west-vancouver/** |
| it services in vancouver | 390 | 13 | 31 | /managed-it-services-vancouver/ |
| cybersecurity vancouver | 260 | 11 | not in top 50 | n/a |
| it consulting vancouver | 260 | 22 | 29 | /it-consulting-vancouver/ |
| vancouver managed it | 260 | 13 | 27 | /managed-it-services-vancouver/ |
| cyber security companies in vancouver | 170 | 11 | 32 | /cybersecurity-services-in-vancouver/ |
| managed it vancouver | 170 | 14 | 15 | /managed-it-services-vancouver/ |
| it outsourcing vancouver | 140 | 10 | 19 | /managed-it-services-vancouver/ |
| managed it services vancouver bc | 110 | 14 | 14 | /managed-it-services-vancouver/ |
| **managed it services for law firms** | 110 | **3** | **2** | /managed-it-for-legal/ |
| small business it support vancouver | 90 | 7 | 7 | /managed-it-services-vancouver/ |
| business it support vancouver | 70 | 10 | 5 | /managed-it-services-vancouver/ |
| managed it services burnaby | 90 | 6 | 25 | **/managed-it-services-west-vancouver/** |
| it services burnaby | 70 | 11 | 21 | /managed-it-services-burnaby/ |
| it support burnaby | 70 | 7 | 36 | /areas-we-serve/ |

Semrush shows 141 Canadian keywords for Adaptive (down 6.6% month on month) and about 35 visits a month.

**What this changes:**
1. **Cannibalization is worse than the overview says.** For the three biggest Vancouver terms, Google ranks the *West Vancouver* page, not the Vancouver page. It does the same for "managed it services burnaby". Fixing which page owns "managed it services vancouver" is the top on-page task. Check Burnaby first, per the protect rule.
2. **Difficulty is low (KD 6 to 22) on every core term.** Authority isn't the main wall. Page targeting, the duplicate city pages and the GBP are.
3. **Revotech wins almost every Vancouver head term with its GBP-linked homepage** (the ranking URL carries `utm_source=gbp`). Its rankings come largely from the map pack. That supports Ian's own top goal: GBP first.
4. **Burnaby is not strong organically** (positions 21 to 36). The Burnaby strength in the overview is probably the map pack. The BrightLocal grid will confirm. Keep the protect rule anyway.
5. **Quick wins:** "managed it services for law firms" (pos 2, KD 3) and "business / small business it support vancouver" (pos 5 to 7). Note: our copy says "business owners", never "small business", so target the term without using the phrase in copy.
6. **Revotech's cybersecurity cluster** (cybersecurity vancouver 260, cyber security companies vancouver, vancouver cybersecurity companies) is a gap. Adaptive sits at 27 to 34 or doesn't rank.

**Still not done:** the full Semrush Keyword Gap export and the Questions filter (PAA). The web app forms wouldn't accept clicks because another Chrome extension was intercepting them. Andrew, or someone with the extension off, can run these in about 5 minutes: Keyword Gap, Canada, beadaptive.ca against revotech-networks.com, seatosky.com and yournucleus.ca.
