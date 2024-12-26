# Python scripts for use with uv run

These Python scripts can be run directly from their URLs using `uv run`.
For more UV info, check [here](https://github.com/astral-sh/uv).

## unlock_pdf.py

A command-line tool to remove password protection from PDF files.

### Usage

Basic usage:
```bash
uv unlock_pdf.py input.pdf password
```

Specify output file:
```bash
uv unlock_pdf.py input.pdf password -o unlocked.pdf
```

### Arguments

- `pdf_file`: Path to the password-protected PDF file
- `password`: Password to unlock the PDF

### Examples

Remove password from 'protected.pdf':
```bash
uv unlock_pdf.py protected.pdf mypassword
```

Save unlocked file with custom name:
```bash
uv unlock_pdf.py protected.pdf mypassword -o final.pdf
```

### Error Messages

- "PDF is not encrypted": The input file has no password protection
- "Invalid password": The provided password is incorrect