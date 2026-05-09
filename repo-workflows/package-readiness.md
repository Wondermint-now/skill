# Package Readiness Workflow

This workflow checks whether the Wondermint skill can be installed as a clean
skill package. It is not part of the installable Wondermint skill.

## Installable Surface

The installable package is exactly:

- `SKILL.md`
- `CHECK_IN.md`
- `skills/`

Do not include `PROGRESS.md`, `PLAN.md`, `START_HERE.md`, `repo-workflows/`,
`evals/`, `research/`, `references/`, `.tmp/`, `.env`, or local credentials.

## Readiness Checks

Run static validation first:

```bash
python3 repo-workflows/validate.py
```

Build an isolated package copy under `.tmp/`:

```bash
rm -rf .tmp/package-readiness
mkdir -p .tmp/package-readiness/wondermint
cp SKILL.md CHECK_IN.md .tmp/package-readiness/wondermint/
cp -R skills .tmp/package-readiness/wondermint/
find .tmp/package-readiness/wondermint -type f | sort
```

Build a drag-and-drop `.skill` artifact for distribution testing:

```bash
rm -f .tmp/package-readiness/wondermint.skill
(cd .tmp/package-readiness && zip -qr wondermint.skill wondermint)
unzip -l .tmp/package-readiness/wondermint.skill | sort
```

The artifact must contain only `wondermint/SKILL.md`,
`wondermint/CHECK_IN.md`, and `wondermint/skills/` files.

Check the package for repo-only references:

```bash
rg -n "evals/|repo-workflows|research/|references/backend-endpoints|mvp-scope|START_HERE|PROGRESS|PLAN" .tmp/package-readiness/wondermint
```

That command should return no matches.

Check the package size:

```bash
wc -l -w .tmp/package-readiness/wondermint/SKILL.md
find .tmp/package-readiness/wondermint/skills -name '*.md' -maxdepth 3 -print | sort | xargs wc -l
```

Check the `.skill` artifact for excluded files:

```bash
unzip -l .tmp/package-readiness/wondermint.skill | rg "wondermint/(evals/|repo-workflows/|research/|references/|PROGRESS.md|PLAN.md|START_HERE.md|\\.env)|\\.DS_Store" && exit 1 || true
```

## Local Install Drift Check

If a local install exists, compare it before syncing:

```bash
find "$HOME/.codex/skills/wondermint" -maxdepth 3 -type f | sort
diff -qr .tmp/package-readiness/wondermint "$HOME/.codex/skills/wondermint"
```

Expected drift means the local installed copy is stale. Do not manually patch
the installed copy. Rebuild from the package surface.

## Sync Command

Only run this after validation passes and the owner wants to update the local
installed skill:

```bash
install_dir="$HOME/.codex/skills/wondermint"
test "$install_dir" = "$HOME/.codex/skills/wondermint"
rm -rf "$install_dir"
mkdir -p "$install_dir"
cp SKILL.md CHECK_IN.md "$install_dir/"
cp -R skills "$install_dir/"
```

After syncing, rerun the local install drift check. It should be clean.

## Future Packaging

`agents/openai.yaml` is recommended by Skill Creator for UI metadata. Add it
only when preparing an install/distribution release, and validate that it still
matches `SKILL.md`.

For creator-facing distribution, treat `.tmp/package-readiness/wondermint.skill`
as the review artifact. Do not publish it until validation passes, package
contents are inspected, and the owner approves distribution.
