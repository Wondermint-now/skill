# Upload Flow

Use this when the user wants to post an image, video, or audio file to
Wondermint.

## Goal

Publish the item with the user's intent preserved: correct media, a useful
thumbnail, accurate metadata, valid subcategories, and a clear report after posting.

## Non-Negotiable Gates

- Do not call `POST /api/v1/agents/listings` until the user has approved the
  upload plan.
- Treat published items as permanent. Draft cleanup is possible after some
  failures, but published `Minted` or `Listing` items may not be deletable.
- For audio, require a cover thumbnail before creating the listing.
- If the agent drafts metadata, show the user the draft and wait for approval.
- If the user says to handle the details, still show a one-line posting summary
  and ask for confirmation before the first API call.
- Include orphan-draft cleanup in the approval: if listing creation succeeds
  but file upload or confirmation fails, the agent may delete that unpublished
  draft to keep the user's account clean.

For confirmation details, use [Confirmation Gates](confirmation-gates.md).

## Phase 1: Confirm The Asset

Confirm:

- source file path or accessible file location
- item type: `Image`, `Video`, or `Audio`
- current plan when visibility matters
- visibility: public by default on Free; ask about private visibility only when
  the account is Unleashed or Genesis, or when the user specifically asks for a
  private asset
- model and prompt if the user wants them recorded

If the user asks to upload a ZIP or asset bundle, explain that current
Wondermint uploads support Image, Video, and Audio only.

For audio, ask:

> Do you have a custom cover image for this? Audio items need their own
> visual in Wondermint's browse grids. Without one, Wondermint uses a generic
> placeholder that hurts discovery. I can use a cover you provide or help
> create one before posting.

Audio uploads require a thumbnail/cover in the agent flow. Include
`thumbnail_name` in the create payload. The create response returns
`thumbnail_upload_url` only when the request includes `thumbnail_name`; if
`thumbnail_name` is omitted, the response includes only the main `upload_url`.
Upload the cover to `thumbnail_upload_url` before confirming the upload.

## Phase 2: Prepare Metadata

Collect or draft:

- `name`: max 50 characters; avoid punctuation that can trigger the special
  character validator
- `description`: max 2000 characters
- `subcategories`: 1 to 5 accepted subcategory names from the precreated
  [Category Reference](../references/categories.md)
- `tags`: up to 10 free-form keywords
- `contract_type`: `public_domain` or `non_exclusive`
- optional `model`, `prompt`, and `private`

If the user is comparing this to the website, map the frontend form labels this
way:

- `Add Media*`: source file
- `Thumbnail`: thumbnail or cover upload, especially important for audio and
  other uploads that need a better preview
- `Pick 3 that describe your post`: upload `subcategories`
- `License*`: `contract_type`
- Non-Exclusive Contract: `non_exclusive`
- Public Domain: `public_domain`
- `Other` model: capture the custom model name

The website asks users to pick exactly 3 descriptors. The REST upload accepts
only precreated `subcategories`; follow the user's frontend picks only when they
exactly match accepted subcategory names.

The website currently warns: "Text or information cannot be edited after you tap
create." When guiding a frontend user, do not promise they can edit text after
submitting the form.

Visibility and rights are separate decisions. `private` controls whether the
item is visible publicly; `contract_type` controls whether the upload is public
domain or non-exclusive. Do not infer contract type from visibility, or
visibility from contract type. Private assets are a paid-plan feature; if a
Free user asks for private visibility, route to [Upgrade Flow](upgrade.md)
before including `private: true`.

Subcategory rule:

- `subcategories` are the exact descriptor strings sent in the upload payload,
  such as `Everyday / Contemporary`, `Cinematic`, or `Warm / Cozy`.
- `subcategories` are not free-form; select them from the category reference
  list only. Put custom descriptors in `tags`.
- Identify the media type (`Image`, `Video`, or `Audio`) before choosing
  subcategories so you use the right precreated list.
