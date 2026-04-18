from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROCESS_SCRIPT = REPO_ROOT / "scripts" / "process_structured_doc_with_routing.py"
DOC_PATH = REPO_ROOT / "codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md"
REGISTRY_PATH = REPO_ROOT / "runtime" / "manifests" / "structured_internal_docs_registry_v1.json"
TICKET_PATH = REPO_ROOT / "runtime" / "manifests" / "ticket_registry_v1.json"
PROVENANCE_PATH = REPO_ROOT / "runtime" / "manifests" / "provenance_link_index_v1.json"
RECEIPT_PATH = REPO_ROOT / "runtime" / "receipts" / "doc_codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1_operation_receipt.md"
BOARD_PATH = REPO_ROOT / "runtime" / "views" / "operation_board_latest.md"
COMMANDS_PATH = REPO_ROOT / "runtime" / "commands" / "structured_doc_routing_commands_v1.md"
LEDGER_PATH = REPO_ROOT / "runtime" / "events" / "engine_event_ledger.jsonl"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    process_count = 4
    procs = [
        subprocess.Popen(
            [sys.executable, str(PROCESS_SCRIPT), "--doc", str(DOC_PATH.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(process_count)
    ]

    run_payloads = []
    failures = []
    for proc in procs:
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            failures.append({"returncode": proc.returncode, "stderr": stderr})
            continue
        run_payloads.append(json.loads(stdout))

    registry = read_json(REGISTRY_PATH)
    tickets = read_json(TICKET_PATH)
    provenance = read_json(PROVENANCE_PATH)
    ledger_tail = LEDGER_PATH.read_text(encoding="utf-8").splitlines()[-40:]
    receipt_text = RECEIPT_PATH.read_text(encoding="utf-8")
    board_text = BOARD_PATH.read_text(encoding="utf-8")
    commands_text = COMMANDS_PATH.read_text(encoding="utf-8")

    doc_id = "doc_codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1"
    ticket_id = "tkt_process_codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1"
    registry_entry = next(row for row in registry["entries"] if row["doc_id"] == doc_id)
    ticket_entry = next(row for row in tickets["entries"] if row["ticket_id"] == ticket_id)
    provenance_matches = [
        row for row in provenance["links"] if row["source_doc_ref"] == "codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md"
    ]
    run_ids = [payload["run_id"] for payload in run_payloads]

    summary = {
        "requested_process_count": process_count,
        "successful_runs": len(run_payloads),
        "failed_runs": len(failures),
        "unique_run_ids": len({payload["run_id"] for payload in run_payloads}),
        "same_idempotency_key_for_all_runs": len({payload["idempotency_key"] for payload in run_payloads}) == 1 if run_payloads else False,
        "registry_entry_has_last_run_id": "last_run_id" in registry_entry,
        "ticket_entry_has_last_run_id": "last_run_id" in ticket_entry,
        "registry_last_run_in_observed_runs": registry_entry.get("last_run_id") in run_ids,
        "ticket_last_run_in_observed_runs": ticket_entry.get("last_run_id") in run_ids,
        "receipt_contains_any_latest_run": any(run_id in receipt_text for run_id in run_ids),
        "board_contains_any_latest_run": any(run_id in board_text for run_id in run_ids),
        "commands_contains_any_latest_run": any(run_id in commands_text for run_id in run_ids),
        "provenance_rows_for_doc": len(provenance_matches),
        "ledger_tail_lines": len(ledger_tail),
        "json_files_parse_ok": True,
        "failures": failures,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
