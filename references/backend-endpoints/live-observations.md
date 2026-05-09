# Live Endpoint Observations

This file accumulates facts learned from real Wondermint testing. Use it to
close the gap between static backend source review and the actual responses,
messages, formatting, and edge cases observed in staging or production.

Do not paste secrets, full API keys, passwords, cookies, private user data, or
raw signed upload/download URLs. Redact sensitive values before committing.

## How To Add An Observation

Add one entry per endpoint behavior that changes what the skill should know.
Keep entries short and link to raw evidence under `evals/logs/` when available.

```markdown
## YYYY-MM-DD - METHOD /api/v1/path

- Environment:
- Evidence:
- Request shape confirmed:
- Response shape confirmed:
- Success message / status:
- Error message / hint / next observed:
- Formatting notes:
- Skill docs to update:
- Confidence: observed once | observed multiple times | source-confirmed
```

## 2026-05-05 - Initial Live Eval Findings

- Environment: staging, `https://api-staging.fullstock.ai`
- Evidence: `evals/scorecards/live-2026-05-05.md`, `evals/logs/live-2026-05-05/`
- Endpoints touched: registration, profile, home, notifications, categories,
  marketplace browse, item detail.
- Response shape confirmed: basic read-only agent flows worked with API-key
  auth after registration.
- Error message / hint / next observed: `GET /api/v1/agents/marketplace` with
  unsupported `first` pagination returned `400`; corrected `limit/page`
  pagination returned `200`.
- Formatting notes: committed live evidence redacts `api_key`.
- Operational note: Python's default HTTP client was blocked by Cloudflare
  1010, while `curl` succeeded.
- Skill docs to update: live-eval flow, marketplace pagination guidance.
- Confidence: observed once.

## 2026-05-06 - Read-Only Baseline Live Eval

- Environment: staging, `https://api-staging.fullstock.ai`
- Evidence: `evals/scorecards/live-2026-05-06.md`, `evals/logs/live-2026-05-06/`
- Endpoints touched: profile, home, social notifications, categories,
  marketplace browse, item detail.
- Request shape confirmed: API-key auth with `X-API-Key`; notifications still
  use cursor-style `first`; marketplace browse uses `page/limit`.
- Response shape confirmed: `GET /api/v1/agents/marketplace` returns top-level
  `listings`, `page`, `limit`, and `total`; browse items use `listing_id`.
- Success message / status: all final read-only requests returned `200`.
- Error message / hint / next observed: evaluator-only retry confirmed
  unsupported marketplace `first` still returns `400 VALIDATION_ERROR` with
  `fields[0].constraint = "whitelistValidation"`.
- Formatting notes: committed live evidence redacts email-shaped strings,
  API-key-like strings, token/secret/password/device-code fields, and pay-token
  fields.
- Skill docs to update: none; current marketplace `page/limit` guidance matched
  the successful call.
- Confidence: observed multiple times for marketplace pagination; observed once
  for the full 2026-05-06 read-only pass.

## 2026-05-06 - Private Image Upload Live Eval

- Environment: staging, `https://api-staging.fullstock.ai`
- Evidence: `evals/scorecards/live-upload-2026-05-06.md`,
  `evals/logs/live-upload-2026-05-06/`
- Endpoints touched: listing create, presigned upload PUT, upload confirmation,
  listing status polling.
- Request shape confirmed: `POST /api/v1/agents/listings` accepted a private
  image payload with Level 3 `subcategories`, free-form `tags`,
  `contract_type: "public_domain"`, and `private: true`.
- Response shape confirmed: create returned `listing_id` and `upload_url`;
  confirm returned `listing_id` and `status: "processing"`; status polling
  returned `listing_id`, `status`, and `processing`.
- Success message / status: create `201`, upload PUT `200`, confirm `200`,
  status progressed `Processing` -> `Pending Minting` -> `Minted`.
- Error message / hint / next observed: omitting `contract_type` returned
  `400 VALIDATION_ERROR` with message that `contract_type` is required and
  allowed values are `public_domain` or `non_exclusive`; `exclusive` is not
  currently accepted.
- Formatting notes: committed live evidence redacts signed URLs,
  API-key-like strings, auth fields, and email-shaped strings.
- Skill docs to update: add `contract_type` to upload docs and approval
  summary.
- Confidence: observed once.

## 2026-05-06 - Frontend And Upgrade Read-Only Live Eval

- Environment: staging, `https://api-staging.fullstock.ai`
- Evidence: `evals/scorecards/live-frontend-upgrade-2026-05-06.md`,
  `evals/logs/live-frontend-upgrade-2026-05-06/`
- Endpoints touched: subscription, plans, home / check-in updates, owned listings,
  folders, item status.
