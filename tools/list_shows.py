#!/usr/bin/env python3
"""
List all Tesla Lightshows in the repository.

Displays a summary of all shows with metadata and file information.
"""
import sys
import argparse
from pathlib import Path

from utils import (
    find_all_shows, get_show_files, load_metadata,
    print_info, print_success, format_size, Colors
)


def list_shows(shows_dir: Path = None, verbose: bool = False):
    """
    List all shows in the repository.
    
    Args:
        shows_dir: Directory containing shows (default: shows/)
        verbose: Show detailed information
    """
    if shows_dir is None:
        shows_dir = Path("shows")
    
    if not shows_dir.exists():
        print_info("No shows directory found. Create one with: mkdir shows")
        return
    
    shows = find_all_shows(shows_dir)
    
    if not shows:
        print_info("No shows found in the shows/ directory.")
        print_info("Create your first show with: python tools/create_show.py \"My Show\"")
        return
    
    print(f"{Colors.BOLD}Found {len(shows)} show(s):{Colors.END}\n")
    
    for i, show_dir in enumerate(shows, 1):
        print(f"{Colors.BLUE}{i}. {show_dir.name}{Colors.END}")
        
        # Get files
        fseq_file, audio_file, metadata_file = get_show_files(show_dir)
        
        # Load metadata if available
        metadata = None
        if metadata_file:
            try:
                metadata = load_metadata(metadata_file)
            except Exception:
                pass
        
        # Display metadata
        if metadata:
            if 'name' in metadata:
                print(f"   Name: {metadata['name']}")
            if 'artist' in metadata:
                print(f"   Artist: {metadata['artist']}")
            if 'duration' in metadata:
                duration = metadata['duration']
                minutes = duration // 60
                seconds = duration % 60
                print(f"   Duration: {minutes}m {seconds}s")
        
        # Display files
        if verbose:
            print(f"   Files:")
            if fseq_file:
                print(f"     • {fseq_file.name} ({format_size(fseq_file.stat().st_size)})")
            if audio_file:
                print(f"     • {audio_file.name} ({format_size(audio_file.stat().st_size)})")
            if metadata_file:
                print(f"     • metadata.json")
        else:
            status_parts = []
            if fseq_file:
                status_parts.append("✓ sequence")
            else:
                status_parts.append("✗ sequence")
            
            if audio_file:
                status_parts.append("✓ audio")
            else:
                status_parts.append("✗ audio")
            
            print(f"   Status: {', '.join(status_parts)}")
        
        print()  # Blank line between shows
    
    print_success(f"Total: {len(shows)} show(s)")


def main():
    parser = argparse.ArgumentParser(
        description='List all Tesla Lightshows',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s           List all shows
  %(prog)s -v        List with detailed file information
        """
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed information'
    )
    
    parser.add_argument(
        '-d', '--directory',
        type=Path,
        default=Path('shows'),
        help='Shows directory (default: shows/)'
    )
    
    args = parser.parse_args()
    
    list_shows(args.directory, args.verbose)


if __name__ == '__main__':
    main()

