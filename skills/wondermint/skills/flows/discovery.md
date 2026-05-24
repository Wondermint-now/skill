# Discovery Flow

Use this when the user wants to browse Wondermint, search for items, find creators, explore public portfolios/playlists/feeds, decide what to engage with, or show a specific image/asset/item in the Agentic Dashboard. Endpoint shapes live in [Discovery](../discovery.md); this file covers the conversation.

## Goal

Help the user find relevant work or creators and decide on a useful next action without taking public engagement actions without approval.

## Phase 1: Understand The Intent

Clarify what to find:

- items by keyword, style, medium, or category
- creators by username or topic
- public portfolios, playlists, or feeds (`COLLECTION` in API = "feed" to the user)
- trending work to browse without a specific query
- examples to inspire an upload or comment
- a specific image/asset/item ID the user wants displayed as a large dashboard preview

If casual, start with trending. If a creator is named, use user search or open their profile.

## Phase 2: Run The Search

See [Discovery](../discovery.md) for endpoint shapes. There's no combined search endpoint — items, folders, and users are separate:

- Items → `GET /api/v1/agents/marketplace?q=&category=&sort=trending`
- Folders → `GET /api/v1/agents/marketplace/folders?q=&type=COLLECTION&sort=viral_score`
- Users → `GET /api/v1/agents/marketplace/users/search?q=` (min 2 chars)
- Known username → `GET /api/v1/agents/marketplace/users/:username`

### Show A Specific Image In Dashboard Activity

When the user says "show me this image," "pull up a large image," "open this asset," or similar and gives an asset/listing ID, do a read-only exact-ID search:

```http
GET /api/v1/agents/marketplace?q=<asset-or-listing-id>&category=Image&limit=1&page=1
```

The Agentic Dashboard activity then renders the item as a large preview, similar to what appears after like/save/share — without creating any engagement. Don't like, save, share, or record a view just to make the image appear. Fetch detail with `GET /marketplace/:id` only if verification is needed.

## Phase 3: Inspect Details When Needed

Browse lists are good for scanning, not authoritative for the current viewer. Fetch item detail (`GET /marketplace/:id`) when:

- the user is deciding whether to like/favorite/share/comment
- `is_liked`, `is_favorite`, or `is_viewed` matters
- the creator username is missing from the browse result
- the user asks for a specific item by slug, name, or id

Use ranking position, not the absolute `viral_score`, when summarizing what's hot — see [Discovery > Browse Items](../discovery.md#browse-items) for why.

## Phase 4: Summarize

Give a compact summary: top 3–5 results, why each matches the intent, media type / creator / engagement context when useful, one recommended next action. Don't dump raw payloads.

## Phase 5: Ask Before Engagement

Discovery is read-first. Route approved actions:

- comments/replies → [Comment And Reply Flow](comment-reply.md)
- likes, favorites, follows, shares → [Social](../social.md)
- uploads → [Upload Flow](upload.md)
- category and tag selection → [Category Selection Flow](category-selection.md)
- portfolio/playlist/feed organization → [Folder Organization Flow](folder-organization.md)

## Final Report

What you searched, the most relevant results, any detail pages opened, the recommended next action, and which public actions still need approval.
