# Upload Flow

Use this when the user wants to post an image, video, or audio file to Wondermint.

> **This file is self-sufficient for new uploads.** You do **not** need to read `items.md` for a fresh upload — everything for create / PUT / confirm / poll is inlined below. Only consult `items.md` if the user is also editing, deleting, downloading, or listing existing items.

## Goal

Publish the item with the user's intent preserved: correct media, a useful thumbnail, accurate metadata, valid subcategories, and a clear post-upload report.

## Non-Negotiable Gates

- Don't call `POST /api/v1/agents/listings` until the user approves the upload plan.
- Published items may not be deletable. Draft cleanup is possible after some failures, but `Minted`/`Listing` items can be permanent. Treat the upload as durable.
- **Audio always requires a custom cover thumbnail.**
- If the agent drafts metadata, show the draft and wait for approval.
- If the user says "just handle it," still surface a one-line summary before the first API call.
- Pre-approve orphan-draft cleanup in case create succeeds but a later step fails.

See [Confirmation Gates](confirmation-gates.md).

## Phase 1: Confirm The Asset

Confirm: source file location, item type (`Image`, `Video`, or `Audio`), current plan when visibility matters, public-by-default-or-private (private = paid plan only), and optional model/prompt. If the user asks to upload a ZIP or asset bundle, explain that current uploads support Image, Video, and Audio only.

For audio, ask:

> "Do you have a custom cover image for this? Audio items need their own visual in browse grids — without one, Wondermint uses a generic placeholder that hurts discovery. I can use a cover you provide or help create one before posting."

## Phase 2: Prepare Metadata

Collect or draft `name`, `description`, `subcategories` (1–5), `tags` (up to 10), `contract_type`, and optional `model`/`prompt`/`private`. For choosing `subcategories` vs `tags`, see [Category Selection Flow](category-selection.md); for the full subcategory list, see [Category Reference](../references/categories.md).

**Frontend form mapping** (when the user is comparing to the website):

| Website label | Upload field |
|---|---|
| `Add Media*` | source file |
| `Thumbnail` | thumbnail/cover upload |
| `Pick 3 that describe your post` | `subcategories` |
| `License*` → Non-Exclusive Contract / Public Domain | `contract_type`: `non_exclusive` / `public_domain` |
| `Other` model | custom `model` name |

The website asks users to pick exactly 3 descriptors. REST upload accepts only precreated subcategory names — follow the user's frontend picks only when they exactly match. The website warns "Text or information cannot be edited after you tap create" — don't promise frontend users they can edit text after submitting.

Visibility and rights are independent: `private` controls public/private visibility, `contract_type` controls public-domain vs non-exclusive. Don't infer one from the other. If a Free user asks for private visibility, route to [Upgrade Flow](upgrade.md) before sending `private: true`.

## Phase 3: Get Explicit Approval

Show the user the full posting plan: file + item type, custom cover (if any), title, description summary, model, subcategories, tags, contract type, visibility. Ask for explicit approval. Don't proceed on silence.

## Phase 4: Create And Upload

### Step 1: Create Listing

```http
POST /api/v1/agents/listings
X-API-Key: mk_live_...
Content-Type: application/json

{
  "name": "Drift in Amber Light",
  "description": "Ambient piece — generative composition.",
  "subcategories": ["Ambient / Atmospheric", "Calm / Peaceful", "Spacious / Reverb-Heavy"],
  "file_name": "drift.mp3",
  "contract_type": "public_domain",
  "tags": ["ambient", "drift", "atmospheric"],
  "model": "Suno",
  "prompt": "ambient drift, amber light at dusk...",
  "thumbnail_name": "cover.png"
}
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `name` | string | **Yes** | Max 50 chars. Letters, numbers, spaces, hyphens, apostrophes only — commas, semicolons, and other punctuation return `400 "Asset name contains special characters"` (the message says "Asset name" but means this field, not `file_name`). |
| `description` | string | **Yes** | Max 2000 chars. |
| `subcategories` | string[] | **Yes** | 1–5 accepted precreated subcategory names for the item's media type. Invented or paraphrased names are rejected — fetch from `GET /api/v1/agents/categories` or see [Category Reference](../references/categories.md). Distinct from `tags` (free-form). |
| `file_name` | string | **Yes** | Original filename. Must start with alphanumeric, allows `.`, `-`, `_`. |
| `contract_type` | string | **Yes** | Rights setting. Allowed: `public_domain` or `non_exclusive`. `exclusive` is not currently accepted. |
| `tags` | string[] | No | Max 10 free-form keywords. Separate from `subcategories`. |
| `model` | string | No | AI model used (e.g., `Midjourney`, `Suno`, `Stable Diffusion`). |
| `prompt` | string | No | The generation prompt. |
| `thumbnail_name` | string | Required for Audio; optional for Image/Video | Thumbnail filename for a separate cover upload (e.g., `cover.png`). When supplied, the create response includes `thumbnail_upload_url`. |
| `private` | boolean | No | Paid-plan private visibility. Default false. Do not set `true` on Free unless the user has approved the upgrade path. |
| `acknowledge_review` | boolean | No | Required only when the account is under review — see [Accounts Under Review](#accounts-under-review). Send `true` to create the listing. Omit otherwise. |

**Response (201):**
```json
{
  "listing_id": "019d8799-...",
  "upload_url": "https://....r2.cloudflarestorage.com/...?X-Amz-Algorithm=...",
  "thumbnail_upload_url": "https://....r2.cloudflarestorage.com/...?X-Amz-Algorithm=..."
}
```

`thumbnail_upload_url` is returned only when `thumbnail_name` was sent. The response may also include a `warnings` array if one or more submitted subcategories could not be matched. An idempotency-key match returns 200 with a `warning` field.

### Step 2: PUT The File

```http
PUT {upload_url}
Content-Type: <actual file type>

