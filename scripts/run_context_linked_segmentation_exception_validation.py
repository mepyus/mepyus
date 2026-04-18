#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


RECOVER_TARGETS = {
    ("explanatory_mechanism", ("exp_002", "exp_003"), "causal_chain"),
    ("mixed_document", ("mix_001", "mix_002"), "answer_completion"),
    ("mixed_document", ("mix_002", "mix_003"), "causal_chain"),
}

FALSE_POSITIVE_GUARDS = {
    ("dialogue_continuation", ("dlg_003", "dlg_004"), "answer_completion"),
    ("explanatory_mechanism", ("exp_003", "exp_004"), "causal_chain"),
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output_root = Path("/tmp/context_linked_segmentation_exception_validation")
    output_root.mkdir(parents=True, exist_ok=True)

    command = [sys.executable, str(root / "scripts/run_context_linked_segmentation_validation.py")]
    subprocess.run(command, cwd=root, check=True)

    validation_path = Path("/tmp/context_linked_segmentation_validation/validation_result.json")
    payload = json.loads(validation_path.read_text(encoding="utf-8"))
    actual_pairs = set()
    false_positive_pairs = set()
    for result in payload["results"]:
        fixture_name = result["fixture_name"]
        for item in result["actual"]:
            actual_pairs.add((fixture_name, tuple(item["segment_ids"]), item["linkage_reason"]))
        for item in result["false_positive"]:
            false_positive_pairs.add((fixture_name, tuple(item["segment_ids"]), item["linkage_reason"]))

    recovered = [
        {
            "fixture_name": fixture_name,
            "segment_ids": list(segment_ids),
            "linkage_reason": reason,
        }
        for fixture_name, segment_ids, reason in sorted(RECOVER_TARGETS & actual_pairs)
    ]
    unrecovered = [
        {
            "fixture_name": fixture_name,
            "segment_ids": list(segment_ids),
            "linkage_reason": reason,
        }
        for fixture_name, segment_ids, reason in sorted(RECOVER_TARGETS - actual_pairs)
    ]
    guard_regressions = [
        {
            "fixture_name": fixture_name,
            "segment_ids": list(segment_ids),
            "linkage_reason": reason,
        }
        for fixture_name, segment_ids, reason in sorted(FALSE_POSITIVE_GUARDS & false_positive_pairs)
    ]

    result = {
        "recovered_targets": recovered,
        "unrecovered_targets": unrecovered,
        "false_positive_regression": guard_regressions,
        "all_false_positive": payload["overall_false_positive"],
        "all_miss": payload["overall_miss"],
        "fixture_summaries": payload["fixture_summaries"],
    }
    output_path = output_root / "exception_result.json"
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
