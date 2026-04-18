#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "app" / "work" / "dialogue_loop_test" / "generated"

OBJECT_READING = {
    "AI의 미래": "발전 방향과 capability trajectory를 여는 장기 전망 객체",
    "일의 미래": "인간 역할, 감독 구조, 노동 재배치를 여는 객체",
    "생산성/코딩": "개발 생산성 압축과 작업 방식 변형을 여는 객체",
    "에이전트 애플리케이션": "앱 형태 재편과 인터페이스 전환을 여는 객체",
    "모델 work": "모델 경쟁, 학습/평가/검증 축을 여는 객체",
    "구현/자동화": "실행화, workflow, 운영 자동화를 여는 객체",
    "전략/방향성": "사업 적응, moat, 시장 재편을 여는 객체",
}

LAYER_READING = {
    "설명/해석 층": "대화가 시대 인식을 설명하고 해석하는 기본 층",
    "구현/실행 층": "실제 자동화와 operationalization으로 내려가는 층",
    "구조/연결 층": "앱/모델/시장 구조가 어떻게 재편되는지 보는 층",
    "전략/방향 층": "적응, moat, 신사업, 시장 포지션을 읽는 층",
    "검증/근거 층": "평가, metric, reward, reliability를 묻는 층",
    "질문 유도 층": "사용자의 다음 탐색 질문을 발생시키는 층",
}

RELATION_READING = {
    "reinforcement_hint": "같은 문제의식이 다른 문단에서 누적 보강되는 운동",
    "contrast_hint": "기존 방식과 새 방식의 긴장/대비가 드러나는 운동",
    "transition_hint": "설명에서 다음 층위로 이동하는 전이 운동",
    "execution_shift_hint": "아이디어가 운영/실행 쪽으로 내려가는 운동",
    "specification_hint": "막연한 전망이 기준/평가/형식 쪽으로 굳어지는 운동",
    "question_generation_hint": "문단이 다음 질문을 직접 발생시키는 운동",
}

