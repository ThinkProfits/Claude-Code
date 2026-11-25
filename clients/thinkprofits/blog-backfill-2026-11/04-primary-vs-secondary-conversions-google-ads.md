**Title tag:** Primary vs Secondary Conversions: Google Ads Checklist (54 characters)

**Meta description:** Primary vs secondary conversions decide what Google Ads bids on. Learn what each setting does, the lead-gen mistakes we see, and a checklist to fix them. (153 characters)

**Slug:** `/digital-news/primary-vs-secondary-conversions-google-ads/`

**Primary keyword:** primary vs secondary conversions

**Secondary keywords:** google ads primary vs secondary conversions, secondary conversion google ads, primary and secondary conversions, google ads conversion actions, conversion goals google ads, include in conversions google ads, google ads conversion tracking, google ads conversion settings

**Search intent:** Informational with practical setup intent. A business owner or in-house marketer wants to know what the primary/secondary setting does to bidding and reporting, and how to set it correctly for lead generation.

**Category:** PPC

---

# Primary vs Secondary Conversions in Google Ads: A Lead-Gen Checklist

> **Quick answer:** In Google Ads, primary vs secondary conversions is the difference between what bidding chases and what you only watch. Primary actions feed the "Conversions" column and Smart Bidding when the campaign uses their goal. Secondary actions are observation only and show in "All conv.", with one exception: custom goals.

[IMAGE: Hero placeholder | alt: Google Ads conversion goals summary showing primary and secondary actions for a lead generation account | file: /images/blog/wp/tp-branded-placeholder.jpg]

Most lead-gen accounts we inherit have a conversion list that grew one tag at a time: a form fill from 2021, a thank-you page from the last rebuild, a GA4 import nobody remembers adding. Each one carries a primary or secondary setting, and that setting quietly decides what Smart Bidding spends your budget chasing.

This post explains what primary vs secondary conversions actually control, the mistakes that inflate lead counts, and a governance checklist you can run in about half an hour. It is written for Vancouver and Canadian service businesses running Google Ads for calls and form leads, not ecommerce. It will not make a weak offer convert, but it can stop the account from learning the wrong lesson.

## What primary and secondary actually control

Primary is about bidding and the main reporting column; secondary is about observation. Almost every problem we see comes from forgetting one side of that.

