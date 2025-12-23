#!/usr/bin/env python3
"""
Validate Tesla Lightshow files.

Checks that all required files are present and properly formatted.
"""
import sys
import argparse
from pathlib import Path

from utils import (
    get_show_files, load_metadata, print_success, print_error,
    print_warning, print_info, get_file_size_mb, format_size
)


def validate_show(show_dir: Path, verbose: bool = False) -> bool:
    """
    Validate a Tesla Lightshow directory.
    
    Args:
        show_dir: Path to show directory
        verbose: Print detailed information
    
    Returns:
        True if valid, False otherwise
    """
    if verbose:
        print_info(f"Validating show: {show_dir.name}")
    
    valid = True
    
    # Check if directory exists
    if not show_dir.exists():
        print_error(f"Show directory does not exist: {show_dir}")
        return False
    
    if not show_dir.is_dir():
        print_error(f"Not a directory: {show_dir}")
        return False
    
    # Get show files
    fseq_file, audio_file, metadata_file = get_show_files(show_dir)
    
    # Validate .fseq file
    if not fseq_file:
        print_error("Missing .fseq file (light sequence)")
        valid = False
    else:
        if verbose:
            print_success(f"Found sequence file: {fseq_file.name}")
        
        # Check file size (typical shows are 1-50 MB)
        size_mb = get_file_size_mb(fseq_file)
        if verbose:
            print_info(f"  Size: {format_size(fseq_file.stat().st_size)}")
        
        if size_mb > 100:
            print_warning(f"Sequence file is very large ({size_mb:.1f} MB)")
        elif size_mb < 0.1:
            print_warning(f"Sequence file is very small ({size_mb:.1f} MB)")
    
    # Validate audio file
    if not audio_file:
        print_error("Missing audio file (.wav or .mp3)")
        valid = False
    else:
        if verbose:
            print_success(f"Found audio file: {audio_file.name}")
            print_info(f"  Size: {format_size(audio_file.stat().st_size)}")
        
        # Check audio format
        if audio_file.suffix not in ['.wav', '.mp3']:
            print_error(f"Invalid audio format: {audio_file.suffix}")
            print_info("  Audio must be .wav or .mp3")
            valid = False
        
        # Check file size (typical songs are 3-50 MB for WAV, 1-10 MB for MP3)
        size_mb = get_file_size_mb(audio_file)
        if audio_file.suffix == '.wav' and size_mb > 100:
            print_warning(f"Audio file is very large ({size_mb:.1f} MB)")
        elif size_mb < 0.5:
            print_warning(f"Audio file is very small ({size_mb:.1f} MB)")
    
    # Validate metadata file
    if not metadata_file:
        print_warning("Missing metadata.json (recommended but optional)")
        if verbose:
            print_info("  Create metadata.json with show information")
    else:
        try:
            metadata = load_metadata(metadata_file)
            if verbose:
                print_success("Found valid metadata.json")
            
            # Check recommended fields
            recommended_fields = ['name', 'duration', 'artist', 'created']
            for field in recommended_fields:
                if field not in metadata:
                    if verbose:
                        print_warning(f"  Missing recommended field: {field}")
            
            # Display metadata if verbose
            if verbose and metadata:
                print_info("  Metadata:")
                for key, value in metadata.items():
                    print_info(f"    {key}: {value}")
        
        except ValueError as e:
            print_error(f"Invalid metadata.json: {e}")
            valid = False
    
    # Check file naming conventions
    if fseq_file and fseq_file.name != "lightshow.fseq":
        print_warning(f"Sequence file should be named 'lightshow.fseq' (found: {fseq_file.name})")
        print_info("  Tesla expects 'lightshow.fseq' on the USB drive")
    
    if audio_file and not audio_file.name.startswith("lightshow"):
        print_warning(f"Audio file should be named 'lightshow.wav' or 'lightshow.mp3' (found: {audio_file.name})")
        print_info("  Tesla expects 'lightshow.wav' or 'lightshow.mp3' on the USB drive")
    
    # Final result
    if valid:
        print_success(f"✓ Show '{show_dir.name}' is valid!")
    else:
        print_error(f"✗ Show '{show_dir.name}' has validation errors")
    
    return valid


def main():
    parser = argparse.ArgumentParser(
        description='Validate Tesla Lightshow files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s shows/my-show              Validate a specific show
  %(prog)s shows/my-show -v           Validate with detailed output
        """
    )
    
    parser.add_argument(
        'show_dir',
        type=Path,
        help='Path to show directory'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output with detailed information'
    )
    
    args = parser.parse_args()
    
    # Validate the show
    is_valid = validate_show(args.show_dir, verbose=args.verbose)
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()

