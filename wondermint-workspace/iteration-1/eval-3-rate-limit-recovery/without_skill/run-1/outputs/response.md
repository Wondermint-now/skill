# Hitting 429s on Wondermint uploads — here's the play

A 429 ("Too Many Requests") on a batch of 20 images while on the free plan almost always means you're brushing against a per-minute or per-hour upload rate limit, not a hard daily quota. The fix is usually a combination of (a) backing off and retrying correctly, and (b) pacing the batch so you don't trip the limit again.

Before I touch anything, a few things I want to confirm and a few caveats up front.

---

## What I'd want to confirm before doing anything

I don't want to guess at limits I can't actually see, so a couple of quick checks:

1. **Can you share one of the 429 response bodies / headers?** Specifically I'm looking for:
   - A `Retry-After` header (seconds or HTTP date) — this is the authoritative answer for how long to wait.
   - Headers like `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` — these tell us the actual budget.
   - The JSON body — many APIs include a human-readable `error.message` and a machine-readable `error.code` (e.g. `rate_limit_exceeded`, `quota_exceeded`, `plan_limit_exceeded`). The distinction matters: rate limit = wait and retry; plan/quota limit = upgrade or wait for the period to roll over.
2. **How are you uploading?** All 20 in a tight `Promise.all` / parallel loop, or sequentially? Parallel fan-out is the most common cause of 429s on free tiers.
3. **Did any of the 20 succeed before the 429s started?** That tells us roughly where the window cap is (e.g. "first 5 went through, then 429" → likely ~5/min).
4. **Is this a one-time batch or part of an ongoing workflow?** That changes whether the right answer is "just wait it out" vs. "upgrade the plan."

If you can't easily grab the headers, no worries — I'll lay out a conservative plan that works without them.

---

## The right move, in order

### 1. Stop hammering the endpoint right now
If your script is still running and retrying immediately, kill it. Immediate retries on a 429 typically extend the cooldown window on most APIs (and look like abuse).

### 2. Respect `Retry-After` if present
If the 429 response includes a `Retry-After` header, that is the answer. Wait *at least* that long before the next request. If it's absent, start with a 60-second wait and exponential backoff from there.

### 3. Switch from parallel to serial + paced
For a free-tier upload of 20 images, I'd default to **one image at a time with a delay between each**. Until we know the real limit, a safe starting cadence is one upload every 3–6 seconds (≈10–20/min). If that completes clean, great; if it 429s again, double the delay.

### 4. Add proper retry-with-backoff for the inevitable straggler
Even when paced, you can hit a 429 if the server's window is tighter than you guessed. Retry that single image with exponential backoff (e.g. 30s → 60s → 120s, cap at ~5 min, max 5 attempts), honoring `Retry-After` when present.

### 5. Decide if the free plan is the actual bottleneck
If pacing gets you through but only barely, and you do this regularly, the right move is to upgrade. If this is a one-off, just pace and move on.

---

## Draft script shape (pseudocode — adjust to whatever client you're using)

```javascript
// Conceptual — adjust endpoint, auth, and payload to Wondermint's actual upload API
async function uploadOne(image, attempt = 1) {
  const res = await fetch("https://api.wondermint.example/v1/uploads", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.WONDERMINT_API_KEY}`,
      "Content-Type": "application/octet-stream",
    },
    body: image.buffer,
  });

  if (res.status === 429) {
    if (attempt > 5) throw new Error(`Gave up on ${image.name} after 5 retries`);
    const retryAfter = parseInt(res.headers.get("retry-after") ?? "0", 10);
    const waitSec = retryAfter > 0 ? retryAfter : Math.min(300, 30 * 2 ** (attempt - 1));
    console.warn(`429 on ${image.name} — waiting ${waitSec}s (attempt ${attempt})`);
    await sleep(waitSec * 1000);
    return uploadOne(image, attempt + 1);
  }

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Upload failed for ${image.name}: ${res.status} ${body}`);
  }

  return res.json();
}

async function uploadBatch(images, delayMs = 4000) {
  const results = [];
  for (const img of images) {
    results.push(await uploadOne(img));
    await sleep(delayMs); // pace the batch
  }
  return results;
}
```

Key points in this shape:
- **Serial, not parallel.** No `Promise.all`.
- **Honors `Retry-After`.** Falls back to exponential backoff if it's missing.
- **Caps retries.** Won't loop forever.
- **Caps wait time.** 5 min ceiling per attempt so a stuck batch doesn't run all night.

---

## Draft message I'd send you once I had the headers

> Quick update: the 429 response includes `Retry-After: 60` and `X-RateLimit-Limit: 10/min` — so the free tier caps at 10 uploads/minute. I've adjusted the script to one upload every 7s (≈8/min, a safe margin) with exponential backoff on any straggler 429s. Re-running the batch now; ETA ~2.5 min for the remaining N images. Let me know if you'd rather upgrade the plan instead of pacing.

(That message is a placeholder — the actual numbers depend on what the headers say.)

---

## When the answer is "upgrade," not "pace"

A few signals that pacing isn't enough and you should look at a paid tier:

- The error body says `plan_limit_exceeded` or `monthly_quota_exceeded` rather than `rate_limit_exceeded`. Pacing won't help — the quota resets on a billing cycle.
- You hit the limit on **upload count per day/month**, not per-minute throughput.
- You need this batch done in under a minute and the free per-minute cap can't accommodate it.
- You expect to do this regularly, not just once.

If any of those are true, I'd check Wondermint's pricing page and see what the next tier up offers for upload throughput and monthly quota before committing.

---

## Things I'd want from you to move forward

1. A copy of the 429 response (headers + body), or at least the error message text.
2. Confirmation of how you're currently sending the batch (parallel vs. serial, what tool/script).
3. Whether this is a one-off or recurring need — affects pace-vs-upgrade.
4. Whether you want me to actually write/adjust the upload script for your stack, or just hand you the pattern.

---

## A caveat I want to be upfront about

I'm working from general knowledge of how rate-limited APIs behave — I don't have Wondermint's specific docs in front of me. The exact endpoint shape, header names, error codes, and free-tier limits above are educated guesses based on industry-standard patterns (RFC 6585 for 429, IETF draft for `RateLimit-*` headers). Before we ship a real fix, we should verify against Wondermint's actual API docs or a real 429 response from your account. If you can paste one, I can tighten everything up to match exactly.
