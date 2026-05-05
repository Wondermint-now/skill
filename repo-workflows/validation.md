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

## Dry Scenario Review

Use realistic prompts without calling live Wondermint unless explicitly asked.

Recommended baseline prompts:

- "Check my Wondermint and tell me what needs attention."
- "Upload this audio file with cover art."
- "Upgrade me to Pro."
- "I created a Wondermint account in the frontend. Connect my agent."
- "I created an agent account. Help me log into the frontend."
- "Reply to this comment on my item."

For each prompt, score whether the skill would:

- choose the correct flow
- ask the right clarifying questions
- stop before unsafe actions
- use the right endpoint reference
- give a useful final user-facing response

## Evidence

Record dry validation in `evals/scorecards/` using
`evals/templates/flow-scorecard.md`.

Save raw notes under `evals/logs/` only when there is useful scenario evidence
to preserve.

## When To Escalate To Live Eval

Move to `repo-workflows/live-eval.md` only after dry validation passes and the
owner explicitly asks for live testing.
