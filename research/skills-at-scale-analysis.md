# Skills At Scale Analysis For Wondermint Skill Development

## Source

- Workshop: *Skills at Scale* by Nick Nisi and Zack Proser, developer-experience engineers on the WorkOS Applied AI team.
- Format: ~80-minute interactive workshop transcript with audience Q&A and live exercises (the "repo roast" skill).
- Date reviewed: 2026-05-07.
- Purpose: extend the existing skill-builder and gstack analyses with a second independent practitioner account and pull out the patterns the Wondermint skill should adopt or test.

## Core Model

The workshop reinforces the same picture as the Pedro Rodrigues video — skill folder, `SKILL.md` as router, progressive disclosure, frontmatter description as routing rule — and then adds three pieces the prior research notes did not have:

1. An *empirical* rule for evals: a skill must beat the no-skill baseline, not merely pass in absolute terms. The presenters caught their own Next.js installer skill regressing accuracy by roughly 30% only because the eval framework compared with-skill versus without-skill behavior side-by-side. Pass rate alone would have shipped the regression.
2. A *deterministic-baseline* mechanism inside skills via bang-backtick script interpolation. `` !`<shell command>` `` inside a skill executes at load time and substitutes the command's output into the skill body before the LLM reasons. This converts vague instructions ("look at the recent commits") into a known starting state.
3. A *confidence-scoring loop* that gates execution behind iterative clarification rather than letting the agent guess past an unclear request. Nick Nisi's `ideation` plugin scores 0–100 across a five-dimension rubric and forces multiple-choice questions through `AskUserQuestion` until the score crosses ≈95% before producing a contract.

The big-frame argument also sharpens: skills are how teams move *off* `CLAUDE.md` for everything-but-the-bare-essentials. Every line of `CLAUDE.md` is paid for in every conversation. Skills load on demand because the description is routing, so the skill layer can be large and rich while the always-on context stays small.

## Patterns Worth Adopting

### 1. Description-As-Routing, With Negative Triggers

The workshop reinforces that the frontmatter `description` is what the LLM uses at runtime to decide whether to load. Wondermint's current description already does the right thing — `Use when the user wants to interact with Wondermint…` followed by `Do not use for…` exclusions. The Skills-at-Scale phrasing the Wondermint skill should keep verifying:

- The positive list should name the *kinds of work* that should trigger it (dashboard, items, social actions, billing) rather than just the product.
- The negative list should call out *plausible-looking* misroutes: generic image/audio generation, generic social posting, unrelated Stripe work, unrelated API integration. Wondermint already covers these.
- Authors note that descriptions often need to mention acronyms, product names, and the verbs users actually use, so the routing fires on natural phrasing. Worth checking whether Wondermint's description names the social verbs (like, comment, follow, favorite, share, download) explicitly enough — currently those are folded into "social actions," which may be the right level of abstraction or may underfire on direct verb prompts.

Test plan: extend the existing eval set with prompts that *should* fire the skill ("favorite the last image I uploaded") and prompts that should *not* ("generate me a Stable Diffusion image of a dog") and confirm routing behavior matches the description's promises in both directions.

### 2. Constraints Over Prescriptions, Backed By A Cautionary Eval

The empirical anchor of the workshop is the Next.js installer regression. Their skill made the model ~30% *worse* at Next.js because Claude was already capable, and the skill's prescriptive instructions were overriding correct default behavior. Constraints — short rules expressed as "never do X" or "always include Y" — outperformed long prescriptive walkthroughs.

For Wondermint this implies a clear discipline:

- Where Claude already understands a generic operation (calling a REST endpoint, parsing JSON, handling rate limits, building an `Authorization` header), the skill should *constrain* the operation, not teach it. Don't explain what `curl` is or how `application/json` works. Do explicitly say "never send the API key to any host other than the configured Wondermint API base URL," "never use GraphQL or `/graphql`," "request fields are snake_case." Those are the lines that earn their tokens.
- Where the platform has product-specific shape that Claude would not guess (the Read-only / Public / Publishing / Billing operating-mode gates, the plan tier names, the `mk_live_…` API key prefix, the `wondermint.now` frontend host, the snake_case-with-folder-exceptions response convention), the skill must teach.
- Anything that falls in between — phrasing of comments, content guidelines, default discovery behavior — should be expressed as constraints rather than scripts. "Engage before you create" is constraint-shaped. "Quality over quantity" is constraint-shaped. Long worked examples are not.

Action: add an eval pair that runs an end-to-end Wondermint operation (e.g., browse dashboard → favorite an item → comment on it) with and without the skill loaded. Require the with-skill score to *strictly exceed* the no-skill baseline. If it does not, the skill is over-prescribing somewhere and needs trimming, not extending.

### 3. Skill Router Pattern For Reference Files

