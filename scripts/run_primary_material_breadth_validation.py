#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_OBSERVER_COHORT = [
    "frag_basic3_002",
    "frag_basic4_003",
    "frag_ytex_001",
    "frag_ytex_002",
    "frag_basic_003",
    "frag_basic3_003",
]

DEFAULT_SOURCE_VIEW_COHORT = [
    "frag_basic3_002",
    "frag_basic4_003",
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


def _load_registry_summary(runtime_root: Path) -> dict:
    registry = json.loads((runtime_root / "manifests" / "line_registry.json").read_text(encoding="utf-8"))
    result = {}
    for line_name in ("transition_over_surface", "input_to_reading_organ", "pre_read_eye", "raw_return_preservation"):
        for row in registry.get("lines", []):
            if row.get("line_name") == line_name:
                result[line_name] = {
                    "status": row.get("status"),
                    "thickness_level": row.get("thickness_level"),
                    "promotion_scope": row.get("promotion_scope"),
                    "validation_profile": row.get("validation_profile"),
                    "profile_basis_summary": row.get("profile_basis_summary"),
                    "broadening_gap_type": row.get("broadening_gap_type"),
                    "next_missing_axis": row.get("next_missing_axis"),
                    "gap_basis_summary": row.get("gap_basis_summary"),
                    "distinct_path_count": row.get("distinct_path_count"),
                    "distinct_independent_evidence_count": row.get("distinct_independent_evidence_count"),
                    "distinct_material_anchor_count": row.get("distinct_material_anchor_count"),
                    "distinct_primary_material_anchor_count": row.get("distinct_primary_material_anchor_count"),
                    "distinct_source_document_count": row.get("distinct_source_document_count"),
                    "cumulative_primary_rows": row.get("cumulative_primary_rows"),
                    "cumulative_derived_rows": row.get("cumulative_derived_rows"),
                    "recent_primary_rows": row.get("recent_primary_rows"),
                    "recent_derived_rows": row.get("recent_derived_rows"),
                    "recent_window_size_used": row.get("recent_window_size_used"),
                    "recent_primary_vs_derived_summary": row.get("recent_primary_vs_derived_summary"),
                    "derived_residue_trend": row.get("derived_residue_trend"),
                    "derived_residue_trend_summary": row.get("derived_residue_trend_summary"),
                    "evidence_independence_summary": row.get("evidence_independence_summary"),
                    "material_independence_summary": row.get("material_independence_summary"),
                }
                break
    return result


def main(argv: list[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) > 1 else (REPO_ROOT / "runtime").resolve()

    observer_result = _run(
        [
            sys.executable,
            "scripts/apply_internal_observer.py",
            str(runtime_root),
            *DEFAULT_OBSERVER_COHORT,
            "--record-line-thickening",
            "--bounded-recurrence-validation",
        ]
    )

    source_results = []
    for fragment_id in DEFAULT_SOURCE_VIEW_COHORT:
        source_results.append(
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
                "observer_cohort": DEFAULT_OBSERVER_COHORT,
                "source_view_cohort": DEFAULT_SOURCE_VIEW_COHORT,
                "observer_result": observer_result["parsed"],
                "source_view_results": [item["parsed"] for item in source_results],
                "registry_summary": _load_registry_summary(runtime_root),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
