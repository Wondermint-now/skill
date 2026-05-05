# G Stack Analysis For Wondermint Skill Development

## Source

- Repo: `/Users/ashokaji/code/External repos/gstack`
- Commit reviewed: `db9447c3`
- Date: 2026-05-05
- Purpose: identify repo and skill-design patterns that should inform the Wondermint skill file.

## High-Level Takeaways

G stack is not just a set of reference docs. It is a workflow system: each skill acts like a specialist with a clear trigger, explicit operating mode, required phases, gates, output artifacts, and follow-up recommendations.

For Wondermint, the useful lesson is to make the skill feel like an operator guide for a complete user experience, not only an API reference.

## Patterns Worth Adopting

### 1. Strong Trigger Metadata

G stack frontmatter descriptions are specific about:

- What the skill does.
- Exact user phrases or situations that should trigger it.
- When to proactively use it.
- Related skills that should run before or after.

Wondermint should apply this by making `SKILL.md` and any flow files explicit about when to use them: upload, check-in/update, onboarding, social engagement, folder organization, troubleshooting, and live eval.

### 2. Workflow Phases

Representative G stack skills use named phases such as context gathering, authenticate, orient, explore, document, wrap up, and capture learnings.

Wondermint flows should be written the same way. Example for upload:

1. Confirm operator intent and permanence.
2. Inspect asset and thumbnail requirements.
3. Choose category, subcategories, and tags.
4. Create listing.
5. Upload file.
6. Confirm processing result.
7. Report live URL, locked fields, and remaining edit window.

### 3. Output Artifacts

G stack writes durable artifacts: design docs, QA reports, baselines, review logs, and eval transcripts.

Wondermint already has `evals/`. Adopt the same discipline:

- Every live eval gets a scorecard.
- Raw evidence stays under `evals/logs/`.
- `PROGRESS.md` points to the latest evaluation.
- Test credentials remain ignored and never appear in artifacts.

### 4. Report-Only vs Mutating Modes

G stack separates `/qa-only` from `/qa`: one reports, the other fixes. This is a useful boundary.

Wondermint should explicitly separate:

- Read-only check-in/eval flows.
- Mutating engagement flows such as liking, commenting, following, marking notifications read.
- Publishing flows such as upload.

This avoids accidental live mutations while still allowing rich testing when requested.

### 5. Approval Gates Before Durable Actions

`skillify` has clear gates before committing durable artifacts. It stages, tests, asks, then commits or discards.

Wondermint should copy this pattern for irreversible or public actions:

- Ask before upload.
- Ask before commenting as the agent.
- Ask before following users or liking items if the user has not already authorized engagement.
- Ask before setting passwords, changing email, or rotating API keys.

### 6. Score Rubrics

G stack uses explicit rubrics for QA health, DX scorecards, and review readiness. This makes quality comparable over time.

Wondermint evals should keep a simple scorecard for now, but future phases should add flow-specific rubrics:

- API correctness.
- Agent autonomy.
- User guidance quality.
- Credential safety.
- Recovery from validation/auth/rate-limit errors.

### 7. Learnings Capture

Many G stack skills end with a learnings-capture block: pattern, pitfall, preference, architecture, tool, operational.

Wondermint should adopt a lightweight version in `PROGRESS.md` or future `research/learnings.md`:

- Pattern: good workflow or API behavior to reuse.
- Pitfall: things that confused the agent.
- Preference: user-stated repo or skill expectations.
- Operational: live testing constraints, such as Cloudflare blocking Python's default HTTP client.

### 8. Development Mode And Packaging Boundary

G stack distinguishes development workflow from installed skill behavior. It uses generated skill files, dev symlinks, and contributor docs, while installable skills remain focused.

Wondermint needs a clear package boundary:

- Repo docs such as `START_HERE.md`, `PROGRESS.md`, `PLAN.md`, `research/`, and `evals/` are for development.
- The installable skill should likely be a clean package containing `SKILL.md`, `CHECK_IN.md`, `skills/`, and any future essential references/assets.

