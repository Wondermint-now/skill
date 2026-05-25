# Error Recovery Flow

Use this when a Wondermint API request fails, returns an unexpected status, or the user asks how to fix a blocked action. The error envelope, coarse codes, and per-code recovery patterns live in [Reference > Error Handling](../reference.md#error-handling); this file is the diagnostic procedure.

## Goal

Diagnose from the response, recover with the least risky next step, and avoid repeating requests the server has already said cannot succeed.

## Phase 1: Capture The Error Shape

Read the response body and status before retrying. Beyond the base `{status_code, message, error}` envelope, look for optional recovery fields: `code`, `hint`, `next`, `details`, `fields`. When `next.options[]` is present, prefer it over hardcoded recovery steps. Full envelope details: [Reference > Error Handling](../reference.md#error-handling).

## Phase 2: Classify And Recover

For the coarse-code lookup table (`UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND`, etc.), see [Reference > Coarse Error Codes](../reference.md#coarse-error-codes). For per-code recovery, see [Reference > Agent Error Codes](../reference.md#agent-error-codes) and the `## Errors & Recovery` section in the relevant sub-skill ([items.md](../items.md#errors--recovery), [folders.md](../folders.md#errors--recovery), [social.md](../social.md#errors--recovery), [account.md](../account.md#errors--recovery)).

Recovery decisions that need explicit user approval:

- **`FOLDER_CAP_REACHED`** — choosing between delete (which portfolio/playlist/feed?), reuse, or upgrade. Ask before any of these. Remember `COLLECTION` and `PLAYLIST` share one cap.
- **`REVIEW_ACK_REQUIRED`** — explain that re-sending creates a held draft; only resend with `acknowledge_review: true` after approval.
- **`PUBLISHED_IMMUTABLE`** — don't retry deletion. Explain that published items aren't removable through the agent endpoint.
- **`LISTING_EDIT_WINDOW_EXPIRED`** — retry only with `details.editable_fields` (usually just `private` after the window). Tell the user the locked fields can't be changed.

## Phase 3: Retry Safely

Auto-retry only when read-only or clearly transient:

- rate limits after backoff
- internal errors after backoff
- not-found caused by a stale username or id after re-resolving

Ask before retrying mutating actions: uploads, comments, follows, folder changes, billing actions, password changes, API key regeneration. Use idempotency keys for listing creation when available.

For upload or bulk-work rate limits, don't immediately start replacement uploads or duplicate queue/add actions. Wait for the reset window, re-check unresolved item statuses, then resume with the minimum request needed.

## Phase 4: 429 / RATE_LIMITED — Always Surface The Recovery

When the platform returns 429, deliver the recovery even if the user didn't ask about rate limits. Wait for `Retry-After` or the reset window, then resume with the minimum request needed. For Free-plan 429s or repeated rate limits, mention upgrading raises the plan-level limit (Unleashed: 120 rpm; Genesis: 600 rpm). If the response points to an endpoint-specific throttle, explain that upgrading may not bypass that endpoint cap. Don't create a checkout or billing link without explicit approval.

## Phase 5: Escalate Clearly

If recovery is blocked, tell the user: the endpoint that failed, status and `error`, fine-grained `code` if present, server `message` or `hint`, what was tried, and the safest next option. Don't expose the API key or any credential in the report.

## Final Report

The diagnosis, the recovery taken or recommended, whether the original goal succeeded, and any user decision still needed before a mutating retry.
