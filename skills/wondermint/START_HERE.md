# Wondermint Start Here

Read this before any Wondermint task. It keeps the package instructions small
while user-specific state lives outside the installed skill.

## User Data Directory

Use `~/Wondermint/` for mutable user state:

```text
~/Wondermint/
├── START_HERE.md
├── .env
├── memory/
│   ├── ONBOARDING_STATUS.md
│   ├── WONDERMINT_MEMORY.md
│   └── STOREFRONT_BRIEF.md
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
3. If `~/Wondermint/` does not exist, say: "No local Wondermint setup was found.
   This usually means this is your first time connecting Wondermint with this
   agent. Is that correct?" If the user says yes, continue to onboarding and ask
   for the email and storefront username/name in one prompt. If they say no, ask
   where their API key or setup files are stored.
4. Read `~/Wondermint/START_HERE.md` if it exists. If it does not exist, create
   it with onboarding marked `incomplete`, then continue to onboarding.
5. If the user asked a specific task and credentials are available, route that
   task normally from [SKILL.md](SKILL.md), even when onboarding is incomplete.
   Offer to resume onboarding after the requested task.
6. If the user asked a specific task but credentials are not available, use
   [Account Setup Flow](skills/flows/onboarding.md) first, then return to the
   requested task. Do not start the personality, storefront, starter-feed, or
   first-asset onboarding steps unless the user asks to continue onboarding.
7. If user `START_HERE.md` says onboarding is `complete`, route the user's task
   normally from [SKILL.md](SKILL.md). Load deeper memory only when useful for
   the task.
8. If onboarding is missing, `incomplete`, or explicitly requested by the user
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
- Assets directory: ~/Wondermint/assets
- Last updated:

## Current Next Action

- Continue onboarding.
```

## Secrets

Store API keys only in `WONDERMINT_API_KEY` in the process environment,
`~/Wondermint/.env`, the user's password manager, or the host agent's approved
secret store. Never store secrets in markdown memory files.
