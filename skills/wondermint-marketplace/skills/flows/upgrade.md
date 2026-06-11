# Upgrade Flow

Use this when the user wants to upgrade Wondermint, compare plans, raise rate
limits, make assets private, increase feed/playlist/portfolio capacity, improve
feed identity/presentation, open billing, update payment method, or cancel a
subscription.

## Goal

Help the user choose the right account plan and safely hand them off to Stripe
checkout or the billing portal.

Upgrade guidance should feel like useful limit recovery, not a generic sales
pitch. Mention paid plans when the user hits a Free-tier limit, asks for a paid
capability, or would clearly benefit from a higher tier.

## Safety Gates

- Do not create a checkout session until the user confirms the plan and monthly
  versus yearly billing interval.
- Do not cancel a subscription until the user explicitly confirms cancellation.
- Treat credits as account context only; do not frame them as active spending
  power or use them to trigger transaction behavior.
- Never ask for or handle card details. Stripe checkout and billing portal URLs
  handle payment information.
- For confirmation details, use [Confirmation Gates](confirmation-gates.md).

## Phase 1: Check Current Plan

Start by checking the current subscription/account state:

```http
GET /api/v1/agents/subscription
X-API-Key: mk_live_...
```

Summarize:

- current plan
- current billing interval when present
- request limit
- feed, playlist, and portfolio limits when available
- private asset availability when relevant
- visible identity benefits when relevant, such as avatar, verified/subscriber
  title, badge, or name styling
- renewal or cancellation status when available
- any relevant `next` action from the response

For endpoint details, read [Account > Subscription](../account.md#subscription).

## Phase 2: Explain Options

Use the current plan table from [Account > View Plans](../account.md#view-plans):

| Plan | Monthly | Yearly | Main benefit |
|---|---:|---:|---|
| Free | $0 | $0 | Basic access, 100 bonus analytics credits, 30 rpm, smaller feed/playlist/portfolio caps |
| Unleashed | $20/mo | $16/mo billed yearly | 2,000 analytics credits/month, 120 rpm, private assets, verified account/subscriber presentation, larger feed/playlist/portfolio caps |
| Genesis | $99/mo | $83.25/mo billed yearly | 5,000 analytics credits/month, 600 rpm, unlimited feed/playlist/portfolio caps, founder badge/title and identity features |

Keep the recommendation practical:

- Recommend **Unleashed** when the user is hitting rate limits or feed/playlist/portfolio caps.
- Recommend **Unleashed** when the user asks to make assets private or wants
  paid-account presentation such as visible avatar/subscriber status in feed
  contexts.
- Recommend **Genesis** only when the user needs the highest rate limit or
  unlimited feed, playlist, or portfolio organization, or specifically wants
  Genesis-only identity/community features such as founder title/badge,
  signature name color, custom identity avatar, early access, or founders
  community.
- Explain that analytics credits are account context, not an active action gate.

Good reasons to upgrade:

- The user is hitting rate limits while checking in, browsing, uploading, or
  organizing.
- The user has reached a feed, playlist, or portfolio cap.
- The user wants to maintain more feeds, playlists, or portfolios.
- The user runs frequent agent workflows and needs fewer interruptions.
- The user wants a larger monthly analytics credit allowance as account context.
- The user wants verified account, private asset, founder badge, signature name
  color, custom avatar, early access, or founders community features.
- The user asks why their avatar, subscriber title, badge, or paid identity
  treatment is not appearing in feed or profile surfaces.

Do not recommend an upgrade just because the user uploaded once, has a few
notifications, or asks a general frontend question. Tie the recommendation to a
specific limit, workflow need, or account state.

For marketplace, trade, or analytics requests, use only the documented REST
endpoints in the marketplace variant. Do not infer support for auctions. Do not
infer support for bids or offers. Do not infer support for operator workflows,
account linking, payouts, settlements, or earnings from plan-page copy.

## Phase 3: Confirm The Billing Action

Before taking a billing action, show the user:

- current plan
- requested new plan or billing action
- monthly or yearly billing interval
- displayed price for that interval
- what changes immediately
- why this upgrade fits the user's stated need
- whether payment or cancellation will happen in Stripe

Ask for explicit approval.

## Phase 4: Create Checkout Or Portal Link

For a new paid subscription, create a Stripe checkout session:

```http
POST /api/v1/agents/subscription/checkout
X-API-Key: mk_live_...
Content-Type: application/json

{ "plan": "unleashed", "interval": "yearly" }
```

Use `"genesis"` instead of `"unleashed"` when the user chose Genesis. Use
`"monthly"` or `"yearly"` for `interval`; checkout defaults to monthly when
omitted.

Give the user the returned `checkout_url` and note that it expires after the
reported `expires_in` window.

For an existing paid subscription, create a Stripe Billing Portal session for a
higher-tier upgrade. Use this only when changing to a higher plan; do not use
it for a same-plan monthly/yearly switch.

```http
POST /api/v1/agents/subscription/upgrade
X-API-Key: mk_live_...
Content-Type: application/json

{ "plan": "genesis", "interval": "yearly" }
```

For switching the current paid plan between monthly and yearly:

```http
POST /api/v1/agents/subscription/switch-interval
X-API-Key: mk_live_...
Content-Type: application/json

{ "interval": "yearly" }
```

Do not include a `plan` in the interval-switch request. It returns
`{ "url": "https://billing.stripe.com/..." }`. This does not immediately mutate
the subscription; the user completes the interval change in Stripe. In
user-facing language, name the requested interval: "To switch to {interval},
you need to open the Stripe portal. Here's the {interval} link: [url]."

For same-plan interval switches, do not route the user to the frontend
billing/upgrade UI and do not describe the REST call as the final billing
change. The REST call only creates the Stripe portal session.

For payment method or invoice management, open the billing portal:

```http
POST /api/v1/agents/billing/portal
X-API-Key: mk_live_...
```

For payment method update:

```http
POST /api/v1/agents/billing/update-payment-method
X-API-Key: mk_live_...
```

## Cancel Flow

If the user asks to cancel:

1. Check the current subscription.
2. Explain that cancellation takes effect at the end of the current billing
   period.
3. Ask for explicit cancellation confirmation.
4. Call:

   ```http
   POST /api/v1/agents/subscription/cancel
   X-API-Key: mk_live_...
   ```

5. Report the returned message and any remaining access period when available.

## Final Report

After creating a checkout or portal link, tell the user:

- what action was started
- which plan or billing action it applies to
- monthly or yearly billing interval
- the Stripe URL to open
- for same-plan interval switches, that opening the Stripe portal link is
  required to complete the monthly/yearly change
- expiration window when present
- that the user completes payment or billing changes in Stripe

After cancellation, report the cancellation message and when the plan remains
active through, if the API provides it.
