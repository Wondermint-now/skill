# Upload Flow

Use this when the user wants to post an image, video, or audio file to Wondermint. Endpoint shapes (create, PUT, confirm, status, payload fields) live in [Items > Upload Flow](../items.md#upload-flow); this file is the user-facing conversation guide.

## Goal

Publish the item with the user's intent preserved: correct media, a useful thumbnail, accurate metadata, valid subcategories, and a clear post-upload report.

## Non-Negotiable Gates

- Don't call `POST /api/v1/agents/listings` until the user approves the upload plan.
- Published items may not be deletable. Draft cleanup is possible after some failures, but `Minted`/`Listing` items can be permanent. Treat the upload as durable.
- **Audio always requires a custom cover thumbnail** (see [Items > Step 2b](../items.md#step-2b-thumbnail-upload)).
- If the agent drafts metadata, show the draft and wait for approval.
- If the user says "just handle it," still surface a one-line summary before the first API call.
- Pre-approve orphan-draft cleanup in case create succeeds but a later step fails.

See [Confirmation Gates](confirmation-gates.md).

## Phase 1: Confirm The Asset

Confirm: source file location, item type (`Image`, `Video`, or `Audio`), current plan when visibility matters, public-by-default-or-private (private = paid plan only), and optional model/prompt. If the user asks to upload a ZIP or asset bundle, explain that current uploads support Image, Video, and Audio only.

For audio, ask:

> "Do you have a custom cover image for this? Audio items need their own visual in browse grids — without one, Wondermint uses a generic placeholder that hurts discovery. I can use a cover you provide or help create one before posting."

## Phase 2: Prepare Metadata

Collect or draft `name`, `description`, `subcategories` (1–5), `tags` (up to 10), `contract_type`, and optional `model`/`prompt`/`private`. For payload constraints and validation rules, see [Items > Step 1: Create Item](../items.md#step-1-create-item). For choosing `subcategories` vs `tags`, see [Category Selection Flow](category-selection.md).

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

Endpoint sequence is in [Items > Upload Flow](../items.md#upload-flow). One Free-plan operational note:

**For bulk uploads or Free-plan users, pace the work around the 30 rpm limit:**

- One active upload at a time when reliability matters — create, PUT, confirm, poll to terminal, then start the next.
- Each listing costs roughly 2–4 Wondermint API requests (create, confirm, status). The direct file PUT to the presigned URL doesn't count against the Wondermint API budget, but failed retries still slow things down.
- Poll sparingly. One status check after confirm, then wait between checks instead of tight-loop polling.
- Before a batch, call `GET /api/v1/agents/rate-limit` and compare `remaining` with the planned calls. If `remaining` is low, wait for `resets_at` rather than starting a create call that may strand a draft.
- For many uploads on Free, explain pacing up front and offer small batches. Don't surprise the user with a long pause after the first 429.

## Failure Handling

For `429 RATE_LIMITED` and orphan-draft cleanup, see [Items > Errors & Recovery](../items.md#errors--recovery) and [Error Recovery Flow](error-recovery.md). Briefly: honor `Retry-After`, don't create replacement uploads while prior listings are unresolved, and only delete the orphan draft if cleanup was pre-approved in Phase 3 or the user approves after the failure. If the item is already published, surface state and the 15-min edit window instead of trying to delete.

## Final Report

After a successful post: what went live, public URL when available, custom thumbnail source (user-provided or flow-created), status (`Minted`/`Listing`/`Pending Approval`), the 15-minute edit deadline, what can still be PATCHed (description, tags, category, privacy), and what's already locked (name and thumbnail). Ask whether they want any metadata changes before the window closes.
