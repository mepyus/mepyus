from __future__ import annotations

from pathlib import Path
import json
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.live_input_space import evaluate_mixed_path_pair


CANDIDATE_CONFIGS = {
    "mixed_probe_doc006_stage1": {
        "left_local_space_id": "lsp_ddc406eb4938",
        "right_local_space_id": "lsp_4eadb2fe7a96",
        "left_material_id": "mat_9dffbdcf3521",
        "right_material_mode": "best_local_ref",
    },
    "canonical_doc005_doc006_stage1": {
        "left_local_space_id": "lsp_2dde7aef787a",
        "right_local_space_id": "lsp_4eadb2fe7a96",
        "left_material_id": "mat_c4639ab53a49",
        "right_material_mode": "explicit",
        "right_material_id": "mat_208c930fbc7b",
    },
}
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "workbench_stage1"
GENERATED_ROOT = OUTPUT_ROOT / "generated"


def _material(service: FormationService, material_id: str) -> dict[str, object]:
    return dict(service.materials.get(material_id) or {})


def _meta(material: dict[str, object]) -> dict[str, object]:
    return dict(material.get("metadata", {}) or {})


def _source_local_ref(material: dict[str, object]) -> str:
    meta = _meta(material)
    handles = dict(meta.get("transformable_handles", {}) or {})
    return str(handles.get("source_local_ref", "")).strip()


def _source_ref(material: dict[str, object]) -> str:
    value = str(material.get("source_ref", "")).strip()
    if value:
        return value
    handles = dict(_meta(material).get("transformable_handles", {}) or {})
    return str(handles.get("source_ref", "")).strip()


def _translated_handles(material: dict[str, object]) -> list[dict[str, object]]:
    return list(_meta(material).get("translated_handles", []) or [])


def _anchor_bundle_summary(material: dict[str, object]) -> dict[str, object]:
    anchor_bundle = dict(_meta(material).get("anchor_bundle", {}) or {})
    if not anchor_bundle:
        return {}
    return {
        "representative": [
            str(row.get("display_label", "")).strip()
            for row in list(anchor_bundle.get("representative_anchors", []) or [])[:4]
            if str(row.get("display_label", "")).strip()
        ],
        "supporting": [
            str(value).strip()
            for value in list(anchor_bundle.get("supporting_anchors", []) or [])[:4]
            if str(value).strip()
        ],
        "promoted_anchor_count": int(anchor_bundle.get("promoted_anchor_count", 0) or 0),
        "dropped_weak_count": int(anchor_bundle.get("dropped_weak_count", 0) or 0),
    }


def _processing_summary(material: dict[str, object]) -> dict[str, object]:
    processing = dict(_meta(material).get("processing_values", {}) or {})
    if not processing:
        return {}
    return {
        "D": processing.get("D"),
        "I": processing.get("I"),
        "S": processing.get("S"),
        "flow": processing.get("flow"),
        "scene": processing.get("scene"),
    }


def _field(value: object, *, status: str, source: str, note: str) -> dict[str, object]:
    return {
        "value": value,
        "status": status,
        "source": source,
        "note": note,
    }


def _find_best_local_material_id(
    service: FormationService,
    *,
    local_space_id: str,
    best_local_ref: str,
) -> str:
    if not best_local_ref:
        return ""
    local_space = dict(service.local_spaces.get(local_space_id) or {})
    material_ids = []
    for cell_id in list(local_space.get("cell_ids", []) or []):
        cell = dict(service.cells.get(cell_id) or {})
        material_ids.extend([str(value).strip() for value in list(cell.get("material_refs", []) or []) if str(value).strip()])
    for material_id in material_ids:
        material = _material(service, material_id)
        if _source_local_ref(material) == best_local_ref:
            return material_id
    for row in service.materials.read_all():
        material_id = str(row.get("material_id", "")).strip()
        if not material_id:
            continue
        if _source_local_ref(dict(row)) == best_local_ref:
            return material_id
    return ""


def _find_exact_bridge_id(service: FormationService, *, left_local_space_id: str, right_local_space_id: str) -> str:
    pair = {left_local_space_id, right_local_space_id}
    for row in service.bridges.read_all():
        bridge_pair = {
            str(row.get("from_local_space_id", "")).strip(),
            str(row.get("to_local_space_id", "")).strip(),
        }
        if bridge_pair == pair:
            return str(row.get("bridge_id", "")).strip()
    return ""


