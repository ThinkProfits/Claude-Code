# Task: Clearset GBP cleanup, Phase 2 (services)

You are editing the Google Business Profile for **Clearset VAC Truck Services** (Port Coquitlam, BC), managed by **seo@thinkprofits.com** (already signed in). The account owner approved these changes on 2026-10-06/07.

**Prerequisite:** Phase 1 (`gbp-phase1-instructions.md`) must already be done, ideally at least 24 hours earlier. Open Edit profile and check that there are exactly 6 categories: Septic system service (primary), Drainage service, Excavating contractor, Sewage disposal service, Portable toilet supplier, Waste management service. If it's not, **stop and report**.

Background: the profile has hundreds of auto-added services that Clearset doesn't offer (pump sales, demolition, dumpster rental, etc.). Phase 2 leaves only real services. The full audit is in `clients/clearset/gbp-audit-2026-10-06.md`.

## How to open the editor

1. Go to `https://www.google.com/search?q=Clearset+VAC+Truck+Services&hl=en`
2. In the "Your business on Google" panel, click **Edit services**.

## Rules

- **Work by KEEP list.** For each category below, keep only the services named in its KEEP list and remove every other service in that category. Matching is by exact name, ignoring capitalization and punctuation. If you're unsure whether a service matches, keep it and note it in the report.
- **Never** use a category-level "Delete" button. That deletes the whole category. Remove services one at a time, using each service's own remove/delete option.
- Don't change prices or descriptions on kept services unless a RENAME or ADD step says so.
- Don't touch categories, name, address, phone, hours, description or photos.
- Save after finishing each category, and confirm that the save worked before starting the next one.
- If Google shows a verification prompt, a suspension or policy warning, or asks for ID or a phone code, **stop and report**.
- This is a long task (about 400 removals). If you run out of time or context, stop cleanly after a saved category and report which categories are done.

## Category 1: Septic system service (primary)

**KEEP (19):**
Septic tank pumping · Septic tank cleaning · Septic system maintenance · Holding tank pumping · Drain field rejuvenation · Emergency septic service · Septic tank locating · Septic line jetting · Septic system camera inspection · Lift station maintenance · Grease trap cleaning · Storm Drains / Catch Basins · Water Delivery · Residential septic service · Commercial septic service · Septic sludge removal · Trailers And Rv's & Pumping · Hydro Flushing · Vacuum Truck Services

**Remove everything else** in this category, including the vague custom entries "24hr Emergency Services", "Residential Services", "Storage Tanks", "Water Supply Services", "Septic Tank Problems", "Tank Maintenance", "Vac Truck Services" and "Water Hauling".

**RENAME (keep the existing price):**
- "Trailers And Rv's & Pumping" → `Trailer & RV septic pumping`
  Description: `Holding tank and septic pumping for trailers, RVs, campers and job-site trailers across Port Coquitlam, Metro Vancouver and the Fraser Valley. We come to you, pump out, and leave the site clean.`
- "Hydro Flushing" → `Hydro flushing & line jetting`
  Description: `High-pressure hydro flushing and jetting to clear grease, roots, sludge and debris from sewer, septic and drain lines for homes and businesses across Metro Vancouver and the Fraser Valley.`
- "Vacuum Truck Services": keep the name and set the description to:
  `Residential and commercial vacuum truck services from Port Coquitlam: septic and holding tank pumping, catch basins, grease traps, lift stations, hydrovac excavation and liquid waste removal. 24/7 emergency dispatch.`

## Category 2: Drainage service

**KEEP (6):** Drain jetting · Storm drain cleaning · High pressure water jetting · Commercial sewer cleaning · Sewer blockage clearance · Drain maintenance

Remove everything else in this category.

## Category 3: Excavating contractor

**KEEP (4):** Hydrovac excavation · Trenching services · Utility trenching · Soil removal

Remove everything else in this category.

**ADD custom service:**
- Name: `Daylighting & utility exposure`
- Description: `Safe hydrovac daylighting to expose buried gas, water, electrical and telecom lines before digging. Non-destructive excavation for contractors, municipalities and homeowners across Metro Vancouver and the Fraser Valley.`
- No price.

## Category 4: Sewage disposal service

**KEEP (17):** Sewage removal · Sewage tank emptying · Residential sewage disposal · Commercial sewage disposal · Sewer line cleaning · Sewer jetting · Hydro jetting · Lift station cleaning · Holding tank cleaning · Catch basin cleaning · Sludge removal · Wastewater removal · Sewer camera inspection · Septic tank location service · Drain cleaning service · Portable restroom wastewater removal · Car wash sump pump-out

Remove everything else in this category.

## Category 5: Portable toilet supplier

**KEEP (23):** Portable toilet rental · Portable sanitation services · Construction site portable toilets · Event portable toilets · Wedding portable toilet rental · Festival portable restroom rental · Film set portable toilets · Special event restroom rental · Long-term portable toilet rental · Short-term toilet rental · Weekend portable toilet rental · Seasonal portable toilet rental · Emergency portable toilet rental · Temporary toilet rental · Portable bathroom rental · Porta potty for parties · Portable toilet delivery · Portable toilet pick-up service · Portable restroom servicing · Portable toilet cleaning service · Hand washing station rental · RV tank pumping service · Monthly portable toilet rental (weekly servicing included)

Remove everything else in this category (luxury/VIP/deluxe, restroom trailers, showers, sinks, urinals, high-rise, handicap/ADA, flushable, green/eco, office restroom, supplies, hand sanitizer stations, concert, corporate, mobile restroom unit, same day, disaster relief, holding tank rental, deodorizer/odour control).

**UPDATE description** on "Portable sanitation services":
`Complete portable sanitation for job sites, events, farms and film sets: portable toilet rentals, hand wash stations, delivery, scheduled pumping, cleaning, restocking and pickup. Serving Port Coquitlam, Metro Vancouver and the Fraser Valley.`

## Category 6: Waste management service

**KEEP:** none of the existing services. **Remove all of them.** They're all solid-waste services (dumpsters, junk removal, shredding, e-waste, medical, asbestos).

**ADD custom services (no price):**
- Name: `Liquid waste removal`
  Description: `Vacuum truck removal of non-hazardous liquid waste, sludge and wastewater from tanks, sumps, pits and job sites across Metro Vancouver and the Fraser Valley.`
- Name: `Non-hazardous liquid waste disposal`
  Description: `Pump-out, transport and proper disposal of non-hazardous liquid waste for residential, commercial and construction clients in Port Coquitlam and the Lower Mainland.`

## Final check and report

Reopen Edit services and count the services per category. Expected totals: Septic system service 19, Drainage 6, Excavating contractor 5, Sewage disposal 17, Portable toilet supplier 23, Waste management 2 (about 72 in all).

Reply with this report filled in:

```
Clearset GBP Phase 2 report (date/time):
Categories completed: [list] | Not completed: [list]
Counts per category: Septic __ | Drainage __ | Excavating __ | Sewage __ | Portable toilet __ | Waste mgmt __
Renames done: [list]
Custom services added: [list]
Descriptions updated: [list]
KEEP items not found: [list]
Uncertain matches kept: [list]
Warnings / "under review" notices / anything skipped: [...]
```
