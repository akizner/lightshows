# Tesla Lightshow Deployment Guide

How to deploy your custom light shows to your Tesla vehicle.

## Prerequisites

- ✅ Custom light show created and validated
- ✅ USB drive (FAT32 or exFAT format)
- ✅ Tesla vehicle with Lightshow feature
- ✅ Vehicle software version 2021.44.25 or later

## USB Drive Preparation

### Format Requirements

Your USB drive must be formatted as:
- **FAT32** (recommended for drives under 32GB)
- **exFAT** (for larger drives)

### Formatting on macOS

```bash
# List drives
diskutil list

# Format drive (replace disk2 with your drive)
sudo diskutil eraseDisk FAT32 TESLA_SHOW /dev/disk2
```

### Formatting on Windows

1. Right-click USB drive in File Explorer
2. Select **Format**
3. Choose **FAT32** or **exFAT**
4. Click **Start**

### Formatting on Linux

```bash
# Find your drive
lsblk

# Format drive (replace sdb1 with your drive)
sudo mkfs.vfat -F 32 /dev/sdb1
```

## Deployment Steps

### Step 1: Build Your Show

```bash
# Validate first
python tools/validate.py shows/my-show

# Build for deployment
python tools/package.py shows/my-show
```

This creates: `build/my-show/LightShow/`

### Step 2: Copy to USB Drive

#### Option A: Direct Copy

```bash
# Copy the LightShow folder to USB root
cp -r build/my-show/LightShow /Volumes/TESLA_SHOW/
```

#### Option B: Manual Copy

1. Open `build/my-show/`
2. Copy the `LightShow` folder
3. Paste at the root of your USB drive

#### Final Structure

Your USB drive should look like:

```
USB Drive (root)
└── LightShow/
    ├── lightshow.fseq
    └── lightshow.wav (or .mp3)
```

⚠️ **Important**: Files must be directly in `LightShow/` folder, not in subfolders!

### Step 3: Eject Safely

**macOS:**
```bash
diskutil eject /Volumes/TESLA_SHOW
```

**Windows:**
- Right-click drive → **Eject**

**Linux:**
```bash
sudo umount /dev/sdb1
```

### Step 4: Load into Tesla

1. **Insert USB** into front USB port (near phone charger)
2. **Put car in Park**
3. **Navigate to**: Toybox → Light Show
4. **Select**: Custom (or your show name if it appears)
5. **Tap**: Start Light Show

## Playing Your Show

### Controls

- **Start**: Begin show
- **Stop**: Stop show mid-sequence
- **Exit**: Return to Toybox

### Best Viewing

1. **Location**: Open area, safe from traffic
2. **Time**: Night or dusk for best effect
3. **Position**: Stand in front or to the side
4. **Volume**: Roll down windows for best audio

### Safety

⚠️ **Always ensure**:
- Car is in Park
- Area is safe and clear
- No pedestrians or vehicles nearby
- You're not blocking traffic
- Emergency brake is on

## Troubleshooting

### Show Not Appearing

**Problem**: Custom show doesn't appear in menu

**Solutions**:
- ✅ Verify files are named exactly `lightshow.fseq` and `lightshow.wav`
- ✅ Check files are in `LightShow/` folder at USB root
- ✅ Confirm USB is formatted as FAT32 or exFAT
- ✅ Try ejecting and reinserting USB
- ✅ Restart car's touchscreen (hold both scroll wheels)

### Show Won't Start

**Problem**: Show appears but won't play

**Solutions**:
- ✅ Ensure car is in Park
- ✅ Check USB is fully inserted
- ✅ Verify `.fseq` file is valid (not corrupted)
- ✅ Try a different USB port
- ✅ Reboot vehicle (Safety > Power Off, wait 3 min)

### Show Plays But No Lights

**Problem**: Audio plays but lights don't activate

**Solutions**:
- ✅ Verify vehicle supports Lightshow feature
- ✅ Check software version (2021.44.25+)
- ✅ Ensure `.fseq` uses correct Tesla channel names
- ✅ Try a known-working show to test
- ✅ Contact Tesla support if hardware issue

### Audio Issues

**Problem**: Lights work but no audio

**Solutions**:
- ✅ Check volume is up
- ✅ Verify audio file format (WAV or MP3)
- ✅ Try different audio file
- ✅ Check file isn't corrupted
- ✅ Ensure `lightshow.wav` is in correct location

### File Size Errors

**Problem**: Files too large or won't copy

**Solutions**:
- ✅ `.fseq` should be under 50MB
- ✅ Audio should be under 100MB
- ✅ Use MP3 instead of WAV to save space
- ✅ Reduce FPS in xLights (increase frame interval)
- ✅ Shorten show duration

## Multiple Shows

### Switching Shows

To have multiple shows ready:

1. Create folders on USB:
   ```
   USB Drive
   ├── Show1/
   │   └── LightShow/
   │       ├── lightshow.fseq
   │       └── lightshow.wav
   └── Show2/
       └── LightShow/
           ├── lightshow.fseq
           └── lightshow.wav
   ```

2. Copy the show you want to play to the root:
   ```
   USB Drive
   ├── LightShow/         ← Active show
   ├── Show1/             ← Backup
   └── Show2/             ← Backup
   ```

3. Swap shows by copying from backups to root

## Performance Tips

### File Optimization

- **Use MP3**: Smaller than WAV, still good quality
- **Compress audio**: 256kbps is usually sufficient
- **Reduce FPS**: 20-25 FPS is optimal
- **Trim silence**: Remove dead air from audio

### Show Design

- **Shorter is better**: 2-3 minutes is ideal
- **Test in daylight**: Verify effects are visible
- **Vary intensity**: Don't blast lights constantly
- **Save finale**: Build to a climax at the end

## Updates and Maintenance

### Software Updates

After Tesla software updates:
1. Verify Lightshow still works
2. Check for new features or channels
3. Update xLights profiles if needed
4. Test all your custom shows

### USB Drive Care

- **Don't remove** during playback
- **Check regularly** for corruption
- **Keep backup** of show files
- **Replace** if experiencing errors

## Sharing Your Show

### With Other Tesla Owners

1. Package your show: `make deploy SHOW=my-show`
2. Share the `build/my-show/` directory
3. Include `README.txt` with instructions
4. Consider uploading to:
   - GitHub
   - r/TeslaLightShow
   - Tesla forums

### Attribution

If sharing, include:
- Show name and creator
- Music credits and licensing
- Any special instructions
- Compatible vehicle models

## Legal Considerations

### Music Rights

⚠️ **Important**: Respect copyright law
- Use royalty-free music
- Get permission for copyrighted songs
- Don't distribute shows with copyrighted audio
- Consider Creative Commons licensed music

### Public Performance

- Shows in public may require licensing
- Check local noise ordinances
- Respect private property
- Don't create traffic hazards

## Resources

- [Tesla Lightshow Support](https://www.tesla.com/support)
- [Official Tesla Lightshow GitHub](https://github.com/teslamotors/light-show)
- [xLights Community](https://nutcracker123.com/forum/)

---

**Enjoy Your Shows! 🎭✨**

