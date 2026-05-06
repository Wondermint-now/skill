# Wondermint Flow Scorecard: Category And Upload

## Version

- Version/tag: post-`v0.1.0`
- Commit: `e87f2be`
- Date: 2026-05-06
- Evaluator: Codex
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: proceed toward `v0.1.1` after owner review or a fresh-agent pass
- Release blocking issues: none

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Category selection | "Help me pick categories and tags for this cyberpunk city image before upload." | Pass | 3 | `SKILL.md` routes category requests to `skills/flows/category-selection.md`; the flow distinguishes Level 1 type, Level 2 group headings, Level 3 upload `subcategories`, and free-form upload `tags`. |
| Upload metadata | "Upload this audio file and choose the best metadata for me." | Pass | 3 | `skills/flows/upload.md` routes taxonomy work to the category flow, keeps audio cover handling explicit, and requires approval before `POST /api/v1/agents/listings`. |
| Taxonomy validation | "Use Mood and Genre / World as the subcategories." | Pass | 3 | `SKILL.md`, `skills/items.md`, `skills/discovery.md`, and `skills/flows/category-selection.md` all say Level 2 group headings must not be sent as upload `subcategories`. |
| Discovery detail handoff | "Open the first item from browse and summarize it." | Pass | 3 | `skills/discovery.md` and `skills/flows/discovery.md` now say to pass browse `listing_id` into `GET /api/v1/agents/marketplace/:id`; browse responses do not expose a generic item `id`. |

## Score Guide

- `0`: wrong flow, unsafe behavior, or misleading guidance.
- `1`: partially useful but needs human rescue.
- `2`: mostly correct with minor friction or missing context.
- `3`: correct flow, clear gates, useful next step, and good user-facing report.

## Checks

- Router check: pass; `SKILL.md` points category/tag requests to the new flow.
- Boundary check: pass; repo-development/eval language stayed out of installable skill docs.
- REST-only check: pass; GraphQL appears only as REST-only prohibition language.
- Approval gate check: pass; upload still requires explicit approval before listing creation.
- UX check: pass; the category flow gives a clear draft shape and approval step.
- Endpoint reference check: pass; the new flow links to detailed item/category references instead of duplicating the full taxonomy.
- Secret check: pass; no real credentials introduced.

## What Worked

- The category flow is short enough to act as a user-facing decision guide.
- The upload flow now has a clear place to route metadata/category decisions.
- The live-eval `listing_id` observation is reflected where agents need it for browse-to-detail handoff.

## What Confused The Agent

- No blocking confusion found in this dry review.

## Missing Context

- No fresh-agent validation was run in this pass.
- No live upload or mutating API call was run.
- The exact best category choices still depend on the specific asset or user description.

## Recommended Changes

- Run a fresh-agent dry validation if we want stronger evidence before tagging `v0.1.1`.
- Run a controlled live upload eval only after explicit approval for the specific disposable asset and public/private settings.

## Raw Evidence

- `rg -n "Category And Tag Selection Flow|listing_id|generic item \`id\`|subcategories|Level 3|tags" SKILL.md skills/flows/category-selection.md skills/flows/upload.md skills/flows/discovery.md skills/discovery.md skills/items.md`
- `rg -n "evals/|scorecard|live eval|repo-workflows|research/|backend-endpoints|mvp-scope|skill evaluation|fresh-agent|dry validation|staging|launch|release|MVP" SKILL.md CHECK_IN.md skills`
- `rg -n "GraphQL|graphql|/graphql|query \\{|mutation \\{" SKILL.md CHECK_IN.md skills`
- Markdown link check across 54 markdown files.
- Secret scan found only documented scan-command examples.
- `git diff --check`
