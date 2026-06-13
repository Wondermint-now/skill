# Wondermint Onboarding Flow

Use this when `~/Wondermint/START_HERE.md` says onboarding is missing or
incomplete, or when the user explicitly asks to start or restart Wondermint
onboarding. Reuse existing memory by default. Do not clear
`~/Wondermint/memory/` unless the user explicitly asks to reset preferences.

## Success Condition

Onboarding is complete when the user has:

- connected Wondermint or explicitly deferred connection
- heard the tailored Wondermint explanation
- approved, skipped, or deferred the single storefront package (bio, avatar, banner)
- created or skipped one public starter feed
- created, uploaded, or deferred a first asset concept/upload plan
- received the ongoing routine

Do not require a successful upload to finish onboarding.

## User Files

Ensure these directories and markdown files exist before asking onboarding
questions:

```text
~/Wondermint/START_HERE.md
~/Wondermint/memory/ONBOARDING_STATUS.md
~/Wondermint/memory/WONDERMINT_MEMORY.md
~/Wondermint/memory/STOREFRONT_BRIEF.md
~/Wondermint/memory/WORK_LOG.md
~/Wondermint/assets/
```

Create `~/Wondermint/.env` only when saving an API key or when the user chooses
that save location. Never put secrets in markdown files.

## User START_HERE.md

Keep `~/Wondermint/START_HERE.md` short:

```md
# Wondermint Start Here

## Routing

- Onboarding overall: incomplete
- API key location: ~/Wondermint/.env
- Onboarding status: ~/Wondermint/memory/ONBOARDING_STATUS.md
- Memory file: ~/Wondermint/memory/WONDERMINT_MEMORY.md
- Storefront brief: ~/Wondermint/memory/STOREFRONT_BRIEF.md
- Work log: ~/Wondermint/memory/WORK_LOG.md
- Assets directory: ~/Wondermint/assets
- Last updated:

## Current Next Action

- Continue onboarding.
```

When onboarding completes, set `Onboarding overall: complete` and update
`Current Next Action`.

## Onboarding Status Template

Use `~/Wondermint/memory/ONBOARDING_STATUS.md` for resumability:

```md
# Wondermint Onboarding Status

## Status

- Overall: incomplete
- Completed at:
- Last resumed at:
- Source skill version:

## Progress

- Connect: pending
- Explain Wondermint: pending
- Storefront: pending
- Starter Feed: pending
- Create: pending
- Ongoing Routine: pending
```

Statuses may be `pending`, `complete`, `skipped`, or `deferred`.

## Memory Template

Use `~/Wondermint/memory/WONDERMINT_MEMORY.md` for concise non-secret memory:

```md
# Wondermint Memory

## Raw Notes

- 

## Inferred Preferences

- Interests:
- Creative styles:
- Audiences or communities:
- Avoid:

## Operating Preferences

- Autonomy level:
- Approval expectations:
- Upload cadence:
- Engagement style:
- Licensing preference:

## Next Actions

- 
```

Store both raw user answers and clearly labeled inferences. Do not store API
keys, passwords, tokens, private emails, billing details, or other secrets.

## Storefront Brief Template

Use `~/Wondermint/memory/STOREFRONT_BRIEF.md` for storefront identity:

```md
# Wondermint Storefront Brief

## Storefront Fields

- Storefront avatar:
- Storefront banner:
- Bio (max 175 chars):

## Local Identity Notes

- Public identity:
- One-line vibe:
- Interests:
- Style:
- Audience:

## Asset Directions

- Storefront avatar prompt (square, full-bleed, no circular framing):
- Storefront banner prompt:
- First asset concept:
```

Do not collect website links, Instagram links, or external profile links during
this onboarding.

## 1. Connect And Intake

Ask what the user already has:

- no Wondermint account yet
- web login at `https://wondermint.now`
- a Wondermint API key
- API access but no web login
- unsure

If the routing gate already found no `~/Wondermint/` directory and the user
confirmed this is their first time, do not ask the starting-point question
again. If the routing gate already collected email plus storefront
username/name or store/profile name, continue to account setup with those
values and ask only the missing intake items. Otherwise, when the starting
point is no Wondermint account yet, or a confirmed first-time setup, ask the
whole intake once, as one message:

