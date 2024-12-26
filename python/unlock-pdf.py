# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "pypdf",
#     "cryptography>=3.1",
# ]
# ///

import click
from pypdf import PdfReader, PdfWriter
from pypdf.errors import FileNotDecryptedError
from pathlib import Path

@click.command()
@click.argument('pdf_file', type=click.Path(exists=True))
@click.argument('password')
@click.option('--output', '-o', help='Output file path (default: input_unlocked.pdf)')
def unlock_pdf(pdf_file: str, password: str, output: str | None):
    """Remove password protection from a PDF file."""
    input_path = Path(pdf_file)
    output_path = Path(output) if output else input_path.with_stem(f"{input_path.stem}_unlocked")
    
    reader = PdfReader(input_path)
    if not reader.is_encrypted:
        raise click.ClickException("PDF is not encrypted")
        
    try:
        reader.decrypt(password)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
            
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        click.echo(f"Unlocked PDF saved to: {output_path}")
    except FileNotDecryptedError:
        raise click.ClickException("Invalid password")

if __name__ == '__main__':
    unlock_pdf()