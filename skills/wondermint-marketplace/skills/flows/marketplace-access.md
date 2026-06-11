# Marketplace Access Flow

Use this when the user wants purchase history, listing access, downloads,
metadata, or transaction history for a specific listing.

## Safety Gates

Most access checks are read-only. Downloads may expose private or purchased
content; confirm the target before fetching a private download URL. Use the
shared [Marketplace Router](../marketplace.md) rules.

## Phase 1: Classify The Access Request

Choose the narrowest read path:

- purchase history
- purchase status for a listing
- access check for a listing
- download URL
- listing metadata
- listing transaction history

Use [Marketplace Endpoint Reference](../references/marketplace-endpoints.md)
for endpoint lookup.

## Phase 2: Inspect State

Fetch only what is needed. Confirm listing id/title when available, current
access state, and whether the user owns or purchased the item.

Do not call buy, publish, unpublish, price, or setup endpoints from this flow.
If the user pivots into one of those actions, route to the matching marketplace
flow and apply its approval gate.

## Phase 3: Handle Downloads

Private download URLs can expire. If a URL is stale, poll or request the
download endpoint again rather than reusing the old URL. Do not paste secrets or
credentials into download reports.

## Final Report

Report:

- request type
- listing id/title when known
- access or purchase status
- download or metadata result when requested
- expiry or next step when relevant
