#!/usr/bin/env python3
"""Static validation for the Wondermint skill repo."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLABLE_ROOTS = [ROOT / "SKILL.md", ROOT / "CHECK_IN.md", ROOT / "skills"]
REPO_ONLY_RE = re.compile(
    r"(?:^|/)(evals|repo-workflows|research|references/backend-endpoints|mvp-scope)(?:/|\.md|$)"
)
SECRET_RE = re.compile(
    r"(mk_live_[A-Za-z0-9_-]{10,}|WONDERMINT_API_KEY=.+|WONDERMINT_PASSWORD=.+)"
)
GRAPHQL_RE = re.compile(r"GraphQL|graphql|/graphql|query \{|mutation \{")
GRAPHQL_ALLOWED_RE = re.compile(
    r"REST-only|must not use GraphQL|GraphQL is not available|GraphQL operations are backend-awareness material"
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def installable_markdown_files() -> list[Path]:
    files: list[Path] = []
    for root in INSTALLABLE_ROOTS:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(sorted(root.rglob("*.md")))
    return files


def repo_markdown_files() -> list[Path]:
    return [
        path
        for path in sorted(ROOT.rglob("*.md"))
        if ".git" not in path.parts and ".tmp" not in path.parts
    ]


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def is_external_link(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target)) or target.startswith("#")


def check_frontmatter(errors: list[str]) -> None:
    skill = ROOT / "SKILL.md"
    text = skill.read_text()
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return

    try:
        _, frontmatter, _ = text.split("---", 2)
    except ValueError:
        errors.append("SKILL.md frontmatter must be closed")
        return

    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()

    for required in ("name", "description", "updated"):
        if not fields.get(required):
            errors.append(f"SKILL.md frontmatter missing `{required}`")

    description = fields.get("description", "")
    if not description.startswith("Use when "):
        errors.append("SKILL.md description must start with `Use when `")
    if "Do not use" not in description:
        errors.append("SKILL.md description must include negative trigger space")


def check_repo_only_links(errors: list[str]) -> None:
    for path in installable_markdown_files():
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            if REPO_ONLY_RE.search(line):
                errors.append(f"{rel}:{lineno}: installable docs reference repo-only material")


def check_graphql(errors: list[str]) -> None:
    for path in installable_markdown_files():
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            if GRAPHQL_RE.search(line) and not GRAPHQL_ALLOWED_RE.search(line):
                errors.append(f"{rel}:{lineno}: GraphQL mention is not REST-only prohibition language")


def check_secrets(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or ".tmp" in path.parts:
            continue
        if path.name == "validate.py":
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(text.splitlines(), 1):
            if SECRET_RE.search(line):
                if rel == Path(".env.example"):
                    continue
                if "rg -n" in line and ("WONDERMINT_API_KEY" in line or "mk_live_" in line):
                    continue
                errors.append(f"{rel}:{lineno}: possible secret or populated credential")


def check_links(errors: list[str]) -> None:
    for path in repo_markdown_files():
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            for match in LINK_RE.finditer(line):
                raw_target = match.group(1).split(None, 1)[0]
                target = strip_anchor(raw_target)
                if not target or is_external_link(target):
                    continue
                if target.startswith("/"):
                    errors.append(f"{rel}:{lineno}: absolute local markdown link `{raw_target}`")
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    errors.append(f"{rel}:{lineno}: broken markdown link `{raw_target}`")


def main() -> int:
    errors: list[str] = []
    check_frontmatter(errors)
    check_repo_only_links(errors)
    check_graphql(errors)
    check_secrets(errors)
    check_links(errors)

    if errors:
        print("Wondermint validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Wondermint validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
