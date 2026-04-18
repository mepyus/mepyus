#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCOPE_REF = "openai_02_11"
DEFAULT_RECEIPT = "runtime/receipts/doc_process_console_state_wiring_v1_operation_receipt.md"
DEFAULT_ENGINE_STATE = "runtime/views/engine_state_latest/openai_02_11.json"
DEFAULT_ENGINE_EVENT = "runtime/views/engine_state_update_events/openai_02_11.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    scope_ref = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCOPE_REF
    cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "build_reconstruction_supervisor_surface.py"),
        "--scope-ref",
        scope_ref,
        "--receipt",
        DEFAULT_RECEIPT,
        "--engine-state",
        DEFAULT_ENGINE_STATE,
        "--engine-event",
        DEFAULT_ENGINE_EVENT,
    ]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    result = json.loads(proc.stdout)

    packet_path = REPO_ROOT / result["json_ref"]
    latest_path = REPO_ROOT / result["latest_json_ref"]
    packet = load_json(packet_path)
    latest = load_json(latest_path)
    state_context = packet.get("state_context", {})

    checks = {
        "state_ref_present": state_context.get("engine_state_latest_ref") == DEFAULT_ENGINE_STATE,
        "event_ref_present": state_context.get("engine_state_update_event_ref") == DEFAULT_ENGINE_EVENT,
        "changed_fields_list_present": isinstance(state_context.get("changed_canonical_fields"), list),
        "latest_traceability_present": state_context.get("latest_traceability_status") is not None,
        "linked_views_include_state": DEFAULT_ENGINE_STATE in packet.get("linked_views", []),
        "linked_views_include_event": DEFAULT_ENGINE_EVENT in packet.get("linked_views", []),
        "state_selection_is_explicit": packet.get("selection_trace", {}).get("state_selection", {}).get("strategy") == "explicit",
        "latest_is_pointer_surface": latest.get("kind") == "bounded_reconstruction_supervisor_latest_pointer_v1",
        "non_governing_guard": packet.get("guards", {}).get("not_decision_surface") is True,
        "no_state_mutation": packet.get("guards", {}).get("state_mutation_performed") is False,
    }

    output = {
        "scope_ref": scope_ref,
        "passed": all(checks.values()),
        "checks": checks,
        "result": result,
        "state_context": state_context,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