- Use only values from the media type's list in the category reference. Invented,
  paraphrased, or custom category names are rejected.
- `tags` are free-form keywords, not subcategories.

For the detailed endpoint fields and category reference, read
[Category And Tag Selection Flow](category-selection.md),
[Items > Upload Flow](../items.md#upload-flow), and
[Category Reference](../references/categories.md).

## Phase 3: Get Explicit Approval

Before creating the listing, show the user:

- file name and item type
- custom cover choice, if any
- title
- description or short summary
- model or custom model, if provided
- subcategories
- tags
- contract type: public domain or non-exclusive
- visibility: public, or private only when the plan supports it or the user has
  approved the upgrade path

Ask for explicit approval. Do not proceed on silence.

## Phase 4: Create And Upload

Before starting, check whether the workflow needs rate-limit budgeting. For
bulk uploads or Free-plan users, read [Reference > Rate Limits](../reference.md#rate-limits)
and avoid creating replacement listings while earlier created listings are
still unresolved.

For Free users, assume a practical budget of **30 API requests per minute** and
keep the upload experience calm:

- Prefer **one active upload at a time**: create listing, upload bytes to the
  presigned URL, confirm, then poll that listing to a terminal state before
  creating replacements or starting another uncertain upload.
- Treat each listing as roughly **2-4 Wondermint API requests** before polling:
  create, confirm, and one or more status checks. The direct file PUT to the
  presigned storage URL is separate from the Wondermint API budget, but failed
  retries still slow the workflow.
- Poll status sparingly. Start with one status check after confirm, then wait
  between checks instead of tight-loop polling. For batches, check a small group
  once per reset window rather than checking every item repeatedly.
- Before a batch, call `GET /api/v1/agents/rate-limit` and compare `remaining`
  with the planned create/confirm/status calls. If `remaining` is low, wait for
  `resets_at` rather than starting a create call that may strand a draft.
- If the user wants many uploads on Free, explain the pacing up front and offer
  to run them in small batches. Do not surprise them with a long pause after the
  first 429.

1. Create the listing:

   ```http
   POST /api/v1/agents/listings
   X-API-Key: mk_live_...
   ```

2. Upload the source file to `upload_url` with the file's actual
   `Content-Type`.

3. If the create request included `thumbnail_name`, the response includes
   `thumbnail_upload_url`; upload the cover image there before confirming. If
   `thumbnail_name` was omitted, no separate thumbnail URL is returned.

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
explain that the listing can be created as a held draft, then get user approval
before resending with `acknowledge_review: true`. See
[Items > Accounts Under Review](../items.md#accounts-under-review).

## Failure Handling

On `429 RATE_LIMITED`, honor `Retry-After` when present, re-check unresolved
listings after the reset window, and do not create replacement uploads until
the prior listings reach terminal statuses or the user approves a new attempt.
Tell Free users that they can continue after the reset window, and mention that
upgrading raises the plan-level request limit (Unleashed: 120 rpm; Genesis: 600
rpm) if they want smoother high-volume uploads.

If `POST /listings` succeeded and a later file upload or confirmation step
fails, delete the orphan draft only if cleanup was pre-approved in Phase 3 or
the user explicitly approves cleanup after the failure:

```http
DELETE /api/v1/agents/listings/:id
X-API-Key: mk_live_...
```

If cleanup is not approved or cleanup fails, report both the original failure
and the stranded draft id to the user.

If the item is already published, do not assume deletion will work. Surface the
state and available edit window instead.

## Final Report

After a successful post, tell the user:

- what went live
- public URL when available
- whether a cover thumbnail was used, and whether it was provided by the user or created during the flow
- status: `Minted`, `Listing`, or `Pending Approval`
- the 15-minute metadata edit deadline
- what can still be changed: description, tags, category, privacy
- what is already locked: name and thumbnail

Ask whether they want any metadata changes before the edit window closes.
