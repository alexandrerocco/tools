# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "youtube_transcript_api",
# ]
# ///

import click
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
import sys

def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from URL."""
    parsed = urlparse(url)
    if parsed.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed.path == '/watch':
            return parse_qs(parsed.query)['v'][0]
        elif parsed.path.startswith('/v/'):
            return parsed.path.split('/')[2]
    elif parsed.hostname == 'youtu.be':
        return parsed.path[1:]
    raise ValueError("Invalid YouTube URL format")

@click.command()
@click.argument('url')
@click.option('--output', '-o', help='Output file name (use "-" for stdout)')
@click.option('--language', '-l', default='en', help='Transcript language (default: en)')
def main(url: str, output: str, language: str):
    """Download YouTube video transcript and save it as a text file."""
    try:
        video_id = extract_video_id(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript_info = transcript_list.find_transcript([language])
        transcript = transcript_info.fetch()
        
        is_generated = transcript_info.is_generated
        transcript_type = f"# Transcript type: {'Auto-generated' if is_generated else 'Manual'}\n\n"
        transcript_content = "".join(f"[{entry['start']:.2f}] {entry['text']}\n" for entry in transcript)
        
        if not output or output == "-":
            # Print to stdout
            click.echo(transcript_type + transcript_content, nl=False)
        else:
            # Save to file
            with open(output, 'w', encoding='utf-8') as f:
                f.write(transcript_type + transcript_content)
            click.echo(f"Transcript saved to {output}")
        
    except ValueError as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)
    except TranscriptsDisabled:
        click.echo("Error: Transcripts are disabled for this video", err=True)
        sys.exit(1)
    except NoTranscriptFound:
        click.echo(f"Error: No transcript found in language '{language}'", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: An unexpected error occurred: {str(e)}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()