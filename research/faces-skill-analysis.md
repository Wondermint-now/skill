# Faces Skill Analysis For Wondermint Skill Development

## Source

- Repo: `/Users/ashokaji/code/fullstock/Test Wondermint/.tmp/faces-skill`
- Commit reviewed: `cf88840`
- Date: 2026-05-05
- Scope: `README.md`, `setup`, five skill folders, and `faces/references/`.
- Purpose: identify patterns that should inform Wondermint skill design without copying Faces platform behavior.

The Faces repo is a bundled skill system, not a single flat skill. It includes:

- `/faces`: core CLI reference and power-user workflow.
- `/face`: guided creation flow.
- `/facechat`: chat with a face or team.
- `/faceteam`: team composition and protocol authoring.
- `/manyface`: transform a skill into a multi-persona workflow.

## High-Level Takeaways

Faces is valuable because it turns a platform API into agent-operable workflows. It does not only document commands. It gives agents a posture, decision rules, setup checks, artifacts to write, and clear success states.

For Wondermint, the useful lesson is to build guided operating flows around user outcomes:

- first-time setup
- check-in/update
- browsing and discovery
- upload/publish
- comments and engagement
- folder organization
- live evaluation
- troubleshooting

Wondermint should not copy the multi-slash-command shape yet. The current repo is better served by one concise `SKILL.md` that routes into focused flow files.

## Patterns Worth Adopting

### 1. Bundle-Level Product Model

Faces presents the repo as a package of related capabilities. Each capability has its own entrypoint, but the README explains how they compose into a system.

Wondermint can use the same product-level framing:

- `SKILL.md` is the main agent entrypoint.
- `CHECK_IN.md` gives the recurring information-gathering workflow.
- `skills/flows/` should hold guided actions.
- `skills/references/` should hold factual API and UX context.
- `evals/` holds evidence about how well the skill works.

### 2. Guided Flows, Not Raw Reference

The strongest Faces files are the guided workflow skills. `/face` walks from interview to research to recipe to compilation. `/faceteam` walks from task understanding to casting to protocol design to review and compile.

Wondermint should make its high-risk user journeys just as procedural:

1. Identify the user's intent and constraints.
2. Confirm credentials and environment.
3. Gather the minimum required inputs.
4. Check existing state before creating duplicates.
5. Take the action behind an approval gate when needed.
6. Verify the result.
7. Report the result, evidence, and next option.

### 3. Strong Response Posture

Faces repeatedly tells the agent to push for specificity, challenge vague requests, and recommend a concrete path instead of offering undifferentiated menus.

Wondermint should adopt a lighter version:

- Ask for missing information only when it affects the action.
- Recommend defaults for category, tags, privacy/publicness, and engagement strategy.
- Challenge vague upload or engagement requests when they could create public, durable, or brand-sensitive outcomes.
- Keep the final response operational: what happened, where it is, and what is next.

### 4. Reuse Before Creation

Faces checks the existing catalog before creating a new face or team. That keeps the system from fragmenting into duplicates.

Wondermint should apply the same rule to:

- folders and saved collections
- item/category/tag patterns
- repeated upload metadata
- comments and replies on the same item
- evaluation records

Before creating a new organizational object, the skill should inspect whether an existing one fits.

### 5. Artifact-First Workflows

Faces creates durable artifacts:

- `FACE.md` records queued sources, compiled sources, lessons, and notes.
- `TEAM.md` records the team protocol and roles.
- Manyfaced skills include setup tables and circuit diagrams.

Wondermint already has scorecards. Future Wondermint artifacts should include:

- upload receipts
- live-eval scorecards
- check-in summaries
- user-flow notes
- reusable metadata examples
- troubleshooting notes from real failures

### 6. Protocol Diagrams As Executable Specs

`/faceteam` uses mermaid diagrams as execution specs. Shape and edge semantics matter:

- rounded nodes call a face
- sharp rectangles are agent-executed instructions
- diamonds are branch conditions
- edges represent explicit data flow

Wondermint does not need this for normal API calls, but the idea is useful for complex UX flows. A future upload or onboarding flow could include a small decision graph that makes branching behavior unambiguous.

### 7. Judgment Versus Mechanical Work

`/manyface` has a useful decomposition rule: persona depth belongs on judgment steps, while file operations, git commands, API calls, and data transforms stay mechanical.

Wondermint should use this when designing flow files:

- Mechanical: auth checks, GET calls, POST schemas, pagination, evidence capture.
- Judgment: choosing categories, summarizing a check-in, deciding what to ask next, drafting comments, recommending upload metadata.

This keeps the skill from over-explaining simple API mechanics while improving the parts where users need guidance.

### 8. Auth Triage Pattern

Faces uses a consistent preamble:

- verify CLI install/version
- check auth
- distinguish returning-user failures from brand-new setup
- never print secrets
- route first-time users into quickstart/auth docs

Wondermint should centralize this pattern in one auth/setup reference instead of duplicating it across every flow.

