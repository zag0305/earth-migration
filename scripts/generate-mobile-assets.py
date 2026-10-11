"""Build the deterministic, low-memory texture pack used by mobile browsers."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "mobile"

TEXTURES = {
    "earth_day_1024.jpg": ("assets/planets/earth_day_4k.jpg", (1024, 512), 78),
    "earth_night_1024.jpg": ("assets/earth/earth_night_4096.jpg", (1024, 512), 76),
    "earth_surface_1024.jpg": ("assets/earth/earth_bump_roughness_clouds_4096.jpg", (1024, 512), 78),
    "earth_clouds_1024.jpg": ("assets/planets/earth_clouds_4k.jpg", (1024, 512), 76),
    "milkyway_1024.jpg": ("assets/sky/milkyway_4k.jpg", (1024, 512), 76),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (source, size, quality) in TEXTURES.items():
        with Image.open(ROOT / source) as image:
            image = image.convert("RGB")
            image.thumbnail(size, Image.Resampling.LANCZOS)
            image.save(
                OUT / name,
                "JPEG",
                quality=quality,
                optimize=True,
                progressive=True,
                subsampling="4:2:0",
            )
        print(f"{name}: {(OUT / name).stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
