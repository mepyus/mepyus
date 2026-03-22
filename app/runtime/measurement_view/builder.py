from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, List
import json

from app.measurement import MeasurementStore
from app.runtime.measurement_view.render import render_measurement_view_html


def build_measurement_view_data(runtime_root: Path) -> Dict[str, object]:
    store = MeasurementStore(runtime_root)
    rows = [measurement.to_record() for measurement in store.read_all()]
    grouped: Dict[str, List[dict]] = defaultdict(list)
    batches: Dict[str, List[dict]] = defaultdict(list)

    for row in rows:
        grouped[row["measurement_type"]].append(row)
        metadata = row.get("metadata") or {}
        batches[metadata.get("ingest_batch_id", "unbatched")].append(row)

    groups = []
    for measurement_type, entries in sorted(grouped.items()):
        entries.sort(key=lambda row: (row.get("fragment_id", ""), row.get("column_key", ""), row.get("recorded_at", "")))
        groups.append(
            {
                "measurement_type": measurement_type,
                "count": len(entries),
                "records": entries,
            }
        )

    batch_groups = []
    def _batch_sort_key(item: tuple) -> tuple:
        batch_id = item[0]
        return (batch_id == "unbatched", batch_id)

    for batch_id, entries in sorted(batches.items(), key=_batch_sort_key):
        entries.sort(key=lambda row: (row.get("recorded_at", ""), row.get("fragment_id", ""), row.get("column_key", "")), reverse=True)
        batch_groups.append(
            {
                "ingest_batch_id": batch_id,
                "count": len(entries),
                "measurement_types": sorted({row.get("measurement_type", "") for row in entries if row.get("measurement_type")}),
                "session_ids": sorted({((row.get("metadata") or {}).get("ingest_session_id", "")) for row in entries if ((row.get("metadata") or {}).get("ingest_session_id", ""))}),
                "records": entries[:20],
            }
        )

    return {
        "summary": {
            "measurement_count": len(rows),
            "measurement_type_count": len(groups),
            "ingest_batch_count": len(batch_groups),
        },
        "groups": groups,
        "batches": batch_groups,
    }


def write_measurement_view(runtime_root: Path) -> Dict[str, Path]:
    data = build_measurement_view_data(runtime_root)
    reports_root = runtime_root / "reports"
    manifests_root = runtime_root / "manifests" / "measurement_views"
    reports_root.mkdir(parents=True, exist_ok=True)
    manifests_root.mkdir(parents=True, exist_ok=True)

    json_path = reports_root / "measurement_view.json"
    html_path = reports_root / "measurement_view.html"
    manifest_path = manifests_root / "latest_measurement_view.json"

    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    html_path.write_text(render_measurement_view_html(data), encoding="utf-8")
    return {"json_path": json_path, "html_path": html_path, "manifest_path": manifest_path}
