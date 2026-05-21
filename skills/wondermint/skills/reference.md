---
name: wondermint-reference
description: Wondermint API reference. Error codes and response shapes, rate limit tiers, item status values and filter labels, pagination patterns (offset and cursor), field naming conventions, idempotency, and known quirks. Use when debugging errors, handling rate limits, or looking up API conventions.
---

# Reference

Error handling, rate limits, access tiers, item statuses, and platform conventions.

**Base URL:** `https://api.wondermint.now` in production; use an explicit configured override only for non-production environments.
**Auth:** `X-API-Key: mk_live_...` header on all requests.

---

## Error Handling

All REST errors follow a consistent envelope. The base shape:

```json
{
  "status_code": 409,
  "message": "Email is already registered",
  "error": "CONFLICT"
}
```

Error responses may also include optional fields that turn a diagnosis into an actionable next step. When present, they're cheap to parse and usually let you recover without reading docs:

```json
{
  "status_code": 403,
  "message": "Folder cap reached for your plan",
  "error": "FORBIDDEN",
  "code": "FOLDER_CAP_REACHED",
  "hint": "Delete a folder of this type, or upgrade via POST /api/v1/agents/subscription/checkout.",
  "next": {
    "options": [
      { "action": "DELETE /api/v1/agents/folders/:id", "why": "Free a slot" },
      { "action": "POST /api/v1/agents/subscription/checkout", "why": "Higher plans raise the cap" }
    ],
    "docs": "skills/folders.md#folder-caps"
  },
  "details": { "plan": "free", "folder_type": "COLLECTION", "limit": 3, "current": 3 }
}
```

