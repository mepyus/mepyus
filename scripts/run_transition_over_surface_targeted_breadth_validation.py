#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

OBSERVER_CONTROL_COHORT = [
    "frag_basic3_002",
    "frag_basic4_003",
]

SOURCE_VIEW_COHORT = [
    "frag_basic3_002",
    "frag_basic_004",
    "frag_basic3_004",
    "frag_ytex_003",
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
    row = next((item for item in registry.get("lines", []) if item.get("line_name") == "transition_over_surface"), {})
    return {
        "status": row.get("status"),
        "thickness_level": row.get("thickness_level"),
        "promotion_scope": row.get("promotion_scope"),
        "validation_profile": row.get("validation_profile"),
        "primary_only_validation_profile": row.get("primary_only_validation_profile"),
        "support_ecology_bias": row.get("support_ecology_bias"),
        "derived_support_role": row.get("derived_support_role"),
        "derived_support_summary": row.get("derived_support_summary"),
        "primary_vs_derived_balance_summary": row.get("primary_vs_derived_balance_summary"),
        "primary_support_share_bucket": row.get("primary_support_share_bucket"),
        "derived_dependency_hint": row.get("derived_dependency_hint"),
        "broadening_gap_type": row.get("broadening_gap_type"),
        "next_missing_axis": row.get("next_missing_axis"),
        "profile_basis_summary": row.get("profile_basis_summary"),
        "primary_only_basis_summary": row.get("primary_only_basis_summary"),
        "gap_basis_summary": row.get("gap_basis_summary"),
        "primary_support_row_count": row.get("primary_support_row_count"),
        "derived_support_row_count": row.get("derived_support_row_count"),
        "self_referential_derived_row_count": row.get("self_referential_derived_row_count"),
        "summary_row_count": row.get("summary_row_count"),
        "cumulative_primary_rows": row.get("cumulative_primary_rows"),
        "cumulative_derived_rows": row.get("cumulative_derived_rows"),
        "recent_primary_rows": row.get("recent_primary_rows"),
        "recent_derived_rows": row.get("recent_derived_rows"),
        "recent_window_size_used": row.get("recent_window_size_used"),
        "recent_primary_vs_derived_summary": row.get("recent_primary_vs_derived_summary"),
        "derived_residue_trend": row.get("derived_residue_trend"),
        "derived_residue_trend_summary": row.get("derived_residue_trend_summary"),
        "primary_only_path_count": row.get("primary_only_path_count"),
        "primary_only_material_count": row.get("primary_only_material_count"),
        "primary_only_source_document_count": row.get("primary_only_source_document_count"),
        "primary_only_independent_evidence_count": row.get("primary_only_independent_evidence_count"),
        "distinct_path_count": row.get("distinct_path_count"),
        "distinct_independent_evidence_count": row.get("distinct_independent_evidence_count"),
        "distinct_primary_material_anchor_count": row.get("distinct_primary_material_anchor_count"),
        "distinct_source_document_count": row.get("distinct_source_document_count"),
        "material_independence_summary": row.get("material_independence_summary"),
        "evidence_independence_summary": row.get("evidence_independence_summary"),
    }


def main(argv: list[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) > 1 else (REPO_ROOT / "runtime").resolve()

    observer_result = _run(
        [
            sys.executable,
            "scripts/apply_internal_observer.py",
            str(runtime_root),
            *OBSERVER_CONTROL_COHORT,
            "--record-line-thickening",
            "--bounded-recurrence-validation",
        ]
    )

    source_view_results = []
    for fragment_id in SOURCE_VIEW_COHORT:
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
                "observer_control_cohort": OBSERVER_CONTROL_COHORT,
                "source_view_cohort": SOURCE_VIEW_COHORT,
                "observer_result": observer_result["parsed"],
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
