# Portfolio, Playlist, And Feed Organization Flow

Use this when the user wants to organize Wondermint items into portfolios, playlists, or feeds. Endpoint shapes live in [Folders](../folders.md); this file covers the conversation around organizing.

## Goal

Help the user pick a clear destination, place the right items in it, and avoid plan-limit surprises.

## Phase 1: Clarify The Organization Job

Ask what the destination is for:

- showcasing the user's own work → `PORTFOLIO`
- curating any creator's work as a feed → `COLLECTION`
- building an ordered sequence → `PLAYLIST`

Use frontend terms in conversation (portfolio, playlist, feed). Don't say "folder" or "collection" unless quoting an API path, enum, or server response.

Also clarify visibility: `PUBLIC` if it should be discoverable, `PRIVATE` for personal organization.

Do not use `PROFILE` or `FAVORITES` for manual organization — they're system-managed.

Create/rename/delete/visibility/membership/reorder/queue mutations follow [Confirmation Gates](confirmation-gates.md). Show the proposed item list and get approval before adding, moving, removing, or reordering.

### "Show me that folder" wording

If the user says "show me that folder," "show that feed," "open that playlist in the dashboard," or similar, route to [Folders > Add To Agentic Dashboard Queue](../folders.md#add-to-agentic-dashboard-queue). When the target is clear from context, this wording authorizes enqueueing with `target_type: "FOLDER"`. If ambiguous, ask which one.

### "Best images" subflow

When the user asks for their "best" items without defining "best":

1. List owned items via [Items > List Your Items](../items.md#list-your-items).
2. Keep only published image items (`category` = `Image`; status `Minted` or `Listing`).
3. Rank by the user's chosen signal. If they don't choose, propose a balanced shortlist using likes, views, comments, and recency. For exact metrics, fetch `GET /api/v1/agents/listings/:id/metrics`.
4. Show candidate names and ids.
5. Get approval before adding or moving them.

## Phase 2: Inspect Existing Destinations

List existing portfolios/playlists/feeds with `GET /api/v1/agents/folders` (optionally `?type=PORTFOLIO|COLLECTION|PLAYLIST|PROFILE`) before creating or changing anything. Folder responses are camelCase — see [Folders](../folders.md). Prefer reusing an existing destination when it clearly matches intent.

## Phase 3: Create Or Mutate

For endpoint shapes (`POST /folders`, `PATCH /folders/:id`, add/remove/move/reorder, get-items), see [Folders](../folders.md). Two notes specific to this flow:

- For ordered destinations (`PLAYLIST` or reordering inside a portfolio/feed), fetch current contents first via `GET /api/v1/agents/folders/:id/listings?limit=20` — `limit` is required.
- A move (`POST /folders/move/:listing_id`) only targets a `PORTFOLIO`; moving to a feed or playlist returns 400.

## Phase 4: Handle Cap Errors

If creation returns `403 FOLDER_CAP_REACHED`, read `details.plan` / `details.folder_type` / `details.limit` / `details.current` and prefer `next.options[]`. Recovery: delete one of the capped family, reuse an existing destination, or upgrade via [Upgrade Flow](upgrade.md). Get explicit approval before any of these. Feeds (`COLLECTION`) and playlists share one cap; portfolios have their own.

## Final Report

Tell the user: which portfolio/playlist/feed was used or created, public or private, whether it was added to the Agentic Dashboard queue, which items moved, any cap or visibility caveat, and what to do next.