Recommended Wondermint auth triage:

- Check whether credentials are available.
- Verify identity with the safest read-only endpoint.
- If credentials exist but auth fails, diagnose without restarting onboarding.
- If no credentials exist, route to setup guidance.
- Never log or commit API keys, passwords, tokens, or real credential payloads.

### 9. Safety Gates Around Paid Or Durable Actions

Faces documentation explicitly says human payment activation must happen in a browser, and destructive config clearing should never be used casually.

Wondermint should mirror this with clear approval gates:

- Ask before upload/publish.
- Ask before comment, like, follow, subscribe, payment, or folder mutations unless already authorized.
- Ask before rotating keys, changing passwords, or updating account settings.
- Keep credentials in `.env` or ignored local files only.

### 10. Reference Files With Clear Routing

Faces has focused reference files: auth, billing, concepts, interviews, OAuth, quickstart, command reference, scope, templates, use cases.

Wondermint should create similarly narrow references as the skill grows:

- `skills/references/auth.md`
- `skills/references/api.md` or endpoint-specific files
- `skills/references/faq.md`
- `skills/references/ux.md`
- `skills/references/errors.md`
- `skills/flows/upload.md`
- `skills/flows/live-eval.md`
- `skills/flows/check-in.md`

The root `SKILL.md` should tell the agent exactly when to read each one.

## Risks And Gaps In The Faces Skill

These are not blockers for studying the repo, but they matter if Wondermint borrows the patterns.

### 1. Duplicated Preamble And Auth Triage

The same setup/auth block appears across multiple skill files. That creates maintenance risk because auth behavior and CLI setup guidance can drift.

Wondermint should avoid copying that pattern directly. Keep shared setup and credential guidance in one file and route to it.

### 2. Some Skill Files Are Long

`manyface/SKILL.md` is 607 lines. The skill-creator guidance prefers concise skill entrypoints with deeper material moved into referenced files.

Wondermint should keep root `SKILL.md` and each flow file lean. When a flow grows past a few hundred lines, split reference material out.

### 3. Host-Specific Frontmatter

Faces uses `allowed-tools`, `AskUserQuestion`, and a `compatibility` frontmatter field. Those are useful for some hosts, but Codex skill discovery is centered on `name` and `description`.

Wondermint should optimize for Codex first:

- use only `name` and `description` in root skill frontmatter unless a host requires more
- keep descriptions under the 1024-character budget
- avoid host-only syntax in installable skill behavior

### 4. Potentially Brittle Shell Interpolation

`faces/SKILL.md` includes a `!` shell interpolation line for `faces config:show`. That is host-specific and could expose configuration unless masking is guaranteed.

Wondermint should avoid automatic config-printing snippets in the skill body. Prefer explicit commands with reminders to mask secrets.

### 5. Description Quality Issue In `/face`

The `/face` description appears to have a broken sentence: it says the flow can "compile, and optionally" and then immediately starts "Trigger when...".

Wondermint should validate frontmatter descriptions for clarity before publishing.

### 6. External And Paid Actions Need More Explicit Gates

Faces includes install, registration, payment activation, top-up, and PR publishing paths. It often has good human-gate language, but the bundle also includes examples that run install or GitHub commands.

Wondermint should make paid, public, or durable actions impossible to miss:

- identify the action as paid/public/durable
- get explicit user approval
- record what changed

### 7. Installable Package Boundary Is Host-Specific

The setup script symlinks multiple skill folders into `~/.claude/skills/`. That is effective for Claude Code slash-command discovery, but it is not the same as a Codex-first packaged skill.

Wondermint should define its own installable package boundary before adding multiple entrypoint folders.

## Wondermint Implications

### Near-Term

Use Faces as a model for flow design, not repo topology.

Add `skills/flows/` with:

- `live-eval.md`
- `upload.md`

Each flow should include:

- when to use it
- required inputs
- auth/setup preflight
- read-only versus mutating status
- approval gates
- exact API calls or references
- evidence to capture
- final report format

### Medium-Term

Add focused reference files:

- auth and credentials
- API endpoint reference
- user-facing FAQ
- upload metadata examples
- platform UX flows
- troubleshooting and known live-test pitfalls

Keep `SKILL.md` as the routing layer.

### Later

Consider diagrams only for complex flows:

- first-time setup
- upload with media processing
- notification/comment response loops
- evaluation sequence

Do not add a many-command bundle until there is evidence that one Wondermint skill entrypoint cannot route cleanly.

## Recommended Next Actions

1. Define the installable package boundary before adding more folders.
2. Add `skills/flows/README.md`, `skills/flows/live-eval.md`, and `skills/flows/upload.md`.
3. Centralize auth and credential setup guidance in one reference file.
4. Update `SKILL.md` with "read this when..." routing only after the first flow files exist.
5. Add a lightweight validation script for links, frontmatter, description length, and secret patterns.
6. Keep scorecards and raw evidence in `evals/` for every future baseline or live test.

