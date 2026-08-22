#!/usr/bin/env python3
"""Extract compact current persona briefs from canonical skill metadata."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path.home() / ".claude" / "skills"
VALID_SKILL = re.compile(r"^agent-[a-z0-9-]+$")
STANCE_PREFIX = "When the user asks for "


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
        if isinstance(parsed, str):
            return parsed
    return value


def parse_frontmatter(lines: list[str], skill: str) -> tuple[str, str]:
    if not lines or lines[0] != "---":
        raise ValueError(f"missing frontmatter: {skill}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"unterminated frontmatter: {skill}") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = unquote(value)

    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != skill:
        raise ValueError(f"name mismatch for persona skill: {skill}")
    if not description:
        raise ValueError(f"missing description: {skill}")
    return name, description


def extract(skill: str) -> str:
    if not VALID_SKILL.fullmatch(skill):
        raise ValueError(f"invalid persona skill name: {skill}")

    path = ROOT / skill / "SKILL.md"
    if not path.is_file():
        raise ValueError(f"unknown persona skill: {skill}")

    lines = path.read_text(encoding="utf-8").splitlines()
    _, description = parse_frontmatter(lines, skill)
    stance = next(
        (line.strip() for line in lines if line.startswith(STANCE_PREFIX)),
        "",
    )
    if not stance:
        raise ValueError(f"missing opening consultation stance: {skill}")

    scope = re.split(r" Use (?:for|when) ", description, maxsplit=1)[0].strip()
    return f"### {skill}\n\nScope: {scope}\n\nStance: {stance}"


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "usage: extract-persona-briefs.py <agent-skill> [<agent-skill> ...]",
            file=sys.stderr,
        )
        raise SystemExit(2)

    try:
        briefs = [extract(skill) for skill in dict.fromkeys(sys.argv[1:])]
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2) from exc

    print("\n\n".join(briefs))


if __name__ == "__main__":
    main()
