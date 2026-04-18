#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.context_linked_segmentation import ContextLinkedSegmenter, Segment


@dataclass(frozen=True)
class ExpectedLink:
    segment_ids: tuple[str, str]
    linkage_reason: str


@dataclass(frozen=True)
class FixtureCase:
    fixture_name: str
    fixture_type: str
    design_intent: str
    segments: list[Segment]
    expected_links: list[ExpectedLink]


def _segment(
    fixture_name: str,
    segment_id: str,
    order_index: int,
    text: str,
    speaker_id: str | None = None,
) -> Segment:
    return Segment(
        segment_id=segment_id,
        source_id=fixture_name,
        text=text,
        order_index=order_index,
        start_anchor={"index": order_index, "offset": 0},
        end_anchor={"index": order_index, "offset": len(text)},
        provenance={"fixture": fixture_name},
        speaker_id=speaker_id,
    )


def _fixtures() -> list[FixtureCase]:
    return [
        FixtureCase(
            fixture_name="dialogue_continuation",
            fixture_type="대화형",
            design_intent="같은 화자 연속 발화에서 speaker_continuation이 살아나는지 확인",
            segments=[
                _segment("dialogue_continuation", "dlg_001", 0, "우리는 먼저 입력을 다시 읽어야 합니다.", "speaker_a"),
                _segment("dialogue_continuation", "dlg_002", 1, "그렇지 않으면 얇은 조각만 남습니다.", "speaker_a"),
                _segment("dialogue_continuation", "dlg_003", 2, "그 다음에는 어떻게 합니까?", "speaker_b"),
                _segment("dialogue_continuation", "dlg_004", 3, "다음 화자에서는 별도 연결이 없어야 합니다.", "speaker_c"),
            ],
            expected_links=[
                ExpectedLink(("dlg_001", "dlg_002"), "speaker_continuation"),
            ],
        ),
        FixtureCase(
            fixture_name="explanatory_mechanism",
            fixture_type="설명형",
            design_intent="setup_to_mechanism과 causal_chain이 설명 문서에서 붙는지 확인",
            segments=[
                _segment("explanatory_mechanism", "exp_001", 0, "이 장치는 먼저 입력의 배경을 정리한다."),
                _segment("explanatory_mechanism", "exp_002", 1, "예를 들면 약한 조각을 앞뒤 문맥으로 다시 잇는다."),
                _segment("explanatory_mechanism", "exp_003", 2, "그래서 독립적으로는 약하던 단서가 다시 살아난다."),
                _segment("explanatory_mechanism", "exp_004", 3, "이후에는 다른 단계로 넘긴다."),
            ],
            expected_links=[
                ExpectedLink(("exp_001", "exp_002"), "setup_to_mechanism"),
                ExpectedLink(("exp_002", "exp_003"), "causal_chain"),
            ],
        ),
        FixtureCase(
            fixture_name="argument_contrast",
            fixture_type="논증형",
            design_intent="unfinished_claim과 contrast_pair가 논증 문서에서 붙는지 확인",
            segments=[
                _segment("argument_contrast", "arg_001", 0, "문서를 하나의 verdict로 닫으면,"),
                _segment("argument_contrast", "arg_002", 1, "문서 내부 variation이 눌린다."),
                _segment("argument_contrast", "arg_003", 2, "하지만 여러 line lens를 열면 다른 결과가 나온다."),
                _segment("argument_contrast", "arg_004", 3, "그 차이가 이후 reread의 출발점이 된다."),
            ],
            expected_links=[
                ExpectedLink(("arg_001", "arg_002"), "unfinished_claim"),
                ExpectedLink(("arg_002", "arg_003"), "contrast_pair"),
            ],
        ),
        FixtureCase(
            fixture_name="mixed_document",
            fixture_type="혼합형",
            design_intent="answer_completion, causal_chain, contrast_pair가 섞일 때 누락과 오탐을 함께 관찰",
            segments=[
                _segment("mixed_document", "mix_001", 0, "왜 context-linked segmentation이 필요한가?"),
                _segment("mixed_document", "mix_002", 1, "혼자 두면 약한 조각이 문맥을 잃기 때문이다."),
                _segment("mixed_document", "mix_003", 2, "따라서 같은 문서 안에서도 여러 결이 다시 열린다."),
                _segment("mixed_document", "mix_004", 3, "그러나 모든 조각을 묶으면 과잉 읽기가 생긴다."),
                _segment("mixed_document", "mix_005", 4, "그래서 보수적으로 남겨야 하는 조각도 있다."),
            ],
            expected_links=[
                ExpectedLink(("mix_001", "mix_002"), "answer_completion"),
                ExpectedLink(("mix_002", "mix_003"), "causal_chain"),
                ExpectedLink(("mix_003", "mix_004"), "contrast_pair"),
                ExpectedLink(("mix_004", "mix_005"), "causal_chain"),
            ],
        ),
    ]


