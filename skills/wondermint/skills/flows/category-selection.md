# Category And Tag Selection Flow

Use this when the user wants help choosing upload categories, subcategories, or
tags before posting to Wondermint.

## Goal

Choose subcategories that match the work and avoid upload validation errors,
while keeping free-form tags useful for discovery.

## Phase 1: Identify The Item

Confirm or infer:

- media type: `Image`, `Video`, or `Audio`
- visible or audible subject matter
- style, mood, genre, technique, and intended audience
- model, prompt, or creator notes if available

Inspect it before choosing subcategories.

## Phase 2: Use The Category Reference

Read [Category Reference](../references/categories.md). Only the precreated
subcategory names in that reference are accepted; do not invent, paraphrase, or
send custom category names.

`subcategories` are not free-form. Select them from the reference list only. If
the user wants a descriptor that is not in the list, put it in `tags` instead.

## Phase 3: Choose Upload `subcategories`

In agent upload payloads, `subcategories` are the exact descriptor strings sent
to Wondermint:

- `Everyday / Contemporary`
- `Cinematic`
- `Warm / Cozy`

First identify the media type (`Image`, `Video`, or `Audio`) so you can use the
right precreated list. The upload payload usually does not need a separate
`category` field; the platform infers the item type from the file and selected
subcategories.

Pick 1 to 5 accepted subcategories for that media type. Prefer:

- one primary genre or subject value
- one visual, sonic, or format style value
- one mood or tone value
- one cultural, aesthetic, or production value when it clearly applies

Do not force five values. Fewer accurate values are better than broad guesses.

In the frontend create form, this appears as "Pick 3 that describe your post".
When the user provides those website selections, use them as upload
`subcategories` only if they exactly match accepted subcategory names.

## Phase 4: Choose Free-Form `tags`

Tags are not subcategories. They are free-form keywords for search and discovery.

Pick up to 20 tags. Prefer:

- concrete subject words
- medium and model words when relevant
- genre and mood words users might search for
- short phrases only when a phrase is the natural search term

Avoid:

- duplicating every subcategory as a tag
- generic tags like `art`, `cool`, or `ai` unless the user asks
- tags that imply content not present in the work

## Phase 5: Present A Draft

Show the user:

- item type
- selected `subcategories`
- selected `tags`
- one-sentence rationale
- any uncertainty or alternate options

Ask for approval or edits before upload. If the user has already approved the
agent to handle metadata, include these selections in the upload approval
summary before `POST /api/v1/agents/listings`.

## Final Output Shape

Use this shape when handing selections to the upload flow:

```json
{
  "subcategories": ["Sci-Fi / Futuristic", "Cinematic", "Dark / Moody"],
  "tags": ["neon", "cityscape", "cyberpunk", "rain", "wide shot"]
}
```

For endpoint details and validation errors, read
[Items > Upload Subcategory Rule](../items.md#upload-subcategory-rule).
