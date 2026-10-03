# Codex Task: Switch GBP Posting Scenario from Webhook to Sheets-Triggered

## Context

The current Make.com scenario publishes Google Business Profile posts when it receives a webhook call from Claude. We're moving to a pull-based model instead: Claude (or a human reviewer) marks a post as approved by adding a row to a spreadsheet tab, and Make polls that tab on its own schedule and publishes from there. This removes the dependency on any external system successfully reaching Make's webhook — a real failure we hit where Claude's cloud automation couldn't reach the webhook at all due to a network policy block.

## Spreadsheet

`https://docs.google.com/spreadsheets/d/1MFFDsfa4aVvVqqR1wpfNrRsQ-EzhSwZ10QjaD87-Nto/edit`

## Step 1 — Add a new tab

Add a tab called **`Approved Queue`** (separate from whatever existing tabs log published posts — don't touch those). Columns, in order:

| Column | Notes |
|---|---|
| `postId` | Stable unique ID per post, e.g. `vision_kelowna__2026-09-07`. Never reused for a different post. |
| `location` | The client's `location_key` (e.g. `vision_kelowna`) — same values already used to route to each client's GBP module. |
| `title` | Post title |
| `summary` | Post body |
| `actionType` | One of: LEARN_MORE, BOOK, CALL, ORDER, SIGN_UP, GET_OFFER |
| `url` | CTA destination URL |
| `imageUrl` | Direct image URL (blank allowed only for `vision_kelowna`, which has a fallback photo configured — every other client requires a real value) |
| `languageCode` | Default `en` |
| `Status` | `Ready` when a row is added; Make updates this after processing |
| `Notes` | Leave blank; Make writes error details here if publishing fails |

## Step 2 — Build a "Watch Rows" (Google Sheets) trigger

Trigger on the `Approved Queue` tab, filtered to `Status = Ready`. Polling interval: every 15 minutes is fine — this isn't time-sensitive to the minute.

## Step 3 — Route each triggered row into the existing per-client Publish GBP Post logic

Reuse the existing 9 client branches already built, keyed by the `location` field — just feed them from this new trigger instead of the webhook's parsed payload.

## Step 4 — After each publish attempt

- **Success**: update that row's `Status` to `Published`, and write the returned post URL somewhere retrievable (either back into this row in a new column, or into the existing published-post log tab, whichever pattern already exists). This row should not be picked up again on the next poll.
- **Failure**: update `Status` to `Failed` and put the error message in `Notes`. Do not retry automatically — leave it for manual review.

## Step 5 — Leave the existing webhook trigger in place, untouched

Don't remove it. It's used for manual one-off testing and shouldn't be deleted as part of this change.

## Important: do not publish anything for real while building/testing this

Validate with the scenario in a paused/draft state, or test against a low-risk client, until this is confirmed working end-to-end. Confirm once it's built and validated so a real test can be planned before turning it fully live.
