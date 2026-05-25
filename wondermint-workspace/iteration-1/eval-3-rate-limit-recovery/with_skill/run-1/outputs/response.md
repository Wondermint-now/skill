# Response to user: 429 errors on a 20-image batch upload (Free plan)

## What's actually happening

A `429` from Wondermint means `RATE_LIMITED`. On the Free plan you have **30 requests per minute** (plan-level, 60-second sliding window). A 20-image upload batch blows through that quickly because each listing costs roughly 2–4 Wondermint API calls (create + confirm + at least one status check), even before any retries or failure-path cleanup. There are also two other limiting layers that can bite independently of plan: per-endpoint throttles (e.g. comments 5/min, trending 20/min) and a global 250 req / 60s burst limit.

Two routes to fix this. They're not mutually exclusive.

1. Pace the uploads to fit inside 30 rpm.
2. Upgrade — **Unleashed** raises the plan-level limit to 120 rpm, **Genesis** to 600 rpm.

Endpoint-specific throttles aren't bypassed by upgrading, but a generic upload-batch 429 on Free is almost always the plan-level cap, which an upgrade does raise.

## What I recommend right now (no API calls yet)

Before doing anything else I'd like to confirm a couple of things, then I'll pick the lightest-touch recovery.

### Step 0: stop firing requests

If a worker is still looping, pause it. Repeating the same calls before the reset window just extends the throttle and risks stranding half-created drafts.

### Step 1: let the current window reset, then check the budget

I'd run a single read to see exactly where you stand:

```http
GET /api/v1/agents/rate-limit
X-API-Key: mk_live_...
```

That returns `requests_per_minute`, `current_usage`, `remaining`, and `resets_at`. If a `Retry-After` header came back on the 429, I'll honor that first.

### Step 2: figure out where the batch actually got to

Before creating any new listings, I want to know which of the 20 made it and in what state, so we don't pile orphan drafts on top of each other:

```http
GET /api/v1/agents/listings?status=uploading
GET /api/v1/agents/listings?status=processing
GET /api/v1/agents/listings?status=failed
GET /api/v1/agents/listings?status=minted
```

(Or whichever subset you want — I can also check `pending_approval` and `listed`.) Anything that's a stuck draft from the failed batch can be cleaned up with `DELETE /api/v1/agents/listings/:id` **only after you approve** — published items aren't deletable so we won't try.

I will **not** start replacement uploads while prior listings from the batch are still unresolved.

### Step 3: pick a path — pace or upgrade

**Path A — stay on Free, pace the work.** For 20 images this is feasible but slow. Concretely:

- One active upload at a time. Create → PUT file to the presigned URL (the PUT does **not** count against your Wondermint API budget; only the API calls do) → `POST /listings/:id/uploaded` → one status check → next.
- Each image costs ~2–4 Wondermint API calls. At 30 rpm with check-ins and a status read, plan ~6–8 uploads per minute, max. Realistically the full batch lands across ~3–5 minutes once we're disciplined about polling.
- Poll sparingly: one status check after confirm, then wait — don't tight-loop.
- Re-check `GET /api/v1/agents/rate-limit` before each small sub-batch; if `remaining` is too low for create + confirm + status, wait for `resets_at` instead of starting a create that might strand a draft.
- The presigned upload URL is valid for 2 hours, so there's no rush between create and PUT.

**Path B — upgrade.** If 20-image batches are routine for you and the pacing above is going to be annoying, Unleashed at 120 rpm comfortably absorbs a 20-batch in a single window. Genesis at 600 rpm is overkill unless you're doing very large batches or high-volume discovery.

| Plan | Limit | Price | Fits this batch comfortably? |
|---|---|---|---|
| Free | 30 rpm | $0 | Possible with pacing, ~3–5 min |
| Unleashed | 120 rpm | $20/mo (or $16/mo billed yearly) | Yes, in a single window |
| Genesis | 600 rpm | $99/mo (or $83.25/mo billed yearly) | Trivially |

I will **not** create a Stripe checkout link without your explicit approval. If you want Unleashed I'll come back with the exact `POST /api/v1/agents/subscription/checkout` payload and the monthly/yearly choice before calling it.

## What I'd like you to confirm

1. **Pause confirmed?** Is there still an automated loop firing uploads? If so, stop it before I do anything else.
2. **Pace or upgrade?** Free + pacing (slow but free), or upgrade to Unleashed (1-click checkout link via Stripe, ~$20/mo)?
3. **Orphan-draft cleanup pre-approval.** If we resume on Free and a create succeeds but a later step fails on one of the 20, do I have your approval to `DELETE` that orphan draft? (I'll skip anything already published — those aren't deletable.)
4. **Any of the 20 images possible duplicates of items you've already posted?** Wondermint dedups on content hash, so identical bytes will fail with `duplicate_content` and won't go through no matter how we pace.
5. **Visibility:** all 20 public, right? Private uploads require a paid plan, so I'll assume `private: false` unless you say otherwise.

## Draft messages I'd send next, depending on your answer

**If you pick Path A (pace on Free):**

> Pausing the batch. I'll check your current rate-limit budget, list which of the 20 already made it through and in what state, and resume one-at-a-time with status checks between uploads. With Free's 30 rpm this'll take roughly 3–5 minutes once we resume. I'll surface any orphan drafts before cleanup. Ready to proceed?

**If you pick Path B (upgrade to Unleashed):**

> Confirming before I create the Stripe checkout link:
> - Plan: Unleashed ($20/mo monthly, or $16/mo billed yearly — which do you want?)
> - Effect: raises your per-minute limit from 30 → 120 rpm, unlocks private uploads and higher folder caps
> - Payment happens in Stripe — I won't see or handle card details
> - I'll send you the `checkout_url` and you complete it in your browser
>
> Approve and tell me monthly or yearly, and I'll generate the link.

## Draft API calls (held until you approve)

Read-only, safe to run as soon as you confirm a path:

```http
GET /api/v1/agents/rate-limit
X-API-Key: mk_live_...
```

```http
GET /api/v1/agents/listings?status=uploading
GET /api/v1/agents/listings?status=processing
GET /api/v1/agents/listings?status=failed
X-API-Key: mk_live_...
```

Mutation, **only after explicit approval per item or per batch**:

```http
DELETE /api/v1/agents/listings/{listing_id}
X-API-Key: mk_live_...
```

Checkout, **only if you pick Path B and confirm the interval**:

```http
POST /api/v1/agents/subscription/checkout
X-API-Key: mk_live_...
Content-Type: application/json

{ "plan": "unleashed", "interval": "monthly" }
```

## Summary

You hit Free's 30 rpm limit because a 20-image batch is ~40–80 API calls back-to-back. Either pace one-at-a-time on Free (3–5 minutes, free) or upgrade to Unleashed for 120 rpm (~$20/mo). Before resuming, I want to wait for the reset window, check `GET /api/v1/agents/rate-limit`, and see which of the 20 already landed so we don't pile drafts on top of drafts. Tell me which path and I'll go.
