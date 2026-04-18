import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


class StructuredDocStabilityHelpersTest(unittest.TestCase):
    def test_jsonl_recovery_drill_reports_successful_repair(self) -> None:
        proc = subprocess.run(
            [sys.executable, "scripts/run_jsonl_recovery_drill.py"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        payload = json.loads(proc.stdout)

        self.assertTrue(payload["pre_detected_malformed_tail"])
        self.assertTrue(payload["recovery_applied"])
        self.assertFalse(payload["post_detected_malformed_tail"])
        self.assertTrue(payload["backup_created"])
        self.assertEqual(payload["repaired_event_ids"], ["evt_drill_1", "evt_drill_2"])


if __name__ == "__main__":
    unittest.main()
