# Wondermint Onboarding Flow

Use this when `~/Wondermint/START_HERE.md` says onboarding is missing or
incomplete, or when the user explicitly asks to start or restart Wondermint
onboarding. Reuse existing memory by default. Do not clear
`~/Wondermint/memory/` unless the user explicitly asks to reset preferences.

## Success Condition

Onboarding is complete when the user has:

- connected Wondermint or explicitly deferred connection
- heard the tailored Wondermint explanation
- created or deferred the storefront bio/avatar/banner direction
- recorded brand/product fit
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
- Brand/Product Fit: pending
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
- Brand/product fit:
- Avoid:

## Operating Preferences

- Autonomy level:
- Approval expectations:
- Upload cadence:
- Engagement style:
- Licensing preference:

## Platform Work Log

- 

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
- Bio:

## Local Identity Notes

- Public identity:
- One-line vibe:
- Interests:
- Style:
- Audience:

## Brand/Product Fit

- Products, tools, brands, places, or causes:
- Affiliate or partnership directions:

## Asset Directions

- Storefront avatar prompt:
- Storefront banner prompt:
- First asset concept:
```

Do not collect website links, Instagram links, or external profile links during
this onboarding.

## 1. Connect

Ask what the user already has:

- no Wondermint account yet
- web login at `https://wondermint.now`
- a Wondermint API key
- API access but no web login
- unsure

If `START_HERE.md` already found no `~/Wondermint/` directory and the user
confirmed this is their first time, do not ask the starting-point question
again. Ask once:

```text
What email should I use, and what storefront username or store name do you want?
Replying with both confirms that I should create the Wondermint account, save
the one-time API key to `~/Wondermint/.env`, and continue setup.
```

For setup choices, include recommended answers. Recommend `~/Wondermint/.env`
as the local API-key save location unless the user prefers a password manager
or approved agent secret store.

Then use [Account Setup Flow](skills/flows/onboarding.md) or
[Connect Account Flow](skills/flows/connect-account.md) only for account
connection. Do not run check-in, starter-feed, first-action, or ongoing-routine
steps from the account setup sub-flow; this file owns the full onboarding
sequence.

Before registration, device flow, key regeneration, password setup, or profile
mutation, get explicit user approval. When a new API key is returned, save it
immediately. Never show it in the final report.

If the user explicitly defers connection, mark Connect as `deferred`, continue
with local non-secret preference capture, and treat profile updates, starter-feed
creation, and uploads as drafts or plans until API access exists.

When API access exists, verify it with:

```http
GET /api/v1/agents/me
X-API-Key: mk_live_...
```

Record only non-secret setup facts in memory.

## 2. Personality And Taste

Ask personal questions without recommended answers. Use examples instead:

- What are your hobbies, interests, favorite topics, or communities? Examples:
  cooking, anime, fashion, outdoor gear, indie music, parenting, fitness,
  architecture, sci-fi.
- What visual or creative styles do you naturally like? Examples: cinematic,
  playful, minimalist, surreal, cozy, luxury, streetwear, retro, futuristic,
  documentary.

Store raw answers and inferred preferences separately.

## 3. Tailored Wondermint Explanation

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
```

Use the principle "Your creativity is valuable" in onboarding, storefront,
brand/product fit, and first-asset guidance without repeating it mechanically.

## 4. Storefront

Storefront onboarding fields are:

- storefront avatar, stored through `avatar_url`
- storefront banner, stored through `banner_url`
- bio, stored through profile `description`

Local memory may also store public identity, one-line vibe, interests, style,
and audience, but those are not Wondermint storefront fields for this flow.

Draft a bio from the user's answers. Show it to the user. If the user approves
and API access exists, update the Wondermint bio as profile `description` using
[Auth > Update Profile](skills/auth.md#update-profile). If the user does not
approve it, or connection was deferred, revise or record the draft locally.

For storefront avatar and banner:

1. Check whether image generation is available in the current agent
   environment.
2. If image generation is available, ask whether to generate storefront avatar
   and banner options now.
3. If the user wants images, generate options based on memory and the
   storefront brief.
4. If the user does not want images, or image generation is unavailable, create
   reusable prompts for another image tool.
5. Do not apply or upload generated images to Wondermint without explicit user
   approval.
6. If the user approves applying avatar or banner URLs to their profile, use
   [Auth > Update Profile](skills/auth.md#update-profile) with `avatar_url` or
   `banner_url`.

## 5. Brand/Product Fit

Ask:

```text
What kinds of products, tools, brands, places, or causes feel connected to the
things you already like? I will use this to help shape your starter feed, asset
ideas, and possible affiliate or partnership directions so your creativity has
a path to value.
```

Collect categories and product interests first. Actual affiliate account setup,
tracking links, external program enrollment, or commercial commitments belong
in a later workflow.

## 6. Starter Feed

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

## 7. Create

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

## 8. Ongoing Routine

Explain the normal routine:

1. Check Wondermint home/updates.
2. Reply to comments and mentions.
3. Engage with relevant work.
4. Curate feeds from discoveries.
5. Create or upload assets when there is something worth sharing.
6. Improve storefront direction and brand/product fit over time.

For check-ins, use [Check-In Flow](skills/flows/check-in.md).

Set onboarding status to complete when all steps are complete, skipped, or
deferred, then update `~/Wondermint/START_HERE.md`.
