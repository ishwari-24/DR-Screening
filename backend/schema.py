"""Builders for the three result types defined in interface contract v1.0.

Every other module creates its output through these functions, so the JSON
shape can never drift between modules.
"""
from backend.config import (
    DISCLAIMER, GRADE_NAMES, INTERFACE_VERSION,
    LOW_CONFIDENCE_THRESHOLD, REFERABLE_MIN_GRADE,
)


def quality_result(good, score, sharpness, illumination, fov_detected, message):
    return {
        "quality": "GOOD" if good else "RECAPTURE_REQUIRED",
        "score": int(score),
        "sharpness": float(sharpness),
        "illumination": float(illumination),
        "fov_detected": bool(fov_detected),
        "message": message,
    }


def prediction_result(probabilities):
    """Build the prediction block from 5 class probabilities."""
    if len(probabilities) != 5:
        raise ValueError("Expected 5 probabilities, got %d" % len(probabilities))
    grade = max(range(5), key=lambda i: probabilities[i])
    confidence = float(probabilities[grade])
    referable = grade >= REFERABLE_MIN_GRADE
    low_conf = confidence < LOW_CONFIDENCE_THRESHOLD

    if low_conf:
        recommendation = "Low confidence - human review recommended"
    elif referable:
        recommendation = "Ophthalmologist review recommended"
    else:
        recommendation = "No referable DR detected; follow routine screening schedule"

    return {
        "grade": grade,
        "grade_name": GRADE_NAMES[grade],
        "confidence": round(confidence, 4),
        "probabilities": [round(float(p), 4) for p in probabilities],
        "referable": referable,
        "low_confidence": low_conf,
        "recommendation": recommendation,
    }


def explainability_result(heatmap_path, overlay_path):
    return {"heatmap_path": str(heatmap_path), "overlay_path": str(overlay_path)}


def ok_result(quality, prediction, explainability):
    return {
        "version": INTERFACE_VERSION,
        "status": "OK",
        "quality": quality,
        "prediction": prediction,
        "explainability": explainability,
        "disclaimer": DISCLAIMER,
    }


def recapture_result(quality):
    return {
        "version": INTERFACE_VERSION,
        "status": "RECAPTURE_REQUIRED",
        "quality": quality,
        "disclaimer": DISCLAIMER,
    }


def error_result(code, message):
    return {
        "version": INTERFACE_VERSION,
        "status": "ERROR",
        "error": {"code": code, "message": message},
        "disclaimer": DISCLAIMER,
    }