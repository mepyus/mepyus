from __future__ import annotations

from ..schema import ObserverFeatureSet, ObserverOutput
from ..rules.anchor_rules import build_candidate_anchors
from ..rules.role_rules import infer_base_role
from ..rules.scene_rules import infer_base_scene
from ..rules.score_rules import infer_base_scores


def codex_like_observer(features: ObserverFeatureSet) -> ObserverOutput:
    scene = infer_base_scene(features)
    role = infer_base_role(features)
    scores = infer_base_scores(features)

    if scene == "reflection" and not features.has_question and not features.has_generalization_marker:
        scene = "explanation"
    if role == "expansion" and not features.has_generalization_marker:
        role = "support"

    scores["ambiguity"] = min(1.0, round(scores["ambiguity"] + 0.06, 3))
    scores["confidence"] = max(0.0, round(scores["confidence"] - 0.03, 3))

    return ObserverOutput(
        profile_name="codex_like",
        scene=scene,
        role=role,
        direction=scores["direction"],
        intensity=scores["intensity"],
        stability=scores["stability"],
        confidence=scores["confidence"],
        ambiguity=scores["ambiguity"],
        anchors=build_candidate_anchors(features),
        semantic_tags=features.anchor_terms[:4],
        structural_tags=_structural_tags(scene, role),
        evidence_text=_evidence(features),
        why_short=f"{scene} 중심으로 읽되 {role} 기능을 보수적으로 유지한다.",
        notes=["conservative baseline"],
    )


def _structural_tags(scene: str, role: str) -> list[str]:
    tags = ["internal_observer", scene, role]
    return tags[:4]


def _evidence(features: ObserverFeatureSet) -> list[str]:
    text = features.text
    parts = [part.strip() for part in text.split(".") if part.strip()]
    return parts[:2] or [text[:80]]
