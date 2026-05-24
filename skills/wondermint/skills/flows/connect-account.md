# Connect Account Flow

Use this when the user wants to add API-key access to an existing Wondermint web account, or add web login to an account created through the API. Endpoint shapes live in [Auth & Identity](../auth.md); this file is the routing logic.

## Goal

End up with one Wondermint account the user can use in both places: browser session at `https://wondermint.now` and API access with `X-API-Key`.

## Choose The Path

Ask which access path exists first:

- **Web-first:** the user already signed up on the website and wants API access. → [Path A](#path-a-web-login-exists-first)
- **API-first:** the user registered through the API and wants to log into the frontend. → [Path B](#path-b-api-access-exists-first)

If they're not sure: can they log into `https://wondermint.now`? → web-first. Do they have an `mk_live_...` key? → API-first.

## Path A: Web Login Exists First

Re-register with the same email as the web account. The server detects the existing account and starts an RFC 8628 device authorization flow — `POST /api/v1/agents/register` returns a 202 with `device_code`, `user_code`, `verification_uri_complete`, `expires_in`, `interval`.

**Do not ask the user to choose a username** — they already chose one with the web account. If a tool requires `username`, use the existing one (ask for it as an identifier, not a new choice).

1. Show the user the `user_code` and `https://wondermint.now{verification_uri_complete}` plus expiration window. Tell them to approve in the browser. Don't expose `device_code` — it's only for polling.
2. Poll `GET /api/v1/agents/register/status?device_code=...` at the returned `interval`. See [Auth > Device Flow Polling](../auth.md#device-flow-polling).
3. On `confirmed`, save the returned `api_key` per [Auth > API Key Storage](../auth.md#api-key-storage) before doing anything else.

## Path B: API Access Exists First

The web login email is the account email — confirm via `GET /api/v1/agents/me` if not known. Check `is_email_verified`. If false, tell the user to open the verification email from API signup and verify before password login will work.

Ask the user to provide a password through the host's approved secret-entry path. Never print, log, or save it in repo files. Then `POST /api/v1/agents/password/set` ([Auth > Set Password](../auth.md#set-password)).

For magic-link login as an alternative, see [Auth > Frontend Login](../auth.md#frontend-login).

## Missing API Key Recovery

If the user can log into the frontend but lost their API key, route to [Auth > Regenerate API Key](../auth.md#regenerate-api-key) — it requires a browser session and disables all previous keys.

## Final Report

Tell the user: which path was used, whether frontend login is available, whether API access is available, where the API key was saved (or that it must be saved immediately), and any remaining action (email verification, password setup).
