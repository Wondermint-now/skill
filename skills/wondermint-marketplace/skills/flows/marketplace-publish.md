# Marketplace Publish Flow

Use this when the user wants to publish, unpublish, price, or estimate an owned
listing.

## Safety Gates

Publishing, unpublishing, and price changes are user-visible marketplace
mutations. Ask for explicit approval before each mutation. Use
[Confirmation Gates](confirmation-gates.md) and the shared
[Marketplace Router](../marketplace.md) rules.

## Phase 1: Confirm Ownership And Target

Identify the owned listing. If the target is unclear, list or inspect owned
listings before continuing. Do not use public marketplace detail alone as proof
that the user owns the listing.

Use [Marketplace Endpoint Reference](../references/marketplace-endpoints.md)
for endpoint lookup.

## Phase 2: Inspect Publish State

Before a mutation, check:

- current listing status
- current price or estimate when relevant
- visibility and publication state
- whether the requested final state is already true

For price changes, use the estimate endpoint first when it helps the user
understand the effect.

## Phase 3: Get Approval

Show the user:

- listing id and title
- current state and intended final state
- price, currency, fees, or estimate details when relevant
- permanence and recovery limits
- exact endpoint or action to call

Wait for explicit approval.

## Phase 4: Mutate And Verify

Call one mutation at a time: publish, unpublish, or price update. After the
mutation, re-check the listing or status endpoint that proves the final state.

If the mutation fails, use [Error Recovery Flow](error-recovery.md) and report
whether the server indicates a partial or already-completed change before
retrying.

## Final Report

Report:

- listing id/title
- action taken
- final publish/price state
- public URL or access path when available
- any remaining action needed before the listing is ready
