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
- Frontend navigation research lives in `references/frontend/navigation-map.md`.
- Frontend create/upload form research lives in `references/frontend/create-upload.md`.
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
- Frontend navigation Q&A dry validation is recorded in `evals/scorecards/flow-frontend-navigation-qa-2026-05-06.md`.
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
- Frontend research update: public release frontend navigation was mapped for home, onboarding, invitation, feed category routes, item detail, creator profile, and login/create redirects. Authenticated dashboard/upload/billing/private-item surfaces still need an approved logged-in pass.
- Frontend navigation Q&A finding: current guidance answers common frontend location questions using visible labels such as My Items, My Portfolios, Library, Playlists, Settings, Billing, Password, Notifications, and `+ Create`; no blocking wording gaps found.
- Frontend plan/FAQ update: owner-provided plan comparison and FAQ copy has been recorded; installable guidance now includes visible yearly plan pricing, analytics-credit amounts, active portfolio/playlist/private/identity features, FAQ answers, and the rule not to treat coming-soon marketplace/trade/analytics copy as MVP action guidance.
- Plan/FAQ dry validation is recorded in `evals/scorecards/flow-plan-faq-dry-2026-05-06.md`; it found and fixed stale root plan prices plus an FAQ caveat for coming-soon marketplace transactions.
- Frontend create/upload update: owner-provided screenshots of the create form have been recorded. Installable guidance now explains the Create page labels, category-specific model choices, "Pick 3" descriptor behavior, custom `Other` model names, and the mapping from frontend `License*` choices to REST `contract_type`.
- Create/upload dry validation is recorded in `evals/scorecards/flow-create-upload-dry-2026-05-06.md`; it passed image, video custom-model, audio thumbnail, edit-lock, taxonomy, and visibility/license separation scenarios with no blockers.
- Frontend create form FAQ has been added to `skills/frontend.md` for Public Domain, Non-Exclusive Contract, visibility versus rights, Pick 3 descriptors, Other model names, edit-lock review, and audio thumbnails.
- Create-form FAQ dry validation is recorded in `evals/scorecards/flow-create-form-faq-dry-2026-05-06.md`; it passed the focused FAQ scenarios with no blockers.
- ZIP uploads have moved post-MVP. Current installable skill guidance supports Image, Video, and Audio uploads only; ZIP/asset bundle upload requests should be declined as out of current scope.
- ZIP post-MVP fresh-agent dry validation is recorded in `evals/scorecards/flow-fresh-agent-zip-post-mvp-2026-05-06.md`; it passed with no blockers and removed one stale "file bundle" wording issue from the comment/reply flow.
- ZIP post-MVP read-only live validation is recorded in `evals/scorecards/live-zip-post-mvp-2026-05-06.md`; live REST responses still expose Zip in categories and browse filters, but the MVP skill remains scoped to Image, Video, and Audio uploads only.
- Root token-efficiency dry validation is recorded in `evals/scorecards/flow-root-token-efficiency-dry-2026-05-06.md`; root `SKILL.md` was reduced from 203 lines / 1,768 words to 144 lines / 1,152 words while preserving core routing and approval gates.
- Tightened-root fresh-agent dry validation is recorded in `evals/scorecards/flow-tightened-root-fresh-agent-dry-2026-05-06.md`; it passed check-in, upload, upgrade, account connection, frontend login, comment/reply, folder-cap recovery, ZIP scope, and negative trigger scenarios with no blockers.
- With-skill versus without-skill comparison is recorded in `evals/scorecards/flow-with-without-skill-comparison-2026-05-06.md`; it found the skill materially improves routing, approval gates, account-linking decisions, folder-cap recovery, ZIP-scope handling, and product-specific upload metadata behavior versus a generic baseline.
- Package readiness review is recorded in `evals/scorecards/package-readiness-2026-05-06.md`; the repo package surface is clean, but the local installed skill under `$HOME/.codex/skills/wondermint` is stale and should be synced only after explicit owner approval.
- Agentic Dashboard, billing interval, and rate-limit dry validation is
  recorded in
  `evals/scorecards/flow-agentic-dashboard-billing-ratelimits-2026-05-09.md`;
  it distinguishes the Home / Check-In / Updates endpoint from the frontend
  Agentic Dashboard UI, keeps yearly checkout on the frontend until REST
  interval support is confirmed, and adds Free/Unleashed rate-limit workflow
  guidance.
- Release-account observation cleanup is recorded in
  `evals/logs/release-account-2026-05-08/` and
  `evals/scorecards/release-account-2026-05-08.md`; local paths were redacted,
  oversized marketplace evidence was compacted, and the resulting skill docs
  now cover folder-save `201`, folder contents without nested listing IDs,
  unknown processing failures, and frontend Agentic Dashboard queue wording.
- Upgrade-benefits dry validation is recorded in
  `evals/scorecards/flow-upgrade-benefits-dry-2026-05-09.md`; it passed
  private-asset, portfolio/feed/playlist cap, rate-limit, avatar/subscriber
  title, founder identity, billing interval, Agentic Dashboard terminology, and
  API-key save-handling scenarios with no blockers.
- Package-readiness checks for the current installable surface passed: the
  `.tmp/package-readiness/wondermint.skill` artifact contains only `SKILL.md`,
  `CHECK_IN.md`, and `skills/`, with no repo-only references or excluded files.
  The local installed skill under `$HOME/.codex/skills/wondermint` still has
  expected drift and was not synced.
- Local installed skill sync completed after owner approval. The installed copy
  at `$HOME/.codex/skills/wondermint` now matches the validated
  `.tmp/package-readiness/wondermint` package surface.