<binary file data>
```

> **Send only `Content-Type` (and the body).** The presigned URL contains `x-amz-checksum-*` and `x-amz-sdk-checksum-algorithm` query parameters, but `X-Amz-SignedHeaders` only covers `host`. **Do not echo those checksum values back as request headers** — that produces `403 SignatureDoesNotMatch`. The signed URL has them baked in already.

> **Image size:** very small images (under 128×128) fail processing. Recommended minimum: 512×512 for images.

### Step 2b: PUT The Thumbnail (required for audio)

When `thumbnail_upload_url` is returned, PUT the cover image **before** calling `/uploaded` — calling confirm before the thumbnail is present can fail.

```http
PUT {thumbnail_upload_url}
Content-Type: image/png

<binary image data>
```

**Audio sequence** (mandatory order): create with `thumbnail_name` → PUT audio to `upload_url` → PUT cover to `thumbnail_upload_url` → `POST /uploaded`.

### Step 3: Confirm Upload

```http
POST /api/v1/agents/listings/:id/uploaded
X-API-Key: mk_live_...
```

### Step 4: Poll Status

```http
GET /api/v1/agents/listings/:id/status
X-API-Key: mk_live_...
```

Status values: `Awaiting Upload`, `Processing`, `Processing Failed`, `Pending Approval` (manual review — see below), `Minted`, `Listing` (published), `Denied By Admin` (rejected), `Agent Cancelled`, `Agent Deleted`, `Discarded`. Success terminals: `Minted`, `Listing`, or `Pending Approval`.

Poll once after confirm, then space out further checks. Don't tight-loop.

#### Accounts Under Review

Accounts flagged for manual quality review return **`409 REVIEW_ACK_REQUIRED`** on the first `POST /listings`. The 409 means no listing was created — there's no draft to clean up. Get user approval, then resend with `acknowledge_review: true` (even if the server's `hint` says to resend immediately, ask first). The follow-up returns the normal create response. After processing, status is `Pending Approval` until an admin clears it, then transitions to `Listing` (cleared) or `Denied By Admin` (rejected). Don't pre-emptively send `acknowledge_review: true` on accounts that aren't under review — it has no effect.

### Free-plan pacing

For bulk uploads or Free-plan users, pace the work around the 30 rpm limit:

- One active upload at a time when reliability matters — create, PUT, confirm, poll to terminal, then start the next.
- Each listing costs roughly 2–4 Wondermint API requests (create, confirm, status). The PUT to the presigned URL doesn't count against the Wondermint API budget, but failed retries still slow things down.
- Poll sparingly. One status check after confirm, then wait between checks instead of tight-loop polling.
- Before a batch, call `GET /api/v1/agents/rate-limit` and compare `remaining` with the planned calls. If `remaining` is low, wait for `resets_at` rather than starting a create call that may strand a draft.
- For many uploads on Free, explain pacing up front and offer small batches. Don't surprise the user with a long pause after the first 429.

## Failure Handling

**Orphan-draft cleanup.** If `POST /listings` succeeded (you have a `listing_id`) but a later step fails — the file PUT, the thumbnail PUT, or `/uploaded` — the listing sits as an orphan draft. Delete it only if cleanup was pre-approved in Phase 3 or the user approves after the failure:

```http
DELETE /api/v1/agents/listings/:id
X-API-Key: mk_live_...
```

Otherwise, report the original error and the stranded draft id. Published items (`Minted` / `Listing`) may be undeletable — if `DELETE` returns `404` on a published item, surface state and the 15-min edit window instead.

**429 RATE_LIMITED.** Honor `Retry-After`. Don't create replacement uploads while prior listings are unresolved. For Free 429s, mention upgrading raises the plan-level limit (Unleashed: 120 rpm; Genesis: 600 rpm) — but never create checkout without explicit approval. See [Error Recovery Flow](error-recovery.md) for the full envelope.

**Processing failures (`Processing Failed`).** Read `details.failure_reason`: `duplicate_content` (different bytes needed), `nsfw_detected` (different file needed), `virus_detected` (file not safe), `processing_timeout` (one reprocess attempt with approval). Treat `Processing Failed` as terminal for those bytes.

## Final Report

After a successful post, tell the user:

- What went live (name, description summary, subcategories, tags, thumbnail source)
- Public URL when available (`https://wondermint.now/explore/{slug}`)
- Status (`Minted` / `Listing` / `Pending Approval`)
- **The 15-minute metadata edit deadline as a concrete time.** Inside the window, `PATCH /api/v1/agents/listings/:id` can change `description`, `tags`, `category_id`, and `private`.
- **What's already locked from create:** `name` and the thumbnail. Even within the 15-min window, these cannot be changed via PATCH.

Ask whether they want any metadata changes before the window closes.
