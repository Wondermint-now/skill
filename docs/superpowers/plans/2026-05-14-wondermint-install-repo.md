# Wondermint Install Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `Wondermint-now/skill` from a raw skill package into a here.now-style installation repository that supports `npx skills`, fallback shell install, and Codex/Cursor plugin metadata.

**Architecture:** Keep one canonical generated package surface under `wondermint/`, then mirror the same files into `skills/wondermint/` for `npx skills` compatibility. Treat the current root `SKILL.md`, `CHECK_IN.md`, and `skills/` files as the source content for this migration, but do not keep root `SKILL.md` as the public install surface because `npx skills` discovery currently fails on the repo.

**Tech Stack:** Markdown skill files, shell installer, JSON plugin manifests, `npx skills`, GitHub archive URLs, existing Wondermint validation script from `/Users/ashokaji/code/fullstock/Wondermint Skill File/repo-workflows/validate.py`.

---

## Success Criteria

- `npx -y skills@1.5.7 add Wondermint-now/skill --list` finds exactly one skill named `wondermint`.
- `npx -y skills@1.5.7 add Wondermint-now/skill --skill wondermint -g --copy -y` can install the skill in a disposable HOME.
- `WONDERMINT_SKILL_ARCHIVE_URL=<local-or-branch-archive> bash install.sh` can install the same package in a disposable HOME before merge, and `bash install.sh` works from `main` after merge.
- The fallback installer installs to exactly one skill directory by default, matching the here.now fallback model. Agent-specific installs across Codex, Claude, Cursor, and other agents are handled by `npx skills`.
- `.codex-plugin/plugin.json` and `.cursor-plugin/plugin.json` exist with Wondermint metadata and a logo path.
- No Wondermint credentials, `.env`, eval artifacts, repo workflow docs, or backend-only references enter any installable package path.

## File Structure

- Create `README.md`: public install instructions and support matrix.
- Create `install.sh`: npm-free fallback installer.
- Create `.codex-plugin/plugin.json`: Codex plugin marketplace metadata.
- Create `.cursor-plugin/plugin.json`: Cursor plugin metadata.
- Create `assets/logo.svg`: placeholder or real Wondermint logo for plugin manifests.
- Create `wondermint/`: canonical installable skill package.
- Create `skills/wondermint/`: mirror for `npx skills` discovery and installs.
- Create `scripts/sync-package.sh`: repo-maintenance script that copies canonical package files into mirrors.
- Modify root layout: move current root package files into `wondermint/`; do not leave a root `SKILL.md` unless later testing proves `npx skills` can parse it cleanly.

---

### Task 1: Create a Branch and Baseline Checks

**Files:**
- No file changes.

- [ ] **Step 1: Create the working branch**

Run:

```bash
git switch main
git pull --ff-only
git switch -c addWondermint-install-repo
```

Expected: new branch `addWondermint-install-repo`.

- [ ] **Step 2: Confirm current CLI discovery fails**

Run:

```bash
npx -y skills@1.5.7 add Wondermint-now/skill --list
```

Expected before implementation: `No skills found`.

- [ ] **Step 3: Confirm source package validation still passes**

Run:

```bash
python3 "/Users/ashokaji/code/fullstock/Wondermint Skill File/repo-workflows/validate.py"
```

Expected: `Wondermint validation passed.`

---

### Task 2: Normalize Skill Frontmatter for CLI Parsing

**Files:**
- Modify: `SKILL.md`

- [ ] **Step 1: Replace inline frontmatter description with block YAML**

Change the top of `SKILL.md` from an inline `description:` value to:

```markdown
---
name: wondermint
description: >
  Use when the user wants to interact with Wondermint: checking home,
  check-in, updates, platform updates, or the frontend Agentic Dashboard;
  uploading or managing AI-generated items; browsing Wondermint content;
  liking, favoriting, commenting, replying, following, sharing, downloading;
  responding to notifications; organizing or queueing portfolios, playlists,
  or feeds; managing account or billing; registering webhooks; or calling the
  Wondermint API. Do not use for generic AI image/audio/video generation,
  generic social posting, unrelated Stripe work, or unrelated API tasks unless
  the result should be posted to or managed on Wondermint.
---
```

Rationale: the current inline string contains colons and semicolons that are valid in some YAML contexts but appear to break `npx skills` discovery.

- [ ] **Step 2: Validate source package after frontmatter edit**

Run:

```bash
python3 "/Users/ashokaji/code/fullstock/Wondermint Skill File/repo-workflows/validate.py"
```

Expected: `Wondermint validation passed.`

- [ ] **Step 3: Commit the frontmatter normalization**

Run:

```bash
git add SKILL.md
git commit -m "chore: normalize skill frontmatter"
```

