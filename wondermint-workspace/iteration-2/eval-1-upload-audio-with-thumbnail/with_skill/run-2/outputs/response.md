# Uploading "Drift in Amber Light" to Wondermint

Happy to walk you through this before I touch the API. Wondermint uploads are durable — once `POST /api/v1/agents/listings` completes and the file processes into `Minted`/`Listing` state, the item is effectively permanent (the `name` and thumbnail are locked from the moment of create, and only `description`/`tags`/`category_id`/`private` can be patched within a 15-minute window). So I want to get the plan right with you first.

Here's exactly what I'd do, in order, once you green-light it.

---

## The shape of the upload

**Mandatory order for audio** (this matters — confirming before the cover is in place can fail):

1. `POST /api/v1/agents/listings` with `thumbnail_name` set — returns `listing_id`, `upload_url`, and `thumbnail_upload_url`
2. `PUT {upload_url}` with the MP3 bytes (Content-Type: `audio/mpeg`)
3. `PUT {thumbnail_upload_url}` with the cover image bytes
4. `POST /api/v1/agents/listings/{listing_id}/uploaded` to confirm
5. `GET /api/v1/agents/listings/{listing_id}/status` once after confirm, then space out further checks until it lands on `Minted`, `Listing`, or `Pending Approval`

All Wondermint API calls go to `https://api.wondermint.now` with `X-API-Key: $WONDERMINT_API_KEY`. The PUTs go to the presigned R2 URLs returned by step 1 — those carry `Content-Type` and the file body only (no echoed `x-amz-checksum-*` headers; the signed URL already bakes them in).

---

## What I need from you before I make any call

There are a few decisions only you can make, plus one piece of input that's a hard blocker:

### 1. Cover art — this is a hard blocker

Audio items **always require a custom cover thumbnail**. Without one, Wondermint falls back to a generic placeholder that hurts discovery in browse grids. I don't see a cover file alongside `/tmp/drift.mp3`.

> Do you have a custom cover image for "Drift in Amber Light"? Audio items need their own visual in browse grids — without one, Wondermint uses a generic placeholder that hurts discovery. I can use a cover you provide (drop the path, e.g. `/tmp/drift-cover.png`), or help create one before posting.

I won't proceed without this.

### 2. Visibility (`private`) — depends on your plan

- Public is the default and works on any plan.
- Private requires a paid plan (Unleashed or Genesis). If you're on Free and want private, we'd need to handle the upgrade flow first.

What plan are you on, and do you want this public or private?

### 3. License (`contract_type`) — irreversible choice

Two options:

- `public_domain` — anyone can use the track freely. Common for ambient/generative pieces meant to be shared widely.
- `non_exclusive` — you retain rights; others license under non-exclusive terms.

These are independent of public/private visibility. Which do you want?

### 4. Description, prompt, model details

- I'll set `model: "Suno"` since you mentioned that.
- Do you have the Suno prompt you used? Optional, but nice for discovery and provenance.
- Description (max 2000 chars) — want to write your own, or want me to draft a short one ("Ambient piece generated with Suno — slow, amber-toned drift") for your approval?

### 5. Pre-approval for orphan-draft cleanup

If create succeeds but a later step fails (PUT, thumbnail PUT, or `/uploaded`), the listing sits as an orphan draft. I'd like pre-approval to `DELETE /api/v1/agents/listings/{listing_id}` in that case rather than leaving it stranded. OK with that fallback?

---

## My draft metadata plan (for your approval)

Pending your answers above, here's what I'd propose:

| Field | Value |
|---|---|
| `name` | `Drift in Amber Light` (locked after create — confirm it's exactly right, including capitalization) |
| `file_name` | `drift.mp3` |
| `thumbnail_name` | (your cover filename, e.g. `cover.png`) |
| `model` | `Suno` |
| `prompt` | (paste from Suno if you have it) |
| `description` | TBD — your text or my draft |
| `contract_type` | TBD — `public_domain` or `non_exclusive` |
| `private` | `false` (or `true` if you're paid and want private) |
| `subcategories` | `["Ambient / Atmospheric", "Calm / Peaceful", "Spacious / Reverb-Heavy"]` |
| `tags` | `["ambient", "suno", "drift", "atmospheric", "generative"]` |

### Why those subcategories

From the Audio category list, the ones that fit an ambient Suno piece called "Drift in Amber Light":

- **Ambient / Atmospheric** — primary genre
- **Calm / Peaceful** — mood
- **Spacious / Reverb-Heavy** — sonic style typical of ambient drift work

If the actual track is more melancholic, darker, or has more texture than that suggests, I'd swap one out — e.g. `Nostalgic / Dreamy`, `Dark / Ominous`, or `Textured`. Worth me listening to it first, or do you want to tell me what it actually sounds like? I want to avoid forcing five values when three accurate ones describe it better.

These have to come from the precreated audio subcategory list — paraphrases get rejected on upload. The values above are all valid.

### Tags vs subcategories

Tags are free-form; subcategories aren't. I'd avoid duplicating subcategories as tags. The draft tag list leans toward concrete search terms (model name, mood, genre) without generic noise like "art" or "ai".

---

## Draft of the actual create call (do not send yet)

```http
POST /api/v1/agents/listings
Host: api.wondermint.now
X-API-Key: $WONDERMINT_API_KEY
Content-Type: application/json

{
  "name": "Drift in Amber Light",
  "description": "<your text or my draft>",
  "file_name": "drift.mp3",
  "thumbnail_name": "<your cover filename>",
  "subcategories": ["Ambient / Atmospheric", "Calm / Peaceful", "Spacious / Reverb-Heavy"],
  "tags": ["ambient", "suno", "drift", "atmospheric", "generative"],
  "contract_type": "<public_domain | non_exclusive>",
  "model": "Suno",
  "prompt": "<Suno prompt, if you have it>",
  "private": false
}
```

A note on the title: `Drift in Amber Light` is fine — letters, spaces only. If you wanted to add punctuation like a comma or em-dash to the title, the API would reject it with `400 "Asset name contains special characters"`. So the current title is safe.

---

## What I'll tell you after it's live

Assuming it lands successfully, I'll come back with:

- Final status (`Minted`, `Listing`, or `Pending Approval` if your account is under manual review)
- The public URL on `https://wondermint.now/explore/{slug}` once available
- The exact **15-minute metadata edit deadline** as a wall-clock time
- A reminder that `name` and the cover are locked even within that window — only `description`, `tags`, `category_id`, and `private` can be patched

If anything fails mid-flow (e.g. a 429, processing failure, or under-review 409), I'll surface the error envelope, the stranded `listing_id` if there is one, and ask before retrying or deleting.

---

## What I need back from you

To get unstuck:

1. **Cover image path** (hard blocker)
2. **`contract_type`**: `public_domain` or `non_exclusive`?
3. **Visibility**: public, or private (and confirm you're on a paid plan)?
4. **Description**: your text, or shall I draft?
5. **Suno prompt**: paste it, or skip?
6. **Subcategories**: my three picks above, or do you want to adjust based on how the track actually sounds?
7. **Pre-approval for orphan-draft cleanup** if a mid-flow step fails — OK?

Once I have those, I'll show you the final exact JSON payload one more time and ask for explicit go-ahead before the first `POST`.
