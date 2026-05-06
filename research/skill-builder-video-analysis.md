# Skill Builder Video Analysis

## Source

User-provided transcript from a skill-file workshop by Pedro Rodrigues, focused
on building, testing, and productionizing agent skills.

## Core Model

Skills are folders, not single files. `SKILL.md` is the entrypoint and router;
referenced markdown files and scripts carry deeper guidance or deterministic
operations.

Progressive disclosure is the main design constraint:

1. frontmatter loads first and decides whether the skill is relevant
2. `SKILL.md` body loads only after the skill triggers
3. referenced files load only when the agent follows those links

The useful mental model is a book: `SKILL.md` is the index, and reference files
are chapters. The root skill file should contain enough context to route and
start the workflow, not the full reference corpus.

## Frontmatter And Triggering

Required frontmatter remains minimal:

```yaml
---
name: my-skill
description: Use when the user asks to do a specific class of work.
---
```

The description is routing behavior, not documentation. It should say when to
load the skill and what class of task it supports. Starting with `Use when...`
appears to improve trigger reliability in practice.

Negative trigger space matters. If similar-looking work should not load the
skill, the description should say so explicitly.

Trigger reliability levels:

- description-only matching is useful but probabilistic
- `use <skill-name>` in the prompt is much more reliable
- slash command invocation is strongest where the agent harness supports it

## Skills And MCP

Skills and MCP tools solve different problems.

Use MCP tools for integrations, authenticated remote actions, and operations
that should run server-side without exposing credentials to the agent's local
environment.

Use skills to explain how and when the agent should use available tools,
scripts, docs, schemas, and workflows. For a large database or API surface, the
MCP tool can expose chunked access while the skill describes the progressive
loading strategy and safety rules.

## Evaluation Lessons

Skill evals should start by defining what good behavior means. The scenarios
matter more than the harness: weak or unrepresentative scenarios produce weak
confidence.

Useful eval structure:

- prompt or task input
- expected behavior
- assertions about tool calls, file changes, outputs, or safety stops
- optional LLM-as-judge criteria when deterministic assertions are impossible

The transcript's strongest eval pattern is comparing behavior with and without
the skill. The goal is to prove that loading the skill changes agent behavior in
the intended direction.

Deterministic checks should be preferred wherever possible. LLM-as-judge can be
useful for nondeterministic outputs, but it can hallucinate or grade the wrong
thing if the assertion is poorly designed.

Fresh environments matter for stronger evals. Local manual runs are useful at
first; later pipelines should isolate state with a clean workspace, container,
or equivalent harness.

## Production Guidance

Treat production skills like code and documentation:

- keep the production skill set small and task-relevant
- update skills when product workflows or APIs change
- include skill maintenance in repo agent instructions
- periodically check whether a skill is still used and still describes the
  right workflow
- keep provenance and versioning visible enough to detect drift

It is acceptable for local development environments to have many experimental
skills installed, because frontmatter descriptions are small. Production or CI
environments should install only the skills needed for that workflow.

## Implications For Wondermint

The current Wondermint repo direction is aligned with this guidance:

- `SKILL.md` is the router
- `CHECK_IN.md` and `skills/` are installable deeper guidance
- `repo-workflows/`, `evals/`, `research/`, and `references/backend-endpoints/`
  are repo-only development surfaces
- `repo-workflows/validate.py` provides deterministic validation
- trigger coverage now includes positive and negative cases

Future Wondermint improvements should prioritize:

- with-skill vs without-skill dry evals for key scenarios
- deterministic assertions before LLM-as-judge scoring
- explicit invocation guidance for high-stakes or must-load workflows
- keeping installable docs free of repo-only evaluation and release procedure
  language
- reviewing trigger descriptions whenever Wondermint product scope changes
