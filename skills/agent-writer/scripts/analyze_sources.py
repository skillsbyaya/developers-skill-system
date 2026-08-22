# /// script
# /// requires-python = ">=3.10"
# /// dependencies = []
# ///
"""Enumerate text sources and estimate scale for document distillation."""

from __future__ import annotations

import argparse
import glob
import json
import os
from pathlib import Path

INCLUDE_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".csv"}
SKIP_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "venv"}
CHARS_PER_TOKEN = 4
INLINE_MAX_TOKENS = 12_000
SINGLE_OUTPUT_MAX_TOKENS = 5_000


def resolve_inputs(inputs: list[str]) -> list[Path]:
    """Resolve files, folders, and globs to unique eligible files."""
    files: list[Path] = []
    for item in inputs:
        path = Path(item)
        if path.is_file():
            files.append(path.resolve())
        elif path.is_dir():
            for root, dirs, filenames in os.walk(path):
                dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
                for filename in sorted(filenames):
                    candidate = Path(root) / filename
                    if candidate.suffix.lower() in INCLUDE_EXTENSIONS:
                        files.append(candidate.resolve())
        else:
            for match in sorted(glob.glob(item, recursive=True)):
                candidate = Path(match)
                if candidate.is_file() and candidate.suffix.lower() in INCLUDE_EXTENSIONS:
                    files.append(candidate.resolve())

    seen: set[Path] = set()
    unique: list[Path] = []
    for path in files:
        if path not in seen:
            seen.add(path)
            unique.append(path)
    return unique


def build_analysis(inputs: list[str]) -> dict:
    """Return a JSON-serializable source inventory and advisory scale hints."""
    files = resolve_inputs(inputs)
    if not files:
        return {
            "status": "error",
            "error": "No readable supported text files found",
            "inputs": inputs,
        }

    details = []
    total_bytes = 0
    for path in files:
        size = path.stat().st_size
        total_bytes += size
        details.append(
            {
                "path": str(path),
                "filename": path.name,
                "size_bytes": size,
                "estimated_tokens": max(1, size // CHARS_PER_TOKEN),
            }
        )

    total_tokens = max(1, total_bytes // CHARS_PER_TOKEN)
    estimated_output_tokens = max(1, total_tokens // 3)
    partition = len(files) > 3 or total_tokens > INLINE_MAX_TOKENS
    split = estimated_output_tokens > SINGLE_OUTPUT_MAX_TOKENS

    return {
        "status": "ok",
        "files": details,
        "summary": {
            "total_files": len(files),
            "total_size_bytes": total_bytes,
            "total_estimated_tokens": total_tokens,
        },
        "routing": {
            "recommendation": "partition" if partition else "inline",
            "reason": (
                f"{len(files)} file(s), ~{total_tokens:,} estimated tokens; "
                f"{'partition into coherent groups' if partition else 'one coherent reading pass is plausible'}"
            ),
        },
        "split_prediction": {
            "prediction": "consider" if split else "unlikely",
            "estimated_output_tokens": estimated_output_tokens,
            "reason": (
                f"rough output estimate ~{estimated_output_tokens:,} tokens; "
                f"{'test semantic splitting after compression' if split else 'a single output is likely sufficient'}"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="File, folder, or glob inputs")
    args = parser.parse_args()
    print(json.dumps(build_analysis(args.inputs), indent=2))


if __name__ == "__main__":
    main()
