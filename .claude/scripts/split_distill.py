#!/usr/bin/env python3
"""Parse a distill_<source>.md file into individual atom/molecule files.

Usage:
  Dry run:    python3 split_distill.py <distill_file>
  Execute:    python3 split_distill.py <distill_file> --execute
  With skips: python3 split_distill.py <distill_file> --execute --skip=file1.md,file2.md
  Cleanup:    python3 split_distill.py <distill_file> --execute --cleanup

Outputs JSON manifest to stdout.
Exit codes: 0 = success, 1 = parse error, 2 = collision found (dry run)
"""

import json
import os
import re
import sys
from pathlib import Path

# LaTeX normalization patterns
# Match \( ... \) for inline math (not preceded by $$)
INLINE_OPEN = re.compile(r"(?<!\$)\\\(")
INLINE_CLOSE = re.compile(r"\\\)(?!\$)")
# Match \[ ... \] for display math — only when \[ starts a line or has only whitespace before it
DISPLAY_OPEN = re.compile(r"^(\s*)\\\[", re.MULTILINE)
DISPLAY_CLOSE = re.compile(r"\\\](\s*)$", re.MULTILINE)


def normalize_latex(content: str) -> str:
    r"""Convert LaTeX delimiters to Obsidian-compatible format.

    \(...\) → $...$  (inline)
    \[...\] → $$...$$ (display, only when on own line)
    Preserves existing $...$ and $$...$$.
    """
    content = INLINE_OPEN.sub("$", content)
    content = INLINE_CLOSE.sub("$", content)
    content = DISPLAY_OPEN.sub(r"\1$$", content)
    content = DISPLAY_CLOSE.sub(r"$$\1", content)
    return content


def parse_sections(content: str) -> list[dict]:
    """Parse distill file into sections split on ## headings."""
    lines = content.split("\n")
    sections = []
    current_name = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("## "):
            # Save previous section
            if current_name is not None:
                sections.append({
                    "name": current_name,
                    "content": "\n".join(current_lines).strip(),
                })
            current_name = line[3:].strip()
            current_lines = []
        else:
            if current_name is not None:
                current_lines.append(line)

    # Save last section
    if current_name is not None:
        sections.append({
            "name": current_name,
            "content": "\n".join(current_lines).strip(),
        })

    return sections


def classify_name(name: str) -> str:
    """Classify file type from name."""
    stem = Path(name).stem
    if stem.startswith("__"):
        return "index"
    if stem.startswith("_"):
        return "molecule"
    return "atom"


def find_scratch_files(target_folder: Path, distill_path: Path) -> list[str]:
    """Find learn_* and progress_* scratch files in the target folder."""
    scratch = []
    for f in target_folder.iterdir():
        if not f.is_file() or not f.name.endswith(".md"):
            continue
        if f == distill_path:
            continue
        stem = f.stem
        if stem.startswith("learn_") or stem.startswith("progress_"):
            scratch.append(f.name)
    return scratch


def main():
    if len(sys.argv) < 2:
        print("Usage: split_distill.py <distill_file> [--execute] [--skip=f1,f2] [--cleanup]",
              file=sys.stderr)
        sys.exit(1)

    distill_path = Path(sys.argv[1]).resolve()
    if not distill_path.is_file():
        print(json.dumps({"error": f"File not found: {distill_path}"}))
        sys.exit(1)

    execute = "--execute" in sys.argv
    cleanup = "--cleanup" in sys.argv

    skip_files: set[str] = set()
    for arg in sys.argv:
        if arg.startswith("--skip="):
            skip_files = set(arg[7:].split(","))

    # Parse
    content = distill_path.read_text(encoding="utf-8")
    sections = parse_sections(content)

    if not sections:
        print(json.dumps({"error": "No ## headings found in distill file"}))
        sys.exit(1)

    target_folder = distill_path.parent

    # Check collisions
    existing_files = {f.name.lower(): f.name for f in target_folder.iterdir()
                      if f.is_file() and f.name.endswith(".md")}

    files = []
    has_collision = False
    for section in sections:
        name = section["name"]
        if not name.endswith(".md"):
            name += ".md"

        collision = name.lower() in existing_files and existing_files[name.lower()] != distill_path.name
        if collision:
            has_collision = True

        files.append({
            "name": name,
            "type": classify_name(name),
            "words": len(section["content"].split()),
            "collision": collision,
            "existing": str(target_folder / existing_files[name.lower()]) if collision else None,
        })

    scratch = find_scratch_files(target_folder, distill_path)

    manifest = {
        "target_folder": str(target_folder),
        "files": files,
        "scratch_files": scratch,
    }

    if not execute:
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
        sys.exit(2 if has_collision else 0)

    # Execute: create files
    created = []
    skipped = []
    for section, file_info in zip(sections, files):
        name = file_info["name"]
        if name in skip_files:
            skipped.append(name)
            continue
        if file_info["collision"] and name not in skip_files:
            # If collision and not explicitly allowed (not in skip), still create (overwrite)
            pass

        normalized = normalize_latex(section["content"])
        out_path = target_folder / name
        out_path.write_text(normalized + "\n", encoding="utf-8")
        created.append(name)

    # Delete distill file
    distill_path.unlink()

    # Cleanup scratch files if requested
    cleaned = []
    if cleanup:
        for sf in scratch:
            sf_path = target_folder / sf
            if sf_path.is_file():
                sf_path.unlink()
                cleaned.append(sf)

    result = {
        "target_folder": str(target_folder),
        "created": created,
        "skipped": skipped,
        "distill_deleted": True,
        "scratch_cleaned": cleaned,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
