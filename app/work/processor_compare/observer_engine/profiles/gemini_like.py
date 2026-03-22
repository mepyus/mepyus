from __future__ import annotations

from ..schema import ObserverFeatureSet, ObserverOutput
from ..rules.anchor_rules import build_candidate_anchors
from ..rules.role_rules import infer_base_role
from ..rules.scene_rules import infer_base_scene
from ..rules.score_rules import infer_base_scores


def gemini_like_observer(features: ObserverFeatureSet) -> ObserverOutput:
    scene = infer_base_scene(features)
    role = infer_base_role(features)
    scores = infer_base_scores(features)

    if scene == "explanation" and (features.has_reflection_marker or features.has_generalization_marker):
        scene = "reflection"
    if role in {"support", "contrast"} and (features.has_generalization_marker or features.has_reflection_marker):
        role = "expansion"

    # apply correction layer directly to keep schema-safe but preserve bias
    scores["ambiguity"] = max(0.22, round(scores["ambiguity"] - 0.04, 3))
    scores["confidence"] = min(0.84, round(scores["confidence"] + 0.01, 3))
    scores["stability"] = max(0.0, round(scores["stability"] - (0.05 if features.has_mixed_signal else 0.0), 3))

    return ObserverOutput(
        profile_name="gemini_like",
        scene=scene,
        role=role,
        direction=scores["direction"],
        intensity=scores["intensity"],
        stability=scores["stability"],
        confidence=scores["confidence"],
        ambiguity=scores["ambiguity"],
        anchors=build_candidate_anchors(features),
        semantic_tags=features.anchor_terms[:4],
        structural_tags=["internal_observer", "abstraction_prone", scene, role][:4],
        evidence_text=_evidence(features),
        why_short=f"상위 의미 이동을 민감하게 읽어 {scene}/{role}로 기울어진다.",
        notes=["secondary abstract observer"],
    )


def _evidence(features: ObserverFeatureSet) -> list[str]:
    text = features.text
    parts = [part.strip() for part in text.split(".") if part.strip()]
    return parts[:2] or [text[:80]]
