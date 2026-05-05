# Live Eval Workflow

This workflow is for improving the Wondermint skill repo. It is not part of
the installable Wondermint skill.

## When To Use

Use this only when the owner explicitly asks to test the skill against live
Wondermint.

Do not run live tests as part of ordinary skill-file edits.

## Safety Rules

- Keep real credentials in `.env` or `.tmp/` only.
- Redact API keys, passwords, cookies, session tokens, and private user data
  before saving evidence.
- Use REST endpoints only. Do not test or document GraphQL behavior for agents.
- Start with read-only endpoints.
- Do not upload, comment, like, follow, mark notifications read, rotate keys,
  set passwords, or change account settings unless the owner explicitly asks.
- Do not add endpoints outside the MVP source of truth unless the owner
  explicitly asks for that endpoint.

## Setup

1. Confirm the working tree with `git status --short`.
2. Load credentials from `.env` or an ignored `.tmp/*.env` file.
3. Prefer `curl` for live HTTP calls. The 2026-05-05 live eval found that
   Python's default HTTP client could be blocked by Cloudflare 1010 with
   `browser_signature_banned`, while `curl` succeeded.
4. Create a dated evidence folder under `evals/logs/`.

## Read-Only Pass

Run only the scenarios needed for the eval request. A typical safe sequence is:

1. Authenticate/register only if needed.
2. `GET /api/v1/agents/me`
3. `GET /api/v1/agents/home`
4. `GET /api/v1/agents/notifications`
5. `GET /api/v1/agents/categories`
6. Browse/discovery endpoints already documented in the current skill.
7. Item detail for public items already returned by browse.

Save sanitized response samples under `evals/logs/<run>/`.

## Evidence Capture

For every observed behavior that matters:

- Save raw or summarized evidence with secrets redacted.
- Update `references/backend-endpoints/live-observations.md`.
- Update static backend reference files only when source-derived docs were
  wrong or incomplete.
- Update skill files only when the observation improves user-facing Wondermint
  behavior.

## Scorecard

Create or update a scorecard under `evals/scorecards/` using
`evals/templates/scorecard.md`.

Record:

- scenario result and score
- evidence paths
- what worked
- what confused the agent
- missing context
- endpoint reference updates
- MVP scope and REST-only checks
- credential safety review

## Wrap Up

Before committing:

1. Confirm no secrets were added.
2. Confirm no GraphQL operations were added to installable skill files.
3. Confirm no repo-development workflow instructions were added to `SKILL.md`,
   `CHECK_IN.md`, or `skills/`.
4. Run `git status --short` and commit the eval artifacts as one logical
   change if the owner asked for committed evidence.