### 9. Static, E2E, And Judge Evals

G stack separates test tiers:

- Static checks.
- E2E skill execution.
- LLM-as-judge scoring.

Wondermint does not need that full system yet, but it should mirror the shape:

- Static review: links, frontmatter, progressive disclosure, secret scan.
- Live API eval: safe read-only endpoints, then opt-in mutating flows.
- Forward-testing: fresh agent uses the skill with realistic prompts and minimal leaked context.

### 10. Read-This-When Routing

G stack skills are long, but they use sectioned workflows and clear trigger metadata. The skill-creator guidance still matters: keep loaded context small.

Wondermint should move toward direct routing language:

- Read `skills/auth.md` when registering, linking, setting password, or rotating keys.
- Read `skills/items.md` when uploading or managing listings.
- Read `skills/flows/upload.md` when the user wants a guided upload.
- Read `skills/flows/live-eval.md` when testing the skill against the live API.

## Recommended Wondermint Conventions

1. Keep root `SKILL.md` as a router plus the most important security/platform rules.
2. Add `skills/flows/` for task workflows.
3. Add `skills/references/` or continue using focused reference files for deeper API and FAQ content.
4. Write flow files with phases, explicit gates, success criteria, and final report format.
5. Distinguish read-only flows from mutating/publishing flows.
6. Record every eval under `evals/` with a scorecard and raw evidence.
7. Record operational learnings in `PROGRESS.md` until a dedicated learnings file is needed.
8. Define a clean installable skill package boundary before reorganizing the repo.

## Immediate Follow-Up Work

The next Wondermint phase should not start by rewriting everything. It should add the smallest structure that unlocks progressive disclosure:

1. Define the package boundary in `START_HERE.md` and `PLAN.md`.
2. Add `skills/flows/README.md` and one or two high-value flow files.
3. Start with `live-eval.md` and `upload.md`, because the live eval found real operational behavior and upload has the highest risk.
4. Update `SKILL.md` only enough to route to those files.
5. Add the Cloudflare/Python-client pitfall to testing guidance.

## Second Pass: Repo Mechanics And Quality System

### Source Areas Reviewed

- `package.json`
- `setup`
- `scripts/gen-skill-docs.ts`
- `scripts/skill-check.ts`
- `scripts/discover-skills.ts`
- `scripts/host-config.ts`
- `hosts/*.ts`, especially `hosts/codex.ts`
- `test/skill-validation.test.ts`
- `test/gen-skill-docs.test.ts`
- `test/skill-budget-regression.test.ts`
- `test/helpers/eval-store.ts`
- `test/helpers/session-runner.ts`
- `.github/workflows/skill-docs.yml`
- `.github/workflows/evals.yml`
- `SKILL.md.tmpl`
- `qa-only/SKILL.md.tmpl`

### 11. Templates Are A Build Boundary, Not Just Convenience

G stack treats `SKILL.md` files as generated outputs from `SKILL.md.tmpl`. The generated files carry an explicit auto-generated header, and CI checks that committed generated docs are fresh.

Wondermint should not adopt template generation yet. The repo has one primary skill and a small number of support files, so templates would add process before they remove pain.

Recommended adaptation:

- Stay hand-authored for now.
- Add generation only after repeated boilerplate appears across flow files.
- If generation is added later, make `SKILL.md.tmpl` the source and mark generated outputs clearly.

### 12. Use Tiny Validation Before Heavy Evals

G stack's `skill:check` validates command references, templates, host outputs, and freshness. Its tests also check frontmatter, description length, unresolved placeholders, hardcoded branch names, path consistency, and output structures.

Wondermint can get most of the benefit with a much smaller validator:

