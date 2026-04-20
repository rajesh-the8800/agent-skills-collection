---
name: pdf
description: Extract text from PDF files
---

# PDF Skill

## When to use
Use this skill when the user wants to extract text from a PDF.

## Instructions

1. Take the PDF file path from the user
2. Run the script:

   python scripts/extract_text.py <file>

3. Return the extracted text

## Example

Input:
sample.pdf

Command:
python scripts/extract_text.py sample.pdf