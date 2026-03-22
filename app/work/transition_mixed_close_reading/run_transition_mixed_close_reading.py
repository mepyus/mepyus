from __future__ import annotations

from collections import Counter
from pathlib import Path
import json


REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "transition_mixed_close_reading" / "generated"

ROUND1_ROOT = REPO_ROOT / "app" / "work" / "youtube_transcript_probe_0322" / "generated"
ROUND2_ROOT = REPO_ROOT / "app" / "work" / "youtube_transcript_probe_0322_b" / "generated"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def build_round_bundle(round_id: str, root: Path) -> dict[str, object]:
    if round_id == "round1":
        source = load_json(root / "youtube_03_22_source_manifest.json")
        windows = load_json(root / "youtube_03_22_window_packets.json")
        anchors = load_json(root / "youtube_03_22_anchor_linkage_report.json")
        stage = load_json(root / "youtube_03_22_stage_passage_summary.json")
    else:
        source = load_json(root / "source_manifest_round2.json")
        windows = load_json(root / "window_packets_round2.json")
        anchors = load_json(root / "anchor_linkage_report_round2.json")
        stage = load_json(root / "stage_passage_summary_round2.json")
    return {"source": source, "windows": windows, "anchors": anchors, "stage": stage}


def excerpt_from_fragments(window: dict[str, object]) -> str:
    fragments = list(window.get("fragment_units", []) or [])
    parts = []
    for row in fragments[:3]:
        title = str(row.get("section_title", "")).strip()
        text = str(row.get("raw_text_excerpt", "")).strip()
        if title or text:
            parts.append(f"[{title}] {text}")
    return " / ".join(parts)[:500]


def detect_transition(window: dict[str, object]) -> tuple[str, str]:
    topics = list(window.get("dominant_topics", []) or [])
    if "model_compute" in topics or "harness_agent" in topics:
        transition_from = "technical"
    else:
        transition_from = "source"
    if "organization_ax" in topics:
        transition_to = "organization"
    elif "ai_business" in topics:
        transition_to = "business"
    else:
        transition_to = "mixed_target"
    return transition_from, transition_to


def select_bridge_fragments(window: dict[str, object]) -> list[dict[str, object]]:
    out = []
    for row in list(window.get("transition_fragments", []) or [])[:5]:
        out.append(
            {
                "fragment_id": row.get("segment_id", ""),
                "section_title": row.get("section_title", ""),
                "speaker": row.get("speaker", ""),
                "note": row.get("note", ""),
            }
        )
    return out


def classify_gap(detail: dict[str, object]) -> list[dict[str, object]]:
    rows = []
    if detail["source_survival"] in {"weak", "lost"}:
        rows.append(
            {
                "unit_id": detail["unit_id"],
                "gap_type": "source_gap",
                "severity": "medium",
                "evidence": "source survival below kept",
                "recovery_hint": "confirm whether source-side local position is actually preserved",
                "layer_owner": "observer_only",
            }
        )
    if detail["translation_survival"] in {"weak", "none"}:
        rows.append(
            {
                "unit_id": detail["unit_id"],
                "gap_type": "translation_gap",
                "severity": "medium",
                "evidence": f"translation_survival={detail['translation_survival']}",
                "recovery_hint": "inspect whether semantic repeat has enough translation explanation",
                "layer_owner": "meaning_layer_candidate",
            }
        )
    rows.append(
        {
            "unit_id": detail["unit_id"],
            "gap_type": "transition_overextension",
            "severity": "high",
            "evidence": detail["closure_gap_point"],
            "recovery_hint": "surface the technical -> business or technical -> organization transition more explicitly",
            "layer_owner": "meaning_layer_candidate",
        }
    )
    rows.append(
        {
            "unit_id": detail["unit_id"],
            "gap_type": "join_gap",
            "severity": "medium",
            "evidence": f"join_closure={detail['join_closure']}",
            "recovery_hint": "keep hold status and show why closure stayed transition-led",
            "layer_owner": "core_candidate" if detail["repeated_anchor_support"] >= 3 else "meaning_layer_candidate",
        }
    )
    if detail["repeated_anchor_support"] >= 3 and detail["join_closure"] == "gap_dominant":
        rows.append(
            {
                "unit_id": detail["unit_id"],
                "gap_type": "closure_spread",
                "severity": "medium",
                "evidence": "anchor support is strong but stable closure does not condense",
                "recovery_hint": "add a tighter explanation layer before considering core changes",
                "layer_owner": "meaning_layer_candidate",
            }
        )
    return rows


