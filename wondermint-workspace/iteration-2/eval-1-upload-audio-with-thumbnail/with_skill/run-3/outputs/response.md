# Uploading "Drift in Amber Light" to Wondermint — what I'd do, and what I need from you first

Happy to walk you through this before I touch the API. Uploads are durable on Wondermint — once an item is `Minted`/`Listing`, it may not be deletable, and the `name` and thumbnail are locked at create time (even inside the 15-minute metadata edit window). So I want to get the plan right before any `POST /api/v1/agents/listings` call.

Here's how I'd run it.

---

## The single biggest blocker: audio needs a custom cover

Wondermint **requires audio to have its own cover image**. If I post `drift.mp3` without one, the platform falls back to a generic placeholder, which kills discovery in browse grids. The upload flow's mandatory sequence is:

1. `POST /listings` with both `file_name: "drift.mp3"` and `thumbnail_name: "cover.png"` (or similar)
2. `PUT` the audio to the returned `upload_url`
3. `PUT` the cover image to the returned `thumbnail_upload_url`
4. `POST /listings/:id/uploaded`
5. `GET /listings/:id/status` to poll to a terminal state

If I send the create call without `thumbnail_name`, there's no `thumbnail_upload_url` in the response, and audio without a cover is a bad post. So **before I do anything, I need a cover image from you**.

> Do you have a custom cover image for "Drift in Amber Light"? If yes, share the path (e.g. `/tmp/drift-cover.png`) and ideally a PNG/JPG at 512×512 or larger. If you don't have one, I can help you generate one — describe the look you want (amber dusk, abstract, gradient, photographic, etc.) and I'll draft a prompt for you to run, or wait for you to drop a file. Either way, the cover is locked at create time, so we choose it once.

I won't proceed to the create call until that's resolved.

---

## What I need confirmed from you before posting

1. **Cover image** — see above. Mandatory.
2. **Plan + visibility.** Default I'd send is **public** (`private: false`). Private visibility is paid-plan only (Unleashed or Genesis). If you want it private and you're on Free, that's an upgrade path conversation, not a posting one. Confirm public is fine.
3. **License / rights — `contract_type`.** Two options:
   - `public_domain` — anyone can use it freely.
   - `non_exclusive` — others can license it, you retain rights.
   This is independent of public/private visibility. Which do you want? My default guess for an ambient Suno track you're sharing socially would be `non_exclusive`, but tell me.
4. **Description.** I'd like one or two sentences from you (or permission to draft one and show you). Max 2000 chars. Something like: *"Ambient piece — slow generative drift, warm reverb, intended as a quiet listening track. Generated with Suno."* Approve, edit, or rewrite.
5. **Prompt (optional).** If you have the Suno prompt you used, send it — it goes in the `prompt` field and helps with discovery. Skip if you'd rather not share it.
6. **Title sanity-check.** "Drift in Amber Light" is 21 characters and contains only letters and spaces — that's well within the 50-char limit and avoids the punctuation gotcha (no commas, semicolons, or special characters that trigger `400 "Asset name contains special characters"`). Good as-is. **Reminder: the title is locked after create, even inside the 15-minute edit window.**

---

## My draft metadata (for your approval)

Based on "ambient piece generated with Suno":

**Title:** `Drift in Amber Light`

**Description (draft — replace if you want):** `Ambient piece — slow, warm, generative drift. Intended as a quiet listening track.`

**`subcategories` (3 chosen from the Audio reference list, exact strings — invented names get rejected):**
- `Ambient / Atmospheric` — primary genre
- `Calm / Peaceful` — mood
- `Spacious / Reverb-Heavy` — production / sonic style

Alternates I considered: `Nostalgic / Dreamy` (if it leans wistful), `Electronic` (if synth-heavy), `Minimal` (if very sparse). Tell me if any of those fit better than my picks.

**`tags` (free-form, separate from subcategories):**
`ambient`, `drift`, `atmospheric`, `suno`, `generative`, `warm`, `reverb`, `chillout`

**`model`:** `Suno`

**`contract_type`:** *needs your call* — `public_domain` or `non_exclusive`

**`private`:** `false` (public) unless you say otherwise

**Cover image:** *needs your file or your go-ahead to draft one*

---

## The exact API calls I'd send, in order

I'm showing these so you can see the full plan before I run anything. Nothing here gets fired until you approve.

### 1. Create the listing

