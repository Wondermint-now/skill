# Fresh-Agent Flow Scorecard: Baseline Ready

## Version

- Version/tag: untagged
- Commit: recorded in the commit that adds this scorecard
- Date: 2026-05-06
- Evaluator: Codex with fresh-agent dry validation

## Summary

- Overall rating: 3 / 3
- Recommendation: baseline-ready from dry validation
- Release blocking issues: none

## Scenarios

| Scenario | Result | Score | Evidence |
|---|---|---:|---|
| Check in via dashboard | Pass | 3 | Routes to `GET /api/v1/agents/home`, follows `what_to_do_next`, cross-checks notifications, and preserves approval gates. |
| Upload item | Pass | 3 | Covers audio cover art, metadata approval, create/upload/thumbnail/confirm/status, `REVIEW_ACK_REQUIRED`, and orphan cleanup approval. |
| Upgrade plan | Pass | 3 | Uses current plan names Free, Unleashed, Genesis; checks current plan and requires approval before Stripe checkout. |
| Connect frontend account to agent | Pass | 3 | Uses same email, displays only user-facing approval values, keeps `device_code` private, and polls at the server interval. |
| Connect agent account to frontend | Pass | 3 | Confirms email, defaults to magic link, and gates password setup behind explicit user choice. |
| Respond to comments | Pass | 3 | Reads item/thread first, asks for item/comment details when ambiguous, drafts specific text, and requires approval before public posting or marking read. |
| Organize public portfolio | Pass | 3 | Clarifies "best," filters published images, uses concrete candidate signals including listing metrics, and gates public folder changes. |
| Handle folder-cap error | Pass | 3 | Reads `details` and `next.options[]`, explains delete/reuse/upgrade options, and requires approval before delete, reuse, item movement, or checkout. |
| First-time onboarding | Pass | 3 | Handles no account, frontend-first, and agent-first paths; registration approval requires only email, username, and API-key handling confirmation. |
| Processing timeout recovery | Pass | 3 | Reprocess wording requires explicit approval before `POST /api/v1/agents/listings/:id/reprocess`. |
| Like, save, follow toggles | Pass | 3 | Endpoint-local wording requires approval before action or undo, with current-state inspection where available. |

## What Worked

- The installable skill docs now route common user intents into focused flows without exposing repo-development procedures.
- Approval gates are repeated near high-risk local actions, not only in global safety sections.
- Fresh-agent validation found no release-blocking issues after the final wording polish.

## What Confused The Agent

- No remaining blockers. Earlier ambiguity around "this comment" was fixed by requiring item/comment details when the comment cannot be resolved from chat, dashboard, or notification context.

## Missing Context

- Live behavior for upload, comments, follows, frontend login, and billing remains untested in this pass.
- Future live evals should confirm actual response shapes before expanding endpoint references.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: none; dry validation only.
- Static endpoint/schema/message docs updated: none beyond installable wording polish.
- Skill docs updated from confirmed behavior: approval wording for comment resolution, reprocess recovery, and like/save/follow toggles.
- MVP scope check: no new endpoints added.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or `/graphql` examples added to skill docs.
- Deferred follow-up: confirm live response shapes during the next approved live eval.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No.

## Raw Evidence

- Static checks passed:
  - installable-doc boundary scan returned no matches.
  - GraphQL scan found only REST-only prohibition language.
  - secret scan found only documented scan-command examples.
  - markdown link check resolved all 51 markdown files.
  - `git diff --check` passed.
- Fresh-agent scenario validation: 8 of 9 original scenarios scored 3 / 3; comment reply scored 2 / 3 before ambiguity wording was patched.
- Fresh-agent safety validation: no release-blocking findings; two non-blocking approval-wording issues were patched.
- Focused fresh-agent validation after patch: pass, no blockers.
