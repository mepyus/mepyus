from __future__ import annotations

from pathlib import Path
import json


REPO_ROOT = Path(__file__).resolve().parents[3]
WORKBENCH_GENERATED = REPO_ROOT / "app" / "work" / "workbench_stage1" / "generated"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "result_value_bundle_stage1" / "generated"


def _load_packet(name: str) -> dict[str, object]:
    path = WORKBENCH_GENERATED / name
    return json.loads(path.read_text(encoding="utf-8"))


def _row(packet: dict[str, object], section: str, key: str) -> dict[str, object]:
    return dict(dict(packet[section]).get(key, {}) or {})


def _status(packet: dict[str, object], section: str, key: str) -> str:
    return str(_row(packet, section, key).get("status", "")).strip() or "missing"


def _value(packet: dict[str, object], section: str, key: str) -> object:
    return _row(packet, section, key).get("value")


def _lineage_strength(packet: dict[str, object], side: str) -> str:
    refs = list(_value(packet, "source", f"{side}_lineage_refs") or [])
    if len(refs) >= 3:
        return "present"
    if refs:
        return "partial"
    return "sparse"


def _anchor_summary(packet: dict[str, object], side: str) -> str:
    summary = dict(_value(packet, "translation_processing", f"{side}_anchor_bundle_summary") or {})
    rep = len(list(summary.get("representative", []) or []))
    sup = len(list(summary.get("supporting", []) or []))
    if not summary:
        return "missing"
    return f"rep={rep}, support={sup}, promoted={summary.get('promoted_anchor_count', 0)}"


def _processing_summary(packet: dict[str, object], side: str) -> str:
    summary = dict(_value(packet, "translation_processing", f"{side}_processing_values_summary") or {})
    if not summary:
        return "missing"
    parts = []
    for key in ("D", "I", "S", "flow", "scene"):
        value = summary.get(key)
        if value not in (None, "", []):
            parts.append(f"{key}={value}")
    return ", ".join(parts) if parts else "present"


def _one_line_verdict(packet: dict[str, object]) -> str:
    category = str(packet["candidate_context"].get("workbench_reading_category", "")).strip()
    if category == "canonical":
        return "source -> translation -> bridge가 비교적 닫힌 stable_reading 후보"
    return "closure gap이 남아 confirmed_hold로 유지되는 후보"


def _reuse_hints(packet: dict[str, object]) -> dict[str, str]:
    category = str(packet["candidate_context"].get("workbench_reading_category", "")).strip()
    return {
        "point_seed": "yes",
        "workbench_seed": "yes",
        "compare_seed": "yes",
        "ribbon_seed": "later" if category == "mixed" else "weak",
    }


def build_compare_card(packet: dict[str, object]) -> str:
    candidate_id = str(packet.get("candidate_id", "")).strip()
    category = str(packet["candidate_context"].get("workbench_reading_category", "")).strip()
    status = str(packet["candidate_context"].get("workbench_reading_status", "")).strip()
    reuse = _reuse_hints(packet)
    lines = [
        f"# result-value compare card: {candidate_id}",
        "",
        "## 1. card header",
        f"- candidate_id: `{candidate_id}`",
        f"- case_type: `{category}`",
        f"- workbench_reading_category: `{category}`",
        f"- workbench_reading_status: `{status}`",
        f"- verdict: {_one_line_verdict(packet)}",
        "",
        "## 2. source",
        f"- source_ref: `left={_value(packet, 'source', 'left_source_ref')}` / `right={_value(packet, 'source', 'right_source_ref')}`",
        f"- source_local_ref: `left={_status(packet, 'source', 'left_source_local_ref')}` / `right={_status(packet, 'source', 'right_source_local_ref')}`",
        f"- lineage_refs: `left={_lineage_strength(packet, 'left')}` / `right={_lineage_strength(packet, 'right')}`",
        "",
        "## 3. translation",
        f"- translated_handles: `left={_status(packet, 'translation_processing', 'left_translated_handles')}` / `right={_status(packet, 'translation_processing', 'right_translated_handles')}`",
        f"- anchor_bundle: `left={_anchor_summary(packet, 'left')}` / `right={_anchor_summary(packet, 'right')}`",
        f"- processing_values: `left={_processing_summary(packet, 'left')}` / `right={_processing_summary(packet, 'right')}`",
        f"- translation_join: `{_value(packet, 'translation_processing', 'translation_join_quality')}`",
        "",
        "## 4. join",
        f"- best_local_ref: `{_value(packet, 'join', 'best_local_ref')}`",
        f"- bridge_trace_ref: `{_status(packet, 'join', 'bridge_trace_ref')}`",
        f"- local_space_ref: `{_status(packet, 'join', 'local_space_ref')}`",
        f"- join_closure: `{_value(packet, 'join', 'current_pair_closure_strength')}`",
        "",
        "## 5. block",
        f"- next_review_blocker: `{_value(packet, 'block', 'next_review_blocker')}`",
        f"- missing_join_points: `{json.dumps(_value(packet, 'block', 'missing_join_points'), ensure_ascii=False)}`",
        f"- block_summary: `{_value(packet, 'block', 'why_not_closed')}`",
    ]
    if category == "mixed":
        lines.extend(
            [
                f"- mixed_record_ref: `{_value(packet, 'block', 'mixed_record_ref')}`",
                f"- closure_gap_summary: `{json.dumps(_value(packet, 'block', 'missing_join_points'), ensure_ascii=False)}`",
                f"- derived_support_summary: `best_local_ref + review_focus + next_review_blocker`",
                f"- next_review_question: `{_value(packet, 'block', 'next_review_question')}`",
            ]
        )
    lines.extend(
        [
            "",
            "## 6. reuse hints",
            f"- point_seed: `{reuse['point_seed']}`",
            f"- workbench_seed: `{reuse['workbench_seed']}`",
            f"- compare_seed: `{reuse['compare_seed']}`",
            f"- ribbon_seed: `{reuse['ribbon_seed']}`",
        ]
    )
    return "\n".join(lines) + "\n"


