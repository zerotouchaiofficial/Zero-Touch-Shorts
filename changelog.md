# Changelog - Zero Touch Shorts 📝

All notable changes to this project will be documented in this file.  
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2026-02-16
### Added
- Initial release of **Zero Touch Shorts**.
- Fully automated YouTube Shorts creation pipeline:
  - Fetches unique random facts from a public API.
  - Converts facts to speech using **Google Text-to-Speech**.
  - Downloads high-quality background images from **Unsplash**.
  - Generates 50–60 second vertical videos with:
    - Attention-grabbing 3-second hooks.
    - Karaoke-style word-by-word text synced to audio.
    - Animated Ken Burns backgrounds with cross-dissolve transitions.
    - Floating particles, progress bar, intro/outro cards, and subscribe popup.
    - Ambient background music.
- Automatic thumbnail generation for each video.
- Uploads videos to YouTube via **YouTube Data API** with:
  - SEO-optimized titles.
  - Keyword-rich descriptions and 30 rotating hashtags.
  - Pinned engagement comment.
  - Playlist addition.
- Workflow runs **10 times/day** at peak hours (12 PM–11 PM EST).
- Persistent `used_facts.json` prevents repeating facts.

### Fixed
- N/A (initial release).

### Changed
- N/A (initial release).

---

## [0.1.0] - Pre-release
### Added
- Prototype of automated fact fetching and TTS conversion.
- Basic video rendering with MoviePy and Pillow.
- Local testing workflow for generating sample Shorts.

---

### How to Use This Changelog

- Increment **minor version** when adding new features.
- Increment **patch version** when fixing bugs.
- Increment **major version** only when introducing breaking changes.
- Update this file with **date, version, and a short summary of changes** for each release.
