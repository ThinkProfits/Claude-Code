**Title tag:** Google Ads vs GA4 Conversions: Why Your Lead Counts Differ (58 characters)

**Meta description:** Google Ads vs GA4 conversions rarely match your CRM. See the settings behind each gap, which number to trust for what, and a monthly routine to reconcile them. (159 characters)

**Slug:** `/digital-news/google-ads-ga4-crm-leads/`

**Primary keyword:** google ads vs ga4 conversions

**Secondary keywords:** google ads conversion tracking, ga4 key events, google ads attribution model, data-driven attribution, import ga4 conversions to google ads, google ads conversion tracking ga4, offline conversion tracking google ads, enhanced conversions for leads, crm lead tracking

**Search intent:** Informational and diagnostic. A business owner or in-house marketer sees different form lead totals in Google Ads, GA4 and their CRM and wants to know which causes are normal, which are errors, and how to reconcile the three.

**Category:** Analytics

---

# Why Google Ads, GA4 and Your CRM Disagree on Form Leads

> **Quick answer:** Google Ads vs GA4 conversions almost never match, and neither will match your CRM, because each system counts a different thing on a different date with different rules. Learn which setting causes each gap, remove the genuine errors (duplicate tags, spam, missing imports) and reconcile the three on a fixed monthly routine.

[IMAGE: ThinkProfits branded placeholder | alt: Google Ads, GA4 and CRM lead counts compared side by side in a monthly report | file: /images/blog/wp/tp-branded-placeholder.jpg]

Here is a version of a month-end report we see often: Google Ads says 48 form leads, GA4 says 41, the CRM has 33 new contacts, and the sales team says only 20 of them were real enquiries. Someone asks which number is right.

All three can be accurate. Google Ads, GA4 and a CRM are answering different questions, and most of the gap between Google Ads vs GA4 conversions comes from settings rather than broken tracking. This guide explains the settings that move each number, what the CRM adds on top, and the monthly routine we use in our [PPC advertising](/ppc-advertising/) work to tell normal differences from real errors. It draws on current Google Ads Help and Analytics Help documentation. The example numbers above are illustrative, not client data.

## Each system is answering a different question

Before comparing totals, be clear about what each tool is built to count. Google's own Analytics Help page on [conversions vs key events](https://support.google.com/analytics/answer/13965727?hl=en) describes conversions as built for advertising measurement, while key events are built for analysing traffic and user behaviour on your site.

| System | The question it answers | What it usually counts for a form lead |
|---|---|---|
| Google Ads | Which ad interactions led to a conversion? | Conversions it can tie to an ad click (or view), including modelled ones |
| GA4 | What did visitors do, and which channel gets credit? | Key events from every channel, credited by your attribution settings |
| CRM | Which people became real leads and customers? | Contact records, usually after deduplication and some manual cleanup |

## The settings that move Google Ads vs GA4 conversions

Most of the gap comes from five settings. The first two usually explain the biggest swings.

### Attribution and creditable channels

Data-driven attribution is now the default for most conversion actions in Google Ads, and Google has retired the old first click, linear, time decay and position-based models. The model is not the main difference, though. GA4's own reports default to crediting paid and organic channels, so a form lead can be credited to organic search, email or a direct visit. Google Ads reports conversions it can connect to an ad interaction, so a person who clicked an ad on Monday and came back through organic search on Thursday can show as a Google Ads conversion and an organic key event at the same time.

### Conversion date

Google Ads reports the Conversions column by the time of the ad click, not the time of the conversion. GA4 records the key event when it happens. A click on March 28 that converts on April 3 counts in March in Google Ads and in April in GA4. Google Ads also offers "by conv. time" columns, which are the better choice when you compare against GA4 or your CRM.

### Counting method

Google's [conversion counting guidance](https://support.google.com/google-ads/answer/3438531) recommends counting "One" conversion per ad click for leads, and our [primary vs secondary conversions checklist](/digital-news/primary-vs-secondary-conversions-google-ads/) covers how to set it. The cross-tool problem is that GA4 key events count "Once per event" by default, so a visitor who submits the same form twice is two key events. With Google Ads on "One" and GA4 on its default, a repeat submission inflates GA4 and not Google Ads.

### Conversion windows

A new Google Ads conversion action uses a 30-day click-through window unless you change it, and the window can be set as long as 90 days. GA4's key event lookback window defaults to 90 days for most key events, with 30 and 60 days as options. For service businesses with long decision cycles, our guide to [GA4 custom conversion windows](/digital-news/ga4-custom-conversion-windows-long-sales-cycles/) covers how to choose them.

### Modelled and view-through conversions

Google Ads reports both modelled and observed conversions in the Conversions column. It models conversions it cannot observe directly, for example when browsers limit cookies, when consent is declined, or when the click and the form happen on different devices. View-through conversions appear in All conv., not in Conversions. GA4 does not show Google Ads conversions in its standard Reports or Explore sections, so neither appears in the key event totals you are comparing.

## Why the CRM number is different again

