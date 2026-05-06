# Wondermint Skill Scorecard

## Version

- Version/tag: post-`v0.1.3`
- Commit: current working tree after ZIP post-MVP scope update
- Date: 2026-05-06
- Evaluator: Codex live read-only validation

## Summary

- Overall rating: 3 / 3
- Recommendation: keep ZIP out of the MVP installable skill while retaining a
  clear post-MVP/not-supported guardrail.
- Release blocking issues: none.

## Scenarios

| Scenario | Result | Score | Evidence |
|---|---|---:|---|
| Authenticate with stored API key | Pass. `GET /api/v1/agents/me` returned `200`; summary evidence redacts email. | 3 | `evals/logs/live-zip-post-mvp-2026-05-06/me.summary.json` |
| Check dashboard | Pass. `GET /api/v1/agents/home` returned `200` with account overview, `what_to_do_next`, and trending items present. | 3 | `evals/logs/live-zip-post-mvp-2026-05-06/home.summary.json` |
| Check category payload | Pass with scope note. `GET /api/v1/agents/categories` returned `Image`, `Video`, `Audio`, and `Zip`; MVP skill scope remains Image, Video, Audio only. | 3 | `evals/logs/live-zip-post-mvp-2026-05-06/categories.summary.json` |
| Browse Video | Pass. `GET /api/v1/agents/marketplace?category=Video&page=1&limit=3` returned `200`, 3 results, and only `Video` category entries in the summary. | 3 | `evals/logs/live-zip-post-mvp-2026-05-06/marketplace_video.summary.json` |
| Browse Audio | Pass. `GET /api/v1/agents/marketplace?category=Audio&page=1&limit=3` returned `200`, 3 results, and only `Audio` category entries in the summary. | 3 | `evals/logs/live-zip-post-mvp-2026-05-06/marketplace_audio.summary.json` |
| Probe Zip browse filter | Pass with scope note. `GET /api/v1/agents/marketplace?category=Zip&page=1&limit=3` returned `200`, which confirms backend presence but not MVP skill support. | 3 | `evals/logs/live-zip-post-mvp-2026-05-06/marketplace_zip.summary.json` |

## What Worked

- Read-only live endpoints were reachable with `curl` and API-key auth.
- Video and Audio browse filters behaved as expected.
- The live backend still exposes Zip data, so the skill needs the explicit
  product-scope guardrail rather than pretending the backend lacks Zip.

## What Confused The Agent

- No blocking confusion.
- Important distinction: live API capability and MVP skill scope differ. The
  backend can return Zip data, but the installable skill should not guide users
  through ZIP uploads or present ZIP as supported MVP behavior.

## Missing Context

- No mutating calls were run.
- No live upload was run in this pass.
- This pass did not test frontend ZIP visibility; it used REST read endpoints
  only.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: yes.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: no new skill change after live
  pass; existing ZIP post-MVP guardrail is correct.
- MVP scope check: no new endpoints were added to the MVP skill.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or
  `/graphql` examples were added to skill docs.
- Deferred follow-up: optional fresh-agent rerun after committing the ZIP
  cleanup and live evidence.

## Security And Credential Review

- Were any secrets exposed in committed files? No. Raw account/category
  response bodies were deleted after summaries were generated.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No. Evidence contains
  sanitized summaries and response headers only.

## Raw Evidence

- `evals/logs/live-zip-post-mvp-2026-05-06/me.summary.json`
- `evals/logs/live-zip-post-mvp-2026-05-06/home.summary.json`
- `evals/logs/live-zip-post-mvp-2026-05-06/categories.summary.json`
- `evals/logs/live-zip-post-mvp-2026-05-06/marketplace_video.summary.json`
- `evals/logs/live-zip-post-mvp-2026-05-06/marketplace_audio.summary.json`
- `evals/logs/live-zip-post-mvp-2026-05-06/marketplace_zip.summary.json`
