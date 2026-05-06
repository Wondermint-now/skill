# Error Recovery Flow

Use this when a Wondermint API request fails, returns an unexpected status, or
the user asks how to fix a blocked action.

## Goal

Diagnose the failure from the response, recover with the least risky next step,
and avoid repeating requests that the server has already said cannot succeed.

## Phase 1: Capture The Error Shape

Read the response body and status before retrying. The base shape is:

```json
{
  "status_code": 409,
  "message": "Email is already registered",
  "error": "CONFLICT"
}
```

Also check for optional recovery fields:

- `code`
- `hint`
- `next`
- `details`
- `fields`

When `next.options[]` is present, prefer it over hardcoded recovery steps.

## Phase 2: Classify The Failure

Use the coarse `error` value first:

| Error | Default response |
|---|---|
| `UNAUTHENTICATED` | Check the API key and configured API host. |
| `FORBIDDEN` | Read `code`, `hint`, and `details`; do not assume retry will help. |
| `NOT_FOUND` | Re-resolve ids, slugs, or usernames before retrying. |
| `CONFLICT` | Determine whether the resource already exists or the action needs confirmation. |
| `VALIDATION_ERROR` | Read `fields[]`, fix only named fields, then ask before retrying mutating requests. |
| `RATE_LIMITED` | Back off; prefer the `Retry-After` header when available. |
| `INTERNAL_ERROR` | Retry with backoff, then report if it persists. |

## Phase 3: Apply Known Recoveries

For `FOLDER_CAP_REACHED`:

- read `details.plan`, `details.folder_type`, `details.limit`, and
  `details.current`
- prefer `next.options[]` when present
- offer to delete/reuse a folder or use the [Upgrade Flow](upgrade.md)
- ask the user to choose and approve the exact recovery before deleting a
  folder, reusing a folder, moving/adding items into a reused folder, or
  starting checkout
- remember `COLLECTION` and `PLAYLIST` share one cap

For `LISTING_EDIT_WINDOW_EXPIRED`:

- retry only with `details.editable_fields`
- usually only `private` remains editable after the window
- tell the user that locked fields cannot be changed

For `PUBLISHED_IMMUTABLE`:

- do not retry deletion
- explain that published items are not removable through the agent endpoint

For `REVIEW_ACK_REQUIRED`:

- explain that the listing can be created as a held draft
- only resend with `acknowledge_review: true` after user approval

For `OPERATOR_MANAGED_BILLING`:

- do not retry billing or subscription endpoints
- check link status if needed and tell the user the operator controls billing

For follow errors:

- `CANNOT_FOLLOW_SELF`: choose another user
- `FOLLOW_TARGET_NOT_FOUND`: search users again before retrying

## Phase 4: Retry Safely

Only retry automatically when the action is read-only or clearly transient:

- rate limits after backoff
- internal errors after backoff
- not-found caused by a stale username or id after re-resolving

Ask before retrying mutating actions such as uploads, comments, follows,
folder changes, billing actions, password changes, or API key regeneration.

Use idempotency keys for listing creation attempts when available.

## Phase 5: Escalate Clearly

If recovery is blocked, tell the user:

- the endpoint that failed
- the status and `error`
- the fine-grained `code`, if present
- the server `message` or `hint`
- what was tried
- the safest next option

Do not expose the API key or any credential value in the report.

## Final Report

Report:

- the diagnosis
- the recovery action taken or recommended
- whether the original goal succeeded
- any user decision still needed before a mutating retry