def build_compare_summary(mixed_packet: dict[str, object], canonical_packet: dict[str, object]) -> str:
    lines = [
        "# result-value compare card compare stage1",
        "",
        "## 1. one-line comparison",
        "- canonical은 persisted closure 중심이고, mixed는 closure gap + derived support 중심이다.",
        "",
        "## 2. four-way compare",
        "- source",
        f"  - mixed: `source_local_ref left={_status(mixed_packet, 'source', 'left_source_local_ref')}`",
        f"  - canonical: `source_local_ref left={_status(canonical_packet, 'source', 'left_source_local_ref')}`",
        "- translation",
        f"  - mixed: `translated_handles left={_status(mixed_packet, 'translation_processing', 'left_translated_handles')}`, `translation_join={_value(mixed_packet, 'translation_processing', 'translation_join_quality')}`",
        f"  - canonical: `translated_handles left={_status(canonical_packet, 'translation_processing', 'left_translated_handles')}`, `translation_join={_value(canonical_packet, 'translation_processing', 'translation_join_quality')}`",
        "- join",
        f"  - mixed: `bridge={_status(mixed_packet, 'join', 'bridge_trace_ref')}`, `closure={_value(mixed_packet, 'join', 'current_pair_closure_strength')}`",
        f"  - canonical: `bridge={_status(canonical_packet, 'join', 'bridge_trace_ref')}`, `closure={_value(canonical_packet, 'join', 'current_pair_closure_strength')}`",
        "- block",
        f"  - mixed: `{_value(mixed_packet, 'block', 'why_not_closed')}`",
        f"  - canonical: `{_value(canonical_packet, 'block', 'why_not_closed')}`",
        "",
        "## 3. conclusion",
        "- compare card가 workbench 보조면으로 충분한가: `YES`",
        "- 점/리본보다 먼저 card가 맞는가: `YES`",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    mixed_packet = _load_packet("workbench_packet_mixed_probe_doc006_stage1.json")
    canonical_packet = _load_packet("workbench_packet_canonical_doc005_doc006_stage1.json")

    mixed_card_path = OUTPUT_ROOT / "result_value_compare_card_mixed_probe_doc006_stage1.md"
    canonical_card_path = OUTPUT_ROOT / "result_value_compare_card_canonical_doc005_doc006_stage1.md"
    compare_path = OUTPUT_ROOT / "result_value_compare_card_compare_stage1.md"

    mixed_card_path.write_text(build_compare_card(mixed_packet), encoding="utf-8")
    canonical_card_path.write_text(build_compare_card(canonical_packet), encoding="utf-8")
    compare_path.write_text(build_compare_summary(mixed_packet, canonical_packet), encoding="utf-8")

    print(
        json.dumps(
            {
                "mixed_card_path": str(mixed_card_path),
                "canonical_card_path": str(canonical_card_path),
                "compare_path": str(compare_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
