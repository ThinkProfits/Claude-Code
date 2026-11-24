# Estate Options (estateoptions.ca): report baseline, November 2026

> Starting point for Geraldine's first monthly report (sending 2026-12-06). Pulled 2026-11-24 by Claude for Francis.
> **Law practice only.** Realtor numbers live in `../geraldine-hampton-realtor/report-baseline-2026-11.md`. Don't mix them.

## Sources and dates

- **Google Search Console** (property `sc-domain:estateoptions.ca`), 2026-11-16 to 2026-11-24 (launch week onward). GSC lags 2 to 3 days, so the last day with data is 2026-11-23.
- **URL Inspection** (GSC), run 2026-11-24.
- **Semrush Position Tracking:** not set up yet (see `semrush-tracking-setup-2026-11.md`). Rank tracking starts the day the campaign is created, so the 6 Dec report will have at most a week or two of Semrush data.

## Search Console totals since launch

| Metric | 2026-11-16 to 11-23 |
|---|---|
| Clicks | 1 |
| Impressions | 34 |
| Days with any impressions | 6 |

### By page

| Page | Clicks | Impressions | Avg. position |
|---|---|---|---|
| Home (reported by GSC as `http://estateoptions.ca/`) | 1 | 29 | 6.3 |
| /wills-estate-planning | 0 | 6 | 64.7 |
| /estates-probate | 0 | 0 | n/a |
| /executor-services | 0 | 0 | n/a |

### All queries that showed up (12)

| Query | Page | Impr. | Avg. pos. |
|---|---|---|---|
| estate administration | Home | 6 | 9.2 |
| estate options | Home | 4 | 4.2 |
| estate planning calgary | /wills-estate-planning | 2 | 89 |
| calgary estate planning | /wills-estate-planning | 1 | 69 |
| will lawyer calgary | /wills-estate-planning | 1 | 69 |
| estate mediation | Home | 1 | 6 |
| geraldine hampton | Home | 1 | 2 |
| notary calgary | Home | 1 | 41 |
| calgary trust and estate retirement | Home | 1 | 1 |
| estate administration paralegal calgary | Home | 1 | 1 |
| estate planning trusts canada | Home | 1 | 1 |
| estate sales calgary | Home | 1 | 1 |

Single impressions at position 1 are long-tail one-offs, not rankings to report as wins.

## Where she stands for "probate lawyer"

- **No probate searches yet.** GSC has zero impressions for any query containing "probate" from 2026-08-01 to 2026-11-24.
- **The reason is simple: Google hasn't indexed the probate page yet.** URL Inspection on 2026-11-24: `/estates-probate` is "Discovered, currently not indexed" (never crawled). A page has to be in Google's index before it can rank for anything.
- Tracked probate terms (Calgary volumes from the tracking list): probate lawyer calgary (110/mo), probate lawyers calgary (90), probate lawyer (90), probate lawyer near me (10), probate alberta (140), probate fees alberta (90), what is probate (170), how long does probate take in alberta (50), grant of probate alberta (40). Baseline position for all of them: **not ranking** (top 100).
- "probate lawyer calgary" carries a top-of-page bid around $28 in Keyword Planner, which tells you how hard established firms compete for it. Moving up for it is a months-long job: indexing first, then reviews and local signals on the Google Business Profile, links from legal directories, and supporting blog content.

## Indexing check (URL Inspection, 2026-11-24)

| URL | Status | Note |
|---|---|---|
| / | **Excluded by 'noindex' tag** (crawled 2026-11-19) | Live page now says `index, follow` (checked 2026-11-24), so the noindex was there at launch and has since been removed. **Action: Request Indexing in GSC** |
| /estates-probate | Discovered, not indexed | Never crawled. **Request Indexing** |
| /executor-services | Indexed (crawled 2026-11-22) | Fine |
| /wills-estate-planning | Getting impressions, so indexed | Fine |

Other technical notes (internal, not for the client):
- `http://estateoptions.ca/` redirects to `https://www.estateoptions.ca/` with a **302** (temporary). A 301 is the right one. GSC is still reporting the home page under the http URL.
- Requesting indexing is a click in the GSC web UI (URL Inspection > Request Indexing); the API can't do it. Do it for `/` and `/estates-probate` this week, and resubmit the sitemap.

## Draft wording for the 6 Dec report (client-facing)

> **Where we're starting from**
> Estate Options went live the week of 16 November, so this first report is a baseline, not a scorecard. In its first week Google showed the site 34 times in search and sent one visitor. That's normal for a brand-new domain: Google is still discovering the pages.
>
> **About "probate lawyer"**
> You asked why the site doesn't come up for "probate lawyer" yet. The short answer: Google hasn't added the probate page to its index yet, and a page can't rank until it's in the index. We've asked Google to crawl it, and we're now tracking "probate lawyer", "probate lawyer calgary" and seven related searches every day so you can see the movement month by month.
>
> Probate is one of the most competitive legal searches in Calgary, with established firms paying close to $30 a click to appear at the top. Organic rankings for terms like this typically build over several months, not weeks. We can't promise a position, but we can show you steady, measurable progress, and every month's report will show exactly where these terms stand.

(Flag for Andrew: the "$30 a click" figure is from Google Keyword Planner, Calgary, pulled 2026-11-24. Keep or cut.)
