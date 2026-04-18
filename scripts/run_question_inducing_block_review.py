#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.run_dialogue_asset_probe import (
    CONVERSATIONAL_FILLER_RESIDUE,
    DISCOURSE_CONNECTIVE_RESIDUE,
    GENERIC_ABSTRACTION_RESIDUE,
    QUASI_TOPIC_RESIDUE,
    SPEAKER_RESIDUE,
)
OUTPUT_DIR = REPO_ROOT / "app" / "work" / "dialogue_loop_test" / "generated"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def _residue_type(value: str) -> str | None:
    lowered = value.lower()
    if value in DISCOURSE_CONNECTIVE_RESIDUE or lowered in {x.lower() for x in DISCOURSE_CONNECTIVE_RESIDUE}:
        return "discourse_connective_residue"
    if value in SPEAKER_RESIDUE or lowered in {x.lower() for x in SPEAKER_RESIDUE}:
        return "speaker_or_source_residue"
    if value in CONVERSATIONAL_FILLER_RESIDUE or lowered in {x.lower() for x in CONVERSATIONAL_FILLER_RESIDUE}:
        return "conversational_filler_residue"
    if value in GENERIC_ABSTRACTION_RESIDUE or lowered in {x.lower() for x in GENERIC_ABSTRACTION_RESIDUE}:
        return "generic_abstraction_residue"
    if value in QUASI_TOPIC_RESIDUE or lowered in {x.lower() for x in QUASI_TOPIC_RESIDUE}:
        return "quasi_topic_residue"
    return None


def _load_json(path: Path) -> Dict:
    return json.loads(path.read_text())


def _candidate_key(row: Dict) -> str:
    headings = "|".join(row.get("headings", [])[:3])
    return f"{row['window_id']}::{headings}"


def _next_questions(objects: List[str]) -> List[str]:
    prompts: List[str] = []
    objset = set(objects)
    if {"전략/방향성", "에이전트 애플리케이션"} <= objset:
        prompts.append("기존 앱의 moat는 agent interface 시대에 무엇으로 남는가?")
    if {"모델 work", "AI의 미래"} <= objset:
        prompts.append("모델 경쟁의 승부처는 pre-train 이후 어떤 평가/환경 축으로 이동하는가?")
    if {"일의 미래", "생산성/코딩"} <= objset:
        prompts.append("사람의 일은 수행에서 감독과 설계 쪽으로 얼마나 이동하는가?")
    if {"구현/자동화", "에이전트 애플리케이션"} <= objset:
        prompts.append("agent layer는 실제 workflow와 운영 구조를 어디까지 대체하는가?")
    if not prompts:
        prompts.append("이 블록은 다음 탐색 질문을 어떤 방향으로 여는가?")
    return prompts[:2]


def _candidate_reason(row: Dict) -> str:
    objects = [item["object"] for item in row.get("object_candidates", [])[:4]]
    relations = row.get("relation_hints", [])
    reasons: List[str] = []
    if len(objects) >= 2:
        reasons.append(f"객체가 함께 살아남음: {', '.join(objects[:3])}")
    if "question_generation_hint" in relations:
        reasons.append("질문 생성 힌트가 직접 동반됨")
    if "transition_hint" in relations or "execution_shift_hint" in relations:
        reasons.append("설명에서 전략/실행 쪽으로 이동하는 전이가 보임")
    return " / ".join(reasons)


def _build_anchor_surfaces(row: Dict) -> Dict[str, object]:
    values = [item["value"] for item in row.get("top_anchor_values", [])[:8]]
    deprioritized = []
    kept = []
    residue_counts: Counter[str] = Counter()
    for value in values:
        residue = _residue_type(value)
        if residue:
            deprioritized.append(value)
            residue_counts[residue] += 1
        else:
            kept.append(value)
    return {
        "before_anchor_surface": ", ".join(values[:6]),
        "after_anchor_surface": ", ".join(kept[:6]) if kept else "",
        "deprioritized_values": deprioritized,
        "residue_types": dict(residue_counts),
    }


def _candidate_status(row: Dict[str, object]) -> Dict[str, object]:
    return {
        "second_order_reading_type": "question_inducing_block",
        "rereading_mode": "high_score_window_rereading",
        "scope_local_page_comparison": "local_plus_page",
        "domain_specific_suspicion": "high_ai_agent_transition" if "에이전트 애플리케이션" in row.get("objects", []) else "medium",
        "reusable_attitude_hint": "question_opening_plus_transition_detection",
        "candidate_status": "hold_candidate",
        "hold_reason": "question-inducing reading is clear but still domain-skewed toward AI/agent/business transition",
        "evidence_pointers": [block.get("heading", "") for block in row.get("sample_blocks", [])],
    }


