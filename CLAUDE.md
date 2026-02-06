# Vault Structure

## Why This Exists

After months away from a topic, reading a molecule should restore your understanding — without returning to the original source. That's the test. If you have to re-read the textbook or re-watch the lecture, the molecule failed.

## What's What

| Prefix | Type | Purpose |
|--------|------|---------|
| `__` | Index | Entry point for a discipline, lists molecules |
| `_` | Molecule | Standalone narrative that teaches the topic. Links to atoms for optional depth. |
| (none) | Atom | Single concept explained fully. Reusable across molecules. |

A molecule is complete on its own — you should understand the topic without clicking any links. Atoms exist for when you want to go deeper on a specific concept.

## Two Kinds of Work

**Folder-level**: Organizing molecules — naming, index structure, removing overlaps, creating missing atoms. Use when navigation is broken.

**Molecule-level**: Splitting large files, refining narrative flow, extracting atoms. Use `/vp-distill`. Don't split molecules during folder work.


<!-- How my Obsidian vault is organized
My coding style preferences (like using Go’s any instead of interface{})
Where to find specific types of information
How to interact with my note-taking system
Custom commands and workflows I’ve developed
 # Knowledge Vault Context for Claude Code

## Project Overview
Personal knowledge management system with automated CI/CD workflows.

## Vault Structure
- `/Daily Notes/` - Timestamped captures and reflections
- `/Projects/` - Active work with deliverables and timelines  
- `/Areas/` - Ongoing responsibilities and interests
- `/Resources/` - Reference materials and research
- `/Archive/` - Completed or inactive content

## Automation Goals
1. Maintain high-quality, interconnected content
2. Automate repetitive maintenance tasks  
3. Generate insights through AI analysis
4. Export knowledge in multiple formats

## Content Standards
- Use descriptive, searchable titles
- Include YAML frontmatter with tags and metadata
- Maintain consistent linking patterns
- Follow semantic markup conventions

## AI Enhancement Tasks
- Link validation and suggestion
- Content quality assessment
- Automatic tagging and categorization
- Knowledge graph generation
- Export automation -->