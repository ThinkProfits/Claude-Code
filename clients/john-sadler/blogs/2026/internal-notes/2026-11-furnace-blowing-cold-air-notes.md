# Internal notes: 2026-11-furnace-blowing-cold-air

Not client facing. Never paste into the Google Doc.

## Scope

> **EDITOR ONLY (remove before publishing):** This is a troubleshooting guide for a gas or electric forced-air furnace that runs but blows cold air. It covers the thermostat, filter, vent and condensate-drain checks a homeowner can safely make, the burner and ignition faults that need a licensed gas fitter, duct problems, and dual fuel heat pump behaviour, then leads into booking furnace repair.
>
> **Masterlist slot:** November 2026 (#1). The topic is "Why Is My Furnace Blowing Cold Air?", proposed-topics row 1 (furnace blowing cold air, Needs PM Review). Chosen by Francis 2026-11-11.

## Image Note

*All images must be real John Sadler job photos. Never use AI-generated images.* There are only a few confirmed real photos on file. Ask Tina for furnace or burner shots, or check the client's Instagram, where Andrew found more real job photos on 2026-11-10.

---

## GBP Post

Furnace blowing cold air? Before you call, set the thermostat fan to Auto, check that it's on Heat, and replace the air filter, since a clogged filter can make the furnace shut off its burners while the fan keeps running. Still cold? Our licensed gas fitters repair furnaces across South Surrey, White Rock and Langley.

**Q: Why does my furnace blow cold air for a minute first?** That's usually normal. The burners heat up before the blower starts, so the first air can feel cool.

**Q: Can a dirty filter cause cold air?** Yes. A clogged filter makes the furnace overheat, and a safety switch shuts off the burners.

**CTA button:** Learn more (link: [blog URL])

---

## Facebook Post

Turned up the heat and got cold air from the vents? There are a few quick checks worth making before you book a service call. Our new guide walks through the thermostat, filter and vent checks, and when it's time to call a technician: [blog URL] #SurreyBC #FurnaceRepair

## Instagram Post

Furnace blowing cold air? Check the fan setting, the filter and the vent pipes outside first. Still cold? We can help. Full guide at the link in our bio. #SurreyBC #WhiteRock #Langley #FurnaceRepair

---

## Implementation Notes

- **Publish timing:** Publish as soon as it's approved. Keyword Planner (Canada) shows searches rising from September, at 1,000 in November and a peak of 1,600 in December, then falling below 100 a month from June to August. Under the 2026-11-10 rule, it can go out on schedule without waiting for approval.
- **Cannibalisation check (2026-11-11, against all 70 live posts via the REST API):**
  - No existing post targets "furnace blowing cold air". None of the furnace posts mention cold air from the vents.
  - Partial overlap: /blog/home-heating-issues/ (filter, furnace switched off, tripped breaker), /blog/what-to-do-if-furnace-breaks-down/ (filter, condensate, reset, vent) and /blog/why-does-my-furnace-keep-shutting-off/ (filter, flame sensor, short cycling).
  - This post is scoped to the cold-air symptom and links to the short-cycling post instead of repeating it.
  - Consider consolidating the two thin older posts into this one later.
  - Also overlaps Oct 2025 #2 "What to Do if My Furnace Won't Start?" (with the client). That one covers a furnace that doesn't run at all, and this one covers a furnace that runs but blows cold air. Once both are live, link them to each other.
- **Title:** The proposed topic is "Why Is My Furnace Blowing Cold Air?". The title tag and H1 lead with "furnace blowing cold air" (590) rather than the question form (260), which is used as the first FAQ. Masterlist volumes (880) were Semrush; this post uses Keyword Planner Canada.
- **Schema:** FAQPage for the five FAQs, and Article (BlogPosting) for the post.
- **Internal links (7 distinct pages, all live, checked 2026-11-11):**
  - /blog/comparing-different-thermostats/
  - /blog/furnace-filter/
  - /blog/why-does-my-furnace-keep-shutting-off/
  - /blog/furnace-leaking-water/
  - /services/heating-cooling/heat-pumps/ (repair copy is live since 2026-11-09)
  - /services/heating-cooling/furnace-repair/
  - /contact-us/
  - plus the phone link
- **External links (2), both verified loading 2026-11-11.** Open both in a new tab with rel="noopener noreferrer".
  - Natural Resources Canada, "Guide to maintaining your home heating and cooling system". It says to "inspect, clean, or change air filters regularly" and to follow the owner's manual for frequency.
  - FortisBC, "Gas leaks and odours": 1-800-663-9911 (24 hours) or 911, call once outside, leave the door open behind you.
- **People Also Ask:** No live PAA pull, because Semrush API units were exhausted on 2026-11-11. The FAQs were chosen from questions that recur across the top-ranking pages (fan On vs Auto, warm-up delay, filter, reset, safety). Re-check with Semrush `phrase_questions` once units are restored.
- **Left out or not verified:**
  - No prices.
  - No same-day or emergency claims (unconfirmed).
  - No oil or propane (out of scope).
  - No specific blower-delay time ("a minute or two" is used instead).
  - No exact lockout duration.
  - The "most furnaces installed in the last 20 years are high-efficiency" line is a general statement, not a statistic. Drop it if Colin disagrees.
  - Brands in the CTA come from the client's serviced-brands list.
- **Colin to confirm:**
  - that their technicians clean or replace flame sensors as part of a repair
  - the dual fuel switchover description
  - whether they want the "turn it off at the power switch and back on once" reset advice in the FAQ
- **Phone link:** The Google Doc conversion dropped the `tel:+16045314355` link on (604) 531-4355 in the CTA. Make it a clickable `tel:` link at implementation so CallRail can swap it.
- **Review:** Run the blog-review-prompt in a fresh chat before sending to the editor.
