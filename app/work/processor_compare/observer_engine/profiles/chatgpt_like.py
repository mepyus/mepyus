from __future__ import annotations

from ..schema import ObserverFeatureSet, ObserverOutput
from ..rules.anchor_rules import build_candidate_anchors
from ..rules.role_rules import infer_base_role
from ..rules.scene_rules import infer_base_scene
from ..rules.score_rules import infer_base_scores


def chatgpt_like_observer(features: ObserverFeatureSet) -> ObserverOutput:
    scene = infer_base_scene(features)
    role = infer_base_role(features)
    scores = infer_base_scores(features)

    if features.has_comparison_marker:
        scene = "comparison"
    if role == "definition":
        role = "thesis" if features.has_generalization_marker else "definition"
    if role == "expansion" and not features.has_reflection_marker:
        role = "support"

    scores["confidence"] = min(1.0, round(scores["confidence"] + 0.02, 3))
    scores["ambiguity"] = max(0.0, round(scores["ambiguity"] - 0.01, 3))

    return ObserverOutput(
        profile_name="chatgpt_like",
        scene=scene,
        role=role,
        direction=scores["direction"],
        intensity=scores["intensity"],
        stability=scores["stability"],
        confidence=scores["confidence"],
        ambiguity=scores["ambiguity"],
        anchors=build_candidate_anchors(features),
        semantic_tags=features.anchor_terms[:4],
        structural_tags=["internal_observer", "surface_structure", scene, role][:4],
        evidence_text=_evidence(features),
        why_short=f"표면 구조 신호를 강하게 읽어 {scene}/{role}로 판정한다.",
        notes=["surface structure sensitive"],
    )


def _evidence(features: ObserverFeatureSet) -> list[str]:
    text = features.text
    parts = [part.strip() for part in text.split(".") if part.strip()]
    return parts[:2] or [text[:80]]
