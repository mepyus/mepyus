#!/usr/bin/env python3
"""Run the Phase 1 deterministic stable-cycle checks.

Local-only verification wrapper. Uses existing tests and replay tools.
No snapshot refresh. No authority mutation. No promotion.
"""
from pathlib import Path
import datetime
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
REPORT = ROOT / "reports" / "phase1_deterministic_stable_cycle_report.json"
RECEIPT = ROOT / "receipts" / "phase1_deterministic_stable_cycle_receipt.md"
EXPORT = ROOT / "exports" / "phase1_deterministic_stable_cycle_export.md"


COMMANDS = [
    {
        "name": "py_compile_phase1_deterministic_files",
        "argv": [
            sys.executable,
            "-m",
            "py_compile",
            "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/fixture_db.py",
            "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_phase1_server.py",
            "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py",
            "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py",
            "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/api_contract_replay.py",
            "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/api_drift_replay_gate.py",
        ],
    },
    {
        "name": "phase1_server_tests",
        "argv": [sys.executable, "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_phase1_server.py"],
    },
    {
        "name": "phase1_readonly_contract_tests",
        "argv": [sys.executable, "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py"],
    },
    {
        "name": "phase1_ui_surface_tests",
        "argv": [sys.executable, "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py"],
    },
    {
        "name": "phase1_api_contract_replay",
        "argv": [sys.executable, "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/api_contract_replay.py"],
    },
    {
        "name": "phase1_api_drift_replay_gate",
        "argv": [sys.executable, "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/api_drift_replay_gate.py"],
    },
    {
        "name": "phase0_5_live_safety",
        "argv": [
            sys.executable,
            "app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py",
            "--mode",
            "live-safety",
        ],
    },
]


def run_command(item):
    proc = subprocess.run(
        item["argv"],
        cwd=str(REPO),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
    )
    return {
        "name": item["name"],
        "argv": item["argv"],
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "passed": proc.returncode == 0,
    }


def write_receipt(report):
    results_md = "\n".join(
        f"- {r['name']}: {'PASS' if r['passed'] else 'FAIL'}"
        for r in report["results"]
    )
    body = f"""# Phase 1 Deterministic Stable Cycle Receipt

classification: PIPELINE_PHASE1_DETERMINISTIC_STABLE_CYCLE_V0
verdict: {report['verdict']}
created_at: {report['created_at']}

## Scope

This stable cycle verifies deterministic Phase 1 read-only server tests and API replay tooling against generated fixture DBs.

It does not refresh the API snapshot and does not create a Phase 0.5 v1 checkpoint.

## Results

{results_md}

## Report

```json
{json.dumps(report, ensure_ascii=False, indent=2)}
```

## Boundary

promotion: HOLD
authority mutation: NO
Program Alpha evidence: NO
M3/M4 claim: NO
router/runner claim: NO
external model/tool/network execution: NO
snapshot refresh: NO
v1 checkpoint creation: NO

## Next Smallest Action

Use this stable-cycle PASS as candidate evidence for deciding whether to create a Phase 0.5 v1 candidate checkpoint, while keeping promotion and authority HOLD.
"""
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    EXPORT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(body, encoding="utf-8")
    EXPORT.write_text(body.replace("Receipt", "Export", 1), encoding="utf-8")


def main():
    results = [run_command(item) for item in COMMANDS]
    problems = [r["name"] for r in results if not r["passed"]]
    report = {
        "classification": "PIPELINE_PHASE1_DETERMINISTIC_STABLE_CYCLE_V0",
        "verdict": "PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD" if not problems else "FAIL_PHASE1_DETERMINISTIC_STABLE_CYCLE",
        "created_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "problem_count": len(problems),
        "problems": problems,
        "results": results,
        "hold": {
            "promotion": "HOLD",
            "authority_mutation": "NO",
            "program_alpha": "NO",
            "m3_m4_claim": "NO",
            "router_runner_claim": "NO",
            "external_model_tool_network_execution": "NO",
            "snapshot_refresh": "NO",
            "v1_checkpoint_creation": "NO",
        },
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    write_receipt(report)
    print(report["verdict"])
    print("problem_count=" + str(report["problem_count"]))
    print("report=" + str(REPORT))
    print("receipt=" + str(RECEIPT))
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
