# Client profiles

Each client folder has two reference files:

- **`CLIENT.md`:** who the client is and how we work with them. It covers 13 sections: overview, services they do and don't offer, geography, competitors, SEO status, scope, PPC, content rules, priorities, social, working rules and tool IDs, open items, and gaps.
- **`keywords.md`:** tracked keywords, which keyword goes to which page, PPC keywords and negatives, keyword rules with dates, and opportunities.

**Before starting any client task, load that client's `CLIENT.md`.** For keyword or content work, load `keywords.md` too. The agency's own profile, standards and full client roster are in [thinkprofits/CLIENT.md](thinkprofits/CLIENT.md).

All profiles are **DRAFT v0.1, built 2026-10-06/07** from Slack, Drive, Semrush, GSC, the live sites and this repo. Facts marked *confirm* are unverified. Don't use them in client-facing work until they've been checked.

## Index

| Client | Profile | Keywords | Domain |
|---|---|---|---|
| AANMC | [CLIENT.md](aanmc/CLIENT.md) | [keywords.md](aanmc/keywords.md) | aanmc.org |
| Aloha Life Massage | [CLIENT.md](aloha-life-massage/CLIENT.md) | [keywords.md](aloha-life-massage/keywords.md) | alohalifemassage.com |
| Clearset VAC Truck | [CLIENT.md](clearset/CLIENT.md) | [keywords.md](clearset/keywords.md) | clearsetvactruck.ca |
| Jamie Davis Towing | [CLIENT.md](jamie-davis/CLIENT.md) | [keywords.md](jamie-davis/keywords.md) | jamiedavistowing.com |
| John Sadler Plumbing & Heating | [CLIENT.md](john-sadler/CLIENT.md) | [keywords.md](john-sadler/keywords.md) | johnsadler.ca |
| Mujo Learning Systems | [CLIENT.md](mujo/CLIENT.md) | [keywords.md](mujo/keywords.md) | mujo.com |
| Munro & Crawford | [CLIENT.md](munro-crawford/CLIENT.md) | [keywords.md](munro-crawford/keywords.md) | munrocrawford.ca |
| MVP Athletic Supplies | [CLIENT.md](mvp/CLIENT.md) | [keywords.md](mvp/keywords.md) | mvpathleticsupplies.com |
| MySaskFarm | [CLIENT.md](mysaskfarm/CLIENT.md) | [keywords.md](mysaskfarm/keywords.md) | mysaskfarm.com |
| SPIEDR | [CLIENT.md](spiedr/CLIENT.md) | [keywords.md](spiedr/keywords.md) | spiedr.com |
| ThinkProfits (agency) | [CLIENT.md](thinkprofits/CLIENT.md) | [keywords.md](thinkprofits/keywords.md) | thinkprofits.com |
| Vision Plumbing Heating Cooling | [CLIENT.md](Vision/CLIENT.md) | [keywords.md](Vision/keywords.md) | visionplumbingandheating.com |
| Wiseworth Canada Industries | [CLIENT.md](wiseworth/CLIENT.md) | [keywords.md](wiseworth/keywords.md) | wiseworth.com |

## Known gaps across all profiles

- **Gmail:** not read. The connector failed with an auth error, so there's no client email history in any profile.
- **BrightLocal:** tool errors, so no live review or citation data.
- **Semrush:** the API units balance hit zero on 2026-10-07. Clearset, Vision, Munro & Crawford, MySaskFarm, Mujo, MVP and ThinkProfits have partial or no live rank data. Several projects also return "campaign not found" for position tracking.
- **GSC:** no agency access for johnsadler.ca or jamiedavistowing.com.

## Keeping these current

- **Update the profile in the same commit** as any work that changes a client fact (a new service, an area dropped, a new approver, a keyword rule).
- **Tick off items** in section 12 (Open items) as they're done.
- **Bump the status line** to "Reviewed by <name>, <date>" once someone has checked a profile.