---

### Task 3: Create Canonical Package Directory

**Files:**
- Create: `wondermint/SKILL.md`
- Create: `wondermint/CHECK_IN.md`
- Create: `wondermint/skills/**`
- Delete or move from root after copy: `SKILL.md`, `CHECK_IN.md`, root `skills/`

- [ ] **Step 1: Create canonical directory from the current package**

Run:

```bash
mkdir -p wondermint
cp SKILL.md CHECK_IN.md wondermint/
cp -R skills wondermint/
```

- [ ] **Step 2: Remove root package files after confirming copy**

Run:

```bash
diff -qr SKILL.md wondermint/SKILL.md
diff -qr CHECK_IN.md wondermint/CHECK_IN.md
diff -qr skills wondermint/skills
rm -rf SKILL.md CHECK_IN.md skills
```

Expected: both `diff` commands produce no output before deletion.

- [ ] **Step 3: Verify canonical package contains only installable files**

Run:

```bash
find wondermint -type f | sort
rg -n "evals/|repo-workflows|research/|references/backend-endpoints|mvp-scope|START_HERE|PROGRESS|PLAN" wondermint || true
```

Expected: package files are under `wondermint/`; `rg` prints nothing.

---

### Task 4: Add Mirror Sync Script

**Files:**
- Create: `scripts/sync-package.sh`

- [ ] **Step 1: Create sync script**

Create `scripts/sync-package.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CANONICAL_DIR="${ROOT_DIR}/wondermint"

[[ -f "${CANONICAL_DIR}/SKILL.md" ]] || {
  echo "error: missing ${CANONICAL_DIR}/SKILL.md" >&2
  exit 1
}

sync_to() {
  local target="$1"
  rm -rf "$target"
  mkdir -p "$(dirname "$target")"
  cp -R "$CANONICAL_DIR" "$target"
}

sync_to "${ROOT_DIR}/skills/wondermint"

echo "synced Wondermint package mirrors"
```

- [ ] **Step 2: Make it executable and run it**

Run:

```bash
chmod +x scripts/sync-package.sh
./scripts/sync-package.sh
```

Expected:

```text
synced Wondermint package mirrors
```

- [ ] **Step 3: Verify mirrors match canonical package**

Run:

```bash
diff -qr wondermint skills/wondermint
```

Expected: no output.

- [ ] **Step 4: Commit package layout and sync script**

Run:

```bash
git add wondermint skills/wondermint scripts/sync-package.sh
git add -u
git commit -m "chore: add installable skill package layout"
```

---

### Task 5: Add Fallback Installer

**Files:**
- Create: `install.sh`

- [ ] **Step 1: Create installer**

Create `install.sh`. Use a GitHub archive instead of trying to recursively download raw directory URLs; GitHub raw URLs do not expose directories, and the GitHub tree API returns JSON rather than a plain file manifest.

```bash
#!/usr/bin/env bash
set -euo pipefail

ARCHIVE_URL="${WONDERMINT_SKILL_ARCHIVE_URL:-https://github.com/Wondermint-now/skill/archive/refs/heads/main.tar.gz}"
SKILL_DIR="${WONDERMINT_SKILL_DIR:-${HOME}/.claude/skills/wondermint}"

die() {
  echo "error: $1" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "requires $1"
}

atomic_download() {
  local url="$1"
  local destination="$2"
  local tmp

  mkdir -p "$(dirname "$destination")"
  tmp="$(mktemp "${destination}.tmp.XXXXXX")"
  curl -fsSL "$url" -o "$tmp"
  mv "$tmp" "$destination"
}

echo "Installing Wondermint skill..."

need_cmd curl
need_cmd mktemp
need_cmd mv
need_cmd tar

tmp_dir="$(mktemp -d)"
archive="${tmp_dir}/wondermint-skill.tar.gz"
extract_dir="${tmp_dir}/extract"
package_dir=""

cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

mkdir -p "$extract_dir"
atomic_download "$ARCHIVE_URL" "$archive"
tar -xzf "$archive" -C "$extract_dir"

for candidate in "$extract_dir"/wondermint "$extract_dir"/*/wondermint; do
  if [[ -f "$candidate/SKILL.md" ]]; then
    package_dir="$candidate"
    break
  fi
done

[[ -n "$package_dir" ]] || die "archive does not contain wondermint/SKILL.md"
[[ -f "$package_dir/CHECK_IN.md" ]] || die "archive does not contain wondermint/CHECK_IN.md"
[[ -d "$package_dir/skills" ]] || die "archive does not contain wondermint/skills"

rm -rf "$SKILL_DIR"
mkdir -p "$(dirname "$SKILL_DIR")"
cp -R "$package_dir" "$SKILL_DIR"

echo ""
echo "done - Wondermint skill installed to ${SKILL_DIR}"
echo "restart Claude Code/Cowork to start using it"
```

