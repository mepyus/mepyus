#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    runtime_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path("runtime").resolve()

    checks = {
        "fragments_dir": runtime_root.joinpath("fragments").exists(),
        "source_documents_dir": runtime_root.joinpath("source_documents").exists(),
        "source_report_json": runtime_root.joinpath("reports", "source_fragment_view.json").exists(),
        "measurement_report_json": runtime_root.joinpath("reports", "measurement_view.json").exists(),
        "work_session_log": runtime_root.joinpath("logs", "work_sessions", "session_20260318_180251.md").exists(),
    }

    source_summary = {}
    measurement_summary = {}
    source_report = runtime_root / "reports" / "source_fragment_view.json"
    measurement_report = runtime_root / "reports" / "measurement_view.json"

    if source_report.exists():
        source_summary = json.loads(source_report.read_text(encoding="utf-8")).get("summary", {})
    if measurement_report.exists():
        measurement_summary = json.loads(measurement_report.read_text(encoding="utf-8")).get("summary", {})

    passed = all(checks.values())
    result = {
        "runtime_root": str(runtime_root),
        "passed": passed,
        "checks": checks,
        "source_summary": source_summary,
        "measurement_summary": measurement_summary,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
