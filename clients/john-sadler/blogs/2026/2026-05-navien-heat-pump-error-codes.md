**Scope (editor review only, delete before publishing):** Error-code explainer for the Navien NAZ heat pump (outdoor unit): every code in Navien's published NAZ table, grouped by letter family, including the normal "running indication" codes like dF (defrost), plus what a homeowner can safely check and when to call a technician. It does not cover heat pump sizing, rebates or installation.

**Masterlist:** May 2026, Blog #1 (row 70), "Navien Heat Pump Error Codes Explained" (topic approved). Series: NAZ.

**Title tag:** Navien Heat Pump Error Codes: NAZ Guide | John Sadler (53 characters)

**Meta description:** Navien heat pump error codes for the NAZ series: what F, P, H and L codes mean, which ones are normal (like dF for defrost), and when to call a technician. (155 characters)

**URL slug:** /blog/navien-heat-pump-error-codes/

**Primary keyword:** navien heat pump error codes (Keyword Planner CA: 0/mo; AEO target, tracked at category level per CLIENT.md).
**Secondary keywords:** navien heat pump (50/mo CA, masterlist 30), navien naz (10), heat pump error codes, heat pump defrost mode.
**Search intent:** Informational/troubleshooting. The reader has a Navien heat pump that has stopped heating or cooling, or a code a technician mentioned, and wants to know what it means.

---

# Navien Heat Pump Error Codes Explained: NAZ Series

> **Quick Answer (Preformatted block):** Navien NAZ heat pump error codes appear on a small segment display on the outdoor unit's control board. Codes starting with F point to a sensor or communication fault, P codes are protective shutdowns, H codes mean a protection tripped repeatedly, and L codes mean the unit has slowed itself down. Some codes are normal, such as dF during a defrost cycle, but an F or H code that keeps returning needs a licensed technician.

A heat pump that stops heating on a cold morning, or stops cooling in July, usually has a reason, and the Navien NAZ keeps a record of it. Navien heat pump error codes are short letter and number combinations that tell a technician which sensor, pressure limit or electrical protection stopped the system.