The CRM is closest to reality, and also the easiest to break. It sees people, not events.

- **Spam and junk submissions:** bots and sales pitches fire the same thank-you event as a real enquiry, so they count in Google Ads and GA4. They only get removed in the CRM, and only if someone marks them.
- **Duplicates and repeat contacts:** the CRM usually merges a returning customer into an existing record. Both analytics tools may count that same person as a new conversion.
- **Leads that never touched the form:** phone calls, walk-ins and email enquiries land in the CRM with no web event at all. They lower the gap in one direction while spam raises it in the other.
- **Date logic:** CRM records are dated when they are created or imported, which can be hours or days after the form, and is never the ad click date.
- **Source fields:** if hidden UTM or click ID fields are not captured on the form, the CRM cannot say which leads came from ads. Our post on [UTM parameters in local SEO reporting](/digital-news/utm-parameters-canonicals-local-seo-reporting/) explains the tagging side.

Feeding CRM quality signals back into Google Ads is a separate build, covered in our [Google Ads lead quality loop](/digital-news/google-ads-lead-quality-loop/) guide.

## A monthly reconciliation routine

Reconciling once a month, on a closed period, gives you a stable comparison without chasing daily noise. This is the routine we use.

1. **Close the period first.** Wait at least a week after month end before comparing, so late conversions inside the window have time to arrive. Pull Google Ads using the "by conv. time" columns so the dates line up with GA4 and the CRM.
2. **List the tracked actions in each tool.** Write down every Google Ads conversion action and GA4 key event that represents a form lead, with its counting method and window, so you know which settings explain the gap. If Google Ads itself is counting one lead twice, fix that first using the [primary vs secondary conversions checklist](/digital-news/primary-vs-secondary-conversions-google-ads/).
3. **Compare like with like.** In GA4, filter to Google Ads traffic before comparing against Google Ads. In the CRM, filter to leads with a paid search source or a captured click ID. Comparing GA4's all-channel total to Google Ads is a common reporting mistake.
4. **Clean the CRM side.** Mark spam, duplicates and test submissions, and note how many there were. That count is a finding in itself, because it tells you how much of the ad platform's number is noise.
5. **Record ratios as well as totals.** Track Google Ads to GA4 (paid) and GA4 (paid) to qualified CRM leads month over month. A stable ratio is normal. A sudden change usually means a tag, form or setting changed, and a [weekly Google Ads change log](/digital-news/weekly-google-ads-change-log/) is the fastest way to find which one.
6. **Write one line of explanation.** Each month's report should say what the gap was and why, in plain language. In our [digital marketing reporting](/digital-marketing-reporting/), this line sits next to the numbers so nobody relitigates it in the meeting.

## Which number to use for which decision

Use each system for the decision it was designed to support, and say so in the report.

- **Bidding and campaign optimization:** use Google Ads conversions, because Smart Bidding learns from them. Clean primary actions matter more here than matching GA4.
- **Channel mix and site behaviour:** use GA4, because it is the only one of the three that compares paid, organic, referral and email on the same rules.
- **Budget, cost per qualified lead and revenue:** use the CRM, because it is the only place where junk is removed and real outcomes are recorded.

The goal is a gap you can explain and that stays roughly stable from month to month. A tidy routine will not make the three numbers identical. Modelled conversions are estimates by design, and offline leads sit outside web analytics unless you import them. Profitability is a separate question; reconciliation only tells you whether your measurement is trustworthy enough to answer it.

## Frequently asked questions

### Why does Google Ads show more conversions than GA4?

Usually because Google Ads includes conversions GA4 does not see in its standard reports: modelled conversions, cross-device conversions and ad-assisted leads that GA4 credits to another channel. Dates also differ, since Google Ads reports by click time by default. Check for a duplicate conversion action before assuming any of these, because that is a frequent real error.

### Should I import GA4 key events into Google Ads or use the Google Ads tag?

Google supports both. The Google Ads tag measures directly in Google Ads, while imported GA4 key events keep both tools working from one event definition, which makes month-end comparisons easier to explain. Either way, only one of them should be primary for a given form.

### How big a gap between Google Ads and GA4 is normal?

Google does not publish a single acceptable range. In practice, we look for a gap that is explained by the settings above and stays roughly stable from month to month. A gap that jumps after a site change, a new form or a consent banner update is worth investigating that week.

### Why are there fewer leads in my CRM than in Google Ads?

The CRM removes what the ad platform cannot: spam, duplicates, test submissions and returning customers merged into existing records. Missing form integrations can also drop leads before they reach the CRM. Count the removed records during each reconciliation so you can see how much of the gap is noise and how much is lost data.

## Not sure which of your numbers to believe?

If your Google Ads, GA4 and CRM totals tell three different stories, we can walk through your conversion actions, key events and form setup with you and show where each gap comes from. Book a free 30-minute consultation and bring last month's numbers. There is no guarantee the totals will ever match exactly, but you should leave knowing which one to use for each decision.

**[Book My Free Consultation](/contact/)**
