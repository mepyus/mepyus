#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.models.entities import PressureAxis, SupportRef


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

    fresh = _find_material_by_role(runtime_root, "fresh_material")

    trace = service.register_trace(
        material_refs=[fresh["material_id"]],
        evidence_kind="fresh_pressure_hint",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=fresh["material_id"], note="fresh_material"),
        ],
        note="Initial pressure-bearing trace for fresh material without linking it into the prior weak relation.",
    )
    pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="session_pressure", strength_hint=0.55),
            PressureAxis(axis="recurrence_pressure", strength_hint=0.35),
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=fresh["material_id"], note="fresh_material"),
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="fresh_pressure_hint"),
        ],
    )
    seed = service.create_point_seed_candidate(
        material_refs=[fresh["material_id"]],
        trace_refs=[trace.trace_id],
        pressure_profile_id=pressure.profile_id,
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "trace_id: %s" % trace.trace_id,
        "pressure_profile_id: %s" % pressure.profile_id,
        "seed_id: %s" % seed.seed_id,
        "seed_state: %s" % seed.state.value,
        "material_ref: %s" % fresh["material_id"],
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
