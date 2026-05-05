# Progress

## Current State

- Imported Wondermint skill files exist in this repo.
- The active skill entrypoint is `SKILL.md`.
- Supporting skill files live under `skills/`.
- The check-in workflow lives in `CHECK_IN.md`.
- The guided check-in flow lives at `skills/flows/check-in.md`.
- The first user-facing flow lives at `skills/flows/upload.md`.
- The billing and plan upgrade flow lives at `skills/flows/upgrade.md`.
- The frontend/agent account connection flow lives at `skills/flows/connect-account.md`.
- The comment and reply flow lives at `skills/flows/comment-reply.md`.
- The discovery flow lives at `skills/flows/discovery.md`.
- The folder organization flow lives at `skills/flows/folder-organization.md`.
- The error recovery flow lives at `skills/flows/error-recovery.md`.
- The first-time onboarding flow lives at `skills/flows/onboarding.md`.
- Backend endpoint reference files live under `references/backend-endpoints/`.
- Repo-development workflows live under `repo-workflows/`.
- Live endpoint observations should be accumulated in `references/backend-endpoints/live-observations.md` after every eval.
- Dry flow validation is recorded in `evals/scorecards/flow-dry-2026-05-05.md`.
- Fresh-agent dry flow validation is recorded in `evals/scorecards/flow-fresh-agent-2026-05-05.md`.
- Post-cleanup fresh-agent dry flow validation is recorded in `evals/scorecards/flow-fresh-agent-post-cleanup-2026-05-05.md`.
- Core-flow fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-core-flows-2026-05-05.md`.
- Safety-rerun fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-safety-rerun-2026-05-05.md`.
- Registration-gate fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-registration-gate-2026-05-05.md`.
- MVP endpoint scope is recorded in `references/mvp-scope.md`; backend endpoint inventory is not scope permission.
- MVP skill docs are REST-only. GraphQL operations are backend-awareness material and must not be copied into the skill.
- Installable skill files are `SKILL.md`, `CHECK_IN.md`, and `skills/`; evaluation and iteration procedures stay outside that surface.
- Current subscription names are Free, Unleashed, and Genesis. Use plan codes `free`, `unleashed`, and `genesis` in current skill docs.
- Current frontend test URL is `https://minti-release.fullstock.ai/`; production user-facing frontend URL is `https://wondermint.now`.

## Current Branch

`chore/initial-skill-files`

## Versioning Policy

Future skill versions should use git tags in the `v0.x.y` format.

Do not create a version tag until there is a matching scorecard in `evals/scorecards/` or the owner explicitly asks for the tag.

## Current Phase

Phase 3: progressive-disclosure restructure is in progress.

The repo foundation is in place, the G stack plus Faces analyses are recorded under `research/`, and the first separation between user-facing skill flows and repo-development workflows has been added.

## Latest Evaluation

