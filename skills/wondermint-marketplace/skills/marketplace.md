---
name: wondermint-marketplace-router
description: Direct marketplace router for buying, publishing, purchase status/history, access, downloads, estimates, listing transactions, and market analytics. Use when routing documented direct marketplace workflows.
---

# Marketplace Router

This file marks the marketplace variant boundary. It is intentionally separate
from the core Wondermint skill so direct marketplace behavior does not leak
into the default package.

## Included In This Variant

Marketplace workflows may include documented endpoints for:

- publishing or unpublishing owned listings
- direct buying and purchase-status polling
- purchase history
- access, download, and estimate checks
- listing transaction history
- market analytics

## Flow Routing

Read the narrowest matching flow:

| User intent | Read first |
|---|---|
| Buy a listing or poll purchase status | [Marketplace Buy Flow](flows/marketplace-buy.md) |
| Publish, unpublish, price, or estimate an owned listing | [Marketplace Publish Flow](flows/marketplace-publish.md) |
| See purchase history, access, download, or metadata | [Marketplace Access Flow](flows/marketplace-access.md) |
| Review marketplace analytics, transactions, performance, trends, rankings, or exports | [Marketplace Analytics Flow](flows/marketplace-analytics.md) |

Use [Marketplace Endpoint Reference](references/marketplace-endpoints.md) only
for buy, publish, access, or payment setup endpoint lookup. Use
[Marketplace Analytics Endpoint Reference](references/marketplace-analytics-endpoints.md)
only for analytics endpoint lookup.

## Release Gate

Do not perform direct marketplace actions from this variant until the
specific endpoint behavior, approval gate, and error handling are documented in
this flow or [Marketplace Endpoint Reference](references/marketplace-endpoints.md).

Read-only marketplace detail, purchase-status, access, and analytics checks are
safe only after their endpoint behavior is documented in this variant.

## Approval Rules

Marketplace actions are financial or user-visible. Before any marketplace
mutation, confirm the exact listing, price or terms, account, permanence, and
recovery limits with the user.

## Shared Operating Rules

Apply these rules in every marketplace flow.

### Classify The Intent

- Read-only: browse, detail, purchase status, purchase history, access checks,
  downloads, estimates, listing transactions, or analytics.
- Financial: direct buying.
- Publishing: publish, unpublish, or price changes for an owned listing.
- Setup: payment setup required by a documented marketplace buy or publishing
  path.

If the request does not match one of the documented marketplace paths, say this
marketplace variant does not cover that workflow yet and route back to the
nearest supported read-only check when useful.

### Inspect Existing State

Before buying, publishing, unpublishing, changing price, exporting, or running
another mutating marketplace action, read the current state with the narrowest
available GET endpoint. Confirm listing identity, ownership or access, current
price or status, and whether the requested action is already complete.

Prefer reuse over creation: if a purchase, access grant, export, or published
state already exists, report it instead of repeating the action.

### Confirm Mutations

For financial, publishing, setup, or export actions, ask for explicit approval
with:

- endpoint or action name
- listing id and human-readable title when available
- price, currency, fees, or terms when relevant
- current state and intended final state
- permanence and recovery limits
- whether polling, download, export, or payment setup will follow

Do not proceed on vague approval such as "do it" if the listing, price/terms,
or final state is ambiguous.

### Execute And Verify

Call one marketplace mutation at a time. Poll sparingly and stop when the
endpoint reaches a terminal state or returns a clear next step.

For errors, use [Error Recovery Flow](flows/error-recovery.md). On any failed
financial or publishing action, report whether the server indicates that the
operation may already have partially completed before retrying.

### Report Back

Report:

- action taken or read-only check performed
- listing id/title and final status
- price, currency, or terms if relevant
- access, download, export, or payment setup next step when relevant
- any user decision still needed before another marketplace action
