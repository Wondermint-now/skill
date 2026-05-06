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
- The category and tag selection flow lives at `skills/flows/category-selection.md`.
- The folder organization flow lives at `skills/flows/folder-organization.md`.
- The error recovery flow lives at `skills/flows/error-recovery.md`.
- The first-time onboarding flow lives at `skills/flows/onboarding.md`.
- Frontend user guidance lives at `skills/frontend.md`.
- Backend endpoint reference files live under `references/backend-endpoints/`.
- Product terminology cleanup notes live in `references/terminology-backlog.md`.
- Repo-development workflows live under `repo-workflows/`.
- Live endpoint observations should be accumulated in `references/backend-endpoints/live-observations.md` after every eval.
- Dry flow validation is recorded in `evals/scorecards/flow-dry-2026-05-05.md`.
- Fresh-agent dry flow validation is recorded in `evals/scorecards/flow-fresh-agent-2026-05-05.md`.
- Post-cleanup fresh-agent dry flow validation is recorded in `evals/scorecards/flow-fresh-agent-post-cleanup-2026-05-05.md`.
- Core-flow fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-core-flows-2026-05-05.md`.
- Safety-rerun fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-safety-rerun-2026-05-05.md`.
- Registration-gate fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-registration-gate-2026-05-05.md`.
- Approval-final-gaps fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-approval-final-gaps-2026-05-05.md`.
- Cleanup-reference fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-cleanup-reference-2026-05-06.md`.
- No-blockers fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-no-blockers-2026-05-06.md`.
- Baseline-ready fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-baseline-ready-2026-05-06.md`.
- `v0.1.0` tags the dry-validation baseline at commit `43f7eb3`.
- Read-only live eval for `v0.1.0` is recorded in `evals/scorecards/live-2026-05-06.md`.
- Category/upload dry validation is recorded in `evals/scorecards/flow-category-upload-2026-05-06.md`.
- Private image upload live eval is recorded in `evals/scorecards/live-upload-2026-05-06.md`.
- Upload visibility/rights dry validation is recorded in `evals/scorecards/flow-upload-visibility-rights-2026-05-06.md`.
- v0.1.1 trigger hardening dry validation is recorded in `evals/scorecards/flow-trigger-hardening-2026-05-06.md`.
- Frontend/upgrade fresh-agent dry validation is recorded in `evals/scorecards/flow-frontend-upgrade-fresh-agent-2026-05-06.md`.
- `v0.1.2` tags the frontend/upgrade guidance baseline at commit `41383f9`.
- Frontend/upgrade read-only live validation is recorded in `evals/scorecards/live-frontend-upgrade-2026-05-06.md`.
- Deterministic repo validation lives at `repo-workflows/validate.py`.
- MVP endpoint scope is recorded in `references/mvp-scope.md`; backend endpoint inventory is not scope permission.
- MVP skill docs are REST-only. GraphQL operations are backend-awareness material and must not be copied into the skill.
- Installable skill files are `SKILL.md`, `CHECK_IN.md`, and `skills/`; evaluation and iteration procedures stay outside that surface.
- Current subscription names are Free, Unleashed, and Genesis. Use plan codes `free`, `unleashed`, and `genesis` in current skill docs.
- Read endpoints may return plan display names (`Free`, `Unleashed`, `Genesis`); checkout and upgrade request bodies use lowercase plan codes (`unleashed`, `genesis`).
- Current frontend test URL is `https://minti-release.fullstock.ai/`; production user-facing frontend URL is `https://wondermint.now`.
- Frontend terminology: use portfolios for things the user owns, playlists for playlist-style saved items, and feeds for saved/curated collections. Avoid "folders" and "collections" in user-facing skill responses except when quoting API paths, enum values, fields, or server messages.

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
- Approval-final-gaps fresh-agent finding: all nine user scenarios scored 3 / 3, but remaining release blockers are optional registration fields without explicit approval language and upload orphan-draft cleanup approval.
- Cleanup-reference fresh-agent finding: all nine user scenarios scored 3 / 3, but release blockers remain in quick-reference wording for orphan-draft cleanup and `REVIEW_ACK_REQUIRED` resend approval.
- No-blockers fresh-agent finding: no release-blocking findings remained, but upload failure handling and folder-cap recovery needed local wording polish before a 3 / 3 baseline scorecard.
- Baseline-ready fresh-agent finding: final focused validation passed with no blockers after polishing ambiguous comment resolution, reprocess approval, and like/save/follow toggle approval wording.
- `v0.1.0` live read-only finding: profile, home, social notifications, categories, marketplace browse, and item detail returned 200 with `curl`; no skill-doc changes were needed.
- Post-baseline doc improvement: browse/detail guidance now clarifies that marketplace browse results use `listing_id`, and category/tag selection has a focused user-facing flow.
- Category/upload dry validation finding: category selection, upload metadata routing, taxonomy validation, and browse-to-detail `listing_id` handoff passed static dry review with no blockers.
- Private image upload live finding: upload succeeded as private and reached `Minted`; `POST /listings` requires `contract_type` with allowed values `public_domain` or `non_exclusive`.
- Upload visibility/rights dry validation finding: `private` visibility and `contract_type` rights are documented as independent choices; focused fresh-agent rerun passed 3 / 3 with no blockers.
- v0.1.1 trigger hardening finding: root skill routing now has explicit positive and negative trigger space, deterministic validation passed, and trigger dry review found no blockers.
- Frontend and upgrade guidance finding: skill docs now include user-facing frontend navigation/troubleshooting guidance and practical upgrade reasons tied to rate limits, folder/portfolio caps, workflow frequency, and billing needs.
- Frontend/upgrade fresh-agent finding: six frontend and upgrade prompts scored 3 / 3 with no blockers; private-upload frontend visibility wording was tightened.
- `v0.1.2` live frontend/upgrade finding: subscription, plans, home, owned listings, folders, and private-upload status all returned `200`; plan display names were confirmed as title case in read responses, while checkout bodies remain lowercase plan codes.
- Terminology update: installable docs now translate backend folder/collection concepts into frontend terms: portfolios, playlists, and feeds. Backend wording cleanup candidates are tracked in `references/terminology-backlog.md`.

## Next Phase

Phase 3: progressive-disclosure restructure.

Phase 2 G stack analysis has been recorded in `research/gstack-analysis.md`.
Faces skill analysis has been recorded in `research/faces-skill-analysis.md`.

Recommended next work:

- Keep repo-development workflows in `repo-workflows/`.
- Keep `skills/flows/` reserved for user-facing Wondermint UX flows.
- Keep release-environment URLs in repo-development docs/config; installable skill docs should use `https://wondermint.now` for public frontend links.
- Continue from the new upload, check-in, upgrade, account-connection, comment/reply, discovery, folder organization, error recovery, onboarding, and category/tag selection flows toward broader flow validation.
- Use `repo-workflows/validation.md` and `evals/templates/flow-scorecard.md` for dry flow validation before live tests.
- Owner review before tagging `v0.1.1`; optionally run a fresh-agent trigger eval for stronger routing evidence.
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

- Whether the next live eval should include a controlled upload with an explicitly approved disposable asset.
- Which mutating Wondermint scenarios should be tested first after read-only validation.
