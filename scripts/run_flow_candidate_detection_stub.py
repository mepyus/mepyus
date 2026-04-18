#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.execution_trace import load_trace_records
from app.core.runtime.flow_candidate_detection import detect_flow_candidates


DEFAULT_TRACE_LOG_PATH = ROOT / "runtime" / "manifests" / "execution_trace_log_v0.jsonl"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect repeated flow candidates from recorded execution traces.")
    parser.add_argument(
        "--trace-log",
        dest="trace_log_path",
        default=str(DEFAULT_TRACE_LOG_PATH),
        help="Path to execution trace jsonl log.",
    )
    return parser.parse_args()


def _resolve_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    return path


def main() -> int:
    args = _parse_args()
    trace_log_path = _resolve_path(args.trace_log_path)
    records = load_trace_records(trace_log_path)
    payload = detect_flow_candidates(records)
    payload["trace_log_path"] = str(trace_log_path)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
