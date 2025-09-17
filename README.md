# Markdown Cleaner

A Python utility that cleans poorly structured Markdown strings and files.  

This tool automatically fixes issues with headers, bullet points, colons, and misplaced formatting to produce clean, consistent Markdown output.

## Input Options

1. **Strings**
   - Accepts a string from the command line  
   - Outputs properly formatted text to the terminal  

2. **Files**
   - Accepts an input file and an output file  
   - Writes a cleanly formatted version of the input to the output file  

## Features

* **Header detection and formatting**  
  Ensures `#` headers are properly separated from body text.  

* **Bullet point normalization**  
  Detects `*` and restructures lines into clean lists.  

* **Colon spacing rules**  
  Splits text after colons (`:`) when appropriate.  

* **Period handling**  
  Separates words incorrectly joined by periods.  

* **Flexible parsing**  
  Fixes malformed sections while preserving all content.  

## Usage

### Strings
```bash
python main.py "<input_string>"
```

### Files
```bash
python main.py <input_file> <output_file>
```
