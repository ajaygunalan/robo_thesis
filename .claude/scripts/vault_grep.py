#!/usr/bin/env python3
"""Parallel multi-term grep with wikilink scoring for an Obsidian vault.

Usage: python3 vault_grep.py [--vault <path>] [--wikilink-weight 2] <term1> <term2> ...

Outputs JSON to stdout with files ranked by total match score.
"""

import json
import os
import re
import sys
from pathlib import Path

EXCLUDE_DIRS = {".obsidian", ".claude", "node_modules", ".git", ".trash", "copilot", ".copilot"}


def build_wikilink_pattern(term: str) -> re.Pattern:
    """Build regex for [[term]] or [[term|alias]]."""
    escaped = re.escape(term)
    return re.compile(rf"\[\[{escaped}(?:\|[^\]]+)?\]\]", re.IGNORECASE)


def search_vault(vault_root: Path, terms: list[str], wikilink_weight: int) -> dict:
    """Search all .md files for all terms in one pass."""
    results: dict[str, dict] = {}

    # Pre-compile patterns
    content_patterns = [(t, re.compile(re.escape(t), re.IGNORECASE)) for t in terms]
    wikilink_patterns = [(t, build_wikilink_pattern(t)) for t in terms]

    for dirpath, dirnames, filenames in os.walk(vault_root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")]

        for fname in filenames:
            if not fname.endswith(".md"):
                continue

            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(full_path, vault_root)

            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError):
                continue

            content_matches = {}
            wikilink_matches = {}
            total = 0

            for term, pat in content_patterns:
                count = len(pat.findall(content))
                if count > 0:
                    content_matches[term] = count
                    total += count

            for term, pat in wikilink_patterns:
                count = len(pat.findall(content))
                if count > 0:
                    wikilink_matches[term] = count
                    total += count * wikilink_weight

            if total > 0:
                results[rel_path] = {
                    "content_matches": content_matches,
                    "wikilink_matches": wikilink_matches,
                    "total_score": total,
                }

    return results


def main():
    vault_root = Path.cwd().resolve()
    wikilink_weight = 2
    terms = []

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--vault" and i + 1 < len(sys.argv):
            vault_root = Path(sys.argv[i + 1]).resolve()
            i += 2
            continue
        if arg == "--wikilink-weight" and i + 1 < len(sys.argv):
            wikilink_weight = int(sys.argv[i + 1])
            i += 2
            continue
        if not arg.startswith("--"):
            terms.append(arg)
        i += 1

    if not terms:
        print("Usage: vault_grep.py [--vault <path>] [--wikilink-weight N] <term1> <term2> ...",
              file=sys.stderr)
        sys.exit(1)

    results = search_vault(vault_root, terms, wikilink_weight)

    # Sort by total_score descending
    sorted_results = dict(sorted(results.items(), key=lambda x: x[1]["total_score"], reverse=True))

    output = {
        "terms": terms,
        "results": sorted_results,
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
