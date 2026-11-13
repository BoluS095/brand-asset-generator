import unittest

from engines.social import get_platform_size, plan_social_assets


class SocialAssetPlanningTests(unittest.TestCase):
    def test_known_platform_size(self):
        self.assertEqual(get_platform_size("instagram_story"), (1080, 1920))

    def test_unknown_asset_type_uses_documented_square_default(self):
        self.assertEqual(get_platform_size("unknown_asset"), (1080, 1080))

    def test_plans_one_record_per_requested_asset(self):
        planned = plan_social_assets(
            [
                {"type": "linkedin_post", "quantity": 2, "theme": "launch"},
                {"type": "instagram_story", "quantity": 1, "theme": "behind the scenes"},
            ],
            {"style": "minimal"},
        )

        self.assertEqual(len(planned), 3)
        self.assertEqual(planned[0].platform, "linkedin")
        self.assertEqual(planned[0].width, 1200)
        self.assertEqual(planned[0].height, 627)
        self.assertEqual(planned[0].theme, "launch")
        self.assertEqual(planned[0].style, "minimal")
        self.assertEqual(planned[2].asset_type, "instagram_story")

    def test_missing_quantity_defaults_to_one(self):
        planned = plan_social_assets([{"type": "instagram_post"}], {})
        self.assertEqual(len(planned), 1)
        self.assertEqual(planned[0].width, 1080)
        self.assertEqual(planned[0].height, 1080)


if __name__ == "__main__":
    unittest.main()
