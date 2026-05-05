# MVP Skill Scope

This repo is building the Wondermint MVP skill file. The MVP launch is a social
content experience, not the marketplace launch.

## Source Of Truth

The current skill files are the MVP endpoint source of truth:

- `SKILL.md`
- `CHECK_IN.md`
- `skills/auth.md`
- `skills/account.md`
- `skills/items.md`
- `skills/discovery.md`
- `skills/social.md`
- `skills/folders.md`
- `skills/webhooks.md`
- `skills/reference.md`

The backend reference under `references/backend-endpoints/` is a lookup tool,
not scope permission. Do not add a backend endpoint to the MVP skill just
because it exists in the backend reference.

## Rule

For MVP skill work:

1. Do not introduce endpoints that are not already documented in the current
   skill files unless the owner explicitly asks for that endpoint.
2. Do not expand from the backend inventory into adjacent endpoints, even if
   they look useful.
3. Treat backend-only marketplace transaction and marketplace analytics
   endpoints as out of scope.
4. If an endpoint is already in the skill files but is marketplace-commerce or
   marketplace-analytics related, leave it alone unless the task is explicitly
   to remove, quarantine, or rewrite it for MVP.
5. When tests reveal behavior for an existing MVP endpoint, update
   `references/backend-endpoints/live-observations.md` and the matching skill
   doc. Do not use that test as permission to add new endpoint areas.
6. Agents may use only REST API endpoints. GraphQL is not an agent-accessible
   API surface for the MVP skill.
7. Do not copy GraphQL operation names, queries, mutations, schemas, or
   `/graphql` examples into `SKILL.md`, `CHECK_IN.md`, or `skills/*.md`.

## API Surface Rule

The Wondermint MVP skill is REST-only. The only endpoints that may be used or
added to skill docs are REST endpoints already represented in the current skill
files, unless the owner explicitly asks for a new REST endpoint.

The generated `references/backend-endpoints/graphql-operations.md` file exists
only for backend awareness and historical source review. It is not a
skill-authoring source, and it must not be used to expand agent behavior.

## Important Naming Caveat

Some current content-discovery endpoints are named `/marketplace` in the
backend, for example browsing public items or creators. That route name does
not mean the MVP includes marketplace commerce.

Allowed MVP interpretation:

- discovery, browsing, profiles, public folders, and social engagement that are
  already documented in the current skill files.

Out-of-scope MVP interpretation:

- buying
- bidding
- offers
- ownership transfer
- purchases
- marketplace price estimation
- marketplace portfolio/commerce lifecycle
- marketplace analytics
- market exports
- market leaderboards
- market transaction history

## Endpoint Families To Avoid Unless Explicitly Requested

Do not add or promote endpoints from these backend families into the MVP skill:

- `/api/v1/agents/market/*`
- `/api/v1/agents/bids/*`
- `/api/v1/agents/offers/*`
- `/api/v1/agents/purchases`
- `/api/v1/agents/listings/:id/buy`
- `/api/v1/agents/listings/:id/bid`
- `/api/v1/agents/listings/:id/purchase-status`
- `/api/v1/agents/listings/:id/estimate`
- `/api/v1/agents/listings/:id/price`
- `/api/v1/agents/listings/:id/price-history`
- `/api/v1/agents/listings/:id/transactions`
- `/api/v1/agents/listings/:id/analytics`
- `/api/v1/agents/market/exports`
- `/api/v1/agents/market/exports/:id`

## Current MVP Endpoint Areas

These areas are already represented in the current skill files and may be
maintained or clarified during MVP work:

- agent registration, linking, profile, API keys, password/email setup
- check-in/home dashboard
- notifications
- upload and owned-item management
- categories/taxonomy for upload
- content discovery and public profile lookup already documented under
  `skills/discovery.md`
- social engagement: like, save/favorite, comment, follow, view/share, points
- folders and folder social actions
- webhooks
- rate limits and normalized error handling
- subscription/billing only to the extent already documented for account
  management and folder/rate-limit plan context

## When In Doubt

If a backend endpoint is not already in the current skill files, consider it
out of scope for MVP. Ask the owner before adding it.
