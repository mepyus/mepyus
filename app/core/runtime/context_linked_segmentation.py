from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


LinkageReason = Literal[
    "unfinished_claim",
    "answer_completion",
    "speaker_continuation",
    "setup_to_mechanism",
    "causal_chain",
    "contrast_pair",
]
LinkageConfidence = Literal["high", "medium", "low"]

_SETUP_PREFIXES = ("예를 들면", "예를 들자면", "즉", "왜냐하면")
_CONTRAST_PREFIXES = ("하지만", "반면", "그러나")
_CAUSAL_MARKERS = ("그래서", "때문에", "따라서", "결과적으로")
_CLAIM_ENDINGS = ("그리고", "또", "즉,", "왜냐하면", "때문에", "따라서")
_ANSWER_META_PREFIXES = ("다음", "이후", "별도", "운영", "메타")
_STAGE_HANDOFF_PREFIXES = ("이후", "다음 단계", "별도", "다른 단계", "넘긴다")
# Spec reference:
# docs/specs/context_linked_segmentation_reason_priority_spec_v0.md
REASON_PRIORITY: dict[LinkageReason, int] = {
    "contrast_pair": 0,
    "causal_chain": 1,
    "speaker_continuation": 2,
    "answer_completion": 3,
    "setup_to_mechanism": 4,
    "unfinished_claim": 5,
}


@dataclass(frozen=True)
class Segment:
    segment_id: str
    source_id: str
    text: str
    order_index: int
    start_anchor: Any
    end_anchor: Any
    provenance: Any
    speaker_id: str | None = None
    segment_type: str | None = None


@dataclass(frozen=True)
class LinkedSegment:
    linked_segment_id: str
    source_id: str
    segment_ids: list[str]
    linked_text: str
    linkage_reason: LinkageReason
    linkage_confidence: LinkageConfidence
    provenance: Any


