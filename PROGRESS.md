# Progress

## Current State

- Imported Wondermint skill files exist in this repo.
- The active skill entrypoint is `SKILL.md`.
- Supporting skill files live under `skills/`.
- The check-in workflow lives in `CHECK_IN.md`.

## Current Branch

`chore/initial-skill-files`

## Versioning Policy

Future skill versions should use git tags in the `v0.x.y` format.

Do not create a version tag until there is a matching scorecard in `evals/scorecards/` or the owner explicitly asks for the tag.

## Current Phase

Phase 1: repo foundation.

This phase adds repo operating docs, credential safety files, and future evaluation-recording structure. It does not restructure the skill and does not run Wondermint tests.

## Latest Evaluation

- Live eval recorded: `evals/scorecards/live-2026-05-05.md`
- Raw live evidence: `evals/logs/live-2026-05-05/`
- Overall rating: 2 / 3
- Live Wondermint tests: registration, profile, check-in, notifications, categories, browse, and item detail
- Not tested: upload, comment, like, follow, frontend login
- Main finding: Python's default HTTP client was blocked by Cloudflare 1010, but `curl` succeeded

## Next Phase

Phase 3: progressive-disclosure restructure.

Phase 2 G stack analysis has been recorded in `research/gstack-analysis.md`.

Recommended next work:

- Define the installable skill package boundary.
- Add `skills/flows/`.
- Start with `live-eval.md` and `upload.md`.
- Update `SKILL.md` only enough to route agents to the new flow files.

## Phase 2 Findings

- G stack treats skills as executable workflows with phases, gates, outputs, and follow-up recommendations.
- Wondermint should separate read-only flows from mutating or publishing flows.
- Upload, comments, follows, password changes, and API key rotation need explicit approval gates.
- Future evals should keep scorecards plus raw evidence, matching the repo's current `evals/` structure.
- The live-eval pitfall from 2026-05-05 should become skill guidance: Python's default HTTP client was blocked by Cloudflare 1010, while `curl` succeeded.

## Open Questions

- Whether the current imported skill should become the first tagged baseline version.
- Whether UX flow files should live under `skills/flows/` or another folder inside the skill structure.
- Which Wondermint scenarios should be used first when evaluation begins.
