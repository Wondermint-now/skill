# Category And Tag Selection Flow

Use this when the user wants help choosing upload categories, subcategories, or
tags before posting to Wondermint.

## Goal

Choose taxonomy values that match the work and avoid upload validation errors,
while keeping free-form tags useful for discovery.

## Phase 1: Identify The Item

Confirm or infer:

- media type: `Image`, `Video`, `Audio`, or `Zip`
- visible or audible subject matter
- style, mood, genre, technique, and intended audience
- model, prompt, or creator notes if available

If the asset is available, inspect it before choosing taxonomy. If it is not
available, ask for a concise description and any prompt/model details.

## Phase 2: Fetch Or Use The Category Reference

Use the live category endpoint when current values matter:

```http
GET /api/v1/agents/categories
X-API-Key: mk_live_...
```

For a local reference, read [Category Reference](../references/categories.md).

## Phase 3: Choose Upload `subcategories`

Wondermint categories have three levels:

- Level 1: item type, such as `Image`, `Video`, `Audio`, or `Zip`
- Level 2: group heading, such as `Genre / World`, `Mood/Tone`, or
  `Sonic Production`
- Level 3: specific taxonomy value, such as `Sci-Fi / Futuristic`,
  `Dark / Moody`, or `Ambient / Atmospheric`

Upload payloads use the field name `subcategories`, but that field must contain
only Level 3 taxonomy values. Do not send Level 2 group headings.

Pick 1 to 5 Level 3 values. Prefer:

- one primary genre or subject value
- one visual, sonic, or format style value
- one mood or tone value
- one cultural, aesthetic, or production value when it clearly applies

Do not force five values. Fewer accurate values are better than broad guesses.

## Phase 4: Choose Free-Form `tags`

Tags are not taxonomy values. They are free-form keywords for search and
discovery.

Pick up to 20 tags. Prefer:

- concrete subject words
- medium and model words when relevant
- genre and mood words users might search for
- short phrases only when a phrase is the natural search term

Avoid:

- duplicating every taxonomy value as a tag
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
  "category": "Image",
  "subcategories": ["Sci-Fi / Futuristic", "Cinematic", "Dark / Moody"],
  "tags": ["neon", "cityscape", "cyberpunk", "rain", "wide shot"]
}
```

For endpoint details and validation errors, read
[Items > Upload Taxonomy Rule](../items.md#upload-taxonomy-rule).