The WorkOS public skills repo uses a "skill router" pattern: a tiny entry-point `SKILL.md` whose job is mostly to point at per-target reference files (`if installing AuthKit into Next.js → load workos-authkit-nextjs.md`). Their migration skills work the same way — one router, *N* migration guides, exactly one loads at a time.

The Wondermint skill already has the right scaffolding (`references/`, `repo-workflows/`, `skills/` subdirectories) but the routing language inside `SKILL.md` itself should be audited:

- Does the skill body explicitly say *when* to follow each reference link? "If the user wants to register a webhook, load `references/webhooks.md`" is router-shaped. Inlining the webhook documentation into the body is not.
- Are the reference files small and single-purpose? A `references/items.md` that mixes upload, edit, delete, and reprocess is a candidate to split if any one operation has enough surface to warrant its own page.
- Could the operating-mode table itself become a router? "If the operation is in the Publishing column, load `references/publishing-confirmation.md` for the confirmation script and required fields" is the same pattern applied to behavior rather than feature.

This is mainly a maintenance-cost argument: smaller, single-purpose reference files are easier to evaluate, easier to replace when the API changes, and easier for the LLM to load only the relevant chunk.

### 4. Bang-Backtick Interpolation For Deterministic Baselines

This is the mechanism the prior research notes did not surface. Inside a skill body, `` !`<command>` `` causes Claude to execute the command at load time and substitute the output into the skill before reasoning. The presenters used it for things like "the latest 10 commits," "stale TODOs from `gh issue list`," and "current branch state."

For Wondermint, the equivalent moves are:

- **Plan and account state**: `` !`curl -s -H "X-API-Key: $WONDERMINT_API_KEY" $WONDERMINT_API_BASE/api/v1/me` `` to inject the user's current plan, item count, and limits at skill-load time. The LLM then reasons about quotas without guessing.
- **Recent activity**: a curl to the dashboard endpoint to inject the last *N* items, recent comments, or unread notifications, so phrases like "the last image I uploaded" resolve without a separate tool call.
- **Status checks**: a quick `curl` to a health or status endpoint to inject API availability before the skill suggests writes against a degraded backend.

The general rule the presenters articulated: *anything you would have run in three terminal tabs before reaching for an LLM is a candidate for codification inside the skill.* For Wondermint, those tabs are usually "what's my current state on the platform" and "is this thing broken." Both are solvable with bang-backtick blocks.

Implementation note: bang-backtick scripts must be safe to run unconditionally because they execute every time the skill loads. They should be read-only, fast, and resilient to a missing API key (so the skill does not error out for first-time users before they have configured `WONDERMINT_API_KEY`).

### 5. Confidence Scoring As An Iterative Clarification Gate

Nick Nisi's `ideation` plugin scores incoming requests 0–100 across problem clarity, goal definition, success criteria, scope boundaries, and consistency, and uses Claude's `AskUserQuestion` tool to drive iterative multiple-choice clarification until the score reaches ≈95% before producing a contract. The presenters were explicit that the math is fuzzy by design — the score is a forcing function for clarification, not a measurement.

For Wondermint, this maps cleanly onto the existing operating-mode gates. The Read-only mode genuinely does not need clarification. The Public/User-visible and Publishing/Billing modes already require explicit approval. The pattern to test:

- For Publishing mode (uploads, item edits, portfolio/playlist/feed mutations, profile changes, API-key rotation), introduce a structured confirmation step modeled on the confidence-loop pattern. Score the request across: target item identity, exact payload, permanence, recovery limits, and audience. Refuse to proceed until each is explicit. The score itself is theatre; the forced enumeration is the point.
- For Billing mode (checkout, cancellation, plan changes, payment-method updates), the same pattern with a tighter rubric: target plan, billing impact, irreversibility window. Stripe still handles card data — the confidence loop only governs whether the *intent* is clear before the agent calls the Wondermint billing endpoint.

The structural reason this is worth doing: irreversible operations are the most expensive failure mode for an autonomous Wondermint agent. A clarification loop costs a few seconds; an unintended public post or an accidental plan downgrade costs reputation and money.

### 6. Eval-Baseline Comparison As A Hard Rule

The presenters' eval framework runs each scenario both with and without the skill, scores each run with a rubric, and requires both a high absolute pass rate (~80–90%) *and* an improvement over the no-skill baseline. The Next.js installer regression is what made this a hard rule rather than a soft preference.

Wondermint's `evals/` directory should encode the same rule. Two follow-ups:

- For each existing eval scenario, ensure there is a paired no-skill run. If the with-skill version does not strictly exceed the without-skill version, that scenario is flagging a section of the skill that is currently neutral or harmful.
- The pass rate threshold should be calibrated against current Claude versions and reset whenever the model changes. The presenters mention that a model upgrade can make a previously-helpful skill redundant or actively harmful, so eval baselines should be re-run on every major model change before assuming the skill is still earning its keep.

