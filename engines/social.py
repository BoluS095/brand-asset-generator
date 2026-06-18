"""Social media asset generation engine."""
from dataclasses import dataclass


PLATFORM_SIZES = {
    "instagram_post": (1080, 1080),
    "instagram_story": (1080, 1920),
    "instagram_reel_cover": (1080, 1920),
    "linkedin_post": (1200, 627),
    "linkedin_banner": (1584, 396),
    "twitter_post": (1200, 675),
    "twitter_header": (1500, 500),
    "facebook_post": (1200, 630),
    "facebook_cover": (820, 312),
}


@dataclass
class SocialAsset:
    platform: str
    asset_type: str
    width: int
    height: int
    theme: str
    style: str
    output_path: str = ""


def get_platform_size(asset_type: str) -> tuple[int, int]:
    """Get the recommended size for a platform asset type."""
    return PLATFORM_SIZES.get(asset_type, (1080, 1080))


def plan_social_assets(assets_config: list, brand: dict) -> list[SocialAsset]:
    """Plan social assets from brief config."""
    planned = []
    for asset in assets_config:
        asset_type = asset.get("type", "instagram_post")
        w, h = get_platform_size(asset_type)
        for i in range(asset.get("quantity", 1)):
            planned.append(SocialAsset(
                platform=asset_type.split("_")[0],
                asset_type=asset_type,
                width=w,
                height=h,
                theme=asset.get("theme", ""),
                style=brand.get("style", ""),
            ))
    return planned
