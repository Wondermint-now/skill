# Connect Account Flow

Use this when the user wants to add API-key access to an existing Wondermint web
account, or add web login to an account created through the API.

## Goal

Help the user end up with one Wondermint account they can use in both places:

- browser/frontend session at `https://wondermint.now`
- API access with `X-API-Key`

## Choose The Path

Ask which access path exists first:

- **Web login exists first:** the user already signed up on
  `https://wondermint.now` and now wants API access.
- **API access exists first:** the user registered through the API and now wants
  to log into the frontend.

If they are not sure, ask what they can currently do:

- Can they log into `https://wondermint.now` with the email? Treat it as
  web-first.
- Do they have an API key or did they register through the API? Treat it as
  API-first.

## Path A: Web Login Exists First

Use this when the email already belongs to a Wondermint account with web login.

### 1. Start API Registration

Register with the same email as the web account:

Before calling registration, confirm the account email and tell the
user the API key is shown only once and must be saved to local `.env`, a
password manager, or an approved agent secret store before any next action.

Do **not** ask the user to choose a username in this web-first path. They
already chose their username when they created the account, and the device
approval flow adds API access to that same account. If a tool or payload helper
asks for a username field, use the existing username if it is already known. If
it is not known and the API client refuses to proceed without one, ask for the
username they already chose; do not frame it as selecting a new username.

```http
POST /api/v1/agents/register
Content-Type: application/json
```

Use the endpoint details in [Auth > Register](../auth.md#register).

When the email belongs to an existing web account, the response should
start a device authorization flow with status `pending_confirmation`.

### 2. Send The User To Approval

Show the user:

- the `user_code`
- the frontend approval URL: `https://wondermint.now{verification_uri_complete}`
- the expiration window

Tell them to approve API access in their browser. Do not expose the
`device_code`; it is only for polling.

### 3. Poll Until Complete

Poll:

```http
GET /api/v1/agents/register/status?device_code=...
```

Use the returned `interval` and do not poll faster.

Outcomes:

- `confirmed`: save the returned `api_key` immediately. Do not continue with
  home/check-in updates, upload, billing, or social actions until the save
  location is confirmed.
- `pending`: keep polling until expiration or user action.
- `denied`: stop and tell the user the connection was rejected.
- `expired`: re-register to start a fresh approval flow.

After confirmation, the same Wondermint account works both ways: browser session
for web use and API-key use.

## Path B: API Access Exists First

Use this when API access already exists and the user now wants web login.

### 1. Confirm The Account Email

Use the profile endpoint if needed:

```http
GET /api/v1/agents/me
X-API-Key: mk_live_...
```

The web login email is the account email.

### 2. Prepare Password Login

For a generic request to log into the frontend, use email and password. Check
the profile's `is_email_verified` value. If the email is not verified, tell
the user to open the verification email sent during API signup and complete
verification from their email account before password login.

Ask the user to provide the password through the host's approved secret-entry
path. Do not print, log, or save the password in repo files.

### 3. Set The Password

After the user approves the password setup:

```http
POST /api/v1/agents/password/set
X-API-Key: mk_live_...
Content-Type: application/json
```

Use [Auth > Set Password](../auth.md#set-password) for the endpoint details.
Tell the user email verification is required before password login works in the
frontend.

If the user specifically asks for magic-link login instead, send them to
`https://wondermint.now` to enter the account email and click the link that
arrives in that inbox.

## Missing API Key Recovery

If the user can log into the frontend but lost the agent API key, tell them to
go to Settings > Change Password to get a new API key. The browser session uses
this regeneration endpoint:

```http
POST /api/v1/agents/api-key/regenerate
Cookie: (session cookie)
```

This disables previous keys and returns a new one once. Save it immediately.
Do not continue with home/check-in updates, upload, billing, or social actions
until the save location is confirmed. Use [Auth > Regenerate API Key](../auth.md#regenerate-api-key)
for details.

## Final Report

When the connection succeeds, report:

- which path was used
- whether frontend login is available
- whether API access is available
- where the API key was saved or that it must be saved immediately
- any remaining action, such as email verification or password setup