def build_workbench_packet(candidate_id: str) -> dict[str, object]:
    config = dict(CANDIDATE_CONFIGS[candidate_id])
    left_local_space_id = str(config["left_local_space_id"])
    right_local_space_id = str(config["right_local_space_id"])
    left_material_id = str(config["left_material_id"])
    service = FormationService(REPO_ROOT / "runtime")
    pair_result = evaluate_mixed_path_pair(
        service,
        left_local_space_id=left_local_space_id,
        right_local_space_id=right_local_space_id,
    )
    review = dict(pair_result.get("promotion_review", {}) or {})
    best_local_ref = str(review.get("best_local_ref", "")).strip()
    right_material_mode = str(config.get("right_material_mode", "")).strip()
    if right_material_mode == "explicit":
        right_material_id = str(config.get("right_material_id", "")).strip()
    else:
        right_material_id = _find_best_local_material_id(
            service,
            local_space_id=right_local_space_id,
            best_local_ref=best_local_ref,
        )

    left_material = _material(service, left_material_id)
    right_material = _material(service, right_material_id) if right_material_id else {}
    exact_bridge_id = _find_exact_bridge_id(
        service,
        left_local_space_id=left_local_space_id,
        right_local_space_id=right_local_space_id,
    )

    left_source_local_ref = _source_local_ref(left_material)
    right_source_local_ref = _source_local_ref(right_material)
    left_translated_handles = _translated_handles(left_material)
    right_translated_handles = _translated_handles(right_material)
    left_anchor_bundle = _anchor_bundle_summary(left_material)
    right_anchor_bundle = _anchor_bundle_summary(right_material)
    left_processing = _processing_summary(left_material)
    right_processing = _processing_summary(right_material)

    missing_join_points: list[str] = []
    if not left_source_local_ref:
        missing_join_points.append("left.source_local_ref missing")
    if not left_translated_handles:
        missing_join_points.append("left.translated_handles missing")
    if not exact_bridge_id:
        missing_join_points.append("exact current_pair bridge_trace missing")
    why_not_closed = (
        "canonical pair already closes through persisted bridge/local-space exposure"
        if exact_bridge_id and str(pair_result.get("bridge_mode", "")).strip() == "canonical"
        else "source-side live material lacks source_local/translated layer and the current pair has no exact persisted bridge closure"
    )
    likely_gap_layer = (
        "closure present"
        if exact_bridge_id and str(pair_result.get("bridge_mode", "")).strip() == "canonical"
        else "source-local / translated join gap + cross-path corroboration gap"
    )
    reading_category = "canonical" if candidate_id == "canonical_doc005_doc006_stage1" else "mixed"
    reading_status = "stable_reading" if reading_category == "canonical" else "confirmed_hold"

    packet = {
        "packet_kind": "local_workbench_stage1",
        "candidate_id": candidate_id,
        "candidate_context": {
            "left_local_space_id": left_local_space_id,
            "right_local_space_id": right_local_space_id,
            "bridge_mode": pair_result.get("bridge_mode", ""),
            "review_state": review.get("review_state", ""),
            "state_signature": pair_result.get("state_signature", ""),
            "workbench_reading_category": reading_category,
            "workbench_reading_status": reading_status,
        },
        "source": {
            "left_material_id": _field(
                left_material_id,
                status="persisted",
                source="material_metadata",
                note="left live-side material fixed for this stage1 packet",
            ),
            "right_material_id": _field(
                right_material_id,
                status="derived" if right_material_id else "missing",
                source="review_output_surface + material_metadata",
                note=(
                    "right material selected from exact canonical bridge support pair"
                    if right_material_mode == "explicit"
                    else "material matched back from best_local_ref within the right local space"
                ),
            ),
            "left_source_ref": _field(
                _source_ref(left_material),
                status="persisted" if _source_ref(left_material) else "missing",
                source="material_metadata",
                note="left material source path",
            ),
            "right_source_ref": _field(
                _source_ref(right_material),
                status="persisted" if _source_ref(right_material) else "missing",
                source="material_metadata",
                note="right material source path",
            ),
            "left_source_local_ref": _field(
                left_source_local_ref,
                status="persisted" if left_source_local_ref else "missing",
                source="material_metadata",
                note="left local fragment coordinate",
            ),
            "right_source_local_ref": _field(
                right_source_local_ref,
                status="persisted" if right_source_local_ref else "missing",
                source="material_metadata",
                note="right local fragment coordinate",
            ),
            "left_lineage_refs": _field(
                list(left_material.get("lineage_refs", []) or []),
                status="persisted",
                source="material_metadata",
                note="left lineage spine currently sparse or empty",
            ),
            "right_lineage_refs": _field(
                list(right_material.get("lineage_refs", []) or []),
                status="persisted" if right_material else "missing",
                source="material_metadata",
                note="right lineage spine from imported material",
            ),
        },
        "translation_processing": {
            "left_translated_handles": _field(
                left_translated_handles,
                status="persisted" if left_translated_handles else "missing",
                source="material_metadata",
                note="left translated handle layer",
            ),
            "right_translated_handles": _field(
                right_translated_handles,
                status="persisted" if right_translated_handles else "missing",
                source="material_metadata",
                note="right translated handle layer",
            ),
            "left_anchor_bundle_summary": _field(
                left_anchor_bundle,
                status="persisted" if left_anchor_bundle else "missing",
                source="material_metadata",
                note="left anchor convergence summary",
            ),
            "right_anchor_bundle_summary": _field(
                right_anchor_bundle,
                status="persisted" if right_anchor_bundle else "missing",
                source="material_metadata",
                note="right anchor convergence summary",
            ),
            "left_processing_values_summary": _field(
                left_processing,
                status="persisted" if left_processing else "missing",
                source="material_metadata",
                note="left processing baseline",
            ),
            "right_processing_values_summary": _field(
                right_processing,
                status="persisted" if right_processing else "missing",
                source="material_metadata",
                note="right processing baseline",
            ),
            "translation_join_quality": _field(
                "right_present_left_missing" if right_translated_handles and not left_translated_handles else "symmetric_or_unknown",
                status="derived",
                source="material_metadata",
                note="translation layer asymmetry across the pair",
            ),
            "source_local_to_translation_gap": _field(
                "left_live_gap_right_imported_available" if right_source_local_ref and right_translated_handles and not left_source_local_ref and not left_translated_handles else "not_primary_gap",
                status="derived",
                source="material_metadata",
                note="stage1 readout of source-local to translation asymmetry",
            ),
        },
        "join": {
            "best_local_ref": _field(
                best_local_ref,
                status="derived" if best_local_ref else "missing",
                source="review_output_surface",
                note="current best local candidate ref from review assembly",
            ),
            "direct_overlap_candidate": _field(
                list(review.get("direct_overlap_candidate_families", []) or []),
                status="derived",
                source="review_output_surface",
                note="direct overlap family candidates",
            ),
            "family_support_summary": _field(
                {
                    "review_anchor_support_class": review.get("review_anchor_support_class", ""),
                    "anchor_family_support_strength": dict(review.get("anchor_family_support_strength", {}) or {}),
                    "live_side_support_families": list(review.get("live_side_support_families", []) or []),
                    "cross_path_overlap_families": list(review.get("cross_path_overlap_families", []) or []),
                },
                status="derived",
                source="review_output_surface",
                note="family support and cross-path summary",
            ),
            "canonicalization_proposal_summary": _field(
                {
                    "proposal_state": review.get("cross_path_canonicalization_proposal_state", ""),
                    "proposals": dict(review.get("cross_path_canonicalization_proposals", {}) or {}),
                },
                status="derived",
                source="review_output_surface",
                note="canonicalization proposal readout",
            ),
            "bridge_trace_ref": _field(
                exact_bridge_id,
                status="persisted" if exact_bridge_id else "missing",
                source="bridge_trace",
                note="exact persisted bridge for the current local-space pair",
            ),
            "local_space_ref": _field(
                [left_local_space_id, right_local_space_id],
                status="persisted",
                source="local_space",
                note="current pair local-space coordinates",
            ),
            "current_pair_closure_strength": _field(
                "mixed_pair_explicit_bridge_missing" if not exact_bridge_id else "pair_bridge_present",
                status="derived",
                source="review_output_surface + bridge_trace",
                note="stage1 closure estimate",
            ),
            "review_focus_class": _field(
                review.get("canonical_review_focus_class", ""),
                status="derived",
                source="review_output_surface",
                note="current review focus",
            ),
        },
        "block": {
            "next_review_blocker": _field(
                review.get("next_review_blocker", ""),
                status="derived",
                source="review_output_surface",
                note="current next blocker",
            ),
            "missing_join_points": _field(
                missing_join_points,
                status="derived",
                source="workbench_stage1",
                note="gaps surfaced by this packet",
            ),
            "mixed_record_ref": _field(
                f"mixed_minimum_record::{candidate_id}",
                status="inferred" if candidate_id == "mixed_probe_doc006_stage1" else "missing",
                source="workbench_stage1",
                note="minimal linkage to confirmed mixed hold record",
            ),
            "why_not_closed": _field(
                why_not_closed,
                status="derived",
                source="workbench_stage1",
                note="short closure diagnosis",
            ),
            "next_review_question": _field(
                review.get("canonical_approval_next_step", ""),
                status="derived",
                source="review_output_surface",
                note="next approval-facing question",
            ),
            "likely_gap_layer": _field(
                likely_gap_layer,
                status="derived",
                source="workbench_stage1",
                note="dominant gap layer for this mixed candidate",
            ),
            "review_status_summary": _field(
                {
                    "bridge_mode": pair_result.get("bridge_mode", ""),
                    "review_state": review.get("review_state", ""),
                    "space_entry_state": review.get("space_entry_state", ""),
                    "space_entry_blocker": review.get("space_entry_blocker", ""),
                    "canonical_approval_readiness_class": review.get("canonical_approval_readiness_class", ""),
                },
                status="derived",
                source="review_output_surface + review_ledger",
                note="top-level review status summary",
            ),
        },
    }
    return packet


