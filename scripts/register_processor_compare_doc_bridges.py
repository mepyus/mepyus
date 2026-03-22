#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from scripts.import_processor_compare_docs import _register_doc_bridges


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    service = FormationService(runtime_root)
    imported_docs = _collect_imported_docs(service)
    bridges = _register_doc_bridges(service, imported_docs)
    print(
        json.dumps(
            {
                "runtime_root": str(runtime_root),
                "doc_count": len(imported_docs),
                "bridge_count": len(bridges),
                "bridges": bridges,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def _collect_imported_docs(service: FormationService) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for local_space in service.local_spaces.read_all():
        cell_refs = list(local_space.get("cell_refs", []))
        if len(cell_refs) != 1:
            continue
        cell = service.cells.get(cell_refs[0]) or {}
        material_ids = list(cell.get("material_refs", []))
        if not material_ids:
            continue
        first_material = service.materials.get(material_ids[0]) or {}
        source_ref = str(first_material.get("source_ref", ""))
        doc_id = str(first_material.get("family_id", ""))
        if not source_ref.startswith("processor_compare/") or not doc_id.startswith("doc_"):
            continue
        trace_ids = list(cell.get("trace_refs", []))
        seed_ids = list(cell.get("seed_refs", []))
        rows.append(
            {
                "doc_id": doc_id,
                "source_ref": source_ref,
                "material_ids": material_ids,
                "trace_ids": trace_ids,
                "seed_ids": seed_ids,
                "cell_id": cell.get("cell_id", ""),
                "local_space_id": local_space.get("local_space_id", ""),
            }
        )
    rows.sort(key=lambda row: str(row["doc_id"]))
    return rows


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
