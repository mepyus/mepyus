from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

from app.core.runtime.context_linked_segmentation import ContextLinkedSegmenter, Segment
from app.core.runtime.multi_lens_document_reading import MultiLensDocumentReader


def build_multi_lens_observation_payload(
    *,
    split_units_path: Path,
    source_id: str,
    registry_path: Path,
    observer_run_id: str,
) -> dict[str, Any]:
    segmenter = ContextLinkedSegmenter()
    reader = MultiLensDocumentReader(str(registry_path))
    segments = _segments_from_split_units(
        split_units_path=split_units_path,
        source_id=source_id,
        observer_run_id=observer_run_id,
    )
    linked_segments = segmenter.link(segments)
    raw_result = reader.read(linked_segments)
    surfaced = reader.surface_readout(raw_result)
    return {
        "kind": "multi_lens_document_reading_v0_observation_flow",
        "source_id": source_id,
        "observer_run_id": observer_run_id,
        "split_units_path": str(split_units_path),
        "invocation_stage": "after_context_linked_segmentation_v0",
        "linked_segments": [asdict(item) for item in linked_segments],
        "raw_reading_result": asdict(raw_result),
        "surfaced_readout": asdict(surfaced),
        "parked_axes": [
            line_id
            for line_id, state in surfaced.line_states.items()
            if state == "parked"
        ],
        "handoff_boundary": {
            "runtime_stops_after": "surfaced_readout",
            "next_owner": "supervisor_docs_operating_loop",
            "decision_logic_in_runtime": False,
        },
    }


def build_multi_lens_supervisor_surface(
    observation_payload: dict[str, Any],
    *,
    observation_artifact_ref: str,
) -> dict[str, Any]:
    surfaced_readout = observation_payload["surfaced_readout"]
    return {
        "kind": "multi_lens_document_reading_v0_supervisor_surface",
        "source_id": observation_payload["source_id"],
        "observer_run_id": observation_payload["observer_run_id"],
        "invocation_stage": observation_payload["invocation_stage"],
        "primary_view": surfaced_readout,
        "line_states": surfaced_readout["line_states"],
        "parked_axes": observation_payload["parked_axes"],
        "handoff_boundary": observation_payload["handoff_boundary"],
        "raw_output_reference": observation_artifact_ref,
        "surface_rule": {
            "primary_view_kind": "surfaced_readout",
            "raw_output_role": "secondary_reference_only",
            "observation_only": True,
            "decision_surface": False,
            "maturity_surface": False,
        },
    }


def _segments_from_split_units(
    *,
    split_units_path: Path,
    source_id: str,
    observer_run_id: str,
) -> list[Segment]:
    import json

    payload = json.loads(split_units_path.read_text(encoding="utf-8"))
    segments: list[Segment] = []
    for index, unit in enumerate(payload):
        segments.append(
            Segment(
                segment_id=str(unit.get("unit_id", f"unit_{index:03d}")),
                source_id=source_id,
                text=str(unit.get("text_excerpt", "")),
                order_index=index,
                start_anchor=str(unit.get("start_ref", "")),
                end_anchor=str(unit.get("end_ref", "")),
                speaker_id=None,
                segment_type=str(unit.get("unit_type", "")) or None,
                provenance={
                    "kind": "observer_ingest_split_unit",
                    "observer_run_id": observer_run_id,
                    "split_units_path": str(split_units_path),
                    "source_segment_ids": list(unit.get("source_segment_ids", [])),
                },
            )
        )
    return segments
