# Package Readiness Scorecard

## Version

- Version/tag: package-readiness-2026-05-06
- Commit: `eec06d7` plus package-readiness workflow
- Date: 2026-05-06
- Evaluator: Codex static package review
- Eval type: package readiness review

## Summary

- Overall rating: 2 / 3
- Recommendation: package surface is ready; local installed copy needs an
  explicit sync before it should be treated as current
- Release blocking issues: no for repo package, yes for local installed copy
  freshness

The installable package surface is clean: `SKILL.md`, `CHECK_IN.md`, and
`skills/`. The isolated package copy contained 22 Markdown files, no repo-only
references, and root `SKILL.md` remained 144 lines / 1,152 words.

## Checks

| Check | Result | Evidence |
|---|---|---|
| Repo validation | Pass | `python3 repo-workflows/validate.py` |
| Installable surface | Pass | Isolated copy built under `.tmp/package-readiness/wondermint` with `SKILL.md`, `CHECK_IN.md`, and `skills/` |
| Repo-only references | Pass | No `evals/`, `repo-workflows`, `research/`, backend inventory, progress, plan, or start-here references in isolated package |
| Root size | Pass | `SKILL.md`: 144 lines / 1,152 words |
| Skill Creator shape | Pass | Root has `name` and `description`; bundled guidance lives in referenced files |
| Local install drift | Needs sync | `$HOME/.codex/skills/wondermint` still contains stale `HEARTBEAT.md`, lacks current flow files, and differs from repo `SKILL.md` |

## What Worked

- The repo already has a clean installable boundary.
- Token-efficiency work kept root `SKILL.md` compact enough for packaging.
- Focused flow files and references are all inside the installable `skills/`
  tree.
- No repo-development workflow, eval, research, backend-inventory, or planning
  content leaked into the package copy.

## Gaps

- The local installed copy is stale and should not be used as the current
  Wondermint skill until it is rebuilt from the package surface.
- There was no repo workflow documenting the package copy/sync process before
  this pass.
- `agents/openai.yaml` is still deferred. Skill Creator recommends it for UI
  metadata, but it is not required for current behavior.

## Recommended Changes

- Use `repo-workflows/package-readiness.md` for future package checks and local
  install syncs.
- Sync the local installed copy only after owner approval because it replaces
  the existing installed skill directory.
- Add `agents/openai.yaml` later when preparing distribution or UI listing
  polish.

## Raw Evidence

- `find .tmp/package-readiness/wondermint -type f | sort`
- `rg -n "evals/|repo-workflows|research/|references/backend-endpoints|mvp-scope|START_HERE|PROGRESS|PLAN" .tmp/package-readiness/wondermint`: no matches
- `wc -l -w .tmp/package-readiness/wondermint/SKILL.md`: 144 lines / 1,152 words
- `find $HOME/.codex/skills/wondermint -maxdepth 3 -type f`: local install contains `HEARTBEAT.md` and lacks current flow files
- `diff -qr SKILL.md $HOME/.codex/skills/wondermint/SKILL.md`: files differ
