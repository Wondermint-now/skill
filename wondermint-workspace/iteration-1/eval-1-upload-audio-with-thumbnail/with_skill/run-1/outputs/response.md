# Uploading "Drift in Amber Light" to Wondermint

Happy to walk you through this before anything goes live. A few things up front so you know how I'm thinking about it:

- This is a **publishing / account-mutation** action. Once an audio listing reaches `Minted` / `Listing`, it's effectively permanent — `DELETE` can return 404 on published items, and only `description`, `tags`, `category_id`, and `private` are editable inside a 15-minute window after create. The `name` and the thumbnail are locked from the moment I call `POST /api/v1/agents/listings`. So I won't post until you've signed off on the exact payload.
- **Audio always requires a custom cover image.** Wondermint uses the cover as the album-art tile in browse/trending/portfolio grids. Without one, audio gets a generic placeholder that hurts discovery. This is the single biggest thing I need from you before I can do anything useful.
- I will not send your API key anywhere except `X-API-Key` headers to `https://api.wondermint.now/api/v1/*`. I'll read `WONDERMINT_API_KEY` from your env at call time and never echo it back in chat, logs, or files.

---

## What I need from you first

### 1. A cover image (required — blocking)

Audio uploads need their own visual. Could you either:

- point me at a local image file (PNG, JPG, or WebP — `cover.png`-style filename, ideally 512×512 or larger), **or**
- ask me to draft a cover concept and we generate one before posting.

If you don't have one and want to skip generating, I'd rather pause than post audio with a placeholder.

### 2. Description

I don't want to invent narrative about a piece I haven't heard. A 1–3 sentence description from you would be ideal. If you'd prefer, I can draft something based on a short brief (mood, intended use, what you were going for with the Suno prompt) and you approve before I send it. Max 2000 chars.

### 3. License / rights (`contract_type`)

Two options, and they're independent of public/private visibility:

- `public_domain` — anyone can use it freely.
- `non_exclusive` — you keep rights; others license non-exclusively.

Which do you want? I won't guess.

### 4. Visibility (`private`)

Public by default. Private requires a paid plan (Unleashed or Genesis). Do you want this public, or are you on a paid plan and want it private?

### 5. Optional but useful

- The Suno prompt text (goes into `prompt` — useful provenance, optional).
- `model`: I'd send `"Suno"` unless you want a different label.

---

## Draft posting plan (for your review)

Here's what I'd send once the blockers above are resolved. **Bracketed items still need your input.**

```json
POST /api/v1/agents/listings
X-API-Key: <from WONDERMINT_API_KEY env>
Content-Type: application/json

{
  "name": "Drift in Amber Light",
  "description": "[your 1–3 sentence description, or my draft after you approve it]",
  "subcategories": ["Ambient / Atmospheric", "Calm / Peaceful", "Spacious / Reverb-Heavy"],
  "file_name": "drift.mp3",
  "thumbnail_name": "cover.png",   // extension will match the cover you provide
  "contract_type": "[public_domain | non_exclusive]",
  "tags": ["ambient", "drift", "amber", "atmospheric", "suno", "generative"],
  "model": "Suno",
  "prompt": "[optional — your Suno prompt if you want it stored]"
}
```

### Why those subcategories

From the audio category reference (only these precreated names are accepted — I can't invent any):

- **Ambient / Atmospheric** — primary genre for an ambient piece.
- **Calm / Peaceful** — mood, matches "drift" and "amber light" framing.
- **Spacious / Reverb-Heavy** — production characteristic typical of ambient.

If the track is actually darker, more melancholic, or more textural than I'm guessing, tell me and I'll swap. Other candidates depending on the vibe: `Nostalgic / Dreamy`, `Melancholic / Sad`, `Dark / Ominous`, `Minimal`, `Lo-fi`, `Textured`, `Electronic`, `Experimental / Noise`. I want to pick from what the piece actually sounds like, not from the title alone.

### Tags

Free-form, separate from subcategories, max 10. Draft above is conservative; happy to add concrete sonic descriptors (e.g. `drone`, `pads`, `field-recording`, `slow`) if they fit. Tell me what's accurate.

---

## The full sequence I'd run (no calls yet — this is the plan)

Once you approve the payload and provide the cover:

1. **Create listing** — `POST /api/v1/agents/listings` with the payload above. Returns `listing_id`, `upload_url` (for the mp3), and `thumbnail_upload_url` (for the cover). Both presigned URLs are good for 2 hours.
2. **PUT the audio** — `PUT {upload_url}` with the bytes of `/tmp/drift.mp3` and `Content-Type: audio/mpeg`. Only that header plus the body — no checksum headers (the presigned URL has them baked in; echoing them back causes `403 SignatureDoesNotMatch`).
3. **PUT the cover** — `PUT {thumbnail_upload_url}` with the cover bytes and the matching image `Content-Type`. Must happen before step 4 or `/uploaded` can fail.
4. **Confirm** — `POST /api/v1/agents/listings/{listing_id}/uploaded`.
5. **Poll status** — `GET /api/v1/agents/listings/{listing_id}/status` once after confirm, then space out further checks. Status walks from `Processing` to `Minted` / `Listing`. Other possible terminals: `Pending Approval` (if your account is under manual review — I'll handle that with a separate `acknowledge_review` confirmation if it comes up), `Processing Failed` (with `failure_reason` like `duplicate_content`, `nsfw_detected`, `virus_detected`, or `processing_timeout`), `Denied By Admin`.

### Pre-approval I'd like to bundle in now (one yes/no)

If create succeeds but the audio PUT, the cover PUT, or `/uploaded` fails partway, the listing sits as an orphan draft. **May I pre-approve deleting the orphan draft via `DELETE /api/v1/agents/listings/{listing_id}` in that specific failure case?** It only applies before the item is published — published items can't be deleted anyway. If you'd rather I stop and ask in the moment, that's fine too.

### If we hit a 429

Free plan is 30 rpm. I'd honor `Retry-After`, not start a replacement upload while a prior draft is unresolved, and surface the limit to you. Upgrading raises the plan-level cap (Unleashed 120 rpm, Genesis 600 rpm) — I won't open any billing or checkout link without explicit approval.

---

## After it's live (so you know what to expect)

As soon as status hits `Minted` or `Listing` I'll report:

- Public URL — `https://wondermint.now/explore/{slug}`.
- What got posted — name, description, subcategories, tags, cover source.
- **The 15-minute edit deadline as a concrete time.** Inside that window, `PATCH /api/v1/agents/listings/{listing_id}` can change `description`, `tags`, `category_id`, and `private`. After it closes, all four lock except possibly `private`.
- **What's already locked from the moment of create:** `name` ("Drift in Amber Light") and the thumbnail. No rename, no cover swap. That's why I'm being careful before posting.

---

## So — to unblock, I need:

1. The **cover image** (path to a local file, or a green light to draft a concept first).
2. A **description** (yours, or approval for me to draft one).
3. **`contract_type`**: `public_domain` or `non_exclusive`.
4. **Visibility**: public, or private (and confirmation you're on a paid plan).
5. **Subcategory check**: does ambient / calm / spacious match the actual track, or should I adjust?
6. **Orphan-draft cleanup pre-approval**: ok to auto-delete a stranded draft if a mid-upload step fails?
7. Optional: Suno prompt text, any tag adjustments.

Once I have those, I'll show you the final exact JSON one more time, wait for an explicit "go," and then run the create → PUT audio → PUT cover → confirm → poll sequence.
