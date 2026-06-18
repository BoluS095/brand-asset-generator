# 🎯 Brand Asset Generator

> Generate complete brand asset packages from a single creative brief.

## What It Does

Feed it a brand brief → get back a full asset package:
- **Social media kits** — Posts, stories, covers for Instagram, LinkedIn, Twitter/X, Facebook
- **Ad creatives** — Display ads in standard IAB sizes
- **Brand collateral** — Business cards, letterheads, presentation templates
- **Content graphics** — Blog headers, email banners, thumbnails

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

## Quick Start

```bash
git clone https://github.com/BoluS095/brand-asset-generator.git
cd brand-asset-generator
pip install -r requirements.txt
cp .env.example .env
# Add your API keys

# Generate from a brief
python generate.py --brief briefs/example.yaml --output ./output
```

## Project Structure

```
brand-asset-generator/
├── generate.py           # Main entry point
├── briefs/               # Brief templates & examples
├── templates/            # Asset layout templates
├── engines/
│   ├── social.py         # Social media asset engine
│   ├── ads.py            # Ad creative engine
│   ├── collateral.py     # Brand collateral engine
│   └── content.py        # Content graphics engine
├── utils/
│   ├── brand_parser.py   # Parse brand guidelines
│   ├── layout.py         # Layout & composition
│   └── export.py         # Multi-format export
├── requirements.txt
└── README.md
```

## Roadmap

- [x] Project architecture
- [x] Brand brief parser
- [ ] Social media asset engine (Instagram, LinkedIn, X)
- [ ] Ad creative engine (IAB standard sizes)
- [ ] Template system for consistent layouts
- [ ] Multi-format export (PNG, SVG, PDF)
- [ ] Web UI for brief input and preview
- [ ] API endpoint for programmatic generation

## License

MIT
