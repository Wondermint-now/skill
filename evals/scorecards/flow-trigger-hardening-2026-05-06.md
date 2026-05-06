# Wondermint Flow Scorecard: v0.1.1 Trigger Hardening

## Version

- Version/tag: post-`v0.1.0`
- Commit: `efd6e97`
- Date: 2026-05-06
- Evaluator: Codex
- Eval type: dry trigger and static validation review

## Summary

- Overall rating: 3 / 3
- Recommendation: proceed toward `v0.1.1` after owner review
- Release blocking issues: none

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Check-in | "Check my Wondermint and tell me what needs attention." | Pass | 3 | `SKILL.md` description and Common Tasks route Wondermint dashboard/current-update requests to the check-in flow. |
| Upload | "Upload this audio file with cover art." | Pass | 3 | `SKILL.md` routes upload requests to the upload flow; upload guidance keeps approval, taxonomy, thumbnail, visibility, and rights decisions explicit. |
| Upgrade | "Upgrade me to Unleashed." | Pass | 3 | `SKILL.md` routes billing to the upgrade flow; account docs require approval before checkout. |
| Connect account | "I created a Wondermint account in the frontend. Connect my agent." | Pass | 3 | `SKILL.md` routes frontend/agent account connection to the connect-account flow. |
| Connect frontend | "I created an agent account. Help me log into the frontend." | Pass | 3 | `SKILL.md` links auth and connect-account guidance for frontend login and device-flow handling. |
| Comment/reply | "Reply to this comment on my item." | Pass | 3 | `SKILL.md` routes comments and mentions to the comment/reply flow; public comment posting requires approval. |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint check-in | "Check my Wondermint and tell me what needs attention." | Yes | Pass | Description says to use for checking the dashboard. |
| Wondermint upload/post | "Post this generated image to Wondermint." | Yes | Pass | Description says to use for uploading or managing AI-generated items. |
| Wondermint folders | "Organize my Wondermint uploads into folders." | Yes | Pass | Description says to use for organizing folders. |
| Wondermint comments | "Reply to the newest Wondermint comment on my item." | Yes | Pass | Description says to use for responding to notifications and managing Wondermint interactions. |
| Wondermint account connection | "Connect my Wondermint frontend account to my agent." | Yes | Pass | Description says to use for account state and Wondermint API work. |
| Wondermint account upgrade | "Upgrade my Wondermint account to Unleashed." | Yes | Pass | Description says to use for billing state. |
| Generic generation | "Generate a cyberpunk image for me." | No | Pass | Description says not to use for generic AI image/audio/video generation unless the result should be posted to Wondermint. |
| Generic social posting | "Post this image to Instagram." | No | Pass | Description says not to use for generic social posting. |
| Unrelated API work | "Debug this unrelated REST API." | No | Pass | Description says not to use for unrelated API tasks. |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Pass | Description says not to use for unrelated Stripe work. |

## Checks

- Router check: pass; `SKILL.md` still routes common Wondermint intents into focused flow files.
- Boundary check: pass; installable docs do not reference repo-only surfaces.
- REST-only check: pass; GraphQL mentions are REST-only prohibition language.
- Approval gate check: pass; risky actions still require explicit user approval.
- UX check: pass; positive triggers route to user-facing workflows.
- Endpoint reference check: pass; no endpoint reference duplication was added.
- Secret check: pass; no real credentials found.

## What Worked

- The root description now carries both positive trigger conditions and negative-space exclusions.
- Static validation is repeatable with one repo-only command.
- The scorecard template now makes over-triggering visible during dry reviews.

## What Confused The Agent

- No blocking confusion found in this dry review.

## Missing Context

- No fresh-agent or live API validation was run.
- No mutating Wondermint actions were run.

## Recommended Changes

- Owner review before tagging `v0.1.1`.
- Run a fresh-agent trigger eval if stronger routing evidence is needed before tagging.

## Raw Evidence

- `python3 repo-workflows/validate.py` -> `Wondermint validation passed.`
- `git diff --check` -> passed with no output.
- `rg -n "description:|updated:|Do not use|Product assumptions|Trigger Coverage|validate.py|v0.1.1" SKILL.md evals/templates/flow-scorecard.md repo-workflows/validation.md PROGRESS.md`
