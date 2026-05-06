# Wondermint Skill Scorecard

## Version

- Version/tag: `v0.1.2`
- Commit: `41383f9`
- Date: 2026-05-06
- Evaluator: Codex live read-only REST pass

## Summary

- Overall rating: 3 / 3 for the read-only frontend and upgrade reference pass.
- Recommendation: keep `v0.1.2` as the current frontend/upgrade baseline.
- Release blocking issues: none found in the tested read-only scope.

## Scenarios

| Scenario | Result | Score | Evidence |
|---|---|---:|---|
| Check subscription state | Pass | 3 | `GET /api/v1/agents/subscription` returned `200` with `plan`, `status`, `credits_balance`, `credits_monthly_limit`, and `current_period_end`. |
| View available plans | Pass | 3 | `GET /api/v1/agents/plans` returned `200` with Free, Unleashed, and Genesis plan entries. |
| Check frontend dashboard context | Pass | 3 | `GET /api/v1/agents/home` returned `200` with account, activity, trending, network, suggestions, and quick links. |
| Review own uploads | Pass | 3 | `GET /api/v1/agents/listings?page=1&limit=10` returned `200` and included the prior private upload. |
| Review folders/playlists state | Pass | 3 | `GET /api/v1/agents/folders` returned `200` with the current profile folder. |
| Check private upload status | Pass | 3 | `GET /api/v1/agents/listings/{listing_id}/status` returned `200` and `status: "Minted"`. |

## What Worked

- The read-only account, plan, home, listing, folder, and item-status endpoints all responded successfully.
- The prior private upload is visible to the owner through the agent listing endpoint with `private: true`.
- Plan names are confirmed as Free, Unleashed, and Genesis.

## What Confused The Agent

- Live read responses return display names such as `Free`, while checkout request bodies use lowercase plan codes such as `unleashed`.

## Missing Context

- This pass did not create checkout, open billing portal, cancel subscription, update payment methods, connect accounts, mutate folders, or upload a new asset.
- Frontend UI screens were not browser-tested; this pass only confirmed API data that supports frontend and upgrade guidance.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: yes.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: `skills/account.md` now distinguishes plan display names from checkout plan codes.
- MVP scope check: no new endpoints were added to the installable skill.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or `/graphql` examples were added to skill docs.
- Deferred follow-up: browser-based frontend validation and an explicitly approved billing-link test.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No; raw evidence was sanitized before commit.

## Raw Evidence

- `evals/logs/live-frontend-upgrade-2026-05-06/`