def unit_is_good_mixed(detail: dict[str, object]) -> bool:
    return detail["repeated_anchor_support"] >= 2 and detail["join_closure"] == "gap_dominant"


def build_reading_material() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    bundles = {
        "round1": build_round_bundle("round1", ROUND1_ROOT),
        "round2": build_round_bundle("round2", ROUND2_ROOT),
    }

    mixed_index: list[dict[str, object]] = []
    detail_packets: list[dict[str, object]] = []
    bridge_map: list[dict[str, object]] = []
    gap_ledger: list[dict[str, object]] = []

    for round_id, bundle in bundles.items():
        window_map = {row["window_id"]: row for row in list(bundle["windows"])}
        anchor_map = {row["anchor_or_handle"]: row for row in list(bundle["anchors"])}
        source_segments = {row["segment_id"]: row for row in list(dict(bundle["source"]).get("segments", []))}

        for row in list(bundle["stage"]):
            if row["workbench_reading_category"] != "mixed":
                continue
            unit_id = str(row["unit_id"])
            window = dict(window_map[unit_id])
            segment_ids = list(window.get("included_segment_ids", []) or [])
            local_range = []
            for sid in segment_ids[:2] + segment_ids[-2:]:
                seg = source_segments.get(sid)
                if seg:
                    local_range.append(seg.get("local_source_ref", ""))
            dominant_transition = row["key_gap"]
            repeated_groups = list(window.get("repeated_anchor_candidates", []) or [])
            excerpt = excerpt_from_fragments(window)
            transition_from, transition_to = detect_transition(window)
            dominant_anchor_group = repeated_groups[0] if repeated_groups else ""
            bridge_fragments = select_bridge_fragments(window)
            detail = {
                "round_id": round_id,
                "unit_id": unit_id,
                "source_survival": row["source_survival"],
                "translation_survival": row["translation_survival"],
                "join_closure": row["join_closure"],
                "repeated_anchor_support": row["repeated_anchor_support"],
                "dominant_anchor_group": dominant_anchor_group,
                "transition_from": transition_from,
                "transition_to": transition_to,
                "bridge_fragments": bridge_fragments,
                "closure_gap_point": row["key_gap"],
                "why_not_canonical": row["why_this_reading"],
                "why_not_unreadable": "repeated anchors survive strongly enough that discarding this window as unreadable would lose a meaningful transition corridor.",
                "good_mixed": unit_is_good_mixed(row),
            }
            mixed_index.append(
                {
                    "round_id": round_id,
                    "unit_id": unit_id,
                    "source_ref": str(dict(bundle["source"]).get("input_file", "")).split("/")[-1],
                    "local_source_range": local_range,
                    "dominant_transition": dominant_transition,
                    "repeated_anchor_support": row["repeated_anchor_support"],
                    "current_mixed_reason": row["why_this_reading"],
                    "readable_excerpt": excerpt,
                }
            )
            detail_packets.append(detail)

            for i, fragment in enumerate(bridge_fragments):
                role = "transition_bridge"
                if i == 0:
                    role = "technical_anchor"
                elif i == len(bridge_fragments) - 1:
                    role = "business_anchor" if transition_to == "business" else "org_anchor"
                bridge_map.append(
                    {
                        "unit_id": unit_id,
                        "round_id": round_id,
                        "fragment_id": fragment["fragment_id"],
                        "bridge_role": role,
                        "incoming_anchor": dominant_anchor_group,
                        "outgoing_anchor": transition_to,
                        "bridge_strength": "medium" if role == "transition_bridge" else "strong",
                        "note": f"{fragment['section_title']} / {fragment['speaker']}",
                    }
                )

            gap_ledger.extend(classify_gap(detail))

    return mixed_index, detail_packets, bridge_map, gap_ledger