def _actual_links(linked_segments: list[dict[str, object]]) -> list[dict[str, object]]:
    actual: list[dict[str, object]] = []
    for linked in linked_segments:
        segment_ids = linked["segment_ids"]
        linkage_reason = linked["linkage_reason"]
        if not isinstance(segment_ids, list):
            continue
        for index in range(len(segment_ids) - 1):
            actual.append(
                {
                    "segment_ids": [segment_ids[index], segment_ids[index + 1]],
                    "linkage_reason": linkage_reason,
                }
            )
    return actual


def _normalize_pairs(items: list[dict[str, object]]) -> set[tuple[str, str, str]]:
    normalized: set[tuple[str, str, str]] = set()
    for item in items:
        segment_ids = item["segment_ids"]
        linkage_reason = item["linkage_reason"]
        if isinstance(segment_ids, list) and len(segment_ids) == 2 and isinstance(linkage_reason, str):
            normalized.add((segment_ids[0], segment_ids[1], linkage_reason))
    return normalized


def main() -> int:
    output_root = Path("/tmp/context_linked_segmentation_validation")
    output_root.mkdir(parents=True, exist_ok=True)

    segmenter = ContextLinkedSegmenter()
    fixtures = _fixtures()
    results: list[dict[str, object]] = []
    fixture_summaries: list[dict[str, object]] = []
    all_false_positives: list[dict[str, object]] = []
    all_misses: list[dict[str, object]] = []

    for fixture in fixtures:
        linked_segments = [asdict(item) for item in segmenter.link(fixture.segments)]
        actual = _actual_links(linked_segments)
        expected = [
            {"segment_ids": list(item.segment_ids), "linkage_reason": item.linkage_reason}
            for item in fixture.expected_links
        ]

        expected_set = _normalize_pairs(expected)
        actual_set = _normalize_pairs(actual)
        matched = expected_set & actual_set
        misses = expected_set - actual_set
        false_positives = actual_set - expected_set
        match_rate = len(matched) / len(expected_set) if expected_set else 1.0

        miss_records = [
            {
                "fixture_name": fixture.fixture_name,
                "segment_ids": [left, right],
                "linkage_reason": reason,
            }
            for left, right, reason in sorted(misses)
        ]
        false_positive_records = [
            {
                "fixture_name": fixture.fixture_name,
                "segment_ids": [left, right],
                "linkage_reason": reason,
            }
            for left, right, reason in sorted(false_positives)
        ]
        all_misses.extend(miss_records)
        all_false_positives.extend(false_positive_records)

        result = {
            "fixture_name": fixture.fixture_name,
            "fixture_type": fixture.fixture_type,
            "design_intent": fixture.design_intent,
            "expected": expected,
            "actual": actual,
            "match": [
                {"segment_ids": [left, right], "linkage_reason": reason}
                for left, right, reason in sorted(matched)
            ],
            "miss": miss_records,
            "false_positive": false_positive_records,
            "linked_segments": linked_segments,
            "match_rate": match_rate,
        }
        results.append(result)
        fixture_summaries.append(
            {
                "fixture_name": fixture.fixture_name,
                "fixture_type": fixture.fixture_type,
                "match_rate": match_rate,
                "miss_count": len(miss_records),
                "false_positive_count": len(false_positive_records),
            }
        )

    payload = {
        "fixture_summaries": fixture_summaries,
        "overall_false_positive": all_false_positives,
        "overall_miss": all_misses,
        "results": results,
    }
    output_path = output_root / "validation_result.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
