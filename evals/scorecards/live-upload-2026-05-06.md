# Wondermint Live Upload Scorecard

## Version

- Version/tag: post-`v0.1.0`
- Commit: `afe20de`
- Date: 2026-05-06
- Evaluator: Codex, controlled private live upload

## Summary

- Overall rating: 3 / 3 for the controlled private image upload
- Recommendation: update upload docs with the observed `contract_type` requirement before considering `v0.1.1`
- Release blocking issues: none

## Scenarios

| Scenario | Result | Score | Evidence |
|---|---|---:|---|
| Fresh-agent category/upload dry validation | Pass | 3 | Four focused prompts scored 3 / 3 with no blockers before live upload. |
| Create private image listing | Pass after correction | 3 | Initial create without `contract_type` returned 400; retry with `contract_type: "public_domain"` returned 201. Evidence: `evals/logs/live-upload-2026-05-06/create.json`. |
| Upload source file to presigned URL | Pass | 3 | PNG PUT returned 200. Evidence: `evals/logs/live-upload-2026-05-06/status.txt`. |
| Confirm upload | Pass | 3 | `POST /api/v1/agents/listings/:id/uploaded` returned 200 and status `processing`. Evidence: `evals/logs/live-upload-2026-05-06/confirm.json`. |
| Poll processing status | Pass | 3 | Status progressed `Processing` -> `Pending Minting` -> `Minted`. Evidence: `evals/logs/live-upload-2026-05-06/status_poll_*.json`. |

## Score Guide

- `0`: failed or misleading.
- `1`: partially works but needs human rescue.
- `2`: works with minor friction.
- `3`: works cleanly and gives useful user-facing guidance.

## What Worked

- The category/tag plan produced valid Level 3 `subcategories`.
- Private image listing creation, file upload, confirmation, and status polling worked after including the required contract type.
- The item reached `Minted`.

## What Confused The Agent

- `contract_type` is required for `POST /api/v1/agents/listings`; omitting it returns `400 VALIDATION_ERROR`.
- Allowed values observed in the error were `public_domain` and `non_exclusive`; `exclusive` is not accepted.

## Missing Context

- This pass did not verify public visibility, comments, likes, follows, folders, frontend rendering, or item detail after minting.
- Because the upload was private, public discovery behavior was not tested.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: yes.
- Static endpoint/schema/message docs updated: pending follow-up.
- Skill docs updated from confirmed behavior: pending follow-up; upload docs should include `contract_type`.
- MVP scope check: no new endpoint was added.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or `/graphql` examples were added.
- Deferred follow-up: add `contract_type` to user-facing upload docs and dry-validate the update.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? Saved evidence redacts signed URLs, API-key-like strings, auth fields, and email-shaped strings.

## Raw Evidence

- `evals/logs/live-upload-2026-05-06/status.txt`
- `evals/logs/live-upload-2026-05-06/summary.json`
- `evals/logs/live-upload-2026-05-06/create.json`
- `evals/logs/live-upload-2026-05-06/confirm.json`
- `evals/logs/live-upload-2026-05-06/status_poll_1.json`
- `evals/logs/live-upload-2026-05-06/status_poll_2.json`
- `evals/logs/live-upload-2026-05-06/status_poll_3.json`
- `evals/logs/live-upload-2026-05-06/status_poll_4.json`
