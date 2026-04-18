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


DEFAULT_RULES_PATH = ROOT / "runtime" / "manifests" / "auto_hint_generation_rules_v0.json"
DEFAULT_HINTS_PATH = ROOT / "runtime" / "manifests" / "source_to_family_hints_v0.json"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate source-to-family hint candidates from a JSON artifact using bundle-match rules."
    )
    parser.add_argument("artifact_path", help="Path to the JSON artifact to inspect.")
    parser.add_argument(
        "--rules",
        dest="rules_path",
        default=str(DEFAULT_RULES_PATH),
        help="Path to the auto hint generation rules JSON.",
    )
    parser.add_argument(
        "--first-only",
        action="store_true",
        help="Return only the first matching hint candidate.",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the first matching hint candidate into source_to_family_hints_v0.json format.",
    )
    parser.add_argument(
        "--hints-manifest",
        dest="hints_manifest_path",
        default=str(DEFAULT_HINTS_PATH),
        help="Path to the source-to-family hints manifest to update when --save is used.",
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
    candidates = generate_hint_candidates(artifact_path, rules_path)
    selected_candidates = candidates[:1] if args.first_only else candidates
    save_result = None
    if args.save and candidates:
        save_result = save_hint_candidate(hints_manifest_path, candidates[0])
    payload = {
        "artifact_path": str(artifact_path),
        "rules_path": str(rules_path),
        "match_count": len(candidates),
        "hint_candidates": selected_candidates,
        "save_result": save_result,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
