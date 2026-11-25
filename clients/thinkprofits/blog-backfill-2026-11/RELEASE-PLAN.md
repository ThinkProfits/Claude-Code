# Blog backfill release plan

Ten posts fill the gap from 2026-09-22 to 2026-11-24 (one per missing week). They go out a few a week, and each post's date is the day it is built. Lovable builds them; **Francis publishes in Lovable** (Publish button). Nothing is published automatically.

| Batch | Build date | Posts | Status |
|---|---|---|---|
| 1 | 2026-11-25 | 01 answer-first, 02 search terms vs keywords, 03 map pack vs organic | built 2026-11-25, commit 90f0dce, awaiting publish |
| 2 | 2026-12-01 | 04 primary vs secondary conversions, 05 local SEO competitor analysis | pending |
| 3 | 2026-12-08 | 06 Google Ads vs GA4 vs CRM, 07 internal linking checklist | pending |
| 4 | 2026-12-15 | 08 GBP suspension, 09 value-based bidding | pending |
| 5 | 2026-12-22 | 10 office move / change business address | pending |

Order matters: 06 and 09 link to 04, so 04 must go out first. After batch 4, add links from 04 to 06 and 09 (the reviewers flagged this).

## How a batch is sent (reusable)

1. Concatenate the batch's `NN-*.md` files, each preceded by `=============== POST: <filename> ===============`, into `lovable/batch-N-copy.md`.
2. Upload it with the Lovable `get_file_upload_url` tool (PUT with the returned headers) and attach it to `send_message`.
3. Message text: the instructions in `lovable/batch-1-posts-01-03.txt` (everything above the first POST marker), with the build date changed to the batch date and the post count updated. relatedServices rule: only service pages the post links to, plus Contact.
4. Wait for completion, check `get_diff` (files_only) shows a page and route file per post plus blogPosts.ts, siteRoutes.generated.ts, sitemap.xml and llms-full.txt, and spot-check that the copy is unchanged.
5. Update the status column here and tell Francis to review the preview and publish.
