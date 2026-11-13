# Brand Asset Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A small Python prototype for loading a YAML brand brief and planning social-media asset dimensions. **It currently plans assets; it does not generate image files.**

## Current implementation

- Load the brand and asset sections from a YAML brief.
- Print brand metadata and a summary table of requested assets.
- Plan social-media asset records using a small set of platform dimension presets.
- Validate a few required brand fields and return warnings.
- Support a dry run that exits before any generation step.

## Not implemented yet

- Image-generation or image-editing provider integrations.
- Logo overlays, typography rendering, or brand collateral rendering.
- Asset export, packaging, or delivery.
- Automated tests or CI.

The non-dry-run CLI currently reports that generation engines are coming soon. The project should be treated as an early-stage planning prototype, not as an end-to-end AI asset generator.

## Quick start

Python 3.10+ is recommended.

```bash
git clone https://github.com/BoluS095/brand-asset-generator.git
cd brand-asset-generator
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python generate.py --brief briefs/example.yaml --dry-run
```

To see the current non-dry-run placeholder behaviour, omit `--dry-run`. It does not produce images.

## Project structure

```
generate.py          # CLI and asset-plan summary
engines/social.py    # Platform dimensions and SocialAsset planning records
utils/brand_parser.py # YAML brand loading and simple validation
briefs/example.yaml  # Example brief
```

## Contributing

Contributions are welcome. The most useful next steps are automated tests for brief validation and asset planning, followed by a clearly scoped first image-generation adapter.

## License

MIT. See [LICENSE](LICENSE).
