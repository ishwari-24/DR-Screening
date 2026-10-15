"""Central configuration for the DR screening backend.

All paths are relative to the project root, so the code runs on any machine.
"""
from pathlib import Path

# Project root = parent of the backend/ folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_ROOT / "model"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
GRADCAM_DIR = OUTPUT_DIR / "gradcam"
REPORT_DIR = OUTPUT_DIR / "reports"
EXAMPLES_DIR = PROJECT_ROOT / "documentation" / "architecture" / "examples"

INTERFACE_VERSION = "1.0"

GRADE_NAMES = {
    0: "No DR",
    1: "Mild DR",
    2: "Moderate DR",
    3: "Severe DR",
    4: "Proliferative DR",
}

# Referable DR = grade 2 or higher
REFERABLE_MIN_GRADE = 2

# Below this top-class probability we recommend human review.
# INITIAL ENGINEERING VALUE - to be tuned on validation data, not clinically validated.
LOW_CONFIDENCE_THRESHOLD = 0.60

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

DISCLAIMER = "AI screening support, not a medical diagnosis."