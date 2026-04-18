#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.classifier_adapter import classify_entry_state
from app.core.runtime.reentry_prebias import build_reentry_prebias, load_hint_by_artifact


DEFAULT_HINTS_PATH = ROOT / "runtime" / "manifests" / "source_to_family_hints_v0.json"
DEFAULT_RESIDUE_RULES_PATH = ROOT / "runtime" / "manifests" / "residue_reentry_rules_v0.json"
DEFAULT_CLASSIFIER_PATH = ROOT / "runtime" / "manifests" / "issue_root_classifier_v0.json"
DEFAULT_SIGNAL_TAXONOMY_PATH = ROOT / "runtime" / "manifests" / "signal_kind_taxonomy_v0.json"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run classifier selection from saved hint state with optional residue-backed reentry."
    )
    parser.add_argument("artifact_path", help="Current artifact path to classify.")
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
        "--requested-outcome",
        dest="requested_outcome",
        default="",
        help="Optional requested outcome override, for example operator_explanation.",
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
    hints_manifest_path = _resolve_path(args.hints_manifest_path)
    residue_rules_path = _resolve_path(args.residue_rules_path)
    classifier_path = _resolve_path(args.classifier_path)
    signal_taxonomy_path = _resolve_path(args.signal_taxonomy_path)

    current_hint = load_hint_by_artifact(hints_manifest_path, artifact_path)
    previous_hint = None
    reentry_prebias = None
    if args.previous_artifact and args.question_shift:
        previous_artifact_path = _resolve_path(args.previous_artifact)
        previous_hint = load_hint_by_artifact(hints_manifest_path, previous_artifact_path)
        reentry_prebias = build_reentry_prebias(
            previous_hint=previous_hint,
            new_hint=current_hint,
            residue_rules_path=residue_rules_path,
            question_shift=args.question_shift,
        )

    classification = classify_entry_state(
        classifier_path=classifier_path,
        signal_taxonomy_path=signal_taxonomy_path,
        current_hint=current_hint,
        reentry_prebias=reentry_prebias,
        requested_outcome=args.requested_outcome,
    )
    payload = {
        "artifact_path": str(artifact_path),
        "current_hint": current_hint,
        "previous_hint": previous_hint,
        "reentry_prebias": reentry_prebias,
        "classification": classification,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
