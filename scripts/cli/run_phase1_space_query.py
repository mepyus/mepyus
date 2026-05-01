#!/usr/bin/env python3
"""Entrypoint for the Phase 1/1.5 space query loop.

This creates the four handoff artifacts for a bounded CLI usage loop:
question packet, exploration result, merge/diff/hold report, and reingress
record. The generated artifacts are draft instances, not baseline locks.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def read_request(args: argparse.Namespace) -> str:
    if args.input_file:
        return args.input_file.read_text(encoding="utf-8").strip()
    if args.request:
        return args.request
    raise SystemExit("Provide a question string or --input-file.")


def default_stem() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"phase1_5_query_{stamp}"


def load_mode(report_path: Path) -> str:
    report = json.loads(report_path.read_text(encoding="utf-8"))
    return report.get("chosen_mode", "merge")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("request", nargs="?")
    parser.add_argument("--input-file", type=Path)
    parser.add_argument("--mode", choices=["exploration", "extraction", "comparison", "merge", "verification", "reflection_support"])
    parser.add_argument("--stem")
    parser.add_argument("--force-merge-mode", choices=["merge", "diff", "hold"], default="merge")
    args = parser.parse_args()
    request = read_request(args)
    stem = args.stem or default_stem()
    root = Path.cwd()
    packet = root / "runtime/query_packets" / f"{stem}_question_packet.json"
    exploration = root / "runtime/exploration_results" / f"{stem}_exploration_result.json"
    merge = root / "runtime/merge_diff_reports" / f"{stem}_merge_diff_report.json"
    reingress = root / "runtime/reingress_records" / f"{stem}_reingress_record.json"
    for path in (packet.parent, exploration.parent, merge.parent, reingress.parent):
        path.mkdir(parents=True, exist_ok=True)
    py = sys.executable
    packet_cmd = [py, "scripts/cli/build_question_packet.py", request, "--out", str(packet)]
    if args.mode:
        packet_cmd.extend(["--mode", args.mode])
    run(packet_cmd)
    run([py, "scripts/cli/explore_space.py", str(packet), "--out", str(exploration)])
    run(
        [
            py,
            "scripts/cli/merge_or_diff.py",
            str(packet),
            str(exploration),
            "--mode",
            args.force_merge_mode,
            "--out",
            str(merge),
        ]
    )
    chosen_mode = load_mode(merge)
    run(
        [
            py,
            "scripts/cli/write_reingress_record.py",
            request,
            "--mode",
            chosen_mode,
            "--question-packet",
            str(packet),
            "--exploration-result",
            str(exploration),
            "--merge-diff-report",
            str(merge),
            "--out",
            str(reingress),
        ]
    )
    summary = {
        "stem": stem,
        "chosen_mode": chosen_mode,
        "artifacts": {
            "question_packet": str(packet),
            "exploration_result": str(exploration),
            "merge_diff_report": str(merge),
            "reingress_record": str(reingress),
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
