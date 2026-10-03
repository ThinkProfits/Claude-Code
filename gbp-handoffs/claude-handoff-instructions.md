# Instructions for Claude: GBP handoff to Codex and Make

After completing `gbp-topic-finder` and `gbp-post-writer`, create one Markdown file per finished GBP post. Do not edit the Google Sheet and do not call the publishing webhook.

## Required filename

Use:

`gbp-handoff__<location>__<YYYY-MM-DD>__<short-slug>.md`

Example:

`gbp-handoff__vision_kelowna__2026-09-10__fall-furnace-check.md`

## Required file format

The first line and JSON structure must be exact. Output valid JSON with no comments, trailing commas, placeholders, or extra fenced blocks.

    GBP-MAKE-HANDOFF/1

    ```json
    {
      "schemaVersion": 1,
      "intent": "QUEUE_AND_PUBLISH_GBP",
      "postId": "vision_kelowna__2026-09-10__fall-furnace-check",
      "location": "vision_kelowna",
      "title": "Prepare Your Furnace Before Kelowna's Cold Weather",
      "summary": "Complete GBP post body here. Keep it at or below 1,500 characters and escape line breaks inside this JSON string.",
      "actionType": "LEARN_MORE",
      "url": "https://example.com/verified-destination/",
      "imageUrl": "https://example.com/wp-content/uploads/verified-photo.jpg",
      "languageCode": "en",
      "researchNotes": "Optional short source and keyword note. Codex will not publish this field."
    }
    ```

The indentation above only displays the template. In the actual file, start the marker in column one and use one JSON fence.

## Field rules

- `postId` must be new and use `<location>__YYYY-MM-DD__<short-slug>`. Never reuse an earlier ID.
- `location` must be exactly one of `thinkprofits_vancouver`, `john_sadler_surrey`, `wiseworth_surrey`, `vision_kelowna`, `mvp_langley`, `jamie_davis_hope`, `munro_crawford`, `clearset_port_coquitlam`, or `spiedr`.
- `actionType` must be exactly `BOOK`, `ORDER`, `SHOP`, `LEARN_MORE`, `SIGN_UP`, or `CALL`.
- `url` must be an existing public HTTPS page checked during the same task.
- `imageUrl` must directly return a public JPG or PNG image. Do not use WebP, a local file, a search result, an HTML page, or an expiring URL.
- Use a real client-owned photo and follow the existing GBP writer requirements.
- Do not claim that the user approved the post. The user's upload message supplies approval.

## Delivery to the user

Give the `.md` file to the user and say exactly:

> Review the attached GBP handoff. If approved, upload it to Codex with the message: **GBP APPROVED — PROCESS**

Do not include alternative formats or ask Codex to interpret prose. Codex identifies the action from the filename, protocol marker, JSON `intent`, and the user's approval phrase.
