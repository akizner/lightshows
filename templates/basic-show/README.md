# Basic Show Template

This is a template structure for creating Tesla light shows.

## Files Needed

Replace these placeholder files with your actual show files:

1. **lightshow.fseq** - Your xLights sequence export
2. **lightshow.wav** or **lightshow.mp3** - Your audio file
3. **metadata.json** - Show information (included, update it!)

## Quick Start

1. Copy this template to create a new show:
   ```bash
   cp -r templates/basic-show shows/my-new-show
   ```

2. Or use the create tool:
   ```bash
   python tools/create_show.py "My New Show"
   ```

3. Add your files:
   - Export your xLights sequence as `lightshow.fseq`
   - Copy your audio as `lightshow.wav` or `lightshow.mp3`
   - Update `metadata.json` with your show details

4. Validate:
   ```bash
   python tools/validate.py shows/my-new-show
   ```

5. Build:
   ```bash
   python tools/package.py shows/my-new-show
   ```

## Metadata Fields

Update `metadata.json` with:

- **name**: Human-readable show name
- **artist**: Music artist or your name
- **duration**: Length in seconds
- **description**: What makes your show special
- **created**: Date created (YYYY-MM-DD)
- **fps**: Frame rate used (typically 25)
- **audio_format**: "wav" or "mp3"

## Tips

- Keep shows under 5 minutes
- Use 25 FPS for best balance
- WAV for quality, MP3 for size
- Test in a safe location first

---

Ready to create something amazing! ✨

