# Brand Asset Generator

[![Python tests](https://github.com/BoluS095/brand-asset-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/BoluS095/brand-asset-generator/actions/workflows/tests.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A small Python prototype for loading a YAML brand brief and planning social-media asset dimensions. **It currently plans assets; it does not generate image files.**

## Current implementation

- Load the brand and asset sections from a YAML brief.
- Print brand metadata and a summary table of requested assets.
- Plan social-media asset records using a small set of platform dimension presets.
- Validate a few required brand fields and return warnings.
- Support a dry run that exits before any generation step.
- Run automated unit tests for YAML parsing, brand validation, palette ordering, platform dimensions, and asset planning.

## Not implemented yet

- Image-generation or image-editing provider integrations.
- Logo overlays, typography rendering, or brand collateral rendering.
- Asset export, packaging, or delivery.

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

## Run tests

The test suite uses Python's standard `unittest` framework. GitHub Actions runs it on Python 3.10, 3.11, and 3.12.

```bash
python -m unittest discover -s tests -v
```

## Project structure

```
generate.py
engines/
  social.py
utils/
  brand_parser.py
briefs/
  example.yaml
tests/
  test_brand_parser.py
  test_social.py
.github/
  workflows/
    tests.yml
```

## Contributing

Contributions are welcome. Please include focused tests for brief parsing, validation, or asset planning. New generation-provider integrations should be clearly scoped and must not imply that image generation is implemented until it is tested end to end.

## License

MIT. See LICENSE.