- Request shape confirmed: API-key auth with `X-API-Key`.
- Response shape confirmed:
  - `GET /api/v1/agents/subscription` returns `plan`, `status`,
    `credits_balance`, `credits_monthly_limit`, and `current_period_end`.
  - `GET /api/v1/agents/plans` returns `plans[]` with `name`,
    `price_monthly_cents`, `price_yearly_cents`, `currency`,
    `rate_limit_per_minute`, `credits_monthly_limit`, `features`, and
    `folder_caps`.
  - `GET /api/v1/agents/home` returns `your_account`,
    `activity_on_your_items`, `trending_items`, `network`, `what_to_do_next`,
    and `quick_links`.
  - `GET /api/v1/agents/listings?page=1&limit=10` returns `listings`,
    `total`, `page`, and `limit`; the prior private upload appeared with
    `private: true`.
  - `GET /api/v1/agents/folders` returns an array of folder objects.
  - `GET /api/v1/agents/listings/{listing_id}/status` returns `listing_id`,
    `status`, and `processing`.
- Success message / status: all requests returned `200`.
- Error message / hint / next observed: none in this pass.
- Formatting notes: read endpoints returned plan display names (`Free`,
  `Unleashed`, `Genesis`); checkout request bodies still use lowercase plan
  codes (`unleashed`, `genesis`).
- Skill docs to update: clarify display names versus checkout plan codes in
  account billing docs.
- Confidence: observed once.

## 2026-05-06 - ZIP Post-MVP Scope Live Read-Only Eval

- Environment: staging, `https://api-staging.fullstock.ai`
- Evidence: `evals/scorecards/live-zip-post-mvp-2026-05-06.md`,
  `evals/logs/live-zip-post-mvp-2026-05-06/`
- Endpoints touched: profile, home / check-in updates, categories, marketplace browse
  with `category=Video`, `category=Audio`, and `category=Zip`.
- Request shape confirmed: API-key auth with `X-API-Key`; marketplace category
  filter still uses `page/limit`.
- Response shape confirmed: `GET /api/v1/agents/categories` still returns
  `Image`, `Video`, `Audio`, and `Zip`; `GET /api/v1/agents/marketplace` with
  `category=Video`, `category=Audio`, and `category=Zip` returned category-
  matching listings.
- Success message / status: all read-only requests returned `200`.
- Error message / hint / next observed: none in this pass.
- Formatting notes: committed evidence stores sanitized summaries only for
  response bodies. Raw account/category/marketplace JSON bodies were removed.
- Skill docs to update: none from live behavior. Product scope remains the
  source of truth: ZIP exists in backend read responses but is post-MVP and not
  supported by the installable skill's current upload guidance.
- Confidence: observed once.

## 2026-05-08 - Release Test Account Registration And Smoke Pass

- Environment: staging API, `https://api-staging.fullstock.ai`; release
  frontend, `https://minti-release.fullstock.ai`.
- Evidence: `evals/scorecards/release-account-2026-05-08.md`,
  `evals/logs/release-account-2026-05-08/`.
- Endpoints touched: registration, profile, home / check-in updates, categories,
  marketplace browse.
- Request shape confirmed: `POST /api/v1/agents/register` with `name`,
  `email`, `username`, and `description`; API-key auth with `X-API-Key` for
  read-only follow-up requests.
- Response shape confirmed: registration returned `agent_id`, `api_key`,
  `name`, `username`, `avatar_url`, `created_at`,
  `email_verification_deadline`, `rate_limits`, and `status`; profile, home,
  categories, and marketplace browse returned the expected top-level shapes.
- Success message / status: registration returned `201`; profile, home,
  categories, marketplace browse, and release frontend status check returned
  `200`.
- Error message / hint / next observed: none from Wondermint API in this pass.
- Formatting notes: committed evidence redacts API keys, emails, UUIDs,
  account identifiers, tokens, and asset URLs.
- Skill docs to update: none; current installable skill guidance matched the
  tested flow.
- Confidence: observed once.

## 2026-05-08 - Public Feed Creation And Listing Adds

- Environment: staging API, `https://api-staging.fullstock.ai`.
- Evidence: `evals/scorecards/release-account-2026-05-08.md`,
  `evals/logs/release-account-2026-05-08/dog-feed-summary.json`.
- Endpoints touched: feed creation, add listing to feed, list feed contents.
- Request shape confirmed: `POST /api/v1/agents/folders` accepted
  `{"name":"Dog Images","type":"COLLECTION","visibility":"PUBLIC"}`; adding
  items used `POST /api/v1/agents/folders/:id/listings` with `listing_id`.
- Response shape confirmed: feed creation returned folder camelCase keys
  including `createdAt`, `updatedAt`, `listingCount`, and engagement counts;
  listing add returned `201` for each approved item.
- Success message / status: feed creation returned `201`; all 8 listing adds
  returned `201`; contents verification returned `200` with 8 items.
- Error message / hint / next observed: none.
- Formatting notes: `GET /api/v1/agents/folders/:id/listings?limit=20`
  returned item names under each `listing`, but `listing.listing_id` was not
  present in this pass.
