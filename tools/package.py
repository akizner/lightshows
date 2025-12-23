#!/usr/bin/env python3
"""
Package Tesla Lightshow for USB deployment.

Creates a build directory with properly named files ready for Tesla.
"""
import sys
import shutil
import argparse
from pathlib import Path

from utils import (
    get_show_files, print_success, print_error, print_info,
    load_metadata
)


def package_show(show_dir: Path, output_dir: Path = None) -> bool:
    """
    Package a show for USB deployment.
    
    Args:
        show_dir: Path to show directory
        output_dir: Output directory (default: build/<show-name>)
    
    Returns:
        True if successful, False otherwise
    """
    print_info(f"Packaging show: {show_dir.name}")
    
    # Set default output directory
    if output_dir is None:
        output_dir = Path("build") / show_dir.name
    
    # Get show files
    fseq_file, audio_file, metadata_file = get_show_files(show_dir)
    
    if not fseq_file:
        print_error("Cannot package: Missing .fseq file")
        return False
    
    if not audio_file:
        print_error("Cannot package: Missing audio file")
        return False
    
    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create LightShow subdirectory (Tesla's expected structure)
    lightshow_dir = output_dir / "LightShow"
    lightshow_dir.mkdir(exist_ok=True)
    
    # Copy and rename files to Tesla's expected names
    try:
        # Copy .fseq file
        dest_fseq = lightshow_dir / "lightshow.fseq"
        shutil.copy2(fseq_file, dest_fseq)
        print_success(f"Copied: {fseq_file.name} → lightshow.fseq")
        
        # Copy audio file with proper name
        dest_audio = lightshow_dir / f"lightshow{audio_file.suffix}"
        shutil.copy2(audio_file, dest_audio)
        print_success(f"Copied: {audio_file.name} → lightshow{audio_file.suffix}")
        
        # Copy metadata if it exists
        if metadata_file:
            dest_metadata = output_dir / "metadata.json"
            shutil.copy2(metadata_file, dest_metadata)
            print_success(f"Copied: metadata.json")
        
        # Create a README for the USB drive
        readme_content = f"""# Tesla Lightshow

Show: {show_dir.name}

## Installation

1. Copy the 'LightShow' folder to the root of your USB drive
2. Safely eject the USB drive
3. Insert into your Tesla's front USB port
4. Put car in Park
5. Navigate to: Toybox > Light Show > Custom

## Files

- lightshow.fseq: Light sequence data
- lightshow{audio_file.suffix}: Audio track

"""
        
        if metadata_file:
            try:
                metadata = load_metadata(metadata_file)
                readme_content += f"\n## Show Details\n\n"
                for key, value in metadata.items():
                    readme_content += f"- **{key.title()}**: {value}\n"
            except Exception:
                pass
        
        readme_path = output_dir / "README.txt"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print_success(f"Created: README.txt")
        
        print_success(f"\n✓ Show packaged successfully!")
        print_info(f"Output directory: {output_dir.absolute()}")
        print_info(f"\nNext steps:")
        print_info(f"  1. Copy '{lightshow_dir}' folder to your USB drive root")
        print_info(f"  2. Eject USB safely")
        print_info(f"  3. Play on your Tesla: Toybox > Light Show > Custom")
        
        return True
    
    except Exception as e:
        print_error(f"Failed to package show: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Package Tesla Lightshow for USB deployment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s shows/my-show                    Package to build/my-show/
  %(prog)s shows/my-show -o /path/to/usb    Package directly to USB drive
        """
    )
    
    parser.add_argument(
        'show_dir',
        type=Path,
        help='Path to show directory'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output directory (default: build/<show-name>)'
    )
    
    args = parser.parse_args()
    
    # Check if show directory exists
    if not args.show_dir.exists():
        print_error(f"Show directory does not exist: {args.show_dir}")
        sys.exit(1)
    
    # Package the show
    success = package_show(args.show_dir, args.output)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

