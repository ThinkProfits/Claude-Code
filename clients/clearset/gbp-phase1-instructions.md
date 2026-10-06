# Task: Clearset GBP cleanup, Phase 1

You are editing the Google Business Profile for **Clearset VAC Truck Services** (Port Coquitlam, BC). The profile is managed by the Google account **seo@thinkprofits.com**, which is already signed in to this browser. The account owner approved every change below on 2026-10-06. Do only these changes, nothing else.

Background: the full audit is in `clients/clearset/gbp-audit-2026-10-06.md` in the ThinkProfits/Claude-Code repo. Phase 2 (the rest of the service cleanup) happens later, in a separate session. Do **not** start it.

## How to open the editor

1. Go to `https://www.google.com/search?q=Clearset+VAC+Truck+Services&hl=en`
2. The "Your business on Google" panel appears at the top. If it doesn't, check the account switcher (top right) and pick seo@thinkprofits.com.
3. Use **Edit profile** for categories and the description, and **Edit services** for services. The editors open as pop-up dialogs.

## Rules

- Make only the changes listed. Don't touch the primary category, the name, address, phone, hours, photos or any other service.
- Don't add categories.
- If a listed item isn't there, or its name differs, skip it and note it in the report. Don't guess.
- If Google shows a verification prompt, a suspension warning, or anything asking for ID or a phone code, **stop and report**. Don't proceed.
- Save after each numbered step, and confirm that the save took effect (the dialog closes or shows the new value) before moving on.

## Step 1: Remove 4 additional categories

Edit profile → About → **Business category** → pencil/edit.

Click the **X** next to each of these additional categories:
- Water pump supplier
- Water utility company
- Water jet cutting service
- Water tank cleaning service

**Keep** these (don't touch them): Septic system service (primary), Drainage service, Excavating contractor, Sewage disposal service, Portable toilet supplier, Waste management service.

Click **Save**. Expected result: 6 categories remain.

Note: removing these categories also removes the services listed under them. That's intended.

## Step 2: Add one custom service

Edit services → under **Sewage disposal service** → **Add more services** → **Add custom service**:

- **Name:** `Car wash sump pump-out`
- **Price:** fixed, `$189` (CAD)
- **Description:**
  `Pump-out and cleaning of car wash sumps and settling pits for commercial wash bays in Port Coquitlam and across Metro Vancouver and the Fraser Valley. Scheduled or on-call service.`

Save.

## Step 3: Remove services that contradict the website

Clearset does **not** do septic inspections (licensed plumbers only), so these must go.

Edit services. Click each service below to open it, then use **Remove service** (or the delete/trash option) and confirm:

Under **Septic system service**:
- Septic system inspection
- Real estate septic inspection
- Septic tank certification

Under **Sewage disposal service**:
- Septic tank inspection

Don't remove "Septic system camera inspection" or "Sewer camera inspection". Those are real services.

Save.

## Step 4: Fix the monthly toilet rental service

Edit services → under **Portable toilet supplier** → open **"Toilet rental per month for once a week cleaning"**:

- **Rename to:** `Monthly portable toilet rental (weekly servicing included)`
- **Price:** change from $140 to `$165` (fixed)
- **Description:**
  `Fully serviced portable toilet rental from $165/month, with weekly pumping, cleaning and restocking included. Delivery and pickup across Port Coquitlam, Metro Vancouver and the Fraser Valley. Ideal for construction sites and long-term projects.`

Save.

## Step 5: Replace the business description

Edit profile → About → **Description** → edit. Delete all existing text and paste exactly:

```
Clearset VAC Truck Services provides septic, water, vacuum truck and portable sanitation services across Metro Vancouver and the Fraser Valley, with 20+ years of experience and 24/7 emergency dispatch. Our crews handle septic tank pumping and cleaning, hydrovac excavation and daylighting, hydro-flushing and line jetting, grease trap cleaning, catch basin and storm drain cleaning, lift station and pump chamber cleaning, holding tank and RV pumping, sewer camera inspections and leach field rejuvenation. We also deliver non-potable water, rent water totes and IBC tanks, and supply fully serviced portable toilet rentals for construction sites and events. Based in Port Coquitlam and serving Squamish to Chilliwack.
```

Save. It must fit under Google's 750-character limit (it's about 690).

## Step 6: Verify and report

Reopen Edit profile and Edit services and check each change. Then reply with this report filled in:

```
Clearset GBP Phase 1 report (date/time):
1. Categories removed: [list] | Remaining categories: [list]
2. Car wash sump pump-out added: yes/no
3. Services removed: [list] | Not found: [list]
4. Monthly rental renamed + $165: yes/no
5. Description replaced: yes/no
Warnings / "under review" notices / anything skipped: [...]
```

"Under review" or "pending" notices after saving are normal and not an error. Note them in the report.
