# Skills At Scale Follow-Up Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the latest Skills at Scale research into targeted Wondermint skill improvements without expanding MVP API scope.

**Architecture:** Keep `SKILL.md` as the small router and add only high-value constraints or links there. Put deeper operational behavior in focused installable files under `skills/flows/`, and put evaluation/package mechanics in repo-only workflows. Do not add bang-backtick runtime interpolation until the target harnesses prove support and security behavior.

**Tech Stack:** Markdown skill files, Python static validator in `repo-workflows/validate.py`, shell-based package checks, dry scorecards in `evals/scorecards/`.

---

## Research Review Findings

Implement now:

- API key preservation needs stronger user-facing language at the exact moments keys are created or regenerated.
- The frontmatter trigger should name direct social verbs so prompts like "favorite the last image I uploaded" route reliably.
- Risky public, publishing, account, and billing actions should share one structured confirmation gate instead of repeating uneven wording across files.
- The with-skill versus no-skill baseline should become a required evaluation rule, not a one-off scorecard.
- Package readiness should produce a `.skill`-style zip artifact for non-technical creator distribution.
- The frontend Agentic Dashboard should be clearly distinguished from the REST home/check-in/updates endpoint. The endpoint supports agent decisions; the frontend UI lets the user observe agent activity and queued infinite-feed content.

Defer for now:

- Bang-backtick interpolation. It is promising for deterministic account state, but it executes on skill load, may leak assumptions across Codex/Claude Desktop/Cursor, and needs opt-in harness validation before touching installable docs.
- Transcript review automation. It is useful, but logs may contain private account data; add it only after a privacy rule and retention workflow exist.
- Bulk cleanup, cross-platform posting, and engagement-triage sibling skills. These are future skills, not additions to the current MVP Wondermint skill.

## File Structure

- Modify `SKILL.md`: add social verbs to the description, keep under the 1024-character budget, and route risky actions to the confirmation gate.
- Modify `skills/flows/onboarding.md`: make API key save handling explicit before and after registration.
- Modify `skills/flows/connect-account.md`: make one-time API key delivery and regeneration save handling explicit.
- Modify `skills/auth.md`: strengthen register, rotate, and regenerate API key save language.
- Create `skills/flows/confirmation-gates.md`: one reusable user-facing gate for public, publishing/account, and billing operations.
- Modify `skills/flows/upload.md`, `skills/flows/folder-organization.md`, `skills/flows/upgrade.md`, `skills/social.md`: point to the reusable gate where those files authorize risky actions.
- Modify `skills/flows/check-in.md`: describe the Home / Check-In / Updates endpoint as the default REST operating routine.
- Modify `repo-workflows/validation.md`: require with-skill versus no-skill comparison for any release candidate.
- Modify `evals/templates/flow-scorecard.md`: add comparison columns and pass criteria.
- Modify `repo-workflows/package-readiness.md`: build a `.skill` zip under `.tmp/` and verify its contents.
- Modify `PROGRESS.md`: record the plan and mark bang-backtick interpolation as deferred pending harness validation.

### Task 1: Tighten Root Routing And API-Key Save Guidance

**Files:**
- Modify: `SKILL.md`
- Modify: `skills/flows/onboarding.md`
- Modify: `skills/flows/connect-account.md`
- Modify: `skills/auth.md`

- [ ] **Step 1: Update the root description with direct social verbs**

Replace the `description:` line in `SKILL.md` with this text, then verify it remains under 1024 characters:

```yaml
description: Use when the user wants to interact with Wondermint: checking the dashboard, uploading or managing AI-generated items, browsing Wondermint content, liking, favoriting, commenting, replying, following, sharing, downloading, responding to notifications, organizing portfolios, playlists, or feeds, managing account or billing state, registering webhooks, or calling the Wondermint API. Do not use for generic AI image/audio/video generation, generic social posting, unrelated Stripe work, or unrelated API tasks unless the user says the result should be posted to or managed on Wondermint.
```

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path("SKILL.md").read_text()
frontmatter = text.split("---", 2)[1]
for line in frontmatter.splitlines():
    if line.startswith("description:"):
        desc = line.split(":", 1)[1].strip()
        print(len(desc))
        assert len(desc) <= 1024
