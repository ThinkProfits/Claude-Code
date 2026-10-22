**Scope (editor review only, delete before publishing):** Error-code explainer for Navien central air conditioners: the NAA series (letter codes such as F0, P2, H5) and the NAE series (numbered alarm and error codes such as 251 and 201), with a short section on how faults on the paired NAS air handler and NAM cased coil show up. Covers what the codes mean, what a homeowner can safely check, and when to call a technician. It does not cover AC sizing, rebates or installation.

**Masterlist:** May 2026, Blog #2 (row 71), "Navien Air Conditioner Error Codes Explained" (topic approved). Series: NAA, NAE (plus NAS and NAM context).

**Title tag:** Navien Air Conditioner Error Codes: NAA & NAE | John Sadler (59 characters)

**Meta description:** Navien air conditioner error codes for NAA and NAE models: what each code means, which ones reset on their own, safe checks, and when to call a technician. (155 characters)

**URL slug:** /blog/navien-air-conditioner-error-codes/

**Primary keyword:** navien air conditioner error code (Keyword Planner CA: 0/mo; AEO target, tracked at category level per CLIENT.md).
**Secondary keywords:** navien air conditioner (30/mo CA, masterlist 20), navien air conditioning (30, masterlist 20), navien naa (10), navien nae, ac error codes.
**Search intent:** Informational/troubleshooting. The reader's Navien AC has stopped cooling or is showing a code, and they want to know what it means and whether to call.

---

# Navien Air Conditioner Error Codes Explained: NAA and NAE

> **Quick Answer (Preformatted block):** Navien air conditioner error codes show on a display on the outdoor unit's control board. The NAA series uses letter codes like F0 (communication failure), P2 (low pressure protection) and H5 (repeated low pressure), while the NAE series uses numbered alarm codes that reset on their own and error codes that lock the unit off until a technician clears them. A code that keeps returning needs a licensed technician.

When the air conditioning quits on a hot July afternoon in Surrey, the first question is whether it's something simple. Navien air conditioner error codes help answer that, because each one points to a specific sensor, pressure limit or electrical protection. The catch is that Navien's two AC lines report problems in different ways, so it helps to know which one you have.