def _select_candidates(probes: List[Dict]) -> List[Dict[str, object]]:
    grouped: Dict[str, Dict[str, object]] = {}
    repeats: Counter[str] = Counter()
    for probe in probes:
        for row in probe.get("top_question_intent_windows", []):
            objects = row.get("object_candidates", [])
            relations = set(row.get("relation_hints", []))
            if row.get("question_intent_score", 0) < 8:
                continue
            if len(objects) < 2:
                continue
            if "question_generation_hint" not in relations:
                continue
            if not ({"transition_hint", "execution_shift_hint"} & relations):
                continue
            key = _candidate_key(row)
            repeats[key] += 1
            if key not in grouped or row["question_intent_score"] > grouped[key]["question_intent_score"]:
                grouped[key] = row
    ranked = sorted(grouped.values(), key=lambda r: (r["question_intent_score"], len(r.get("object_candidates", []))), reverse=True)
    output: List[Dict[str, object]] = []
    for row in ranked[:8]:
        objects = [item["object"] for item in row.get("object_candidates", [])[:4]]
        layers = [item["layer"] for item in row.get("layer_hints", [])[:4]]
        anchor_view = _build_anchor_surfaces(row)
        output.append(
            {
                "window_id": row["window_id"],
                "question_intent_score": row["question_intent_score"],
                "objects": objects,
                "layers": layers,
                "relation_hints": row.get("relation_hints", []),
                "why_candidate": _candidate_reason(row),
                "next_questions": _next_questions(objects),
                "existing_opening_summary": row.get("opening_summary", ""),
                "before_anchor_surface": anchor_view["before_anchor_surface"],
                "after_anchor_surface": anchor_view["after_anchor_surface"],
                "deprioritized_values": anchor_view["deprioritized_values"],
                "residue_types": anchor_view["residue_types"],
                "headings": row.get("headings", []),
                "sample_blocks": row.get("sample_blocks", [])[:2],
                **_candidate_status(
                    {
                        "objects": objects,
                        "sample_blocks": row.get("sample_blocks", [])[:2],
                    }
                ),
            }
        )
    return output


def _summarize_deprioritization(candidates: List[Dict[str, object]]) -> List[Dict[str, object]]:
    value_counter: Counter[str] = Counter()
    type_counter: Counter[str] = Counter()
    examples: Dict[str, List[str]] = defaultdict(list)
    for row in candidates:
        for value in row.get("deprioritized_values", []):
            value_counter[value] += 1
            residue = _residue_type(value)
            if residue:
                type_counter[residue] += 1
                if value not in examples[residue]:
                    examples[residue].append(value)
    output = []
    for residue, count in type_counter.most_common():
        output.append(
            {
                "residue_type": residue,
                "count": count,
                "example_values": examples[residue][:5],
                "why_not_hard_suppress": "문서 전체의 의미를 없애려는 것이 아니라 opening summary 선두에서만 뒤로 밀기 위한 후보이기 때문",
                "why_summary_stage_only": "질문 유도 블록의 핵심 객체와 relation movement는 유지한 채, surface opening만 더 선명하게 하기 위함",
            }
        )
    return output


