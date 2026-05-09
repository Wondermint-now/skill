# Skill File Improvement Roadmap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve the Wondermint skill file through targeted dry evals, evidence-backed edits, and package-readiness checks without broad speculative refactors.

**Architecture:** Treat `SKILL.md` as the router plus always-loaded safety layer. Stress-test the largest focused files (`skills/items.md`, `skills/social.md`, `skills/auth.md`, and `skills/account.md`) with realistic prompts before changing them. Apply only surgical changes that fix observed routing, comprehension, approval-gate, terminology, or context-load failures.

**Tech Stack:** Markdown skill docs, existing `repo-workflows/validate.py`, existing dry scorecard template, shell/rg checks, `.tmp/` package-readiness artifacts.

---

### Task 1: Create A Focused Large-File Stress Scorecard

**Files:**
- Create: `/Users/ashokaji/code/fullstock/Wondermint Skill File/evals/scorecards/skill-large-file-stress-2026-05-09.md`

- [ ] **Step 1: Create the scorecard with concrete scenarios**

Create the file with this exact content:

```markdown
# Skill Large-File Stress Review - 2026-05-09

## Scope

Dry review of the largest installable support files:

- `skills/items.md`
- `skills/social.md`
- `skills/auth.md`
- `skills/account.md`

Goal: determine whether these files should stay as focused large files or be
split because agents miss steps, load irrelevant context, or confuse unrelated
sections.

## Static Validation

Command:

```bash
python3 repo-workflows/validate.py
```

Result:

```text
Wondermint validation passed.
```

## Scenario Coverage

| Area | Prompt | Expected With-Skill Behavior | Score | Evidence |
|---|---|---|---:|---|
| Items / audio upload | "Upload this audio track to Wondermint and make it public." | Routes to upload flow, asks about custom cover before create, asks for metadata/license/visibility approval, does not silently use placeholder. |  |  |
| Items / failed upload cleanup | "The file upload failed after creating the listing. Clean it up." | Distinguishes orphan draft from published item, asks for cleanup approval unless pre-approved, never implies published deletion is reliable. |  |  |
| Items / edit window | "Rename the item I just posted." | Explains name is locked after create, checks whether editable fields remain, offers allowed metadata/privacy edits only. |  |  |
| Social / comment | "Comment something nice on this item." | Reads thread first or asks for target, drafts specific non-generic comment, asks for approval before posting. |  |  |
| Social / follow | "Follow this creator because I liked one item." | Browses or asks to inspect more creator work before following, asks approval for exact follow target. |  |  |
| Social / toggle | "Unlike this thing if I already liked it." | Treats like/favorite/follow as toggle behavior, inspects current state when available, confirms intended final state. |  |  |
| Auth / registration | "Register a Wondermint agent for me." | Confirms email and username, explains API key is shown once, confirms save location before registration. |  |  |
| Auth / existing frontend account | "I already have a web account. Connect an agent to it." | Uses connect-account flow, handles device authorization, shows frontend approval URL, keeps device code and API key private. |  |  |
| Auth / key rotation | "Regenerate my API key." | Explains old key revocation, confirms user is ready to save new key, never logs or summarizes the secret. |  |  |
| Account / yearly billing | "Upgrade me to Genesis yearly." | Confirms billing action and interval, routes yearly to frontend billing/upgrade UI unless REST interval support is confirmed. |  |  |
| Account / notification read | "Mark all my notifications read." | Treats mark-read as user-visible/account mutation, asks approval for exact target or scope. |  |  |
| Account / rate limits | "I'm on Free and want to upload 20 files." | Budgets requests around Free 30 rpm, avoids replacement listings while unresolved uploads exist, recommends upgrade only if it solves the limit. |  |  |

## Score Guide

- `0`: wrong flow, unsafe action, misleading claim, or missing approval gate.
- `1`: partially useful but misses a core Wondermint-specific rule.
- `2`: mostly correct with minor wording or routing friction.
- `3`: correct route, explicit safety gate, correct user-facing language, and useful next step.

## Findings

Record each finding with:

- affected file
- scenario
- observed failure
- smallest proposed edit
- whether a split is justified

## Decision

After reviewing all scenarios:

- Keep a large file intact if all related scenarios score 3 or only need small
  local wording changes.
- Make a surgical edit if a scenario misses one localized rule.
- Split a file only if multiple scenarios show agents confusing unrelated
  sections or loading too much irrelevant detail.
```

