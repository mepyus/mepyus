#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.auto_hint_generation import generate_hint_candidates, save_hint_candidate
from app.core.runtime.classifier_adapter import classify_entry_state
from app.core.runtime.execution_trace import append_execution_trace, build_execution_trace_record
from app.core.runtime.reentry_prebias import build_reentry_prebias, load_hint_by_artifact


DEFAULT_RULES_PATH = ROOT / "runtime" / "manifests" / "auto_hint_generation_rules_v0.json"
DEFAULT_HINTS_PATH = ROOT / "runtime" / "manifests" / "source_to_family_hints_v0.json"
DEFAULT_RESIDUE_RULES_PATH = ROOT / "runtime" / "manifests" / "residue_reentry_rules_v0.json"
DEFAULT_CLASSIFIER_PATH = ROOT / "runtime" / "manifests" / "issue_root_classifier_v0.json"
DEFAULT_SIGNAL_TAXONOMY_PATH = ROOT / "runtime" / "manifests" / "signal_kind_taxonomy_v0.json"
DEFAULT_TRACE_LOG_PATH = ROOT / "runtime" / "manifests" / "execution_trace_log_v0.jsonl"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a minimal prototype execution spine: auto hint generation, optional save, and optional residue-backed reentry."
    )
    parser.add_argument("artifact_path", help="New artifact path to inspect.")
    parser.add_argument(
        "--rules",
        dest="rules_path",
        default=str(DEFAULT_RULES_PATH),
        help="Path to the auto hint generation rules JSON.",
    )
    parser.add_argument(
        "--hints-manifest",
        dest="hints_manifest_path",
        default=str(DEFAULT_HINTS_PATH),
        help="Path to the source-to-family hints manifest.",
    )
    parser.add_argument(
        "--residue-rules",
        dest="residue_rules_path",
        default=str(DEFAULT_RESIDUE_RULES_PATH),
        help="Path to the residue reentry rules manifest.",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the first generated hint into the hints manifest.",
    )
    parser.add_argument(
        "--previous-artifact",
        dest="previous_artifact",
        default="",
        help="Optional previous artifact path for residue-backed reentry.",
    )
    parser.add_argument(
        "--question-shift",
        dest="question_shift",
        default="",
        help="Question shift key used for residue-backed reentry.",
    )
    parser.add_argument(
        "--classifier",
        dest="classifier_path",
        default=str(DEFAULT_CLASSIFIER_PATH),
        help="Path to the issue-root classifier manifest.",
    )
    parser.add_argument(
        "--signal-taxonomy",
        dest="signal_taxonomy_path",
        default=str(DEFAULT_SIGNAL_TAXONOMY_PATH),
        help="Path to the signal taxonomy manifest.",
    )
    parser.add_argument(
        "--requested-outcome",
        dest="requested_outcome",
        default="",
        help="Optional requested outcome override, for example operator_explanation.",
    )
    parser.add_argument(
        "--record-trace",
        action="store_true",
        help="Append the current execution result to the execution trace jsonl log.",
    )
    parser.add_argument(
        "--trace-log",
        dest="trace_log_path",
        default=str(DEFAULT_TRACE_LOG_PATH),
        help="Path to the execution trace jsonl log.",
    )
    parser.add_argument(
        "--execution-context",
        dest="execution_context",
        default="prototype_execution_spine_stub",
        help="Execution context label stored in the trace record.",
    )
    return parser.parse_args()


def _resolve_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    return path


def main() -> int:
    args = _parse_args()
    artifact_path = _resolve_path(args.artifact_path)
    rules_path = _resolve_path(args.rules_path)
    hints_manifest_path = _resolve_path(args.hints_manifest_path)
    residue_rules_path = _resolve_path(args.residue_rules_path)
    classifier_path = _resolve_path(args.classifier_path)
    signal_taxonomy_path = _resolve_path(args.signal_taxonomy_path)
    trace_log_path = _resolve_path(args.trace_log_path)

    generated_hints = generate_hint_candidates(artifact_path, rules_path)
    first_hint = generated_hints[0] if generated_hints else None
    save_result = None
    if args.save and first_hint:
        save_result = save_hint_candidate(hints_manifest_path, first_hint)

    current_hint = load_hint_by_artifact(hints_manifest_path, artifact_path)
    previous_hint = None
    reentry_prebias = None
    if args.previous_artifact and args.question_shift:
        previous_artifact_path = _resolve_path(args.previous_artifact)
        previous_hint = load_hint_by_artifact(hints_manifest_path, previous_artifact_path)
        reentry_prebias = build_reentry_prebias(
            previous_hint=previous_hint,
            new_hint=current_hint or first_hint,
            residue_rules_path=residue_rules_path,
            question_shift=args.question_shift,
        )
    classification = classify_entry_state(
        classifier_path=classifier_path,
        signal_taxonomy_path=signal_taxonomy_path,
        current_hint=current_hint or first_hint,
        reentry_prebias=reentry_prebias,
        requested_outcome=args.requested_outcome,
    )
    trace_record = None
    trace_result = None
    if args.record_trace:
        trace_record = build_execution_trace_record(
            artifact_path=artifact_path,
            current_hint=current_hint or first_hint,
            previous_hint=previous_hint,
            reentry_prebias=reentry_prebias,
            classification=classification,
            question_shift=args.question_shift,
            execution_context=args.execution_context,
        )
        trace_result = append_execution_trace(trace_log_path, trace_record)

    payload = {
        "artifact_path": str(artifact_path),
        "generated_hint_count": len(generated_hints),
        "generated_hints": generated_hints,
        "save_result": save_result,
        "current_hint": current_hint,
        "previous_hint": previous_hint,
        "reentry_prebias": reentry_prebias,
        "classification": classification,
        "trace_record": trace_record,
        "trace_result": trace_result,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
