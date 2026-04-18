from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROCESS_SCRIPT = REPO_ROOT / "scripts" / "process_structured_doc_with_routing.py"
DOC_PATH = REPO_ROOT / "codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md"
RECEIPT_PATH = REPO_ROOT / "runtime" / "receipts" / "doc_codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1_operation_receipt.md"
LEDGER_PATH = REPO_ROOT / "runtime" / "events" / "engine_event_ledger.jsonl"


def main() -> None:
    first = subprocess.run(
        [sys.executable, str(PROCESS_SCRIPT), "--doc", str(DOC_PATH.relative_to(REPO_ROOT))],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    second = subprocess.run(
        [sys.executable, str(PROCESS_SCRIPT), "--doc", str(DOC_PATH.relative_to(REPO_ROOT))],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    first_payload = json.loads(first.stdout)
    second_payload = json.loads(second.stdout)
    receipt_text = RECEIPT_PATH.read_text(encoding="utf-8")
    ledger_tail = LEDGER_PATH.read_text(encoding="utf-8").splitlines()[-12:]

    summary = {
        "doc_ref": first_payload["doc_ref"],
        "first_run_id": first_payload["run_id"],
        "second_run_id": second_payload["run_id"],
        "same_idempotency_key": first_payload["idempotency_key"] == second_payload["idempotency_key"],
        "receipt_has_second_run_id": second_payload["run_id"] in receipt_text,
        "latest_commands_exists": (REPO_ROOT / second_payload["generated_files"][7]).exists(),
        "per_run_commands_exists": (REPO_ROOT / second_payload["generated_files"][8]).exists(),
        "per_run_board_exists": (REPO_ROOT / second_payload["generated_files"][-1]).exists(),
        "ledger_tail_lines": len(ledger_tail),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
