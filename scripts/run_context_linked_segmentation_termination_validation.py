#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


TARGET_FALSE_POSITIVES = {
    ("dialogue_continuation", ("dlg_003", "dlg_004"), "answer_completion"),
    ("explanatory_mechanism", ("exp_003", "exp_004"), "causal_chain"),
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output_root = Path("/tmp/context_linked_segmentation_termination_validation")
    output_root.mkdir(parents=True, exist_ok=True)

    command = [sys.executable, str(root / "scripts/run_context_linked_segmentation_validation.py")]
    subprocess.run(command, cwd=root, check=True)

    validation_path = Path("/tmp/context_linked_segmentation_validation/validation_result.json")
    payload = json.loads(validation_path.read_text(encoding="utf-8"))
    remaining = []
    for item in payload["overall_false_positive"]:
        key = (
            item["fixture_name"],
            tuple(item["segment_ids"]),
            item["linkage_reason"],
        )
        if key in TARGET_FALSE_POSITIVES:
            remaining.append(item)

    result = {
        "target_false_positive_before": [
            {
                "fixture_name": fixture_name,
                "segment_ids": list(segment_ids),
                "linkage_reason": reason,
            }
            for fixture_name, segment_ids, reason in sorted(TARGET_FALSE_POSITIVES)
        ],
        "target_false_positive_after": remaining,
        "all_false_positive": payload["overall_false_positive"],
        "all_miss": payload["overall_miss"],
    }
    output_path = output_root / "termination_result.json"
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