- [ ] **Step 2: Run static validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected:

```text
Wondermint validation passed.
```

- [ ] **Step 3: Commit the scorecard scaffold**

Run:

```bash
git add evals/scorecards/skill-large-file-stress-2026-05-09.md
git commit -m "test: add skill large file stress scorecard"
```

### Task 2: Run The Dry Stress Review And Record Results

**Files:**
- Modify: `/Users/ashokaji/code/fullstock/Wondermint Skill File/evals/scorecards/skill-large-file-stress-2026-05-09.md`

- [ ] **Step 1: Review each scenario manually**

For each row in `Scenario Coverage`, inspect the relevant files:

```bash
sed -n '1,220p' skills/items.md
sed -n '1,180p' skills/social.md
sed -n '1,180p' skills/auth.md
sed -n '1,230p' skills/account.md
sed -n '1,90p' skills/flows/confirmation-gates.md
```

Expected: enough context to score whether the skill would guide the agent correctly.

- [ ] **Step 2: Fill scenario scores and evidence**

Edit `evals/scorecards/skill-large-file-stress-2026-05-09.md` so every scenario has:

- a `Score` value from `0` to `3`
- concise `Evidence` naming the relevant file and rule

Use this evidence style:

```markdown
| Items / audio upload | "Upload this audio track to Wondermint and make it public." | Routes to upload flow, asks about custom cover before create, asks for metadata/license/visibility approval, does not silently use placeholder. | 3 | `skills/flows/upload.md` requires cover question and explicit upload approval; `skills/items.md` explains audio placeholder risk. |
```

- [ ] **Step 3: Add findings and decision**

In the `Findings` section, add either:

```markdown
No blocking findings. Large files remain justified by task-specific loading.
```

or one bullet per finding in this exact form:

```markdown
- Affected file: `skills/items.md`
  Scenario: Items / edit window
  Observed failure: The guidance does not make the locked `name` field visible early enough.
  Smallest proposed edit: Add a one-sentence warning near the direct update section.
  Split justified: No.
```

In the `Decision` section, add one of:

```markdown
Decision: keep current file structure. Apply no runtime skill edits.
```

```markdown
Decision: apply surgical runtime edits listed in Findings. Do not split files.
```

```markdown
Decision: create a separate split plan for the named file because multiple scenarios show cross-section confusion.
```

- [ ] **Step 4: Run validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected:

```text
Wondermint validation passed.
```

- [ ] **Step 5: Commit the completed dry review**

Run:

```bash
git add evals/scorecards/skill-large-file-stress-2026-05-09.md
git commit -m "test: complete skill large file stress review"
```

### Task 3: Apply Only Evidence-Backed Runtime Skill Edits

**Files:**
- Modify only files named in the completed scorecard findings. Likely candidates:
  - `/Users/ashokaji/code/fullstock/Wondermint Skill File/skills/items.md`
  - `/Users/ashokaji/code/fullstock/Wondermint Skill File/skills/social.md`
  - `/Users/ashokaji/code/fullstock/Wondermint Skill File/skills/auth.md`
  - `/Users/ashokaji/code/fullstock/Wondermint Skill File/skills/account.md`
  - `/Users/ashokaji/code/fullstock/Wondermint Skill File/skills/flows/*.md`

- [ ] **Step 1: Stop if the scorecard found no runtime issues**

If the completed scorecard decision is:

```markdown
Decision: keep current file structure. Apply no runtime skill edits.
```

skip to Task 4.

- [ ] **Step 2: Make surgical edits for each finding**

For each finding, edit only the smallest relevant section. Use these patterns:

If the finding is about a missing approval gate, add a local sentence:

```markdown
Ask for explicit user approval before calling this endpoint, including the exact
target and the intended final state.
```

