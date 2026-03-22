from __future__ import annotations

from ..schema import ObserverFeatureSet


def infer_base_role(features: ObserverFeatureSet) -> str:
    if features.has_problem_marker and features.has_generalization_marker:
        return "problem"
    if features.has_comparison_marker:
        return "contrast"
    if features.has_definition_marker:
        return "definition"
    if features.has_example_marker or (features.has_quote and features.has_evidence_marker):
        return "example"
    if features.has_generalization_marker and features.has_reflection_marker:
        return "expansion"
    return "support"
