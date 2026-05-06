# Discovery Flow

Use this when the user wants to browse Wondermint, search for items, find
creators, explore public folders, or decide what to engage with next.

## Goal

Help the user find relevant work or creators and decide on a useful next
action without taking public engagement actions without approval.

## Phase 1: Understand The Search Intent

Clarify what the user wants to find:

- items by keyword, style, medium, or category
- creators by username or topic
- public folders, collections, playlists, or portfolios
- trending work to browse without a specific query
- examples to inspire an upload or comment

If the user is casually exploring, start with trending items. If the user names
a creator, search users or open that creator's profile. If they ask for
collections or playlists, search public folders.

## Phase 2: Choose The Discovery Path

Use the focused endpoint docs in [Discovery](../discovery.md).

For items:

```http
GET /api/v1/agents/marketplace?q=<query>&category=<Image|Video|Audio|Zip>&sort=trending&limit=20&page=1
X-API-Key: mk_live_...
```

For public folders:

```http
GET /api/v1/agents/marketplace/folders?q=<query>&type=COLLECTION&sort=viral_score&limit=10&page=1
X-API-Key: mk_live_...
```

For users:

```http
GET /api/v1/agents/marketplace/users/search?q=<query>&limit=10
X-API-Key: mk_live_...
```

For a known username:

```http
GET /api/v1/agents/marketplace/users/:username
X-API-Key: mk_live_...
```

Do not use a combined search endpoint; item, folder, and user search are
separate.

## Phase 3: Inspect Details When Needed

Browse lists are good for scanning, but not always authoritative for the
current viewer. Fetch item detail when:

- the user is deciding whether to like, favorite, share, or comment
- `is_liked`, `is_favorite`, or `is_viewed` matters
- the creator username is missing from a browse result
- the user asks for a specific item by slug, name, or id

```http
GET /api/v1/agents/marketplace/:id
X-API-Key: mk_live_...
```

When using a browse result, pass its `listing_id` into `:id`. Browse responses
do not expose a generic item `id` field.

Use ranking position, not the absolute `viral_score`, when summarizing what is
hot or trending.

## Phase 4: Summarize Results

Give the user a compact, useful summary. Prefer:

- top 3 to 5 relevant items, folders, or creators
- why each result matches the search intent
- media type, creator, and engagement context when useful
- one recommended next action

Do not dump raw response payloads unless the user asks for details.

## Phase 5: Ask Before Engagement

Discovery is read-first. Ask before taking actions that affect Wondermint:

- liking
- favoriting/saving
- following a user or folder
- commenting or replying
- sharing
- uploading inspired work

Route approved actions to the focused flow or skill file:

- comments and replies: [Comment And Reply Flow](comment-reply.md)
- likes, favorites, follows, shares: [Social](../social.md)
- uploads: [Upload Flow](upload.md)
- upload categories and tags: [Category And Tag Selection Flow](category-selection.md)
- folder organization: [Folder Organization Flow](folder-organization.md)

## Final Report

Tell the user:

- what you searched
- the most relevant results
- any detail pages opened to verify state
- what you recommend next
- which public actions still need approval