def build_cards(mixed_index: list[dict[str, object]], detail_packets: list[dict[str, object]]) -> str:
    detail_map = {(d["round_id"], d["unit_id"]): d for d in detail_packets}
    lines = ["# mixed transition readable cards", ""]
    for row in mixed_index:
        detail = detail_map[(row["round_id"], row["unit_id"])]
        lines.extend(
            [
                f"## {row['round_id']} / {row['unit_id']}",
                f"- excerpt: {row['readable_excerpt']}",
                f"- transition: `{detail['transition_from']} -> {detail['transition_to']}`",
                f"- survived_anchor: `{detail['dominant_anchor_group']}` with repeated support `{detail['repeated_anchor_support']}`",
                f"- broken_or_spread: `{detail['closure_gap_point']}`",
                f"- why_mixed: {detail['why_not_canonical']}",
                f"- why_hold_worth: {detail['why_not_unreadable']}",
                f"- reread point: compare the bridge fragments in `{row['unit_id']}` against the original section flow",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_compare_board(detail_packets: list[dict[str, object]], gap_ledger: list[dict[str, object]]) -> str:
    r1 = [d for d in detail_packets if d["round_id"] == "round1"]
    r2 = [d for d in detail_packets if d["round_id"] == "round2"]
    repeated_gap_types = Counter(g["gap_type"] for g in gap_ledger)
    lines = [
        "# mixed transition compare board",
        "",
        "## round1 mixed vs round2 mixed 공통점",
        "- 두 round 모두 repeated anchor support는 충분하지만 stable closure는 전환부에서 얇아진다.",
        "- 두 round 모두 `technical -> business/organization` 계열 passage가 mixed confirmed_hold로 남는다.",
        "",
        "## 반복되는 전환 패턴",
        "- capability/tool/harness 설명 -> business or org leverage 판단",
        "- product or demo 설명 -> 산업적 의미 or startup thesis",
        "",
        "## 반복되는 closure weakness",
        "- repeated anchor는 strong인데 closure가 transition-led에 머문다.",
        "- source survival은 kept인데 join은 gap_dominant로 남는다.",
        "",
        "## 반복되는 anchor survival 패턴",
        "- harness_agent / model_compute / ai_business / organization_ax 축이 mixed에서도 계속 살아남는다.",
        "",
        "## canonical과 달라지는 경계",
        "- canonical은 straight flow가 길고 전환 설명이 closure를 압도하지 않는다.",
        "- mixed는 bridge는 있지만 그 bridge가 stable reading까지 닫아주지 못한다.",
        "",
        "## 지금 수정해도 되는 것 / 아직 관찰만 할 것",
        "- 지금 수정해도 되는 것: transition-led gap 설명 보강, mixed hold 이유 표기 강화",
        "- 아직 관찰만 할 것: source_local_ref / translated handle 수준 세분 원인 일반화",
        "",
        "## counts",
        f"- round1 mixed units: `{len(r1)}`",
        f"- round2 mixed units: `{len(r2)}`",
        f"- repeated gap types: {dict(repeated_gap_types)}",
    ]
    return "\n".join(lines) + "\n"


def build_fix_boundary_note(gap_ledger: list[dict[str, object]]) -> str:
    lines = [
        "# mixed transition fix boundary note",
        "",
        "## A. 지금 손대도 되는 후보",
        "- transition-led mixed 이유를 workbench/passage 보조면에서 더 직접 표기하는 것",
        "- bridge fragment가 어떤 전환 문장인지 readable card에 더 선명히 드러내는 것",
        "",
        "## B. 아직 관찰만 해야 하는 후보",
        "- source gap과 translation gap이 mixed transcript 전반에서 실제 주원인인지 여부",
        "- good mixed / bad mixed를 더 많은 사례 없이 곧바로 코어 규칙으로 올리는 것",
        "",
        "## C. 코어가 아니라 observer/meaning layer 문제",
        "- hold 이유 표시 부족",
        "- bridge 설명 부족",
        "- report 해상도 부족",
        "",
        "## ledger owner summary",
        f"- {dict(Counter(row['layer_owner'] for row in gap_ledger))}",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    mixed_index, detail_packets, bridge_map, gap_ledger = build_reading_material()
    (OUTPUT_ROOT / "mixed_unit_index.json").write_text(json.dumps(mixed_index, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_transition_detail_packets.json").write_text(json.dumps(detail_packets, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_transition_bridge_map.json").write_text(json.dumps(bridge_map, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_transition_gap_ledger.json").write_text(json.dumps(gap_ledger, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_transition_readable_cards.md").write_text(build_cards(mixed_index, detail_packets), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_transition_compare_board.md").write_text(build_compare_board(detail_packets, gap_ledger), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_transition_fix_boundary_note.md").write_text(build_fix_boundary_note(gap_ledger), encoding="utf-8")
    print(
        json.dumps(
            {
                "mixed_unit_count": len(mixed_index),
                "detail_packet_count": len(detail_packets),
                "bridge_row_count": len(bridge_map),
                "gap_ledger_count": len(gap_ledger),
                "generated_dir": str(OUTPUT_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
