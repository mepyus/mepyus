#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

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


def _load_json(path: Path) -> Dict:
    return json.loads(path.read_text())


def _parse_window_id(window_id: str) -> Tuple[int, int]:
    try:
        start, end = window_id.split("_", 1)
        return int(start), int(end)
    except Exception:
        return (0, 0)


def _pass_a(purpose: Dict, question_review: Dict) -> Dict[str, object]:
    return {
        "name": "object_layer_relation_question_reading",
        "second_order_reading_type": "object_layer_relation_question",
        "rereading_mode": "same_asset_reinterpretation",
        "scope_local_page_comparison": "page",
        "front_objects": [row["object"] for row in purpose.get("top_objects", [])[:6]],
        "front_layers": [row["layer"] for row in purpose.get("top_layers", [])[:6]],
        "front_relations": [row["relation"] for row in purpose.get("top_relations", [])[:6]],
        "question_blocks": [row["window_id"] for row in question_review.get("question_inducing_candidates", [])[:6]],
        "residue_note": "residue exists but is not the front reading target in pass A",
        "what_looks_new": [
            "객체가 단순 키워드가 아니라 AI 시대의 주요 질문 묶음으로 보인다",
            "질문 유도 블록이 object growth와 함께 잡힌다",
        ],
    }


def _pass_b(question_review: Dict) -> Dict[str, object]:
    pivot_rows = question_review.get("question_inducing_candidates", [])
    pivot_windows = []
    pivot_objects: Counter[str] = Counter()
    pivot_relations: Counter[str] = Counter()
    headings = []
    for row in pivot_rows[:8]:
        pivot_windows.append(row["window_id"])
        for obj in row.get("objects", []):
            pivot_objects[obj] += 1
        for rel in row.get("relation_hints", []):
            pivot_relations[rel] += 1
        headings.extend(row.get("headings", [])[:2])
    return {
        "name": "page_flow_transition_pivot_reading",
        "second_order_reading_type": "page_flow_transition_pivot",
        "rereading_mode": "same_asset_reinterpretation",
        "scope_local_page_comparison": "page_plus_comparison",
        "pivot_windows": pivot_windows,
        "pivot_objects": [value for value, _ in pivot_objects.most_common(5)],
        "pivot_relations": [value for value, _ in pivot_relations.most_common(5)],
        "pivot_headings": headings[:8],
        "what_looks_new": [
            "같은 블록이 객체 후보가 아니라 페이지 흐름을 꺾는 pivot로 보인다",
            "Bundle-Unbundle, UX 마찰, RLVR/CUA 구간이 실행 질문을 발생시키는 전이점으로 보인다",
        ],
    }


def _pass_c(question_review: Dict) -> Dict[str, object]:
    deprioritized: Counter[str] = Counter()
    residue_types: Counter[str] = Counter()
    candidate_losses = []
    for row in question_review.get("question_inducing_candidates", [])[:8]:
        for value in row.get("deprioritized_values", []):
            deprioritized[value] += 1
        for key, count in row.get("residue_types", {}).items():
            residue_types[key] += count
        candidate_losses.append(
            {
                "window_id": row["window_id"],
                "before": row.get("before_anchor_surface", ""),
                "after": row.get("after_anchor_surface", ""),
                "deprioritized_values": row.get("deprioritized_values", []),
            }
        )
    return {
        "name": "summary_opening_residue_priority_reading",
        "second_order_reading_type": "summary_opening_residue_priority",
        "rereading_mode": "same_asset_reinterpretation",
        "scope_local_page_comparison": "summary_opening",
        "front_residue_types": [value for value, _ in residue_types.most_common(5)],
        "front_deprioritized_values": [value for value, _ in deprioritized.most_common(8)],
        "candidate_losses": candidate_losses[:4],
        "what_looks_new": [
            "같은 block이 요약 opening에서는 residue 때문에 덜 살아난다",
            "삭제가 아니라 summary-stage 우선순위 조정이 핵심이라는 점이 보인다",
        ],
    }


