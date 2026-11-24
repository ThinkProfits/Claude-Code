# Semrush Position Tracking setup: Estate Options (estateoptions.ca)

> Written 2026-11-24. **Not set up yet.** Claude couldn't create it: the Semrush API has 0 units (campaign creation needs units), and clicks hang on Semrush pages in Chrome. Follow these steps in the Semrush web app, signed in as the ThinkProfits SEO account.
> **Estate Options keywords only.** The realtor site has its own file in `../geraldine-hampton-realtor/`.

## 0. Check first

- The API (`list_projects`, domain estateoptions.ca, all scopes) returned no project, and page 1 of the Projects list has none either. Pages 2 and 3 weren't checked. Search Projects for "estate" before creating, so we don't make a duplicate.

## 1. Create the project

1. Projects > **Create project**.
2. Domain: `estateoptions.ca`. Project name: `Estate Options`.
3. **Create project**.

## 2. Desktop campaign

1. On the project card, Position Tracking > **Set up**.
2. Targeting:
   - Search engine: Google
   - Device: **Desktop**
   - Location: **Calgary, Alberta, Canada**
   - Language: English
   - Business name: `Estate Options` (so local pack results count)
   - Domain scope: root domain (`estateoptions.ca`, so www and non-www both count)
3. **Continue to Keywords**. Paste each batch below, type its tag in the **Tags** field, then click **Add keywords to campaign**. Repeat for every batch.
4. Competitors (in the wizard, or Settings > Competitors later): `willsandestates.ca`, `housecallwills.ca`, `macdonaldlawnorth.ca`, `brunilaw.com`, `kahanelaw.com`
5. **Start tracking**.

## 3. Mobile campaign

In the Position Tracking campaign menu, duplicate the desktop campaign (or add a new campaign in the same project) and change **Device** to **Mobile**. Keep the same location, keywords, tags and competitors. If the keyword limit is tight, run desktop only and tell Francis.

## Keyword batches (57 total)

Tag: **Home** (14)
```
estate lawyer calgary
estate lawyers calgary
calgary estate lawyers
wills and estates calgary
wills and estates lawyer calgary
wills and estates lawyer
estate lawyer
estate lawyer near me
best wills and estate lawyers calgary
lawyers nw calgary
estates lawyer
estate mediation
loss of capacity
asset protection lawyer
```

Tag: **Wills & Estate Planning** (19)
```
wills lawyer calgary
will lawyer calgary
lawyers for wills in calgary
estate planning lawyer
estate planning
estate planning calgary
estate planning lawyer calgary
wills lawyer
wills calgary
wills lawyer near me
power of attorney alberta
enduring power of attorney
enduring power of attorney alberta
personal directive alberta
personal directives
power of attorney calgary
how much does a will cost in alberta
power of attorney
wills
```

Tag: **Estates & Probate** (11)
```
probate lawyer calgary
probate lawyers calgary
probate lawyer
probate lawyer near me
probate alberta
probate fees alberta
what is probate
how long does probate take in alberta
grant of probate alberta
executor of estate
estate administration
```

Tag: **Executor Services** (10)
```
professional executor
professional executor services
executor services
will executor services
estate executor services
lawyer as executor
executor lawyer
i have no one to be executor of my will
executor
executor of will
```

Tag: **Brand** (3)
```
estate options
estate options calgary
geraldine hampton lawyer
```

Later (tag **Blog**): add the section 6 keywords from `keyword-tracking-list-2026-11.md` as each post goes live.

## After setup

- Note the project ID on `CARD.md` and in `memory/` so the next session can pull ranks through the API once units are topped up.
- First data shows the next day. The 6 Dec report can show the starting positions from that first day.