```http
POST https://api.wondermint.now/api/v1/agents/listings
X-API-Key: $WONDERMINT_API_KEY
Content-Type: application/json

{
  "name": "Drift in Amber Light",
  "description": "Ambient piece — slow, warm, generative drift. Intended as a quiet listening track.",
  "subcategories": ["Ambient / Atmospheric", "Calm / Peaceful", "Spacious / Reverb-Heavy"],
  "file_name": "drift.mp3",
  "thumbnail_name": "cover.png",
  "contract_type": "non_exclusive",
  "tags": ["ambient", "drift", "atmospheric", "suno", "generative", "warm", "reverb", "chillout"],
  "model": "Suno",
  "prompt": "<your Suno prompt here, or omit>"
}
```

Expected `201` response:
```json
{
  "listing_id": "...",
  "upload_url": "https://....r2.cloudflarestorage.com/...",
  "thumbnail_upload_url": "https://....r2.cloudflarestorage.com/..."
}
```

### 2. PUT the audio file

```http
PUT {upload_url}
Content-Type: audio/mpeg

<binary contents of /tmp/drift.mp3>
```

Important: I send **only** `Content-Type` and the body. I do **not** echo `x-amz-checksum-*` headers — those are baked into the presigned URL, and adding them as request headers causes `403 SignatureDoesNotMatch`.

### 3. PUT the cover image

```http
PUT {thumbnail_upload_url}
Content-Type: image/png

<binary contents of cover image>
```

This **must** happen before the confirm call. Confirming before the thumbnail is in place can fail the post.

### 4. Confirm the upload

```http
POST https://api.wondermint.now/api/v1/agents/listings/{listing_id}/uploaded
X-API-Key: $WONDERMINT_API_KEY
```

### 5. Poll status (once, then space out further checks)

```http
GET https://api.wondermint.now/api/v1/agents/listings/{listing_id}/status
X-API-Key: $WONDERMINT_API_KEY
```

Success terminals: `Minted`, `Listing`, or `Pending Approval` (if your account is under manual review). Failure terminals: `Processing Failed`, `Denied By Admin`. I won't tight-loop — one check after confirm, then wait.

---

## Failure plan (pre-approving cleanup now saves a round-trip later)

If create succeeds (we have a `listing_id`) but a later step fails — the audio PUT, the cover PUT, or `/uploaded` — we'll have an **orphan draft**. Standard practice is to clean it up with `DELETE /api/v1/agents/listings/{listing_id}` so it doesn't sit on your account.

**Are you pre-approving me to delete an orphan draft if a mid-flow step fails?** If yes, I'll handle it inline and just report what happened. If no, I'll stop, surface the error, and wait for your call.

Other failure cases I'll handle:
- `409 REVIEW_ACK_REQUIRED` on the first create — your account is flagged for manual review. I'll stop, tell you, and re-ask before resending with `acknowledge_review: true`.
- `429 RATE_LIMITED` — I'll honor `Retry-After`, not retry blindly, and mention the plan limits if you're on Free (30 rpm; Unleashed 120; Genesis 600). I won't create checkout without explicit approval.
- `Processing Failed` with `failure_reason: duplicate_content` / `nsfw_detected` / `virus_detected` — terminal for these bytes. I'll surface and stop.

---

## A note on your API key

You said `WONDERMINT_API_KEY` is in your env — good. I'll only send it as the `X-API-Key` header to `https://api.wondermint.now/api/v1/*` endpoints. It does not go to the R2 presigned URLs (the upload/thumbnail PUTs), it does not go to any other domain, and it does not get logged or echoed back to you in any report.

---

## What I need from you to proceed (checklist)

1. **Cover image** — path to a file, or "go ahead and help me make one."
2. **`contract_type`** — `public_domain` or `non_exclusive`?
3. **Visibility** — public (default) confirmed? Or did you want private (paid-plan only)?
4. **Description** — approve my draft, edit it, or send your own.
5. **Subcategories + tags** — approve my picks, or swap any.
6. **Prompt** — share the Suno prompt for the `prompt` field, or skip.
7. **Orphan-draft cleanup pre-approval** — yes/no on auto-deleting a stranded draft if a mid-flow step fails.

Reply with the answers (cover image is the hard blocker — the rest I can default if you just say "use your draft"), and I'll show you the final consolidated payload one more time before sending the create call.

After it's live I'll report:
- Public URL (`https://wondermint.now/explore/{slug}`)
- Final status
- The **15-minute metadata edit deadline as a concrete clock time** — inside that window I can `PATCH` `description`, `tags`, `category_id`, and `private`, but **not** `name` or the thumbnail.