According to [Google's help page on primary and secondary conversion actions](https://support.google.com/google-ads/answer/11461796?hl=en), a primary action is reported in the "Conversions" column and is used for bidding when the campaign optimizes toward the goal that action belongs to. A secondary action is for observation only. It is reported in the "All conv." column and does not drive bidding, even if its goal is used in a campaign.

| Setting | Shows in | Used for bidding? | Good for |
|---|---|---|---|
| Primary | "Conversions" and "All conv." | Yes, when the campaign uses its goal | The actions you want the account to buy more of |
| Secondary | "All conv." only | No (unless it sits in a custom goal) | Supporting signals you want to watch without paying for them |

Two details matter for lead-gen accounts:

- **Goals sit above actions.** Google groups conversion actions into goals by category, such as "Submit lead forms" or "Contacts". A campaign set to use account-default goals optimizes toward every goal marked account-default, so a stray primary action in one of those goals affects every campaign using them.
- **Custom goals override the label.** Google states that a secondary action placed in a custom goal is used for bidding once that custom goal is set on a campaign. If you use custom goals, "secondary" no longer means "safe to ignore."

## The common lead-gen mistakes

Most problems come from treating the conversion list as a reporting tool rather than as instructions to the bidding system. These are the patterns we find most often in audits.

1. **Page views or scroll events set as primary.** A "visited the contact page" action is cheap to get and has a weak link to actual leads. When it sits in a primary goal, bidding finds people who browse, and the conversion count rises while the phone stays quiet.
2. **The same form counted twice.** A form-submit event and a thank-you page view often track the same inquiry. If both are primary, one lead becomes two conversions, your cost per lead looks far lower than it really is, and bidding treats the duplicated signal as stronger than it is.
3. **A GA4 import duplicating a native tag.** Google notes that conversions created from Google Analytics are secondary by default and can only be promoted to primary inside Google Ads. Problems start when someone promotes the GA4 version while the Google Ads tag for the same action is still primary.
4. **"Every" counting on lead forms.** [Google's conversion counting guidance](https://support.google.com/google-ads/answer/3438531?hl=en) describes "One" as counting one conversion per ad click and says it suits leads, because usually only one unique lead per click adds value. "Every" is the default for website actions, so a lead form left on the default can count repeat submissions from the same person.
5. **Calls of every length counted the same.** A two-second misdial and a ten-minute booking call should not carry equal weight. If call conversions are primary, check the call length threshold before trusting the numbers.

None of these break the account visibly. They show up as a cost per lead that looks healthy in Google Ads and does not match what your intake team sees, the gap our post on [target CPA versus business CPA](/digital-news/target-cpa-vs-business-cpa-google-ads/) digs into.

## How to decide what should be primary

Make an action primary only if you would be happy for bidding to chase more of it at your current cost. That one test settles most debates.

For a typical service business, that usually means:

- **Primary:** completed lead form submissions (counted once per click), qualified phone calls above a sensible duration, and booked appointments if your booking tool reports them reliably. These are the actions that tend to turn into revenue.
- **Secondary:** contact page views, clicks on the email address, brochure downloads, and chat opens. They are useful for spotting landing page problems, but a rise in them does not mean the business got busier.
- **Neither, until it is clean:** any action that fires on page load, on every form step, or from a tag you cannot trace. Fix or remove these instead of parking them as secondary forever.

If your CRM can tell you which leads became customers, the stronger setup is to feed those outcomes back into Google Ads and treat raw inquiries as secondary. We cover the stages, ownership and reconciliation for that in our [Google Ads lead quality loop](/digital-news/google-ads-lead-quality-loop/) post, so we will not repeat it here.

## A conversion governance checklist

Run this before any bid strategy change, after any website rebuild, and at least once a quarter.

1. **Export the full conversion list.** Go to Goals, then Conversions, then Summary, and note each action's source, goal, status, count setting and whether it sits in a custom goal. This is your baseline.
2. **Map each action to a real business event.** Write one sentence for each: "fires when a visitor submits the quote form on /contact/." If nobody can write that sentence, the action is a candidate for removal, not promotion.
3. **Find duplicates.** Look for pairs that track the same moment, such as a form event and its thank-you page, or a Google Ads tag and its GA4 import. Keep one as primary and set the other to secondary or remove it.
4. **Check counting.** Lead forms and calls should normally count "One" per click. Google states that count changes only apply to future conversions, so note the date you changed them.
5. **Check which goals each campaign uses.** Confirm whether campaigns follow account-default goals or campaign-specific goals, and whether any custom goal pulls in secondary actions. A campaign-level override is easy to forget.
6. **Fire a test conversion for every primary action.** Submit the form and place a test call, then confirm each records once, not twice. Our [account handoff checklist](/digital-news/google-ads-account-handoff-checklist/) uses the same step when an account changes hands.
7. **Log the change and wait.** Record what changed and why in your [weekly Google Ads change log](/digital-news/weekly-google-ads-change-log/). Google advises giving the system one to two conversion cycles to adapt when goals change, so judge results after that window rather than the next morning.

## What to expect after you clean it up

Expect the reported conversion count to drop once duplicates and soft actions leave the primary column. The leads were never there; the account is simply reporting closer to the number your front desk already knows.

Cost per conversion will usually rise on paper for the same reason, and bidding may need time to settle. This is when people get nervous and ask to switch things back, so agree in advance which number you will judge success by, ideally qualified leads from your own records, shown in a [marketing report](/digital-marketing-reporting/) next to the Google Ads figures.

A cleaner conversion setup does not guarantee more leads. It makes sure that whatever the account learns, it learns from the actions that matter to your business. If volume is the real constraint rather than measurement, our piece on [budget-limited vs demand-limited Google Ads](/digital-news/budget-limited-vs-demand-limited-google-ads/) is the better next read.

## Frequently asked questions

### Do secondary conversions affect Smart Bidding?

Not in a standard setup. Google describes secondary actions as observation only. The exception is a custom goal: a secondary action inside a custom goal is used for bidding once that goal is set on a campaign.

### Why is my "All conv." number higher than "Conversions"?

"All conv." includes secondary actions as well as primary ones, so it is almost always the larger figure. A large gap is worth a look, because it often means useful actions are sitting as secondary or that soft actions such as page views are inflating the total.

### Should I count lead form conversions as "One" or "Every"?

For most lead forms, "One". Google's counting guidance says "One" counts a single conversion per ad click and suits leads, while "Every" suits sales. Changes only apply to future conversions, so past reports keep the old counting.

### Can I make a GA4 key event a primary conversion in Google Ads?

Yes. Google states that conversions imported from Google Analytics are secondary by default and can only be changed to primary inside Google Ads. Before promoting one, check that a native Google Ads tag is not already tracking the same action as primary.

### How long should I wait after changing primary actions?

Google suggests allowing one to two conversion cycles for the system to adapt to new goals. A conversion cycle is the usual gap between the ad click and the conversion, so it varies by business. If most leads arrive within a few days of the click, we still like at least two weeks of data before judging, because small accounts produce noisy numbers; if people take weeks to decide, wait longer.

## Want a second set of eyes on your conversion setup?

Primary and secondary settings take minutes to change and months to cost you if they are wrong. If you are not sure what your account is bidding toward, book a free 30-minute consultation and we will talk through how your conversions are set up, which questions to ask of your current setup and where we would start. You can also learn more about how we run [Google Ads management](/ppc-advertising/) for service businesses.

**[Book My Free Consultation](/contact/)**
