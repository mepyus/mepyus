from __future__ import annotations

from ..schema import ObserverFeatureSet


def infer_base_scores(features: ObserverFeatureSet) -> dict[str, float]:
    direction = 0.72
    intensity = 0.58
    stability = 0.64
    confidence = 0.72
    ambiguity = 0.28

    if features.has_problem_marker:
        direction += 0.05
        intensity += 0.05
    if features.has_comparison_marker:
        stability -= 0.06
        ambiguity += 0.05
    if features.has_reflection_marker:
        ambiguity += 0.08
        confidence -= 0.04
    if features.has_evidence_marker:
        confidence += 0.04
    if features.has_mixed_signal:
        stability -= 0.12
        ambiguity += 0.08
    if features.has_question:
        ambiguity += 0.05
        confidence -= 0.03

    return {
        "direction": _clamp(direction),
        "intensity": _clamp(intensity),
        "stability": _clamp(stability),
        "confidence": _clamp(confidence),
        "ambiguity": _clamp(ambiguity),
    }


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, round(value, 3)))
