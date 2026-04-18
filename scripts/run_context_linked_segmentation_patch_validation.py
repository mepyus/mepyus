#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


BASELINE_MATCH_RATES = {
    "dialogue_continuation": 1.0,
    "explanatory_mechanism": 0.5,
    "argument_contrast": 0.5,
    "mixed_document": 0.25,
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output_root = Path("/tmp/context_linked_segmentation_patch_validation")
    output_root.mkdir(parents=True, exist_ok=True)

    command = [sys.executable, str(root / "scripts/run_context_linked_segmentation_validation.py")]
    subprocess.run(command, cwd=root, check=True)

    validation_path = Path("/tmp/context_linked_segmentation_validation/validation_result.json")
    payload = json.loads(validation_path.read_text(encoding="utf-8"))
    before_after = []
    for item in payload["fixture_summaries"]:
        fixture_name = item["fixture_name"]
        before_after.append(
            {
                "fixture_name": fixture_name,
                "before_match_rate": BASELINE_MATCH_RATES[fixture_name],
                "after_match_rate": item["match_rate"],
                "delta": item["match_rate"] - BASELINE_MATCH_RATES[fixture_name],
            }
        )

    result = {
        "before_after": before_after,
        "overall_false_positive": payload["overall_false_positive"],
        "overall_miss": payload["overall_miss"],
    }
    output_path = output_root / "comparison_result.json"
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
