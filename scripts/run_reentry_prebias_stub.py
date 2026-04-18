#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.reentry_prebias import build_reentry_prebias, load_hint_by_artifact


DEFAULT_HINTS_PATH = ROOT / "runtime" / "manifests" / "source_to_family_hints_v0.json"
DEFAULT_RESIDUE_RULES_PATH = ROOT / "runtime" / "manifests" / "residue_reentry_rules_v0.json"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a minimal residue-backed reentry prebias from previous and new artifact hints."
    )
    parser.add_argument("--previous-artifact", required=True, help="Artifact path for the previous family hint.")
    parser.add_argument("--new-artifact", required=True, help="Artifact path for the new source artifact.")
    parser.add_argument("--question-shift", required=True, help="Question shift key such as entry_shaping_to_transition_condition.")
    parser.add_argument(
        "--hints-manifest",
        default=str(DEFAULT_HINTS_PATH),
        help="Path to the source-to-family hints manifest.",
    )
    parser.add_argument(
        "--residue-rules",
        default=str(DEFAULT_RESIDUE_RULES_PATH),
        help="Path to the residue reentry rules manifest.",
    )
    return parser.parse_args()


def _resolve_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    return path


def main() -> int:
    args = _parse_args()
    previous_artifact = _resolve_path(args.previous_artifact)
    new_artifact = _resolve_path(args.new_artifact)
    hints_manifest = _resolve_path(args.hints_manifest)
    residue_rules = _resolve_path(args.residue_rules)

    previous_hint = load_hint_by_artifact(hints_manifest, previous_artifact)
    new_hint = load_hint_by_artifact(hints_manifest, new_artifact)
    prebias = build_reentry_prebias(
        previous_hint=previous_hint,
        new_hint=new_hint,
        residue_rules_path=residue_rules,
        question_shift=args.question_shift,
    )
    payload = {
        "previous_artifact": str(previous_artifact),
        "new_artifact": str(new_artifact),
        "previous_hint": previous_hint,
        "new_hint": new_hint,
        "reentry_prebias": prebias,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
