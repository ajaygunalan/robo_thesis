#!/usr/bin/env python3
"""
Compare token usage between PDF and Markdown files for Chapter 3.
Uses character count and word count as proxies for token estimation.
Rough estimate: 1 token ≈ 4 characters for English text
"""

import fitz  # PyMuPDF
import os
from pathlib import Path

def extract_pdf_text(pdf_path):
    """Extract all text from PDF"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def read_markdown_files(directory):
    """Read all markdown files in directory"""
    md_files = list(Path(directory).glob("*.md"))
    combined_text = ""
    file_stats = []

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            combined_text += content + "\n"
            chars = len(content)
            words = len(content.split())
            file_stats.append({
                'name': md_file.name,
                'chars': chars,
                'words': words,
                'est_tokens': chars // 4
            })

    return combined_text, file_stats

def analyze_text(text, name):
    """Analyze text and return statistics"""
    chars = len(text)
    words = len(text.split())
    lines = len(text.splitlines())

    # Token estimation (rough: 1 token ≈ 4 chars for English)
    est_tokens = chars // 4

    return {
        'name': name,
        'characters': chars,
        'words': words,
        'lines': lines,
        'estimated_tokens': est_tokens
    }

def main():
    chapter_dir = "/media/ajay/gdrive/_robo_thesis/_geometric_algebra/chapter_3"
    pdf_path = os.path.join(chapter_dir, "Ch03_Metric_Products_of_Subspaces.pdf")

    print("=" * 70)
    print("TOKEN USAGE COMPARISON: PDF vs Markdown")
    print("=" * 70)

    # Analyze PDF
    print("\n📄 EXTRACTING PDF TEXT...")
    pdf_text = extract_pdf_text(pdf_path)
    pdf_stats = analyze_text(pdf_text, "PDF")

    print(f"\nPDF Statistics:")
    print(f"  Characters:       {pdf_stats['characters']:,}")
    print(f"  Words:            {pdf_stats['words']:,}")
    print(f"  Lines:            {pdf_stats['lines']:,}")
    print(f"  Estimated Tokens: {pdf_stats['estimated_tokens']:,}")

    # Analyze Markdown files
    print("\n📝 READING MARKDOWN FILES...")
    md_text, md_file_stats = read_markdown_files(chapter_dir)
    md_stats = analyze_text(md_text, "All Markdown")

    print(f"\nMarkdown Statistics (Combined):")
    print(f"  Characters:       {md_stats['characters']:,}")
    print(f"  Words:            {md_stats['words']:,}")
    print(f"  Lines:            {md_stats['lines']:,}")
    print(f"  Estimated Tokens: {md_stats['estimated_tokens']:,}")

    print(f"\n📊 Individual Markdown Files:")
    print("-" * 60)
    print(f"{'File':<45} {'Chars':>8} {'Tokens':>8}")
    print("-" * 60)
    for f in sorted(md_file_stats, key=lambda x: x['chars'], reverse=True):
        print(f"{f['name']:<45} {f['chars']:>8,} {f['est_tokens']:>8,}")

    # Comparison
    print("\n" + "=" * 70)
    print("📈 COMPARISON SUMMARY")
    print("=" * 70)

    ratio = pdf_stats['estimated_tokens'] / md_stats['estimated_tokens'] if md_stats['estimated_tokens'] > 0 else 0
    diff = pdf_stats['estimated_tokens'] - md_stats['estimated_tokens']

    print(f"\n  PDF Estimated Tokens:      {pdf_stats['estimated_tokens']:>10,}")
    print(f"  Markdown Estimated Tokens: {md_stats['estimated_tokens']:>10,}")
    print(f"  Difference:                {diff:>10,}")
    print(f"  Ratio (PDF/MD):            {ratio:>10.2f}x")

    if diff > 0:
        print(f"\n  ➡️  PDF uses ~{diff:,} MORE tokens than Markdown")
        print(f"  ➡️  PDF is {ratio:.2f}x larger in token terms")
    else:
        print(f"\n  ➡️  Markdown uses ~{abs(diff):,} MORE tokens than PDF")
        print(f"  ➡️  Markdown is {1/ratio:.2f}x larger in token terms")

    # Recommendation
    print("\n" + "=" * 70)
    print("💡 RECOMMENDATION")
    print("=" * 70)

    if ratio > 1.2:
        print(f"""
  The PDF consumes significantly MORE tokens ({ratio:.1f}x).

  For LLM context efficiency, the MARKDOWN files are better:
  - Save ~{diff:,} tokens per read
  - Atomic notes allow selective loading
  - Can load just the summary note (~{md_file_stats[0]['est_tokens'] if md_file_stats else 0:,} tokens)
    instead of the full content
""")
    elif ratio < 0.8:
        print("""
  The Markdown files consume MORE tokens.
  Consider using the PDF for full chapter reads.
""")
    else:
        print("""
  Token usage is roughly similar between PDF and Markdown.
  Choose based on other factors (searchability, figures, etc.)
""")

if __name__ == "__main__":
    main()
