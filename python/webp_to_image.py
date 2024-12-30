# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "pillow",
# ]
# ///

import click
from pathlib import Path
from PIL import Image

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), help='Output file path')
@click.option('-f', '--format', type=click.Choice(['png', 'jpeg']), default='png', help='Output image format')
def convert(input_file, output, format):
    """Convert a WebP image to PNG or JPEG format"""
    input_path = Path(input_file)
    
    if not input_path.suffix.lower() == '.webp':
        raise click.BadParameter('Input file must be a WebP image')
    
    img = Image.open(input_path)
    
    if output:
        output_path = Path(output)
    else:
        output_path = input_path.with_suffix(f'.{format}')
    
    img.save(output_path, format.upper())
    
    click.echo(f'Converted {input_path} to {output_path}')

if __name__ == '__main__':
    convert()