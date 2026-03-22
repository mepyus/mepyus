from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class ObserverFeatureSet:
    text: str
    lowered: str
    sentence_count: int
    has_quote: bool
    has_question: bool
    has_comparison_marker: bool
    has_reflection_marker: bool
    has_evidence_marker: bool
    has_example_marker: bool
    has_problem_marker: bool
    has_definition_marker: bool
    has_generalization_marker: bool
    has_mixed_signal: bool
    token_count: int
    anchor_terms: List[str] = field(default_factory=list)

    def to_record(self) -> Dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class ObserverAnchor:
    label: str
    anchor_type: str
    evidence_text: str
    score: float

    def to_record(self) -> Dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class ObserverOutput:
    profile_name: str
    scene: str
    role: str
    direction: float
    intensity: float
    stability: float
    confidence: float
    ambiguity: float
    anchors: List[ObserverAnchor] = field(default_factory=list)
    semantic_tags: List[str] = field(default_factory=list)
    structural_tags: List[str] = field(default_factory=list)
    evidence_text: List[str] = field(default_factory=list)
    why_short: str = ""
    notes: List[str] = field(default_factory=list)

    def to_record(self) -> Dict[str, object]:
        payload = asdict(self)
        payload["anchors"] = [anchor.to_record() for anchor in self.anchors]
        return payload


@dataclass(frozen=True)
class MergedObserverOutput:
    scene: str
    role: str
    direction: float
    intensity: float
    stability: float
    confidence: float
    ambiguity: float
    anchors: List[ObserverAnchor] = field(default_factory=list)
    semantic_tags: List[str] = field(default_factory=list)
    structural_tags: List[str] = field(default_factory=list)
    evidence_text: List[str] = field(default_factory=list)
    why_short: str = ""
    signals: List[str] = field(default_factory=list)
    profile_outputs: Dict[str, Dict[str, object]] = field(default_factory=dict)

    def to_record(self) -> Dict[str, object]:
        payload = asdict(self)
        payload["anchors"] = [anchor.to_record() for anchor in self.anchors]
        return payload
