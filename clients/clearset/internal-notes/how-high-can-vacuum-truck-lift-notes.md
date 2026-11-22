# Internal notes: How High Can a Vacuum Truck Lift? (Clearset blog)

> Internal only. Never paste into the client doc. Client-facing draft: `../Clearset - Blog - How High Can a Vacuum Truck Lift.docx`. Drafted 2026-11-21.

## Scope

Informational explainer, revised from Sean's own draft. It covers why suction lift tops out near 34 feet, why real jobs get less, and how Clearset gets past the limit (air injection, inline pumps, diaphragm vs trash pumps). New sections: a site-planning walkthrough and an FAQ. Not on the blog masterlist. Sean wrote it because he hears this question every week.

## What changed from Sean's version (for the reply to Andrew/Sean)

**Kept as written:** title (H1), the opening question, the physics explanation, the 34-foot rule, the real-world limits list, both methods, the pump comparison and the closing section. Almost all of it is still word for word.

**Fixed**
- **Grease removed from "Heavier material."** Grease is lighter than water (it floats in a grease trap), so listing it as denser would be a factual slip a sharp reader could catch. It now says "thick sludge and grit-laden septage."
- Both methods were numbered "1." They're now H3 subheadings.
- Removed a pasted Slack timestamp ("[5:43 PM]") from the inline pumps section.
- The phone number is formatted as (778) 825-1032. The CTA links to the contact page on clearsetvactruck.ca, not clearset.ca, which redirects there anyway.

**Added**
- A "Quick answer" box under the H1, written for Google snippets and AI answers.
- A local line in the intro (Port Moody, Anmore, Fraser Valley acreages).
- An altitude figure: about 2 ft of lift lost per 1,000 ft of elevation (Honda pump theory page). The physics figures are linked to the same source.
- A hose-friction note: thick material drags harder than water.
- New H2 "Planning a Hard-to-Reach Pump-Out: What We Look At." It's a 4-step process and turns "every site is different" into what the customer should tell Clearset.
- An FAQ with 4 questions, none of which repeat an H2.
- 5 internal links and image/video placements where Sean's draft had gaps.

## Keyword research

Semrush MCP was out of API units on 2026-11-21, so the volumes below come from Google Ads Keyword Planner (BC, avg monthly). Rerun in Semrush (KD + phrase_questions) once units reset.

| Keyword | BC vol. | Note |
|---|---|---|
| septic tank pumping | 1,000 | Main commercial head (seasonal peak Jun–Aug) |
| vacuum truck (incl. vac truck) | 480 | Clearset already ranks #1–4 on "vac truck service(s)" |
| septic tank pumping near me | 320 | |
| diaphragm pump / trash pump | 260 each | Mostly equipment buyers, secondary only |
| septic pumping / septic tank cleaning | 210 each | |
| inline pump | 70 | |
| vacuum truck services | 70 | |
| how high can a vacuum truck lift, how far can a septic truck reach, hard to reach septic tank, septic tank pumping steep driveway, 34 foot rule | 0 measured | Expected for question long-tail |

**Read:** the exact question has no measurable volume, which is normal for this kind of long-tail. The post's value is:
1. AEO/AI answers. It's a clean, quotable explanation of a niche question Sean says customers ask weekly.
2. A sales asset Sean can send to "can you reach my tank?" callers.
3. Topical support for the septic pumping and vacuum truck pages through internal links.

Don't promise traffic from it.

**PAA:** Semrush phrase_questions couldn't run. FAQ questions came from forum/SERP research on "septic tank too far / pumped uphill / hose reach" (tractorbynet, InspectApedia, Pumper threads).

**Cannibalization:** none. The site has no published posts (only 2022 "Blog 1–3"/"Test" placeholder drafts) and no page about lift, distance or hard-to-reach tanks. The unpublished "Septic Repair Warning Signs" draft doesn't overlap.

## Images

Sean sent 3 files with Andrew's #clearset post (2026-11-21, ts 1795225352.725389):

| File | Slack ID | What it is | Placement in doc |
|---|---|---|---|
| 20260402_135959.jpg (3.9 MB, 3000×4000) | F0CKBLCKKST | Looking down into a deep concrete wet well (likely a lift station: guide rails, chains, ladder rungs) with a green suction hose running into the liquid | End of "The 34-Foot Rule". Embedded in the docx. Web copy saved at `../blog-media/vacuum-truck-lift/suction-hose-deep-wet-well-pump-out.jpg` (1200×1600, 482 KB). |
| 20260402_135558.mp4 (50.5 MB) | F0CKWNT8PKN | Truck parked outside a home, long hose run going inside the house to pump out the job (described by Francis, 2026-11-21) | End of the intro, under "what it means for you if your tank is hard to reach" |
| 20261106_205402.mp4 (92.6 MB) | F0CKLQRGB27 | A different home, same setup: truck outside, long hose run through the house (described by Francis) | End of "Why Real-World Lift Is Even Lower", after "suction alone won't do it" |

