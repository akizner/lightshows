"""
Utility functions for Tesla Lightshow management.
"""
import os
import json
from pathlib import Path
from typing import Dict, Tuple, Optional


class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_success(message: str):
    """Print success message in green."""
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")


def print_error(message: str):
    """Print error message in red."""
    print(f"{Colors.RED}✗ {message}{Colors.END}")


def print_warning(message: str):
    """Print warning message in yellow."""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.END}")


def print_info(message: str):
    """Print info message in blue."""
    print(f"{Colors.BLUE}ℹ {message}{Colors.END}")


def get_show_files(show_dir: Path) -> Tuple[Optional[Path], Optional[Path], Optional[Path]]:
    """
    Find the required files in a show directory.
    
    Returns:
        Tuple of (fseq_file, audio_file, metadata_file)
    """
    fseq_file = None
    audio_file = None
    metadata_file = show_dir / "metadata.json"
    
    if not metadata_file.exists():
        metadata_file = None
    
    # Look for .fseq file
    fseq_files = list(show_dir.glob("*.fseq"))
    if fseq_files:
        fseq_file = fseq_files[0]
    
    # Look for audio file (wav or mp3)
    audio_files = list(show_dir.glob("*.wav")) + list(show_dir.glob("*.mp3"))
    if audio_files:
        audio_file = audio_files[0]
    
    return fseq_file, audio_file, metadata_file


def load_metadata(metadata_file: Path) -> Dict:
    """Load and parse metadata JSON file."""
    try:
        with open(metadata_file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in metadata file: {e}")
    except Exception as e:
        raise ValueError(f"Error reading metadata file: {e}")


def save_metadata(metadata_file: Path, data: Dict):
    """Save metadata to JSON file."""
    with open(metadata_file, 'w') as f:
        json.dump(data, f, indent=2)


def get_file_size_mb(file_path: Path) -> float:
    """Get file size in megabytes."""
    return file_path.stat().st_size / (1024 * 1024)


def format_size(size_bytes: int) -> str:
    """Format bytes to human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def normalize_show_name(name: str) -> str:
    """
    Normalize show name to valid directory name.
    
    Converts to lowercase, replaces spaces with hyphens,
    removes special characters.
    """
    # Convert to lowercase and replace spaces with hyphens
    name = name.lower().replace(' ', '-')
    
    # Remove special characters, keep only alphanumeric and hyphens
    name = ''.join(c for c in name if c.isalnum() or c == '-')
    
    # Remove consecutive hyphens
    while '--' in name:
        name = name.replace('--', '-')
    
    # Remove leading/trailing hyphens
    name = name.strip('-')
    
    return name


def find_all_shows(shows_dir: Path) -> list:
    """
    Find all show directories in the shows folder.
    
    Returns:
        List of Path objects for directories containing show files.
    """
    shows = []
    
    if not shows_dir.exists():
        return shows
    
    for item in shows_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            # Check if it looks like a show directory
            fseq, audio, _ = get_show_files(item)
            if fseq or audio:
                shows.append(item)
    
    return sorted(shows)

