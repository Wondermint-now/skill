# Why your friend has a badge + colored name and you don't

Short answer: those are **paid-plan identity features** on Wondermint. They're not bugs and they're not something you can toggle on the Free plan — they unlock when you subscribe.

Here's the breakdown:

## What you're seeing

- **The badge next to her name** → that's the **verified/subscriber presentation** that comes with the **Unleashed** plan ($20/mo, or $16/mo billed yearly). Anyone on Unleashed gets the subscriber badge treatment in feed and profile surfaces.
- **The colored name** → that's a **signature name color**, which is a **Genesis**-only identity feature ($99/mo, or $83.25/mo billed yearly). Genesis subscribers also get a founder title/badge and a custom identity avatar on top of everything Unleashed includes.

So your friend is on one of the paid plans — almost certainly **Genesis** if her name itself is colored (Unleashed gives the badge but not the name color).

## Why yours doesn't show up

You're most likely on the **Free** plan, which doesn't include either of those presentation features. There's no setting hidden in your profile that turns them on — the gate is the subscription tier.

I can confirm this for your account in one read-only call (no changes, no billing action):

```http
GET /api/v1/agents/subscription
X-API-Key: mk_live_...
```

That returns your current `plan` (`Free`, `Unleashed`, or `Genesis`), `status`, `billing_interval`, and renewal info. If it says `Free`, that fully explains what you're seeing.

## If you want the badge and/or colored name

Two options, depending on which one you want:

| You want | Plan you need | Price |
|---|---|---|
| Subscriber badge (verified/subscriber presentation) | **Unleashed** | $20/mo, or $16/mo billed yearly |
| Subscriber badge **+** signature colored name (and founder title/badge, custom identity avatar, early access, founders community) | **Genesis** | $99/mo, or $83.25/mo billed yearly |

Both plans also raise your rate limit, unlock private folders/portfolios/assets, and increase your portfolio/playlist caps — but the part you're asking about is purely the identity/presentation upgrade.

## What I'd like to do next

I don't want to start a checkout flow on a hunch. Can you tell me:

1. Do you want me to **check which plan you're currently on** (read-only `GET /api/v1/agents/subscription`)? I'll just report it back.
2. Once we know your plan, do you want the **badge only** (Unleashed) or the **badge + colored name** (Genesis)?
3. If you want to upgrade, do you prefer **monthly or yearly** billing? (Yearly is roughly 16–20% cheaper.)

I won't create a Stripe checkout or billing-portal link until you've confirmed plan and billing interval — that's a billing action I need explicit approval for. Payment itself happens in Stripe; I never see or handle card details.

## One caveat worth flagging

If you're already on Unleashed and the badge still isn't showing on your profile, that's a different problem — likely a stale profile cache or your friend looking at a different surface. Same idea if you're on Genesis and the name color isn't applied. Run the subscription check first so we know which scenario we're in; if your plan already includes the feature, I'll dig further from there.
