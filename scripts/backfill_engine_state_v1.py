from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Dict, List


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.models.entities import EngineStateRecord, SupportRef
from app.core.state_store import EngineStateStore
from app.core.states import (
    CarryoverRisk,
    ComparisonMemoryReason,
    EmergenceStatus,
    GateBlockerSummary,
    GroundingStatus,
    MaturationState,
    PacketTexture,
    TraceabilityStatus,
    UpdateTriggerType,
)

RUNTIME_ROOT = REPO_ROOT / "runtime"
REPORT_PATH = REPO_ROOT / "docs" / "reports" / "engine_state_backfill_v1_report.md"


def _support(ref_kind: str, ref_id: str, note: str | None = None) -> SupportRef:
    return SupportRef(ref_kind=ref_kind, ref_id=ref_id, note=note)


def representative_records() -> Dict[str, EngineStateRecord]:
    return {
        "youtube_03_22": EngineStateRecord(
            asset_id="youtube_03_22",
            asset_name="youtube_03_22",
            source_type="dialogue_asset",
            packet_texture=PacketTexture.MODERATELY_OPEN,
            grounding_status=GroundingStatus.PARTIALLY_GROUNDED,
            emergence_status=EmergenceStatus.QUESTION_OPENING_PRESENT,
            carryover_risk=CarryoverRisk.MEDIUM,
            maturation_state=MaturationState.BREATHING,
            traceability_status=TraceabilityStatus.TRACEABLE,
            comparison_memory_reason=(
                ComparisonMemoryReason.BREATHING_CONTRAST,
            ),
            gate_blocker_summary=(
                GateBlockerSummary.SCAFFOLD_CARRYOVER_RISK,
            ),
            state_notes="Process-console trace is strong and packet breathes, but second-order institutions still show some prepared dialogue scaffold carryover.",
            evidence_refs=(
                _support("report", "docs/reports/youtube_03_22_process_trace_validation_v1.md"),
                _support("report", "docs/reports/asset_wise_memory_packet_texture_comparison_v1.md"),
            ),
            experimental_namespace={
                "context_unit_candidates_ref": "app/work/dialogue_loop_test/generated/context_unit_candidates_20260328T071836Z.json",
                "question_inducing_candidate_present": True,
            },
        ),
        "openai_02_11": EngineStateRecord(
            asset_id="openai_02_11",
            asset_name="openai_02_11",
            source_type="structured_markdown_asset",
            packet_texture=PacketTexture.STRUCTURED_OPEN_LOW_EMERGENCE,
            grounding_status=GroundingStatus.FALLBACK_GROUNDED,
            emergence_status=EmergenceStatus.LOW_EMERGENCE,
            carryover_risk=CarryoverRisk.MEDIUM,
            maturation_state=MaturationState.HOLD,
            traceability_status=TraceabilityStatus.TRACEABLE,
            comparison_memory_reason=(
                ComparisonMemoryReason.SAME_FALLBACK_DOMINANCE,
                ComparisonMemoryReason.SIMILAR_GROUNDING_FAILURE_SURFACE,
            ),
            gate_blocker_summary=(
                GateBlockerSummary.QUESTION_INDUCING_CANDIDATE_ABSENCE,
                GateBlockerSummary.FALLBACK_GROUNDING_DOMINANCE,
                GateBlockerSummary.WEAK_ROLE_LIKE_ONLY,
                GateBlockerSummary.PIVOT_COMPRESSION_NON_RECURRENCE,
            ),
            state_notes="Trace is stable and reusable attitudes survive, but emergence stays low and grounding remains fallback-dominant.",
            evidence_refs=(
                _support("report", "docs/reports/openai_02_11_process_trace_validation_v1.md"),
                _support("report", "docs/reports/openai_02_11_next_loop_gate_validation_v1.md"),
            ),
            experimental_namespace={
                "context_unit_candidates_ref": "app/work/dialogue_loop_test/generated/openai_02_11_context_unit_candidates_v1_20260328.json",
                "question_inducing_candidate_count": 0,
            },
        ),
        "knowledge_editing_youtube": EngineStateRecord(
            asset_id="knowledge_editing_youtube",
            asset_name="knowledge_editing_youtube",
            source_type="dialogue_asset",
            packet_texture=PacketTexture.OVERCOMPRESSED_CLOSURE_HEAVY,
            grounding_status=GroundingStatus.EMPTY_REF_RISK,
            emergence_status=EmergenceStatus.NO_EMERGENCE,
            carryover_risk=CarryoverRisk.PREPARED_SCAFFOLD_CARRYOVER,
            maturation_state=MaturationState.BLOCKED,
            traceability_status=TraceabilityStatus.TRACEABLE,
            comparison_memory_reason=(
                ComparisonMemoryReason.SAME_COMPRESSED_FAMILY,
                ComparisonMemoryReason.SAME_FALLBACK_DOMINANCE,
                ComparisonMemoryReason.SIMILAR_CARRYOVER_PATTERN,
            ),
            gate_blocker_summary=(
                GateBlockerSummary.QUESTION_INDUCING_CANDIDATE_ABSENCE,
                GateBlockerSummary.FALLBACK_GROUNDING_DOMINANCE,
                GateBlockerSummary.WEAK_ROLE_LIKE_ONLY,
                GateBlockerSummary.SCAFFOLD_CARRYOVER_RISK,
            ),
            state_notes="Bridge is confirmed, but packet is overcompressed and closure-heavy, with empty-ref tendency and strong scaffold carryover.",
            evidence_refs=(
                _support("report", "docs/reports/knowledge_editing_youtube_process_trace_validation_v1.md"),
                _support("report", "docs/reports/asset_wise_memory_packet_texture_comparison_v1.md"),
            ),
            experimental_namespace={
                "paragraph_role_ref": "app/work/dialogue_loop_test/generated/paragraph_role_interpretation_knowledge_editing_youtube_v1_20260328.json",
                "question_inducing_candidate_count": 0,
            },
        ),
        "gary_tan_brain": EngineStateRecord(
            asset_id="gary_tan_brain",
            asset_name="gary_tan_brain",
            source_type="dialogue_asset",
            packet_texture=PacketTexture.OVERCOMPRESSED_BREATHING,
            grounding_status=GroundingStatus.FALLBACK_GROUNDED,
            emergence_status=EmergenceStatus.MINIMAL_EMERGENCE,
            carryover_risk=CarryoverRisk.HIGH,
            maturation_state=MaturationState.BREATHING,
            traceability_status=TraceabilityStatus.TRACEABLE,
            comparison_memory_reason=(
                ComparisonMemoryReason.BREATHING_CONTRAST,
                ComparisonMemoryReason.SAME_COMPRESSED_FAMILY,
            ),
            gate_blocker_summary=(
                GateBlockerSummary.FALLBACK_GROUNDING_DOMINANCE,
                GateBlockerSummary.WEAK_ROLE_LIKE_ONLY,
                GateBlockerSummary.SCAFFOLD_CARRYOVER_RISK,
            ),
            state_notes="Packet is still compressed, but it breathes enough to show minimal non-zero emergence while second-order carryover remains visible.",
            evidence_refs=(
                _support("report", "docs/reports/gary_tan_brain_process_trace_validation_v1.md"),
                _support("report", "docs/reports/asset_wise_memory_packet_texture_comparison_v1.md"),
            ),
            experimental_namespace={
                "paragraph_role_ref": "app/work/dialogue_loop_test/generated/paragraph_role_interpretation_gary_tan_brain_v1_20260328.json",
                "question_inducing_candidate_count": 1,
            },
        ),
    }


