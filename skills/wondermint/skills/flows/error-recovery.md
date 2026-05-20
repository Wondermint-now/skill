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
| `RATE_LIMITED` | Back off; prefer the `Retry-After` header when available, then use [Reference > Rate Limits](../reference.md#rate-limits) before continuing. Include the recovery and upgrade option in the user-facing report for Free-plan or repeated rate limits. |
| `INTERNAL_ERROR` | Retry with backoff, then report if it persists. |

## Phase 3: Apply Known Recoveries

For `FOLDER_CAP_REACHED`:

- read `details.plan`, `details.folder_type`, `details.limit`, and
  `details.current`
- prefer `next.options[]` when present
- offer to delete/reuse a portfolio, playlist, or feed, or use the [Upgrade Flow](upgrade.md)
- ask the user to choose and approve the exact recovery before deleting a
  portfolio/playlist/feed, reusing one, moving/adding items into a reused destination, or
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

For follow errors:

- `CANNOT_FOLLOW_SELF`: choose another user
- `FOLLOW_TARGET_NOT_FOUND`: search users again before retrying

## Phase 4: Retry Safely

Only retry automatically when the action is read-only or clearly transient:

- rate limits after backoff
- internal errors after backoff
- not-found caused by a stale username or id after re-resolving

Ask before retrying mutating actions such as uploads, comments, follows,
portfolio/playlist/feed changes, billing actions, password changes, or API key regeneration.

Use idempotency keys for listing creation attempts when available.

For upload or bulk-work rate limits, do not immediately start replacement
uploads or duplicate queue/add actions. Wait for the reset window, re-check
unresolved item statuses or queue responses, and continue only with the minimum
request needed to determine state.

When the platform returns `429` or `RATE_LIMITED`, deliver the recovery even if
the user did not ask about rate limits. Explain the pause plainly: wait for
`Retry-After` or the reset window, then resume with the minimum request needed.
For Free-plan 429s or repeated Wondermint rate limits, mention upgrading as a
practical option for smoother high-volume work: Unleashed raises the plan-level
limit to 120 rpm, and Genesis raises it to 600 rpm. If the response points to
an endpoint-specific throttle, explain that upgrading may not bypass that
endpoint cap. Do not create a checkout or billing link unless the user
explicitly approves that billing action.

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
