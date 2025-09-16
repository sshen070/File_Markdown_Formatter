# Markdown Cleaner

A Python utility that cleans and reformats poorly structured Markdown files.  

This tool automatically fixes headers, bullet points, colons, and misplaced text formatting to produce clean and consistent Markdown output.

---

## Features

- **Header detection and formatting**  
  Ensures `#` headers are properly separated from body text.  

- **Bullet point normalization**  
  Detects `*` and restructures lines into clean lists.  

- **Colon spacing rules**  
  Splits text after colons (`:`) when appropriate.  

- **Period handling**  
  Splits words incorrectly stuck together by periods.  

- **Flexible parsing**  
  Skips malformed sections but preserves all content.  

---

## Usage

```bash
python cleaner.py input.md output.md
