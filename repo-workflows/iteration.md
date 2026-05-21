# Skill Iteration Workflow

This workflow is for developing the Wondermint skill repo. It is not part of
the installable Wondermint skill.

## Inputs

Use any of these inputs when improving the skill:

- owner feedback
- live eval scorecards
- `references/backend-endpoints/live-observations.md`
- static backend reference files
- `research/` findings
- current MVP scope rules

## Boundaries

- Keep user-facing Wondermint behavior in `wondermint/` and
  `skills/wondermint/`.
- Keep repo-development process in `repo-workflows/`, `evals/`, `research/`,
  `PLAN.md`, `PROGRESS.md`, and `START_HERE.md`.
- Do not link installable skill files to repo-only planning, scorecard,
  research, or backend-inventory files.
- Use only REST endpoints in skill docs.
- Do not add marketplace transaction, marketplace analytics, or other
  non-MVP endpoints unless the owner explicitly asks.

## Iteration Steps

1. Read `START_HERE.md`, `PROGRESS.md`, and `PLAN.md`.
2. Identify whether the change is user-facing skill behavior or repo-development
   process.
3. For a new or expanded user-facing flow, define the intake before editing:
   task/domain covered, concrete use cases, whether deterministic scripts are
   needed, reference materials to consult or cite, and the verifiable success
   condition.
4. For user-facing behavior, update the smallest relevant installable skill
   file and keep package root `SKILL.md` files as concise routers.
5. For development process, update repo docs or `repo-workflows/`, not the
   installable skill.
6. If the change comes from test evidence, update
   `references/backend-endpoints/live-observations.md` before changing user
   guidance.
7. Keep detailed API shapes and recovery notes in focused files; avoid
   duplicating long reference material in package root `SKILL.md` files.

## Review Checklist

Before committing an iteration:

- New or expanded flows have a clear task/domain, concrete use cases, script
  decision, source references, and success condition.
- Installable skill docs contain only user-facing Wondermint instructions.
- Evaluation, scorecard, release, and repo-maintenance instructions stay out of
  `wondermint/` and `skills/wondermint/`.
- Frontmatter descriptions include concrete `Use when...` trigger language and
  stay within the description budget.
- Any new script performs deterministic validation, formatting, repeated
  operations, or explicit error handling; scripts are not added just to encode
  prose workflows.
- Long or mixed-topic material is split into focused references instead of
  expanding package root `SKILL.md` files or a flow file unnecessarily.
- No real credentials were added.
- No GraphQL operations, queries, mutations, schemas, or `/graphql` examples
  were added to skill docs.
- Any new endpoint guidance is already in the current MVP skill files or was
  explicitly requested by the owner.
- `PROGRESS.md` reflects the current state when the phase or next action
  changes.