- Dashboard onboarding update: installable docs now name
  `https://wondermint.now/dashboard` as the frontend Agentic Dashboard URL and
  the onboarding flow explains both the dashboard and `GET /api/v1/agents/home`
  before the first check-in. The local installed skill was rebuilt and synced
  after validation.

## Next Phase

Phase 3: progressive-disclosure restructure.

Phase 2 G stack analysis has been recorded in `research/gstack-analysis.md`.
Faces skill analysis has been recorded in `research/faces-skill-analysis.md`.
Skill builder video analysis has been recorded in `research/skill-builder-video-analysis.md`.
Current skill comparison against Phase 2 research has been recorded in `research/phase-2-current-skill-comparison.md`.

Recommended next work:

- Emphasize the importance of saving the user's Wondermint API key safely after
  creation, including clear guidance that keys should be kept in `.env` or the
  user's password manager and never pasted into shared docs, logs, or committed
  files.
- Explore the "skill file" promotional-service idea next; confirm whether this
  means the skill file/package itself or a separate promotional asset/service
  before changing installable guidance.
- Clarification received: the promotional-service idea means paid-plan guidance
  inside the skill should clearly explain when Free-tier limits or paid features
  make upgrading useful, including private assets, portfolio/feed/playlist caps,
  rate limits, avatar display, subscriber titles, founder badges, and identity
  presentation benefits.
- Upgrade-benefits guidance has been updated, dry validated, package checked,
  and synced to the local installed skill after owner approval.
- Incorporate the agentic dashboard into the next workstream alongside API-key
  save guidance and the promotional-service exploration.
- Keep "Agentic Dashboard" reserved for the frontend UI where users observe
  agent behavior and queued infinite-feed content. Use home, check-in, updates,
  or platform updates for `GET /api/v1/agents/home`.
- Defer live Free/Unleashed rate-limit tests until the owner explicitly
  approves a bounded live test pass.
- Keep repo-development workflows in `repo-workflows/`.
- Keep `skills/flows/` reserved for user-facing Wondermint UX flows.
- Keep release-environment URLs in repo-development docs/config; installable skill docs should use `https://wondermint.now` for public frontend links.
- Continue from the new upload, check-in, upgrade, account-connection, comment/reply, discovery, folder organization, error recovery, onboarding, and category/tag selection flows toward broader flow validation.
- Use `repo-workflows/validation.md` and `evals/templates/flow-scorecard.md` for dry flow validation before live tests.
- Use `repo-workflows/validation.md`'s skill-file review checklist during the
  next release-candidate/package-readiness pass, and split large support files
  only if dry or fresh-agent evals show concrete agent failures.
- Owner review before tagging `v0.1.1`; optionally run a fresh-agent trigger eval for stronger routing evidence.
- Update `SKILL.md` only enough to route agents to user-facing flow files.
- Use `references/backend-endpoints/` as the source-derived API reference when updating existing endpoint docs.
- When running tests, update `live-observations.md` and the scorecard's endpoint-reference section before committing.
- Do not add marketplace transaction or marketplace analytics endpoints to the MVP skill unless the owner explicitly asks.
- Do not add GraphQL operations, queries, mutations, schemas, or `/graphql` examples to skill docs.
- Do not add live-eval, scorecard, release, or iteration procedures to installable skill files.
- Use `repo-workflows/package-readiness.md` before syncing the local installed
  skill package.

## Phase 2 Findings

- G stack treats skills as executable workflows with phases, gates, outputs, and follow-up recommendations.
- Wondermint should separate read-only flows from mutating or publishing flows.
- Upload, comments, follows, password changes, and API key rotation need explicit approval gates.
- Future evals should keep scorecards plus raw evidence, matching the repo's current `evals/` structure.
- The live-eval pitfall from 2026-05-05 belongs in repo workflow guidance: Python's default HTTP client was blocked by Cloudflare 1010, while `curl` succeeded.
- Second-pass G stack analysis found useful repo mechanics, but Wondermint should start smaller: define package boundaries, add lightweight validation, and avoid templates until duplication justifies them.
- Faces skill analysis found useful guided-flow patterns: posture, auth triage, reuse before creation, artifact-first workflows, and executable protocol diagrams for complex flows.
- Wondermint should borrow Faces flow design but not its multi-command topology yet. Keep one concise `SKILL.md` that routes into focused files.
- Skill builder video analysis reinforces the current progressive-disclosure shape, MCP-plus-skill division of labor, explicit positive/negative trigger evals, with-skill versus without-skill comparisons, deterministic checks before LLM-as-judge, and treating production skills like maintained code/docs.
- Writing Skills reference analysis adds a lightweight authoring checklist for future flow work: clarify task/domain, concrete use cases, script need, reference materials, and success condition before editing installable files. It reinforces the existing description budget, progressive-disclosure, deterministic-script, and shallow-reference guidance rather than adding new Wondermint runtime behavior.
- The practical Writing Skills additions are now encoded in `repo-workflows/iteration.md` as an intake step and review checks for new or expanded flow work.
- Skill-file review implementation rule: keep the current installable skill
  structure unless validation or eval evidence shows routing, comprehension, or
  context-load problems. Large support files are watch items, not automatic
  refactor targets.
- Current skill comparison found that the main Phase 2 patterns are already adopted. This pass added root operating modes, reduced duplicate root plan details, aligned root frontmatter with Codex-first `name`/`description` guidance, and added description-length validation.
- Token-efficiency pass confirmed the same direction: keep root `SKILL.md` as the trigger, safety, and routing layer; move examples, JSON envelopes, frontend observation details, and detailed workflow mechanics into focused installable files.

## Open Questions

- Whether the next live eval should include a controlled upload with an explicitly approved disposable asset.
- Which mutating Wondermint scenarios should be tested first after read-only validation.
