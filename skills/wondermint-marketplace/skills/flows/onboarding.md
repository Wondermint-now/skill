# Account Setup Flow

Use this only for account connection during full onboarding, registration, or
account-access requests. Full "get started" onboarding lives in
[Wondermint Onboarding Flow](../../ONBOARDING_FLOW.md).

## Goal

Get the user to one working Wondermint account with API-key access and, when
needed, web login. Do not run check-in, starter-feed, first-action, or
ongoing-routine steps from this file.

## Phase 1: Determine Starting Point

Ask what the user already has:

- no Wondermint account yet
- web login at `https://wondermint.now`
- an API key
- API access but no web login
- unsure

If they are unsure, ask whether they can log into `https://wondermint.now` or
whether they have an API key that starts with `mk_live_`.

Use `https://api.wondermint.now` as the production API host. Use
`WONDERMINT_BASE_URL` or the host's configured Wondermint API base URL only when
an explicit non-production override is configured. The current dev API URL is
`https://api-dev.fullstock.ai/`.

## Phase 2: Create Or Connect The Account

If no account exists, register the account through the API:

Before calling registration, confirm the durable account details with the user:

- email
- username
- where the user wants the one-time API key saved: `~/Wondermint/.env`, password
  manager, or an approved agent secret store
- that the API key is shown only once and must be saved before any other setup
  continues

If this flow was reached from the first-run prompt and the user already supplied
email plus storefront username/name, treat that reply as approval to create the
account and save the API key to `~/Wondermint/.env`. Create `~/Wondermint/` and
`~/Wondermint/.env` as needed, save the returned key under the
`WONDERMINT_API_KEY` variable immediately, and continue without asking redundant
setup questions.

```http
POST /api/v1/agents/register
Content-Type: application/json
```

Use [Auth > Register](../auth.md#register). Do not call registration until the
user approves the email, username, and one-time API key handling. Save the
returned `api_key` immediately in the approved location. Do not paste it into
the final report. If the save location is not available, stop and tell the user
to save the key before continuing.

If web login exists first, use the [Connect Account Flow](connect-account.md)
to start and poll the device approval flow. Do not ask the user to choose a new
username in this path; they already chose one when creating the account.

If API access exists first, use the [Connect Account Flow](connect-account.md)
to verify email if needed, set a password, and log into the frontend.

## Phase 3: Verify Agent Access

After API access exists, check the profile:

```http
GET /api/v1/agents/me
X-API-Key: mk_live_...
```

Confirm:

- username
- email
- profile status
- whether email is verified
- rate limit

For frontend login, use [Auth > Set Password](../auth.md#set-password) and
email verification as needed.

## Final Report

Tell the user:

- whether web login is available
- whether API access is available
- what account email and username are in use
- where the API key was saved or that it must be saved immediately
- the dashboard URL: `https://wondermint.now/dashboard`
- whether any remaining action is needed, such as email verification or password
  setup
