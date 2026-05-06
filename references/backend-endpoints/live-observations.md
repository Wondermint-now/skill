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
- Endpoints touched: subscription, plans, home dashboard, owned listings,
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
