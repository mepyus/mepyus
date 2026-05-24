#!/usr/bin/env python3
"""Bounded local simulation of a Gemini script lens runner.
No network. No Gemini/Codex invocation. Reads only request-declared local input files.
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

FORBIDDEN_MARKERS = [
    "component approved", "workflow approved", "baseline confirmed",
    "update memory", "write SKILL.md", "authority mutation",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: gemini_lens_runner_sim.py REQUEST_JSON", file=sys.stderr)
        return 2

    request_path = Path(sys.argv[1]).resolve()
    request = json.loads(request_path.read_text(encoding="utf-8"))
    output_dir = Path(request["output_dir"]).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    files_read = [str(request_path)]
    observed = []
    combined = []
    for p in request.get("input_files", []):
        path = Path(p).resolve()
        if not path.exists():
            raise FileNotFoundError(str(path))
        text = path.read_text(encoding="utf-8")
        files_read.append(str(path))
        observed.append({"path": str(path), "chars": len(text), "lines": len(text.splitlines())})
        combined.append(text.lower())

    corpus = "\n".join(combined)
    patterns = []
    for phrase in ["hermes", "codex", "gemini", "receipt", "authority", "promotion", "runner", "lite output"]:
        count = corpus.count(phrase)
        if count:
            patterns.append({"pattern": phrase, "count": count})

    lite = {
        "format": "GEMINI_BULK_REVIEW_LITE_SIMULATED",
        "observed_files": observed,
        "repeated_patterns": patterns,
        "candidate_items": [
            "script lens can reduce Codex runtime burden by producing bounded lite output",
            "raw/lite output split supports Codex reading lite by default",
            "runner ownership must remain tool/lens executor, not judge"
        ],
        "uncertainties": [
            "real Gemini CLI/API latency and output stability not tested",
            "model API transport boundary remains design-only in this simulation"
        ],
        "possible_risks": [
            "runner output being treated as truth",
            "script runner becoming automation bridge",
            "Codex recovery check being skipped"
        ],
        "do_not_promote": [
            "do not promote this simulation to component/workflow/schema/registry/ontology/baseline",
            "do not treat simulated runner success as Gemini runtime validation"
        ],
        "questions_for_codex": [
            "Is lite output sufficient for recovery check without raw reread?",
            "What exact fields should CODEX_WORKER_REQUEST_V0 require?"
        ],
        "raw_limits": [
            "local simulation only",
            "no real Gemini execution",
            "no model API transport",
            "no live web/source lookup"
        ]
    }

    raw = {
        "format": "GEMINI_RAW_OUTPUT_SIMULATED",
        "request_id": request.get("request_id"),
        "simulated_observation": "Declared files were read and reduced into lite output by a bounded local script.",
        "full_observed_text_lowercase_sample": corpus[:1200],
        "non_authority_statement": "This raw output is evidence only, not truth or promotion."
    }

    receipt = {
        "verdict": "GEMINI_SCRIPT_RUNNER_BOUNDARY_SANDBOX_SIMULATION_RETURNED_WITH_WATCH",
        "request_path": str(request_path),
        "files_read": files_read,
        "files_written": [],
        "codex_executed": False,
        "gemini_executed": False,
        "simulated_gemini_only": True,
        "network_used": False,
        "model_api_transport_used": False,
        "live_web_lookup_used": False,
        "external_connector_used": False,
        "memory_modified": False,
        "skill_modified": False,
        "cron_modified": False,
        "config_modified": False,
        "vectorfl_authority_modified": False,
        "promotion_performed": False,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    raw_path = output_dir / "gemini_raw_output_simulated.json"
    lite_path = output_dir / "gemini_lite_output_simulated.json"
    receipt_path = output_dir / "runner_receipt.json"
    report_path = output_dir / "sandbox_feasibility_report.md"

    raw_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lite_path.write_text(json.dumps(lite, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    receipt["files_written"] = [str(raw_path), str(lite_path), str(receipt_path), str(report_path)]
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = f"""# Gemini Script Runner Boundary Sandbox v0

## Verdict

GEMINI_SCRIPT_RUNNER_BOUNDARY_SANDBOX_SIMULATION_RETURNED_WITH_WATCH

## What Was Tested

A Codex-authored request file was consumed by a bounded local script runner.
The runner read only declared local input files and produced raw + lite outputs.
This simulated Gemini as a script lens without invoking Gemini, Codex, network, browser, MCP, or connectors.

## Feasibility Judgment

The structure is feasible as a Level 1.5 / cautious Level 2 design pattern.
The key workable split is:

```text
Codex: request author + recovery judge
Hermes: workbench / possible runner host
Gemini script lens: bounded bulk output producer
User: approval
```

## Files

request: {request_path}
raw_output: {raw_path}
lite_output: {lite_path}
receipt: {receipt_path}

## WATCH

- simulated success is not real Gemini validation
- runner output must not become truth
- Codex recovery check must remain required
- model API transport remains untested
- script runner must not become recurring automation

## HOLD

- no real Codex run
- no real Gemini run
- no bridge connection
- no network/API/browser/MCP
- no external connector
- no memory/skill/cron/config mutation
- no VectorFL authority mutation
- no promotion

## Next Smallest Action

Draft GEMINI_SCRIPT_RUNNER_BOUNDARY_MODEL_V0 or CODEX_WORKER_REQUEST_V0 as template only.
Do not execute a real Gemini runner until model API transport and exact command are packet-approved.
"""
    report_path.write_text(report, encoding="utf-8")
    print(json.dumps({"ok": True, "report": str(report_path), "receipt": str(receipt_path), "lite": str(lite_path)}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
