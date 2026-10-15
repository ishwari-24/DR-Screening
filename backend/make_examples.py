"""Generates example result files for the frontend team (one per status)."""
import json

from backend import schema
from backend.config import EXAMPLES_DIR


def save(name, data):
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    path = EXAMPLES_DIR / name
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print("Wrote", path)


ok = schema.ok_result(
    schema.quality_result(True, 82, 123.4, 0.81, True, "Image quality acceptable"),
    schema.prediction_result([0.02, 0.05, 0.87, 0.04, 0.02]),
    schema.explainability_result("outputs/gradcam/example_heatmap.png",
                                 "outputs/gradcam/example_overlay.png"),
)
recapture = schema.recapture_result(
    schema.quality_result(False, 31, 12.0, 0.55, True,
                          "Image is too blurry. Please hold the camera steady and recapture.")
)
error = schema.error_result("UNSUPPORTED_FORMAT", "Unsupported file type '.gif'.")

save("example_ok.json", ok)
save("example_recapture.json", recapture)
save("example_error.json", error)
print("\nNOTE: all values are FORMAT ILLUSTRATIONS, not real model results.")