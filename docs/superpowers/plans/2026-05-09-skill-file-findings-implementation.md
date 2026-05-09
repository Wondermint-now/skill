# Skill File Findings Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the current skill-file review findings into durable repo workflow, targeted validation, and only evidence-backed installable skill changes.

**Architecture:** Keep runtime Wondermint behavior in `SKILL.md`, `CHECK_IN.md`, and `skills/`. Put review process, thresholds, and scorecards in `repo-workflows/` and `evals/` so agents can repeatedly evaluate the skill without loading repo-maintenance guidance into the installable package.

**Tech Stack:** Markdown workflow docs, existing `repo-workflows/validate.py`, existing scorecard templates, shell/rg static checks.

---

### Task 1: Add A Skill-File Review Checklist To Validation

**Files:**
- Modify: `/Users/ashokaji/code/fullstock/Wondermint Skill File/repo-workflows/validation.md`

- [ ] **Step 1: Add a dedicated review section**

Add this section after `## Flow Review`:

```markdown
## Skill-File Review

Use this when reviewing the installable skill surface against accumulated
research findings from `research/`.

Check:

- Root `SKILL.md` is a router plus always-loaded safety and scope rules, not a
  full endpoint inventory.
- Frontmatter descriptions include concrete `Use when...` trigger language and
  stay under the 1024-character budget.
- Positive triggers name real user verbs and product nouns.
- Negative trigger space covers plausible misroutes such as generic generation,
  unrelated social posting, unrelated Stripe work, and unrelated API work.
- Non-read-only actions route through approval gates before public,
  user-visible, durable, account-mutating, or billing actions.
- Large files are justified by task-specific loading. If a file is over 300
  lines, check whether agents are actually missing steps or loading irrelevant
  context before splitting it.
- Scripts are used only for deterministic validation, formatting, repeated
  operations, or explicit error handling.
- Repo-maintenance, eval, package-readiness, and research guidance stay out of
  `SKILL.md`, `CHECK_IN.md`, and `skills/`.

Do not split or rewrite installable files only to satisfy a line-count
heuristic. Split only when validation or eval evidence shows routing,
comprehension, or context-load problems.
```

- [ ] **Step 2: Run validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected: `Wondermint validation passed.`

- [ ] **Step 3: Commit**

```bash
git add repo-workflows/validation.md
git commit -m "chore: add skill file review checklist"
```

### Task 2: Add A Focused Scorecard For Skill-File Review

**Files:**
- Create: `/Users/ashokaji/code/fullstock/Wondermint Skill File/evals/scorecards/skill-file-review-2026-05-09.md`

- [ ] **Step 1: Create the scorecard**

Create:

```markdown
# Skill File Review - 2026-05-09

## Scope

Reviewed the installable Wondermint skill surface:

- `SKILL.md`
- `CHECK_IN.md`
- `skills/`

Compared against current research findings from:

- `research/gstack-analysis.md`
- `research/faces-skill-analysis.md`
- `research/skill-builder-video-analysis.md`
- `research/skills-at-scale-analysis.md`
- `research/writing-skills-analysis.md`

## Static Validation

Command:

```bash
python3 repo-workflows/validate.py
```

Result:

```text
Wondermint validation passed.
```

## Review Results

| Area | Result | Notes |
|---|---|---|
| Root routing | Pass | `SKILL.md` routes into focused files and keeps always-loaded safety context. |
| Description budget | Pass | Root and focused descriptions are under 1024 characters. |
| Positive triggers | Pass | Root description names check-in, dashboard, upload, discovery, social, folders, account, billing, webhooks, and API use. |
| Negative triggers | Pass | Root description excludes generic generation, generic social posting, unrelated Stripe, and unrelated API work. |
| Progressive disclosure | Pass | Common tasks route to flow/domain files instead of inlining all detail. |
| Approval gates | Pass | Non-read-only actions route through `skills/flows/confirmation-gates.md`. |
| Repo/installable boundary | Pass | No repo-only references found in installable files. |
| Deterministic scripts | Pass | Script usage remains in repo workflow validation, not runtime skill behavior. |
| Large support files | Watch | `items.md`, `social.md`, `auth.md`, and `account.md` exceed 300 lines. Do not split without eval evidence. |

## Findings

No blocking issues.

The current skill already implements the main cross-example findings:
frontmatter routing, progressive disclosure, approval gates, repo/installable
separation, and deterministic validation.

## Follow-Up

- Use the new `Skill-File Review` section in `repo-workflows/validation.md`
  during future package-readiness and release-candidate reviews.
- Add a split/refactor task only if dry or fresh-agent evals show agents are
  missing steps, loading irrelevant context, or confusing unrelated sections in
  large focused files.
```

- [ ] **Step 2: Run validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected: `Wondermint validation passed.`

- [ ] **Step 3: Commit**

```bash
git add evals/scorecards/skill-file-review-2026-05-09.md
git commit -m "chore: record skill file review"
```

### Task 3: Add Progress Notes For The Implementation Rule

**Files:**
- Modify: `/Users/ashokaji/code/fullstock/Wondermint Skill File/PROGRESS.md`

- [ ] **Step 1: Add a progress finding**

Add this bullet under `## Phase 2 Findings`:

```markdown
- Skill-file review implementation rule: keep the current installable skill
  structure unless validation or eval evidence shows routing, comprehension, or
  context-load problems. Large support files are watch items, not automatic
  refactor targets.
```

- [ ] **Step 2: Add next-work guidance**

Add this bullet under `Recommended next work`:

```markdown
- Use `repo-workflows/validation.md`'s skill-file review checklist during the
  next release-candidate/package-readiness pass, and split large support files
  only if dry or fresh-agent evals show concrete agent failures.
```

- [ ] **Step 3: Run validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected: `Wondermint validation passed.`

- [ ] **Step 4: Commit**

```bash
git add PROGRESS.md
git commit -m "chore: note skill file implementation rule"
```

### Task 4: Re-Run Package Boundary Checks Before Any Runtime Refactor

**Files:**
- No file changes unless failures are found.

- [ ] **Step 1: Run the standard validator**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected: `Wondermint validation passed.`

- [ ] **Step 2: Run repo-only reference scan**

Run:

```bash
rg -n "evals/|scorecard|live eval|repo-workflows|research/|backend-endpoints|mvp-scope|skill evaluation" SKILL.md CHECK_IN.md skills
```

Expected: no output.

- [ ] **Step 3: Run REST-only scan**

Run:

```bash
rg -n "GraphQL|graphql|/graphql|query \{|mutation \{" SKILL.md CHECK_IN.md skills
```

Expected: only REST prohibition language in `SKILL.md` and `skills/reference.md`.

- [ ] **Step 4: Decide whether runtime edits are justified**

If all checks pass and no eval evidence shows agent failure, make no runtime
skill edits.

If eval evidence identifies a concrete large-file problem, create a separate
plan for that specific split. The split plan must name:

- exact file being split
- exact user flow or endpoint group being extracted
- prompts that currently fail
- expected with-skill behavior after the split
- validation commands and scorecard location

## Self-Review

Spec coverage:

- Review findings are implemented as durable workflow checks, not loose advice.
- A scorecard captures the current review result.
- Progress records the operating rule for future work.
- Runtime skill changes are gated on eval evidence.

Placeholder scan:

- No TBD/TODO placeholders.
- Commands and expected outputs are explicit.

Type consistency:

- This plan modifies Markdown workflow, scorecard, and progress docs only.
