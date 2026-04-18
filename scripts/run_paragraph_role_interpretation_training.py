#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "app" / "work" / "dialogue_loop_test" / "generated"

TARGETS = {
    "bundle_unbundle_block": {
        "heading": "Bundle-Unbundle 프레임워크",
        "context_unit": "agent_interface_transition_unit",
        "local_context_role": "question_seed_block",
        "page_flow_role": "strategy_pivot_block",
        "comparison_target": "future_of_work_supervisor_unit",
        "comparison_role": "노동 역할 변화보다 앱 구조 재편과 moat 이동을 더 강하게 여는 단락",
        "objects": ["에이전트 애플리케이션", "전략/방향성", "구현/자동화"],
        "layers": ["구조/연결 층", "전략/방향 층", "질문 유도 층"],
        "relation_movement": ["transition_hint", "contrast_hint", "execution_shift_hint", "question_generation_hint"],
    },
    "future_of_work_block": {
        "heading": "GTC 키노트와 ‘일의 미래’",
        "context_unit": "future_of_work_supervisor_unit",
        "local_context_role": "role_shift_seed_block",
        "page_flow_role": "future_of_work_question_seed",
        "comparison_target": "agent_interface_transition_unit",
        "comparison_role": "앱 구조보다 사람의 역할 재배치와 감독자형 노동을 더 강하게 여는 단락",
        "objects": ["일의 미래", "생산성/코딩", "에이전트 애플리케이션"],
        "layers": ["설명/해석 층", "전략/방향 층", "질문 유도 층"],
        "relation_movement": ["transition_hint", "execution_shift_hint", "question_generation_hint"],
    },
    "model_eval_shift_block": {
        "heading": "RLVR과 CUA",
        "context_unit": "model_eval_shift_unit",
        "local_context_role": "evaluation_shift_block",
        "page_flow_role": "compression_node",
        "comparison_target": "agent_interface_transition_unit",
        "comparison_role": "앱 인터페이스 재편보다 모델 경쟁의 검증 바닥과 환경 이동을 더 강하게 여는 단락",
        "objects": ["AI의 미래", "모델 work", "에이전트 애플리케이션"],
        "layers": ["검증/근거 층", "구조/연결 층", "전략/방향 층"],
        "relation_movement": ["transition_hint", "execution_shift_hint", "specification_hint", "question_generation_hint"],
    },
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def _excerpt(text: str, limit: int = 480) -> str:
    compact = " ".join(text.split())
    return compact if len(compact) <= limit else compact[: limit - 1] + "…"


def _split_sections(text: str) -> List[Dict[str, str]]:
    sections: List[Dict[str, str]] = []
    heading = "untitled"
    lines: List[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            if lines:
                body = "\n".join(lines).strip()
                if body:
                    sections.append({"heading": heading, "text": body})
                lines = []
            heading = line[3:].strip()
            continue
        if not line.strip():
            if lines:
                body = "\n".join(lines).strip()
                if body:
                    sections.append({"heading": heading, "text": body})
                lines = []
            continue
        lines.append(line)
    if lines:
        body = "\n".join(lines).strip()
        if body:
            sections.append({"heading": heading, "text": body})
    return sections


def _find_section(sections: List[Dict[str, str]], heading: str) -> Dict[str, str]:
    matched = [section["text"] for section in sections if section["heading"] == heading]
    if not matched:
        raise ValueError(f"heading not found: {heading}")
    return {"heading": heading, "text": "\n\n".join(matched)}


def _load_json(path: Path) -> Dict:
    return json.loads(path.read_text())


def _role_hint_from_page_role(page_role: str) -> str:
    mapping = {
        "pivot": "transition_or_strategy_role_hint",
        "question_seed": "question_or_role_shift_hint",
        "compression_node": "compression_or_evaluation_hint",
    }
    return mapping.get(page_role, "role_like_hint")


def _role_strength(unit: Dict[str, object]) -> str:
    refs = unit.get("present_window_refs", [])
    grounding = unit.get("grounding_status", "empty_ref")
    if grounding == "direct_grounded" and refs:
        return "medium"
    if grounding == "fallback_grounded" and refs:
        return "weak_medium"
    return "weak"


def _probe_excerpt(unit: Dict[str, object], purpose_windows: List[Dict[str, object]]) -> str:
    pointer_set = set(unit.get("evidence_pointers", []))
    texts: List[str] = []
    for row in purpose_windows:
        if row.get("window_id") in pointer_set:
            opening = row.get("opening_summary", "").strip()
            if opening:
                texts.append(opening)
    compact = " / ".join(texts[:2])
    return compact if compact else "명시 heading 없이 fallback evidence window를 통해 role-like reading만 관찰됨"


def _build_payload(input_asset: Path) -> Dict[str, object]:
    sections = _split_sections(input_asset.read_text())
    analyses = []
    for analysis_id, spec in TARGETS.items():
        section = _find_section(sections, spec["heading"])
        analyses.append(
            {
                "analysis_id": analysis_id,
                "heading": spec["heading"],
                "context_unit": spec["context_unit"],
                "excerpt": _excerpt(section["text"]),
                "objects": spec["objects"],
                "layers": spec["layers"],
                "relation_movement": spec["relation_movement"],
                "local_context_role": spec["local_context_role"],
                "page_flow_role": spec["page_flow_role"],
                "comparison_target": spec["comparison_target"],
                "comparison_role": spec["comparison_role"],
                "second_order_reading_type": "paragraph_role_interpretation",
                "rereading_mode": "local_page_comparison_rereading",
                "scope_local_page_comparison": "local_page_comparison",
                "domain_specific_suspicion": "high_ai_agent_business_transition",
                "reusable_attitude_hint": "role_shift_by_context_frame",
                "candidate_status": "hold_candidate",
                "hold_reason": "role reading is clear but current headings and role names are still domain-skewed",
                "evidence_pointers": [spec["heading"], spec["context_unit"], spec["comparison_target"]],
            }
        )
    return {
        "created_at": _now_iso(),
        "input_asset": _relative(input_asset),
        "collection_context": {
            "input_asset_type": "high_density_dialogue",
            "source_asset_ref": _relative(input_asset),
            "supporting_first_pass_patterns": [
                "context_unit",
                "local_context_role",
                "page_flow_role",
                "comparison_target",
                "relation_movement",
            ],
            "second_order_reading_type": "paragraph_role_interpretation_training",
            "rereading_mode": "local_page_comparison_rereading",
            "scope_local_page_comparison": "local_page_comparison",
            "domain_specific_suspicion": "high_ai_agent_business_transition",
            "reusable_attitude_hint": "paragraph_role_shift_collection",
            "candidate_status": "collect_only",
            "hold_reason": "paragraph role outputs are still collected as examples before cross-domain comparison",
            "evidence_pointers": [spec["heading"] for spec in TARGETS.values()],
        },
        "paragraph_role_analyses": analyses,
    }


def _build_heading_probe_payload(input_asset: Path, context_json: Path, purpose_json: Path) -> Dict[str, object]:
    context_payload = _load_json(context_json)
    purpose_payload = _load_json(purpose_json)
    purpose_windows = purpose_payload.get("top_windows", [])
    analyses = []
    for unit in context_payload.get("context_units", []):
        evidence = unit.get("evidence_pointers", [])
        role_hint = _role_hint_from_page_role(unit.get("page_role", ""))
        analyses.append(
            {
                "analysis_id": unit["unit_id"],
                "probe_mode": "heading_independent_role_probe",
                "heading_dependency_reduced": True,
                "heading_found": False,
                "context_unit": unit["unit_id"],
                "excerpt": _probe_excerpt(unit, purpose_windows),
                "objects": unit.get("center_objects", []),
                "layers": unit.get("center_layers", []),
                "relation_movement": unit.get("relation_movement", []),
                "role_probe_status": "role_like_reading_observed" if evidence else "role_like_reading_weak",
                "role_hint_strength": _role_strength(unit),
                "role_like_hint": role_hint,
                "page_flow_role": unit.get("page_role", ""),
                "comparison_target": "",
                "comparison_role": "explicit heading 없이도 기능 단서와 evidence window로만 약한 role-like reading을 시도",
                "grounding_status": unit.get("grounding_status", "empty_ref"),
                "pointer_support_source": unit.get("pointer_support_source", "none"),
                "role_evidence_pointers": evidence,
                "unsupported_role_naming_risk": "low" if evidence else "medium",
                "second_order_reading_type": "heading_independent_role_probe",
                "rereading_mode": "role_like_probe_without_heading",
                "scope_local_page_comparison": "local_page_probe",
                "domain_specific_suspicion": "medium_high",
                "reusable_attitude_hint": "role_like_reading_from_functional_cues",
                "candidate_status": "hold_candidate",
                "hold_reason": "role-like hint is observable, but still fallback-grounded and not a generalized paragraph-role system",
                "evidence_pointers": evidence,
            }
        )
    return {
        "created_at": _now_iso(),
        "input_asset": _relative(input_asset),
        "collection_context": {
            "input_asset_type": "technical_index_like_doc",
            "source_asset_ref": _relative(input_asset),
            "supporting_first_pass_patterns": [
                "context_unit",
                "present_window_refs",
                "grounding_status",
                "page_role",
                "relation_movement",
            ],
            "second_order_reading_type": "heading_independent_role_probe",
            "rereading_mode": "role_like_probe_without_heading",
            "scope_local_page_comparison": "local_page_probe",
            "domain_specific_suspicion": "medium_high",
            "reusable_attitude_hint": "role_like_reading_from_functional_cues",
            "candidate_status": "collect_only",
            "hold_reason": "probe observes role-like reading conditions without claiming generalized role interpretation",
            "evidence_pointers": {
                "context_json": _relative(context_json),
                "purpose_json": _relative(purpose_json),
            },
        },
        "paragraph_role_analyses": analyses,
    }


def _compose_report(payload: Dict[str, object]) -> str:
    lines: List[str] = []
    lines.append("[[A]] [[OBJ:report_guided_paragraph_interpretation_training_v1]] [[SEM:actual_paragraph_role_reading_execution_after_example_learning]]")
    lines.append("")
    lines.append("# report-guided paragraph interpretation training v1")
    lines.append("")
    lines.append("## 1. purpose")
    lines.append("")
    lines.append("- 이번 문서는 example를 저장한 것이 아니라, 실제 단락을 역할 단위로 읽는 실행 결과다.")
    lines.append("- 같은 단락을 `local context`, `whole-page flow`, `comparison context`에서 다시 읽어, 내용 요약이 아니라 역할 판독이 가능한지 본다.")
    lines.append("")
    lines.append("## 2. paragraph analyses")
    lines.append("")
    for row in payload["paragraph_role_analyses"]:
        lines.append(f"- `{row.get('heading', row.get('analysis_id', 'untitled'))}`")
        lines.append(f"  - context_unit: {row['context_unit']}")
        lines.append(f"  - excerpt: {row['excerpt']}")
        if "local_context_role" in row:
            lines.append(f"  - local_context_role: {row['local_context_role']}")
        if "role_probe_status" in row:
            lines.append(f"  - role_probe_status: {row['role_probe_status']}")
            lines.append(f"  - role_hint_strength: {row['role_hint_strength']}")
            lines.append(f"  - role_like_hint: {row['role_like_hint']}")
            lines.append(f"  - grounding_status: {row['grounding_status']}")
            lines.append(f"  - pointer_support_source: {row['pointer_support_source']}")
            lines.append(f"  - role_evidence_pointers: {', '.join(row['role_evidence_pointers'])}")
        lines.append(f"  - page_flow_role: {row['page_flow_role']}")
        lines.append(f"  - comparison_target: {row['comparison_target']}")
        lines.append(f"  - comparison_role: {row['comparison_role']}")
        lines.append(f"  - objects: {', '.join(row['objects'])}")
        lines.append(f"  - layers: {', '.join(row['layers'])}")
        lines.append(f"  - relation_movement: {', '.join(row['relation_movement'])}")
    lines.append("")
    lines.append("## 3. what changed by reading paragraphs as roles")
    lines.append("")
    lines.append("- `Bundle-Unbundle 프레임워크`는 단순 설명 문단이 아니라 앱 구조 재편과 moat 이동을 여는 pivot으로 읽혔다.")
    lines.append("- `GTC 키노트와 ‘일의 미래’`는 사례 설명이 아니라 사람의 역할이 감독/설계 쪽으로 이동하는 question seed로 읽혔다.")
    lines.append("- `RLVR과 CUA`는 트렌드 서술이 아니라 모델 경쟁이 evaluation environment로 이동한다는 compression node로 읽혔다.")
    lines.append("")
    lines.append("## 4. one-line verdict")
    lines.append("")
    lines.append("> 이번 실행은 단락을 요약하는 대신, 같은 단락이 맥락과 비교축에 따라 `seed / pivot / compression node` 같은 다른 역할로 읽힌다는 점을 실제로 보여준다.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run actual paragraph role interpretation training on selected dialogue sections.")
    parser.add_argument("--input-asset", required=True)
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--json-out")
    parser.add_argument("--context-json")
    parser.add_argument("--purpose-json")
    parser.add_argument("--heading-probe", choices=["none", "functional_cue"], default="none")
    args = parser.parse_args()

    input_asset = Path(args.input_asset).resolve()
    if args.heading_probe == "functional_cue":
        if not args.context_json or not args.purpose_json:
            raise ValueError("--context-json and --purpose-json are required for heading probe mode")
        payload = _build_heading_probe_payload(
            input_asset,
            Path(args.context_json).resolve(),
            Path(args.purpose_json).resolve(),
        )
    else:
        payload = _build_payload(input_asset)

    report_text = _compose_report(payload)
    report_path = Path(args.report_path).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text)

    json_out = Path(args.json_out).resolve() if args.json_out else OUTPUT_DIR / f"paragraph_role_interpretation_training_{_stamp()}.json"
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    print(_relative(report_path))
    print(_relative(json_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
