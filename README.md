# 🎯 Brand Asset Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> Generate complete brand asset packages from a single creative brief using AI.

## What It Does

Feed it a brand brief → get back a full asset package:

- **Social media kits** — Posts, stories, covers for Instagram, LinkedIn, Twitter/X, Facebook
- **Ad creatives** — Display ads in standard IAB sizes
- **Brand collateral** — Business cards, letterheads, presentation templates
- **Content graphics** — Blog headers, email banners, thumbnails

## Quick Start

```bash
git clone https://github.com/BoluS095/brand-asset-generator.git
cd brand-asset-generator
pip install -r requirements.txt
cp .env.example .env

# Generate from example brief
python generate.py --brief briefs/example.yaml --output ./output
```

## How It Works

```
1. Upload your brand brief (colors, fonts, logo, style direction)
2. Select which asset types you need
3. Generator creates multiple variations per asset
4. Review, approve, and download your package
```

## Use Cases

- **Agencies** — Generate first-draft assets for client pitches in minutes
- **Startups** — Get a complete visual identity package without a design team
- **Content creators** — Produce consistent branded content at scale
- **E-commerce** — Auto-generate product marketing assets from catalog data

## Project Structure

```
brand-asset-generator/
├── generate.py          # Main entry point
├── engines/
│   ├── social.py        # Social media asset generation
│   └── __init__.py
├── utils/
│   ├── brand_parser.py  # Brief parsing and validation
│   └── __init__.py
├── briefs/              # Example brand briefs
└── requirements.txt
```

## Brief Format

```yaml
# briefs/example.yaml
brand:
  name: "Acme Corp"
  colors:
    primary: "#2563EB"
    secondary: "#1E40AF"
    accent: "#F59E0B"
  fonts:
    heading: "Inter"
    body: "Open Sans"
  style: "modern, clean, professional"

assets:
  - type: social_media
    platforms: [instagram, linkedin]
    variations: 3
  - type: display_ads
    sizes: ["300x250", "728x90", "160x600"]
```

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — see [LICENSE](LICENSE).

## Author

**Rafał Korzeniewski** — Python developer, trainer, and [PyWaw](https://pywaw.org) co-organizer.