- Live eval recorded: `evals/scorecards/live-2026-05-05.md`
- Dry flow eval recorded: `evals/scorecards/flow-dry-2026-05-05.md`
- Fresh-agent dry flow eval recorded: `evals/scorecards/flow-fresh-agent-2026-05-05.md`
- Post-cleanup fresh-agent dry flow eval recorded: `evals/scorecards/flow-fresh-agent-post-cleanup-2026-05-05.md`
- Raw live evidence: `evals/logs/live-2026-05-05/`
- Overall rating: 2 / 3
- Live Wondermint tests: registration, profile, check-in, notifications, categories, browse, and item detail
- Not tested: upload, comment, like, follow, frontend login
- Main finding: Python's default HTTP client was blocked by Cloudflare 1010, but `curl` succeeded
- Latest dry-flow finding: current flows were coherent, but discovery, folder organization, onboarding, and error-recovery flows were still missing at the time of that eval
- Latest fresh-agent finding: flow selection and safety gates passed, but upgrade/billing and upload docs need cleanup to avoid leaking internal MVP/testing/staging language into user-facing responses
- Post-cleanup fresh-agent finding: tested flows scored 3 / 3 with no expected internal launch/testing/staging leakage; remaining cleanup is user-language polish and field-convention consistency
- Core-flow fresh-agent finding: scenario routing mostly passed, but direct endpoint docs still need local approval gates for compact check-in, social actions, billing, auth mutations, folders, and webhooks.
- Direct-doc safety cleanup has been applied after the core-flow eval: compact check-in, social, account/billing, auth, folders, and webhooks now carry local approval gates; device-flow URL guidance and folder "best item" selection guidance were clarified.
- Safety-rerun fresh-agent finding: prior P1 approval-gate issues are resolved, but remaining P2/P3 cleanup is needed for export references, item-management gates, notification-read consistency, folder candidate selection, onboarding registration approval, and live/eval wording in installable docs.
- Safety-rerun cleanup has been applied: export references were removed, item-management gates were added, notification-read approval was made consistent, folder candidate selection and onboarding registration approval were clarified, and live/eval wording was removed from installable item docs.
- Registration-gate fresh-agent finding: prior safety-rerun cleanup mostly passed, but direct registration paths in `SKILL.md`, `skills/auth.md`, and frontend-first account connection still need explicit approval gates before `POST /api/v1/agents/register`.

## Next Phase

Phase 3: progressive-disclosure restructure.

Phase 2 G stack analysis has been recorded in `research/gstack-analysis.md`.
Faces skill analysis has been recorded in `research/faces-skill-analysis.md`.

Recommended next work:

- Keep repo-development workflows in `repo-workflows/`.
- Keep `skills/flows/` reserved for user-facing Wondermint UX flows.
- Keep release-environment URLs in repo-development docs/config; installable skill docs should use `https://wondermint.now` for public frontend links.
- Continue from the new upload, check-in, upgrade, account-connection, comment/reply, discovery, folder organization, error recovery, and onboarding flows toward category/tag selection and broader flow validation.
- Use `repo-workflows/validation.md` and `evals/templates/flow-scorecard.md` for dry flow validation before live tests.
- Fix direct registration approval gates and rerun fresh-agent dry validation before tagging a baseline.
- Update `SKILL.md` only enough to route agents to user-facing flow files.
- Use `references/backend-endpoints/` as the source-derived API reference when updating existing endpoint docs.
- When running tests, update `live-observations.md` and the scorecard's endpoint-reference section before committing.
- Do not add marketplace transaction or marketplace analytics endpoints to the MVP skill unless the owner explicitly asks.
- Do not add GraphQL operations, queries, mutations, schemas, or `/graphql` examples to skill docs.
- Do not add live-eval, scorecard, release, or iteration procedures to installable skill files.

## Phase 2 Findings

- G stack treats skills as executable workflows with phases, gates, outputs, and follow-up recommendations.
- Wondermint should separate read-only flows from mutating or publishing flows.
- Upload, comments, follows, password changes, and API key rotation need explicit approval gates.
- Future evals should keep scorecards plus raw evidence, matching the repo's current `evals/` structure.
- The live-eval pitfall from 2026-05-05 belongs in repo workflow guidance: Python's default HTTP client was blocked by Cloudflare 1010, while `curl` succeeded.
- Second-pass G stack analysis found useful repo mechanics, but Wondermint should start smaller: define package boundaries, add lightweight validation, and avoid templates until duplication justifies them.
- Faces skill analysis found useful guided-flow patterns: posture, auth triage, reuse before creation, artifact-first workflows, and executable protocol diagrams for complex flows.
- Wondermint should borrow Faces flow design but not its multi-command topology yet. Keep one concise `SKILL.md` that routes into focused files.

## Open Questions

- Whether the current imported skill should become the first tagged baseline version.
- Which Wondermint scenarios should be used first when evaluation begins.