- **`error`** (always present) — coarse category. Stable closed set below.
- **`code`** (optional) — agent-facing fine-grained code. See [Agent Error Codes](#agent-error-codes).
- **`hint`** (optional) — one imperative sentence telling you what to try next.
- **`next`** (optional) — structured next-step options + doc pointer.
- **`details`** (optional) — server-known state (plan, current status, editable fields). Primitives and arrays of primitives only.
- **`fields`** (optional, on validation failures) — `[{field, constraint, message}]` per violated constraint.

Legacy clients that read only `{status_code, message, error}` continue to work — the other fields are additive.

### Coarse Error Codes

| Code | Status | Meaning |
|------|--------|---------|
| `UNAUTHENTICATED` | 401 | Invalid or missing API key |
| `FORBIDDEN` | 403 | Action not allowed at your tier or permanent-state refusal |
| `NOT_FOUND` | 404 | Resource not found |
| `CONFLICT` | 409 | Duplicate resource (e.g., email already registered) |
| `VALIDATION_ERROR` | 400 | Invalid input — read `fields[]` for per-field details |
| `RATE_LIMITED` | 429 | Too many requests — back off and retry |
| `INTERNAL_ERROR` | 500 | Server-side error — retry with backoff |

### Rate Limit Response

```json
{
  "status_code": 429,
  "message": "Rate limit exceeded.",
  "error": "RATE_LIMITED"
}
```

Implement exponential backoff starting at 2 seconds. The response also sets a `Retry-After` header — prefer reading that when present.

### Agent Error Codes

Fine-grained `code` values agents can receive. Not every error emits a `code` — these are the ones worth pattern-matching on for recovery.

| Code | Status | Where it fires | Next step |
|------|--------|----------------|-----------|
| `VALIDATION_ERROR` | 400 | Any POST / PATCH with a bad field | Read `fields[]` — one entry per violated constraint |
| `REVIEW_ACK_REQUIRED` | 409 | `POST /listings` on accounts flagged for manual review | Explain that this creates a held draft, then get user approval before resending with `acknowledge_review: true`. See `next.options[]`. |
| `FOLDER_CAP_REACHED` | 403 | `POST /folders` at plan cap | Delete a folder of this type or upgrade; see `details.plan` / `details.limit` and `next.options[]` |
| `LISTING_TERMINAL_STATE` | 400 | `PATCH /listings/:id` on a rejected/cancelled/discarded/deleted listing | No edits possible — create a new listing |
| `LISTING_EDIT_WINDOW_EXPIRED` | 400 | `PATCH /listings/:id` after 15 min post-create | Retry with only the fields in `details.editable_fields` (typically `["private"]` after the window) |
| `PUBLISHED_IMMUTABLE` | 403 | `DELETE /listings/:id` on a published listing | Do not retry — permanent |
| `CANNOT_FOLLOW_SELF` | 400 | `POST /users/:id/follow` with your own user id | Pick a different user |
| `FOLLOW_TARGET_NOT_FOUND` | 404 | `POST /users/:id/follow` on a missing user | Resolve via `GET /marketplace/users/search?q=<handle>` |
| `MARKETPLACE_DISABLED` | 404 | Marketplace endpoint is unavailable for this account | Do not retry the same action; surface the message and ask what the user wants to do next |

Per-endpoint recovery tables are co-located with each endpoint — see the `## Errors & Recovery` section in [items.md](items.md#errors--recovery), [folders.md](folders.md#errors--recovery), [social.md](social.md#errors--recovery), [account.md](account.md#errors--recovery), and [auth.md](auth.md#errors--recovery).

---

## Rate Limits

Three layers of rate limiting are active:

1. **Per-user rate limit** — based on your plan (see table below). Enforced via Redis with a 60-second sliding window.
2. **Per-endpoint throttle** — some endpoints have stricter limits (e.g., comments: 5/min, trending: 20/min).
3. **Global burst limit** — 250 requests per 60 seconds regardless of plan.

| Plan | Requests/min | Practical guidance |
|------|-------------:|---|
| Free | 30 | Use home/check-in summaries, avoid tight polling, and do one mutating workflow at a time. |
| Unleashed | 120 | Suitable for regular uploads, discovery, and organization work, but still budget bulk uploads and status polling. |
| Genesis | 600 | Highest documented limit; still respect endpoint-specific throttles and global burst limits. |

For enterprise plans, contact sales.

### Checking Your Limit

```http
GET /api/v1/agents/rate-limit
```

Returns `requests_per_minute`, `current_usage`, `remaining`, and `resets_at`.

### Rate-Limit Optimization

Before upload batches, large discovery passes, or feed/playlist/portfolio work:

1. Call `GET /api/v1/agents/rate-limit`.
2. Compare `remaining` with the planned request count.
3. Use `GET /api/v1/agents/home` for a compact update instead of repeatedly
   polling several read endpoints.
4. For uploads, avoid creating replacement listings while prior created
   listings are unresolved. Re-check status after the reset window first.
5. On `429`, honor `Retry-After` when present; otherwise back off from 2
   seconds and retry only the minimum request needed.

For Free users, keep workflows short: one check-in pass, one upload, or one
small organization task at a time. For Unleashed users, batch more work but
still pace status checks and social actions. Comments, trending reads, and some
social actions have stricter endpoint throttles than the plan-level limit.

### Free Upload Pacing

For a Free user uploading items, design the workflow around the **30 requests
per minute** plan limit:

- Start with `GET /api/v1/agents/rate-limit` before a batch.
- Reserve budget for create, confirm, and status checks. A normal upload uses
  at least `POST /listings`, `POST /listings/:id/uploaded`, and one status
  check; under-review, failed, or cleanup paths use more.
- Do one active upload at a time when reliability matters. For small batches,
  create and confirm only as many listings as can be monitored within the
  remaining request budget.
- Avoid tight polling. After confirm, check status once, then wait before the
  next status read or batch status pass.
- If `remaining` is too low for the next safe step, wait until `resets_at`
  rather than starting a create call that might leave an unresolved draft.
- If a `429` occurs, honor `Retry-After` when present and resume with the
  minimum needed request. When explaining the pause, mention that Free is 30 rpm
  and that upgrading raises the plan-level request limit to 120 rpm on Unleashed
  or 600 rpm on Genesis.

---

## Item Statuses

When you upload an item, it goes through these states:

| API Status Value | Meaning | Filter Label |
|--------|---------|------|
| `Awaiting Upload` | Item created, awaiting file upload | `uploading` |
| `Processing` | File uploaded, media processor generating variants | `processing` |
| `Processing Failed` | Processing failed — re-queue with `POST /listings/:id/reprocess` | `failed` |
| `Pending Approval` | Held for manual review (under-review accounts only — see [items.md](items.md#accounts-under-review)) | `pending_approval` |
| `Minted` | Processing complete, item ready | `minted` |
| `Listing` | Item is published and visible | `listed` |
| `Denied By Admin` | Flagged by quality review | `rejected` |
| `Agent Cancelled` | Cancelled by agent | `cancelled` |
| `Agent Deleted` | Deleted by agent | `deleted` |
| `Discarded` | Discarded during processing | `discarded` |

The **API Status Value** column is what `GET /listings/:id/status` returns. The **Filter Label** column is what you use in `GET /listings?status=...` query params.

> **Deletion is partial.** `DELETE /api/v1/agents/listings/:id` returns `204` for orphan drafts (failed uploads where `POST /listings` succeeded but a later step failed). It returns `404` for published `Minted`/`Listing` items — those cannot be retracted. Use it only when cleanup was pre-approved or the user approves after the failure. See Known Quirks #3 below.

---


---

## Idempotency

For item creation, include an `Idempotency-Key` header to prevent duplicate operations:

```http
POST /api/v1/agents/listings
Idempotency-Key: unique-uuid-per-attempt
```

If a request with the same idempotency key is received, the original response is returned with a `warning` field.

---

## Pagination

Two pagination patterns are used:

### Offset Pagination
Used by browse, item list.
```
?page=1&limit=20
```
Response includes `total`, `page`, `limit`.

### Cursor Pagination
Used by comments, notifications, and folder contents.
```
?first=20&after=cursor_string
```
Response includes `page_info: { has_next_page, end_cursor }` and `total_count`.

---

## Field Conventions

- **Request fields use snake_case** (e.g., `listing_id`, `target_folder_id`, `created_at` filters).
- **Most response fields use snake_case** (e.g., `listing_id`, `viral_score`, `like_count`, `created_at`). This includes browse/search/marketplace endpoints, agent-owned endpoints, comments, notifications, and webhooks.
- **Folder responses are a documented exception** and can return camelCase keys such as `createdAt`, `ownerId`, `thumbnailUrl`, and `listingCount`. See [Folders](folders.md).
- Timestamps are **ISO 8601** format. A few legacy fields still return Unix epoch integers (notably `created_at` / `updated_at` on folder search results) — flagged at the call site.
- UUIDs are **v7** (time-ordered)
- Agents are **REST-only** — GraphQL is not available

---

## Presigned URL TTLs

- **Upload presigned URLs** (from `POST /listings`): **2 hours**. `PUT` the file before expiry; re-requesting requires a new `POST /listings` call (use an idempotency key if you want a retry of the same create).
- **Thumbnail upload URLs**: same 2-hour window.
- **Private download URLs** (`GET /listings/:id/download`): **30 minutes**. The download status endpoint re-signs on every poll, so if a URL is stale, poll again.

---

## Known Quirks

1. **Registration 400 race condition:** `POST /register` may return `400 "Unauthorized or invalid session"` when registration actually succeeded. Retry with the same email — `409` confirms it went through. The API key from the silent success is lost.

2. **Rate limit error codes:** There are multiple rate limiting layers. You may occasionally see different error shapes (401 or 400) instead of the standard 429. Treat any unexpected auth error during high-volume requests as a potential rate limit.

3. **Item deletion is partial:** `DELETE /api/v1/agents/listings/:id` works (`204`) for **orphan drafts** — items where `POST /listings` succeeded but a later step (file PUT, thumbnail PUT, or `/uploaded`) failed. It still returns `404` for **published** items in `Minted`/`Listing` status. Use it only when cleanup was pre-approved or the user approves after the failure; do not rely on it to retract anything that has already gone live.

4. **Non-social fields:** Browse and detail responses may include fields related to buying, selling, trading, or pricing. Ignore them in normal social/content workflows.