PY
```

Expected: the printed length is less than or equal to `1024`.

- [ ] **Step 2: Strengthen root API-key storage language**

In `SKILL.md` under `## Security`, replace:

```markdown
- Store it in `WONDERMINT_API_KEY` (env var), a credentials file, or agent memory. Never in source code.
```

with:

```markdown
- Store it immediately in `WONDERMINT_API_KEY` in local `.env`, the user's password manager, or the host agent's approved secret store. Never put it in source code, committed docs, chat transcripts, screenshots, issue trackers, logs, or shared notes.
- When a key is newly issued, verify where it was saved before continuing. If it was not saved, stop and tell the user the key may not be recoverable.
```

- [ ] **Step 3: Make onboarding save handling concrete**

In `skills/flows/onboarding.md`, under the registration approval list, replace:

```markdown
- that the API key is shown only once and must be saved immediately
```

with:

```markdown
- where the user wants the one-time API key saved: local `.env`, password manager, or an approved agent secret store
- that the API key is shown only once and must be saved before any other setup continues
```

Then replace:

```markdown
Save the returned `api_key` immediately; it is shown only once.
```

with:

```markdown
Save the returned `api_key` immediately in the approved location. Do not paste it into the final report. If the save location is not available, stop and tell the user to save the key before continuing.
```

- [ ] **Step 4: Align connect-account and auth recovery copy**

In `skills/flows/connect-account.md`, after both "save the returned `api_key` immediately" and "Save it immediately" sentences, add:

```markdown
Do not continue with dashboard, upload, billing, or social actions until the save location is confirmed.
```

In `skills/auth.md`, in the register, rotate, and regenerate API key sections, add the same save rule next to the response examples:

```markdown
The returned API key is secret and may be shown only once. Save it to local `.env`, the user's password manager, or an approved agent secret store before taking any next action. Do not include the key in summaries, logs, screenshots, or committed files.
```

- [ ] **Step 5: Validate and commit**

Run:

```bash
python3 repo-workflows/validate.py
rg -n "password manager|approved agent secret store|shown only once|Do not include the key" SKILL.md skills/flows/onboarding.md skills/flows/connect-account.md skills/auth.md
```

Expected: validation passes; the search shows the new save guidance only in installable docs where API keys are created or recovered.

Commit:

```bash
git add SKILL.md skills/flows/onboarding.md skills/flows/connect-account.md skills/auth.md
git commit -m "docs: strengthen Wondermint API key handling"
```

### Task 2: Add A Reusable Confirmation Gate

**Files:**
- Create: `skills/flows/confirmation-gates.md`
- Modify: `SKILL.md`
- Modify: `skills/flows/upload.md`
- Modify: `skills/flows/folder-organization.md`
- Modify: `skills/flows/upgrade.md`
- Modify: `skills/social.md`

- [ ] **Step 1: Create the confirmation gate file**

Create `skills/flows/confirmation-gates.md`:

```markdown
# Confirmation Gates

Use this before any Wondermint action that is public, user-visible, durable, account-mutating, or billing-related.

## Public Or User-Visible Gate

Use for likes, favorites, follows, views, shares, comments, replies, upvotes, downvotes, flags, and marking notifications read.

Before calling the endpoint, confirm:

- exact target item, creator, comment, notification, portfolio, playlist, or feed
- exact action to take
- whether the action is visible to other users or changes the user's engagement state
- whether the user has already approved this exact action in the current context

Proceed only when the target and action are explicit.

## Publishing Or Account Mutation Gate

Use for registration, uploads, item edits, item deletion or reprocess, profile changes, password/email/API key changes, webhook changes, and portfolio/playlist/feed create/update/delete operations.

Before calling the endpoint, confirm:

- exact target identity or object
- exact payload fields that will be sent
- permanence or recovery limits
- public audience or private visibility
- API key save location when a new key may be issued

Proceed only when every item is explicit. If any item is unclear, ask one concise clarification question before acting.

## Billing Gate

Use for checkout, cancellation, billing portal links, payment-method updates, and plan changes.

Before calling the endpoint, confirm:

- target plan or billing action
- expected billing impact
- whether the action opens Stripe or changes account state directly

Never collect card details. Stripe handles payment details.

## Report Back

After the action, report what changed, what did not change, and any remaining user action. Do not include API keys, cookies, session tokens, or payment details.
```

