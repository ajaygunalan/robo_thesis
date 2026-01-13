# Remove Redundancy from Notes

Read all files in the specified folder and remove redundancies.

## Input
- Folder: `$ARGUMENTS` (e.g., `_geometric_algebra/chapter_2`)

## Process

1. **Read all files** in the folder

2. **Identify redundancies** — look for:
   - Same formula explained/derived in multiple files
   - Same identity with interpretation appearing twice
   - Duplicate formulas within the same file
   - Concepts explained in detail outside their canonical location

3. **Decide canonical locations** using this principle:
   - Each concept belongs where it is *defined*, not where it is *used*
   - Application files should reference definition files, not repeat them
   - Overview files can have a "formula kit" summary — that's intentional, not redundancy

4. **For each redundancy, choose one of:**
   - **Keep in canonical location, remove elsewhere** — replace with a link `[[File#Section]]`
   - **Keep in canonical location, shorten elsewhere** — e.g., "The formula above" instead of repeating
   - **Merge** — if two files both partially cover a topic, consolidate into one

5. **Preserve the style:**
   - Short headers, bullets, LaTeX formulas
   - Conceptual hooks ("the honest definition is...", "the real primitive is...")
   - Links between notes using `[[...]]` syntax

## Output
- List all redundancies found with file locations
- Edit each file to remove redundancies
- Ensure all Obsidian links still work
