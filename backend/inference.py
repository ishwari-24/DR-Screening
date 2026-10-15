"""Single entry point of the backend.

DUMMY VERSION: returns fake placeholder values so the frontend and tests can
be built before the real model exists. Dummy output is clearly labelled and
must never be shown as a real result.

Usage (run from the project root):
    python -m backend.inference --image path/to/image.jpg --json out.json
"""
import argparse
import json
import sys
from pathlib import Path

from backend import schema
from backend.config import SUPPORTED_EXTENSIONS


def run_pipeline(image_path):
    """Run the screening pipeline on one image and return a result dict."""
    path = Path(image_path)

    # --- Input validation (real logic, stays in the final version) ---
    if not path.exists():
        return schema.error_result("FILE_NOT_FOUND", f"File not found: {path}")
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        return schema.error_result(
            "UNSUPPORTED_FORMAT",
            f"Unsupported file type '{path.suffix}'. "
            f"Use one of: {', '.join(sorted(SUPPORTED_EXTENSIONS))}",
        )

    # --- DUMMY steps (replaced in later tasks) ---
    # A file named like "blurry_x.jpg" triggers the recapture path for UI testing.
    if "blurry" in path.name.lower():
        q = schema.quality_result(
            False, 31, 12.0, 0.55, True,
            "[DUMMY] Image is too blurry. Please hold the camera steady and recapture.",
        )
        return schema.recapture_result(q)

    q = schema.quality_result(True, 82, 123.4, 0.81, True,
                              "[DUMMY] Image quality acceptable")
    p = schema.prediction_result([0.02, 0.05, 0.87, 0.04, 0.02])
    e = schema.explainability_result("outputs/gradcam/dummy_heatmap.png",
                                     "outputs/gradcam/dummy_overlay.png")
    return schema.ok_result(q, p, e)


def main():
    parser = argparse.ArgumentParser(description="DR screening inference (dummy)")
    parser.add_argument("--image", required=True, help="Path to fundus image")
    parser.add_argument("--json", help="Optional path to save the result JSON")
    args = parser.parse_args()

    result = run_pipeline(args.image)
    text = json.dumps(result, indent=2)
    print(text)

    if args.json:
        out = Path(args.json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")

    # Exit code 0 for OK and RECAPTURE (valid outcomes), 1 for ERROR
    sys.exit(1 if result["status"] == "ERROR" else 0)


if __name__ == "__main__":
    main()