# Phase 2 Current Skill Comparison

## Scope

Compared the current Wondermint installable skill surface against the Phase 2
research set:

- `research/gstack-analysis.md`
- `research/faces-skill-analysis.md`
- `research/skill-builder-video-analysis.md`

This treats the current installable surface as `SKILL.md`, `CHECK_IN.md`, and
`skills/`.

## Current Read

The current skill has already adopted the highest-value Phase 2 patterns:

- `SKILL.md` is a router, not a full endpoint inventory.
- Guided flows live under `skills/flows/` and use phase-based execution.
- Read-only tasks are separated from public, publishing, billing, and account
  mutations through approval gates.
- Repo-only research, evals, backend inventory, and workflows are outside the
  installable skill surface.
- `repo-workflows/validate.py` gives deterministic checks before heavier dry or
  live evals.
- Trigger coverage includes positive and negative prompt space.

## Useful Gaps Found

### 1. Root action mode classification

G Stack's report-only versus mutating-mode split is present in individual files,
but the root skill did not force the agent to classify a request before acting.
Adding a compact operating-mode table makes the first decision explicit:
read-only, public/user-visible, publishing/account mutation, or billing.

### 2. Root plan detail duplication

The root skill repeated pricing and plan-limit details that also live in
`skills/account.md`, `skills/frontend.md`, and `skills/flows/upgrade.md`. Recent
plan-copy updates already showed the stale-data risk. The root should retain
only stable routing facts: plan names, checkout plan codes, billing approval
gate, and where to read current plan details.

### 3. Frontmatter compatibility

The Phase 2 sources and skill-builder transcript both point to minimal
frontmatter for Codex-first compatibility: `name` and `description`. The
previous root `updated` field was harmless, but not required for skill
discovery. Repo history and tags are a better provenance mechanism.

### 4. Description budget validation

G Stack's validator checks frontmatter compatibility and description budget.
Wondermint already had root-frontmatter validation, but it did not enforce the
1024-character description limit called out by the research.

## Implemented In This Pass

- Removed the nonessential `updated` root-frontmatter field from `SKILL.md`.
- Added `SKILL.md` operating modes for read-only, public/user-visible,
  publishing/account mutation, and billing tasks.
- Replaced the duplicated root plan table with routing to the account and
  upgrade guidance.
- Updated `repo-workflows/validate.py` to enforce the 1024-character root
  description budget.
- Updated `repo-workflows/validation.md` to document that check.

## Deferred Ideas

These are useful but not urgent:

- Add with-skill versus without-skill dry evals for the highest-risk prompts.
- Add `evals/runs.jsonl` only after more evals reveal stable fields worth
  tracking.
- Add mermaid-style protocol diagrams only for flows that become genuinely
  branch-heavy, such as onboarding or upload review recovery.
- Add templates only after repeated boilerplate creates maintenance pain across
  several flow files.
- Revisit nested support-file frontmatter when the final install/distribution
  packaging model is chosen.
