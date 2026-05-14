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
