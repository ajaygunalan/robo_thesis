#!/usr/bin/env python3
"""Build a wikilink graph + health report for an Obsidian vault.

Usage: python3 vault_graph.py [vault_root]
Default vault_root: current directory

Outputs:
  - .claude/vault_graph.json (graph data)
  - stdout: health summary
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

EXCLUDE_DIRS = {".obsidian", ".claude", "node_modules", ".git", ".trash", "copilot", ".copilot"}
SCRATCH_PREFIXES = ("learn_", "progress_", "distill_", "quiz_")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def classify_file(name: str) -> str | None:
    """Classify a markdown file by its prefix. Returns None for scratch files."""
    stem = Path(name).stem
    if any(stem.startswith(p) for p in SCRATCH_PREFIXES):
        return None
    if stem.startswith("__"):
        return "index"
    if stem.startswith("_"):
        return "molecule"
    return "atom"


def walk_vault(vault_root: Path) -> tuple[list[dict], list[dict]]:
    """Walk all .md files, extract nodes and edges."""
    nodes = []
    edges = []

    for dirpath, dirnames, filenames in os.walk(vault_root):
        # Prune excluded directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")]

        rel_dir = os.path.relpath(dirpath, vault_root)
        if rel_dir == ".":
            rel_dir = ""

        for fname in filenames:
            if not fname.endswith(".md"):
                continue

            file_type = classify_file(fname)
            if file_type is None:
                continue  # scratch file

            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.join(rel_dir, fname) if rel_dir else fname

            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError):
                continue

            words = len(content.split())
            links = WIKILINK_RE.findall(content)

            node = {
                "path": rel_path,
                "name": Path(fname).stem,
                "type": file_type,
                "folder": rel_dir if rel_dir else ".",
                "words": words,
            }
            nodes.append(node)

            for link_target in links:
                edges.append({
                    "source": rel_path,
                    "target": link_target.strip(),
                    "resolved": None,  # filled in resolve pass
                })

    return nodes, edges


def resolve_edges(nodes: list[dict], edges: list[dict]) -> None:
    """Resolve wikilink targets to actual file paths."""
    # Build lookup: lowercase stem -> path
    name_to_path: dict[str, list[str]] = {}
    for node in nodes:
        key = node["name"].lower()
        name_to_path.setdefault(key, []).append(node["path"])

    for edge in edges:
        target = edge["target"].strip()
        # Try exact match first (case-insensitive on stem)
        key = Path(target).stem.lower() if "." in target else target.lower()
        matches = name_to_path.get(key, [])
        if len(matches) == 1:
            edge["resolved"] = matches[0]
        elif len(matches) > 1:
            # Multiple matches — pick the one in the same folder as source
            source_folder = str(Path(edge["source"]).parent)
            same_folder = [m for m in matches if str(Path(m).parent) == source_folder]
            edge["resolved"] = same_folder[0] if same_folder else matches[0]
        # else: remains None (broken link)


def check_stale_indexes(nodes: list[dict], vault_root: Path) -> list[str]:
    """Find folders where the index doesn't mention all molecules."""
    stale = []

    # Group by folder
    folders: dict[str, dict[str, list[dict]]] = {}
    for node in nodes:
        folder = node["folder"]
        folders.setdefault(folder, {"indexes": [], "molecules": []})
        if node["type"] == "index":
            folders[folder]["indexes"].append(node)
        elif node["type"] == "molecule":
            folders[folder]["molecules"].append(node)

    for folder, contents in folders.items():
        if not contents["indexes"] or not contents["molecules"]:
            continue
        for index_node in contents["indexes"]:
            idx_path = vault_root / index_node["path"]
            try:
                with open(idx_path, "r", encoding="utf-8") as f:
                    idx_content = f.read().lower()
            except (OSError, UnicodeDecodeError):
                continue
            missing = []
            for mol in contents["molecules"]:
                # Check if molecule name appears in index (as wikilink or plain text)
                if mol["name"].lower() not in idx_content:
                    missing.append(mol["name"])
            if missing:
                stale.append(f"{index_node['path']} missing: {', '.join(missing)}")

    return stale


def compute_health(nodes: list[dict], edges: list[dict], vault_root: Path) -> dict:
    """Compute health summary."""
    broken = [e for e in edges if e["resolved"] is None]

    # Orphan atoms: atoms with zero incoming edges
    incoming: set[str] = set()
    for e in edges:
        if e["resolved"]:
            incoming.add(e["resolved"])

    orphans = [n for n in nodes if n["type"] == "atom" and n["path"] not in incoming]
    stale = check_stale_indexes(nodes, vault_root)

    folders = set(n["folder"] for n in nodes)
    molecules = [n for n in nodes if n["type"] == "molecule"]
    atoms = [n for n in nodes if n["type"] == "atom"]
    indexes = [n for n in nodes if n["type"] == "index"]

    return {
        "folders": len(folders),
        "molecules": len(molecules),
        "atoms": len(atoms),
        "indexes": len(indexes),
        "broken_links": len(broken),
        "broken_details": [{"source": e["source"], "target": e["target"]} for e in broken],
        "orphan_atoms": len(orphans),
        "orphan_details": [n["path"] for n in orphans],
        "stale_indexes": len(stale),
        "stale_details": stale,
    }


def main():
    vault_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()

    if not vault_root.is_dir():
        print(f"Error: {vault_root} is not a directory", file=sys.stderr)
        sys.exit(1)

    nodes, edges = walk_vault(vault_root)
    resolve_edges(nodes, edges)
    health = compute_health(nodes, edges, vault_root)

    graph = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "nodes": nodes,
        "edges": edges,
    }

    # Write JSON
    out_dir = vault_root / ".claude"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "vault_graph.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"Vault: {health['folders']} folders, {health['molecules']} molecules, "
          f"{health['atoms']} atoms, {health['indexes']} indexes")
    print(f"Broken links: {health['broken_links']}")
    if health["broken_details"]:
        for b in health["broken_details"][:10]:
            print(f"  {b['source']} → [[{b['target']}]]")
        if health["broken_links"] > 10:
            print(f"  ... and {health['broken_links'] - 10} more")
    print(f"Orphan atoms: {health['orphan_atoms']}")
    if health["orphan_details"]:
        for o in health["orphan_details"][:10]:
            print(f"  {o}")
        if health["orphan_atoms"] > 10:
            print(f"  ... and {health['orphan_atoms'] - 10} more")
    print(f"Stale indexes: {health['stale_indexes']}")
    if health["stale_details"]:
        for s in health["stale_details"]:
            print(f"  {s}")

    print(f"\nGraph written to {out_path}")


if __name__ == "__main__":
    main()
