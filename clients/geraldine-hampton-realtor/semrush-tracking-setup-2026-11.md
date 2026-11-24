# Semrush Position Tracking setup: Geraldine Hampton, REALTOR® (geraldinehampton.com)

> Written 2026-11-24. **Not set up yet.** Claude couldn't create it: the Semrush API has 0 units (campaign creation needs units), and clicks hang on Semrush pages in Chrome. Follow these steps in the Semrush web app, signed in as the ThinkProfits SEO account.
> **Realtor keywords only.** Estate Options has its own file in `../estate-options/`.

## 0. Check first

- The API (`list_projects`, domain geraldinehampton.com, all scopes) returned no project, and page 1 of the Projects list has none either. Pages 2 and 3 weren't checked. Search Projects for "hampton" before creating, so we don't make a duplicate.

## 1. Create the project

1. Projects > **Create project**.
2. Domain: `geraldinehampton.com`. Project name: `Geraldine Hampton Realtor`.
3. **Create project**.

## 2. Desktop campaign

1. On the project card, Position Tracking > **Set up**.
2. Targeting:
   - Search engine: Google
   - Device: **Desktop**
   - Location: **Calgary, Alberta, Canada**
   - Language: English
   - Business name: `Geraldine Hampton` (so local pack results count)
   - Domain scope: root domain (`geraldinehampton.com`)
3. **Continue to Keywords**. Paste each batch below, type its tag in the **Tags** field, then click **Add keywords to campaign**. Repeat for every batch.
4. Competitors (in the wizard, or Settings > Competitors later): `kirbycox.com`, `sellingcalgaryrealestate.ca`, `jdrealestatecalgary.ca`, `mohammademon.ca`, `calgaryseniorsrealestateservices.com`
5. **Start tracking**.

## 3. Mobile campaign

In the Position Tracking campaign menu, duplicate the desktop campaign (or add a new campaign in the same project) and change **Device** to **Mobile**. Keep the same location, keywords, tags and competitors. If the keyword limit is tight, run desktop only and tell Francis.

## Keyword batches (51 total)

Tag: **Home** (21)
```
calgary realtor
realtors in calgary alberta
realtor calgary
calgary real estate agents
real estate agent calgary
calgary real estate
realtor near me
realtors near me
real estate agent near me
real estate agents near me
best realtor calgary
top realtor calgary
varsity homes for sale
edgemont homes for sale
scenic acres homes for sale
lake bonavista homes for sale
dalhousie homes for sale
brentwood homes for sale
varsity realtor
edgemont realtor
buy a house calgary
```

Tag: **Selling** (11)
```
sell house calgary
calgary home evaluation
home evaluation
how much is my house worth
what is my house worth
sell my house
house value calgary
home staging calgary
real estate agent for selling a house
listing agent
how to sell a house
```

Tag: **Estate & Transition** (10)
```
probate realtor
probate real estate
selling an estate home
seniors downsizing
seniors downsizing calgary
downsizing home
seniors real estate
realtors for seniors
selling parents house with power of attorney
can you sell a house before probate
```

Tag: **About** (2)
```
realtor and lawyer calgary
lawyer realtor
```

Tag: **Brand** (2)
```
geraldine hampton
geraldine hampton realtor
```

Tag: **Blog** (5)
```
calgary housing market
calgary house prices
calgary real estate market
average house price in calgary
best time to sell a house in calgary
```

Left out until answered: "senior real estate specialist" (only if she holds the SRES® designation). Later: add the section 7 keywords from `keyword-tracking-list-2026-11.md` as each post goes live.

## After setup

- Note the project ID on `CARD.md` and in `memory/` so the next session can pull ranks through the API once units are topped up.
- First data shows the next day. The 6 Dec report can show the starting positions from that first day.
