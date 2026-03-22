#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.models.entities import SupportRef


def _find_material_by_role(runtime_root: Path, formation_role: str) -> dict:
    materials_root = runtime_root / "core" / "materials"
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("metadata", {}).get("formation_role") == formation_role:
            return record
    raise RuntimeError("missing material for role: %s" % formation_role)


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    observer = _find_material_by_role(runtime_root, "observer_material")

    trace = service.register_trace(
        material_refs=[engine_self["material_id"], observer["material_id"]],
        evidence_kind="observer_reflection",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=engine_self["material_id"], note="engine_self_material"),
            SupportRef(ref_kind="material", ref_id=observer["material_id"], note="observer_material"),
        ],
        note="Initial weak relation between engine-self runtime record and observer summary.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "trace_id: %s" % trace.trace_id,
        "evidence_kind: %s" % trace.evidence_kind,
        "material_refs: %s" % ",".join(trace.material_refs),
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
