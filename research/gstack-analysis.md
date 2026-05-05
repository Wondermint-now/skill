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