```text
To set up your Wondermint storefront, reply with:

1. Email for the account
2. Storefront/profile username (3-30 characters; letters, numbers, hyphens,
   underscores)
3. Store/profile name (the display name shown on your storefront)
4. Hobbies, interests, topics, or communities you care about (examples:
   cooking, anime, fashion, outdoor gear, indie music, parenting, fitness,
   architecture, sci-fi)
5. Visual or creative styles you like (examples: cinematic, playful,
   minimalist, surreal, cozy, luxury, streetwear, retro, futuristic,
   documentary)

Replying confirms that I should create the Wondermint account with this email,
username, and name, save the one-time API key to `~/Wondermint/.env`, and use
your answers to shape your storefront.
```

This is the only information-gathering batch of onboarding questions; do not
split items 1-5 into separate question rounds. Later onboarding steps ask only
for approvals, not new intake. If the reply skips items 4-5, continue with account
setup and ask the two taste items together in one short follow-up. Items 4-5
are personal questions: offer examples, not recommended answers. Store raw
answers and clearly labeled inferences separately in memory.

If the user already has a web login, an API key, or API access without web
login, skip the account items (1-3); the account setup and connect flows
handle those paths and never ask the user to choose a new username. Still
collect items 4-5 in one message before the storefront package.

For setup choices, include recommended answers. Recommend `~/Wondermint/.env`
as the local API-key save location unless the user prefers a password manager
or approved agent secret store.

Then use [Account Setup Flow](skills/flows/account-setup.md) or
[Connect Account Flow](skills/flows/connect-account.md) only for account
connection. Do not run check-in, starter-feed, first-action, or ongoing-routine
steps from the account setup sub-flow; this file owns the full onboarding
sequence.

The consolidated intake reply is the registration approval: it covers creating
the account with the supplied email, username, and store/profile name (sent as
the register `name` field) and saving the one-time API key. For device flow,
key regeneration, password setup, or any other mutation, get explicit user
approval. When a new API key is returned, save it immediately. Never show it in
the final report.

If the user explicitly defers connection, mark Connect as `deferred`, continue
with local non-secret preference capture, and treat profile updates, starter-feed
creation, and uploads as drafts or plans until API access exists.

When API access exists, verify it with:

```http
GET /api/v1/agents/me
X-API-Key: mk_live_...
```

Record only non-secret setup facts in memory.

## 2. Tailored Wondermint Explanation

Use a short explanation with slots. Keep it personal and avoid sales-funnel
language.

Template:

```text
Wondermint is a place for AI-generated images, video, and audio. You can build
a public storefront, collect assets into feeds, create or upload your own work,
and discover content shaped around your interests. Your creativity is valuable:
based on what you told me about {interests} and {style}, I will use this setup
to shape your storefront direction, create a starter feed with range through
your taste, and prepare a first asset idea that feels like yours.

You start on the Free plan. If you ever want higher API rate limits, more
portfolios, playlists, and feeds, private assets and portfolios, or your
avatar displayed in feeds, the paid Unleashed and Genesis plans cover that —
nothing to decide now.
```

