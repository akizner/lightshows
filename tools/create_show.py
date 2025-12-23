#!/usr/bin/env python3
"""
Create a new Tesla Lightshow from template.

Sets up directory structure and metadata file for a new show.
"""
import sys
import argparse
from pathlib import Path
from datetime import datetime

from utils import (
    normalize_show_name, save_metadata, print_success,
    print_error, print_info
)


def create_show(show_name: str, shows_dir: Path = None) -> bool:
    """
    Create a new show directory with template files.
    
    Args:
        show_name: Human-readable name for the show
        shows_dir: Directory to create show in (default: shows/)
    
    Returns:
        True if successful, False otherwise
    """
    # Set default shows directory
    if shows_dir is None:
        shows_dir = Path("shows")
    
    # Normalize the name for directory
    dir_name = normalize_show_name(show_name)
    show_dir = shows_dir / dir_name
    
    # Check if show already exists
    if show_dir.exists():
        print_error(f"Show already exists: {show_dir}")
        return False
    
    print_info(f"Creating new show: {show_name}")
    print_info(f"Directory: {show_dir}")
    
    try:
        # Create show directory
        show_dir.mkdir(parents=True, exist_ok=True)
        
        # Create metadata file
        metadata = {
            "name": show_name,
            "artist": "Unknown Artist",
            "duration": 0,
            "description": "A custom Tesla light show",
            "created": datetime.now().strftime("%Y-%m-%d"),
            "fps": 25,
            "audio_format": "wav"
        }
        
        metadata_file = show_dir / "metadata.json"
        save_metadata(metadata_file, metadata)
        print_success(f"Created: metadata.json")
        
        # Create README for the show
        readme_content = f"""# {show_name}

A custom Tesla Lightshow.

## Setup Instructions

1. **Create your light sequence in xLights:**
   - Open xLights
   - Create a new sequence
   - Import your audio file
   - Design your light show
   - Export as `lightshow.fseq`

2. **Add your files to this directory:**
   - `lightshow.fseq` - Your exported sequence from xLights
   - `lightshow.wav` or `lightshow.mp3` - Your audio file
   - Update `metadata.json` with show details

3. **Validate your show:**
   ```bash
   python tools/validate.py {show_dir}
   ```

4. **Package for USB:**
   ```bash
   python tools/package.py {show_dir}
   ```

## Metadata

Edit `metadata.json` to update show information:
- name: Show title
- artist: Music artist/composer
- duration: Length in seconds
- description: What makes this show special
- fps: Frame rate used (typically 25)
- audio_format: wav or mp3

## Tips

- Keep shows under 5 minutes
- Use 25 FPS for best balance of quality and file size
- WAV files give better audio quality but are larger
- Test your show in a safe location first

## Resources

- [xLights Download](https://xlights.org/)
- [Tesla Lightshow Guide](https://github.com/teslamotors/light-show)
"""
        
        readme_file = show_dir / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        print_success(f"Created: README.md")
        
        # Create placeholder file to remind about required files
        placeholder_file = show_dir / "PLACE_YOUR_FILES_HERE.txt"
        placeholder_content = """Place your show files here:

Required files:
- lightshow.fseq (from xLights export)
- lightshow.wav or lightshow.mp3 (your audio)

Optional:
- metadata.json (already created - please update it!)

Once you have your files:
1. Delete this placeholder file
2. Run: python tools/validate.py shows/{dir_name}
3. Run: python tools/package.py shows/{dir_name}
""".format(dir_name=dir_name)
        
        with open(placeholder_file, 'w') as f:
            f.write(placeholder_content)
        print_success(f"Created: PLACE_YOUR_FILES_HERE.txt")
        
        print_success(f"\n✓ Show created successfully!")
        print_info(f"\nNext steps:")
        print_info(f"  1. Create your light sequence in xLights")
        print_info(f"  2. Export as 'lightshow.fseq'")
        print_info(f"  3. Place files in: {show_dir}/")
        print_info(f"  4. Update metadata.json with show details")
        print_info(f"  5. Validate: python tools/validate.py {show_dir}")
        print_info(f"  6. Package: python tools/package.py {show_dir}")
        
        return True
    
    except Exception as e:
        print_error(f"Failed to create show: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Create a new Tesla Lightshow from template',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "My Awesome Show"           Create show in shows/ directory
  %(prog)s "Holiday Special" -d custom Create show in custom/ directory
        """
    )
    
    parser.add_argument(
        'name',
        help='Name of the show (e.g., "My Awesome Show")'
    )
    
    parser.add_argument(
        '-d', '--directory',
        type=Path,
        default=Path('shows'),
        help='Base directory for shows (default: shows/)'
    )
    
    args = parser.parse_args()
    
    # Create the show
    success = create_show(args.name, args.directory)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

