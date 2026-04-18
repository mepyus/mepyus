from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from app.core.runtime.context_linked_segmentation import LinkedSegment
from app.core.runtime.multi_lens_document_readout import (
    SurfacedDocumentReadout,
    surface_readout,
)


ReadingStrength = Literal["strong", "weak", "caution", "absent"]
LineOperatingState = Literal["active", "parked", "candidate"]

_PRIMARY_LENS_KEYWORDS: dict[str, dict[str, tuple[str, ...]]] = {
}

_KNOWN_LINE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "line_pre_read_eye": ("pre-read", "pre read", "eye", "pre_read_eye", "사전 읽기"),
    "line_raw_return_preservation": ("raw", "return", "preservation", "source", "원문", "raw_return"),
}


@dataclass(frozen=True)
class SegmentLineReading:
    linked_segment_id: str
    source_id: str
    line_id: str
    line_name: str
    reading_strength: ReadingStrength
    reading_basis: str
    provenance: Any
    caution_reason: str | None = None


@dataclass(frozen=True)
class DocumentLineLensingResult:
    source_id: str
    readings: list[SegmentLineReading]
    lens_ids_used: list[str]
    is_stable_lens_only: bool


@dataclass(frozen=True)
class LineDefinition:
    line_id: str
    line_name: str
    status: str
    thickness_level: str
    operating_state: LineOperatingState
    is_primary: bool


