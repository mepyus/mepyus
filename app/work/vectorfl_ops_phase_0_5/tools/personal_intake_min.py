#!/usr/bin/env python3
"""Minimal personal intake for Stage 1 VectorFL personal program unit.

Local-only. No model/API/network execution. No authority mutation. No promotion.
Designed fixture-first through VECTORFL_PHASE0_DB.
"""
from pathlib import Path
import argparse
import datetime
import json
import os
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "vectorfl_ops_phase_0_5.sqlite"
DEFAULT_RECEIPT_DIR = ROOT / "receipts" / "personal_intake"


def db_path():
    return Path(os.environ.get("VECTORFL_PHASE0_DB", str(DEFAULT_DB)))


def require_text(name, value):
    if value is None or not value.strip():
        raise ValueError(f"{name} is required")
    return value.strip()


def connect(path):
    if not path.exists():
        raise FileNotFoundError(str(path))
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    return con


def write_receipt(receipt_dir, result):
    receipt_dir = Path(receipt_dir)
    receipt_dir.mkdir(parents=True, exist_ok=True)
    path = receipt_dir / f"personal_intake_request_{result['request_id']:03d}.md"
    body = f"""# Personal Intake Receipt

classification: VECTORFL_PERSONAL_INTAKE_MIN_V0
verdict: {result['verdict']}
created_at: {result['created_at']}

## Request

- request_id: {result['request_id']}
- title: {result['title']}
- source_type: {result['source_type']}
- lens: {result['lens']}
- boundary_level: {result['boundary_level']}
- placement_candidate: {result['placement_candidate']}

## Boundary

- authority_status: NO
- promotion_status: HOLD
- external_execution: NO
- real_company_data: NO
- program_alpha_evidence: NO
- router_runner_claim: NO

## Valid For

{result['valid_for']}

## Not Valid For

{result['not_valid_for']}

## Next Smallest Action

{result['next_smallest_action']}
"""
    path.write_text(body, encoding="utf-8")
    return path


def intake(args):
    title = require_text("title", args.title)
    body = require_text("body", args.body)
    source_type = require_text("source_type", args.source_type)
    lens = require_text("lens", args.lens)
    boundary_level = require_text("boundary_level", args.boundary_level)
    valid_for = require_text("valid_for", args.valid_for)
    not_valid_for = require_text("not_valid_for", args.not_valid_for)
    placement_candidate = require_text("placement_candidate", args.placement_candidate)
    next_smallest_action = args.next_smallest_action.strip() if args.next_smallest_action else "review personal intake receipt and keep HOLD"
    now = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    path = db_path()
    with connect(path) as con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO requests
            (title, body, depth, state, source_known, audience_known, sensitivity_known,
             promotion_status, authority_status)
            VALUES (?, ?, 'PERSONAL_INTAKE', 'MATURED_OR_HELD', 1, 1, 1, 'HOLD', 'NO')""",
            (title, body),
        )
        request_id = cur.lastrowid
        cur.execute(
            "INSERT INTO decisions (request_id, decision, reason) VALUES (?, ?, ?)",
            (
                request_id,
                "PERSONAL_INTAKE_PLACED_WITH_HOLD",
                f"source_type={source_type}; lens={lens}; boundary={boundary_level}; placement={placement_candidate}",
            ),
        )
        cur.execute(
            "INSERT INTO executions (request_id, execution_type, status, output_classification) VALUES (?, 'LOCAL_NO_MODEL_PERSONAL_INTAKE', 'CREATED', 'CANDIDATE_MATERIAL')",
            (request_id,),
        )
        execution_id = cur.lastrowid
        receipt_content = (
            "Personal intake captured as candidate material with HOLD. "
            f"Valid for: {valid_for}. Not valid for: {not_valid_for}."
        )
        cur.execute(
            "INSERT INTO receipts (request_id, execution_id, content) VALUES (?, ?, ?)",
            (request_id, execution_id, receipt_content),
        )
        cur.execute(
            "INSERT INTO reviews (request_id, verdict, next_smallest_action, promotion_status, authority_status) VALUES (?, 'PASS_PERSONAL_INTAKE_WITH_HOLD', ?, 'HOLD', 'NO')",
            (request_id, next_smallest_action),
        )
        cur.execute(
            "INSERT INTO maturation_entries (request_id, summary, next_work_easier_value, authority_mutation) VALUES (?, ?, ?, 'NO')",
            (
                request_id,
                "Personal intake preserved as local candidate evidence.",
                "Future personal inputs can reuse the same intake/receipt pattern.",
            ),
        )
        con.commit()
    result = {
        "classification": "VECTORFL_PERSONAL_INTAKE_MIN_V0",
        "verdict": "PASS_PERSONAL_INTAKE_MIN_WITH_HOLD",
        "created_at": now,
        "db": str(path),
        "request_id": request_id,
        "execution_id": execution_id,
        "title": title,
        "source_type": source_type,
        "lens": lens,
        "boundary_level": boundary_level,
        "valid_for": valid_for,
        "not_valid_for": not_valid_for,
        "placement_candidate": placement_candidate,
        "next_smallest_action": next_smallest_action,
        "hold": {
            "authority_mutation": "NO",
            "promotion": "HOLD",
            "program_alpha": "NO",
            "external_model_tool_network_execution": "NO",
            "router_runner_claim": "NO",
        },
    }
    receipt_path = write_receipt(args.receipt_dir, result)
    result["receipt_path"] = str(receipt_path)
    return result


def build_parser():
    parser = argparse.ArgumentParser(description="Minimal local personal intake with HOLD boundary.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--source-type", required=True)
    parser.add_argument("--lens", required=True)
    parser.add_argument("--boundary-level", required=True)
    parser.add_argument("--valid-for", required=True)
    parser.add_argument("--not-valid-for", required=True)
    parser.add_argument("--placement-candidate", required=True)
    parser.add_argument("--next-smallest-action", default="")
    parser.add_argument("--receipt-dir", default=str(DEFAULT_RECEIPT_DIR))
    parser.add_argument("--json", action="store_true")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = intake(args)
    except Exception as exc:
        print("PERSONAL_INTAKE_MIN_FAIL", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(result["verdict"])
        print("request_id=" + str(result["request_id"]))
        print("receipt=" + result["receipt_path"])
        print("authority_mutation=NO")
        print("promotion=HOLD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
