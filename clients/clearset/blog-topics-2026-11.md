# Clearset: blog topic options (Nov 2026)

- **Asked by:** Andrew, scrum 2026-11-12: "two to four kind of blog topics that we think would really help move the needle, one ones that would have a good chance of ranking and getting some clicks." Sean picks from the list. The plan is two blogs, with one of his landing pages swapped for blogs.
- **Written:** 2026-11-13 by Francis (with Claude). DRAFT for Andrew's review.
- **Still to come from Sean:** the list of questions his customers ask all the time. When it arrives, check it against these four and swap in anything that's stronger.

**Sources and limits**
- Volumes come from Google Ads Keyword Planner (British Columbia, Nov 2025 to Oct 2026). It rounds figures for low-spend accounts, so read them as ranges.
- Semrush was out of API units on 2026-11-13. That means **no keyword difficulty, PAA question pull or `resource_organic_unique` check** this run. Rerun all three before drafting.
- Site rules come from [CLIENT.md](CLIENT.md) sections 2 and 8 and the [keywords.md](keywords.md) rules in section 5.

## Existing content check

- The sitemap (`page-sitemap.xml`, 2026-11-13) lists 28 pages: the homepage, services, city pages and legal pages. `post-sitemap.xml` is empty. **The site has no published blog posts**, so no existing post overlaps these topics.
- The only blog so far is the unpublished draft "5 Warning Signs You Need Septic Repair" (Sept 2026). Topic 1 below stays clear of it by covering routine maintenance, not warning signs.
- WordPress (checked 2026-11-13, all statuses): 4 posts, all drafts from 2022. Three are lorem-ipsum placeholders ("Blog 1–3") and one is a "Test" post. No real post content. The warning-signs draft is not in WordPress.
- Overlaps with service pages are listed under each topic, with the angle that keeps the blog from competing with the page.

### GSC cannibalization check (2026-11-13)

Search Console, query + page, 2026-08-13 to 2026-11-10, for each topic's keyword stems. This shows which URL Google already ranks for each query.

| Topic | What GSC shows | Risk |
|---|---|---|
| 1. How often to pump | No "how often" queries at all. "septic maintenance near me / coquitlam / port coquitlam" go to the homepage (GBP link) and the Port Coquitlam city page. | **Low**, but only if the blog targets the "how often" questions. The "septic maintenance + city / near me" queries are local service searches and belong to the city pages. |
| 2. Pumping cost | "septic tank cleaning price" goes to /services/septic-tank-cleaning/ (pos 11). "septic tank pumping near me prices" goes to the Burnaby city page (pos 71). Price queries are already split across two pages. | **Medium.** A cost blog would be a third URL for the same queries. |
| 3. RV dump station | Every RV query is a service search ("mobile rv pumping service" pos 4, "rv septic tank pumping" pos 8.7), all on /services/trailers-and-rvs-pumping/. No "dump station" queries. | **Low.** Different intent, as long as the blog doesn't target "mobile RV pump-out". |
| 4. What is hydrovac | No "what is" queries. The hydrovac page ranks for cost-per-hour queries (pos 7.5–10) and "daylighting hydrovac" (pos 30). | **Low**, if the blog stays off pricing. |

**Existing overlap found (not caused by these topics):** "hydrovac services vancouver" shows the homepage at pos 12.5 and the hydrovac page at pos 43.7. The homepage is outranking its own service page. That should be fixed in the hydrovac page work anyway, and topic 4's internal links will help.

## Recommended topics

### 1. How often should you pump your septic tank? A BC homeowner's maintenance guide
- **Target keyword:** how often should a septic tank be pumped (about 10 variants at 20–40/mo each). Changed after the GSC check: the "how often" questions have no ranking page yet, so the blog takes them cleanly.
- **Supporting:** septic tank maintenance (590/mo BC; grouped with "septic system maintenance", "septic tank care" and "maintaining septic tank"), septic drain field maintenance (30), septic tank filter cleaning (20). GSC also shows "septic system filter maintenance" at 181 impressions on the homepage, so the filter section is worth keeping.
- **Keep out of the blog:** "septic maintenance near me" (260) and "septic maintenance + city". They're local service searches that the homepage and Port Coquitlam page already rank for.
- **Search intent:** informational, from homeowners planning ahead
- **Why it helps:** it's the biggest informational cluster we found. Readers who own a septic system will need a pump-out, and the post funnels them to the septic hub.
- **Overlap watch:** /services/septic-system-maintenance/ already lists "septic system maintenance" as a secondary keyword. Keep the blog as a how-to guide (schedule, household size, what to avoid) and link to that page and the hub for the service itself.
- **Rules:** use HealthLink BC's 2–5 year guidance and don't cite a BC-mandated pumping interval, because there isn't one. No inspection or repair as a Clearset service.

