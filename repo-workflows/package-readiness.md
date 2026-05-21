# Package Readiness Workflow

This workflow checks whether a Wondermint skill variant can be installed as a
clean skill package. It is not part of the installable Wondermint skill.

## Installable Surface

The core installable packages are exactly:

- `wondermint/SKILL.md`
- `wondermint/CHECK_IN.md`
- `wondermint/skills/`
- `skills/wondermint/SKILL.md`
- `skills/wondermint/CHECK_IN.md`
- `skills/wondermint/skills/`

The marketplace installable packages are exactly:

- `wondermint-marketplace/SKILL.md`
- `wondermint-marketplace/CHECK_IN.md`
- `wondermint-marketplace/skills/`
- `skills/wondermint-marketplace/SKILL.md`
- `skills/wondermint-marketplace/CHECK_IN.md`
- `skills/wondermint-marketplace/skills/`

Do not include `PROGRESS.md`, `PLAN.md`, `START_HERE.md`, `repo-workflows/`,
`evals/`, `research/`, `references/`, `.tmp/`, `.env`, or local credentials.

## Readiness Checks

Run static validation first. Use `--variant core`, `--variant marketplace`, or
`--variant all`:

```bash
python3 repo-workflows/validate.py --variant all
```

Build an isolated package copy under `.tmp/`, replacing `<package>` with
`wondermint` or `wondermint-marketplace`:

```bash
rm -rf .tmp/package-readiness
mkdir -p .tmp/package-readiness
cp -R <package> .tmp/package-readiness/<package>
find .tmp/package-readiness/<package> -type f | sort
```

Build a drag-and-drop `.skill` artifact for distribution testing:

```bash
rm -f .tmp/package-readiness/<package>.skill
(cd .tmp/package-readiness && zip -qr <package>.skill <package>)
unzip -l .tmp/package-readiness/<package>.skill | sort
```

The artifact must contain only that package's `SKILL.md`, `CHECK_IN.md`, and
`skills/` files.

Check both package copies for repo-only references:

```bash
rg -n "evals/|repo-workflows|research/|references/backend-endpoints|mvp-scope|START_HERE|PROGRESS|PLAN" wondermint skills/wondermint wondermint-marketplace skills/wondermint-marketplace
```

That command should return no matches.

Check package size:

```bash
wc -l -w wondermint/SKILL.md skills/wondermint/SKILL.md wondermint-marketplace/SKILL.md skills/wondermint-marketplace/SKILL.md
find wondermint/skills skills/wondermint/skills wondermint-marketplace/skills skills/wondermint-marketplace/skills -name '*.md' -maxdepth 3 -print | sort | xargs wc -l
```

Check the `.skill` artifact for excluded files:

```bash
unzip -l .tmp/package-readiness/<package>.skill | rg "<package>/(evals/|repo-workflows/|research/|references/|PROGRESS.md|PLAN.md|START_HERE.md|\\.env)|\\.DS_Store" && exit 1 || true
```

## Local Install Drift Check

If a local install exists, compare it before syncing. Replace `<package>` and
`<install_dir>` with the target variant values:

```bash
find "<install_dir>" -maxdepth 3 -type f | sort
diff -qr <package> "<install_dir>"
```

Expected drift means the local installed copy is stale. Do not manually patch
the installed copy. Rebuild from the package surface.

## Sync Command

Only run this after validation passes and the owner wants to update the local
installed skill. Use `wondermint` for core or `wondermint-marketplace` for the
marketplace variant:

```bash
install_dir="$HOME/.codex/skills/wondermint"
package="wondermint"
test "$install_dir" = "$HOME/.codex/skills/wondermint" -o "$install_dir" = "$HOME/.codex/skills/wondermint-marketplace"
rm -rf "$install_dir"
mkdir -p "$install_dir"
cp -R "$package/." "$install_dir/"
```

After syncing, rerun the local install drift check. It should be clean.

## Future Packaging

`agents/openai.yaml` is recommended by Skill Creator for UI metadata. Add it
only when preparing an install/distribution release, and validate that it still
matches the package root `SKILL.md` files.

For creator-facing distribution, treat `.tmp/package-readiness/<package>.skill`
as the review artifact. Do not publish it until validation passes, package
contents are inspected, the scorecard names the variant, and the owner approves
distribution.
