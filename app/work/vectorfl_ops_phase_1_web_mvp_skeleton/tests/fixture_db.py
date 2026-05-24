#!/usr/bin/env python3
"""Deterministic Phase 0.5 fixture DB for Phase 1 read-only server tests.

Local-only test material. No authority mutation. No promotion.
"""
from pathlib import Path
import sqlite3

PHASE0_ROOT = Path(__file__).resolve().parents[2] / "vectorfl_ops_phase_0_5"
SCHEMA = PHASE0_ROOT / "SCHEMA.sql"


def create_fixture_db(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    con = sqlite3.connect(path)
    try:
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        cur = con.cursor()
        requests = [
            ("Run 001 LIGHT meeting summary", "Summarize local meeting notes.", "LIGHT", "REVIEWED"),
            ("Run 002 STANDARD shorts script", "Recover a shorts script from local notes.", "STANDARD", "REVIEWED"),
            ("Run 003 DEEP repo feature", "Inspect local repo feature evidence.", "DEEP", "REVIEWED"),
            ("Run 004 BLOCKED authority request", "Request authority mutation without approval.", "BLOCKED", "STOPPED"),
            ("Probe G1 direct transition", "Negative guardrail probe for direct transition.", "PROBE", "STOPPED"),
            ("Probe G6 close without receipt", "Negative guardrail probe for missing receipt.", "PROBE", "STOPPED"),
            ("Probe G8 close without review", "Negative guardrail probe for missing review.", "PROBE", "STOPPED"),
        ]
        for title, body, depth, state in requests:
            cur.execute(
                """INSERT INTO requests
                (title, body, depth, state, source_known, audience_known, sensitivity_known,
                 promotion_status, authority_status)
                VALUES (?, ?, ?, ?, 1, 1, 1, 'HOLD', 'NO')""",
                (title, body, depth, state),
            )
        for rid in range(1, 5):
            cur.execute(
                "INSERT INTO decisions (request_id, decision, reason) VALUES (?, 'KEEP_HOLD', 'fixture preserves review-only candidate boundary')",
                (rid,),
            )
        for rid in range(1, 4):
            cur.execute(
                "INSERT INTO executions (request_id, execution_type, status, output_classification) VALUES (?, 'LOCAL_NO_MODEL', 'CREATED', 'CANDIDATE_MATERIAL')",
                (rid,),
            )
            cur.execute(
                "INSERT INTO receipts (request_id, execution_id, content) VALUES (?, ?, ?)",
                (rid, rid, f"Fixture receipt for request {rid}; HOLD maintained."),
            )
            cur.execute(
                "INSERT INTO reviews (request_id, verdict, next_smallest_action, promotion_status, authority_status) VALUES (?, 'PASS_WITH_HOLD', 'continue bounded local review', 'HOLD', 'NO')",
                (rid,),
            )
            cur.execute(
                "INSERT INTO maturation_entries (request_id, summary, next_work_easier_value, authority_mutation) VALUES (?, 'candidate material only', 'fixture supports deterministic Phase 1 read tests', 'NO')",
                (rid,),
            )
        cur.execute(
            "INSERT INTO reviews (request_id, verdict, next_smallest_action, promotion_status, authority_status) VALUES (4, 'STOP_WITH_HOLD', 'keep blocked authority request as residue', 'HOLD', 'NO')"
        )
        cur.execute(
            "INSERT INTO maturation_entries (request_id, summary, next_work_easier_value, authority_mutation) VALUES (4, 'blocked authority request retained as negative evidence', 'fixture keeps STOP path visible', 'NO')"
        )
        cur.execute(
            "INSERT INTO receipts (request_id, execution_id, content) VALUES (7, NULL, 'Intentional G8 receipt without review residue.')"
        )
        guardrails = [
            (1, "SOURCE_BOUNDARY", "PASS_BLOCKED", "local-only boundary preserved"),
            (1, "AUTHORITY", "PASS_BLOCKED", "authority mutation blocked"),
            (1, "PROMOTION", "PASS_BLOCKED", "promotion held"),
            (1, "RECEIPT", "PASS_BLOCKED", "receipt required"),
            (1, "REVIEW", "PASS_BLOCKED", "review required"),
            (2, "SOURCE_BOUNDARY", "PASS_BLOCKED", "local-only boundary preserved"),
            (2, "AUTHORITY", "PASS_BLOCKED", "authority mutation blocked"),
            (2, "PROMOTION", "PASS_BLOCKED", "promotion held"),
            (2, "RECEIPT", "PASS_BLOCKED", "receipt required"),
            (2, "REVIEW", "PASS_BLOCKED", "review required"),
            (3, "SOURCE_BOUNDARY", "PASS_BLOCKED", "local-only boundary preserved"),
            (3, "AUTHORITY", "PASS_BLOCKED", "authority mutation blocked"),
            (3, "PROMOTION", "PASS_BLOCKED", "promotion held"),
            (3, "RECEIPT", "PASS_BLOCKED", "receipt required"),
            (3, "REVIEW", "PASS_BLOCKED", "review required"),
            (4, "AUTHORITY_REQUEST", "PASS_BLOCKED", "blocked request did not mutate authority"),
            (4, "PROMOTION_REQUEST", "PASS_BLOCKED", "blocked request did not promote"),
            (4, "NO_EXTERNAL_EXECUTION", "PASS_BLOCKED", "external execution absent"),
            (4, "STOP_PATH", "PASS_BLOCKED", "blocked path retained"),
            (5, "G1", "PASS_BLOCKED", "direct transition blocked"),
            (6, "G6", "PASS_BLOCKED", "close without receipt blocked"),
            (7, "G8", "PASS_BLOCKED", "close without review blocked"),
        ]
        cur.executemany(
            "INSERT INTO guardrail_events (request_id, guardrail, result, detail) VALUES (?, ?, ?, ?)",
            guardrails,
        )
        con.commit()
    finally:
        con.close()
    return path
