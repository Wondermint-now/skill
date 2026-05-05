# Wondermint Skill Development Plan

## Summary

Use this repo to develop the Wondermint multi-folder skill file. Keep the active skill concise and useful for agents, store deeper context in referenced files, and record future evaluation evidence without requiring tests during setup.

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

Keep `SKILL.md` lean and route deeper details into focused referenced files.

Move detailed explanations, FAQs, examples, API schemas, and troubleshooting into direct references from `SKILL.md`. Avoid duplicating the same information in multiple places.

Recommended first restructure:

- Add `skills/flows/`.
- Start with `skills/flows/live-eval.md` and `skills/flows/upload.md`.
- Add direct "read this when..." routing from `SKILL.md`.
- Add the live-eval finding that Python's default HTTP client may be blocked by Cloudflare 1010 and `curl` worked in the 2026-05-05 test.

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
- Update `PROGRESS.md` with improvements, regressions, and next recommended work.
- Use forward-testing with fresh agents when the skill becomes complex enough.

Tests are not required during Phase 1.
