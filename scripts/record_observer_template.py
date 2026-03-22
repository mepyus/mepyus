#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.fragment.store import FragmentStore
from app.measurement import MeasurementStore, build_connection_observation, build_revision_judgment


def _find(store: FragmentStore, fragment_id: str):
    fragment = store.get(fragment_id)
    if fragment is None:
        raise SystemExit(f"missing fragment: {fragment_id}")
    return fragment


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: record_observer_template.py <runtime_root> <observer_template.json>")
        return 1

    runtime_root = Path(sys.argv[1]).resolve()
    template_path = Path(sys.argv[2]).resolve()
    payload = json.loads(template_path.read_text(encoding="utf-8"))

    fragment_store = FragmentStore(runtime_root)
    measurement_store = MeasurementStore(runtime_root)
    created_ids = []

    for row in payload.get("revision_judgments", []):
        fragment = _find(fragment_store, row["fragment_id"])
        measurement = build_revision_judgment(
            fragment_id=fragment.fragment_id,
            source_id=fragment.source_id,
            column_key=row["column_key"],
            previous_value=row.get("previous_value", {}),
            new_value=row.get("new_value", {}),
            reason=row.get("reason", ""),
            reason_family=row.get("reason_family", ""),
            operator=row.get("operator", "reviewer"),
            batch_id=str(fragment.metadata.get("ingest_batch_id", "")),
            session_id=str(fragment.metadata.get("ingest_session_id", "")),
            related_measurement_id=row.get("related_measurement_id", ""),
            notes=row.get("notes", ""),
            confidence=float(row.get("confidence", 0.8)),
        )
        measurement_store.put(measurement)
        created_ids.append(measurement.measurement_id)

    for row in payload.get("connection_observations", []):
        fragment = _find(fragment_store, row["fragment_id"])
        counterpart = _find(fragment_store, row["counterpart_fragment_id"])
        measurement = build_connection_observation(
            fragment_id=fragment.fragment_id,
            counterpart_fragment_id=counterpart.fragment_id,
            source_id=fragment.source_id,
            counterpart_source_id=counterpart.source_id,
            relation_status=row["relation_status"],
            reason=row.get("reason", ""),
            reason_family=row.get("reason_family", ""),
            shared_signals=row.get("shared_signals", []),
            missing_signals=row.get("missing_signals", []),
            operator=row.get("operator", "reviewer"),
            batch_id=str(fragment.metadata.get("ingest_batch_id", "")),
            session_id=str(fragment.metadata.get("ingest_session_id", "")),
            notes=row.get("notes", ""),
            confidence=float(row.get("confidence", 0.45)),
        )
        measurement_store.put(measurement)
        created_ids.append(measurement.measurement_id)

    print("recorded observer template")
    print(json.dumps({"count": len(created_ids), "measurement_ids": created_ids}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
