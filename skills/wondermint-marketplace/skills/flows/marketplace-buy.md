# Marketplace Buy Flow

Use this when the user wants to buy a listing or check a direct purchase status.

## Safety Gates

Buying is financial. Do not call `POST /api/v1/agents/listings/:id/buy` until
the user approves the exact listing, price or terms, account, and follow-up
polling plan. Use [Confirmation Gates](confirmation-gates.md) and the shared
[Marketplace Router](../marketplace.md) rules.

## Phase 1: Identify The Listing

Confirm the listing id and human-readable title. If the user gives a slug,
title, or vague reference, resolve it read-only through discovery or detail
before asking for purchase approval.

Use [Marketplace Endpoint Reference](../references/marketplace-endpoints.md)
for endpoint lookup.

## Phase 2: Inspect Current State

Before buying:

- fetch listing detail when needed
- check existing access or purchase status when available
- report if the user already has access
- confirm price, currency, fees, and purchase terms when present

Prefer reporting an existing purchase or access grant over repeating the buy
action.

## Phase 3: Get Purchase Approval

Show the user:

- listing id and title
- seller or creator when available
- price, currency, fees, or terms
- current access/purchase state
- what endpoint will be called
- how purchase status will be verified

Wait for explicit approval.

## Phase 4: Buy And Poll

Call the buy endpoint once. Preserve the idempotency key returned or used by the
request and use it when polling purchase status. Poll sparingly until terminal
status or a clear next step.

If the request fails or times out, check purchase status before retrying. Do not
send another buy request until the server state and user approval are clear.

## Final Report

Report:

- listing id/title
- purchase status
- idempotency key if useful and non-secret
- access or download next step
- whether any user action is still required
