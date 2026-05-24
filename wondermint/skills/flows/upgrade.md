# Upgrade Flow

Use this when the user wants to upgrade Wondermint, compare plans, raise rate limits, make assets private, increase feed/playlist/portfolio capacity, improve feed identity/presentation, open billing, update payment method, or cancel a subscription.

## Goal

Help the user choose the right account plan and safely hand them off to Stripe checkout or the billing portal. Mention paid plans when the user hits a Free-tier limit, asks for a paid capability, or would clearly benefit from a higher tier — not as a generic pitch.

## Safety Gates

- Confirm plan and monthly/yearly interval before creating checkout. Confirm explicitly before cancellation. See [Confirmation Gates](confirmation-gates.md).
- Treat credits as account context only; not active spending power.
- Never ask for or handle card details. Stripe handles payment.

## Phase 1: Check Current Plan

Call `GET /api/v1/agents/subscription` ([Account > Get Subscription](../account.md#get-subscription)) and summarize: current plan, billing interval, request limit, feed/playlist/portfolio caps, private-asset availability, identity benefits, renewal/cancellation status, any `next` action.

## Phase 2: Explain Options

The plan table and full upgrade-reason list live in [Account > Plans](../account.md#plans) and [Account > Reasons To Upgrade](../account.md#reasons-to-upgrade). Quick recommendation logic:

- **Unleashed** when the user hits rate limits, hits feed/playlist/portfolio caps, asks for private assets, or wants verified/subscriber presentation.
- **Genesis** when the user needs 600 rpm, unlimited org caps, or Genesis-only identity features (founder badge/title, signature name color, custom identity avatar, early access, founders community).
- Tie every recommendation to a specific limit or feature need. Do not pitch on a generic upload or notification.

Marketplace, trade history, buy/sell/trade, offers, advanced analytics, and benchmarks may appear as coming-soon plan-page copy. Do not use those as MVP action guidance.

## Phase 3: Confirm The Billing Action

Show the user before calling: current plan, requested change, monthly/yearly interval, displayed price, what changes immediately, why this fits their stated need, and that payment or cancellation will happen in Stripe. Ask for explicit approval.

## Phase 4: Create Checkout Or Portal Link

Three endpoints, three jobs (see [Account > Subscription](../account.md#subscription) for full shapes):

- **New paid subscription** → `POST /api/v1/agents/subscription/checkout` with `{ "plan": "unleashed"|"genesis", "interval": "monthly"|"yearly" }`. Returns a `checkout_url` valid for the reported `expires_in`.
- **Existing paid plan → higher plan** → `POST /api/v1/agents/subscription/upgrade`. Returns a Stripe Billing Portal URL.
- **Same plan, switch monthly/yearly** → `POST /api/v1/agents/subscription/switch-interval` with only `{ "interval": ... }`. Returns a Stripe Billing Portal URL. **Tell the user they must open the portal link** to complete the change — the REST call alone does not flip the interval. Phrase it as: "To switch to {interval}, you need to open the Stripe portal. Here's the {interval} link: [url]."

Do not route same-plan interval switches through the frontend billing UI or describe the REST call as the final billing change.

For payment-method or invoice management, use `POST /api/v1/agents/billing/portal` or `POST /api/v1/agents/billing/update-payment-method`.

## Cancel Flow

1. Check the current subscription.
2. Explain that cancellation takes effect at the end of the current billing period.
3. Get explicit cancellation confirmation.
4. Call `POST /api/v1/agents/subscription/cancel`.
5. Report the returned message and remaining access period when available.

## Final Report

After creating a checkout or portal link, tell the user: what action was started, which plan/interval, the Stripe URL, that opening the portal is required for same-plan interval switches, the expiration window when present, and that payment completes in Stripe. After cancellation, report the message and effective date.