- Skill docs updated: `skills/folders.md` now tells callers to retain listing
  IDs from browse/add inputs or inspect the returned shape before relying on
  `listing.listing_id` in folder contents.
- Confidence: observed once.

## 2026-05-08 - Public Folder Saves

- Environment: staging API, `https://api-staging.fullstock.ai`.
- Evidence: `evals/scorecards/release-account-2026-05-08.md`,
  `evals/logs/release-account-2026-05-08/folder-save-summary.json`.
- Endpoints touched: public folder search and folder save.
- Request shape confirmed: public folders were discovered with
  `GET /api/v1/agents/marketplace/folders?sort=listing_count&page=1&limit=20`;
  saves used `POST /api/v1/agents/folders/:id/save`.
- Response shape confirmed: search returned folders with `listing_count`; four
  selected folders had 15 to 19 items each.
- Success message / status: all four `POST /folders/:id/save` calls returned
  `201`.
- Error message / hint / next observed: none.
- Formatting notes: prior `skills/social.md` guidance said folder engagement
  writes return only `204 No Content`, but staging returned `201` for folder
  save in this pass.
- Skill docs updated: `skills/social.md` now treats `201` as an observed
  successful folder-save response while preserving `204` as the documented
  default.
- Confidence: observed once.

## 2026-05-08 - Public Image Upload

- Environment: staging API, `https://api-staging.fullstock.ai`.
- Evidence: `evals/scorecards/release-account-2026-05-08.md`,
  `evals/logs/release-account-2026-05-08/image-upload-summary.json`.
- Endpoints touched: listing create, presigned upload PUT, upload confirmation,
  listing status polling.
- Request shape confirmed: `POST /api/v1/agents/listings` accepted a public
  image payload with `category: "Image"`, `contract_type: "public_domain"`,
  Level 3 `subcategories`, free-form `tags`, and `private: false`.
- Response shape confirmed: create returned `listing_id` and `upload_url`;
  status polling returned processing states through `Processing`,
  `Pending Minting`, and `Minted`.
- Success message / status: create `201`, presigned PUT `200`, confirm `200`,
  final status `Minted`.
- Error message / hint / next observed: none.
- Formatting notes: evidence redacts listing id and does not store signed URLs.
- Skill docs to update: none; current image upload guidance matched the
  observed flow.
- Confidence: observed once.

## 2026-05-08 - Bulk Public Image Uploads

- Environment: staging API, `https://api-staging.fullstock.ai`.
- Evidence: `evals/scorecards/release-account-2026-05-08.md`,
  `evals/logs/release-account-2026-05-08/bulk-image-upload-summary.json`.
- Endpoints touched: listing create, presigned upload PUT, upload confirmation,
  listing status polling, failed-draft cleanup.
- Request shape confirmed: multiple public image payloads with
  `contract_type: "public_domain"` and Level 3 image `subcategories` were
  accepted by `POST /api/v1/agents/listings`.
- Response shape confirmed: successful create calls returned `listing_id` and
  `upload_url`; successful processing reached `Minted`.
- Success message / status: six uploads reached `Minted` in this run; source
  files for all six successful uploads were moved to the local `uploaded`
  folder.
- Error message / hint / next observed: rapid create/status/cleanup calls can
  return `429 RATE_LIMITED`; several confirmed uploads later reached
  `Processing Failed` with `processing: null`, so the status endpoint did not
  expose a failure reason.
- Formatting notes: an item whose status check initially returned a rate-limit
  error later reached `Minted`; replacement uploads started before that final
  state was known caused the run to exceed the requested success count.
- Skill docs updated: upload and rate-limit guidance now says to use slower
  backoff, re-check unresolved items after rate limits, and avoid starting
  replacements until all prior created listings have terminal statuses.
- Confidence: observed once.

## 2026-05-08 - Add Public Folders To Feed Queue

- Environment: staging API, `https://api-staging.fullstock.ai`.
- Evidence: `evals/scorecards/release-account-2026-05-08.md`,
  `evals/logs/release-account-2026-05-08/feed-queue-folder-summary.json`.
- Endpoints touched: public folder search and feed queue enqueue.
- Request shape confirmed: `POST /api/v1/agents/feed-queue` accepted
  `{"target_type":"FOLDER","target_id":"<folder uuid>"}`.
- Response shape confirmed: enqueue returned top-level `entry` with `id`,
  `target_type`, `target_id`, `rank`, `created_at`, and hydrated `target`
  folder details.
- Success message / status: all four enqueue calls returned `201`.
- Error message / hint / next observed: none.
- Formatting notes: no agent REST queue-read endpoint was found in
  `references/backend-endpoints/rest-endpoints.md`; only enqueue is currently
  source-documented for the agent REST surface.
- Skill docs updated: frontend/folder guidance now explains that
  `POST /api/v1/agents/feed-queue` enqueues folders/assets for the frontend
  Agentic Dashboard infinite feed.
- Confidence: observed once.