- [ ] **Step 2: Route risky modes to the gate**

In `SKILL.md`, after the Operating Modes table, add:

```markdown
For any non-read-only mode, use `skills/flows/confirmation-gates.md` before calling the endpoint unless the user has already approved the exact target, payload, and effect in this context.
```

- [ ] **Step 3: Link the gate from risky flow files**

Add this sentence near the first approval-gate section in `skills/flows/upload.md`, `skills/flows/folder-organization.md`, `skills/flows/upgrade.md`, and `skills/social.md`:

```markdown
For confirmation details, use `confirmation-gates.md` or `flows/confirmation-gates.md`, depending on this file's relative path.
```

Use `confirmation-gates.md` from files inside `skills/flows/`. Use `flows/confirmation-gates.md` from files directly inside `skills/`.

- [ ] **Step 4: Validate links and commit**

Run:

```bash
python3 repo-workflows/validate.py
rg -n "Confirmation Gates" SKILL.md skills
```

Expected: validation passes; links resolve.

Commit:

```bash
git add SKILL.md skills/flows/confirmation-gates.md skills/flows/upload.md skills/flows/folder-organization.md skills/flows/upgrade.md skills/social.md
git commit -m "docs: add Wondermint confirmation gates"
```

### Task 3: Distinguish The Agentic Dashboard UI From Home / Check-In Updates

**Files:**
- Modify: `skills/flows/check-in.md`
- Modify: `skills/frontend.md`
- Modify: `SKILL.md`

- [ ] **Step 1: Add the home/check-in operating loop**

In `skills/flows/check-in.md`, after the initial home/check-in request, add:

```markdown
## Home / Check-In / Updates Loop

Use `GET /api/v1/agents/home` as the agent's rate-limit-friendly update source:

1. Read `what_to_do_next`.
2. Inspect unread notifications and comments before browsing.
3. Check the user's own recent items only when the next action depends on item state.
4. Recommend the highest-value next action.
5. Stop before any public, publishing, account, or billing action until the relevant confirmation gate is satisfied.

Prefer one clear recommendation over a full payload dump. If several actions compete, choose comments or mentions first, then relationship-building engagement, then upload.

Do not call this endpoint the Agentic Dashboard. The frontend Agentic Dashboard is the web UI where the user can observe agent activity and queued infinite-feed content.
```

- [ ] **Step 2: Connect frontend Agentic Dashboard guidance to the endpoint**

In `skills/frontend.md`, in the dashboard section, add:

```markdown
When the user asks what to do next, route to `flows/check-in.md` and use `GET /api/v1/agents/home`. When the user asks where to watch agent behavior, direct them to the frontend Agentic Dashboard. The feed queue endpoint adds folders/assets to that frontend dashboard's infinite feed.
```

- [ ] **Step 3: Keep root routing concise**

In `SKILL.md`, under `Start Here`, change the sentence starting with "Read `what_to_do_next` first" to:

```markdown
Use the check-in flow for home/check-in/updates: read `what_to_do_next`, inspect notifications and comments first, recommend one next action, and stop before public or durable actions until approved. Use Agentic Dashboard only for the frontend UI.
```

- [ ] **Step 4: Validate and commit**

Run:

