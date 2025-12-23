# xLights Setup Guide for Tesla Lightshows

Complete guide to setting up xLights for creating Tesla light shows.

## Installation

### Download xLights

1. Visit [xlights.org](https://xlights.org/)
2. Download the latest version for your OS:
   - Windows: `.exe` installer
   - macOS: `.dmg` package
   - Linux: AppImage or package

### First Launch

1. Open xLights
2. Select a location for your show data folder
3. xLights will create the necessary directory structure

## Creating a Tesla Lightshow

### Step 1: Create New Sequence

1. Click **New Sequence**
2. Choose **Musical Sequence**
3. Select your audio file (WAV or MP3)
4. Click **OK**

### Step 2: Configure Sequence Settings

In the sequence settings:

- **Frame Interval**: 40ms (25 FPS) recommended
  - Lower interval = smoother but larger file
  - Higher interval = smaller file but less smooth
- **Duration**: Auto-detected from audio

### Step 3: Setup Tesla Model

#### Download Tesla Profile

1. Get the official Tesla xLights profile from:
   - [Tesla Light Show GitHub](https://github.com/teslamotors/light-show)

2. Import the profile:
   - Go to **Layout** tab
   - Click **Model** → **Import**
   - Select the Tesla `.xmodel` file

#### Tesla Channels

The Tesla profile includes these controllable elements:

**Exterior Lights:**
- Front lights (left/right)
- Rear lights (left/right)
- Front fog lights
- Turn signals

**Closures:**
- Trunk (open/close)
- Frunk (open/close)
- Charging port (open/close)

**Interior:**
- Ambient lighting
- Screen brightness (limited control)

### Step 4: Design Your Show

#### Timeline

1. Switch to **Sequencer** tab
2. You'll see:
   - Timeline at top
   - Tesla model channels on left
   - Waveform of your audio

#### Adding Effects

1. **Select a timing section** on the timeline
2. **Choose a channel** (e.g., "Front Lights")
3. **Add an effect**:
   - Click **Effects** panel
   - Drag effect to timeline
   - Common effects:
     - **On**: Light stays on
     - **Intensity**: Fade in/out
     - **Strobe**: Flashing
     - **Pulse**: Rhythmic

#### Timing Marks

1. Create timing marks to sync with music beats:
   - Right-click timeline → **Add Timing Track**
   - Use **Papagayo** or manual marks
   - Snap effects to timing marks

### Step 5: Preview Your Show

1. Click **Play** button
2. Watch the timeline animation
3. Listen to audio sync
4. Adjust timing as needed

### Step 6: Export for Tesla

#### Export Sequence

1. Go to **File** → **Export**
2. Select **FSEQ** format
3. Name it exactly: `lightshow.fseq`
4. Choose export location (your show directory)

#### Prepare Audio

1. Your audio file should be named: `lightshow.wav` or `lightshow.mp3`
2. Recommended specs:
   - **WAV**: 44.1kHz, 16-bit, stereo
   - **MP3**: 320kbps, 44.1kHz

## Tips for Great Shows

### Timing

- **Sync to beats**: Use strong beats for dramatic effects
- **Build up**: Start subtle, increase intensity
- **Breaks**: Give the audience (and car) a rest
- **Finale**: End with a big climax

### Effects

- **Don't overdo it**: Constant flashing gets tiresome
- **Vary effects**: Mix static, pulses, and strobes
- **Use closures sparingly**: Opening/closing takes time
- **Test in daylight**: Effects look different in day vs night

### Technical

- **File size**: Keep `.fseq` under 50MB
- **Duration**: Under 5 minutes recommended
- **FPS**: 25 FPS is the sweet spot
- **Audio quality**: WAV for best quality, MP3 to save space

### Common Mistakes to Avoid

❌ **Too fast effects**: Tesla hardware has limits
❌ **Constant movement**: Closures wear out
❌ **No contrast**: Vary intensity
❌ **Poor audio sync**: Always test playback
❌ **Too complex**: Keep it viewable by audience

## Troubleshooting

### Export Failed

- Check file permissions
- Ensure enough disk space
- Try exporting to different location

### Audio Not Syncing

- Verify audio file is not corrupted
- Re-import audio into sequence
- Check frame interval (should be consistent)

### File Too Large

- Reduce FPS (increase frame interval)
- Simplify effects
- Shorten duration
- Use MP3 instead of WAV

### Effects Not Working on Tesla

- Verify channel names match Tesla profile
- Check `.fseq` file is named correctly
- Ensure all files are in `LightShow/` folder
- Test USB drive is formatted correctly (FAT32/exFAT)

## Advanced Techniques

### Multi-Channel Synchronization

Create complex patterns by syncing multiple channels:
```
Time 0-2s: Front lights fade in
Time 1-3s: Rear lights fade in
Time 2-4s: All lights pulse together
```

### Beat Detection

Use xLights' audio analysis:
1. Right-click timeline → **Papagayo**
2. Select audio file
3. Generate timing marks automatically
4. Snap effects to marks

### Color Coordination

While Tesla lights are white, you can create "color" through intensity patterns:
- **Warm**: Slower pulses, medium intensity
- **Cool**: Faster strobes, high intensity
- **Dramatic**: Sharp on/off transitions

## Resources

- [xLights Documentation](https://xlights.org/docs/)
- [xLights Forum](https://nutcracker123.com/forum/)
- [Tesla Lightshow GitHub](https://github.com/teslamotors/light-show)
- [xLights Zoom Room](https://www.youtube.com/c/xLights) (tutorials)

## Community

Join the community for help and inspiration:
- xLights Facebook Group
- r/TeslaLightShow (Reddit)
- Tesla Forums (Lightshow section)

---

**Happy Show Creating! 🎭✨**