class ContextLinkedSegmenter:
    def __init__(self, adjacency_window: int = 2) -> None:
        # TBD: adjacency window size is contract-fixed only as an initial default.
        self.adjacency_window = adjacency_window

    def link(self, segments: list[Segment]) -> list[LinkedSegment]:
        if not segments:
            return []

        ordered = sorted(segments, key=lambda item: (item.source_id, item.order_index))
        linked_segments: list[LinkedSegment] = []
        consumed_ids: set[str] = set()

        for source_segments in self._group_by_source(ordered):
            source_linked = self._link_source_segments(source_segments)
            linked_segments.extend(source_linked)
            for linked in source_linked:
                consumed_ids.update(linked.segment_ids)
            for segment in source_segments:
                if segment.segment_id not in consumed_ids:
                    singleton = self._build_linked_segment([segment], None, "low")
                    linked_segments.append(singleton)
                    consumed_ids.add(segment.segment_id)
        return linked_segments

    def _link_source_segments(self, segments: list[Segment]) -> list[LinkedSegment]:
        linked_segments: list[LinkedSegment] = []
        active_group: list[Segment] = []
        active_reason: LinkageReason | None = None
        active_confidence: LinkageConfidence = "low"
        active_pair_count = 0

        for index in range(1, len(segments)):
            previous = segments[index - 1]
            current = segments[index]
            candidates = self._detect_reasons(previous, current)
            selected = self._select_reason(candidates)
            next_segment_text = segments[index + 1].text if index + 1 < len(segments) else ""

            if selected is None:
                if active_group:
                    linked_segments.append(
                        self._build_linked_segment(active_group, active_reason, active_confidence)
                    )
                    active_group = []
                    active_reason = None
                    active_confidence = "low"
                    active_pair_count = 0
                continue

            reason, confidence = selected
            current_pair_text = f"{previous.text.strip()}\n{current.text.strip()}"
            if self._should_terminate_pair(reason, current_pair_text, next_segment_text):
                if active_group:
                    linked_segments.append(
                        self._build_linked_segment(active_group, active_reason, active_confidence)
                    )
                    active_group = []
                    active_reason = None
                    active_confidence = "low"
                    active_pair_count = 0
                continue

            if not active_group:
                active_group = [previous, current]
                active_reason = reason
                active_confidence = confidence
                active_pair_count = 1
                continue

            if self._should_reset_chain(active_reason, reason, active_pair_count):
                linked_segments.append(
                    self._build_linked_segment(active_group, active_reason, active_confidence)
                )
                active_group = [previous, current]
                active_reason = reason
                active_confidence = confidence
                active_pair_count = 1
                continue

            if active_group[-1].segment_id == previous.segment_id:
                active_group.append(current)
                active_pair_count += 1
                continue

            linked_segments.append(
                self._build_linked_segment(active_group, active_reason, active_confidence)
            )
            active_group = [previous, current]
            active_reason = reason
            active_confidence = confidence
            active_pair_count = 1

        if active_group:
            linked_segments.append(
                self._build_linked_segment(active_group, active_reason, active_confidence)
            )
        return linked_segments

    def _detect_reasons(
        self, previous: Segment, current: Segment
    ) -> list[tuple[LinkageReason, LinkageConfidence]]:
        distance = current.order_index - previous.order_index
        if distance <= 0 or distance > self.adjacency_window:
            return []

        previous_text = previous.text.strip()
        current_text = current.text.strip()
        if not previous_text or not current_text:
            return []

        confidence: LinkageConfidence = "high" if distance == 1 else "medium"
        current_lower = current_text.lower()
        previous_lower = previous_text.lower()
        candidates: list[tuple[LinkageReason, LinkageConfidence]] = []

        if self._looks_like_unfinished_claim(previous_text):
            candidates.append(("unfinished_claim", confidence))
        if previous_text.endswith("?") and self._looks_like_answer(current_text):
            candidates.append(("answer_completion", confidence))
        if previous.speaker_id and previous.speaker_id == current.speaker_id:
            candidates.append(("speaker_continuation", confidence))
        if current_text.startswith(_SETUP_PREFIXES):
            candidates.append(("setup_to_mechanism", confidence))
        if current_text.startswith(_CONTRAST_PREFIXES):
            candidates.append(("contrast_pair", confidence))
        if self._contains_any(previous_lower, _CAUSAL_MARKERS) or self._contains_any(
            current_lower, _CAUSAL_MARKERS
        ):
            candidates.append(("causal_chain", confidence))
        return candidates

    def _select_reason(
        self, candidates: list[tuple[LinkageReason, LinkageConfidence]]
    ) -> tuple[LinkageReason, LinkageConfidence] | None:
        if not candidates:
            return None
        return min(candidates, key=lambda item: REASON_PRIORITY[item[0]])

    def _should_reset_chain(
        self,
        active_reason: LinkageReason | None,
        next_reason: LinkageReason,
        active_pair_count: int,
    ) -> bool:
        if active_reason is None:
            return False
        if active_reason in {"answer_completion", "contrast_pair"} and active_pair_count >= 1:
            return True
        if active_reason == "unfinished_claim" and next_reason in {"contrast_pair", "causal_chain"}:
            return True
        if active_reason == "setup_to_mechanism" and next_reason in {"contrast_pair", "causal_chain"}:
            return True
        if active_reason == "speaker_continuation" and next_reason in {"contrast_pair", "causal_chain"}:
            return True
        if active_reason != next_reason and REASON_PRIORITY[next_reason] < REASON_PRIORITY[active_reason]:
            return True
        return False

    def _should_terminate_pair(
        self, reason: str, current_pair_text: str, next_segment_text: str
    ) -> bool:
        current_text = current_pair_text.strip()
        pair_lines = [line.strip() for line in current_text.splitlines() if line.strip()]
        current_segment_text = pair_lines[-1] if pair_lines else current_text
        next_text = next_segment_text.strip()

        if reason == "answer_completion":
            if self._is_direct_answer_continuation(current_text) and not self._looks_like_stage_handoff(
                current_segment_text
            ):
                return False
            if self._is_closed_sentence(current_segment_text) and not self._looks_like_direct_answer_extension(
                current_segment_text
            ):
                return True
            if next_text and not self._looks_like_direct_answer_extension(next_text):
                return True
            return False

        if reason == "causal_chain":
            if self._has_causal_marker(current_text) and not self._looks_like_stage_handoff(
                current_segment_text
            ):
                return False
            if self._looks_like_stage_handoff(current_segment_text):
                return True
            if not next_text:
                return False
            if not self._has_causal_marker(next_text):
                return True
            return False

        return False

    @staticmethod
    def _group_by_source(segments: list[Segment]) -> list[list[Segment]]:
        grouped: list[list[Segment]] = []
        current_group: list[Segment] = []
        current_source_id: str | None = None
        for segment in segments:
            if current_source_id != segment.source_id:
                if current_group:
                    grouped.append(current_group)
                current_group = [segment]
                current_source_id = segment.source_id
                continue
            current_group.append(segment)
        if current_group:
            grouped.append(current_group)
        return grouped

    def _build_linked_segment(
        self,
        segments: list[Segment],
        reason: LinkageReason | None,
        confidence: LinkageConfidence,
    ) -> LinkedSegment:
        first = segments[0]
        last = segments[-1]
        linked_reason: LinkageReason = reason or "unfinished_claim"
        linked_confidence: LinkageConfidence = confidence if reason is not None else "low"
        linked_text = " ".join(segment.text.strip() for segment in segments if segment.text.strip())
        provenance = {
            "kind": "context_linked_segmentation_v0",
            "source_id": first.source_id,
            "segment_count": len(segments),
            "input_segment_ids": [segment.segment_id for segment in segments],
            "linkage_reason": linked_reason,
        }
        return LinkedSegment(
            linked_segment_id=f"{first.source_id}:{first.order_index}-{last.order_index}",
            source_id=first.source_id,
            segment_ids=[segment.segment_id for segment in segments],
            linked_text=linked_text,
            linkage_reason=linked_reason,
            linkage_confidence=linked_confidence,
            provenance=provenance,
        )

    @staticmethod
    def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
        return any(marker in text for marker in markers)

    @staticmethod
    def _looks_like_unfinished_claim(text: str) -> bool:
        stripped = text.strip()
        if stripped.endswith((":", ";", ",")):
            return True
        return stripped.endswith(_CLAIM_ENDINGS)

    @staticmethod
    def _looks_like_answer(text: str) -> bool:
        stripped = text.strip()
        if not stripped:
            return False
        if stripped.startswith(("네", "아니요", "그것은", "이는", "이것은")):
            return True
        return not stripped.endswith("?")

    @staticmethod
    def _is_closed_sentence(text: str) -> bool:
        return text.strip().endswith((".", "?", "!"))

    @staticmethod
    def _looks_like_direct_answer_extension(text: str) -> bool:
        stripped = text.strip()
        if not stripped:
            return False
        if stripped.startswith(_ANSWER_META_PREFIXES):
            return False
        if "?" in stripped:
            return False
        if stripped.startswith(("네", "아니요", "그것은", "이는", "이것은")):
            return True
        return "때문" in stripped or "이다" in stripped or "합니다" in stripped

    @staticmethod
    def _looks_like_stage_handoff(text: str) -> bool:
        stripped = text.strip()
        if not stripped:
            return False
        return stripped.startswith(_STAGE_HANDOFF_PREFIXES) or "단계" in stripped

    @staticmethod
    def _has_causal_marker(text: str) -> bool:
        return ContextLinkedSegmenter._contains_any(text.lower(), _CAUSAL_MARKERS)

    @staticmethod
    def _is_direct_answer_continuation(text: str) -> bool:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if len(lines) < 2:
            return False
        question_text = lines[0]
        answer_text = lines[-1]
        if "?" not in question_text:
            return False
        if ContextLinkedSegmenter._looks_like_stage_handoff(answer_text):
            return False
        if answer_text.startswith(_ANSWER_META_PREFIXES):
            return False
        return ContextLinkedSegmenter._is_closed_sentence(
            answer_text
        ) and ContextLinkedSegmenter._looks_like_direct_answer_extension(answer_text)