- Check every markdown link target exists.
- Check root `SKILL.md` frontmatter has `name` and `description`.
- Check description length stays under 1024 characters for Codex compatibility.
- Check no committed file contains a real-looking Wondermint API key.
- Check `.env.example` exists and `.env` is ignored.
- Check `evals/scorecards/` entries link to raw evidence when applicable.

This should be a simple script before any G-stack-style build system exists.

### 13. Keep Host Compatibility In Mind

G stack has host configs for Claude, Codex, Factory, OpenCode, OpenClaw, Hermes, GBrain, and others. The key Codex-specific constraint is that frontmatter is reduced to `name` and `description`, with a 1024-character description limit.

Wondermint should optimize for Codex first:

- Keep root frontmatter to `name` and `description`.
- Avoid extra fields unless a host requires them.
- Keep the description comprehensive but comfortably under 1024 characters.
- Add `agents/openai.yaml` later only when preparing install/distribution.

### 14. Project-Scoped Eval History Matters

G stack stores machine-readable eval runs with schema version, branch, git SHA, timestamps, tier, cost, duration, and per-test results. It can compare the latest run to prior runs and detect budget regressions.

Wondermint's current markdown scorecards are appropriate for this stage, but future eval records should add a small machine-readable index:

- `evals/runs.jsonl` or one JSON summary per run.
- Include commit, branch, date, scenario names, pass/fail, and score.
- Keep raw evidence in `evals/logs/`.
- Keep human summaries in `evals/scorecards/`.

This would enable trend tracking without needing G stack's full eval store.

### 15. Budget Regression Is A Skill Quality Signal

G stack tracks whether later eval runs take far more tool calls or turns than earlier runs. That catches prompt bloat and confusion.

Wondermint should eventually track a simpler version:

- Number of API calls per eval scenario.
- Number of agent turns or manual interventions.
- Whether the agent used the intended flow file.
- Whether the agent mixed up endpoint parameters, as happened with `first` vs `limit`.

This will show whether skill revisions make the agent more autonomous or more confused.

### 16. Installation And Development Should Be Separate

G stack's setup/dev-mode system links a working tree into host skill directories so changes can be tested live. It also separates runtime assets and generated host-specific skill outputs.

Wondermint should define two surfaces:

- **Development repo:** this full repository, including `research/`, `evals/`, `PLAN.md`, and `PROGRESS.md`.
- **Installable skill package:** only the files an agent should load/use, likely `SKILL.md`, `CHECK_IN.md`, `skills/`, and any future `agents/openai.yaml`.

The package boundary should be explicit before broad restructuring.

### 17. CI Can Start Very Small

G stack has multiple CI lanes: skill-doc freshness, evals, Windows free tests, version gates, and workflow lint.

Wondermint only needs a small local check first. Later CI can run the same check:

- Markdown links exist.
- Frontmatter is valid enough for Codex.
- No real API keys or local credential files are tracked.
- Eval scorecards have expected headings.

Do not add live Wondermint API tests to CI unless there is a deliberate credentials and rate-limit plan.

### 18. Templates Use Placeholders For Shared Policy

G stack templates inject shared blocks such as preamble, browse setup, learnings search, QA methodology, and learnings logging. This prevents policy drift across many skills.

Wondermint may eventually need a lighter equivalent if `skills/flows/` grows:

- Shared credential safety block.
- Shared approval-gate language.
- Shared final report format.
- Shared eval evidence format.

For now, copy the shared pattern manually and revisit generation only after three or more flow files duplicate the same block.

## Second-Pass Recommendations

1. Add a "Package Boundary" section to `START_HERE.md`.
2. Add a small validation script before adding more eval complexity.
3. Add `skills/flows/` manually; do not introduce templates yet.
4. Add `skills/flows/live-eval.md` first, because it can encode the current live-test learning.
5. Add `skills/flows/upload.md` second, because it needs the strongest approval gates.
6. Keep future `agents/openai.yaml` as a packaging task, not a core authoring task.
7. Consider `evals/runs.jsonl` after the next one or two evals, once the fields are clear from real use.
