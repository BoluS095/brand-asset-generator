import tempfile
import unittest
from pathlib import Path

from utils.brand_parser import get_color_palette, load_brand, validate_brand


class BrandParserTests(unittest.TestCase):
    def test_loads_brand_from_yaml_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "brief.yaml"
            path.write_text(
                "brand:\n  name: Example\n  style: minimal\nassets: []\n",
                encoding="utf-8",
            )
            self.assertEqual(load_brand(str(path)), {"name": "Example", "style": "minimal"})

    def test_reports_missing_optional_brand_guidance(self):
        warnings = validate_brand({"name": "Example"})
        self.assertIn("No colors defined — output will use defaults", warnings)
        self.assertIn("No fonts specified — using system defaults", warnings)
        self.assertIn("No logo path — assets won't include logo overlay", warnings)

    def test_reports_missing_name_and_primary_color(self):
        warnings = validate_brand({"colors": {"secondary": "#ffffff"}})
        self.assertIn("Brand name is missing", warnings)
        self.assertIn("No primary color defined", warnings)

    def test_returns_palette_in_documented_order(self):
        brand = {
            "colors": {
                "accent": "#333333",
                "primary": "#111111",
                "background": "#ffffff",
                "secondary": "#222222",
            }
        }
        self.assertEqual(
            get_color_palette(brand),
            ["#111111", "#222222", "#333333", "#ffffff"],
        )

    def test_empty_palette_is_empty(self):
        self.assertEqual(get_color_palette({}), [])


if __name__ == "__main__":
    unittest.main()