def _stitch_pointer_support(units: List[Dict[str, object]], purpose: Dict, question_review: Dict, mode: str) -> List[Dict[str, object]]:
    available = {row["window_id"] for row in question_review.get("question_inducing_candidates", [])}
    purpose_windows = purpose.get("top_windows", [])
    for unit in units:
        direct_refs = [w for w in unit["source_windows"] if w in available]
        unit["present_window_refs"] = direct_refs
        unit["pointer_support_source"] = "question_inducing_candidates" if direct_refs else "none"
        unit["grounding_status"] = "direct_grounded" if direct_refs else "empty_ref"
        unit["grounding_note"] = "question-inducing candidate와 직접 연결됨" if direct_refs else "질문 유도 candidate 직접 ref가 없음"
        unit["evidence_pointers"] = direct_refs[:]
        if direct_refs or mode == "none":
            continue

        scored = []
        center_objects = set(unit.get("center_objects", []))
        source_midpoints = []
        for ref in unit.get("source_windows", []):
            start, end = _parse_window_id(ref)
            source_midpoints.append((start + end) / 2.0)
        for row in purpose_windows:
            row_objects = set(row.get("objects", []))
            overlap = len(center_objects & row_objects)
            if overlap <= 0:
                continue
            start, end = _parse_window_id(row.get("window_id", "0_0"))
            midpoint = (start + end) / 2.0
            if source_midpoints:
                distance = min(abs(midpoint - source_mid) for source_mid in source_midpoints)
            else:
                distance = 10_000.0
            scored.append((overlap, -distance, row.get("question_intent_score", 0), row))
        scored.sort(key=lambda item: (item[0], item[1], item[2]), reverse=True)
        fallback_rows = [row for _, _, _, row in scored[:2]]
        if fallback_rows:
            unit["present_window_refs"] = [row["window_id"] for row in fallback_rows]
            unit["pointer_support_source"] = "purpose_top_windows"
            unit["grounding_status"] = "fallback_grounded"
            unit["grounding_note"] = "직접 candidate ref는 없지만 object-overlap 기반 fallback window로 grounding 보조"
            unit["evidence_pointers"] = [row["window_id"] for row in fallback_rows]
    return units


