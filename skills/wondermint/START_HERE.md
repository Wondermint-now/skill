# Wondermint Routing Gate

Read this package file before any Wondermint task, unless the task is only a
skill file version or update check. This file decides whether to use existing
credentials, run narrow account setup, run full onboarding, or continue to the
requested task.

Important: this installed package file is different from the user's local
routing state file at `~/Wondermint/START_HERE.md`. When these instructions say
"user routing state file," they mean the file under `~/Wondermint/`.

## User Data Directory

Use `~/Wondermint/` for mutable user state:

```text
~/Wondermint/
├── START_HERE.md
├── .env
├── memory/
│   ├── ONBOARDING_STATUS.md
│   ├── WONDERMINT_MEMORY.md
│   ├── STOREFRONT_BRIEF.md
│   └── WORK_LOG.md
└── assets/
```

Create missing directories and markdown files as needed. Create `.env` only
when saving an API key or when the user chooses that save location. Preserve
existing files; update them surgically instead of overwriting.

## Routing

Skill file version or update checks bypass onboarding and use the package
source-check instructions in `SKILL.md`. Do not create user memory or load an
API key for version checks.

1. If `WONDERMINT_API_KEY` is already available in the process environment, use
   it for authenticated Wondermint API calls.
2. If `~/Wondermint/.env` exists, load `WONDERMINT_API_KEY` from it using the
   host's safe environment-loading method. Never print the key.
3. If either step 1 or 2 found credentials, do not ask the first-run local setup
   question solely because `~/Wondermint/` is missing. Continue with the routing
   rules below.
4. If credentials are not available and `~/Wondermint/` does not exist, preserve
   the user's original request and say exactly: "No local Wondermint setup was
   found. This usually means this is your first time connecting Wondermint with
   this agent. Is that correct?"
   If the user says no, ask where their API key or setup files are stored.
   If the user says yes and the original request was a specific task, ask for
   the email, storefront/profile username, and store/profile name in one
   prompt, then run [Account Setup Flow](skills/flows/account-setup.md) and
   return to the original task. Do not run the taste, storefront, starter-feed,
   or first-asset steps unless the user asks to continue onboarding.
   If the user says yes and the original request was open-ended setup,
   "get started," or onboarding, use [ONBOARDING_FLOW.md](ONBOARDING_FLOW.md)
   and ask only its single consolidated intake prompt; do not collect email or
   username in a separate round first.
5. Read the user routing state file if it exists. If it does not exist, create
   `~/Wondermint/START_HERE.md` with onboarding marked `incomplete`, then
   continue with the routing rules below.
6. If the user asked a specific task and credentials are available, route that
   task normally from [SKILL.md](SKILL.md), even when onboarding is incomplete.
   Offer to resume onboarding after the requested task.
7. If the user asked a specific task but credentials are not available, use
   [Account Setup Flow](skills/flows/account-setup.md) first, then return to the
   requested task. Do not start the taste, storefront, starter-feed, or
   first-asset onboarding steps unless the user asks to continue onboarding.
8. If the user routing state file says onboarding is `complete`, continue with
   the requested task using the matching task area in [SKILL.md](SKILL.md).
   Load deeper memory only when useful for the task.
9. If onboarding is missing, `incomplete`, or explicitly requested by the user
   and the request is open-ended setup, "get started," or onboarding, read
   [ONBOARDING_FLOW.md](ONBOARDING_FLOW.md).

## Minimal User START_HERE.md

Keep `~/Wondermint/START_HERE.md` short and predictable:

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

## Work Log

Use `~/Wondermint/memory/WORK_LOG.md` only as a thin audit trail of durable
platform actions: uploads, profile changes, portfolio/playlist/feed changes,
billing actions, and webhook changes. One dated line per action, newest first.
Keep at most 50 entries; delete the oldest lines when appending past that cap.
Wondermint is the source of truth for platform history — query the API instead
of duplicating responses into the log.

Do not load the work log during routing or normal tasks. Read it only when the
user asks about past Wondermint activity or before repeating an action that may
already have been done.

## Secrets

Store API keys only in `WONDERMINT_API_KEY` in the process environment,
`~/Wondermint/.env`, the user's password manager, or the host agent's approved
secret store. Never store secrets in markdown memory files.
