#!/usr/bin/env python3
"""Tests for personal_intake_min.py.

Fixture-only local tests. Shared/live DB intake remains HOLD.
"""
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
SCHEMA = ROOT / "SCHEMA.sql"
SCRIPT = ROOT / "tools" / "personal_intake_min.py"


def counts(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    facts = {
        "requests": cur.execute("SELECT COUNT(*) FROM requests").fetchone()[0],
        "decisions": cur.execute("SELECT COUNT(*) FROM decisions").fetchone()[0],
        "executions": cur.execute("SELECT COUNT(*) FROM executions").fetchone()[0],
        "receipts": cur.execute("SELECT COUNT(*) FROM receipts").fetchone()[0],
        "reviews": cur.execute("SELECT COUNT(*) FROM reviews").fetchone()[0],
        "maturation_entries": cur.execute("SELECT COUNT(*) FROM maturation_entries").fetchone()[0],
        "fail_guardrail_events": cur.execute("SELECT COUNT(*) FROM guardrail_events WHERE result LIKE 'FAIL%'").fetchone()[0],
    }
    con.close()
    return facts


def create_fixture_db(path):
    con = sqlite3.connect(path)
    con.executescript(SCHEMA.read_text(encoding="utf-8"))
    con.commit()
    con.close()


class PersonalIntakeMinTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.tmp.name)
        self.db = self.tmp_path / "fixture.sqlite"
        self.receipt_dir = self.tmp_path / "receipts"
        create_fixture_db(self.db)
        self.env = os.environ.copy()
        self.env["VECTORFL_PHASE0_DB"] = str(self.db)

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self, extra_args):
        return subprocess.run(
            [sys.executable, str(SCRIPT)] + extra_args,
            cwd=str(REPO),
            env=self.env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def base_args(self):
        return [
            "--title", "Fixture personal intake",
            "--body", "A local personal input that should become candidate material only.",
            "--source-type", "personal_note",
            "--lens", "input_localization",
            "--boundary-level", "STANDARD",
            "--valid-for", "local review; receipt rehearsal",
            "--not-valid-for", "authority; promotion; Program Alpha",
            "--placement-candidate", "personal_program_unit_stage1_candidate",
            "--next-smallest-action", "review receipt through read-only surface",
            "--receipt-dir", str(self.receipt_dir),
        ]

    def test_fixture_db_intake_succeeds_and_writes_receipt(self):
        before = counts(self.db)
        r = self.run_script(self.base_args())
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertIn("PASS_PERSONAL_INTAKE_MIN_WITH_HOLD", r.stdout)
        after = counts(self.db)
        self.assertEqual(after["requests"], before["requests"] + 1)
        self.assertEqual(after["decisions"], before["decisions"] + 1)
        self.assertEqual(after["executions"], before["executions"] + 1)
        self.assertEqual(after["receipts"], before["receipts"] + 1)
        self.assertEqual(after["reviews"], before["reviews"] + 1)
        self.assertEqual(after["maturation_entries"], before["maturation_entries"] + 1)
        self.assertEqual(after["fail_guardrail_events"], 0)
        receipts = list(self.receipt_dir.glob("personal_intake_request_*.md"))
        self.assertEqual(len(receipts), 1)
        text = receipts[0].read_text(encoding="utf-8")
        self.assertIn("authority_status: NO", text)
        self.assertIn("promotion_status: HOLD", text)
        self.assertIn("external_execution: NO", text)

    def test_inserted_rows_preserve_hold_and_no_authority(self):
        r = self.run_script(self.base_args())
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        con = sqlite3.connect(self.db)
        con.row_factory = sqlite3.Row
        req = con.execute("SELECT * FROM requests ORDER BY id DESC LIMIT 1").fetchone()
        self.assertEqual(req["promotion_status"], "HOLD")
        self.assertEqual(req["authority_status"], "NO")
        self.assertIn("PERSONAL_INTAKE", req["depth"])
        decision = con.execute("SELECT * FROM decisions WHERE request_id=?", (req["id"],)).fetchone()
        self.assertIn("personal_note", decision["reason"])
        review = con.execute("SELECT * FROM reviews WHERE request_id=?", (req["id"],)).fetchone()
        self.assertEqual(review["promotion_status"], "HOLD")
        self.assertEqual(review["authority_status"], "NO")
        maturation = con.execute("SELECT * FROM maturation_entries WHERE request_id=?", (req["id"],)).fetchone()
        self.assertEqual(maturation["authority_mutation"], "NO")
        execution = con.execute("SELECT * FROM executions WHERE request_id=?", (req["id"],)).fetchone()
        self.assertEqual(execution["execution_type"], "LOCAL_NO_MODEL_PERSONAL_INTAKE")
        self.assertEqual(execution["output_classification"], "CANDIDATE_MATERIAL")
        con.close()

    def test_missing_required_body_fails_without_db_mutation(self):
        before = counts(self.db)
        args = self.base_args()
        body_index = args.index("--body")
        del args[body_index:body_index + 2]
        r = self.run_script(args)
        self.assertNotEqual(r.returncode, 0)
        after = counts(self.db)
        self.assertEqual(after, before)
        self.assertFalse(list(self.receipt_dir.glob("personal_intake_request_*.md")))

    def test_missing_required_title_fails_without_db_mutation(self):
        before = counts(self.db)
        args = self.base_args()
        title_index = args.index("--title")
        del args[title_index:title_index + 2]
        r = self.run_script(args)
        self.assertNotEqual(r.returncode, 0)
        after = counts(self.db)
        self.assertEqual(after, before)
        self.assertFalse(list(self.receipt_dir.glob("personal_intake_request_*.md")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
