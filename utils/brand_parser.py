"""Parse and validate brand guidelines from YAML briefs."""
import yaml
from pathlib import Path


def load_brand(brief_path: str) -> dict:
    """Load brand info from a brief YAML file."""
    with open(brief_path) as f:
        config = yaml.safe_load(f)
    return config.get("brand", {})


def validate_brand(brand: dict) -> list[str]:
    """Validate brand config and return any warnings."""
    warnings = []
    if not brand.get("name"):
        warnings.append("Brand name is missing")
    if not brand.get("colors"):
        warnings.append("No colors defined — output will use defaults")
    elif not brand["colors"].get("primary"):
        warnings.append("No primary color defined")
    if not brand.get("fonts"):
        warnings.append("No fonts specified — using system defaults")
    if not brand.get("logo"):
        warnings.append("No logo path — assets won't include logo overlay")
    return warnings


def get_color_palette(brand: dict) -> list[str]:
    """Extract ordered color palette from brand config."""
    colors = brand.get("colors", {})
    palette = []
    for key in ["primary", "secondary", "accent", "background"]:
        if key in colors:
            palette.append(colors[key])
    return palette