def _make_context_units(question_review: Dict, purpose: Dict, pointer_stabilization: str) -> List[Dict[str, object]]:
    units = [
        {
            "unit_id": "agent_interface_transition_unit",
            "candidate_status": "hold_candidate",
            "domain_specific_suspicion": "high_ai_agent_product_transition",
            "reusable_attitude_hint": "transition_plus_question_seed_pairing",
            "source_windows": ["75_80", "80_87", "84_91", "84_89"],
            "why_more_alive_than_paragraph": "OpenClaw, 앱 대체/대리 조작, bundle-unbundle가 따로가 아니라 하나의 앱 구조 재편 맥락으로 읽히기 때문",
            "center_objects": ["에이전트 애플리케이션", "전략/방향성", "구현/자동화"],
            "center_layers": ["구조/연결 층", "전략/방향 층", "질문 유도 층"],
            "relation_movement": ["transition_hint", "contrast_hint", "execution_shift_hint", "question_generation_hint"],
            "page_role": "pivot",
            "question_seed": [
                "기존 앱의 moat는 어디로 이동하는가?",
                "agent layer는 workflow의 기본 인터페이스가 되는가?",
            ],
            "residue_interference": ["speaker_or_source_residue", "discourse_connective_residue"],
        },
        {
            "unit_id": "future_of_work_supervisor_unit",
            "candidate_status": "hold_candidate",
            "domain_specific_suspicion": "medium_ai_future_of_work",
            "reusable_attitude_hint": "role_shift_plus_question_seed_pairing",
            "source_windows": ["20_27", "21_26"],
            "why_more_alive_than_paragraph": "GTC와 일의 미래, 생산성/코딩, 감독자형 노동이 하나의 역할 전환 맥락으로 묶이기 때문",
            "center_objects": ["일의 미래", "생산성/코딩", "에이전트 애플리케이션"],
            "center_layers": ["설명/해석 층", "전략/방향 층", "질문 유도 층"],
            "relation_movement": ["transition_hint", "execution_shift_hint", "question_generation_hint"],
            "page_role": "question_seed",
            "question_seed": [
                "사람의 일은 수행보다 감독과 설계로 이동하는가?",
                "생산성 도구 변화가 역할 구조를 어떻게 바꾸는가?",
            ],
            "residue_interference": ["discourse_connective_residue", "speaker_or_source_residue"],
        },
        {
            "unit_id": "model_eval_shift_unit",
            "candidate_status": "hold_candidate",
            "domain_specific_suspicion": "high_ai_model_eval_transition",
            "reusable_attitude_hint": "compression_plus_specification_shift_pairing",
            "source_windows": ["32_39"],
            "why_more_alive_than_paragraph": "AI 산업 스냅샷과 RLVR/CUA가 미래 담론을 평가/환경/검증 축으로 내리는 하나의 맥락이기 때문",
            "center_objects": ["AI의 미래", "모델 work", "에이전트 애플리케이션"],
            "center_layers": ["검증/근거 층", "구조/연결 층", "전략/방향 층"],
            "relation_movement": ["transition_hint", "execution_shift_hint", "specification_hint", "question_generation_hint"],
            "page_role": "compression_node",
            "question_seed": [
                "모델 경쟁의 승부처는 evaluation environment로 이동하는가?",
                "미래 담론은 어떤 검증 바닥 위에서만 의미를 갖는가?",
            ],
            "residue_interference": ["discourse_connective_residue", "conversational_filler_residue"],
        },
    ]
    return _stitch_pointer_support(units, purpose, question_review, pointer_stabilization)


