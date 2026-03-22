#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.work.processor_compare.anchor_engine import run_anchor_pipeline


SOURCE_DOCS_DIR = REPO_ROOT / "app" / "work" / "processor_compare" / "inputs" / "source_docs"
REPORT_PATH = REPO_ROOT / "app" / "work" / "processor_compare" / "reports" / "processor_doc_anchor_runtime_20260321.json"


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    docs = _load_documents(SOURCE_DOCS_DIR)
    pipeline = run_anchor_pipeline(docs)
    doc_lookup = _collect_imported_doc_runtime_map(runtime_root)
    bridge_lookup = _collect_bridge_runtime_map(runtime_root)

    local_space_updates = []
    for region in pipeline["region_summary"]:
        doc_id = str(region["region_id"])
        runtime_row = doc_lookup.get(doc_id)
        if not runtime_row:
            continue
        local_space_path = runtime_root / "core" / "local_spaces" / f"{runtime_row['local_space_id']}.json"
        payload = _read_json(local_space_path)
        payload["doc_id"] = doc_id
        payload["source_label"] = doc_id
        payload["representative_anchors"] = region["representative_anchors"]
        payload["supporting_anchors"] = region["supporting_anchors"]
        payload["dropped_weak_anchors"] = region["dropped_weak_anchors"]
        _write_json(local_space_path, payload)
        local_space_updates.append({"doc_id": doc_id, "local_space_id": runtime_row["local_space_id"]})

    bridge_updates = []
    for bridge in pipeline["bridge_summary"]:
        left_doc = str(bridge["left_region_id"])
        right_doc = str(bridge["right_region_id"])
        bridge_id = bridge_lookup.get(tuple(sorted((left_doc, right_doc))))
        if not bridge_id:
            continue
        bridge_path = runtime_root / "core" / "bridge_traces" / f"{bridge_id}.json"
        payload = _read_json(bridge_path)
        payload["left_doc_id"] = left_doc
        payload["right_doc_id"] = right_doc
        payload["shared_anchors"] = bridge["shared_anchors"]
        payload["rejected_overlap_anchors"] = bridge["rejected_overlap_anchors"]
        if bridge["shared_anchors"]:
            payload["note"] = "canonical shared anchors: " + ", ".join(
                anchor["display_label"] for anchor in bridge["shared_anchors"][:4]
            )
        _write_json(bridge_path, payload)
        bridge_updates.append(
            {
                "bridge_id": bridge_id,
                "left_doc": left_doc,
                "right_doc": right_doc,
                "shared_anchor_labels": [anchor["display_label"] for anchor in bridge["shared_anchors"][:4]],
            }
        )

    for pair, bridge_id in bridge_lookup.items():
        if any(update["bridge_id"] == bridge_id for update in bridge_updates):
            continue
        left_doc, right_doc = pair
        bridge_path = runtime_root / "core" / "bridge_traces" / f"{bridge_id}.json"
        payload = _read_json(bridge_path)
        payload["left_doc_id"] = left_doc
        payload["right_doc_id"] = right_doc
        payload.setdefault("shared_anchors", [])
        payload.setdefault("rejected_overlap_anchors", [])
        _write_json(bridge_path, payload)

    report = {
        "runtime_root": str(runtime_root),
        "doc_count": len(docs),
        "promoted_count": len(pipeline["promoted"]),
        "region_summary_count": len(pipeline["region_summary"]),
        "bridge_summary_count": len(pipeline["bridge_summary"]),
        "local_space_updates": local_space_updates,
        "bridge_updates": bridge_updates,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def _load_documents(source_dir: Path) -> List[Dict[str, object]]:
    docs = []
    for path in sorted(source_dir.glob("doc_*.txt")):
        docs.append(
            {
                "doc_id": path.stem,
                "title": path.stem,
                "text": path.read_text(encoding="utf-8"),
                "sections": [],
                "metadata": {"source_type": "processor_compare"},
            }
        )
    return docs


def _collect_imported_doc_runtime_map(runtime_root: Path) -> Dict[str, Dict[str, str]]:
    local_spaces_dir = runtime_root / "core" / "local_spaces"
    space_cells_dir = runtime_root / "core" / "space_cells"
    rows: Dict[str, Dict[str, str]] = {}
    for path in sorted(local_spaces_dir.glob("*.json")):
        payload = _read_json(path)
        cell_refs = list(payload.get("cell_refs", []))
        if len(cell_refs) != 1:
            continue
        cell_payload = _read_json(space_cells_dir / f"{cell_refs[0]}.json")
        note = str(cell_payload.get("cohesion_note", ""))
        if " imported from processor_compare source_docs" not in note:
            continue
        doc_id = note.split(" imported from processor_compare source_docs", 1)[0].strip()
        rows[doc_id] = {
            "local_space_id": str(payload.get("local_space_id", "")),
            "cell_id": str(cell_payload.get("cell_id", "")),
        }
    return rows


def _collect_bridge_runtime_map(runtime_root: Path) -> Dict[tuple[str, str], str]:
    local_doc = _collect_imported_doc_runtime_map(runtime_root)
    reverse = {row["local_space_id"]: doc_id for doc_id, row in local_doc.items()}
    bridge_dir = runtime_root / "core" / "bridge_traces"
    rows: Dict[tuple[str, str], str] = {}
    for path in sorted(bridge_dir.glob("*.json")):
        payload = _read_json(path)
        left = reverse.get(str(payload.get("from_local_space_id", "")))
        right = reverse.get(str(payload.get("to_local_space_id", "")))
        if not left or not right:
            continue
        rows[tuple(sorted((left, right)))] = str(payload.get("bridge_id", ""))
    return rows


def _read_json(path: Path) -> Dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Dict[str, object]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
