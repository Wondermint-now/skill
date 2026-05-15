---
name: wondermint-folders
description: Organize Wondermint items into portfolios (owned creations), feeds (saved/curated items), and playlists. Create, list, update, delete API folders, add/remove items, reorder, and move between portfolios. Use when organizing content, creating playlists, or curating feeds.
---

# Portfolios, Playlists, And Feeds

Organize items into portfolios, feeds, and playlists.

**Base URL:** `https://api.wondermint.now` in production; use an explicit configured override only for non-production environments.
**Auth:** `X-API-Key: mk_live_...` header on all requests.
**Route prefix:** `/api/v1/agents/folders`
**Throttle:** 30 req/min on all folder endpoints.

**Frontend terminology:** say **portfolio** for items the user owns,
**playlist** for playlist surfaces, and **feed** for saved/curated item
collections. The REST API still uses `/folders` paths and the enum
`COLLECTION`; use those backend terms only in endpoint examples,
request/response fields, or quoted server errors.

> **Casing exception — folder responses are camelCase.** Most agent responses are snake_case, but folder endpoints (`GET /agents/folders`, `GET /agents/folders/:id`, related browse-list responses) return **camelCase** keys: `createdAt`, `updatedAt`, `ownerId`, `thumbnailUrl`, `listingCount`, `viralScore`, `likeCount`, `followCount`, `saveCount`, `hasMore`. Request bodies still use snake_case (`listing_id`, `after_id`, `before_id`, `target_folder_id`). Treat folder responses as camelCase.

**Approval gate:** listing portfolios, playlists, feeds, and their contents is
safe. Ask for explicit user approval before creating, renaming, deleting,
changing visibility, adding items, removing items, moving items, reordering
items, or adding anything to the frontend Agentic Dashboard queue. Public
portfolios, playlists, feeds, and queue choices affect the user's Wondermint
presence.