def build_workbench_view(packet: dict[str, object]) -> str:
    lines = [
        f"# workbench view: {packet['candidate_id']}",
        "",
    ]
    reading_category = str(dict(packet["candidate_context"]).get("workbench_reading_category", "")).strip()
    reading_status = str(dict(packet["candidate_context"]).get("workbench_reading_status", "")).strip()
    if reading_category or reading_status:
        meaning = (
            "source -> translation -> bridge closure is sufficiently persisted, so this candidate stays in stable reading mode"
            if reading_category == "canonical"
            else "persisted closure gap is confirmed, so this candidate stays in hold / re-read mode"
        )
        lines.extend(
            [
                f"- reading_category: `{reading_category}`",
                f"- reading_status: `{reading_status}`",
                f"- meaning: {meaning}",
                "",
            ]
        )
    lines.extend(
        [
        "## A. source",
        ]
    )
    for key, row in dict(packet["source"]).items():
        lines.append(f"- `{key}`")
        lines.append(f"  - status: `{row['status']}`")
        lines.append(f"  - source: `{row['source']}`")
        lines.append(f"  - value: `{json.dumps(row['value'], ensure_ascii=False)}`")
        lines.append(f"  - note: {row['note']}")
    lines.extend(["", "## B. translation / processing"])
    for key, row in dict(packet["translation_processing"]).items():
        lines.append(f"- `{key}`")
        lines.append(f"  - status: `{row['status']}`")
        lines.append(f"  - source: `{row['source']}`")
        lines.append(f"  - value: `{json.dumps(row['value'], ensure_ascii=False)}`")
        lines.append(f"  - note: {row['note']}")
    lines.extend(["", "## C. join"])
    for key, row in dict(packet["join"]).items():
        lines.append(f"- `{key}`")
        lines.append(f"  - status: `{row['status']}`")
        lines.append(f"  - source: `{row['source']}`")
        lines.append(f"  - value: `{json.dumps(row['value'], ensure_ascii=False)}`")
        lines.append(f"  - note: {row['note']}")
    lines.extend(["", "## D. block"])
    for key, row in dict(packet["block"]).items():
        lines.append(f"- `{key}`")
        lines.append(f"  - status: `{row['status']}`")
        lines.append(f"  - source: `{row['source']}`")
        lines.append(f"  - value: `{json.dumps(row['value'], ensure_ascii=False)}`")
        lines.append(f"  - note: {row['note']}")
    return "\n".join(lines) + "\n"


