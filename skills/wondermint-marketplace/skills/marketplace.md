---
name: wondermint-marketplace-scope
description: Marketplace variant scope for Wondermint buying, selling, orders, seller analytics, and payouts. Use this file only in the marketplace variant, after endpoint references and scorecards have confirmed the behavior.
---

# Marketplace Scope

This file marks the marketplace variant boundary. It is intentionally separate
from the core Wondermint skill so transactional marketplace behavior does not
leak into the default package.

## Included In This Variant

Marketplace workflows may include:

- buying or purchasing items
- selling items or configuring sale terms
- order lookup and order management
- seller analytics and marketplace analytics
- payouts, balances, or earnings workflows

## Release Gate

Do not perform transactional marketplace actions from this variant until the
specific endpoint reference, approval gate, error handling, and scorecard
evidence have been added for that workflow.

Read-only marketplace status checks are safe only after their endpoint behavior
is documented in this variant.

## Approval Rules

Marketplace actions are financial or user-visible. Before any marketplace
mutation, confirm the exact item, price or terms, account, permanence, and
recovery limits with the user.
