# Wondermint Skill Development Plan

## Summary

Use this repo to develop the Wondermint multi-folder skill file. Keep the active skill concise and useful for agents, store deeper user-facing context in referenced installable files, and keep evaluation/iteration workflows outside the installable skill surface.

## Phase 1: Repo Foundation

Create the repo operating structure:

- `START_HERE.md` for agent handoff.
- `PROGRESS.md` for current state and next work.
- `PLAN.md` for the phased roadmap.
- `.env.example` for credential variable names only.
- `.gitignore` for credentials and transient artifacts.
- `evals/` folders and templates for future test evidence.

Do not restructure skill files, tag a release, or run Wondermint tests in this phase.

## Phase 2: G Stack Analysis

Analyze `/Users/ashokaji/code/External repos/gstack`.

Capture useful patterns in `research/gstack-analysis.md`, especially:

- Skill routing and trigger design.
- Progressive disclosure.
- Workflow-style skill files.
- Validation and release discipline.
- Test and evidence capture.

Convert the useful patterns into Wondermint-specific conventions in this plan.

Adopted conventions from G stack:

- Treat Wondermint skill files as workflow instructions, not only API reference.
- Use phase-based flow files with explicit setup, action, evidence, and wrap-up sections.
- Separate read-only flows from mutating or publishing flows.
- Add approval gates before durable actions such as upload, comments, follows, password changes, and API key rotation.
- Keep scorecards and raw evidence for every eval.
- Capture operational learnings, including live-test pitfalls, in repo docs.
- Define a clean boundary between development repo files and the installable skill package.

## Phase 3: Progressive-Disclosure Restructure

Keep `SKILL.md` lean and route deeper user-facing details into focused installable files.

Move detailed explanations, FAQs, examples, API schemas, and troubleshooting into direct user-facing references from `SKILL.md`. Avoid duplicating the same information in multiple places.

Package boundary:

- Installable skill: `SKILL.md`, `CHECK_IN.md`, and `skills/`.
- Repo-development surface: `repo-workflows/`, `evals/`, `research/`,
  `references/backend-endpoints/`, `PLAN.md`, `PROGRESS.md`, and
  `START_HERE.md`.
- Do not link installable skill files to repo-only evaluation, research,
  planning, scorecard, or backend-inventory workflow docs.

Backend source reference:

- Keep source-derived endpoint inventory in `references/backend-endpoints/`.
- Use that inventory to update the current skill docs before adding new flow files.
- Treat backend source and line references as the authority when existing skill docs disagree.
- Treat `references/mvp-scope.md` as the scope gate. Backend endpoints outside
  the current skill files are out of scope for MVP unless the owner explicitly
  asks to add them.
- Use only REST endpoints when updating skill docs. GraphQL operations are
  backend-awareness material only and are out of scope for agent behavior.
- Exclude marketplace transactions and marketplace analytics from MVP skill
  expansion.

Recommended first restructure:

- Add `repo-workflows/` for live eval and iteration procedures.
- Add `skills/flows/` only for Wondermint user experience flows.
- Start the installable flow work with `skills/flows/upload.md`.
- Keep live-eval procedure and the Cloudflare/curl testing finding in
  `repo-workflows/live-eval.md`, not in `SKILL.md`.
- Add direct "read this when..." routing from `SKILL.md` only for user-facing
  Wondermint flows.
- Define the installable package boundary before moving repo-management files around.
- Add a small local validation script before introducing any generated-template system.
- Do not adopt G stack-style templates until repeated boilerplate appears across multiple flow files.

Additional pattern source: Faces skill bundle.

Use the Faces analysis in `research/faces-skill-analysis.md` to shape the
first Wondermint flow files:

- Borrow guided flow structure, auth triage, reuse-before-creation, artifact
  records, and approval gates.
- Do not copy the multi-command topology yet.
- Keep root `SKILL.md` as a concise router and put detailed flow behavior in
  directly referenced files.
- Keep evaluation and iteration procedures out of the installable skill files.
- Avoid host-specific shell interpolation or frontmatter unless it is required
  by the target install environment.

## Phase 4: UX Flow Expansion

Add guided flow files inside the larger skill structure for common Wondermint user journeys:

- first-time setup
- check-in/update
- upload
- category and tag selection
- comment/reply
- discovery and engagement
- folder organization
- error recovery

Each flow should include when to use it, what to ask the user, which API calls matter, success criteria, and what to report back.

## Phase 5: Future Evaluation Loop

When testing starts later, record results consistently:

- Save scorecards in `evals/scorecards/`.
- Save raw evidence in `evals/logs/vX.Y.Z/`.
- Follow `repo-workflows/live-eval.md` for live evaluation procedure.
- Update `PROGRESS.md` with improvements, regressions, and next recommended work.
- Confirm no GraphQL operations or `/graphql` examples were added to skill docs.
- Confirm no repo-development workflow links were added to installable skill docs.
- Use forward-testing with fresh agents when the skill becomes complex enough.
- Consider adding `evals/runs.jsonl` after more live evals so score trends can be compared mechanically.

Tests are not required during Phase 1.
