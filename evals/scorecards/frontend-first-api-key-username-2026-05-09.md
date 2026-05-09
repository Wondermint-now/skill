# Frontend-First API Key Username Review - 2026-05-09

## Scope

Dry review for the flow where a user already created a Wondermint frontend
account, then wants to add agent/API access and receive an API key.

## Prompt

"I already created my Wondermint account in the frontend. Help me set up the API
key."

## Expected Behavior

- Treat the flow as frontend-first account connection.
- Confirm the existing frontend account email.
- Confirm where the one-time API key will be saved.
- Do not ask the user to choose a new username.
- Preserve the existing frontend username.
- If a payload helper requires `username`, use the already-chosen frontend
  username if known; otherwise ask for the existing username as an identifier,
  not as a new choice.
- Start and poll the device authorization flow.

## Result

Pass.

## Evidence

- `skills/flows/connect-account.md` now says not to ask for a username in the
  frontend-first path and explains that the device approval flow upgrades the
  same identity for agent/API use.
- `skills/auth.md` now documents the same exception under registration.
- `skills/flows/onboarding.md` routes frontend-first users to the connect flow
  and says not to ask for a new username.

## Validation

Command:

```bash
python3 repo-workflows/validate.py
```

Result:

```text
Wondermint validation passed.
```
