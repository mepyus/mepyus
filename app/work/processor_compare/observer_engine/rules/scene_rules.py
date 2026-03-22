from __future__ import annotations

from ..schema import ObserverFeatureSet


def infer_base_scene(features: ObserverFeatureSet) -> str:
    if features.has_comparison_marker and not features.has_reflection_marker:
        return "comparison"
    if features.has_evidence_marker and features.has_quote:
        return "evidence"
    if features.has_reflection_marker and features.has_question and not features.has_comparison_marker:
        return "reflection"
    return "explanation"