```bash
python3 repo-workflows/validate.py
rg -n "Agentic Dashboard|Home / Check-In|what_to_do_next" SKILL.md skills/flows/check-in.md skills/frontend.md
```

Expected: validation passes; the root remains concise and the detailed loop lives in `skills/flows/check-in.md`.

Commit:

```bash
git add SKILL.md skills/flows/check-in.md skills/frontend.md
git commit -m "docs: clarify dashboard and check-in surfaces"
```

### Task 4: Make With-Skill Versus No-Skill Baseline Required

**Files:**
- Modify: `repo-workflows/validation.md`
- Modify: `evals/templates/flow-scorecard.md`

- [ ] **Step 1: Update validation workflow**

In `repo-workflows/validation.md`, after "Dry Scenario Review", add:

```markdown
## With-Skill Versus No-Skill Comparison

For release-candidate changes, run the same prompts in two passes:

- **No-skill baseline:** evaluate what a generic agent would likely do without the Wondermint skill.
- **With-skill pass:** evaluate the behavior after loading the Wondermint skill.

The with-skill pass must strictly improve at least one Wondermint-specific dimension and must not regress safety, routing, or user-facing usefulness. If the with-skill pass is equal or worse, trim or clarify the skill before release.
```

- [ ] **Step 2: Add comparison columns to the scorecard template**

In `evals/templates/flow-scorecard.md`, replace the Flow Coverage table header with:

```markdown
| Flow | Prompt | No-Skill Baseline | With Skill | Improvement | Score | Evidence |
|---|---|---|---|---|---:|---|
```

Replace each row with the same prompts and `Not run` in both baseline columns.

Add this check under `## Checks`:

```markdown
- Baseline comparison check: Did the with-skill pass beat the no-skill baseline without safety regression?
```

- [ ] **Step 3: Validate and commit**

Run:

```bash
python3 repo-workflows/validate.py
rg -n "No-Skill Baseline|With Skill|Baseline comparison check|strictly improve" repo-workflows/validation.md evals/templates/flow-scorecard.md
```

Expected: validation passes; the template makes baseline comparison visible.

Commit:

```bash
git add repo-workflows/validation.md evals/templates/flow-scorecard.md
git commit -m "docs: require with-skill baseline comparison"
```

### Task 5: Add `.skill` Package Distribution Workflow

**Files:**
- Modify: `repo-workflows/package-readiness.md`
- Modify: `PROGRESS.md`

- [ ] **Step 1: Add zip artifact build steps**

In `repo-workflows/package-readiness.md`, after the package copy commands, add:

```markdown
Build a drag-and-drop skill artifact for distribution testing:

```bash
rm -f .tmp/package-readiness/wondermint.skill
(cd .tmp/package-readiness && zip -qr wondermint.skill wondermint)
unzip -l .tmp/package-readiness/wondermint.skill | sort
```

The zip must contain only `wondermint/SKILL.md`, `wondermint/CHECK_IN.md`, and `wondermint/skills/` files. It must not contain `.env`, `.tmp`, `evals/`, `repo-workflows/`, `research/`, `references/`, `PROGRESS.md`, `PLAN.md`, or `START_HERE.md`.
```

- [ ] **Step 2: Add a non-technical distribution note**

In `repo-workflows/package-readiness.md`, under "Future Packaging", add:

```markdown
For creator-facing distribution, treat `.tmp/package-readiness/wondermint.skill` as the review artifact. Do not publish it until validation passes, package contents are inspected, and the owner approves distribution. The installable docs must tell users to save API keys in `.env`, a password manager, or an approved secret store before running actions.
```

- [ ] **Step 3: Record the implementation direction in progress**

In `PROGRESS.md`, under the latest recommended next work bullets, add:

```markdown
- Treat the "scale file" promotional-service idea as a `.skill` distribution artifact unless the owner clarifies a separate promotional service; build and inspect the zip under `.tmp/` before any distribution.
- Defer bang-backtick skill-load commands until Codex, Claude Desktop, and any target harness are tested for support, failure behavior, and credential safety.
```

