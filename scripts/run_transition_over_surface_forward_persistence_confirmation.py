#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.line_thickening import refresh_line_registry_entry

# Use only new pointer-bearing primary anchors so the check confirms direction
# without depending on same-material replay.
FORWARD_REFRESH_COHORT = [
    "frag_basic3_003",
    "frag_ytex_002",
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
        "parsed": parsed,
    }


def _line_summary(runtime_root: Path, line_name: str) -> dict:
    registry = json.loads((runtime_root / "manifests" / "line_registry.json").read_text(encoding="utf-8"))
    row = next((item for item in registry.get("lines", []) if item.get("line_name") == line_name), {})
    return {
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
        "recent_primary_rows": row.get("recent_primary_rows"),
        "recent_derived_rows": row.get("recent_derived_rows"),
        "recent_window_size_used": row.get("recent_window_size_used"),
        "distinct_primary_material_anchor_count": row.get("distinct_primary_material_anchor_count"),
        "distinct_source_document_count": row.get("distinct_source_document_count"),
        "persistence_basis_summary": row.get("persistence_basis_summary"),
    }


def main(argv: list[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) > 1 else (REPO_ROOT / "runtime").resolve()

    source_view_results = []
    for fragment_id in FORWARD_REFRESH_COHORT:
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

    refreshed = {}
    for line_name in (
        "transition_over_surface",
        "input_to_reading_organ",
        "pre_read_eye",
        "raw_return_preservation",
    ):
        refreshed[line_name] = refresh_line_registry_entry(runtime_root, line_name)

    print(
        json.dumps(
            {
                "runtime_root": str(runtime_root),
                "forward_refresh_cohort": FORWARD_REFRESH_COHORT,
                "source_view_results": [item["parsed"] for item in source_view_results],
                "registry_summary": {
                    name: _line_summary(runtime_root, name)
                    for name in (
                        "transition_over_surface",
                        "input_to_reading_organ",
                        "pre_read_eye",
                        "raw_return_preservation",
                    )
                },
                "failure_conditions": {
                    "persistent_decay_breaks_if": [
                        "a recent window includes derived support again",
                        "recent_decay_streak falls back to 1 after a reappearing derived row",
                    ],
                    "stable_mixed_reads_when": [
                        "there is enough history but no derived residue history to decay from",
                    ],
                    "reappearing_reads_when": [
                        "recent window derived rows return after a cleaner period",
                    ],
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
