# Wondermint Skill Version Scorecard

## Version

- Version/tag: v0.1.7
- Variant: core
- Marketplace transactions included: no
- Commit: working tree after `5326cd2`
- Date: 2026-05-21
- Evaluator: Codex static package review
- Eval type: package readiness and repo review

## Summary

- Overall rating: 3 / 3 for static package readiness.
- Recommendation: ready to commit and tag as `core-v0.1.7` after owner review.
- Release blocking issues: none after updating validation and package-readiness
  workflow paths for the current package layout.

## Checks

| Check | Result | Evidence |
|---|---|---|
| Repo validation | Pass | `python3 repo-workflows/validate.py` |
| Package copy parity | Pass | `diff -qr wondermint skills/wondermint` returned no differences |
| Package artifact | Pass | `.tmp/package-readiness/wondermint.skill` contains only `wondermint/SKILL.md`, `wondermint/CHECK_IN.md`, and `wondermint/skills/` |
| Repo-only references | Pass | No `evals/`, `repo-workflows`, `research/`, backend inventory, progress, plan, or start-here references in `wondermint` or `skills/wondermint` |
| REST-only guard | Pass | GraphQL matches are limited to explicit REST-only prohibition language |
| Whitespace check | Pass | `git diff --check` |

## What Changed Since v0.1.6

- Added plugin distribution metadata for Codex and Cursor.
- Added the `wondermint/` package copy and kept it in sync with
  `skills/wondermint/`.
- Added fallback installer support.
- Updated production API URL guidance to `https://api.wondermint.now`.
- Clarified account setup language around web login and API-key access.
- Added rate-limit recovery guidance and validation prompts.
- Added Agentic Dashboard routing for showing items and queueing folders.
- Updated billing interval guidance for higher-plan changes and same-plan
  monthly/yearly switches.

## Notes

- No live Wondermint API tests were run for this scorecard.
- No git tag was created from this scorecard because the release state is still
  in the uncommitted working tree.
- Historical `v0.1.x` tags belong to the core line; use `core-v...` for new
  core tags.
