# Clearset: site changes, 2026-11-11 (service-area wording + H1 local modifiers)

**Why:** Weekly Team Check-in, 2026-11-10. Andrew (00:48:23): the site says "all over British Columbia / all over BC", but Clearset only serves the Lower Mainland. Andrew and Francis (00:49:36–00:51:15) agreed that generic service pages get "Port Coquitlam and the Lower Mainland" in the headings.

**How:** edited through the wp-clearset MCP (back end, raw post_content, not the Divi visual builder, so CallRail could not save swapped numbers). Each edit is in the WordPress revision history.

## 1. "All over BC" service claims replaced (60 edits, 22 pages)

| Old phrasing | New phrasing |
|---|---|
| all over British Columbia (, Canada) / all over BC / all over the province | across the Lower Mainland |
| throughout / around / across British Columbia, around the province, around BC | throughout / around / across the Lower Mainland |
| (fleets serving) all of British Columbia | the Lower Mainland |
| anywhere in BC / British Columbia | anywhere in the Lower Mainland |
| Greater Vancouver and BC neighbourhoods | Greater Vancouver and Lower Mainland neighbourhoods |
| service in British Columbia, including …, In British Columbia we provide …, to our customers in British Columbia, services in British Columbia for 20 years, Management services in British Columbia | the same with "the Lower Mainland" |
| in a remote location in British Columbia (RV page), especially in remote areas in British Columbia (water hauling) | "in a remote location", "especially in remote areas" |

Pages: Home (13), About (15), Services (17), Grease Trap (34), Holding Tank (36), Hydro Flushing (38), Lift Station (40), Pump Chambers (42), Septic Tank Cleaning (44), Storm Drains (46), RV/Trailer (48), Water Hauling (50), Hydrovac (1133), Portable Toilets (1504), Water Totes (1564), Sewer Camera (1638), Leach Field (1650), Port Moody (901), Richmond (909), Burnaby (915), Surrey (921), Port Coquitlam (927).

Also on Water Hauling (50): the in-page schema description said "Get **potable** water anywhere in British Columbia". Changed to "Get non-potable water anywhere in the Lower Mainland" (standing rule: no potable water).

Left on purpose: the address (Port Coquitlam, BC), BC regulations (Ministry of Environment, bylaws), BC weather and septic-frequency FAQs, "Surrey, British Columbia"-style city mentions, legal pages, and "over 20 years of experience in British Columbia".

Re-scan of every page's live content after the edits found no remaining BC-wide service claims, apart from the About meta description below.

## 2. H1s: local modifier added (10 generic service pages)

Appended " in Port Coquitlam & the Lower Mainland" to the H1:

| Page | New H1 |
|---|---|
| /services/ibc-portable-water-tank-rentals/ | Portable Water Storage Tanks & Water Tank Rentals in Port Coquitlam & the Lower Mainland |
| /services/water-hauling/ | Water Hauling & Water Truck Delivery Services in Port Coquitlam & the Lower Mainland |
| /services/trailers-and-rvs-pumping/ | Mobile RV & Trailer Tank Pumping Services in Port Coquitlam & the Lower Mainland |
| /services/storm-drains-catch-basins/ | Catch Basin Pumping, Storm Drain Cleaning & Emergency Flood Control Services in Port Coquitlam & the Lower Mainland |
| /services/septic-tank-cleaning/ | Septic Tank Pumping & Septic Tank Cleaning Services in Port Coquitlam & the Lower Mainland |
| /services/pump-chambers/ | Septic System with Pump Chamber Maintenance & Cleaning in Port Coquitlam & the Lower Mainland |
| /services/lift-stations-cleaning/ | Professional Lift Station Maintenance and Cleaning in Port Coquitlam & the Lower Mainland |
| /services/hydro-flushing/ | Hydro Jetting & Line Flushing Services in Port Coquitlam & the Lower Mainland |
| /services/holding-tank-cleaning/ | Septic Holding Tank Pumping & Cleaning Services in Port Coquitlam & the Lower Mainland |
| /services/grease-trap-cleaning/ | Residential & Commercial Grease Trap Cleaning Services in Port Coquitlam & the Lower Mainland |

Not changed (already have a modifier): Leach Field ("In Coquitlam & Port Coquitlam"), Sewer Camera ("In Coquitlam & Port Coquitlam"), Portable Toilets ("In The Lower Mainland"), Hydrovac ("Lower Mainland BC").

Septic Tank Cleaning: the second H1 span had an inline `font-size: 100px`, which broke words mid-letter on mobile ("Septi / c"). Removed it, so the heading uses the theme's responsive size. Checked at 375 px and 1440 px.

## Still open (not done here)

- **About page meta description** (Yoast) still says "across British Columbia". The MCP's Yoast integration is off, so change it in WP admin > About > Yoast: "Clearset offers professional wastewater management and septic services across the Lower Mainland, with 20 years under their belt. Contact us now!"
- **Wrong-service review heading on most service pages:** "What Our Customers Say About Clearset's **Portable Sanitation** Services" appears on Leach Field, Sewer Camera, Water Totes, Hydrovac, Storm Drains, Septic Tank Cleaning and Hydro Flushing (likely a Divi global module). Same mismatch the client has flagged before.
- **Septic Tank Cleaning** lists every province's pumping frequency, including Alberta, and gives "British Columbia: 3-5 years". This conflicts with the "no Alberta" rule and the HealthLink BC 2–5 year guidance.
- **Superlatives** to review: homepage "British Columbia's leader in hydro jetting and vacuuming"; About H "BC's Trusted Septic and Wastewater Management Experts".
- **Phone numbers:** fixed the same day, except the sitewide head schema. See [phone-number-audit-2026-11-10.md](phone-number-audit-2026-11-10.md). "(778) 208-2510" turned out to be a malformed `tel:+1(778)%208251032` link in the city pages' tablet/phone variants, now fixed.
- Log these changes in #clearset (draft below).

## Slack draft for #clearset

> Site update (Nov 11): following the team check-in, I replaced every "all over BC / British Columbia" service-area claim with "the Lower Mainland" across 22 pages (home, about, services, every service page and the 5 city pages). I also added "in Port Coquitlam & the Lower Mainland" to the H1s of the 10 generic service pages that had no location (septic tank cleaning, holding tank, RV/trailer, water hauling, grease trap, hydro flushing, lift station, pump chambers, storm drains, water totes). Small extra fixes: the water hauling schema no longer says "potable", and the septic page hero no longer breaks words on mobile. Full list: clients/clearset/site-changes-2026-11-11-service-area-and-h1s.md
