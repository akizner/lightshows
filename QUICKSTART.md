# Quick Start Guide

Get started creating Tesla light shows in 5 minutes!

## 🚀 Installation

```bash
# Navigate to project
cd tesla-light-show

# Install dependencies (minimal - uses Python standard library)
pip install -r requirements.txt

# Make tools executable (Unix/Mac)
chmod +x tools/*.py
```

## 📝 Create Your First Show

### Step 1: Create Show Structure

```bash
python tools/create_show.py "My First Show"
```

This creates a new directory in `shows/my-first-show/` with template files.

### Step 2: Design in xLights

1. **Download xLights**: [xlights.org](https://xlights.org/)
2. **Create sequence**:
   - New Sequence → Musical Sequence
   - Import your audio file
   - Set Frame Interval: 40ms (25 FPS)
3. **Add Tesla model**:
   - Get Tesla profile from [Tesla's GitHub](https://github.com/teslamotors/light-show)
   - Import in Layout tab
4. **Design your show**:
   - Add effects to timeline
   - Sync with music beats
   - Preview and test
5. **Export**:
   - File → Export → FSEQ
   - Save as `lightshow.fseq`

### Step 3: Add Files to Your Show

```bash
cd shows/my-first-show/

# Copy your exported sequence
cp /path/to/exported/lightshow.fseq .

# Copy your audio
cp /path/to/audio/my-song.wav lightshow.wav
# OR
cp /path/to/audio/my-song.mp3 lightshow.mp3

# Update metadata.json with your show details
nano metadata.json
```

### Step 4: Validate

```bash
python tools/validate.py shows/my-first-show -v
```

Fix any issues reported before proceeding.

### Step 5: Build for USB

```bash
python tools/package.py shows/my-first-show
```

This creates: `build/my-first-show/LightShow/` ready to copy to USB.

### Step 6: Deploy to Tesla

1. **Prepare USB**:
   - Format as FAT32 or exFAT
   - Copy `build/my-first-show/LightShow/` to USB root

2. **Test on Tesla**:
   - Insert USB into front port
   - Put car in Park
   - Navigate: Toybox → Light Show → Custom
   - Enjoy! 🎉

## 🛠️ Using Make Commands

Quick commands for common tasks:

```bash
# Create new show
make new SHOW="Show Name"

# Validate all shows
make validate-all

# Build all shows
make build-all

# Quick deploy a specific show
make deploy SHOW=my-show-directory

# Clean build directory
make clean

# See all commands
make help
```

## 📚 Essential Commands

```bash
# List all shows
python tools/list_shows.py

# Validate specific show
python tools/validate.py shows/show-name

# Package specific show
python tools/package.py shows/show-name

# Create new show from scratch
python tools/create_show.py "Show Name"
```

## 🎨 Show Design Tips

### For First-Timers

1. **Keep it simple**: Start with basic on/off effects
2. **Short and sweet**: 1-2 minutes is perfect for learning
3. **Use templates**: Copy patterns from example shows
4. **Test early**: Build and test on hardware ASAP

### Frame Rate

- **20 FPS** (50ms): Smaller files, slightly choppy
- **25 FPS** (40ms): **Recommended** - good balance
- **50 FPS** (20ms): Smoothest, but larger files

### Audio Format

- **WAV**: Better quality, larger size (~5-10MB/min)
- **MP3**: Smaller size, good quality (~1-2MB/min at 256kbps)

### Effects

Start with these basic effects:
- **On**: Simple light on/off
- **Intensity**: Fade in/out
- **Strobe**: Flashing patterns
- **Chase**: Sequential lighting

## 🔍 Troubleshooting

### Show Not Appearing in Tesla

```bash
# Check file names (must be exact)
ls shows/my-show/
# Should see: lightshow.fseq and lightshow.wav (or .mp3)

# Validate the show
python tools/validate.py shows/my-show -v

# Rebuild
python tools/package.py shows/my-show
```

### USB Issues

- Format: Must be FAT32 or exFAT
- Location: Front USB port only
- Structure: `USB:/LightShow/lightshow.fseq` and `lightshow.wav`

### Show Won't Play

- Car must be in Park
- Check software version (2021.44.25+)
- Try reinserting USB
- Reboot touchscreen (hold both scroll wheels)

## 📖 Learning Resources

### Documentation

- `README.md` - Project overview
- `docs/XLIGHTS_SETUP.md` - Detailed xLights guide
- `docs/DEPLOYMENT.md` - Deployment instructions
- `CONTRIBUTING.md` - Sharing your shows

### External Resources

- [Tesla Lightshow Official Guide](https://github.com/teslamotors/light-show)
- [xLights Documentation](https://xlights.org/docs/)
- [xLights Video Tutorials](https://www.youtube.com/c/xLights)

## 🎯 Next Steps

1. ✅ Create your first simple show
2. ✅ Test on your Tesla
3. ✅ Learn xLights effects
4. ✅ Design more complex sequences
5. ✅ Share with the community!

## 💡 Example Workflow

```bash
# Create show
python tools/create_show.py "Birthday Celebration"

# ... Design in xLights and export ...

# Add files
cp ~/Downloads/lightshow.fseq shows/birthday-celebration/
cp ~/Music/happy-birthday.wav shows/birthday-celebration/lightshow.wav

# Validate
python tools/validate.py shows/birthday-celebration -v

# Build
python tools/package.py shows/birthday-celebration

# Copy to USB
cp -r build/birthday-celebration/LightShow /Volumes/USB_DRIVE/

# Test on Tesla!
```

## ❓ Need Help?

- Check existing documentation in `docs/`
- Review example shows in `templates/`
- Open an issue on GitHub
- Join Tesla forums and communities

---

**Happy Show Creating! 🎭✨**

