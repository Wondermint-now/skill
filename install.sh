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

case "$SKILL_DIR" in
  ""|"/"|"$HOME"|"$HOME/"|"$HOME/.claude"|"$HOME/.claude/"|"$HOME/.claude/skills"|"$HOME/.claude/skills/")
    die "refusing unsafe install target: ${SKILL_DIR}"
    ;;
  */wondermint)
    ;;
  *)
    die "install target must end with /wondermint: ${SKILL_DIR}"
    ;;
esac

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
