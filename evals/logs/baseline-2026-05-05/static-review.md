# Baseline Static Review

## Metadata

- Eval name: `baseline-2026-05-05`
- Date: 2026-05-05
- Branch: `chore/initial-skill-files`
- Commit reviewed: `252124e`
- Eval type: static skill-file review
- Live Wondermint API tests: not run

## Commands Run

```bash
git status --short
git branch --show-current
git rev-parse --short HEAD
find . -maxdepth 3 -type f | sort
wc -l SKILL.md CHECK_IN.md skills/*.md skills/references/categories.md evals/templates/scorecard.md
sed -n '1,90p' SKILL.md
sed -n '1,80p' CHECK_IN.md
rg -n "\\]\\(([^)#]+\\.md|[^)#]+\\.md#[^)]+)\\)" .
rg -n "mk_live_[A-Za-z0-9_\\-]+|WONDERMINT_API_KEY=.+|WONDERMINT_PASSWORD=.+|password\\s*[:=]\\s*['\\\"][^'\\\"]+" .
python3 /Users/ashokaji/.codex/skills/.system/skill-creator/scripts/quick_validate.py "/Users/ashokaji/code/fullstock/Wondermint Skill File"
```

## Observations

- The repo was clean before the eval began.
- The reviewed commit was `252124e`.
- The active branch was `chore/initial-skill-files`.
- The skill entrypoint is `SKILL.md`.
- The check-in workflow is `CHECK_IN.md`.
- Supporting domain files live under `skills/`.
- The active skill docs total 3,146 lines across root and support files.
- `SKILL.md` is 162 lines, which is manageable but already carrying more than pure routing.
- `skills/items.md` is the largest support file at 584 lines.
- Link search found many internal markdown links and no obvious missing target from the static review.
- Secret-pattern search did not find real-looking committed credentials. It found placeholder strings such as `mk_live_...`, `api_key`, and password documentation.

## Validator Result

The skill-creator validator could not run in this environment:

```text
ModuleNotFoundError: No module named 'yaml'
```

This means baseline validation is incomplete until PyYAML is available or the validator is run in an environment that already has it.

## Skill-Creator Review Notes

- The root `description` is strong for triggering: it names Wondermint, media uploads, social actions, folders, subscriptions, webhooks, notifications, and API interaction.
- The skill uses progressive disclosure partly: `SKILL.md` routes to `skills/auth.md`, `skills/items.md`, `skills/social.md`, and other focused files.
- The skill should keep moving detailed API examples and FAQs out of `SKILL.md` as it grows.
- The repo now contains repo-management docs, which are appropriate for this development repo but should not be confused with the installable skill package.
- Future packaging should decide whether the installable skill is the whole repo or a clean subfolder containing only skill-essential files.
- Some reference files are long enough that tables of contents would help agents preview scope before loading details.
- No live forward-testing was run.

## Recommended Next Work

1. Run Phase 2 G stack analysis and identify repo/skill structure patterns worth adopting.
2. Decide the final installable skill package boundary.
3. Add tables of contents to long reference files during the progressive-disclosure pass.
4. Add `agents/openai.yaml` later if this skill will be installed directly into Codex skill directories.
5. Re-run `quick_validate.py` once the Python environment has PyYAML.