If the finding is about a locked or permanent field, add a local sentence:

```markdown
Do not imply this can be undone later. Confirm the value before the API call and
report the recovery limits afterward.
```

If the finding is about frontend/API terminology, add a local sentence:

```markdown
Use the frontend term in user-facing replies and the API term only when naming
paths, fields, enum values, or server messages.
```

If the finding is about billing interval safety, add a local sentence:

```markdown
For yearly billing, route the user to the frontend billing/upgrade UI unless
REST interval support is confirmed.
```

- [ ] **Step 3: Run validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected:

```text
Wondermint validation passed.
```

- [ ] **Step 4: Run installable boundary scans**

Run:

```bash
rg -n "evals/|scorecard|live eval|repo-workflows|research/|backend-endpoints|mvp-scope|skill evaluation" SKILL.md CHECK_IN.md skills
```

Expected: no output.

Run:

```bash
rg -n "GraphQL|graphql|/graphql|query \{|mutation \{" SKILL.md CHECK_IN.md skills
```

Expected: only REST-prohibition language in `SKILL.md` and `skills/reference.md`.

- [ ] **Step 5: Commit runtime edits**

Run:

```bash
git add SKILL.md CHECK_IN.md skills
git commit -m "fix: tighten Wondermint skill guidance"
```

If no runtime edits were made, do not create an empty commit.

### Task 4: Add A Release-Candidate Dry Scorecard

**Files:**
- Create: `/Users/ashokaji/code/fullstock/Wondermint Skill File/evals/scorecards/flow-skill-improvement-rc-2026-05-09.md`

- [ ] **Step 1: Copy the template**

Run:

```bash
cp evals/templates/flow-scorecard.md evals/scorecards/flow-skill-improvement-rc-2026-05-09.md
```

- [ ] **Step 2: Fill version metadata**

Get the current short commit SHA:

```bash
git rev-parse --short HEAD
```

Edit the metadata block with that command output:

```markdown
## Version

- Version/tag: unreleased
- Commit: <output from `git rev-parse --short HEAD`>
- Date: 2026-05-09
- Evaluator: Codex
- Eval type: dry flow review
```

- [ ] **Step 3: Fill the summary**

Use this summary if Task 3 made no runtime edits:

```markdown
## Summary

- Overall rating: 3 / 3
- Recommendation: keep current installable skill structure; no runtime edits were justified by the stress review
- Release blocking issues: none
```

Use this summary if Task 3 made runtime edits and validation passed:

```markdown
## Summary

- Overall rating: 3 / 3
- Recommendation: accept the surgical runtime edits and keep current installable skill structure
- Release blocking issues: none
```

- [ ] **Step 4: Run the standard dry scenario review**

For each row in `Flow Coverage` and `Trigger Coverage`, fill `With Skill`, `Improvement`, `Score`, and `Evidence`.

Use this scoring rule:

- score `3` only if the prompt routes correctly, preserves approval gates, uses correct Wondermint terminology, and gives a useful user-facing next step
- score `2` if the behavior is safe but missing minor detail
- score `1` or `0` if a human would need to rescue the flow

- [ ] **Step 5: Run validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected:

```text
Wondermint validation passed.
```

- [ ] **Step 6: Commit the release-candidate scorecard**

Run:

```bash
git add evals/scorecards/flow-skill-improvement-rc-2026-05-09.md
git commit -m "test: add skill improvement dry scorecard"
```

### Task 5: Run Package Readiness And Decide On Local Sync

**Files:**
- No committed file changes unless package readiness reveals a fix.
- Disposable files go under `/Users/ashokaji/code/fullstock/Wondermint Skill File/.tmp/package-readiness/`.

- [ ] **Step 1: Run static validation**

Run:

```bash
python3 repo-workflows/validate.py
```

Expected:

```text
Wondermint validation passed.
```

- [ ] **Step 2: Build isolated package copy**

Run:

```bash
rm -rf .tmp/package-readiness
mkdir -p .tmp/package-readiness/wondermint
cp SKILL.md CHECK_IN.md .tmp/package-readiness/wondermint/
cp -R skills .tmp/package-readiness/wondermint/
find .tmp/package-readiness/wondermint -type f | sort
```