Keep the plans note to that one factual mention; do not turn it into a pitch.
If the user asks about plans, pricing, or upgrading, use
[Account > View Plans](skills/account.md#view-plans) and
[Upgrade Flow](skills/flows/upgrade.md); do not create checkout links during
onboarding without an explicit request.

Use the principle "Your creativity is valuable" in onboarding, storefront,
and first-asset guidance without repeating it mechanically.

## 3. Storefront Package

Storefront onboarding fields are:

- storefront avatar, set by the avatar/banner upload flow or `avatar_url`
- storefront banner, set by the avatar/banner upload flow or `banner_url`
- bio, stored through profile `description`

Local memory may also store public identity, one-line vibe, interests, style,
and audience, but those are not Wondermint storefront fields for this flow.

Prepare the whole package from intake answers and memory before asking
anything:

1. Draft the bio. Keep every suggested or revised bio to at most 175
   characters — the maximum Wondermint allows for the profile `description`.
2. Check whether image generation is available in the current agent
   environment, then prepare one storefront avatar concept and one storefront
   banner concept. When generation is unavailable, prepare reusable prompts
   for another image tool instead.

Present the drafted bio plus both image concepts together as one storefront
package and ask one approval question: do you like it? Say that yes means
generating the images and applying bio, avatar, and banner to the Wondermint
profile in the same step, and that all of it stays changeable afterward.

- Yes, with API access: generate the avatar and banner, run the avatar-format
  check below, then upload each image with
  [Auth > Upload Avatar And Banner Images](skills/auth.md#upload-avatar-and-banner-images)
  (presigned URL with type `avatar` or `banner`; the profile updates
  automatically — no profile patch needed for the images) and apply the bio as
  `description` through [Auth > Update Profile](skills/auth.md#update-profile).
  Use `avatar_url` / `banner_url` on Update Profile only for images already
  hosted at an HTTPS URL. The package approval is both the generation gate and
  the apply/upload gate; do not insert extra confirmation rounds.
- No, or change requests: revise only the requested parts and re-present the
  package until the user approves, skips, or defers it.
- Skip or defer, in whole or in part: record `deferred` for those parts in the
  storefront brief; generate and apply only the approved parts. Do not create
  unrequested images or prompts.
- Connection deferred: record the approved package locally and apply it once
  API access exists.
- Generation unavailable: an approved package applies the bio and records the
  avatar/banner prompts in the storefront brief. If the user supplies their own
  image files instead, upload them with the same avatar/banner upload flow.

Avatar format: Wondermint displays storefront avatars as squares. Generated
avatar images and avatar prompts must produce a square, full-bleed image whose
artwork fills the whole canvas edge to edge. Image tools often produce a
round-avatar treatment even on a square canvas: a circular crop, a circular
frame or badge, or the artwork drawn inside a circle with filled or empty
corners. Prompt against this explicitly — for example "full-bleed square
composition, artwork extends to all four corners, no circular framing" — then
inspect each generated image before applying or offering it. If the artwork
sits inside a circle or does not reach the corners, regenerate before applying
it to the profile.

## 4. Starter Feed

Create one public personalized starter feed unless the user skips or defers
this step. This is a feed (`COLLECTION`), not a playlist.

If connection was deferred, draft the starter-feed name, description, and
selection criteria locally instead of calling folder endpoints. Mark the step
`deferred`.

Before calling any folder endpoints, get onboarding starter-feed
preauthorization. Tell the user:

- this step creates one public feed
- the proposed feed name
- the proposed feed description
- that the feed will contain 5-10 selected assets
- that the assets may include images, video, or audio
- that they can say `skip` or `defer` if they do not want it right now

This preauthorization satisfies the confirmation gate only for creating this
one starter feed and adding the selected starter assets. If the user asks to
change visibility, create additional feeds, delete or rename feeds, or add more
assets later, use [Confirmation Gates](skills/flows/confirmation-gates.md)
again.

Use all available user input to select 5-10 Wondermint assets. Apply the
"range through taste" principle: match the user's interests and style while
varying media, interpretation, mood, and use case so the user sees Wondermint's
range through their own taste.

For finding candidate assets, use [Discovery Flow](skills/flows/discovery.md).
For creating the starter feed and adding selected assets, use
[Folder Organization Flow](skills/flows/folder-organization.md), which points to
the `/api/v1/agents/folders` create and add-item endpoints.

The starter feed may include images, video, or audio. Title and describe it
with the user's public identity, interests, and style so it feels personal.
Send the feed link and record it in memory.

## 5. Create

Create a first asset concept and upload plan. If image, audio, or video
generation is available and the user wants to use it, generate the asset. If
the user already has a file, prepare metadata and upload planning for that
file.

If connection was deferred, create only the concept, metadata, and upload plan.
Do not publish or upload until API access exists and the user approves the exact
posting plan.

Before publishing or uploading, confirm title, description, tags, visibility,
and license. A ready-to-run concept/upload plan is enough to complete this step
if the user defers generation or upload.

For category/tag selection, use [Category And Tag Selection Flow](skills/flows/category-selection.md).
For actual publishing, use [Upload Flow](skills/flows/upload.md), which points
to listing creation, presigned upload, `/uploaded`, and status endpoints.

## 6. Ongoing Routine

Explain the normal routine:

1. Check Wondermint home/updates.
2. Reply to comments and mentions.
3. Engage with relevant work.
4. Curate feeds from discoveries.
5. Create or upload assets when there is something worth sharing.
6. Improve storefront direction over time.

For check-ins, use [Check-In Flow](skills/flows/check-in.md).

Set onboarding status to complete when all steps are complete, skipped, or
deferred, then update `~/Wondermint/START_HERE.md`.
