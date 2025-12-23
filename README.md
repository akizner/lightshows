# Tesla Lightshow Creator

A complete toolkit for creating, managing, and deploying custom Tesla light shows.

## 🚗 What is Tesla Lightshow?

Tesla Lightshow is a feature that allows Tesla vehicles to perform synchronized light shows choreographed to music. Vehicles can coordinate their exterior lights, interior lights, trunk/frunk movements, and charging port to create entertaining displays.

## 🎯 Project Overview

This repository provides:
- **Organized structure** for managing multiple light shows
- **Build tools** for packaging shows ready for USB deployment
- **Validation tools** to ensure show files are properly formatted
- **Documentation** and examples to get started quickly

## 📁 Project Structure

```
tesla-light-show/
├── shows/                  # Your custom light shows
│   ├── example-show/
│   │   ├── lightshow.fseq # Light sequence file (from xLights)
│   │   ├── lightshow.wav  # Audio file
│   │   └── metadata.json  # Show information
│   └── another-show/
├── build/                  # Built shows ready for USB
├── tools/                  # Python scripts for management
│   ├── validate.py        # Validate show files
│   ├── package.py         # Package shows for deployment
│   └── utils.py           # Utility functions
├── templates/             # Templates for new shows
├── docs/                  # Additional documentation
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

1. **xLights** - Download from [xlights.org](https://xlights.org/)
   - Used to create the `.fseq` sequence files
2. **Python 3.8+** - For build tools
3. **USB Drive** - Formatted as FAT32 or exFAT

### Installation

```bash
# Clone this repository
git clone <your-repo-url>
cd lightshows

# Install Python dependencies
pip install -r requirements.txt
```

### Creating Your First Show

1. **Create a new show directory:**
```bash
python tools/create_show.py "My Awesome Show"
```

2. **Add your files:**
   - Design your light sequence in xLights
   - Export as `lightshow.fseq`
   - Add your audio file as `lightshow.wav` or `lightshow.mp3`
   - Update `metadata.json` with show details

3. **Validate your show:**
```bash
python tools/validate.py shows/my-awesome-show
```

4. **Build for deployment:**
```bash
python tools/package.py shows/my-awesome-show
```

5. **Deploy to USB:**
   - Copy the built show from `build/my-awesome-show/` to your USB drive
   - The structure should be: `USB:/LightShow/lightshow.fseq` and `USB:/LightShow/lightshow.wav`

## 🎨 Creating Shows with xLights

### Setup

1. Open xLights and create a new sequence
2. Configure your sequence:
   - **Frame Rate**: 20-50 FPS (Tesla recommends 25 FPS)
   - **Duration**: Match your audio length
   - **Audio**: Import your music file

3. Define your Tesla model:
   - Use Tesla's provided xLights profile
   - Configure channels for lights, closures, and charging port

4. Design your show:
   - Create effects and timing
   - Test and preview
   - Export as `.fseq` format

### Supported Features

Your light show can control:
- 🔦 **Lights**: Front/rear, fog, turn signals
- 🚪 **Closures**: Trunk, frunk
- 🔌 **Charging port**: Open/close
- 💡 **Interior lights**: Ambient lighting

## 🛠️ Tools Reference

### validate.py
```bash
python tools/validate.py <show-directory>
```
Checks that:
- Required files exist (`.fseq` and audio)
- File sizes are reasonable
- Metadata is properly formatted

### package.py
```bash
python tools/package.py <show-directory> [--output BUILD_DIR]
```
Packages a show for USB deployment with proper structure.

### create_show.py
```bash
python tools/create_show.py <show-name>
```
Creates a new show directory with template files.

## 📋 Show Metadata Format

Each show directory includes a `metadata.json`:

```json
{
  "name": "My Awesome Show",
  "artist": "Artist Name",
  "duration": 180,
  "description": "A spectacular light show",
  "created": "2025-12-23",
  "fps": 25,
  "audio_format": "wav"
}
```

## 🚀 Deploying to Your Tesla

1. **Prepare USB Drive**:
   - Format as FAT32 or exFAT
   - Create folder: `LightShow`

2. **Copy Files**:
   ```
   USB:/LightShow/
   ├── lightshow.fseq
   └── lightshow.wav (or .mp3)
   ```

3. **Play on Tesla**:
   - Insert USB into front USB port
   - Put car in Park
   - Tap Toybox > Light Show
   - Select "Custom" and enjoy!

## 🔧 Build System

Use the Makefile for common tasks:

```bash
make validate-all    # Validate all shows
make build-all       # Build all shows
make clean           # Clean build directory
make help            # Show available commands
```

## 📚 Resources

- [Tesla Lightshow GitHub](https://github.com/teslamotors/light-show)
- [xLights Documentation](https://xlights.org/docs/)
- [Tesla Lightshow Guide](https://github.com/teslamotors/light-show/blob/main/xLights_Guide.pdf)

## 🤝 Contributing

1. Create a new branch for your show
2. Add your show to the `shows/` directory
3. Validate and test thoroughly
4. Submit a pull request

## 📝 License

MIT License - Feel free to use and modify for your own light shows!

## ⚠️ Notes

- Shows must be under 5 minutes
- USB drive must be in front USB port
- Car must be in Park to play shows
- Not all Tesla models support all features
- Test your shows in a safe location

---

**Happy Show Creating! 🎭✨**