- [ ] **Step 2: Test installer in disposable HOME from local archive**

Run:

```bash
tmp_home="$(mktemp -d)"
tmp_archive_dir="$(mktemp -d)"
tmp_archive="$tmp_archive_dir/wondermint-skill.tar.gz"
tmp_tree="$tmp_archive_dir/Wondermint-skill-main"
mkdir -p "$tmp_tree"
rsync -a --exclude='.git' --exclude='.tmp' ./ "$tmp_tree/"
tar -czf "$tmp_archive" -C "$tmp_archive_dir" Wondermint-skill-main
HOME="$tmp_home" WONDERMINT_SKILL_ARCHIVE_URL="file://$tmp_archive" bash install.sh
find "$tmp_home/.claude/skills/wondermint" -type f | sort
diff -qr wondermint "$tmp_home/.claude/skills/wondermint"
test ! -e "$tmp_home/.codex/skills/wondermint"
test ! -e "$tmp_home/.cursor/skills/wondermint"
rm -rf "$tmp_home" "$tmp_archive_dir"
```

Expected: installer prints success; `diff` produces no output.

- [ ] **Step 3: Commit installer**

Run:

```bash
chmod +x install.sh
git add install.sh
git commit -m "chore: add fallback installer"
```

---

### Task 6: Add Plugin Metadata and Logo

**Files:**
- Create: `.codex-plugin/plugin.json`
- Create: `.cursor-plugin/plugin.json`
- Create: `assets/logo.svg`

- [ ] **Step 1: Add Codex plugin manifest**

Create `.codex-plugin/plugin.json`:

```json
{
  "name": "wondermint",
  "version": "0.1.0",
  "description": "Interact with Wondermint, the social platform for AI-generated images, video, and audio.",
  "author": { "name": "Wondermint", "url": "https://wondermint.now" },
  "homepage": "https://wondermint.now",
  "repository": "https://github.com/Wondermint-now/skill",
  "license": "MIT",
  "keywords": ["wondermint", "ai-art", "ai-video", "ai-audio", "social", "agents", "uploads"],
  "interface": {
    "displayName": "Wondermint",
    "shortDescription": "Manage Wondermint uploads, discovery, social actions, folders, and account flows.",
    "longDescription": "Wondermint is a social platform for AI-generated images, video, and audio. This skill helps agents check in, upload and manage items, browse and engage with content, respond to comments and notifications, organize portfolios, playlists, and feeds, and handle account or billing flows through the Wondermint API.",
    "developerName": "Wondermint",
    "category": "Productivity",
    "websiteURL": "https://wondermint.now",
    "logo": "./assets/logo.svg"
  }
}
```

- [ ] **Step 2: Add Cursor plugin manifest**

Create `.cursor-plugin/plugin.json`:

```json
{
  "name": "wondermint",
  "description": "Interact with Wondermint, the social platform for AI-generated images, video, and audio.",
  "version": "0.1.0",
  "author": { "name": "Wondermint" },
  "homepage": "https://wondermint.now",
  "repository": "https://github.com/Wondermint-now/skill",
  "license": "MIT",
  "keywords": ["wondermint", "ai-art", "ai-video", "ai-audio", "social", "agents", "uploads"],
  "logo": "assets/logo.svg"
}
```

- [ ] **Step 3: Add placeholder logo**

Create `assets/logo.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-labelledby="title desc">
  <title id="title">Wondermint</title>
  <desc id="desc">Wondermint skill logo</desc>
  <rect width="128" height="128" rx="24" fill="#101820"/>
  <circle cx="46" cy="48" r="22" fill="#59d6c4"/>
  <circle cx="82" cy="80" r="22" fill="#ffcf5a"/>
  <path d="M36 82c18-26 38-38 60-38" fill="none" stroke="#ffffff" stroke-width="10" stroke-linecap="round"/>
</svg>
```

Replace this with official brand art if available.

- [ ] **Step 4: Validate JSON**

Run:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .cursor-plugin/plugin.json >/dev/null
```

Expected: both commands exit 0.

- [ ] **Step 5: Commit metadata**

Run:

```bash
git add .codex-plugin/plugin.json .cursor-plugin/plugin.json assets/logo.svg
git commit -m "chore: add plugin metadata"
```

---

### Task 7: Add Public README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Create README**

Create `README.md`:

```markdown
# Wondermint Skill

Wondermint is a social platform for AI-generated images, video, and audio. This repository distributes the Wondermint agent skill for checking in, uploading and managing items, browsing and engaging with content, organizing portfolios/playlists/feeds, and handling account flows through the Wondermint API.