### 7. Self-Improvement Via Transcript Review

The presenters' workflow: wait a week, then point Claude (or its bundled `skill-builder` / `skill-creator`) at the local JSONL conversation logs and ask it to identify spinning loops, repeated tool sequences, skipped steps, and recurring questions. Each of those is a candidate for a constraint to add to the skill, a reference file to extract, or a bang-backtick script to codify.

For Wondermint specifically, the questions to ask the skill-builder during a transcript review:

- Where did the agent ask the user for information that was already available via an API call (suggesting a missing bang-backtick block)?
- Where did the agent get the response shape wrong despite snake_case being documented (suggesting the constraint is not landing — perhaps it should be repeated near the relevant operation rather than only in the header)?
- Where did the agent fall back to GraphQL despite the explicit "REST only" rule (suggesting the negative trigger needs to appear in more places, or that specific endpoints are mistaken for GraphQL-shaped)?
- Where did the agent skip the operating-mode classification step before acting (suggesting the gate needs to be enforced as a constraint, not a recommendation)?

The pre-LLM-era impulse — wipe context on Friday, start fresh Monday — actively burns the most useful raw material the skill has. Failure transcripts are the richest source of refinement signal, so they should be retained until the skill author has reviewed them.

### 8. Cross-Harness Portability As A Distribution Channel

The presenters demonstrated the same skill folder running in Claude Code, Claude Desktop, Codex, Cursor, and Pi, plus a `.skill` zip workflow that lets non-technical teammates drag a skill into Claude Desktop. They explicitly highlighted a recruiting-team use case: non-engineers building and using skills that pull from Slack, Notion, and an ATS into uniform reports.

For Wondermint this is a real distribution surface. Wondermint's audience includes creators who are not developers. The implications:

- The Wondermint skill should be tested in Claude Desktop, not just Claude Code. Bang-backtick blocks that depend on a CLI environment may need fallbacks or alternative reference paths for Desktop users.
- A `.skill` zip artifact should be a published deliverable — installable by a non-technical creator with one drag-and-drop. The plan documentation should reference this distribution channel, not just the developer-oriented `claude mcp add`-style installation.
- The security constraints on API-key handling (already in `SKILL.md`) become more important in this distribution mode, because non-technical users are less likely to instinctively scrutinize where the key is being sent. The "never send the API key to any host other than the configured Wondermint API base URL" rule should arguably appear once per major section, not only in the header.

### 9. The Cognitive-Resistance Heuristic For Future Skills

The presenters' rule for what to turn into a skill next: "the nagging things you find the most cognitive resistance to doing every week." Zach Proser's first non-coding skill monitored Slack, deduped against Linear, and filed tickets without breaking flow.

For Wondermint, the same lens identifies the next-skill candidates — workflows where the existing skill currently helps but where the operator still feels friction:

- Bulk operations (cleaning up draft items, batch-editing tags, archiving old portfolios) where the operating-mode confirmation pattern would be tedious if applied per-item.
- Cross-platform posting (when a Wondermint upload should fan out to other social destinations) — explicitly outside the current skill's scope, but a candidate for a sibling skill that *delegates* to the Wondermint skill rather than absorbing it.
- Engagement triage (reviewing the day's notifications and comments and producing a recommended response set) — currently possible but high-friction, and a clean fit for a confidence-loop-gated skill.

Each of these is a separate, smaller skill that depends on the Wondermint skill rather than an extension of it. That is the composition pattern the workshop kept returning to: small skills, composed at runtime by description-based routing.

## What This Adds Beyond The Existing Research Notes

- The skill-builder video analysis already covered: progressive disclosure, frontmatter routing, eval-driven development, MCP-vs-skill boundaries.
- The gstack analysis already covered: strong trigger metadata, phased workflow patterns, gates, output artifacts.
- Skills at Scale adds: the empirical eval-baseline rule (with the Next.js cautionary tale), bang-backtick script interpolation for deterministic baselines, the confidence-scoring iterative-clarification pattern, and the cross-harness portability / non-technical distribution argument.

## Open Questions For The Wondermint Skill

- Which operations in the current skill are over-prescribed versus correctly constrained? An eval pass with the with-skill / without-skill rule will surface this.
- Where in `SKILL.md` is a bang-backtick block worth more than the equivalent inline instruction? The plan, account state, and recent-activity blocks are the strongest candidates; the rest should be evaluated case by case.
- Should the Wondermint skill ship a `.skill` zip artifact for Claude Desktop installation, and if so, what does the install path look like for a non-technical creator?
- Does the operating-mode table want a routing layer (per-mode reference files) or is the inline table the right level of disclosure given how often modes are referenced together?
