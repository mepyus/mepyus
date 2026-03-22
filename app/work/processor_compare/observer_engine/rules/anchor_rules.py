from __future__ import annotations

from typing import List

from ..schema import ObserverAnchor, ObserverFeatureSet


def build_candidate_anchors(features: ObserverFeatureSet) -> List[ObserverAnchor]:
    anchors: List[ObserverAnchor] = []
    for term in features.anchor_terms[:3]:
        anchor_type = "semantic"
        if term in {"comparison", "contrast", "problem", "evidence"}:
            anchor_type = "structural"
        anchors.append(
            ObserverAnchor(
                label=term.replace(" ", "_"),
                anchor_type=anchor_type,
                evidence_text=_anchor_evidence(features.text, term),
                score=0.66,
            )
        )
    return anchors


def _anchor_evidence(text: str, term: str) -> str:
    compact = " ".join(text.split())
    if term in compact.lower():
        return compact[:120]
    return compact[:80]
