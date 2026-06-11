#!/usr/bin/env python3
"""Static validation for the Wondermint skill repo."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VARIANTS = {
    "core": {
        "roots": [ROOT / "wondermint", ROOT / "skills" / "wondermint"],
        "skill_name": "wondermint",
    },
    "marketplace": {
        "roots": [ROOT / "skills" / "wondermint-marketplace"],
        "skill_name": "wondermint-marketplace",
    },
}
REPO_ONLY_RE = re.compile(
    r"(?:^|/)(evals|repo-workflows|research|references/backend-endpoints|mvp-scope)(?:/|\.md|$)"
)
SECRET_RE = re.compile(
    r"(mk_live_[A-Za-z0-9_-]{10,}|WONDERMINT_API_KEY=.+|WONDERMINT_PASSWORD=.+)"
)
GRAPHQL_RE = re.compile(r"GraphQL|graphql|/graphql|query \{|mutation \{")
GRAPHQL_ALLOWED_RE = re.compile(
    r"REST-only|must not use GraphQL|GraphQL is not available|GraphQL operations are backend-awareness material|Exclude GraphQL|Do not include.*GraphQL"
)
EXCLUSION_LANGUAGE_RE = re.compile(r"\b(do not|must not|exclude|excludes|excluded|excluding|no |not include|not add)\b", re.IGNORECASE)
CORE_MARKETPLACE_ONLY_RE = re.compile(
    r"\b(purchase|purchasing|buyer|seller|order management|seller analytics|marketplace analytics|payout|payouts|earnings|settlement)\b",
    re.IGNORECASE,
)
MARKETPLACE_EXCLUDED_RE = re.compile(
    r"(/api/v1/agents/(?:bids|offers|link)\b|/offers\b|/bids\b|/link\b|/graphql\b|query \{|mutation \{|(?<!non-)\bauctions?\b|\bbids?\b|\bcounter-?offers?\b|\boperator\b|\bclaim-?link\b|\bagent-?link\b)",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ONBOARDING_TRIGGER_RE = re.compile(
    r"\b(onboarding|get(?:ting)? started|set up|setup|register|connect(?:ing)? (?:my |your )?account)\b",
    re.IGNORECASE,
)


def package_roots_for(variant: str) -> list[Path]:
    if variant == "all":
        roots: list[Path] = []
        for config in VARIANTS.values():
            roots.extend(config["roots"])
        return roots
    return VARIANTS[variant]["roots"]


def installable_markdown_files(package_roots: list[Path]) -> list[Path]:
    files: list[Path] = []
    for root in package_roots:
        if root.is_dir():
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


def split_link_target(target: str) -> tuple[str, str | None]:
    if "#" not in target:
        return target, None
    path, anchor = target.split("#", 1)
    return path, anchor


def is_external_link(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target)) or target.startswith("#")


def github_slug(heading: str) -> str:
    text = re.sub(r"<[^>]*>", "", heading)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text)
    text = re.sub(r"\s", "-", text.strip().lower())
    return text.strip("-")


def markdown_anchors(path: Path) -> set[str]:
    counts: dict[str, int] = {}
    anchors: set[str] = set()
    for line in path.read_text().splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = github_slug(match.group(2))
        counts[base] = counts.get(base, 0) + 1
        anchors.add(base if counts[base] == 1 else f"{base}-{counts[base] - 1}")
    return anchors


def parse_frontmatter(frontmatter: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current_key: str | None = None
    folded = False
    folded_lines: list[str] = []

    def flush_folded() -> None:
        nonlocal current_key, folded, folded_lines
        if current_key and folded:
            fields[current_key] = " ".join(line.strip() for line in folded_lines).strip()
        current_key = None
        folded = False
        folded_lines = []

    for line in frontmatter.splitlines():
        match = FRONTMATTER_KEY_RE.match(line)
        if match:
            flush_folded()
            key, value = match.groups()
            current_key = key.strip()
            value = value.strip()
            if value in {">", "|"}:
                folded = True
                folded_lines = []
            else:
                fields[current_key] = value
                current_key = None
            continue

        if folded:
            folded_lines.append(line)

    flush_folded()
    return fields


def check_frontmatter(errors: list[str], variant: str, package_roots: list[Path]) -> None:
    expected_names = {
        config["skill_name"]
        for name, config in VARIANTS.items()
        if variant in {name, "all"}
    }
    for package_root in package_roots:
        skill = package_root / "SKILL.md"
        rel = skill.relative_to(ROOT)
        if not skill.exists():
            errors.append(f"{rel} is missing")
            continue

        text = skill.read_text()
        if not text.startswith("---\n"):
            errors.append(f"{rel} must start with YAML frontmatter")
            continue

        try:
            _, frontmatter, _ = text.split("---", 2)
        except ValueError:
            errors.append(f"{rel} frontmatter must be closed")
            continue

        fields = parse_frontmatter(frontmatter)

        for required in ("name", "description"):
            if not fields.get(required):
                errors.append(f"{rel} frontmatter missing `{required}`")

        name = fields.get("name", "")
        if name not in expected_names:
            expected = ", ".join(sorted(expected_names))
            errors.append(f"{rel} frontmatter name `{name}` must be one of: {expected}")

        description = fields.get("description", "")
        if not description.startswith("Use when "):
            errors.append(f"{rel} description must start with `Use when `")
        if "Do not use" not in description:
            errors.append(f"{rel} description must include negative trigger space")
        if len(description) > 1024:
            errors.append(f"{rel} description must be 1024 characters or fewer")
        if not ONBOARDING_TRIGGER_RE.search(description):
            errors.append(f"{rel} description must include onboarding/account setup trigger language")


def check_repo_only_links(errors: list[str], package_roots: list[Path]) -> None:
    for path in installable_markdown_files(package_roots):
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            if REPO_ONLY_RE.search(line):
                errors.append(f"{rel}:{lineno}: installable docs reference repo-only material")


def check_graphql(errors: list[str], package_roots: list[Path]) -> None:
    for path in installable_markdown_files(package_roots):
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            if GRAPHQL_RE.search(line) and not GRAPHQL_ALLOWED_RE.search(line):
                errors.append(f"{rel}:{lineno}: GraphQL mention is not REST-only prohibition language")


def check_variant_boundaries(errors: list[str], variant: str) -> None:
    if variant in {"core", "all"}:
        for path in installable_markdown_files(VARIANTS["core"]["roots"]):
            rel = path.relative_to(ROOT)
            for lineno, line in enumerate(path.read_text().splitlines(), 1):
                if CORE_MARKETPLACE_ONLY_RE.search(line):
                    errors.append(
                        f"{rel}:{lineno}: core variant references marketplace-only transactional scope"
                    )

    if variant in {"marketplace", "all"}:
        for root in VARIANTS["marketplace"]["roots"]:
            rel = root.relative_to(ROOT)
            marketplace_file = root / "skills" / "marketplace.md"
            if not marketplace_file.exists():
                errors.append(f"{rel}/skills/marketplace.md is required for marketplace variant")

        for path in installable_markdown_files(VARIANTS["marketplace"]["roots"]):
            rel = path.relative_to(ROOT)
            for lineno, line in enumerate(path.read_text().splitlines(), 1):
                if MARKETPLACE_EXCLUDED_RE.search(line) and not EXCLUSION_LANGUAGE_RE.search(line):
                    errors.append(
                        f"{rel}:{lineno}: marketplace variant references excluded GraphQL, auction/bid/offer, operator, or linking scope"
                    )


def check_secrets(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or ".tmp" in path.parts:
            continue
        if path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example"):
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
    anchors_by_path: dict[Path, set[str]] = {}
    for path in repo_markdown_files():
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            for match in LINK_RE.finditer(line):
                raw_target = match.group(1).split(None, 1)[0]
                target, anchor = split_link_target(raw_target)
                if not target or is_external_link(target):
                    continue
                if target.startswith("/"):
                    errors.append(f"{rel}:{lineno}: absolute local markdown link `{raw_target}`")
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    errors.append(f"{rel}:{lineno}: broken markdown link `{raw_target}`")
                    continue
                if anchor and resolved.suffix == ".md":
                    anchors = anchors_by_path.setdefault(resolved, markdown_anchors(resolved))
                    if anchor.lower() not in anchors:
                        errors.append(f"{rel}:{lineno}: broken markdown anchor `{raw_target}`")


def check_onboarding_routing(errors: list[str], package_roots: list[Path]) -> None:
    for package_root in package_roots:
        skill = package_root / "SKILL.md"
        start_here = package_root / "START_HERE.md"
        rel_skill = skill.relative_to(ROOT)
        rel_start = start_here.relative_to(ROOT)

        if skill.exists():
            text = skill.read_text()
            compact_text = re.sub(r"\s+", " ", text)
            if "Get started for the first time | [Wondermint Onboarding Flow](ONBOARDING_FLOW.md)" not in text:
                errors.append(f"{rel_skill}: get-started route must point to ONBOARDING_FLOW.md")
            if "For account registration, API-key access, or adding web login" not in compact_text:
                errors.append(f"{rel_skill}: account setup sub-flow must be scoped separately from full onboarding")

        if start_here.exists():
            text = start_here.read_text()
            if "If the user asked a specific task and credentials are available" not in text:
                errors.append(f"{rel_start}: incomplete onboarding must not hijack specific credentialed tasks")
            if "If the user asked a specific task but credentials are not available" not in text:
                errors.append(f"{rel_start}: missing specific-task account-setup route for keyless users")
            if "Skill file version or update checks bypass onboarding" not in text:
                errors.append(f"{rel_start}: skill-version checks must bypass onboarding")
            if "No local Wondermint setup was found" not in text:
                errors.append(f"{rel_start}: missing first-run local setup detection wording")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Wondermint skill packages.")
    parser.add_argument(
        "--variant",
        choices=["core", "marketplace", "all"],
        default="all",
        help="Variant to validate. Defaults to all.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    package_roots = package_roots_for(args.variant)
    errors: list[str] = []
    check_frontmatter(errors, args.variant, package_roots)
    check_repo_only_links(errors, package_roots)
    check_graphql(errors, package_roots)
    check_variant_boundaries(errors, args.variant)
    check_secrets(errors)
    check_links(errors)
    check_onboarding_routing(errors, package_roots)

    if errors:
        print("Wondermint validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Wondermint validation passed for variant: {args.variant}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