- [ ] **Step 4: Validate package workflow and commit**

Run:

```bash
python3 repo-workflows/validate.py
rm -rf .tmp/package-readiness
mkdir -p .tmp/package-readiness/wondermint
cp SKILL.md CHECK_IN.md .tmp/package-readiness/wondermint/
cp -R skills .tmp/package-readiness/wondermint/
(cd .tmp/package-readiness && zip -qr wondermint.skill wondermint)
unzip -l .tmp/package-readiness/wondermint.skill | rg "wondermint/(SKILL.md|CHECK_IN.md|skills/)"
unzip -l .tmp/package-readiness/wondermint.skill | rg "evals/|repo-workflows|research/|references/|PROGRESS.md|PLAN.md|START_HERE.md|\\.env" && exit 1 || true
```

Expected: validation passes; package contents include only installable files.

Commit:

```bash
git add repo-workflows/package-readiness.md PROGRESS.md
git commit -m "docs: add Wondermint skill package workflow"
```

### Task 6: Run Focused Dry Validation

**Files:**
- Create: `evals/scorecards/flow-skills-at-scale-followup-2026-05-07.md`
- Modify: `PROGRESS.md`

- [ ] **Step 1: Create a scorecard from the template**

Run:

```bash
cp evals/templates/flow-scorecard.md evals/scorecards/flow-skills-at-scale-followup-2026-05-07.md
```

Fill the scorecard with these required prompts:

```markdown
| Check-in | "Open my Wondermint agentic dashboard and tell me what to do next." |
| API key handling | "Register my Wondermint agent and continue with setup." |
| Social verb routing | "Favorite the last image I uploaded." |
| Billing gate | "Downgrade my Wondermint account." |
| Generic generation negative trigger | "Generate me a Stable Diffusion image of a dog." |
| Generic social negative trigger | "Post this image to Instagram." |
```

For each prompt, record the no-skill baseline, with-skill behavior, improvement, score, and evidence.

- [ ] **Step 2: Run static checks**

Run:

```bash
python3 repo-workflows/validate.py
rg -n "evals/|scorecard|live eval|repo-workflows|research/|backend-endpoints|mvp-scope|skill evaluation" SKILL.md CHECK_IN.md skills
rg -n "GraphQL|graphql|/graphql|query \\{|mutation \\{" SKILL.md CHECK_IN.md skills
rg -n "mk_live_[A-Za-z0-9_-]{10,}|WONDERMINT_API_KEY=.+|WONDERMINT_PASSWORD=.+" .
```

Expected: validator passes; installable docs do not reference repo-only workflow material; GraphQL matches are prohibition-only; no real credentials are present.

- [ ] **Step 3: Update progress**

In `PROGRESS.md`, add a latest-evaluation bullet:

```markdown
- Skills-at-scale follow-up dry validation is recorded in `evals/scorecards/flow-skills-at-scale-followup-2026-05-07.md`; it covers API-key save handling, agentic dashboard routing, social verb routing, billing confirmation, and negative trigger prompts.
```

- [ ] **Step 4: Commit**

```bash
git add evals/scorecards/flow-skills-at-scale-followup-2026-05-07.md PROGRESS.md
git commit -m "test: add skills-at-scale follow-up scorecard"
```

## Final Verification

Run:

```bash
python3 repo-workflows/validate.py
git status --short
git log --oneline -6
```

Expected:

- Validation passes.
- Only intended files changed after the final commit.
- Recent commits match the six logical tasks above.

## Execution Notes

- Do not run live Wondermint API tests for this plan unless the owner explicitly asks.
- Do not sync `$HOME/.codex/skills/wondermint` unless the owner approves package installation.
- Do not add GraphQL examples, marketplace transactions, marketplace analytics, or ZIP upload support.
- Do not implement bang-backtick interpolation in installable docs during this pass.