This guide covers every code in Navien's NAZ installation and operation manual, grouped so they're easier to understand. John Sadler Plumbing & Heating is a Navien Certified Service Specialist in Surrey, BC, and our [heat pump services](https://www.johnsadler.ca/services/heating-cooling/heat-pumps/) cover Navien systems across Surrey, White Rock and Langley. If you're still deciding how a heat pump fits with your existing heating, our guide to [heating with a heat pump or furnace](https://www.johnsadler.ca/blog/heating-with-heat-pump-or-furnace/) is a good place to start.

[IMAGE: Navien NAZ heat pump outdoor unit on a concrete pad beside a Surrey home | alt: Navien NAZ heat pump outdoor unit installed at a Surrey home | file: navien-heat-pump-error-codes-surrey.jpg]

## Where Navien Heat Pump Codes Appear

Unlike a boiler or hydro furnace, the NAZ doesn't have a front panel you can read from the hallway. Its codes show on a segment display on the main control board inside the outdoor unit, behind the service panel. Technicians can also read system data through Navien's Multikit app, which Navien's manual describes as a contractor tool rather than a homeowner app.

That means most homeowners first notice a symptom, not a code: no heat, no cooling, an outdoor unit that won't start, or a fan that runs without the compressor. Please don't remove the outdoor unit's panels to look for the display. The control board carries line voltage, and the NAZ uses R-454B refrigerant, which Navien's manual says must only be handled by qualified technicians following its flammable refrigerant safety procedures.

## Normal Codes That Aren't a Problem

Several codes on the NAZ display are status messages, not faults. If a technician mentions one of these, or you see one while the unit is running normally, there's nothing to fix.

- **dF, running in defrost mode:** in heating mode, frost builds up on the outdoor coil, and the unit reverses briefly to melt it. Navien's manual says defrost ends once the coil reaches 64°F (17.8°C) for one minute or after 8 minutes, whichever comes first. Steam and dripping water from the outdoor unit during this time are normal.
- **d0, running in oil return mode:** the system is moving compressor oil back where it belongs.
- **dC, running under force cooling mode:** a test mode technicians use when checking the refrigerant charge.
- **PRH, crankcase heater in progress, no start-up:** the compressor is warming up before it starts, which is common after a power outage or on a cold day.

A short pause during defrost or a delay on startup is the heat pump protecting itself. A system that never restarts is a different story.

## F Codes: Sensor and Communication Faults

F codes mean a sensor, memory chip or communication link isn't reporting properly. These almost always need a technician with a meter.

- **F0, Communication failure (outdoor unit):** the outdoor unit isn't communicating as expected, which can involve wiring between the indoor and outdoor units.
- **F4, F5, F6 and F7:** errors from the outdoor ambient (T4), compressor discharge (T5), condensing (T3) and T7 temperature sensors.
- **F8, T7 temperature sensor error in detecting condensate risks:** a fault with the sensor that helps prevent condensation on the control board.
- **F9, AC overvoltage/undervoltage protection:** incoming power is outside the safe range.
- **FA and FB, EEPROM failure:** a memory fault on the outdoor board or the driver chip.
- **FC, FD, FE and FF:** errors from the IPM module sensor, the pressure sensor (HLP), a disconnected T3 or T5 sensor, and a disconnected condenser sensor (HPS).

F9 is the one code in this group where the cause may sit outside the heat pump. Repeated voltage faults are worth mentioning when you call, since a technician may need to check the supply wiring as well as the unit.

## P and H Codes: Protective Shutdowns

P codes mean the heat pump stopped itself to prevent damage. H codes mean the same protection has tripped several times in a short period, so the unit locks out instead of trying again.

| Code | What Navien's manual calls it |
|---|---|
| P1 | High pressure switch error |
| P2 | Low pressure protection |
| P3 | Inverter overcurrent protection |
| P4 | T5 compressor discharge temp sensor high temp protection |
| P5 | T3 condenser sensor high temp protection (in cooling mode) |
| P6 | IPM protection |
| P8 | IPM high temperature protection |
| P9 | DC fan motor error |
| PC | Wet operation error |
| PD | High pressure abnormal error (in heating mode) |
| H0 | Communication fault of master board and driver chip |
| H1 | T3 sensor high temperature error (3 times P5 within 180 minutes) |
| H2 | High pressure switch error (3 times P1 within 150 minutes) |
| H3 | High pressure abnormal in heating mode (3 times PD within 180 minutes) |
| H4 | IPM modular high temp error (3 times P8 within 120 minutes) |
| H5 | Low pressure error (5 times P2 within 240 minutes) |
| H6 | Discharge temperature abnormal error (3 times P4 within 100 minutes) |
| H7 | Moisture exposure operation error (3 times PC within 200 minutes) |
| H8 | T3 condenser sensor disconnect error (3 times FE within 120 minutes) |
| HC | Discharge temp sensor disconnect error (3 times FE within 180 minutes) |
| HE | Condensate error (3 times within 60 minutes) |

Source: Navien NAZ Installation and Operation Manual, section 4.7.2, from [Navien's NAZ downloads page](https://www.navieninc.com/products/naz-17v36/downloads).

Pressure codes like P1, P2, PD, H2 and H5 are often tied to airflow or refrigerant problems. A blocked outdoor coil, a clogged indoor filter or a low refrigerant charge can all push pressures out of range. You can clear leaves, snow and ice from around the outdoor unit and check the indoor filter, but refrigerant work is for a certified technician only.

## L Codes and Other Limits

L codes mean the heat pump is still running but has limited its own speed, or has stopped briefly because of a power issue.

- **L0 and L1, DC bus low or high voltage protection:** the unit's internal DC voltage is out of range.
- **LA, Frequency limitation by voltage:** the compressor has slowed because of supply voltage.
- **LB, LC, LD, LE and LF:** the compressor has slowed because of high pressure, condenser temperature, discharge temperature, IPM module temperature or current.
- **ATL, Overtemperature protection:** a temperature limit has been reached.

An occasional L code on a very hot or very cold day is the system managing itself. If you notice the heat pump struggling to keep up for days at a time, it's worth having a technician look at why it keeps limiting.

## What You Can Safely Check, and When to Call

Most of what a homeowner can do happens at the thermostat and around the outdoor unit:

1. **Check the thermostat.** Make sure it's set to the right mode (heat or cool) and that the set temperature is above or below the room temperature as needed.
2. **Check the breakers.** A tripped breaker for the outdoor unit or the indoor air handler will stop the system. Reset it once; if it trips again, leave it off and call.
3. **Clear the outdoor unit.** Remove snow, ice, leaves or anything stored against it. Navien's manual calls for placing the unit so roof water and snow can't fall directly on it, so ongoing ice buildup is worth mentioning.
4. **Check the indoor filter.** A clogged filter restricts airflow and can trigger pressure protection codes.

If your NAZ is paired with a gas furnace in a dual-fuel setup, the gas safety rules still apply: if you smell gas, leave the home and call FortisBC at 1-800-663-9911 or 911.

Call for service if the system stops heating or cooling after these checks, if it shuts down repeatedly, or if a technician has already found an F or H code. If your NAZ is paired with a Navien furnace, our guide to [Navien furnace error codes](https://www.johnsadler.ca/blog/navien-furnace-error-codes/) covers the indoor side, and the [Navien air conditioner error codes](https://www.johnsadler.ca/blog/navien-air-conditioner-error-codes/) guide covers Navien's cooling-only units.

[IMAGE: John Sadler technician servicing a Navien heat pump outdoor unit with the service panel removed | alt: Technician diagnosing a Navien heat pump error code at the outdoor unit | file: navien-heat-pump-service-surrey.jpg]

## Keep Your Navien Heat Pump Running Smoothly

Navien NAZ heat pump error codes fall into clear families: d codes and PRH are normal operation, F codes are sensor and communication faults, P codes are protective shutdowns, H codes are repeated shutdowns, and L codes are self-imposed limits. Homeowners can safely check the thermostat, breakers, outdoor unit and filter, while anything inside the unit is a job for a licensed technician.

As a Navien Certified Service Specialist, we work on Navien heating and cooling equipment every week. Visit our [Navien service page](https://www.johnsadler.ca/services/navien/) to see what we service, then call (604) 531-4355 or [contact our team](https://www.johnsadler.ca/contact-us/) Monday to Friday, 8:30 to 5:00. We've served South Surrey, White Rock and Langley for 50 years.

## Frequently Asked Questions

### Where do I find the error code on a Navien heat pump?

The NAZ shows its codes on a segment display on the main control board inside the outdoor unit, behind the service panel. Because the board carries line voltage and the system uses a flammable refrigerant, the panel should only be opened by a qualified technician. Homeowners usually notice a symptom first, such as no heat or an outdoor unit that won't start.

### What does dF mean on a Navien heat pump?

dF means the heat pump is running a defrost cycle to melt frost off the outdoor coil. Navien's manual says each defrost ends once the coil warms to 64°F (17.8°C) for one minute or after 8 minutes. Steam and water dripping from the outdoor unit during defrost are normal.

### Why does my Navien heat pump keep shutting off?

Repeated shutdowns usually mean a protection is tripping, such as high pressure, low pressure or high discharge temperature. Common causes include a blocked outdoor coil, a clogged indoor filter, ice buildup or a refrigerant problem. When the same protection trips several times in a few hours, the unit locks out with an H code until a technician resets it.

### Is it normal for a heat pump to stop running in cold weather?

Short pauses are normal. In cold, damp weather a heat pump stops heating for a few minutes to run a defrost cycle, and it may wait for its compressor crankcase heater to warm up before starting. A heat pump that stays off for hours, or blows cold air indoors for a long time, needs a service call.

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

Heat pump stopped working, or a technician mentioned a code like dF, P2 or H5? Our new guide explains Navien NAZ heat pump error codes, which ones are normal, what you can safely check, and when to call. Q: What does dF mean on a Navien heat pump? A: It's a normal defrost cycle that melts frost off the outdoor coil, and Navien's manual says it lasts up to 8 minutes. Questions? Call our Surrey team at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

Steam coming off your heat pump in winter? That's usually defrost mode, and it's normal. Our new guide explains Navien NAZ heat pump error codes, which ones need attention, and the safe checks you can do before calling us. [blog URL] #SurreyBC #HeatPump

## Instagram Post

dF, PRH, P2, H5: what is your Navien heat pump trying to tell you? Our latest blog breaks down NAZ heat pump error codes in plain language. Link in bio. [blog URL] #Navien #HeatPump #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **BLOCKER (from CARD.md): do not publish until the "installs only / refer repairs elsewhere" copy is removed from `/services/heating-cooling/heat-pumps/`.** Checked live on 2026-10-23: the page still has a section titled "Why 'installs only' matters for heat pumps". This post links to that page and its CTA invites service calls, so publishing first would send readers to a page that says John Sadler doesn't repair heat pumps. Needs Tina/Colin approval of the page edits in `page-update-ac-heat-pump-repair-2026-10-16.md` first.
- **Also confirm with Tina/Colin:** that John Sadler is happy to promote Navien heat pump diagnosis and service (repairs are "early stage" per the brief). The CTA is worded as "we work on Navien heating and cooling equipment" and "call", without promising repair turnaround.
- **Schema:** FAQPage for the four FAQs (answers have no links and no branded language). Article/BlogPosting with author John Sadler Plumbing & Heating.
- **Publish date:** Masterlist slot is May 2026 (overdue). "navien heat pump" searches peak March to June (90/mo in March), so a February or March 2027 publish works if the blocker isn't cleared sooner.
- **Source of every code:** Navien NAZ Installation and Operation Manual (Version 2.0, July 2026), section 4.7.2 "Error Codes"; defrost figures from section 4.1; display and Multikit details from sections 5 and 6.2. Downloaded from navieninc.com on 2026-10-23. Every code in the NAZ table is in the post, except that F4 to F7, FC to FF and LB to LF are grouped in prose. The NAZ service manual (with fix procedures) is behind a login and was not used.
- **Codes not in Navien's table:** P7, PA, PB, H9, HA, HB, HD, L2 to L9 and F1 to F3 don't appear in the NAZ manual, so they aren't mentioned. (F1 "Low pressure switch error" does appear in the NAA air conditioner table, but not the NAZ one.)
- **Cannibalization check (johnsadler.ca sitemaps, pulled 2026-10-23):** no existing post covers Navien heat pump codes. Related posts (`/blog/heat-pump-vs-ac-unit/`, `/blog/heating-with-heat-pump-or-furnace/`, `/blog/know-before-installing-heat-pump-ac/`, `/blog/choosing-heat-pump-contractor/`) are buying and comparison content. The 2025-backlog draft "How Does a Heat Pump Work?" mentions defrost in general terms; this post covers Navien-specific defrost timing only, so no conflict. Link to it once it's live.
- **Internal links (6 distinct):** /services/heating-cooling/heat-pumps/, /blog/heating-with-heat-pump-or-furnace/, /blog/navien-furnace-error-codes/ and /blog/navien-air-conditioner-error-codes/ (sibling posts, not live yet), /services/navien/, /contact-us/.
- **External links (1, verified loading 2026-10-23, open in new tab with rel="noopener noreferrer"):** Navien NAZ product downloads page (lists the NAZ Installation and Operation Manual). The FortisBC number is stated in the dual-fuel note without a link; it was verified on fortisbc.com the same day.
- **Wording decisions:** "certified technician" is used for refrigerant work rather than naming a specific BC certificate, since that wasn't verified. "Flammable refrigerant" follows the NAZ manual's own safety section ("FLAMMABLE REFRIGERANTS" safety checks for R-454B work). No prices, rebates, 24/7 or emergency claims.
- **PAA research:** Semrush returned "no API units" on 2026-10-23 and Keyword Planner has no question data. FAQs follow common heat pump question patterns (where's the code, what is defrost, why does it keep shutting off, cold weather). Re-check with Semrush `phrase_questions` (database ca) once units are restored.
- **Images:** 3 placements, all must be real John Sadler photos, never AI or stock.
- **Quick Answer:** use the WordPress Preformatted block.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
