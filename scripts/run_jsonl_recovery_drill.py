from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.events.event_append_guard import load_jsonl_with_tail_recovery, recover_jsonl_tail


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        ledger_path = Path(tmp_dir) / "drill_ledger.jsonl"
        ledger_path.write_text(
            json.dumps({"event_id": "evt_drill_1", "status": "recorded"}) + "\n"
            + json.dumps({"event_id": "evt_drill_2", "status": "recorded"}) + "\n"
            + '{"event_id":"evt_drill_broken","status":"recorded"',
            encoding="utf-8",
        )

        pre_rows, pre_detected_malformed_tail = load_jsonl_with_tail_recovery(ledger_path)
        recovery_applied = recover_jsonl_tail(ledger_path)
        post_rows, post_detected_malformed_tail = load_jsonl_with_tail_recovery(ledger_path)
        broken_backup = ledger_path.with_suffix(ledger_path.suffix + ".broken")

        summary = {
            "drill_path": str(ledger_path),
            "pre_valid_rows": len(pre_rows),
            "pre_detected_malformed_tail": pre_detected_malformed_tail,
            "recovery_applied": recovery_applied,
            "post_valid_rows": len(post_rows),
            "post_detected_malformed_tail": post_detected_malformed_tail,
            "backup_created": broken_backup.exists(),
            "backup_size": broken_backup.stat().st_size if broken_backup.exists() else 0,
            "repaired_event_ids": [row["event_id"] for row in post_rows],
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