### 2. How much does septic tank pumping cost in BC?
- **Target keyword:** septic tank pumping cost (50/mo BC)
- **Supporting:** price to pump septic tank (50), septic tank pumping rates (50), septic tank pumping prices (20), septic system pumping cost (20), cost for pumping a septic tank (20)
- **Search intent:** commercial. These readers are close to booking.
- **Why it helps:** together the variants are close to the volume of topic 1, competition is LOW, and cost searchers convert well. It also backs up the hub's weak "septic tank pumping" rankings.
- **Cannibalization (medium):** price queries already land on /services/septic-tank-cleaning/ and the Burnaby city page. If this goes ahead, make the blog *the* price page: link both pages to it with cost-focused anchor text, and keep price wording off the city pages. The other option is to put a pricing section on /services/septic-tank-cleaning/ and drop this topic.
- **Blocker:** **prices must be confirmed with Sean before drafting.** The last figure we had was $530 starting (2025-09), and the content rules say not to quote prices until they're reconfirmed. If Sean won't publish a figure, write it around cost factors (tank size, access, distance, how overdue the pump-out is) and invite readers to call for a quote.

### 3. RV dump station or mobile pump-out? Emptying your RV tanks in Metro Vancouver
- **Target keyword:** rv dump station near me (1,000/mo BC)
- **Supporting:** rv black tank cleaning (50), how to clean rv black tank (10), where to dump rv waste (10)
- **Search intent:** mostly navigational/local. Most people searching want a dump station. The post meets that, then offers mobile pump-out as the easier option.
- **Why it helps:** RV was the main loss in the GSC YoY drop: the RV pumping page lost about 90% of its clicks (see [gsc-yoy-drop-aug-oct-2026-11.md](gsc-yoy-drop-aug-oct-2026-11.md)). This builds topical support and internal links into /services/trailers-and-rvs-pumping/.
- **Risk:** the intent mismatch is real. Many readers will only want a station address. Every station listed must be verified (location, hours, fees) under the blog fact-check standard. Expect clicks, not many direct leads.

### 4. What is hydrovac excavation, and when do you need it?
- **Target keyword:** what is hydrovac (40/mo BC)
- **Supporting:** what is hydro excavation (10), daylighting utilities (10), plus the synonym set hydro excavation / daylighting / potholing / slot trenching
- **Search intent:** informational, from contractors and property managers
- **Why it helps:** hydrovac is a top revenue line that Sean keeps raising, but the page sits around position 36. A plain-language explainer gives that page internal links and topical support.
- **Overlap watch:** stay with the explanation and use cases. Leave pricing and booking to /services/hydrovac-excavation-and-hot-water-services/.

## Also considered

| Topic | BC vol. | Why it's not in the four |
|---|---|---|
| Septic-safe toilet paper / what not to flush | 170 | Good volume, but it's product-led and ad-heavy (HIGH competition) with weak lead intent. Could become an FAQ section in topic 1. |
| Signs your septic tank is full | 10 | Overlaps the existing warning-signs draft |
| Grease trap cleaning frequency | 10 | Low volume. Better aimed at restaurants via GBP and the service page. |
| Hydro jetting vs snaking | 10 | Low volume, plumbers dominate that search, and it would compete with /services/hydro-flushing/ (GSC shows "hydro jetting" queries there) |
| Holding tank vs septic tank | 10 | Low volume. Could be a later post. |

Anything about potable water, septic inspection, septic or drain field repair and Alberta is excluded under the standing keyword rules.

## Suggested pick for the two blogs

1. **Topic 1:** biggest cluster, lowest risk, supports the septic hub.
2. **Topic 3** (RV): it targets the RV loss directly and has low cannibalization risk. **Topic 2** only if Sean confirms prices *and* we agree the blog becomes the price page (see its cannibalization note).

## Before drafting

- Rerun Semrush once API units are back: KD for each target keyword, `phrase_questions` for the PAA/FAQ section, and `resource_organic_unique` for the indexed-page check.
- Fold in Sean's customer-question list.
- Confirm prices (topic 2) and verify RV station details (topic 3).
