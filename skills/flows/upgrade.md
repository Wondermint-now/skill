# Upgrade Flow

Use this when the user wants to upgrade Wondermint, compare plans, raise rate
limits, increase folder capacity, open billing, update payment method, or cancel
a subscription.

## Goal

Help the user choose the right account plan and safely hand them off to Stripe
checkout or the billing portal.

## Safety Gates

- Do not create a checkout session until the user confirms the plan.
- Do not cancel a subscription until the user explicitly confirms cancellation.
- Treat credits as account context only; do not frame them as active spending
  power or use them to trigger transaction behavior.
- Never ask for or handle card details. Stripe checkout and billing portal URLs
  handle payment information.

## Phase 1: Check Current Plan

Start by checking the current subscription/account state:

```http
GET /api/v1/agents/subscription
X-API-Key: mk_live_...
```

Summarize:

- current plan
- request limit
- folder and portfolio limits when available
- renewal or cancellation status when available
- any relevant `next` action from the response

For endpoint details, read [Account > Subscription](../account.md#subscription).

## Phase 2: Explain Options

Use the current plan table from [Account > Plans](../account.md#plans):

| Plan | Price/mo | Main benefit |
|---|---:|---|
| Free | $0 | Basic access, lower rate limit, smaller folder caps |
| Unleashed | $20 | Higher rate limit and larger folder caps |
| Genesis | $99 | Highest rate limit and unlimited folder caps |

Keep the recommendation practical:

- Recommend **Unleashed** when the user is hitting rate limits or folder caps.
- Recommend **Genesis** only when the user needs the highest rate limit or
  unlimited folder organization.
- Explain that credits are account context, not an active action
  gate.

## Phase 3: Confirm The Billing Action

Before taking a billing action, show the user:

- current plan
- requested new plan or billing action
- monthly price
- what changes immediately
- whether payment or cancellation will happen in Stripe

Ask for explicit approval.

## Phase 4: Create Checkout Or Portal Link

For an upgrade, create a Stripe checkout session:

```http
POST /api/v1/agents/subscription/checkout
X-API-Key: mk_live_...
Content-Type: application/json

{ "plan": "unleashed" }
```

Use `"genesis"` instead of `"unleashed"` when the user chose Genesis.

Give the user the returned `checkout_url` and note that it expires after the
reported `expires_in` window.

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
- the Stripe URL to open
- expiration window when present
- that the user completes payment or billing changes in Stripe

After cancellation, report the cancellation message and when the plan remains
active through, if the API provides it.
