from __future__ import annotations

from collections import Counter
from typing import Dict, Iterable, List

from .schema import MergedObserverOutput, ObserverAnchor, ObserverOutput


def merge_observer_outputs(outputs: Iterable[ObserverOutput]) -> MergedObserverOutput:
    items = list(outputs)
    by_name = {item.profile_name: item for item in items}
    codex = by_name["codex_like"]
    chatgpt = by_name["chatgpt_like"]
    gemini = by_name["gemini_like"]

    signals: List[str] = []

    scene = codex.scene if codex.scene == chatgpt.scene else codex.scene
    if codex.scene != chatgpt.scene:
        signals.append("scene_disagreement")
    if gemini.scene in {"reflection"} and scene != "reflection":
        signals.append("gemini_reflection_signal")

    role = codex.role if codex.role == chatgpt.role else codex.role
    if codex.role != chatgpt.role:
        signals.append("role_disagreement")
    if gemini.role == "expansion" and role != "expansion":
        signals.append("gemini_expansion_signal")

    ambiguity = max(codex.ambiguity, chatgpt.ambiguity)
    confidence = round((codex.confidence + chatgpt.confidence) / 2.0, 3)
    direction = round((codex.direction + chatgpt.direction) / 2.0, 3)
    intensity = round((codex.intensity + chatgpt.intensity) / 2.0, 3)
    stability = min(codex.stability, chatgpt.stability)
    if "gemini_expansion_signal" in signals or "gemini_reflection_signal" in signals:
        stability = max(0.0, round(stability - 0.03, 3))

    anchors = _merge_anchors(codex.anchors, chatgpt.anchors, gemini.anchors)
    semantic_tags = _merge_tags(codex.semantic_tags, chatgpt.semantic_tags)
    structural_tags = _merge_tags(codex.structural_tags, chatgpt.structural_tags)
    evidence_text = _merge_tags(codex.evidence_text, chatgpt.evidence_text)[:3]

    return MergedObserverOutput(
        scene=scene,
        role=role,
        direction=direction,
        intensity=intensity,
        stability=round(stability, 3),
        confidence=confidence,
        ambiguity=round(ambiguity, 3),
        anchors=anchors,
        semantic_tags=semantic_tags,
        structural_tags=structural_tags,
        evidence_text=evidence_text,
        why_short=f"{scene}/{role}는 codex_like와 chatgpt_like 합의 또는 codex_like 우선으로 병합됐다.",
        signals=signals,
        profile_outputs={name: output.to_record() for name, output in by_name.items()},
    )


def _merge_anchors(*anchor_groups: List[ObserverAnchor]) -> List[ObserverAnchor]:
    seen = set()
    merged: List[ObserverAnchor] = []
    for group in anchor_groups:
        for anchor in group:
            key = (anchor.label, anchor.anchor_type)
            if key in seen:
                continue
            seen.add(key)
            merged.append(anchor)
            if len(merged) >= 4:
                return merged
    return merged


def _merge_tags(*groups: List[str]) -> List[str]:
    seen = []
    for group in groups:
        for item in group:
            if item not in seen:
                seen.append(item)
    return seen[:5]
