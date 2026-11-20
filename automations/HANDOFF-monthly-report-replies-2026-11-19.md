# Handoff: reply to November 2026 client monthly reports (from session of 2026-11-19)

Start a new session in `E:\ThinkProfits\Claude-Code` and paste or point it at this file.

## Goal

Reply to every client's November 2026 monthly report thread in Slack with a short, specific summary: what the report showed, what has been done about it, and what's next. Then keep doing this every month.

Source: Weekly Team Check-in, 2026-11-17 (Gemini notes, [full doc](https://docs.google.com/document/d/17GzIw1xzagRGRhDj8Fi2SmK2iVsPYxp9FYNWZqnnPsk/edit)). Action item: "[Francis Uy] Summarize Reports: Include detailed summaries and specific action plans when replying to client monthly reports. Ensure replies contain enough context for team tracking."

## Andrew's instructions, word for word

From the Gemini transcript, 01:29:16 to the end of the meeting. The transcript is machine-generated, so expect small errors ("cla thing" is probably "Claude thing", "Sean" is Shawn).

> **Andrew Silbernagel:** awesome. And then did you have a chance and or your bot to kind of go through all the monthly reports that came out this month?
>
> **Francis Uy:** Oh,
>
> **Andrew Silbernagel:** And okay,
>
> **Francis Uy:** not yet for this one.
>
> **Andrew Silbernagel:** that's a good one.
>
> **Francis Uy:** But but but I'm but I'm slowly working on it.
>
> **Andrew Silbernagel:** Okay.
>
> **Francis Uy:** I've actually I actually did the spider one while we were talking with Shawn.
>
> **Andrew Silbernagel:** Okay,
>
> **Francis Uy:** So
>
> **Andrew Silbernagel:** awesome. Um, I think a good thing to do is if you're able to, whether it's you manually or just updating whichever cla thing you have doing stuff, um, I think replying to those reports with a little summary of either what you have done based on the report or like what's being done.
>
> **Francis Uy:** What?
>
> **Andrew Silbernagel:** I think with a little detail would be super helpful so that um I know what's up, Sean knows what's up, Claude knows what's up with my bots and everything goes through and it's like, "Oh, the report said this, we summarized this. Francis did this or I did whatever like whoever it is." Um,
>
> **Francis Uy:** Oh, okay. Yeah.
>
> **Andrew Silbernagel:** yeah, I think I think following up with those is just a little more detail on what's being done because a lot of the replies are like, "Oh, I'm on this or I'm working on this or I've got this covered." So,
>
> **Francis Uy:** Yeah. Okay. Yeah.
>
> **Andrew Silbernagel:** yeah, just a little detail.
>
> **Francis Uy:** And no context.
>
> **Andrew Silbernagel:** I'm doing Yeah, it can be super it can be short even if it's just a couple bullet points of this is what I'm going to do or this is what I have done or both if if you've done stuff. Yeah. And then it also will help all of us remember to check up on it or do it later if needed. If it's some like, holy crap, it needs seven new pages and it's going to be a few months to solve this problem. We'll actually remember to follow up on it.
>
> **Francis Uy:** Okay.
>
> **Andrew Silbernagel:** Yeah, I think that would be super helpful. And yeah, I haven't looked at blogs for this month, so I don't know if you've started those or not yet, but that can be a later this week problem.

Background from earlier in the same meeting (01:05:46 to 01:07:00), Andrew describing his automations:

> "on the automation side, what I've got running without any input is mainly my monthly report automations to read all the reviews, come up with synopsises of the reviews, action items from the reviews, and they're pushing it into Slack to Francis and I. Um, and then my and that kind of lives with like the co-work side. So, it's got all of its memories and contacts and it kind of runs a report processor to process the reports."
>
> "sometimes it fails to send a report and it never notifies you that a report was never sent. So I have got an automation that checks the day the couple days after reports are supposed to go out um to warn me in Slack that hey like this last month John Silo didn't get their report."

## Read first

1. `memory/monthly-report-reply-standard.md`: the standing rule in short form
2. `clients/<client>/CARD.md` (status) and `CLIENT.md` (rules, "Monthly report trend" section) for each client before writing its reply

## Where the reports are

- Semrush sends each client's report around the 7th of the month. Andrew's report processor then posts a review (synopsis + action items) as a thread in that client's Slack channel, e.g. `#clearset`, `#firestorm_spiedr`, `#adaptive`.
- Find this month's threads with the Slack connector (search the client channels for messages from about 2026-11-07 onward that contain the review). Don't guess channel names; search.
- Spiedr: Francis replied during the 2026-11-17 meeting. Check that reply against the format below and add detail if it's thin.

## Reply format

Short, bullets, specific. Template:

```
November report (October data), quick summary:
• What stood out: <1-2 key numbers or changes from the report, e.g. GSC clicks -22% MoM, Port Coquitlam visibility up 4 pts>
Done:
• <action already taken because of the report, with a link or page name>
Next:
• <planned action> (<owner>, <rough timing>)
• <long fix, if any, e.g. "needs 3 new city pages, a 2-3 month project"; give it its own line so it gets followed up>
```

Rules for the reply:
- Never write "I'm on it" without saying what "it" is.
- No "Waiting on client:" lines, for any client (Francis, 2026-11-19). Client blockers stay in CARD.md.
- Name the owner when it's not Francis (Andrew, Shawn).
- Don't promise rankings or results; describe actions.
- Canadian English, no jargon the client wouldn't follow (the client may be in the channel).
- SEO only: no Google Ads / PPC / LSA lines (Francis, 2026-11-19).
- Use real numbers from the report thread only. If a figure looks wrong (e.g. the automated review mentions a campaign that doesn't exist), flag it in the reply instead of repeating it.

## Steps

1. List every client channel that got a November report review. Make a checklist table below (client, channel, thread link, status).
2. For each client: read the review thread, the client's CARD/CLIENT files and any work done since the last report (repo files, Teamwork, Slack). Draft the reply in the format above.
3. **Show Francis each draft in chat and wait for his OK before posting.** Posting in Slack is sending a message on his behalf. Approval is per message.
4. After posting, add the month's key numbers to the client's "Monthly report trend" section in `CLIENT.md` and update `CARD.md` if the next steps changed.
5. Log each client in the checklist below. Note any client with no report this month (Andrew's checker should flag these, but list them).

## Checklist (November 2026)

| Client | Channel | Thread | Status |
|---|---|---|---|
Checked in Slack 2026-11-19: 12 report reviews (posted 2026-11-10/11), **none replied**. Spiedr's 2026-11-17 "This is done." went into an older thread, not the November report. Drafts: [monthly-report-replies-2026-11-drafts.md](monthly-report-replies-2026-11-drafts.md).

| Client | Channel | Thread ts | Status |
|---|---|---|---|
| Spiedr | #firestorm_spiedr | 1793991764.756459 | **Posted 2026-11-19**, CLIENT.md trend + CARD updated |
| Munro & Crawford | #munrocrawford | 1794260945.604579 | **Posted 2026-11-19**, SEO only ([link](https://thinkprofitscom.slack.com/archives/C019AAP51U6/p1795043744996069?thread_ts=1794260945.604579&cid=C019AAP51U6)); first version with Ads lines deleted. CLIENT.md trend + CARD updated |
| John Sadler | #johnsadler | 1794268753.591129 | **Posted 2026-11-19** ([link](https://thinkprofitscom.slack.com/archives/C019H8FNN9H/p1795043747338409?thread_ts=1794268753.591129&cid=C019H8FNN9H)), CLIENT.md trend + CARD updated |
| Wiseworth | #wiseworth | 1793991764.957429 | **Posted 2026-11-21** ([link](https://thinkprofitscom.slack.com/archives/C019E04B2AZ/p1795194087245909?thread_ts=1793991764.957429&cid=C019E04B2AZ)), CLIENT.md trend + CARD updated |
| MVP | #mvp | 1793991766.711739 | Draft, has [confirm] |
| AANMC | #aanmc | 1793988326.908629 | Draft, has [confirm] |
| Vision | #vision-plumbing | 1793988331.585869 | **Posted 2026-11-21**, SEO only ([link](https://thinkprofitscom.slack.com/archives/C052P7H4FUG/p1795194086505199?thread_ts=1793988331.585869&cid=C052P7H4FUG)). CLIENT.md trend + CARD not yet updated |
| Mujo | #mujo | 1793991784.903429 | Draft, has [confirm]; client in channel |
| Clearset | #clearset | 1793988332.217269 | **Posted 2026-11-21**, SEO only ([link](https://thinkprofitscom.slack.com/archives/C04BXUMV0ES/p1795194089705219?thread_ts=1793988332.217269&cid=C04BXUMV0ES)). CLIENT.md trend + CARD not yet updated |
| Aloha Life Massage | #aloha-life-massage | 1793991762.316779 | Draft, has [confirm] |
| Jamie Davis Towing | #jamiedavistowing | 1793988327.315509 | Draft, has [confirm] |
| MySaskFarm | #mysaskfarm | 1793988324.092899 | Draft, has [confirm] |

No November review found for: Adaptive, Estate Options, Geraldine Hampton, ThinkProfits, On Guard (may not be on the report automation).

## Later

Once a few months are done by hand, consider a recurring task: around the 9th, draft replies for every new report thread and post them to Francis for approval. Agree this with Andrew first, since it touches his report automation.