class MultiLensDocumentReader:
    def __init__(self, registry_path: str) -> None:
        self.registry_path = Path(registry_path)
        self.line_definitions = self._load_line_definitions()
        self.primary_line_definitions = [line for line in self.line_definitions if line.is_primary]
        self.secondary_line_definitions = [line for line in self.line_definitions if not line.is_primary]
        self.line_definitions_by_id = {line.line_id: line for line in self.line_definitions}

    def read(self, segments: list[LinkedSegment]) -> DocumentLineLensingResult:
        if not segments:
            return DocumentLineLensingResult(
                source_id="",
                readings=[],
                lens_ids_used=[],
                is_stable_lens_only=True,
            )

        source_id = segments[0].source_id
        ordered_lenses = self.primary_line_definitions
        readings = [
            self._apply_lens(segment, lens)
            for segment in segments
            for lens in ordered_lenses
        ]
        return DocumentLineLensingResult(
            source_id=source_id,
            readings=readings,
            lens_ids_used=[line.line_id for line in ordered_lenses],
            is_stable_lens_only=True,
        )

    def surface_readout(self, result: DocumentLineLensingResult) -> SurfacedDocumentReadout:
        return surface_readout(result, self.line_definitions_by_id)

    def _load_line_definitions(self) -> list[LineDefinition]:
        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        lines = list(registry.get("lines", []))
        return [self._line_definition_from_registry(line) for line in lines]

    def _line_definition_from_registry(self, line: dict[str, Any]) -> LineDefinition:
        line_id = str(line.get("line_id", ""))
        status = str(line.get("status", ""))
        thickness_level = str(line.get("thickness_level", ""))
        is_primary = status == "stable" and thickness_level == "thick"
        if line_id == "line_transition_over_surface":
            operating_state: LineOperatingState = "parked"
        elif is_primary:
            operating_state = "active"
        else:
            operating_state = "candidate"
        return LineDefinition(
            line_id=line_id,
            line_name=str(line.get("line_name", "")),
            status=status,
            thickness_level=thickness_level,
            operating_state=operating_state,
            is_primary=is_primary,
        )

    def _apply_lens(self, segment: LinkedSegment, line: LineDefinition) -> SegmentLineReading:
        line_id = line.line_id
        line_name = line.line_name
        linked_text = segment.linked_text.lower()
        maturity_note = self._lens_basis_note(line)

        if line_id == "line_transition_over_surface":
            reading_strength, reading_basis, caution_reason = self._apply_transition_over_surface_lens(
                segment=segment,
                line=line,
                linked_text=linked_text,
                maturity_note=maturity_note,
            )
        elif line_id == "line_input_to_reading_organ":
            reading_strength, reading_basis, caution_reason = self._apply_input_to_reading_organ_lens(
                segment=segment,
                line=line,
                linked_text=linked_text,
                maturity_note=maturity_note,
            )
        else:
            strong_seeds, partial_seeds = self._keywords_for_line(line_id, line_name)

            # TBD: reading strength stays on a minimal keyword heuristic in v0.
            matched_strong = [seed for seed in strong_seeds if seed.lower() in linked_text]
            matched_partial = [seed for seed in partial_seeds if seed.lower() in linked_text]

            caution_reason = None
            if matched_strong and segment.linkage_confidence != "low":
                reading_strength = "strong"
                reading_basis = f"matched seed: {matched_strong[0]}; {maturity_note} basis"
            elif matched_strong and segment.linkage_confidence == "low":
                reading_strength = "weak"
                reading_basis = f"matched seed but low-confidence downgrade: {matched_strong[0]}; {maturity_note} basis"
            elif matched_partial:
                reading_strength = "weak"
                reading_basis = f"partial match only: {matched_partial[0]}; downgraded to weak; {maturity_note} basis"
            elif segment.linkage_confidence == "low":
                reading_strength = "weak"
                reading_basis = f"low linkage_confidence with no relevant seed; {maturity_note} basis"
            elif not line.is_primary:
                reading_strength = "caution"
                caution_reason = "candidate_or_thin_lens"
                reading_basis = f"non-primary lens with no relevant seed; {maturity_note}"
            else:
                reading_strength = "absent"
                reading_basis = f"no relevant seed / no basis; {maturity_note}"

        return SegmentLineReading(
            linked_segment_id=segment.linked_segment_id,
            source_id=segment.source_id,
            line_id=line_id,
            line_name=line_name,
            reading_strength=reading_strength,
            reading_basis=reading_basis,
            caution_reason=caution_reason,
            provenance={
                "kind": "multi_lens_document_reading_v0",
                "registry_path": str(self.registry_path),
                "linked_segment_id": segment.linked_segment_id,
                "line_id": line_id,
                "operating_state": line.operating_state,
            },
        )

    def _apply_input_to_reading_organ_lens(
        self,
        segment: LinkedSegment,
        line: LineDefinition,
        linked_text: str,
        maturity_note: str,
    ) -> tuple[ReadingStrength, str, str | None]:
        pattern = self._input_to_reading_pattern(linked_text)

        if segment.linkage_confidence == "low":
            if pattern["signal_count"] > 0:
                return (
                    "caution",
                    f"input-processing flow is hinted, but linkage confidence is low; {self._join_pattern_basis(pattern)}; {maturity_note}",
                    "low_linkage_confidence",
                )
            return (
                "caution",
                f"input-processing flow is unclear and linkage confidence is low; {maturity_note}",
                "low_linkage_confidence",
            )
        if segment.linkage_reason == "contrast_pair" and pattern["signal_count"] > 0 and not pattern["has_flow"]:
            return (
                "caution",
                f"processing hint appears inside contrast context without a clear input-to-result flow; {self._join_pattern_basis(pattern)}; {maturity_note}",
                "contrast_pair_context",
            )
        if pattern["has_flow"] and pattern["signal_count"] >= 2:
            return (
                "strong",
                f"text shows an input-to-processing-to-result flow; {self._join_pattern_basis(pattern)}; {maturity_note}",
                None,
            )
        if pattern["signal_count"] >= 1:
            return (
                "weak",
                f"text hints at input-processing movement, but the full flow stays partial; {self._join_pattern_basis(pattern)}; {maturity_note}",
                None,
            )
        if not line.is_primary:
            return (
                "caution",
                f"non-primary lens with no clear input-processing pattern; {maturity_note}",
                "candidate_or_thin_lens",
            )
        return "absent", f"no input-processing-result pattern is visible in the text; {maturity_note}", None

    def _apply_transition_over_surface_lens(
        self,
        segment: LinkedSegment,
        line: LineDefinition,
        linked_text: str,
        maturity_note: str,
    ) -> tuple[ReadingStrength, str, str | None]:
        pattern = self._transition_over_surface_pattern(linked_text)

        if segment.linkage_confidence == "low":
            if pattern["signal_count"] > 0:
                return (
                    "caution",
                    f"transition-like movement is hinted, but linkage confidence is low; {self._join_pattern_basis(pattern)}; {maturity_note}",
                    "low_linkage_confidence",
                )
            return (
                "caution",
                f"transition pattern is unclear and linkage confidence is low; {maturity_note}",
                "low_linkage_confidence",
            )
        if segment.linkage_reason == "contrast_pair" and pattern["signal_count"] > 0 and not pattern["has_boundary_bridge"]:
            return (
                "caution",
                f"change is present inside contrast context, but boundary-crossing remains ambiguous; {self._join_pattern_basis(pattern)}; {maturity_note}",
                "contrast_pair_context",
            )
        if pattern["has_boundary_bridge"] and pattern["signal_count"] >= 2:
            return (
                "strong",
                f"text shows a surface or boundary transition across two sides; {self._join_pattern_basis(pattern)}; {maturity_note}",
                None,
            )
        if pattern["signal_count"] >= 1:
            return (
                "weak",
                f"text hints at movement or transition, but the full boundary-crossing stays partial; {self._join_pattern_basis(pattern)}; {maturity_note}",
                None,
            )
        return "absent", f"no surface-transition or boundary-crossing pattern is visible in the text; {maturity_note}", None

    def _input_to_reading_pattern(self, linked_text: str) -> dict[str, object]:
        input_tokens = (
            "입력",
            "자료",
            "source",
            "feed",
            "ingest",
            "input",
            "가져온",
            "가져와",
            "받아",
            "들어온",
            "넣어",
        )
        processing_tokens = (
            "읽",
            "해석",
            "파싱",
            "처리",
            "변환",
            "정리",
            "가공",
            "parse",
            "interpret",
            "process",
            "transform",
        )
        result_tokens = (
            "결과",
            "출력",
            "response",
            "output",
            "return",
            "report",
            "surface",
            "보여",
            "나온",
        )
        has_input = any(token in linked_text for token in input_tokens)
        has_processing = any(token in linked_text for token in processing_tokens)
        has_result = any(token in linked_text for token in result_tokens)
        has_flow = (
            has_input and has_processing and has_result
        ) or (
            (has_input and has_processing and ("결과" in linked_text or "출력" in linked_text))
            or ("->" in linked_text and has_processing)
        )
        basis = []
        if has_input:
            basis.append("input material enters the reading path")
        if has_processing:
            basis.append("processing or interpretation step is described")
        if has_result:
            basis.append("result or output side is visible")
        if has_flow:
            basis.append("the sentence keeps the flow rather than a single token")
        return {
            "has_input": has_input,
            "has_processing": has_processing,
            "has_result": has_result,
            "has_flow": has_flow,
            "signal_count": sum((has_input, has_processing, has_result)),
            "basis": basis,
        }

    def _transition_over_surface_pattern(self, linked_text: str) -> dict[str, object]:
        transition_tokens = (
            "전환",
            "이동",
            "넘어",
            "건너",
            "바뀌",
            "올라",
            "shift",
            "transition",
            "cross",
            "move across",
            "handoff",
        )
        boundary_tokens = (
            "표면",
            "경계",
            "레이어",
            "층위",
            "interface",
            "api",
            "surface",
            "layer",
            "boundary",
            "runtime",
        )
        bridge_patterns = (
            "에서",
            "으로",
            "에서 ",
            "으로 ",
            "from ",
            "to ",
        )
        has_transition = any(token in linked_text for token in transition_tokens)
        has_boundary = any(token in linked_text for token in boundary_tokens)
        has_bridge_pattern = any(token in linked_text for token in bridge_patterns)
        has_boundary_bridge = has_transition and has_boundary and has_bridge_pattern
        basis = []
        if has_transition:
            basis.append("movement or transition is explicitly described")
        if has_boundary:
            basis.append("surface, layer, runtime, or boundary is named")
        if has_bridge_pattern:
            basis.append("the sentence carries an across-from-to structure")
        if has_boundary_bridge:
            basis.append("both sides of the transition are visible together")
        return {
            "has_transition": has_transition,
            "has_boundary": has_boundary,
            "has_bridge_pattern": has_bridge_pattern,
            "has_boundary_bridge": has_boundary_bridge,
            "signal_count": sum((has_transition, has_boundary)),
            "basis": basis,
        }

    def _join_pattern_basis(self, pattern: dict[str, object]) -> str:
        basis = list(pattern.get("basis", []))
        if not basis:
            return "no clear semantic pattern survived"
        return "; ".join(basis[:3])

    def _lens_basis_note(self, line: LineDefinition) -> str:
        if line.is_primary:
            return f"primary stable/thick lens; operating_state={line.operating_state}"
        return (
            f"lens status={line.status} thickness={line.thickness_level}; "
            f"operating_state={line.operating_state}"
        )

    def _keywords_for_line(self, line_id: str, line_name: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
        if line_id in _PRIMARY_LENS_KEYWORDS:
            config = _PRIMARY_LENS_KEYWORDS[line_id]
            return config["strong"], config["partial"]
        if line_id in _KNOWN_LINE_KEYWORDS:
            return _KNOWN_LINE_KEYWORDS[line_id], ()
        normalized_name = line_name.replace("_", " ").lower().strip()
        name_parts = tuple(part for part in normalized_name.split() if part)
        fallback = tuple(dict.fromkeys((line_name.lower(), normalized_name, *name_parts)))
        return fallback, ()
