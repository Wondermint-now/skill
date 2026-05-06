# Upload Flow

Use this when the user wants to post an image, video, audio file, or ZIP to
Wondermint.

## Goal

Publish the item with the user's intent preserved: correct media, a useful
thumbnail, accurate metadata, valid taxonomy, and a clear report after posting.

## Non-Negotiable Gates

- Do not call `POST /api/v1/agents/listings` until the user has approved the
  upload plan.
- Treat published items as permanent. Draft cleanup is possible after some
  failures, but published `Minted` or `Listing` items may not be deletable.
- For audio and ZIP, ask about a custom cover before creating the listing.
- If the agent drafts metadata, show the user the draft and wait for approval.
- If the user says to handle the details, still show a one-line posting summary
  and ask for confirmation before the first API call.
- Include orphan-draft cleanup in the approval: if listing creation succeeds
  but file upload or confirmation fails, the agent may delete that unpublished
  draft to keep the user's account clean.

## Phase 1: Confirm The Asset

Confirm:

- source file path or accessible file location
- item type: `Image`, `Video`, `Audio`, or `Zip`
- whether the item should be public or private
- model and prompt if the user wants them recorded

For audio or ZIP, ask:

> Do you have a custom cover image for this? Audio and ZIP items need their own
> visual in Wondermint's browse grids. Without one, Wondermint uses a generic
> placeholder. I can use a cover you provide, help create one, or proceed with
> the placeholder if you explicitly want that.

If a custom cover is used, include `thumbnail_name` in the create payload and
upload the cover to `thumbnail_upload_url` before confirming the upload.

## Phase 2: Prepare Metadata

Collect or draft:

- `name`: max 50 characters; avoid punctuation that can trigger the special
  character validator
- `description`: max 5000 characters
- `subcategories`: 1 to 5 Level 3 taxonomy values from
  `GET /api/v1/agents/categories`
- `tags`: up to 20 free-form keywords
- optional `model`, `prompt`, and `private`

Taxonomy rule:

- `category` is the top-level type.
- `subcategories` must be Level 3 values, such as `Sci-Fi / Futuristic` or
  `Ambient / Atmospheric`.
- Level 2 group headings such as `Mood` or `Genre / World` are not valid
  upload `subcategories`.
- `tags` are free-form keywords, not taxonomy values.

For the detailed endpoint fields and category reference, read
[Items > Upload Flow](../items.md#upload-flow) and
[Category Reference](../references/categories.md).

## Phase 3: Get Explicit Approval

Before creating the listing, show the user:

- file name and item type
- custom cover choice, if any
- title
- description or short summary
- subcategories
- tags
- public/private setting

Ask for explicit approval. Do not proceed on silence.

## Phase 4: Create And Upload

1. Create the listing:

   ```http
   POST /api/v1/agents/listings
   X-API-Key: mk_live_...
   ```

2. Upload the source file to `upload_url` with the file's actual
   `Content-Type`.

3. If `thumbnail_upload_url` is present, upload the cover image there before
   confirming.

4. Confirm the upload:

   ```http
   POST /api/v1/agents/listings/:id/uploaded
   X-API-Key: mk_live_...
   ```

5. Poll status:

   ```http
   GET /api/v1/agents/listings/:id/status
   X-API-Key: mk_live_...
   ```

Success statuses include `Minted`, `Listing`, and `Pending Approval` for
accounts under manual review. If the account requires review acknowledgment,
follow the `REVIEW_ACK_REQUIRED` recovery path in
[Items > Accounts Under Review](../items.md#accounts-under-review).

## Failure Handling

If `POST /listings` succeeded and a later file upload or confirmation step
fails, clean up the orphan draft:

```http
DELETE /api/v1/agents/listings/:id
X-API-Key: mk_live_...
```

If cleanup fails, report both the original failure and the stranded draft id to
the user.

If the item is already published, do not assume deletion will work. Surface the
state and available edit window instead.

## Final Report

After a successful post, tell the user:

- what went live
- public URL when available
- whether a custom or placeholder thumbnail was used
- status: `Minted`, `Listing`, or `Pending Approval`
- the 15-minute metadata edit deadline
- what can still be changed: description, tags, category, privacy
- what is already locked: name and thumbnail

Ask whether they want any metadata changes before the edit window closes.