## Install

```bash
npx skills add Wondermint-now/skill --skill wondermint -g
```

To install for a specific agent:

```bash
npx skills add Wondermint-now/skill --skill wondermint -g --agent codex
npx skills add Wondermint-now/skill --skill wondermint -g --agent claude-code
npx skills add Wondermint-now/skill --skill wondermint -g --agent cursor
```

Or without npm:

```bash
curl -fsSL https://raw.githubusercontent.com/Wondermint-now/skill/main/install.sh | bash
```

The fallback installer follows the Claude-style install path: `~/.claude/skills/wondermint`.
Use `npx skills` when installing for Codex, Cursor, or another supported agent.

## Install via Plugins

**Codex** - install from the plugin directory in the Codex app or CLI.

**Cursor** - install from Cursor plugin support when available.

## Usage

After installation, restart your agent. Ask it to use Wondermint for check-ins, uploads, discovery, comments, notifications, folders, account setup, billing flows, or Wondermint API work.

## Security

Store Wondermint API keys only in environment variables, local `.env` files, password managers, or the host agent's approved secret store. Never commit credentials.

## Website

Wondermint: https://wondermint.now
```

- [ ] **Step 2: Commit README**

Run:

```bash
git add README.md
git commit -m "docs: add install instructions"
```

---

### Task 8: Validate All Install Paths

**Files:**
- No file changes unless validation exposes a bug.

- [ ] **Step 1: Validate `npx skills` discovery**

Run:

```bash
npx -y skills@1.5.7 add . --list
```

Expected: one skill named `wondermint`.

- [ ] **Step 2: Validate `npx skills` local install in disposable HOME**

Run:

```bash
tmp_home="$(mktemp -d)"
HOME="$tmp_home" npx -y skills@1.5.7 add . --skill wondermint -g --copy -y
find "$tmp_home/.codex/skills" "$tmp_home/.claude/skills" -maxdepth 3 -type f 2>/dev/null | sort || true
rm -rf "$tmp_home"
```

Expected: command installs without error. The exact agent path may vary by detected agents.

- [ ] **Step 3: Validate mirrors**

Run:

```bash
./scripts/sync-package.sh
diff -qr wondermint skills/wondermint
```

Expected: sync succeeds; diff produces no output.

- [ ] **Step 4: Validate no repo-only references leaked**

Run:

```bash
rg -n "evals/|repo-workflows|research/|references/backend-endpoints|mvp-scope|START_HERE|PROGRESS|PLAN" wondermint skills/wondermint || true
```

Expected: no output.

- [ ] **Step 5: Validate source repo rules**

Run:

```bash
python3 "/Users/ashokaji/code/fullstock/Wondermint Skill File/repo-workflows/validate.py"
```

Expected: `Wondermint validation passed.`

---

### Task 9: Push and Open PR

**Files:**
- No file changes.

- [ ] **Step 1: Check final diff**

Run:

```bash
git status --short --branch
git log --oneline --decorate -8
```

Expected: working tree clean except intended uncommitted changes, if any.

- [ ] **Step 2: Commit final validation fixups if needed**

If any validation fixups were required:

```bash
git add README.md install.sh .codex-plugin/plugin.json .cursor-plugin/plugin.json assets/logo.svg wondermint skills/wondermint scripts/sync-package.sh
git commit -m "chore: fix install repository validation"
```

- [ ] **Step 3: Push branch**

Run:

```bash
git push -u origin addWondermint-install-repo
```

- [ ] **Step 4: Open PR**

Run:

```bash
gh pr create \
  --repo Wondermint-now/skill \
  --base main \
  --head addWondermint-install-repo \
  --title "Add Wondermint install repository support" \
  --body "## Summary
- Restructure the Wondermint skill repo for installer discovery.
- Add npx skills, plugin, and fallback shell install surfaces.
- Add validation and sync workflow for mirrored package paths.

## Validation
- npx skills discovery/install checks
- fallback install.sh check in disposable HOME
- mirror diff checks
- Wondermint skill validation"
```

Expected: PR URL is printed.

---

## Follow-Up Decisions

- Whether `assets/logo.svg` should use official Wondermint brand art.
- Whether to host `install.sh` at `https://wondermint.now/install.sh`.
- Whether to publish plugin metadata into any external marketplace beyond repository metadata.

## Self-Review

- Spec coverage: plan covers `npx skills`, fallback installer, Codex, Cursor, README, metadata, mirrored package paths, and validation.
- Placeholder scan: no implementation step uses TODO/TBD language. The only intentionally deferred item is replacing placeholder logo art with official brand art.
- Type/path consistency: canonical package is always `wondermint/`; the installer mirror is always `skills/wondermint/`.
