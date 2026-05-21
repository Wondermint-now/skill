# Start Here

This repo develops Wondermint skill package variants. The default core skill
starts at `wondermint/SKILL.md` and `skills/wondermint/SKILL.md`. The
transactional marketplace variant starts at `wondermint-marketplace/SKILL.md`
and `skills/wondermint-marketplace/SKILL.md`.

## Package Boundary

The installable Wondermint skill surfaces are:

- `wondermint/SKILL.md`, `wondermint/CHECK_IN.md`, and `wondermint/skills/`
- `skills/wondermint/SKILL.md`, `skills/wondermint/CHECK_IN.md`, and
  `skills/wondermint/skills/`
- `wondermint-marketplace/SKILL.md`, `wondermint-marketplace/CHECK_IN.md`, and
  `wondermint-marketplace/skills/`
- `skills/wondermint-marketplace/SKILL.md`,
  `skills/wondermint-marketplace/CHECK_IN.md`, and
  `skills/wondermint-marketplace/skills/`

Everything else in this repo is for developing and improving the skill. Do not
put evaluation process, scorecard maintenance, release/versioning workflow,
research notes, or backend-inventory review instructions into the installable
skill files.

## Agent Handoff

When working in this repo:

1. Read `variants/core.md` or `variants/marketplace.md` to identify the active
   package line, then read the matching `SKILL.md`.
2. Read `PROGRESS.md` for the current state and next action.
3. Read `PLAN.md` for the phased roadmap.
4. Read `references/mvp-scope.md` before adding or expanding core endpoint
   coverage. Read `variants/marketplace.md` before adding transactional
   marketplace coverage.
5. Use only REST endpoints in skill docs. GraphQL operations are backend-awareness material only and must not be copied into the skill.
6. Keep user-facing Wondermint flows in the package `skills/flows/` directories.
7. Keep repo-development workflows in `repo-workflows/`.
8. Keep root package `SKILL.md` files concise. Move deeper API details,
   examples, FAQs, and flow guidance into referenced installable files.
9. Never commit real credentials or secrets.
10. Record future test evidence under `evals/`, but do not run Wondermint tests unless explicitly asked.
11. When tests reveal endpoint behavior, update `references/backend-endpoints/live-observations.md` before closing the task.

## Repo Purpose

The goal is to make the Wondermint skill useful for agents and users across the full Wondermint experience: setup, check-ins, uploads, discovery, social engagement, folders, notifications, and recovery from API errors.

## Versioning

Use variant-specific git tags for new skill versions:

- Core/default skill: `core-v0.1.7`, `core-v0.1.8`, `core-v0.2.0`
- Marketplace skill: `marketplace-v0.1.0`, `marketplace-v0.1.1`

Historical tags `v0.1.0` through `v0.1.6` belong to the core/default line.

Do not tag a version until there is a matching scorecard under
`evals/scorecards/` or the owner explicitly asks for a tag. Scorecards must
state the variant and whether transactional marketplace workflows are included.

## Credentials

Use `.env.example` as the committed template. Keep real credentials in local `.env` only.

Expected local variables:

```bash
WONDERMINT_API_KEY=
WONDERMINT_EMAIL=
WONDERMINT_PASSWORD=
WONDERMINT_BASE_URL=https://api.wondermint.now
WONDERMINT_FRONTEND_URL=
WONDERMINT_PRODUCTION_FRONTEND_URL=
```

Never paste, log, or commit real API keys, passwords, session tokens, cookies, or other sensitive values.

## Environment URLs

Use `https://api.wondermint.now` as the production API URL. Use
`https://minti-release.fullstock.ai/` as the current frontend URL for repo
testing. The production user-facing frontend URL is `https://wondermint.now`.

Installable skill docs should use `https://wondermint.now` for public web links
unless a task is explicitly about testing the release environment.

## Evaluation Evidence

Future evaluation artifacts belong in `evals/`:

- `evals/scorecards/` for version summaries.
- `evals/logs/` for raw notes, transcripts, screenshots, and API observations.
- `evals/templates/scorecard.md` for the reusable scorecard format.

Evaluation procedures belong in `repo-workflows/`, not in `wondermint/` or
`skills/wondermint/`.

Do not run Wondermint live tests unless explicitly asked.

## Repo Workflows

Development workflows belong in `repo-workflows/`:

- `repo-workflows/live-eval.md` for live skill evaluation.
- `repo-workflows/iteration.md` for changing skill files from feedback,
  research, backend observations, and eval results.
- `repo-workflows/validation.md` for dry checks before live testing.
- `repo-workflows/package-readiness.md` for checking and syncing installable
  skill packages by variant.

## Backend Source Reference

Source-derived backend endpoint references belong in `references/backend-endpoints/`.
Use that directory when updating API details in the skill files. Keep package
root skill files concise and route detailed endpoint shapes, errors, and
backend-only notes into focused reference files.

The backend reference is not the MVP scope. The current core skill files plus
`references/mvp-scope.md` define what belongs in the core skill. Do not add
transactional marketplace workflows to `wondermint/` or `skills/wondermint/`.
Marketplace buying, selling, order, seller analytics, payout, earnings, or
settlement workflows belong only in `wondermint-marketplace/` and
`skills/wondermint-marketplace/`.

Only REST endpoints may be used to update the active skill. GraphQL operations
may remain in backend reference files for awareness, but they are not an
agent-facing API surface.

During every eval or live test, compare observed responses against the backend
reference. Add confirmed behavior, exact response formatting, success messages,
error messages, hints, and recovery notes to
`references/backend-endpoints/live-observations.md`, then update the relevant
skill docs if the agent's behavior should change.
