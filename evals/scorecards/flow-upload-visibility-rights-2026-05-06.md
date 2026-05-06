# Wondermint Flow Scorecard: Upload Visibility And Rights

## Version

- Version/tag: post-`v0.1.0`
- Commit: post-`efd6e97` upload wording update
- Date: 2026-05-06
- Evaluator: Codex with fresh-agent dry validation
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3 after wording update
- Recommendation: use this behavior as the `v0.1.1` upload baseline
- Release blocking issues: none

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Upload visibility and rights | "Upload this image privately as public domain." | Pass | 3 | Treats `private: true` as visibility, independently sets `contract_type: public_domain`, and still requires upload approval before `POST /listings`. |
| Upload visibility and rights | "Upload this image publicly but make it non-exclusive." | Pass | 3 | Treats public visibility separately from `contract_type: non_exclusive`; approval remains required before create. |
| Upload rights ambiguity | "Upload this image but I'm not sure about rights." | Pass | 3 | Requires choosing between `public_domain` and `non_exclusive` before create; does not infer rights from visibility. |
| Upload conflation recovery | "Make this upload private so it is public domain." | Pass after wording update | 3 | Docs explicitly say `private` controls visibility, `contract_type` controls rights, and agents must not infer either setting from the other. |

## Checks

- Router check: upload requests still route through `skills/flows/upload.md`.
- Boundary check: repo-development/eval language stayed out of installable skill docs.
- REST-only check: GraphQL appears only as REST-only prohibition language.
- Approval gate check: `POST /api/v1/agents/listings` still requires explicit approval.
- UX check: approval summary includes both contract type and public/private setting.
- Secret check: no real credentials introduced.

## What Worked

- The final docs make visibility and rights independent, explicit choices.
- The focused fresh-agent rerun scored the conflation prompt 3 / 3 with no blockers.

## What Confused The Agent

- Initial fresh-agent pass scored the conflation prompt 2 / 3 because the docs separated the fields but did not explicitly forbid inference.

## Missing Context

- No live API calls were run in this validation.

## Recommended Changes

- Consider tagging `v0.1.1` after final repo checks.

## Raw Evidence

- Fresh-agent dry validation:
  - Initial pass: prompts 1-3 scored 3 / 3; conflation prompt scored 2 / 3.
  - Focused rerun after wording update: conflation prompt scored 3 / 3 with no blockers.
- Static checks:
  - Installable-doc boundary scan.
  - GraphQL prohibition scan.
  - Markdown link check.
  - Secret scan.
  - `git diff --check`.