def _compose_report(input_asset: str, pass_a: Dict, pass_b: Dict, pass_c: Dict, context_units: List[Dict[str, object]], references: Dict[str, str]) -> str:
    lines: List[str] = []
    lines.append("[[A]] [[OBJ:multi_pass_interpretation_and_context_unit_rereading_training_v1]] [[SEM:training_report_for_repeated_reinterpretation_and_context_unit_reconstruction]]")
    lines.append("")
    lines.append("# multi-pass interpretation and context-unit rereading training v1")
    lines.append("")
    lines.append("## 1. training purpose")
    lines.append("")
    lines.append(f"- input_asset: `{input_asset}`")
    lines.append("- 이번 훈련의 목적은 같은 자산을 여러 번 요약하는 것이 아니라, 다른 해석 레이어로 다시 읽고 그 차이로 더 살아 있는 맥락 단위를 다시 세우는 것이다.")
    lines.append("")
    lines.append("## 2. pass별 해석 차이")
    lines.append("")
    lines.append(f"- Pass A `{pass_a['name']}`")
    lines.append(f"  - front_objects: {', '.join(pass_a['front_objects'])}")
    lines.append(f"  - front_layers: {', '.join(pass_a['front_layers'])}")
    lines.append(f"  - what_changed: {' / '.join(pass_a['what_looks_new'])}")
    lines.append(f"- Pass B `{pass_b['name']}`")
    lines.append(f"  - pivot_windows: {', '.join(pass_b['pivot_windows'][:6])}")
    lines.append(f"  - pivot_relations: {', '.join(pass_b['pivot_relations'])}")
    lines.append(f"  - what_changed: {' / '.join(pass_b['what_looks_new'])}")
    lines.append(f"- Pass C `{pass_c['name']}`")
    lines.append(f"  - front_residue_types: {', '.join(pass_c['front_residue_types'])}")
    lines.append(f"  - front_deprioritized_values: {', '.join(pass_c['front_deprioritized_values'][:6])}")
    lines.append(f"  - what_changed: {' / '.join(pass_c['what_looks_new'])}")
    lines.append("")
    lines.append("## 3. 반복 판독으로 더 선명해진 객체")
    lines.append("")
    lines.append("- `에이전트 애플리케이션`")
    lines.append("  - Pass A에서는 주요 객체였다.")
    lines.append("  - Pass B에서는 앱 구조 재편과 workflow 전환을 일으키는 pivot 중심 객체로 바뀌어 보였다.")
    lines.append("  - Pass C에서는 opening summary에서 residue 때문에 덜 살아나는 희생자이기도 하다는 점이 보였다.")
    lines.append("- `일의 미래`")
    lines.append("  - 미래 담론의 부속 객체가 아니라 감독자형 노동과 역할 재배치를 여는 객체로 더 두꺼워졌다.")
    lines.append("- `모델 work`")
    lines.append("  - 단순 모델 담론이 아니라 RLVR/CUA, evaluation, 환경 이동과 연결된 검증 바닥 객체로 더 선명해졌다.")
    lines.append("")
    lines.append("## 4. 새로 세운 context unit")
    lines.append("")
    for unit in context_units:
        lines.append(f"- `{unit['unit_id']}`")
        lines.append(f"  - present_window_refs: {', '.join(unit['present_window_refs'])}")
        lines.append(f"  - grounding_status: {unit['grounding_status']}")
        lines.append(f"  - pointer_support_source: {unit['pointer_support_source']}")
        lines.append(f"  - grounding_note: {unit['grounding_note']}")
        lines.append(f"  - evidence_pointers: {', '.join(unit['evidence_pointers'])}")
        lines.append(f"  - why_more_alive_than_paragraph: {unit['why_more_alive_than_paragraph']}")
        lines.append(f"  - center_objects: {', '.join(unit['center_objects'])}")
        lines.append(f"  - center_layers: {', '.join(unit['center_layers'])}")
        lines.append(f"  - relation_movement: {', '.join(unit['relation_movement'])}")
        lines.append(f"  - page_role: {unit['page_role']}")
        lines.append(f"  - question_seed: {' / '.join(unit['question_seed'])}")
    lines.append("")
    lines.append("## 5. 템플릿 기준 재해석")
    lines.append("")
    lines.append("- 객체")
    lines.append("  - 맥락 단위는 기존 객체를 더 두껍게 만들었고, 특히 agent app / 미래의 일 / 모델 검증 축을 다시 보강했다.")
    lines.append("- 층위")
    lines.append("  - 설명층만 남지 않고 구조/전략/질문 유도/검증 층이 context unit마다 다르게 전면화됐다.")
    lines.append("- 관계 운동")
    lines.append("  - transition, execution shift, question generation이 문단보다 context unit 수준에서 더 설득력 있게 읽혔다.")
    lines.append("- 전체 흐름 속 역할")
    lines.append("  - 일부 단위는 pivot, 일부는 question seed, 일부는 compression node로 다시 보였다.")
    lines.append("- residue 간섭")
    lines.append("  - residue는 문서 전체가 아니라 summary opening과 anchor 선두 경쟁에서 문제를 일으킨다는 점이 더 분명해졌다.")
    lines.append("")
    lines.append("## 6. 학습 포인트")
    lines.append("")
    lines.append("- 같은 자산도 해석 레이어를 바꾸면 완전히 다른 역할이 보인다.")
    lines.append("- 중요한 것은 정보량보다 전이와 역할일 수 있다.")
    lines.append("- 문단은 고정 단위가 아니라 재구성 가능한 context unit일 수 있다.")
    lines.append("- 템플릿은 채우는 양식이 아니라 읽기 장치로 작동할 수 있다.")
    lines.append("- 좋은 결과는 정답 문장을 뽑는 것이 아니라, 무엇이 새로 보였는지 기록하는 것이다.")
    lines.append("")
    lines.append("## 7. 한 줄 판정")
    lines.append("")
    lines.append("- status: `PASS_WITH_NOTE`")
    lines.append("- 이번 훈련은 정답 추출이 아니라 해석 감각 학습으로 실제 작동했다. 다만 context unit 재설정은 아직 `youtube_03_22` 한 자산 중심이므로, 이후 다른 dialogue asset에 같은 방식이 반복되는지 더 봐야 한다.")
    lines.append("")
    lines.append("## 8. references")
    lines.append("")
    for key, value in references.items():
        lines.append(f"- {key}: `{value}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a multi-pass interpretation training report and context-unit candidates.")
    parser.add_argument("--input-asset", required=True)
    parser.add_argument("--purpose-json", required=True)
    parser.add_argument("--question-json", required=True)
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--pass-json-out")
    parser.add_argument("--context-json-out")
    parser.add_argument("--pointer-stabilization", choices=["none", "nearest_top_window"], default="none")
    args = parser.parse_args()

    purpose_path = Path(args.purpose_json).resolve()
    question_path = Path(args.question_json).resolve()
    purpose = _load_json(purpose_path)
    question = _load_json(question_path)

    pass_a = _pass_a(purpose, question)
    pass_b = _pass_b(question)
    pass_c = _pass_c(question)
    context_units = _make_context_units(question, purpose, args.pointer_stabilization)

    payload = {
        "created_at": _now_iso(),
        "input_asset": _relative(Path(args.input_asset).resolve()),
        "collection_context": {
            "input_asset_type": "high_density_dialogue",
            "source_asset_ref": _relative(Path(args.input_asset).resolve()),
            "supporting_first_pass_patterns": [
                "top_objects",
                "top_layers",
                "top_relations",
                "question_inducing_candidates",
                "summary_stage_deprioritization_candidates",
            ],
            "second_order_reading_type": "multi_pass_interpretation",
            "rereading_mode": "same_asset_multi_layer_rereading",
            "scope_local_page_comparison": "local_page_comparison",
            "domain_specific_suspicion": "high_ai_agent_product_transition",
            "reusable_attitude_hint": "context_unit_reconstruction_from_pass_difference",
            "candidate_status": "collect_only",
            "hold_reason": "context units are still observed as rereading outputs, not generalized units",
            "evidence_pointers": {
                "purpose_json": _relative(purpose_path),
                "question_json": _relative(question_path),
            },
            "pointer_stabilization": args.pointer_stabilization,
        },
        "pass_a": pass_a,
        "pass_b": pass_b,
        "pass_c": pass_c,
        "references": {
            "purpose_json": _relative(purpose_path),
            "question_json": _relative(question_path),
        },
    }

    context_payload = {
        "created_at": _now_iso(),
        "input_asset": _relative(Path(args.input_asset).resolve()),
        "collection_context": payload["collection_context"],
        "context_units": context_units,
    }

    report_text = _compose_report(
        payload["input_asset"],
        pass_a,
        pass_b,
        pass_c,
        context_units,
        payload["references"],
    )
    report_path = Path(args.report_path).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text)

    pass_json_out = Path(args.pass_json_out).resolve() if args.pass_json_out else OUTPUT_DIR / f"multi_pass_interpretation_training_{_stamp()}.json"
    context_json_out = Path(args.context_json_out).resolve() if args.context_json_out else OUTPUT_DIR / f"context_unit_candidates_{_stamp()}.json"
    pass_json_out.parent.mkdir(parents=True, exist_ok=True)
    context_json_out.parent.mkdir(parents=True, exist_ok=True)
    pass_json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    context_json_out.write_text(json.dumps(context_payload, ensure_ascii=False, indent=2) + "\n")

    print(_relative(report_path))
    print(_relative(pass_json_out))
    print(_relative(context_json_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
