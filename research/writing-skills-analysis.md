# Writing Skills Reference Analysis

## Source

User-provided "Writing Skills" process note covering requirements gathering,
skill folder structure, `SKILL.md` frontmatter, description-writing rules,
script-selection criteria, file-splitting criteria, and a review checklist.

## What It Adds

Most of the source reinforces patterns already captured in the skill-builder,
G Stack, Faces, and Skills-at-Scale research:

- `SKILL.md` is the required entrypoint.
- The frontmatter description is routing metadata, not general documentation.
- Supporting files and scripts should be added only when they reduce loaded
  context or make repeated deterministic operations more reliable.
- Review should check trigger clarity, stale information, terminology, and
  concrete examples.

The main useful addition is that it compresses those ideas into a practical
authoring checklist for new or changed skill files.

## Useful Patterns For This Repo

### 1. Requirements Before Skill Changes

The source starts with explicit requirements questions:

- What task or domain does the skill cover?
- Which concrete use cases should it handle?
- Does it need scripts or only instructions?
- Are there reference materials to include?

Wondermint already has domain scope in `references/mvp-scope.md`, but this
checklist is useful before adding any new user-facing flow. It should prevent
scope creep into marketplace transactions, analytics, generic generation, or
unrelated Stripe/API work.

Recommended adoption: add these questions mentally to future flow work, but do
not copy them into the installable skill. For this repo, they belong in
`repo-workflows/iteration.md` if the workflow needs a stronger intake step.

### 2. Description Budget And Trigger Shape

The source repeats two constraints that already match this repo:

- Keep descriptions under 1024 characters.
- Write descriptions in third person with a concrete "Use when..." trigger.

Wondermint's root description already follows this pattern and
`repo-workflows/validate.py` already enforces the 1024-character budget. The
most actionable extension is to keep applying the same standard to focused
skill files under `skills/`, not only the root `SKILL.md`.

Recommended adoption: when adding or editing any frontmatter description,
verify that it names user verbs, product nouns, and plausible negative trigger
space where needed.

### 3. Scripts Only For Deterministic Repetition

The source gives a clean rule for scripts:

- add scripts for deterministic validation, formatting, repeated operations, or
  explicit error handling;
- do not add scripts just to encode prose workflows.

This fits the current repo. `repo-workflows/validate.py` is valuable because it
performs deterministic checks that would otherwise be repeated manually. The
same bar should apply to any future scripts.

Recommended adoption: future scripts should live in repo workflow space unless
they are truly part of the installable Wondermint skill package. Do not add
host-specific or credential-printing scripts to the installable surface without
separate security review.

### 4. File Splitting Heuristic

The source suggests splitting files when:

- `SKILL.md` exceeds 100 lines;
- content has distinct domains;
- advanced material is rarely needed.

The exact 100-line threshold is useful as a warning, not a hard rule. The
current Wondermint root skill is intentionally above that size because it
contains security, operating-mode gates, routing, and high-risk platform rules.
The better Wondermint-specific rule remains: keep root `SKILL.md` as a router
plus the safety rules that must be loaded every time, and move details into
focused installable files.

Recommended adoption: use "100 lines" as a review prompt for new flow files.
If a flow grows because of endpoint fields, examples, or uncommon recovery
paths, split those details into a focused reference section or file.

### 5. Review Checklist

The source review checklist is small and useful:

- description includes "Use when..." triggers;
- `SKILL.md` stays compact;
- no time-sensitive info;
- terminology is consistent;
- concrete examples are included;
- references are shallow.

This maps well to Wondermint's existing validation workflow. The only nuance is
that Wondermint necessarily includes time-sensitive product facts such as plan
names, limits, and frontend URLs. Those facts should remain marked as current
assumptions and revalidated through scorecards, live observations, or owner
input when they matter.

Recommended adoption: fold the checklist into manual review, especially for
new flow files and package-readiness checks.

## What Not To Adopt Blindly

- Do not impose a hard 100-line limit on the current root skill while it still
  needs always-loaded security and approval-gate context.
- Do not add `REFERENCE.md` or `EXAMPLES.md` generically. Wondermint already
  uses domain-specific files under `skills/`, `skills/flows/`, and
  `skills/references/`.
- Do not copy generic skill-authoring instructions into installable Wondermint
  files. They are repo-development process, not user-facing product behavior.
- Do not add scripts unless they pass the deterministic-repetition bar and avoid
  logging credentials.

## Net Recommendation

This source is useful as a lightweight authoring and review checklist, not as a
new Wondermint runtime capability. The repo has already adopted the core model:
frontmatter routing, progressive disclosure, deterministic validation, and
repo/installable boundary separation.

The only near-term repo change worth considering is tightening
`repo-workflows/iteration.md` with an intake step for new skill-flow work:
define the task/domain, concrete use cases, script need, reference materials,
and success condition before editing installable files.
