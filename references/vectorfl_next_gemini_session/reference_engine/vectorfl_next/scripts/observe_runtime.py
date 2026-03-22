#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.reporting import should_issue_workspace_report
from app.runtime.reactive_space_report import write_reactive_space_report
from app.runtime.workspace_manifest import build_workspace_manifest
from app.runtime.workspace_report import write_workspace_report


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    manifest = build_workspace_manifest(runtime_root)
    report_decision = should_issue_workspace_report(runtime_root)
    report_path = write_workspace_report(runtime_root) if report_decision["issue_report"] else None
    reactive_report_path = write_reactive_space_report(runtime_root) if report_decision["issue_report"] else None

    lines = [
        "runtime_root: %s" % runtime_root,
        "coexistence_status: %s" % manifest["coexistence_status"],
        "core_total: %s" % sum(manifest["core_counts"].values()),
        "manifest_total: %s" % sum(manifest["manifest_counts"].values()),
        "legacy_count: %s" % len(manifest["legacy_paths"]),
        "issue_report: %s" % report_decision["issue_report"],
    ]
    if report_decision["reasons"]:
        lines.append("reasons:")
        for reason in report_decision["reasons"]:
            lines.append("- %s" % reason)
    if report_path is not None:
        lines.append("report_path: %s" % report_path)
    if reactive_report_path is not None:
        lines.append("reactive_report_path: %s" % reactive_report_path)
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
