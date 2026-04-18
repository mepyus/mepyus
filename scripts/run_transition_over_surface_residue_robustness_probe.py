#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.line_thickening import refresh_line_registry_entry


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
        "derived_residue_trend": row.get("derived_residue_trend"),
        "derived_residue_persistence": row.get("derived_residue_persistence"),
        "derived_residue_robustness": row.get("derived_residue_robustness"),
        "recent_decay_streak": row.get("recent_decay_streak"),
        "last_derived_support_offset": row.get("last_derived_support_offset"),
        "recent_primary_rows": row.get("recent_primary_rows"),
        "recent_derived_rows": row.get("recent_derived_rows"),
        "recent_window_size_used": row.get("recent_window_size_used"),
        "tested_window_sizes": row.get("tested_window_sizes"),
        "trend_window_agreement_summary": row.get("trend_window_agreement_summary"),
        "persistence_basis_summary": row.get("persistence_basis_summary"),
    }


def main(argv: list[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) > 1 else (REPO_ROOT / "runtime").resolve()
    for line_name in (
        "transition_over_surface",
        "input_to_reading_organ",
        "pre_read_eye",
        "raw_return_preservation",
    ):
        refresh_line_registry_entry(runtime_root, line_name)

    print(
        json.dumps(
            {
                "runtime_root": str(runtime_root),
                "tested_window_sizes": [3, 5, 7, 9],
                "registry_summary": {
                    line_name: _line_summary(runtime_root, line_name)
                    for line_name in (
                        "transition_over_surface",
                        "input_to_reading_organ",
                        "pre_read_eye",
                        "raw_return_preservation",
                    )
                },
                "robustness_reading_rule": {
                    "robust_decay": "multiple tested windows agree on decaying/persistent direction",
                    "weak_decay": "some windows decay but the agreement is too thin",
                    "window_sensitive": "window choices disagree materially",
                    "non_decay_stable": "no derived residue history is decaying; line is stable without a residue story",
                    "insufficient_history": "not enough informative history across the tested windows",
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