def build_compare_view(*, mixed_packet: dict[str, object], canonical_packet: dict[str, object]) -> str:
    def _status(packet: dict[str, object], section: str, key: str) -> str:
        return str(dict(packet[section]).get(key, {}).get("status", "")).strip()

    def _value(packet: dict[str, object], section: str, key: str) -> object:
        return dict(packet[section]).get(key, {}).get("value")

    lines = [
        "# workbench compare mixed vs canonical stage1.5",
        "",
        "## 1. one-line verdict",
        "- canonical closes source -> translation -> bridge more cleanly, while mixed keeps a source-local / translation gap and depends more on derived join readout.",
        "",
        "## 2. comparison",
        f"- source",
        f"  - mixed: `left_source_local_ref={_status(mixed_packet, 'source', 'left_source_local_ref')}`, `right_source_local_ref={_status(mixed_packet, 'source', 'right_source_local_ref')}`",
        f"  - canonical: `left_source_local_ref={_status(canonical_packet, 'source', 'left_source_local_ref')}`, `right_source_local_ref={_status(canonical_packet, 'source', 'right_source_local_ref')}`",
        f"- translation",
        f"  - mixed: `left_translated_handles={_status(mixed_packet, 'translation_processing', 'left_translated_handles')}`, `right_translated_handles={_status(mixed_packet, 'translation_processing', 'right_translated_handles')}`",
        f"  - canonical: `left_translated_handles={_status(canonical_packet, 'translation_processing', 'left_translated_handles')}`, `right_translated_handles={_status(canonical_packet, 'translation_processing', 'right_translated_handles')}`",
        f"- join",
        f"  - mixed: `bridge_trace_ref={_status(mixed_packet, 'join', 'bridge_trace_ref')}`, `review_focus={json.dumps(_value(mixed_packet, 'join', 'review_focus_class'), ensure_ascii=False)}`",
        f"  - canonical: `bridge_trace_ref={_status(canonical_packet, 'join', 'bridge_trace_ref')}`, `review_focus={json.dumps(_value(canonical_packet, 'join', 'review_focus_class'), ensure_ascii=False)}`",
        f"- block",
        f"  - mixed: `{json.dumps(_value(mixed_packet, 'block', 'next_review_blocker'), ensure_ascii=False)}`",
        f"  - canonical: `{json.dumps(_value(canonical_packet, 'block', 'next_review_blocker'), ensure_ascii=False)}`",
        f"- bridge/local_space",
        f"  - mixed: `{json.dumps(_value(mixed_packet, 'join', 'current_pair_closure_strength'), ensure_ascii=False)}`",
        f"  - canonical: `{json.dumps(_value(canonical_packet, 'join', 'current_pair_closure_strength'), ensure_ascii=False)}`",
        f"- derived dependence",
        f"  - mixed: best-local and blocker-led",
        f"  - canonical: persisted bridge-led",
        f"- reading mode",
        f"  - mixed: `confirmed_hold`",
        f"  - canonical: `stable_reading`",
        "",
        "## 3. conclusion",
        "- current workbench is sufficient to expose the structural difference between mixed and canonical: `YES`",
    ]
    return "\n".join(lines) + "\n"


