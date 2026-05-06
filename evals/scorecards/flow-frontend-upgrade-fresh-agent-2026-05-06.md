# Wondermint Flow Scorecard: Frontend And Upgrade Fresh-Agent Validation

## Version

- Version/tag: post-`v0.1.1`
- Commit: `766f952` plus frontend clarity wording before commit
- Date: 2026-05-06
- Evaluator: fresh-agent dry validation
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: frontend and upgrade guidance is ready for the next baseline
- Release blocking issues: none

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Upgrade | "Why should I upgrade from Free?" | Pass | 3 | Routes to upgrade/account guidance, ties reasons to rate limits, folder/portfolio caps, workflow frequency, and credits as context; approval required before checkout. |
| Upgrade and folder-cap recovery | "I hit a folder cap. What should I do?" | Pass | 3 | Explains delete/reuse or upgrade, ties Unleashed/Genesis to caps, and requires approval before checkout or folder deletion. |
| Frontend uploads | "Where do I find my uploads on the website?" | Pass | 3 | Routes to frontend knowledge base; points to profile/uploads/item management and API item listing when needed. |
| Frontend private uploads | "I uploaded privately via the agent. Where should I see it in the frontend?" | Pass | 3 | Says the frontend mirrors the API account; private items should be visible to the account but not promised in public discovery. |
| Frontend account connection | "How do I connect my frontend account to my agent?" | Pass | 3 | Routes to Connect Account Flow, protects `device_code` and API keys, and shows only user-facing codes/URLs. |
| Frontend playlists | "Where are my playlists?" | Pass | 3 | Explains folder/playlists/collections/portfolio surfaces and confirms exact visible folder name plus API type before mutation. |

## Checks

- Router check: pass; `SKILL.md` routes frontend questions to `skills/frontend.md` and upgrade questions to `skills/flows/upgrade.md`.
- Boundary check: pass; repo-development/eval language stayed out of installable skill docs.
- REST-only check: pass; GraphQL appears only as REST-only prohibition language.
- Approval gate check: pass; checkout, folder deletion, connection secrets, and public/mutating actions stay gated.
- UX check: pass; frontend guidance gives user-facing website locations plus API-backed routes.
- Secret check: pass; no real credentials introduced.

## What Worked

- The new frontend knowledge base covers website navigation without pulling repo-development procedures into the installable skill.
- Upgrade guidance avoids pushing paid plans without a concrete limit, workflow, or billing need.

## What Confused The Agent

- No blocking confusion found.

## Missing Context

- No live frontend/browser validation was run.
- Exact frontend navigation labels may need refinement after browser-based observation.

## Recommended Changes

- Optional clarity improvement from the validator was applied: private uploads should be visible to the owning account in profile/uploads/item management but not public discovery.

## Raw Evidence

- Fresh-agent dry validation: six prompts scored 3 / 3, no blockers.
- Static checks:
  - `python3 repo-workflows/validate.py`
  - installable-doc boundary scan
  - GraphQL prohibition scan
  - markdown link check
  - secret scan
  - `git diff --check`
