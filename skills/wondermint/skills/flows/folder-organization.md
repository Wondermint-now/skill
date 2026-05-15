# Portfolio, Playlist, And Feed Organization Flow

Use this when the user wants to organize Wondermint items into portfolios,
playlists, or feeds.

## Goal

Help the user make a clear organization structure, place the right items in it, and
avoid plan-limit surprises.

## Phase 1: Clarify The Organization Job

Ask what the destination is for:

- showcasing the user's own work: use `PORTFOLIO`
- curating any creator's work as a feed: use `COLLECTION`
- building an ordered sequence: use `PLAYLIST`

Use frontend terms in conversation: portfolio, playlist, and feed. Do not say
"folder" or "collection" to the user unless quoting an API path, enum, or
server response.

For creating, changing, deleting, moving, reordering, or queueing portfolios,
playlists, feeds, or assets, use [Confirmation Gates](confirmation-gates.md).

Also clarify visibility:

- `PUBLIC` if the folder should be discoverable
- `PRIVATE` if it is for personal organization

If the user asks for their "best" items, ask what "best" means before changing
portfolios, playlists, or feeds. Good defaults to offer are user-selected picks, highest likes, highest
views, highest comments, or most recent finished uploads. Show the proposed
item list and get approval before adding, moving, removing, or reordering items.

For "best images" when the user wants the agent to choose candidates:

1. List owned items with [Items > List Your Items](../items.md#list-your-items).
2. Keep only published image items (`category` or item detail indicates `Image`;
   status is `Minted` or `Listing`).
3. Rank by the user's chosen signal. If they do not choose, propose a balanced
   shortlist using likes, views, comments, and recency. For exact owned-item
   metrics, fetch `GET /api/v1/agents/listings/:id/metrics`.
4. Show the candidate item names and ids.
5. Get approval before adding or moving them into the destination.

Do not use `PROFILE` or `FAVORITES` for manual organization. They are
system-managed folders.

## Phase 2: Inspect Existing Destinations

List existing portfolios, playlists, and feeds before creating or changing anything:

```http
GET /api/v1/agents/folders
X-API-Key: mk_live_...
```

If the user named a type, filter by type:

```http
GET /api/v1/agents/folders?type=PORTFOLIO
X-API-Key: mk_live_...
```

Folder API responses may use camelCase response keys even when request bodies use
snake_case.

Prefer reusing an existing portfolio, playlist, or feed when it clearly matches
the user's intent.

## Phase 3: Create Or Update The Destination

For a new portfolio, playlist, or feed:

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

For renaming or changing visibility:

```http
PATCH /api/v1/agents/folders/:id
X-API-Key: mk_live_...
Content-Type: application/json

{
  "name": "Updated Name",
  "visibility": "PRIVATE"
}
```

Ask before creating, renaming, deleting, or changing visibility. Public
portfolios, playlists, and feeds affect the user's Wondermint presence.

## Phase 4: Add, Remove, Move, Or Reorder Items

Add an item:

```http
POST /api/v1/agents/folders/:id/listings
X-API-Key: mk_live_...
Content-Type: application/json

{ "listing_id": "019d8799-..." }
```

Remove an item:

```http
DELETE /api/v1/agents/folders/:id/listings/:listing_id
X-API-Key: mk_live_...
```

Move an owned item between portfolios:

```http
POST /api/v1/agents/folders/move/:listing_id
X-API-Key: mk_live_...
Content-Type: application/json

{ "target_folder_id": "019d878d-..." }
```

Reorder an item:

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

If order matters, fetch the current contents first:

```http
GET /api/v1/agents/folders/:id/listings?limit=20
X-API-Key: mk_live_...
```

Include `limit`; omitting it can fail.

## Phase 5: Handle Folder Limits

Free, Unleashed, and Genesis have different portfolio/feed/playlist caps. If creation returns
`FOLDER_CAP_REACHED`, read `details.plan`, `details.folder_type`,
`details.limit`, `details.current`, and `next.options[]`.

Recovery options usually are:

- delete an existing portfolio, feed, or playlist of the capped family
- upgrade through the [Upgrade Flow](upgrade.md)
- reuse an existing portfolio, feed, or playlist

Ask the user to choose and approve the exact recovery before deleting a
portfolio, feed, or playlist, starting checkout, reusing an existing
destination, or moving/adding items into a reused destination. Prefer the
server's `next.options[]` when present.

Feeds (`COLLECTION`) and playlists share one cap. Portfolios (`PORTFOLIO`) have
their own cap.

## Final Report

Tell the user:

- which portfolio, playlist, or feed was used or created
- whether it is public or private
- which items were added, removed, moved, or reordered
- any cap or visibility caveat
- what they can do next, such as sharing it or adding more items
