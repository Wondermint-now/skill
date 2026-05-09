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

If the user chooses yearly, do not create a REST checkout link unless REST
interval support is confirmed. Route them to the frontend billing/upgrade UI to
select yearly there.

## Report Back

After the action, report what changed, what did not change, and any remaining
user action. Do not include API keys, cookies, session tokens, or payment
details.