This guide covers the codes in Navien's NAA and NAE installation and operation manuals, plus how problems with the indoor coil or air handler tend to show up. John Sadler Plumbing & Heating is a Navien Certified Service Specialist in Surrey, BC, and our [air conditioning services](https://www.johnsadler.ca/services/heating-cooling/air-conditioning/) cover homes across Surrey, White Rock and Langley. If you're comparing systems, our guide to [heat pumps versus AC units](https://www.johnsadler.ca/blog/heat-pump-vs-ac-unit/) explains the difference.

[IMAGE: Navien air conditioner outdoor unit beside a Surrey home in summer | alt: Navien air conditioner outdoor unit installed at a home in Surrey, BC | file: navien-air-conditioner-error-codes-surrey.jpg]

## Where Navien AC Codes Appear

Both the NAA and NAE show their codes on a small display on the control board inside the outdoor unit, behind the service panel. You won't usually see them from inside the house, so most homeowners first notice a symptom: warm air from the vents, an outdoor unit that won't start, or a fan running without any cooling.

Please don't open the outdoor unit to look for the display. The board carries line voltage, and both series use R-454B, a refrigerant Navien's manuals treat as flammable and require qualified technicians to handle. Write down what you're noticing and when it started, and let the technician read the code.

## NAA Series Error Codes

The NAA is Navien's standard central air conditioner, and its codes use a letter followed by a number or letter. The letter tells you the type of problem.

### F Codes: Sensor and Communication Faults

F codes mean a sensor, memory chip or communication link isn't reporting properly.

- **F0, Communication failure (outdoor unit), and H0, Communication fault of master board and driver chip:** a communication problem on the outdoor unit.
- **F1, Low pressure switch error:** the low pressure switch isn't reading as expected.
- **F4 to F8:** errors from the outdoor ambient (T4), discharge (T5), condensing (T3) and T7 temperature sensors.
- **F9, AC overvoltage/undervoltage protection:** incoming power is outside the safe range.
- **FA to FF:** memory (EEPROM) failures and errors from the IPM sensor, pressure sensor or a disconnected T3, T5 or condenser sensor.

### P and H Codes: Protective Shutdowns

P codes mean the AC stopped itself to prevent damage. H codes mean the same protection tripped several times in a short window, so the unit locks out.

| Code | What Navien's manual calls it |
|---|---|
| P1 | High pressure switch error |
| P2 | Low pressure protection |
| P3 | Inverter overcurrent protection |
| P4 | T5 compressor discharge temp sensor high temp protection |
| P5 | T3 condenser sensor high temp protection |
| P6 | IPM protection |
| P8 | IPM high temperature protection |
| P9 | DC fan motor error |
| PC | Wet operation error |
| H1 | T3 sensor high temperature error (3 times P5 within 180 minutes) |
| H2 | High pressure switch error (3 times P1 within 150 minutes) |
| H4 | IPM modular high temp error (3 times P8 within 120 minutes) |
| H5 | Low pressure error (5 times P2 within 240 minutes) |
| H6 | Discharge temperature abnormal error (3 times P4 within 100 minutes) |
| H7 | Moisture exposure operation error (3 times PC within 200 minutes) |
| H8 | T3 condenser sensor disconnect error (3 times FE within 120 minutes) |
| HC | Discharge temp sensor disconnect error (3 times FE within 180 minutes) |
| HE | Condensate error (3 times within 60 minutes) |

Source: Navien NAA Air Conditioner Installation and Operation Manual, section 4.5.2, from [Navien's NAA downloads page](https://www.navieninc.com/products/naa17v36/downloads).

### L, d and Other Status Codes

L codes (L0, L1 and LA to LF) mean the AC is limiting its own speed because of voltage, pressure, temperature or current, and ATL is an overtemperature protection. d0 (oil return mode), dC (force cooling, a technician test mode) and PRH (crankcase heater warming up before start) are normal status messages, not faults.

## NAE Series Alarm and Error Codes

The NAE is Navien's hydro air conditioner. It sprays water onto the outdoor coil to help it shed heat, so it has a water supply line, nozzles and an air intake filter that the NAA doesn't. It also reports problems with three-digit numbers on its display, and Navien's manual splits them into three types:

- **Alarm codes:** a warning. The unit stops, then restarts on its own after a set time once it's safe to do so.
- **Error codes:** the same alarm has happened repeatedly, so the unit shuts down and stays off until the problem is fixed and the error is reset.
- **Minor codes:** a small issue the unit can keep running with, though Navien still recommends an inspection.

During normal operation, the display shows a status instead: ST.10 (standby), ST.20 (initial startup), ST.30 (normal operation) or ST.40 (post-stop delay).

| Code range | What Navien's manual says it covers | Resets |
|---|---|---|
| 251 to 260 | Alarms for high pressure, low pressure, discharge temperature, compression ratio, overcurrent, heatsink, compressor temperature, suction temperature, superheat and the high pressure switch | Automatically |
| 851 to 874 | Alarms for inverter and electrical trips, such as communication, current sensors, voltage, fan motor and board temperature | Automatically |
| 201 to 210 | Errors triggered when alarms 251 to 260 repeat (four times for most, three for 258 to 260) | Manual |
| 501 to 507, 561, 562 | Temperature sensor and pressure sensor open or short faults | Automatic once the fault clears |
| 702 | Outdoor unit to inverter driver communication failure | Automatic once the fault clears |
| 801 to 824 | Errors triggered when inverter alarms 851 to 874 repeat four times | Manual |
| 999 | Error of unknown cause | Manual |

Source: Navien NAE Series Installation and Operation Manual, section 7, from [Navien's NAE downloads page](https://www.navieninc.com/products/nae28v36/downloads). The manual notes that the alarm count resets after one hour of continuous normal operation.

For the high pressure and discharge temperature codes (251, 253, 201, 203), Navien's troubleshooting steps start with the water side: is the water spraying properly, and is the air intake filter clean? Its manual says the air intake filter can be removed and cleaned with the unit off, and that the main water valve should be open. For the low pressure codes (252, 202), the first checks are the indoor filter and indoor airflow.

[IMAGE: Close-up of a Navien NAE outdoor unit showing the water supply connection | alt: Water supply line connected to a Navien NAE hydro air conditioner outdoor unit | file: navien-nae-water-supply.jpg]

## What About the NAS Air Handler and NAM Coil?

Navien's NAS air handlers and NAM cased coils are the indoor half of the system, and their manuals don't include error code tables of their own. When something goes wrong indoors, such as low airflow from a clogged filter, it usually shows up as a pressure code at the outdoor unit instead.

There's one indoor behaviour worth knowing about. Both use a refrigerant leak sensor, and Navien's NAM manual explains that if it detects a leak, the system goes into leak mitigation mode: the indoor blower runs and the outdoor unit is disabled. If your fan is running but the outdoor unit won't start and you're getting no cooling, call a technician and mention it.

## What You Can Safely Check, and When to Call

A few checks are safe for any homeowner:

1. **Check the thermostat.** Make sure it's set to cool and the set temperature is below the room temperature.
2. **Check the breakers.** Reset a tripped breaker for the outdoor unit or air handler once. If it trips again, leave it off and call.
3. **Check the indoor filter.** A clogged filter restricts airflow and is a common trigger for low pressure codes.
4. **Clear the outdoor unit.** Keep leaves, grass clippings and stored items away from it so air can move freely.
5. **On an NAE, check the water.** Make sure the water supply valve to the unit is open and the air intake filter is clean.

Call for service when cooling doesn't return after these checks, when the unit shuts down repeatedly, or when the indoor fan runs but the outdoor unit won't start. Refrigerant and electrical work belong with a certified technician.

## Get Your Navien AC Cooling Again

Navien air conditioner error codes follow two systems: letter codes on the NAA, and numbered alarm and error codes on the NAE. In both, a protection that trips once and clears is the unit doing its job, while a lockout code, a code that keeps coming back or a leak mitigation shutdown needs a technician.

As a Navien Certified Service Specialist, we work on Navien heating and cooling equipment, and we've served Surrey, White Rock and Langley for 50 years. Visit our [Navien service page](https://www.johnsadler.ca/services/navien/), read our [Navien heat pump error codes](https://www.johnsadler.ca/blog/navien-heat-pump-error-codes/) guide if your system also heats, or call (604) 531-4355. You can also [contact our team](https://www.johnsadler.ca/contact-us/) Monday to Friday, 8:30 to 5:00.

## Frequently Asked Questions

### Where is the error code on a Navien air conditioner?

Navien NAA and NAE air conditioners show their codes on a display on the control board inside the outdoor unit, behind the service panel. The board carries line voltage, so the panel should only be opened by a qualified technician. Homeowners usually notice a symptom first, such as warm air from the vents.

### What is the difference between an alarm and an error on a Navien NAE?

An alarm is a warning: the unit stops, then restarts on its own once it's safe. An error means the same alarm has happened repeatedly, usually three or four times, so the unit stays off until the cause is fixed and the error is reset. The alarm count clears after one hour of continuous normal operation.

### Why is my air conditioner fan running but not cooling?

A fan that runs without cooling can mean the outdoor unit has stopped on a protection code, a breaker has tripped or the thermostat is set to fan only. On systems with a refrigerant leak sensor, the indoor blower also runs on its own while the outdoor unit is disabled if a leak is detected. If the thermostat and breakers check out, book a service call.

### Can a dirty filter cause an air conditioner error code?

Yes. A clogged indoor filter cuts airflow across the indoor coil, which can lower system pressure and trigger a low pressure protection code. Replacing a dirty filter is one of the first checks to try before calling for service.

*Image note: all images must be real John Sadler photos (team, vans, job sites), never AI-generated or stock.*

---

## GBP Post

AC stopped cooling? Navien air conditioners record a code that points to the cause. Our new guide explains Navien NAA and NAE error codes, which ones reset on their own, what you can safely check, and when to call. Q: Can a dirty filter cause an AC error code? A: Yes, a clogged filter cuts airflow and can trigger a low pressure code, so check it first. Questions? Call our Surrey team at (604) 531-4355.

**CTA button:** Learn more, linking to [blog URL]

## Facebook Post

Warm air from the vents on a hot day? Before you sweat it, check our new guide to Navien air conditioner error codes. It explains what the NAA and NAE codes mean, the safe checks you can do yourself, and when it's time to call us. [blog URL] #SurreyBC #AirConditioning

## Instagram Post

P2, H5, 251, 201: what is your Navien AC trying to tell you? Our latest blog explains Navien air conditioner error codes in plain language. Link in bio. [blog URL] #Navien #AirConditioning #SurreyBC #WhiteRock #LangleyBC

---

## Implementation Notes

- **BLOCKER (from CARD.md): do not publish until the "installs only / refer repairs elsewhere" copy is removed from `/services/heating-cooling/air-conditioning/`.** Checked live on 2026-10-23: the page still says "Why 'installs only' is the right call for AC" and "If you need an AC repair, we'll happily refer you to a trusted local repair contractor." This post links to that page in the intro and invites service calls, which contradicts it. Needs Tina/Colin approval of the edits in `page-update-ac-heat-pump-repair-2026-10-16.md` first.
- **Also confirm with Tina/Colin:** that John Sadler services Navien NAA and NAE units (AC repair is "early stage"). The CTA avoids promising repair turnaround. Best publish window is April to May 2027, ahead of the summer peak ("navien air conditioner" peaks May to July at 50/mo CA).
- **Schema:** FAQPage for the four FAQs (answers have no links and no branded language). Article/BlogPosting with author John Sadler Plumbing & Heating.
- **Source of every code:** Navien NAA Air Conditioner Installation and Operation Manual (Version 1.0, January 2026, section 4.5.2); Navien NAE Series Installation and Operation Manual (Version 1.0, July 2025, sections 3.2 and 7.1 to 7.2); Navien NAM Installation and Operation Manual (Version 1.0, December 2024, "Refrigerant Leak Detection System"); Navien NAS Installation and Operation Manual (Version 1.0, December 2024). All downloaded from navieninc.com on 2026-10-23. The NAA, NAS and NAE service manuals are behind a login and were not used.
- **NAS/NAM claim (masterlist note says faults "surface on paired NAA/NAE display"):** verified only partly. Neither the NAS nor NAM manual has an error code table (confirmed by text search). The NAE manual lists low indoor airflow and a dirty indoor filter as causes of low pressure codes 252/202, which supports "indoor problems show up as outdoor pressure codes". The leak mitigation behaviour (indoor blower on, outdoor unit disabled) is quoted from the NAM manual; the NAS manual references the same refrigerant leak sensor. Colin to confirm whether the NAS/NAM leak alarm also produces a code on the outdoor display (not documented in the manuals reviewed).
- **NAE table reading note for Colin:** the NAE error table PDF prints the codes and names in separate columns, so the pairing in the post (201 to 210 = alarms 251 to 260 repeated; 501/505/506/507 = T_a, TD, TS, T_cond sensors; 561/562 = PD/PS pressure sensors; 702 = outdoor unit to inverter driver communication; 801 to 824 = alarms 851 to 874 repeated; 999 = unknown) follows the order of the names column. Reading the reset column line by line gives 201 to 210 = Manual, 501 to 702 = Auto, 801 to 999 = Manual, which is what the table shows ("Automatic once the fault clears" is our plain-language reading of Navien's "A = Auto" for error codes). Please confirm against a unit.
- **NAE homeowner steps:** "clean the air intake filter with the unit off" and "check the main water valve" come from Navien's own E201/E203 troubleshooting flowcharts in the I&O manual. Nozzle replacement is described there as a service-centre job and is not suggested to homeowners.
- **Cannibalization check (johnsadler.ca sitemaps, pulled 2026-10-23):** no existing post covers Navien AC codes. `/blog/heat-pump-vs-ac-unit/`, `/blog/can-i-install-ac/` and `/blog/know-before-installing-heat-pump-ac/` are buying content. The 2025-backlog draft "AC Not Blowing Cold Air?" covers general symptoms for any AC brand; this post is Navien code-specific. Link the two to each other once both are live.
- **Internal links (5 distinct, meets the 5 minimum):** /services/heating-cooling/air-conditioning/, /blog/heat-pump-vs-ac-unit/, /services/navien/, /blog/navien-heat-pump-error-codes/ (sibling post, not live yet: publish together or hold the link), /contact-us/. If the sibling link has to wait, add /blog/can-i-install-ac/ or /blog/furnace-filter/ (filter section) to keep five. Note: /blog/heat-pump-vs-ac-unit/ still quotes an outdated "$10,000" rebate (flagged in the 2025 backlog README); fix that before linking traffic to it, or swap the link for /blog/ac-heat-pump-ductless-split/.
- **External links (2 Navien downloads pages, both verified loading 2026-10-23, open in new tab with rel="noopener noreferrer"):** NAA and NAE product downloads pages, placed under the reference tables as citations. No gas safety link is needed (electric cooling equipment).
- **Wording decisions:** "certified technician" for refrigerant work rather than naming a specific BC certificate (not verified). No prices, rebates, 24/7 or emergency claims.
- **PAA research:** Semrush returned "no API units" on 2026-10-23 and Keyword Planner has no question data. FAQs follow common AC troubleshooting question patterns (where is the code, alarm vs error, fan running but not cooling, dirty filter). Re-check with Semrush `phrase_questions` (database ca) once units are restored.
- **Images:** 3 placements, all must be real John Sadler photos, never AI or stock.
- **Quick Answer:** use the WordPress Preformatted block.
- **Review:** run the blog-review-prompt on this draft in a fresh chat before it goes to the editor.