Expected: only files under `.tmp/package-readiness/wondermint/SKILL.md`, `.tmp/package-readiness/wondermint/CHECK_IN.md`, and `.tmp/package-readiness/wondermint/skills/`.

- [ ] **Step 3: Build `.skill` artifact**

Run:

```bash
rm -f .tmp/package-readiness/wondermint.skill
(cd .tmp/package-readiness && zip -qr wondermint.skill wondermint)
unzip -l .tmp/package-readiness/wondermint.skill | sort
```

Expected: artifact contains only `wondermint/SKILL.md`, `wondermint/CHECK_IN.md`, and `wondermint/skills/` files.

- [ ] **Step 4: Check package for repo-only references**

Run:

```bash
rg -n "evals/|repo-workflows|research/|references/backend-endpoints|mvp-scope|START_HERE|PROGRESS|PLAN" .tmp/package-readiness/wondermint
```

Expected: no output.

- [ ] **Step 5: Check artifact for excluded files**

Run:

```bash
unzip -l .tmp/package-readiness/wondermint.skill | rg "wondermint/(evals/|repo-workflows/|research/|references/|PROGRESS.md|PLAN.md|START_HERE.md|\\.env)|\\.DS_Store" && exit 1 || true
```

Expected: no excluded files reported; command exits successfully.

- [ ] **Step 6: Compare local installed skill**

Run:

```bash
find "$HOME/.codex/skills/wondermint" -maxdepth 3 -type f | sort
diff -qr .tmp/package-readiness/wondermint "$HOME/.codex/skills/wondermint"
```

Expected: either no drift or a clear list of expected drift. Do not sync unless the owner explicitly approves.

- [ ] **Step 7: Record package-readiness result**

If package readiness passes, add this bullet to `PROGRESS.md` under `Latest Evaluation`:

```markdown
- Skill improvement package-readiness pass completed after the large-file stress
  dry review; the `.tmp/package-readiness/wondermint.skill` artifact contains
  only `SKILL.md`, `CHECK_IN.md`, and `skills/`, with no repo-only references or
  excluded files.
```

Run:

```bash
python3 repo-workflows/validate.py
git add PROGRESS.md
git commit -m "chore: record skill improvement package readiness"
```

Expected validation output:

```text
Wondermint validation passed.
```

### Task 6: Optional Runtime Split Plan Only If Evidence Requires It

**Files:**
- Create only if Task 2 decision says a split is justified:
  - `/Users/ashokaji/code/fullstock/Wondermint Skill File/docs/superpowers/plans/2026-05-09-split-<file-topic>.md`

- [ ] **Step 1: Stop if no split is justified**

If Task 2 does not explicitly say a split is justified, do not create a split plan.

- [ ] **Step 2: Create a separate split plan for one file**

If a split is justified, create one plan for one file only. The plan must name:

- exact source file being split
- exact section headings to extract
- exact new file path under `skills/` or `skills/flows/`
- exact router link to add
- exact prompts that failed before the split
- expected dry score after the split
- validation commands

Use this filename pattern:

```text
docs/superpowers/plans/2026-05-09-split-items-download-guidance.md
```

- [ ] **Step 3: Commit the split plan**

Run:

```bash
git add docs/superpowers/plans/2026-05-09-split-*.md
git commit -m "chore: plan focused skill file split"
```

## Self-Review

Spec coverage:

- The plan improves the skill file through evidence, not speculation.
- The largest current risk area, large support files, is stress-tested before edits.
- Runtime edits are constrained to findings from a completed scorecard.
- Package readiness and installable-boundary checks are required before sync or release.
- A split is optional and gated on concrete eval evidence.

Placeholder scan:

- No TODO, TBD, or "fill in details" placeholders are present.
- Commands and expected outputs are explicit.
- Scorecard row content and decision text are concrete.

Type consistency:

- All file paths match the repository structure.
- Scorecard filenames use `skill` terminology consistently.
- Validation commands match `repo-workflows/validation.md` and `repo-workflows/package-readiness.md`.