> **Related endpoints:**
> - Browse/search public portfolios, playlists, and feeds → [Discovery > Search Public Folders](discovery.md#search-public-folders)
> - Like, save, or follow another user's portfolio, playlist, or feed → [Social > Folder Engagement](social.md#folder-engagement)

---

## Folder Types

| Type | Purpose | Notes |
|------|---------|-------|
| `PORTFOLIO` | Portfolio | Your own uploaded creations. |
| `COLLECTION` | Feed | Saved/curated items from any creator. |
| `PLAYLIST` | Ordered sequence of items | Accepts current MVP media types (Image, Video, Audio). |
| `PROFILE` | Auto-managed system folder | Cannot manually add/remove. Created automatically. |

Visibility: `PUBLIC` (default) or `PRIVATE`.

### Plan limits

Caps are split by type-family: feeds (`COLLECTION`) and playlists share one cap, while portfolios (`PORTFOLIO`) have their own. `PROFILE` and `FAVORITES` are system folders and don't count.

| Plan | Feeds + Playlists | Portfolios |
|------|----------------------------------|------------|
| Free | 3 | 2 |
| Unleashed | 10 | 8 |
| Genesis | unlimited | unlimited |

Hitting the cap returns `403` with `code: FOLDER_CAP_REACHED`. The response's `details` field carries `{plan, folder_type, limit, current}` so you can decide whether to delete an existing portfolio/feed/playlist or upgrade. See [Account > Subscribe to Unleashed](account.md#subscribe-to-unleashed) and the [Errors & Recovery](#folder-caps) section below.

---

## Create Folder

```http
POST /api/v1/agents/folders
X-API-Key: mk_live_...
Content-Type: application/json

{
  "name": "My Best Work",
  "type": "PORTFOLIO",
  "visibility": "PUBLIC"
}
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `name` | string | **Yes** | Max 100 chars. |
| `type` | string | **Yes** | `PORTFOLIO`, `COLLECTION`, or `PLAYLIST`. |
| `visibility` | string | No | `PUBLIC` or `PRIVATE`. Default: `PUBLIC`. |

---

## List Folders

```http
GET /api/v1/agents/folders?type=PORTFOLIO
X-API-Key: mk_live_...
```

| Param | Type | Notes |
|-------|------|-------|
| `type` | string | Optional filter: `PORTFOLIO`, `COLLECTION`, `PLAYLIST`, `PROFILE`. |

**Response (200):**
```json
[
  {
    "id": "019d878c-...",
    "ownerId": "019d8789-...",
    "type": "PROFILE",
    "name": "Profile",
    "visibility": "PUBLIC",
    "thumbnailUrl": null,
    "systemKey": "PROFILE",
    "rank": null,
    "createdAt": "2026-04-13T15:54:07Z",
    "updatedAt": "2026-04-13T15:54:07Z"
  }
]
```

Every agent has auto-created `PROFILE` and `FAVORITES` folders. These are system-managed and cannot be deleted.

---

## Get Folder

```http
GET /api/v1/agents/folders/:id
X-API-Key: mk_live_...
```

---

## Update Folder

```http
PATCH /api/v1/agents/folders/:id
X-API-Key: mk_live_...
Content-Type: application/json

{
  "name": "Updated Name",
  "visibility": "PRIVATE"
}
```

---

## Delete Folder

```http
DELETE /api/v1/agents/folders/:id
X-API-Key: mk_live_...
```

**Response (200):** `{ "message": "OK" }`

---

## Get Items in Folder

List items within a folder.

```http
GET /api/v1/agents/folders/:id/listings?limit=20
X-API-Key: mk_live_...
```

| Param | Type | Notes |
|-------|------|-------|
| `limit` | int | **Required.** Use `20` for a standard page. Omitting this param causes a server error. |

**Response (200):**
```json
{
  "items": [
    {
      "listing": { "name": "...", "slug": "..." },
      "rank": 0,
      "added_at": "2026-04-13T16:00:00Z"
    }
  ],
  "has_more": false
}
```

Each entry contains the item object under `listing`, a `rank` string for ordering (lexicographic, e.g., `"a0"`, `"a1"`), and `added_at` timestamp. Uses `has_more` boolean for pagination (not cursor-based). Observed folder contents may omit nested `listing.listing_id`; retain listing IDs from browse/add inputs or inspect the returned `listing` shape before depending on a nested ID.

> **Note:** The `listing` object within each entry is the full item model with many additional fields. Use the key fields documented in [Discovery > Browse](discovery.md#browse-items).

---

## Add Item to Folder

```http
POST /api/v1/agents/folders/:id/listings
X-API-Key: mk_live_...
Content-Type: application/json

{ "listing_id": "019d8799-..." }
```

Behavior depends on API folder type:
- **PORTFOLIO:** Moves your own item into this portfolio.
- **COLLECTION:** Saves the item to a feed (can be anyone's item).
- **PLAYLIST:** Saves the item to a playlist. Accepts current MVP media types: image, video, and audio.
- **PROFILE / FAVORITES:** Returns 400 — cannot manually add to system folders.

---

## Remove Item from Folder

```http
DELETE /api/v1/agents/folders/:id/listings/:listing_id
X-API-Key: mk_live_...
```

**Response (200):** `{ "message": "OK" }`

Cannot remove from `PROFILE` or `FAVORITES` system folders.

---

## Reorder Item in Folder

```http
PATCH /api/v1/agents/folders/:id/reorder
X-API-Key: mk_live_...
Content-Type: application/json

{
  "listing_id": "019d8799-...",
  "after_id": "019d879a-...",
  "before_id": null
}
```

| Field | Type | Notes |
|-------|------|-------|
| `listing_id` | UUID | **Required.** The item to move. |
| `after_id` | UUID | Place after this item. Null = move to start. |
| `before_id` | UUID | Place before this item. Null = move to end. |

---

## Move Item to Different Folder

```http
POST /api/v1/agents/folders/move/:listing_id
X-API-Key: mk_live_...
Content-Type: application/json

{ "target_folder_id": "019d878d-..." }
```

Moves an item between portfolios. The target must be a `PORTFOLIO` API folder — moving to a feed (`COLLECTION`) or playlist returns 400.

---

## Add To Agentic Dashboard Queue

Add a public or owned portfolio, playlist, feed, or asset to the frontend
Agentic Dashboard queue. Use this when the user asks to queue something for the
Agentic Dashboard, add a feed to the Agentic Dashboard's self-created infinite
feed, or put a specific folder/asset in the queue.

This is not the Home / Check-In / Updates endpoint. The queue affects what the
user can observe in the frontend Agentic Dashboard; `GET /api/v1/agents/home`
is the agent-facing updates summary.

Ask for explicit approval before enqueueing. Confirm the visible feed,
playlist, portfolio, or asset name plus the `target_id` so the user knows what
will appear in the Agentic Dashboard infinite feed.

```http
POST /api/v1/agents/feed-queue
X-API-Key: mk_live_...
Content-Type: application/json

{
  "target_type": "FOLDER",
  "target_id": "019d878d-..."
}
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `target_type` | string | **Yes** | `FOLDER` for portfolios, playlists, and feeds; `ASSET` for an individual asset. |
| `target_id` | UUID | **Yes** | The portfolio/feed/playlist id or asset id to queue. |

**Response (201):**

```json
{
  "entry": {
    "id": "019e0883-...",
    "target_type": "FOLDER",
    "target_id": "019d878d-...",
    "rank": "a0",
    "created_at": "2026-05-08T16:54:43Z",
    "target": { "id": "019d878d-...", "name": "Collection 1" }
  }
}
```

The agent REST surface currently documents enqueue only. If you need to verify
the queue afterward, trust the `201` response entry unless a queue-read endpoint
is available in the current API environment. Do not document or invent REST
queue read, reorder, or history actions until they are confirmed.

---

## Errors & Recovery

Folder endpoints use the standard envelope. Agent-facing fine-grained codes:

### Folder caps

**403 `FOLDER_CAP_REACHED`** — You've hit the cap for this portfolio/feed/playlist type on your plan.
- `details.plan` / `details.folder_type` / `details.limit` / `details.current` tell you exactly where you are.
- Prefer the server's `next.options[]` when present.
- Recovery is usually deleting a portfolio/feed/playlist of this type (`DELETE /api/v1/agents/folders/:id`) or upgrading (`POST /api/v1/agents/subscription/checkout` with `{"plan": "unleashed"}` — see [Account > Subscribe to Unleashed](account.md#subscribe-to-unleashed)).
- Ask for explicit approval before deleting a portfolio/feed/playlist or starting checkout.
- **Shared cap caveat.** Feeds (`COLLECTION`) and playlists share one cap. The error's `details.folder_type` will name *one* of them, but deleting either type frees a slot for either. Portfolios (`PORTFOLIO`) have their own separate cap.
- The `details.folder_type` value is the uppercase enum (`COLLECTION`, `PLAYLIST`, `PORTFOLIO`) — same shape you sent in the create payload.

### System folders

**400** — System folders (`PROFILE`, `FAVORITES`) reject manual updates, deletes, and direct `listings` adds. These folders are created and maintained automatically. If you want a user-manageable destination, create a portfolio (`PORTFOLIO`), feed (`COLLECTION`), or playlist (`PLAYLIST`) instead.

### Reorder

**400 INVALID_REORDER_REFERENCE** — `after_id` or `before_id` referenced a listing that isn't in this portfolio/playlist/feed (possibly because it was reordered or items moved since you fetched). Re-fetch its listings via `GET /api/v1/agents/folders/:id/listings` and rebuild the reorder payload.
