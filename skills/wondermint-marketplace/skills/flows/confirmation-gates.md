# Confirmation Gates

Use this before any Wondermint action that is public, user-visible, durable,
account-mutating, or billing-related.

## Public Or User-Visible Gate

Use for likes, favorites, follows, views, shares, comments, replies, upvotes,
downvotes, flags, marking notifications read, and queueing content into the
frontend Agentic Dashboard infinite feed.

Before calling the endpoint, confirm:

- exact target item, creator, comment, notification, portfolio, playlist, feed,
  or asset
- exact action to take
- whether the action is visible to other users or changes the user's engagement
  or dashboard state
- whether the user has already approved this exact action in the current context

Proceed only when the target and action are explicit.

## Publishing Or Account Mutation Gate

Use for registration, uploads, item edits, item deletion or reprocess, profile
changes, password/email/API key changes, webhook changes, and
portfolio/playlist/feed create/update/delete operations.

Before calling the endpoint, confirm:

- exact target identity or object
- exact payload fields that will be sent
- permanence or recovery limits
- public audience or private visibility
- API key save location when a new key may be issued

Proceed only when every item is explicit. If any item is unclear, ask one
concise clarification question before acting.

## Billing Gate

Use for checkout, cancellation, billing portal links, payment-method updates,
and plan changes.

Before calling the endpoint, confirm:

- target plan or billing action
- monthly versus yearly billing interval
- expected billing impact
- whether the action opens Stripe or changes account state directly

Never collect card details. Stripe handles payment details.

For REST checkout, include `interval: "monthly"` or `"yearly"` in the request;
omitting it defaults to monthly.

For existing paid subscriptions, use `/subscription/upgrade` only for a higher
plan. Use `/subscription/switch-interval` for same-plan monthly/yearly changes.
That interval-switch endpoint returns a Stripe Billing Portal URL; tell the
user they must open the portal link to complete the monthly/yearly change.

## Report Back

After the action, report what changed, what did not change, and any remaining
user action. Do not include API keys, cookies, session tokens, or payment
details.
