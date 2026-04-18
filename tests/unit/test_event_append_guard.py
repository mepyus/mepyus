import json
import tempfile
import unittest
from pathlib import Path

from app.core.events.event_append_guard import (
    append_jsonl_locked,
    load_jsonl_with_tail_recovery,
    recover_jsonl_tail,
)


class EventAppendGuardTest(unittest.TestCase):
    def test_load_jsonl_with_tail_recovery_ignores_malformed_tail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "ledger.jsonl"
            path.write_text(
                json.dumps({"event_id": "evt_1"}) + "\n" + json.dumps({"event_id": "evt_2"}) + "\n" + '{"event_id": "broken"',
                encoding="utf-8",
            )

            rows, recovered = load_jsonl_with_tail_recovery(path)

            self.assertTrue(recovered)
            self.assertEqual([row["event_id"] for row in rows], ["evt_1", "evt_2"])

    def test_recover_jsonl_tail_rewrites_only_valid_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "ledger.jsonl"
            path.write_text(
                json.dumps({"event_id": "evt_1"}) + "\n" + '{"event_id": "broken"',
                encoding="utf-8",
            )

            changed = recover_jsonl_tail(path)

            self.assertTrue(changed)
            repaired = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(repaired), 1)
            self.assertEqual(json.loads(repaired[0])["event_id"], "evt_1")
            self.assertTrue((Path(tmp_dir) / "ledger.jsonl.broken").exists())

    def test_append_jsonl_locked_appends_complete_json_line(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "ledger.jsonl"

            append_jsonl_locked(path, {"event_id": "evt_1", "status": "recorded"})
            append_jsonl_locked(path, {"event_id": "evt_2", "status": "recorded"})

            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(json.loads(lines[0])["event_id"], "evt_1")
            self.assertEqual(json.loads(lines[1])["event_id"], "evt_2")


if __name__ == "__main__":
    unittest.main()
