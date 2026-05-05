# Start Here

This repo develops the Wondermint multi-folder skill file. The active skill starts at `SKILL.md`, with supporting domain files in `skills/`.

## Agent Handoff

When working in this repo:

1. Read `SKILL.md` to understand the active Wondermint skill.
2. Read `PROGRESS.md` for the current state and next action.
3. Read `PLAN.md` for the phased roadmap.
4. Keep `SKILL.md` concise. Move deeper API details, examples, FAQs, and flow guidance into referenced files.
5. Never commit real credentials or secrets.
6. Record future test evidence under `evals/`, but do not run Wondermint tests unless explicitly asked.

## Repo Purpose

The goal is to make the Wondermint skill useful for agents and users across the full Wondermint experience: setup, check-ins, uploads, discovery, social engagement, folders, notifications, and recovery from API errors.

## Versioning

Use git tags for skill versions, with tags like `v0.1.0`, `v0.2.0`, and `v0.3.0`.

Do not tag a version until there is a matching scorecard under `evals/scorecards/` or the owner explicitly asks for a tag.

## Credentials

Use `.env.example` as the committed template. Keep real credentials in local `.env` only.

Expected local variables:

```bash
WONDERMINT_API_KEY=
WONDERMINT_EMAIL=
WONDERMINT_PASSWORD=
WONDERMINT_BASE_URL=
WONDERMINT_FRONTEND_URL=
```

Never paste, log, or commit real API keys, passwords, session tokens, cookies, or other sensitive values.

## Evaluation Evidence

Future evaluation artifacts belong in `evals/`:

- `evals/scorecards/` for version summaries.
- `evals/logs/` for raw notes, transcripts, screenshots, and API observations.
- `evals/templates/scorecard.md` for the reusable scorecard format.

Phase 1 creates the structure only. It does not require running Wondermint flows.

## Backend Source Reference

Source-derived backend endpoint references belong in `references/backend-endpoints/`.
Use that directory when updating API details in the skill files. Keep the root
skill concise and route detailed endpoint shapes, errors, and backend-only
notes into focused reference files.
