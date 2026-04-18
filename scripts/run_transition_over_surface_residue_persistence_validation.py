#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

PERSISTENCE_COHORT = [
    "frag_basic_003",
    "frag_ytex_001",
]


def _run(cmd: list[str]) -> dict:
    completed = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    stdout = completed.stdout.strip().splitlines()
    payload = stdout[-1] if stdout else "{}"
    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError:
        parsed = {"stdout": completed.stdout}
    return {
        "command": cmd,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "parsed": parsed,
    }


def _registry_summary(runtime_root: Path) -> dict:
    registry = json.loads((runtime_root / "manifests" / "line_registry.json").read_text(encoding="utf-8"))
    result = {}
    for line_name in ("transition_over_surface", "input_to_reading_organ", "pre_read_eye", "raw_return_preservation"):
        row = next((item for item in registry.get("lines", []) if item.get("line_name") == line_name), {})
        result[line_name] = {
            "status": row.get("status"),
            "thickness_level": row.get("thickness_level"),
            "promotion_scope": row.get("promotion_scope"),
            "validation_profile": row.get("validation_profile"),
            "primary_only_validation_profile": row.get("primary_only_validation_profile"),
            "support_ecology_bias": row.get("support_ecology_bias"),
            "derived_support_role": row.get("derived_support_role"),
            "derived_dependency_hint": row.get("derived_dependency_hint"),
            "derived_residue_trend": row.get("derived_residue_trend"),
            "derived_residue_persistence": row.get("derived_residue_persistence"),
            "recent_decay_streak": row.get("recent_decay_streak"),
            "last_derived_support_offset": row.get("last_derived_support_offset"),
            "cumulative_primary_rows": row.get("cumulative_primary_rows"),
            "cumulative_derived_rows": row.get("cumulative_derived_rows"),
            "recent_primary_rows": row.get("recent_primary_rows"),
            "recent_derived_rows": row.get("recent_derived_rows"),
            "recent_window_size_used": row.get("recent_window_size_used"),
            "recent_primary_vs_derived_summary": row.get("recent_primary_vs_derived_summary"),
            "persistence_basis_summary": row.get("persistence_basis_summary"),
            "profile_basis_summary": row.get("profile_basis_summary"),
            "primary_only_basis_summary": row.get("primary_only_basis_summary"),
            "gap_basis_summary": row.get("gap_basis_summary"),
        }
    return result


def main(argv: list[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) > 1 else (REPO_ROOT / "runtime").resolve()

    source_view_results = []
    for fragment_id in PERSISTENCE_COHORT:
        source_view_results.append(
            _run(
                [
                    sys.executable,
                    "scripts/build_source_view.py",
                    str(runtime_root),
                    "--record-line-thickening",
                    "--fragment-id",
                    fragment_id,
                ]
            )
        )

    print(
        json.dumps(
            {
                "runtime_root": str(runtime_root),
                "persistence_cohort": PERSISTENCE_COHORT,
                "source_view_results": [item["parsed"] for item in source_view_results],
                "registry_summary": _registry_summary(runtime_root),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