- Both videos show long hose runs into houses, so they sit where the copy talks about tanks with no truck access and long horizontal runs. Neither shows air injection or the inline pumps, so those sections have no media yet. Ask Sean what each house's tank was (septic, holding tank, sump) and roughly how long the hose run was. That would make good captions and video titles.
- If the photo is a lift station job, it could also link to /services/lift-stations-cleaning/. Ask Sean what the job was and how deep the well is. A real depth figure would make a great caption.
- Embed the videos via YouTube or Instagram rather than uploading 50 to 90 MB files to Kinsta (watch page weight; see the 2025 heavy-image crawl issue). Use the compressed photo, not the 3.9 MB original.
- Nice-to-have shots that weren't supplied: the three inline pumps in series, and the 3" diaphragm and trash pumps. Ask Sean if he has them.
- Real Clearset media only, never AI.

## GBP post

"Can you reach my tank? It's way down the hill." We hear it every week. Suction alone can't lift liquid much past 34 feet, so Clearset uses air injection and inline pumps to reach septic and holding tanks other trucks can't. We've pumped over 40 feet of elevation. Read how it works, then call (778) 825-1032 to talk through your site.

CTA button: Learn more → blog URL. (~390 characters.) Photo: the wet well shot (suction-hose-deep-wet-well-pump-out.jpg), or a frame from one of the videos.

## Social posts

**Facebook:** No vacuum truck on earth can lift liquid much past 34 feet with suction alone. Physics says so. Here's how we get past that limit with air injection and inline pumps, and what it means if your tank is way down the hill. [BLOG URL] #SepticPumping #LowerMainland

**Instagram:** Three inline pumps in series plus air injection, all to reach a tank most trucks can't. Here's the physics behind the 34-foot rule and how we work around it. Full breakdown at the link in bio. #VacTruck #SepticPumping #PortCoquitlam

(No emojis. Confirm whether Clearset's own posts use them.)

## Implementation notes

- **Schema:** Article schema with the image. For the FAQ, build the accordion with the Divi class `tp-faq-accordion`, which auto-generates FAQPage schema (CLIENT.md, stack). Don't hand-code it.
- **Blog doesn't exist yet:** the site has no /blog/ page. This would be the first live post if it goes out before the Septic Repair draft, so the blog index and category need setting up. Blogs being in scope is still unconfirmed (CARD.md blocker).
- **Internal links** (5 distinct, all live): /services/septic-tank-cleaning/, /services/holding-tank-cleaning/, /services/storm-drains-catch-basins/, /contact-us/, /septic-tank-service-port-coquitlam/.
- **External link** (1): Honda Power Equipment "Pump Theory," https://direct.powerequipment.honda.com/pumps/pump-theory. Opened 2026-11-21. It confirms 14.7 psi, 33.9 ft, a 26 ft practical lift for centrifugal pumps, and ~2 ft lost per 1,000 ft of altitude. It's a manufacturer page written for US products, but the figures are physics, not regulation. Open in a new tab.
- **Checked against the physics:** 29.92 inHg = perfect vacuum ✔; 33.9 / 1.2 ≈ 28 ft for material 20% heavier ✔; 20–25 ft practical (a fire-service guide uses two-thirds of theoretical, ~22.5 ft) ✔; low-pressure boiling ✔; slug flow from air injection ✔; diaphragm pumps self-prime and run dry ✔.
- **Sean to confirm**
  - "Routinely pumps over 40 feet" is his own claim. Keep it if he's comfortable with "routinely."
  - The three-pumps-in-series job: does he want the location or distance named? A real number (e.g. "X feet of hose, Y feet of head") would make the post much stronger.
  - FAQ "quote before booking" and asking customers for site photos: confirm that's how he works.
  - Whether hard-to-reach jobs cost more (FAQ 3 says "it can," with no figures, per the no-prices rule).
- **Self-check:** about 1,700 words (excluding media markers); 0 em/en dashes; primary keyword 4×; no competitors named; no prices; no septic inspection/repair or potable water mentions; Canadian spelling (vapour).
- **Next:** run the blog-review prompt in a fresh chat, then send to Andrew to relay to Sean.