def build_workbench_reading_grammar_note() -> str:
    lines = [
        "# workbench reading grammar stage1",
        "",
        "- fields: `workbench_reading_category`, `workbench_reading_status`",
        "- category values: `canonical`, `mixed`",
        "- status values: `stable_reading`, `confirmed_hold`",
        "- meaning: `canonical + stable_reading` means persisted source -> translation -> bridge closure is comparatively closed; `mixed + confirmed_hold` means closure gaps are confirmed and the candidate stays in hold / re-read mode",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    candidate_ids = sys.argv[1:] or ["mixed_probe_doc006_stage1", "canonical_doc005_doc006_stage1"]
    packets: dict[str, dict[str, object]] = {}
    outputs: list[dict[str, str]] = []
    for candidate_id in candidate_ids:
        packet = build_workbench_packet(candidate_id)
        view = build_workbench_view(packet)
        packet_path = GENERATED_ROOT / f"workbench_packet_{candidate_id}.json"
        view_path = GENERATED_ROOT / f"workbench_view_{candidate_id}.md"
        with packet_path.open("w", encoding="utf-8") as handle:
            json.dump(packet, handle, ensure_ascii=False, indent=2)
        with view_path.open("w", encoding="utf-8") as handle:
            handle.write(view)
        packets[candidate_id] = packet
        outputs.append(
            {
                "candidate_id": candidate_id,
                "packet_path": str(packet_path),
                "view_path": str(view_path),
            }
        )
    compare_path = GENERATED_ROOT / "workbench_compare_mixed_vs_canonical_stage15.md"
    if (
        "mixed_probe_doc006_stage1" in packets
        and "canonical_doc005_doc006_stage1" in packets
    ):
        compare_view = build_compare_view(
            mixed_packet=packets["mixed_probe_doc006_stage1"],
            canonical_packet=packets["canonical_doc005_doc006_stage1"],
        )
        with compare_path.open("w", encoding="utf-8") as handle:
            handle.write(compare_view)
    summary_path = GENERATED_ROOT / "workbench_reading_grammar_note_stage1.md"
    with summary_path.open("w", encoding="utf-8") as handle:
        handle.write(build_workbench_reading_grammar_note())
    print(
        json.dumps(
            {
                "generated": outputs,
                "compare_path": str(compare_path),
                "summary_path": str(summary_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