RESIDUE_READING = {
    "discourse_connective_residue": "발화 연결어가 의미 층위 opening을 덮는 residue",
    "speaker_or_source_residue": "화자/출처 흔적이 topic signal과 경쟁하는 residue",
    "conversational_filler_residue": "구어 filler가 summary 선두를 흐리는 residue",
    "generic_abstraction_residue": "너무 일반적인 추상어가 의미층을 흐리게 하는 residue",
    "quasi_topic_residue": "주제처럼 보이지만 broad discourse에 가까운 residue",
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


def _load_probe(path: Path) -> Dict:
    return json.loads(path.read_text())


def _top(counter: Counter[str], limit: int = 6) -> List[Dict[str, object]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _top_objects_with_reading(counter: Counter[str], limit: int = 6) -> List[Dict[str, object]]:
    rows = []
    for value, count in counter.most_common(limit):
        rows.append(
            {
                "object": value,
                "count": count,
                "reading": OBJECT_READING.get(value, "반복적으로 살아난 객체 후보"),
            }
        )
    return rows


def _top_layers_with_reading(counter: Counter[str], limit: int = 6) -> List[Dict[str, object]]:
    rows = []
    for value, count in counter.most_common(limit):
        rows.append(
            {
                "layer": value,
                "count": count,
                "reading": LAYER_READING.get(value, "사용자 질문을 여는 의미 층"),
            }
        )
    return rows


def _top_relations_with_reading(counter: Counter[str], limit: int = 6) -> List[Dict[str, object]]:
    rows = []
    for value, count in counter.most_common(limit):
        rows.append(
            {
                "relation": value,
                "count": count,
                "reading": RELATION_READING.get(value, "반복 relation hint"),
            }
        )
    return rows


def _top_residue_with_reading(counter: Counter[str], limit: int = 5) -> List[Dict[str, object]]:
    rows = []
    for value, count in counter.most_common(limit):
        rows.append(
            {
                "residue": value,
                "count": count,
                "reading": RESIDUE_READING.get(value, "반복 residue"),
            }
        )
    return rows


def _dedupe_top_windows(probes: List[Dict], limit: int = 6) -> List[Dict[str, object]]:
    by_id: Dict[str, Dict[str, object]] = {}
    counts: Counter[str] = Counter()
    for probe in probes:
        for row in probe.get("top_question_intent_windows", []):
            window_id = row["window_id"]
            counts[window_id] += 1
            if window_id not in by_id or row["question_intent_score"] > by_id[window_id]["question_intent_score"]:
                by_id[window_id] = row
    ranked = sorted(
        by_id.values(),
        key=lambda row: (row["question_intent_score"], counts[row["window_id"]], row["start_index"]),
        reverse=True,
    )
    output = []
    for row in ranked[:limit]:
        output.append(
            {
                "window_id": row["window_id"],
                "repeat_count": counts[row["window_id"]],
                "question_intent_score": row["question_intent_score"],
                "objects": [item["object"] for item in row.get("object_candidates", [])[:4]],
                "relation_hints": row.get("relation_hints", []),
                "opening_summary": row.get("opening_summary", ""),
                "headings": row.get("headings", []),
                "sample_blocks": row.get("sample_blocks", [])[:2],
            }
        )
    return output


def _era_questions(object_counter: Counter[str], layer_counter: Counter[str]) -> List[str]:
    questions: List[str] = []
    if object_counter["AI의 미래"] > 0:
        questions.append("AI capability가 어디까지 가고 어떤 방향으로 수렴하는가")
    if object_counter["일의 미래"] > 0:
        questions.append("인간의 일은 수행자에서 감독자/설계자로 어떻게 이동하는가")
    if object_counter["에이전트 애플리케이션"] > 0:
        questions.append("앱과 서비스의 형태는 agent interface 쪽으로 어떻게 재편되는가")
    if object_counter["모델 work"] > 0:
        questions.append("모델 경쟁은 pre-train 이후 evaluation, RLVR, harness 쪽으로 어떻게 이동하는가")
    if object_counter["전략/방향성"] > 0:
        questions.append("기업과 제품은 moat, bundle/unbundle, 적응 경쟁 속에서 어떻게 살아남는가")
    if layer_counter["검증/근거 층"] > 0:
        questions.append("검증과 신뢰는 미래 담론 속에서 어떤 바닥 역할을 맡는가")
    return questions


def _object_growth_reading(object_counter: Counter[str]) -> List[str]:
    readings: List[str] = []
    if object_counter["에이전트 애플리케이션"] and object_counter["모델 work"]:
        readings.append("이 자산은 모델 능력 경쟁과 agent application 형태 전환을 서로 붙여 키운다")
    if object_counter["AI의 미래"] and object_counter["일의 미래"]:
        readings.append("미래 담론을 추상 전망으로만 두지 않고 인간 역할 변화와 일의 재배치로 끌어내린다")
    if object_counter["전략/방향성"] and object_counter["구현/자동화"]:
        readings.append("전략 담론을 실제 구현/운영 자동화와 접속시키며 사업 적응 문제로 내린다")
    if object_counter["생산성/코딩"]:
        readings.append("개발 생산성 변화는 독립 객체라기보다 실행층과 일의 미래를 잇는 중간층으로 자란다")
    return readings


def _engine_learning_targets(layer_counter: Counter[str], relation_counter: Counter[str], residue_counter: Counter[str]) -> List[str]:
    targets: List[str] = []
    if relation_counter["question_generation_hint"] > 0:
        targets.append("질문 유도 문단을 별도 candidate로 승격할 수 있는지 계속 본다")
    if relation_counter["execution_shift_hint"] > 0:
        targets.append("설명층에서 실행층으로 내려가는 전이 문단을 relation movement로 더 잘 읽게 만든다")
    if layer_counter["전략/방향 층"] > 0:
        targets.append("전망 담론을 전략/적응 문제로 번역하는 층을 user-layer opening에 더 직접 연결한다")
    if residue_counter["discourse_connective_residue"] > 0 or residue_counter["conversational_filler_residue"] > 0:
        targets.append("interview/dialogue 특유 residue가 summary 선두를 덮지 않게 summary-stage 후순위화를 검토한다")
    return targets


def _collection_context(input_asset: Path, probe_paths: List[Path]) -> Dict[str, object]:
    return {
        "input_asset_type": "high_density_dialogue",
        "source_asset_ref": _relative(input_asset),
        "supporting_first_pass_patterns": [
            "overall_object_candidates",
            "overall_layer_hints",
            "overall_relation_hints",
            "overall_residue_breakdown",
            "top_question_intent_windows",
        ],
        "second_order_reading_type": "purpose_synthesis",
        "rereading_mode": "cross_run_probe_synthesis",
        "scope_local_page_comparison": "page",
        "domain_specific_suspicion": "high_ai_agent_product_transition",
        "reusable_attitude_hint": "object_opening_and_question_opening_collection",
        "candidate_status": "collect_only",
        "hold_reason": "purpose reading is still strongly tied to AI/agent/business transition discourse",
        "evidence_pointers": [_relative(path) for path in probe_paths],
    }


def _compose_report(data: Dict[str, object]) -> str:
    lines: List[str] = []
    lines.append("[[A]] [[OBJ:youtube_03_22_engine_purpose_reset_reading_v1]] [[SEM:purpose_aligned_reading_of_high_density_dialogue_asset_for_engine_learning]]")
    lines.append("")
    lines.append("# youtube_03_22 엔진 목적 정렬 재해석 v1")
    lines.append("")
    lines.append("## 1. 이번 재해석의 목적")
    lines.append("")
    lines.append("- 이번 문서의 목적은 `youtube_03_22.md`가 잘 분절되는지 다시 확인하는 것이 아니다.")
    lines.append("- 목적은 이 자산이 `AI 시대를 어떻게 살아갈 것인가`라는 큰 질문 아래 어떤 객체를 두껍게 하고, 어떤 관계 운동을 만들며, 어떤 사용자 질문 층위를 여는지 엔진 관점에서 다시 읽는 것이다.")
    lines.append("- 즉 이 문서는 loop 결과 요약이 아니라, 반복 실험 산출물을 엔진 직무 정의와 사용자 층위 번역 기준으로 다시 정렬한 purpose-reading이다.")
    lines.append("")
    lines.append("## 2. 이 자산을 어떻게 읽어야 하는가")
    lines.append("")
    lines.append("- `youtube_03_22.md`는 단순 AI 업계 대화 스크립트가 아니다.")
    lines.append("- 이 자산은 `모델 경쟁`, `에이전트 애플리케이션`, `일의 미래`, `전략/적응`, `구현/자동화`가 한 문서 안에서 함께 자라는 고밀도 객체 성장 사건이다.")
    lines.append("- 따라서 엔진이 이 자산에서 배워야 할 것은 키워드 몇 개가 아니라, AI 시대의 세계 이해가 어떤 층과 질문들로 열리는지다.")
    lines.append("")
    lines.append("## 3. 반복적으로 살아난 객체와 그 의미")
    lines.append("")
    for row in data["top_objects"]:
        lines.append(f"- `{row['object']}`: {row['reading']} (`count={row['count']}`)")
    lines.append("")
    lines.append("### 객체 성장 읽기")
    for row in data["object_growth_reading"]:
        lines.append(f"- {row}")
    lines.append("")
    lines.append("## 4. 이 대화가 실제로 여는 시대 질문")
    lines.append("")
    for row in data["era_questions"]:
        lines.append(f"- {row}")
    lines.append("")
    lines.append("## 5. 반복적으로 보이는 층위")
    lines.append("")
    for row in data["top_layers"]:
        lines.append(f"- `{row['layer']}`: {row['reading']} (`count={row['count']}`)")
    lines.append("")
    lines.append("### 현재 읽기")
    lines.append("- 가장 두꺼운 층은 여전히 설명/해석 층이다.")
    lines.append("- 하지만 이 자산의 중요한 점은 설명층 아래에서 전략/방향, 질문 유도, 검증/근거, 구현/실행 층이 같이 살아난다는 점이다.")
    lines.append("- 즉 이 대화는 단순 해설문이 아니라, 미래 전망이 실행과 사업 적응 문제로 내려오는 전이형 자산이다.")
    lines.append("")
    lines.append("## 6. 관계 운동")
    lines.append("")
    for row in data["top_relations"]:
        lines.append(f"- `{row['relation']}`: {row['reading']} (`count={row['count']}`)")
    lines.append("")
    lines.append("### 관계 운동 해석")
    lines.append("- 이 자산에서 중요한 것은 객체가 따로따로 뜨는 것이 아니라, 미래 담론이 검증/실행/전략 쪽으로 반복 이동한다는 점이다.")
    lines.append("- 특히 `transition_hint`, `execution_shift_hint`, `question_generation_hint`가 강하다는 것은 이 대화가 그냥 설명을 끝내지 않고 다음 판단과 실행 질문을 발생시킨다는 뜻이다.")
    lines.append("")
    lines.append("## 7. 질문 의도와 강하게 닿는 구간")
    lines.append("")
    for row in data["top_windows"]:
        lines.append(f"- window `{row['window_id']}` (`repeat_count={row['repeat_count']}`, `score={row['question_intent_score']}`)")
        lines.append(f"  - objects: {', '.join(row['objects'])}")
        lines.append(f"  - relation_hints: {', '.join(row['relation_hints'])}")
        lines.append(f"  - summary: {row['opening_summary']}")
        for block in row["sample_blocks"]:
            lines.append(f"  - block: `{block['heading']}`")
    lines.append("")
    lines.append("### 왜 중요한가")
    lines.append("- 이 구간들은 `AI의 미래`를 추상 미래론으로 두지 않고, RLVR/CUA, bundle-unbundle, moat, 자동화, 일의 재배치 같은 실제 문제로 끌어내린다.")
    lines.append("- 즉 사용자의 다음 질문이 자연스럽게 생기는 문단들이다.")
    lines.append("")
    lines.append("## 8. residue는 무엇을 방해하는가")
    lines.append("")
    for row in data["top_residue"]:
        lines.append(f"- `{row['residue']}`: {row['reading']} (`count={row['count']}`)")
    lines.append("")
    lines.append("### 현재 해석")
    lines.append("- interview/dialogue 특유 residue는 이 자산을 무의미하게 만들지는 않는다.")
    lines.append("- 다만 summary 선두를 차지하면서 `AI 시대를 어떻게 살아갈 것인가`라는 큰 질문의 opening을 흐릴 수 있다.")
    lines.append("- 따라서 이 자산의 다음 bounded step은 hard suppression이 아니라 summary-stage 후순위화 검토가 맞다.")
    lines.append("")
    lines.append("## 9. 엔진이 이 자산에서 실제로 배워야 할 것")
    lines.append("")
    for row in data["engine_learning_targets"]:
        lines.append(f"- {row}")
    lines.append("")
    lines.append("### 하지 말아야 할 해석")
    lines.append("- 이 대화를 철학 정답 추출 자산처럼 취급하지 않는다.")
    lines.append("- broad review count가 높다고 해서 설명형 문서로만 닫지 않는다.")
    lines.append("- 객체 후보가 잡혔다고 바로 ontology나 general law로 승격하지 않는다.")
    lines.append("")
    lines.append("## 10. 한 줄 결론")
    lines.append("")
    lines.append("> `youtube_03_22.md`는 단순 분절 테스트 문서가 아니라, AI 시대의 모델 경쟁·에이전트 앱 전환·일의 재배치·사업 적응을 한 공간 안에 겹쳐 놓은 고밀도 객체 성장 자산이며, 엔진은 이 자산을 통해 미래를 설명하는 언어가 어떻게 실행·전략·질문 의도로 이동하는지 배워야 한다.")
    lines.append("")
    lines.append("## 11. provenance")
    lines.append("")
    lines.append(f"- created_at: `{data['created_at']}`")
    lines.append(f"- input_asset: `{data['input_asset']}`")
    lines.append("- probe_files:")
    for row in data["probe_files"]:
        lines.append(f"  - `{row}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Synthesize purpose-aligned dialogue asset reading from repeated loop probes.")
    parser.add_argument("--input-asset", required=True, help="Path to original dialogue asset")
    parser.add_argument("--probe", action="append", required=True, help="Probe JSON path; pass multiple times")
    parser.add_argument("--report-path", required=True, help="Markdown report output path")
    parser.add_argument("--json-out", help="Optional JSON summary path")
    args = parser.parse_args()

    input_asset = Path(args.input_asset).resolve()
    probe_paths = [Path(p).resolve() for p in args.probe]
    probes = [_load_probe(path) for path in probe_paths]

    object_counter: Counter[str] = Counter()
    layer_counter: Counter[str] = Counter()
    relation_counter: Counter[str] = Counter()
    residue_counter: Counter[str] = Counter()

    for probe in probes:
        for row in probe.get("overall_object_candidates", []):
            object_counter[row["object"]] += row["count"]
        for row in probe.get("overall_layer_hints", []):
            layer_counter[row["layer"]] += row["count"]
        for row in probe.get("overall_relation_hints", []):
            relation_counter[row["hint"]] += row["count"]
        for key, count in probe.get("overall_residue_breakdown", {}).items():
            residue_counter[key] += count

    summary = {
        "created_at": _now_iso(),
        "input_asset": _relative(input_asset),
        "probe_files": [_relative(path) for path in probe_paths],
        "collection_context": _collection_context(input_asset, probe_paths),
        "top_objects": _top_objects_with_reading(object_counter),
        "top_layers": _top_layers_with_reading(layer_counter),
        "top_relations": _top_relations_with_reading(relation_counter),
        "top_residue": _top_residue_with_reading(residue_counter),
        "top_windows": _dedupe_top_windows(probes),
        "era_questions": _era_questions(object_counter, layer_counter),
        "object_growth_reading": _object_growth_reading(object_counter),
        "engine_learning_targets": _engine_learning_targets(layer_counter, relation_counter, residue_counter),
    }

    report_text = _compose_report(summary)
    report_path = Path(args.report_path).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text)

    json_out = Path(args.json_out).resolve() if args.json_out else OUTPUT_DIR / f"dialogue_asset_purpose_synthesis_{_stamp()}.json"
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")

    print(_relative(report_path))
    print(_relative(json_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
