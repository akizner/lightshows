# Contributing to Tesla Lightshow Creator

Thank you for considering contributing to this project! 🎭✨

## How to Contribute

### Sharing Your Shows

1. **Fork** this repository
2. **Create** a branch for your show: `git checkout -b show/my-awesome-show`
3. **Add** your show to the `shows/` directory
4. **Test** your show thoroughly
5. **Commit** your changes: `git commit -m "Add My Awesome Show"`
6. **Push** to your fork: `git push origin show/my-awesome-show`
7. **Submit** a Pull Request

### Improving Tools

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/improvement`
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a Pull Request with description

## Contribution Guidelines

### Show Submissions

When submitting a show, ensure:

- ✅ Show is validated: `python tools/validate.py shows/your-show`
- ✅ All required files are included
- ✅ `metadata.json` is complete and accurate
- ✅ Music rights are cleared (use royalty-free or licensed music)
- ✅ Show has been tested on actual Tesla vehicle (if possible)
- ✅ README.md in show folder with description and credits

### Code Contributions

- Follow existing code style
- Add comments for complex logic
- Update documentation if needed
- Test your changes
- Keep Python code compatible with 3.8+

### Documentation

- Use clear, simple language
- Include examples
- Update README.md if adding features
- Check for typos and formatting

## Show Guidelines

### Content

- ✅ Family-friendly content
- ✅ Safe for public viewing
- ✅ Respects copyright and licensing
- ✅ No offensive or inappropriate content
- ✅ Credits original artists/creators

### Technical

- ✅ Duration: Under 5 minutes
- ✅ FPS: 20-50 (25 recommended)
- ✅ Audio: Royalty-free or properly licensed
- ✅ File size: `.fseq` under 50MB
- ✅ Format: Follows Tesla specifications

### Attribution

Always include in your show's README:

```markdown
## Credits

- **Show Creator**: Your Name
- **Music**: Artist Name - Song Title
- **License**: [License Type]
- **Created**: YYYY-MM-DD

## License

[Specify your show's license]
```

## Music Licensing

### Recommended Sources

**Royalty-Free Music:**
- [Free Music Archive](https://freemusicarchive.org/)
- [Incompetech](https://incompetech.com/)
- [YouTube Audio Library](https://www.youtube.com/audiolibrary)
- [Bensound](https://www.bensound.com/)

**Creative Commons:**
- [ccMixter](http://ccmixter.org/)
- [Jamendo](https://www.jamendo.com/)

### License Attribution

Always include proper attribution in your show's metadata:

```json
{
  "name": "My Show",
  "music": {
    "title": "Song Title",
    "artist": "Artist Name",
    "license": "CC BY 3.0",
    "url": "https://..."
  }
}
```

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Inappropriate content

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/tesla-light-show.git
cd tesla-light-show

# Install dependencies
pip install -r requirements.txt

# Make scripts executable
chmod +x tools/*.py

# Create a test show
python tools/create_show.py "Test Show"
```

## Testing

Before submitting:

1. **Validate all shows**:
   ```bash
   make validate-all
   ```

2. **Build all shows**:
   ```bash
   make build-all
   ```

3. **Test on actual hardware** (if possible):
   - Deploy to USB drive
   - Test on Tesla vehicle
   - Verify all effects work

## Pull Request Process

1. **Update** documentation for any new features
2. **Test** your changes thoroughly
3. **Describe** your changes in the PR description
4. **Link** any related issues
5. **Wait** for review and address feedback

## Questions?

- Open an issue for bugs or features
- Start a discussion for questions
- Check existing issues first

## Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Acknowledged in documentation

Thank you for making this project better! 🙏

---

**Let's create amazing light shows together! ✨**