def _compose_report(input_asset: str, probes: List[str], candidates: List[Dict[str, object]], deprioritization: List[Dict[str, object]]) -> str:
    lines: List[str] = []
    lines.append("[[A]] [[OBJ:question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1]] [[SEM:bounded_refinement_for_question_inducing_dialogue_blocks_and_summary_priority_shift]]")
    lines.append("")
    lines.append("# question-inducing block promotion and summary-stage deprioritization review v1")
    lines.append("")
    lines.append("## 1. input")
    lines.append("")
    lines.append(f"- input_asset: `{input_asset}`")
    lines.append("- probe_files:")
    for probe in probes:
        lines.append(f"  - `{probe}`")
    lines.append("")
    lines.append("## 2. top-level verdict")
    lines.append("")
    if candidates:
        lines.append("- status: `PASS_WITH_NOTE`")
        lines.append("- one-line verdict: 질문 유도 block candidate는 선명하게 보였고 summary-stage 후순위화 후보도 정리됐지만, 이 단계는 여전히 local bounded refinement이며 hard suppression이나 일반화 잠금 단계는 아니다.")
    else:
        lines.append("- status: `HOLD`")
        lines.append("- one-line verdict: high-score window는 있으나 질문 유도 block candidate 경계가 충분히 선명하지 않다.")
    lines.append("")
    lines.append("## 3. question-inducing block candidates")
    lines.append("")
    for row in candidates:
        lines.append(f"- window `{row['window_id']}` (`score={row['question_intent_score']}`)")
        lines.append(f"  - objects: {', '.join(row['objects'])}")
        lines.append(f"  - layers: {', '.join(row['layers'])}")
        lines.append(f"  - relation_hints: {', '.join(row['relation_hints'])}")
        lines.append(f"  - why: {row['why_candidate']}")
        for question in row["next_questions"]:
            lines.append(f"  - next_question: {question}")
        for block in row["sample_blocks"]:
            lines.append(f"  - block: `{block['heading']}`")
    lines.append("")
    lines.append("## 4. why these are not just high-score summary blocks")
    lines.append("")
    lines.append("- 이 블록들은 객체가 2개 이상 같이 살아남고, 질문 생성 힌트와 전이/실행 이동 힌트를 같이 갖는다.")
    lines.append("- 따라서 단순 요약 density가 아니라 다음 탐색을 여는 응축핵 후보로 읽을 수 있다.")
    lines.append("- 특히 `Bundle-Unbundle`, `기존 사업자의 UX 마찰`, `적응 경쟁`, `RLVR/CUA` 계열은 미래 담론을 전략/실행/검증 질문으로 끌어내린다.")
    lines.append("")
    lines.append("## 5. summary-stage deprioritization candidates")
    lines.append("")
    for row in deprioritization:
        lines.append(f"- `{row['residue_type']}`")
        lines.append(f"  - example_values: {', '.join(row['example_values'])}")
        lines.append(f"  - why_not_hard_suppress: {row['why_not_hard_suppress']}")
        lines.append(f"  - why_summary_stage_only: {row['why_summary_stage_only']}")
    lines.append("")
    lines.append("## 6. before / after reading")
    lines.append("")
    for row in candidates[:4]:
        lines.append(f"- window `{row['window_id']}`")
        lines.append(f"  - existing_opening_summary: {row['existing_opening_summary']}")
        lines.append(f"  - anchor_surface_before: {row['before_anchor_surface']}")
        lines.append(f"  - anchor_surface_after: {row['after_anchor_surface']}")
        lines.append(f"  - deprioritized_values: {', '.join(row['deprioritized_values']) if row['deprioritized_values'] else '(none)'}")
    lines.append("")
    lines.append("## 7. current interpretation")
    lines.append("")
    lines.append("- 지금 필요한 건 residue 삭제가 아니라 summary 선두 우선순위 재배치다.")
    lines.append("- 앞으로 올릴 것은 객체 후보, 질문 유도 block, 전략/실행/전이/질문 생성 힌트다.")
    lines.append("- 뒤로 미룰 것은 connective, filler, 화자 반복 흔적, 너무 일반적인 추상어다.")
    lines.append("")
    lines.append("## 8. next bounded step")
    lines.append("")
    lines.append("- summary generation 단계에서만 residue-aware deprioritization을 시험하는 얇은 patch를 검토한다.")
    lines.append("- broad concept probe 안정성은 유지한 채 dialogue 자산에만 국한된 surface adjustment로 제한한다.")
    lines.append("- question-inducing block candidate를 page seed / object growth seed 후보로 다루는 로컬 실험을 이어갈 수 있다.")
    lines.append("")
    lines.append("## 9. one-line summary")
    lines.append("")
    lines.append("> `youtube_03_22.md`에서는 단순 high-score window가 아니라 다음 질문을 여는 question-inducing block candidate가 실제로 보였고, residue 문제는 삭제보다 summary-stage 후순위화로 다루는 것이 맞다는 점이 bounded하게 정리됐다.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Review question-inducing dialogue blocks and summary-stage deprioritization candidates.")
    parser.add_argument("--input-asset", required=True)
    parser.add_argument("--probe", action="append", required=True)
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--json-out")
    args = parser.parse_args()

    probe_paths = [Path(p).resolve() for p in args.probe]
    probes = [_load_json(path) for path in probe_paths]

    candidates = _select_candidates(probes)
    deprioritization = _summarize_deprioritization(candidates)

    payload = {
        "created_at": _now_iso(),
        "input_asset": _relative(Path(args.input_asset).resolve()),
        "probe_files": [_relative(path) for path in probe_paths],
        "collection_context": {
            "input_asset_type": "high_density_dialogue",
            "source_asset_ref": _relative(Path(args.input_asset).resolve()),
            "supporting_first_pass_patterns": [
                "top_question_intent_windows",
                "object_candidates",
                "layer_hints",
                "relation_hints",
                "top_anchor_values",
            ],
            "second_order_reading_type": "question_inducing_block_review",
            "rereading_mode": "cross_window_candidate_selection",
            "scope_local_page_comparison": "local_plus_page",
            "domain_specific_suspicion": "high_ai_agent_product_transition",
            "reusable_attitude_hint": "question_opening_and_residue_deprioritization_collection",
            "candidate_status": "collect_only",
            "hold_reason": "question-inducing candidate rules are still being observed as patterns, not generalized",
            "evidence_pointers": [_relative(path) for path in probe_paths],
        },
        "question_inducing_candidates": candidates,
        "summary_stage_deprioritization_candidates": deprioritization,
    }

    report_text = _compose_report(payload["input_asset"], payload["probe_files"], candidates, deprioritization)
    report_path = Path(args.report_path).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text)

    json_out = Path(args.json_out).resolve() if args.json_out else OUTPUT_DIR / f"question_inducing_block_candidates_{_stamp()}.json"
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    print(_relative(report_path))
    print(_relative(json_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