def _record_to_dict(record: EngineStateRecord) -> Dict[str, object]:
    return {
        "asset_id": record.asset_id,
        "asset_name": record.asset_name,
        "source_type": record.source_type,
        "packet_texture": record.packet_texture.value,
        "grounding_status": record.grounding_status.value,
        "emergence_status": record.emergence_status.value,
        "carryover_risk": record.carryover_risk.value,
        "maturation_state": record.maturation_state.value,
        "traceability_status": record.traceability_status.value,
        "comparison_memory_reason": [entry.value for entry in record.comparison_memory_reason],
        "gate_blocker_summary": [entry.value for entry in record.gate_blocker_summary],
        "state_notes": record.state_notes,
        "evidence_refs": [
            {"ref_kind": ref.ref_kind, "ref_id": ref.ref_id, "note": ref.note}
            for ref in record.evidence_refs
        ],
        "experimental_namespace": record.experimental_namespace,
        "updated_at": record.updated_at,
    }


def write_report(records: List[EngineStateRecord]) -> None:
    lines: List[str] = []
    lines.append("[[A]] [[OBJ:engine_state_backfill_v1_report]] [[SEM:report_for_canonical_engine_state_backfill_across_representative_assets]]")
    lines.append("")
    lines.append("# engine_state_backfill_v1_report")
    lines.append("")
    lines.append("## 1. purpose")
    lines.append("")
    lines.append("- 이번 report의 목적은 representative asset에 `engine_state_schema_v1`를 실제로 붙여 repeatability를 검증하는 것이다.")
    lines.append("- 이번 단계의 canonicalization 대상은 상위 의미 객체가 아니라 operating state field다.")
    lines.append("")
    lines.append("## 2. per-asset records")
    lines.append("")
    for record in records:
        lines.append(f"### {record.asset_id}")
        lines.append("")
        lines.append(f"- asset_id: `{record.asset_id}`")
        lines.append(f"- packet_texture: `{record.packet_texture.value}`")
        lines.append(f"- grounding_status: `{record.grounding_status.value}`")
        lines.append(f"- emergence_status: `{record.emergence_status.value}`")
        lines.append(f"- carryover_risk: `{record.carryover_risk.value}`")
        lines.append(f"- maturation_state: `{record.maturation_state.value}`")
        lines.append(f"- traceability_status: `{record.traceability_status.value}`")
        lines.append(f"- comparison_memory_reason: `{', '.join(entry.value for entry in record.comparison_memory_reason)}`")
        lines.append(f"- gate_blocker_summary: `{', '.join(entry.value for entry in record.gate_blocker_summary)}`")
        lines.append(f"- why this state: {record.state_notes}")
        lines.append("- experimental namespace values:")
        for key, value in record.experimental_namespace.items():
            lines.append(f"  - `{key}`: `{value}`")
        lines.append("- evidence refs:")
        for ref in record.evidence_refs:
            lines.append(f"  - `{ref.ref_kind}` -> `{ref.ref_id}`")
        lines.append("")
    lines.append("## 3. overall read")
    lines.append("")
    lines.append("- schema fit was stable across representative assets.")
    lines.append("- 가장 안정적인 field는 `packet_texture`, `grounding_status`, `traceability_status`, `maturation_state`였다.")
    lines.append("- 가장 해석 흔들림이 남는 field는 `emergence_status`와 `carryover_risk`였다.")
    lines.append("- `context unit`, `paragraph role`, `high-level naming`은 canonical field에 올리지 않고 experimental namespace로 밀어낸 것이 repeatability를 지키는 데 중요했다.")
    lines.append("")
    lines.append("## 4. one-line verdict")
    lines.append("")
    lines.append("> representative asset 4개에 `engine_state_schema_v1`를 무리 없이 붙일 수 있었고, 현재 엔진이 먼저 canonicalize해야 하는 것은 상위 의미 객체가 아니라 process-console operating state라는 점이 다시 확인됐다.")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--asset-id", action="append", dest="asset_ids", default=[])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    candidates = representative_records()
    selected_ids = args.asset_ids or list(candidates.keys())
    records = [candidates[asset_id] for asset_id in selected_ids]

    if args.dry_run:
        payload = [_record_to_dict(record) for record in records]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    store = EngineStateStore(RUNTIME_ROOT)
    for record in records:
        store.append_state(
            record,
            trigger_type=UpdateTriggerType.BACKFILL,
            update_reason="representative_asset_backfill_v1",
        )
    write_report(records)
    print(json.dumps({"backfilled_asset_ids": selected_ids, "report": str(REPORT_PATH.relative_to(REPO_ROOT))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
