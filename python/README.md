# Python scripts for use with uv run

These Python scripts can be run directly from their URLs using `uv run`.
For more UV info, check [here](https://github.com/astral-sh/uv).

## Table Of Contents

- [unlock\_pdf.py](#unlock_pdfpy)
- [youtube\_transcript.py](#youtube_transcriptpy)
- [web\_to\_image.py](#webp_to_imagepy)

## unlock_pdf.py

A command-line tool to remove password protection from PDF files.

### Usage

Basic usage:

```bash
uv run unlock_pdf.py input.pdf password
```

Specify output file:

```bash
uv run unlock_pdf.py input.pdf password -o unlocked.pdf
```

### Arguments

- `pdf_file`: Path to the password-protected PDF file
- `password`: Password to unlock the PDF

### Examples

Remove password from 'protected.pdf':

```bash
uv run unlock_pdf.py protected.pdf mypassword
```

Save unlocked file with custom name:

```bash
uv run unlock_pdf.py protected.pdf mypassword -o final.pdf
```

### Error Messages

- "PDF is not encrypted": The input file has no password protection
- "Invalid password": The provided password is incorrect

## youtube_transcript.py

Downloads YouTube video transcripts and saves them as text files. The script extracts transcripts with timestamps, indicates whether the transcript was auto-generated, and supports multiple languages.

### Usage

Basic usage (saves to video_id.txt):

```bash
uv run youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Print to stdout:

```bash
uv run youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" -o -
```

Save to custom file with specific language:

```bash
uv run youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" -o transcript.txt -l es
```

### Arguments

- `url`: YouTube video URL (required)
- `--output`, `-o`: Output file name (use "-" for stdout, defaults to video_id.txt if not specified)
- `--language`, `-l`: Transcript language code (optional, defaults to 'en')

### Examples

Download English transcript:

```bash
uv run youtube_transcript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Download Spanish transcript to specific file:

```bash
uv run youtube_transcript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o rickroll.txt -l es
```

### Error Messages

- "Invalid YouTube URL format": The provided URL is not a valid YouTube video URL
- "Transcripts are disabled for this video": The video owner has disabled transcripts
- "No transcript found in language '{language}'": No transcript is available in the requested language
- "Unable to find transcript information": Failed to retrieve transcript metadata from YouTube

## webp_to_image.py

Script to convert a WebP image file to PNG or JPEG format.

### Usage

Basic usage:
```bash
python webp_to_image.py INPUT_FILE
```

### Arguments

- `INPUT_FILE`: Path to the input WebP image file
- `-o`, `--output`: (Optional) Output file path. If not provided, the output file will have the same name as the input file with - the new extension.
- `-f`, `--format`: (Optional) Output image format. Choices: png, jpeg. Default: png

### Examples

Convert image.webp to PNG format with default output path:

```bash
uv run webp_to_image.py image.webp
```

Convert image.webp to JPEG format with custom output path:

```bash
uv run webp_to_image.py image.webp -o output/converted.jpeg -f jpeg
```

### Error Messages

- "Input file must be a WebP image": The provided input file does not have a .webp extension. Ensure the input file is a valid `.webp` image.