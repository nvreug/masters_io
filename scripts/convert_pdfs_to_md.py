#!/usr/bin/env python3
"""Convert PDFs in hector_course folder to markdown files."""

import pymupdf
from pathlib import Path


def pdf_to_markdown(pdf_path: Path, output_path: Path) -> None:
    """Convert a PDF file to markdown.

    Args:
        pdf_path: Path to the PDF file
        output_path: Path for the output markdown file
    """
    doc = pymupdf.open(pdf_path)

    markdown_content = []
    markdown_content.append(f"# {pdf_path.stem.replace('_', ' ')}\n")
    markdown_content.append(f"*Converted from: {pdf_path.name}*\n\n---\n")

    for page_num, page in enumerate(doc, 1):
        # Extract text from page
        text = page.get_text()

        if text.strip():
            markdown_content.append(f"\n## Page {page_num}\n")
            markdown_content.append(text)

    doc.close()

    # Write markdown file
    output_path.write_text("\n".join(markdown_content), encoding="utf-8")
    print(f"Converted: {pdf_path.name} -> {output_path.name}")


def main():
    """Convert all PDFs in hector_course folder to markdown."""
    source_dir = Path("previous_courses/hector_course")
    output_dir = source_dir / "markdown"
    output_dir.mkdir(exist_ok=True)

    pdf_files = list(source_dir.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files to convert\n")

    for pdf_path in sorted(pdf_files):
        output_path = output_dir / f"{pdf_path.stem}.md"
        try:
            pdf_to_markdown(pdf_path, output_path)
        except Exception as e:
            print(f"Error converting {pdf_path.name}: {e}")

    print(f"\nDone! Markdown files saved to: {output_dir}")


if __name__ == "__main__":
    main()
