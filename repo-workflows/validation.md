# Validation Workflow

This workflow is for checking whether the Wondermint skill files are coherent,
safe, and agent-operable. It is not part of the installable Wondermint skill.

## When To Use

Use this after adding or changing installable skill files, especially files in
`skills/flows/`.

Run dry validation before live Wondermint testing.

## Static Checks

Run these before scenario review:

```bash
python3 repo-workflows/validate.py
```

The validator checks root frontmatter, the 1024-character description budget,
installable/repo-only boundaries, REST-only GraphQL language, obvious secrets,
and markdown links.

```bash
git status --short
```

```bash
rg -n "evals/|scorecard|live eval|repo-workflows|research/|backend-endpoints|mvp-scope|skill evaluation" SKILL.md CHECK_IN.md skills
```

This command should return no installable-skill matches.

```bash
rg -n "GraphQL|graphql|/graphql|query \\{|mutation \\{" SKILL.md CHECK_IN.md skills
```

Only REST-only prohibition language should match.

```bash
rg -n "mk_live_[A-Za-z0-9_-]{10,}|WONDERMINT_API_KEY=.+|WONDERMINT_PASSWORD=.+" .
```

Real credentials should not match. Existing committed references to the secret
scan command itself are acceptable.

Check markdown links with a local relative-link scan or equivalent.

## Flow Review

For each flow, inspect:

- `SKILL.md` routes the relevant user request to the flow.
- The flow starts from a real user intent, not a repo-development task.
- The flow points to detailed endpoint docs instead of duplicating large API
  references.
- Risky public, billing, account, or irreversible actions have explicit
  approval gates.
- The flow says what to report back to the user.
- The flow stays within MVP scope and REST-only behavior.

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

## Dry Scenario Review

Use realistic prompts without calling live Wondermint unless explicitly asked.

Recommended baseline prompts:

- "Check my Wondermint updates and tell me what to do next."
- "Open my Wondermint check-in endpoint."
- "Where do I watch my agent's behavior in the Agentic Dashboard?"
- "Add this feed to my Agentic Dashboard infinite feed."
- "Upload this audio file with cover art."
- "Upgrade me to Unleashed yearly."
- "Upgrade me to Unleashed monthly."
- "Upload these items on a Free plan without hitting rate limits."
- "How should my workflow change on Unleashed?"
- "I created a Wondermint account in the frontend. Connect my agent."
- "I created an agent account. Help me log into the frontend."
- "Reply to this comment on my item."

Recommended trigger prompts:

- should load: "Check my Wondermint and tell me what needs attention."
- should load: "Check my Wondermint platform updates."
- should load: "Show me where to watch my agent in the Agentic Dashboard."
- should load: "Add this public feed to my Agentic Dashboard queue."
- should load: "Post this generated image to Wondermint."
- should load: "Organize my Wondermint uploads into folders."
- should load: "Reply to the newest Wondermint comment on my item."
- should load: "Connect my Wondermint frontend account to my agent."
- should load: "Upgrade my Wondermint account to Unleashed."
- should not load: "Generate a cyberpunk image for me."
- should not load: "Post this image to Instagram."
- should not load: "Debug this unrelated REST API."
- should not load: "Set up a generic Stripe checkout flow."

For each prompt, score whether the skill would:

- choose the correct flow
- ask the right clarifying questions
- stop before unsafe actions
- use the right endpoint reference
- give a useful final user-facing response

## With-Skill Versus No-Skill Comparison

For release-candidate changes, run the same prompts in two passes:

- **No-skill baseline:** evaluate what a generic agent would likely do without
  the Wondermint skill.
- **With-skill pass:** evaluate the behavior after loading the Wondermint skill.

The with-skill pass must strictly improve at least one Wondermint-specific
dimension and must not regress safety, routing, or user-facing usefulness. Pay
special attention to dashboard terminology, feed queue routing, billing
interval clarity, and rate-limit safety.

## Evidence

Record dry validation in `evals/scorecards/` using
`evals/templates/flow-scorecard.md`.

Save raw notes under `evals/logs/` only when there is useful scenario evidence
to preserve.

## When To Escalate To Live Eval

Move to `repo-workflows/live-eval.md` only after dry validation passes and the
owner explicitly asks for live testing.
