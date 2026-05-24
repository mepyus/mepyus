#!/usr/bin/env python3
"""Preflight Phase 0.5 candidate baseline v1 checkpoint creation.

Read-only preview of what a v1 checkpoint would capture.
Does not create the v1 snapshot directory. No authority mutation. No promotion.
"""
from pathlib import Path
import datetime
import hashlib
import json
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
V0_SNAPSHOT = ROOT / "snapshots" / "phase0_5_candidate_baseline_v0"
V1_SNAPSHOT = ROOT / "snapshots" / "phase0_5_candidate_baseline_v1"
STABLE_CYCLE_RECEIPT = REPO / "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md"
DB = ROOT / "data" / "vectorfl_ops_phase_0_5.sqlite"
RECEIPT = ROOT / "receipts" / "phase0_5_candidate_baseline_v1_preflight_receipt.md"
EXPORT = ROOT / "exports" / "phase0_5_candidate_baseline_v1_preflight_export.md"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def db_facts():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    facts = {
        "requests": cur.execute("SELECT COUNT(*) FROM requests").fetchone()[0],
        "executions": cur.execute("SELECT COUNT(*) FROM executions").fetchone()[0],
        "receipts": cur.execute("SELECT COUNT(*) FROM receipts").fetchone()[0],
        "reviews": cur.execute("SELECT COUNT(*) FROM reviews").fetchone()[0],
        "maturation_entries": cur.execute("SELECT COUNT(*) FROM maturation_entries").fetchone()[0],
        "guardrail_events": cur.execute("SELECT COUNT(*) FROM guardrail_events").fetchone()[0],
        "fail_events": cur.execute("SELECT COUNT(*) FROM guardrail_events WHERE result LIKE 'FAIL%'").fetchone()[0],
        "authority_mutations": cur.execute("SELECT COUNT(*) FROM maturation_entries WHERE authority_mutation!='NO'").fetchone()[0],
        "non_hold_reviews": cur.execute("SELECT COUNT(*) FROM reviews WHERE promotion_status!='HOLD' OR authority_status!='NO'").fetchone()[0],
        "probe_requests": cur.execute("SELECT COUNT(*) FROM requests WHERE title LIKE 'Probe %'").fetchone()[0],
    }
    con.close()
    return facts


def should_include(path):
    rel = path.relative_to(ROOT)
    parts = set(rel.parts)
    if "__pycache__" in parts:
        return False
    if "snapshots" in parts:
        return False
    if path.name == ".DS_Store":
        return False
    if path.name in {
        "phase0_5_candidate_baseline_v1_preflight_receipt.md",
        "phase0_5_candidate_baseline_v1_preflight_export.md",
    }:
        return False
    if path.is_dir():
        return False
    return True


def manifest_preview():
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if not should_include(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        entries.append(
            {
                "path": str(path),
                "relative_path": rel,
                "exists": path.exists(),
                "kind": "file",
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return entries


def write_receipt(result):
    body = f"""# Phase 0.5 Candidate Baseline V1 Preflight Receipt

classification: PIPELINE_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_V0
verdict: {result['verdict']}
created_at: {result['created_at']}

## Scope

This is a read-only preflight for a possible `phase0_5_candidate_baseline_v1` checkpoint.

It does not create the v1 snapshot directory and does not write a v1 manifest or checksum file.

## Preflight Facts

- candidate_file_count: {result['candidate_file_count']}
- problem_count: {result['problem_count']}
- v0_snapshot_present: {result['v0_snapshot_present']}
- v1_snapshot_already_exists: {result['v1_snapshot_already_exists']}
- stable_cycle_pass_present: {result['stable_cycle_pass_present']}

## DB Facts

```json
{json.dumps(result['db_facts'], ensure_ascii=False, indent=2)}
```

## Problems

```json
{json.dumps(result['problems'], ensure_ascii=False, indent=2)}
```

## Preview

```json
{json.dumps(result, ensure_ascii=False, indent=2)}
```

## Boundary

authority mutation: NO
promotion: HOLD
Program Alpha evidence: NO
M3/M4 claim: NO
router/runner claim: NO
external model/tool/network execution: NO
v1 snapshot creation: NO
v0 snapshot mutation: NO
schema/registry mutation: NO

## Next Smallest Action

If the user explicitly approves Option B, execute the bounded Hermes v1 checkpoint packet. Otherwise keep v1 snapshot creation on HOLD.
"""
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    EXPORT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(body, encoding="utf-8")
    EXPORT.write_text(body.replace("Receipt", "Export", 1), encoding="utf-8")


def main():
    facts = db_facts()
    problems = []
    stable_text = STABLE_CYCLE_RECEIPT.read_text(encoding="utf-8") if STABLE_CYCLE_RECEIPT.exists() else ""
    stable_pass = "PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD" in stable_text
    if not V0_SNAPSHOT.exists():
        problems.append({"code": "V0_SNAPSHOT_MISSING", "path": str(V0_SNAPSHOT)})
    if V1_SNAPSHOT.exists():
        problems.append({"code": "V1_SNAPSHOT_ALREADY_EXISTS", "path": str(V1_SNAPSHOT)})
    if not stable_pass:
        problems.append({"code": "STABLE_CYCLE_PASS_MISSING", "path": str(STABLE_CYCLE_RECEIPT)})
    if facts.get("fail_events") != 0:
        problems.append({"code": "FAIL_EVENTS_NONZERO", "detail": facts.get("fail_events")})
    if facts.get("authority_mutations") != 0:
        problems.append({"code": "AUTHORITY_MUTATIONS_NONZERO", "detail": facts.get("authority_mutations")})
    if facts.get("non_hold_reviews") != 0:
        problems.append({"code": "NON_HOLD_REVIEWS_NONZERO", "detail": facts.get("non_hold_reviews")})
    entries = manifest_preview()
    result = {
        "classification": "PIPELINE_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_V0",
        "verdict": "PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD" if not problems else "FAIL_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT",
        "created_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "root": str(ROOT),
        "candidate_snapshot_dir": str(V1_SNAPSHOT),
        "candidate_file_count": len(entries),
        "problem_count": len(problems),
        "problems": problems,
        "v0_snapshot_present": V0_SNAPSHOT.exists(),
        "v1_snapshot_already_exists": V1_SNAPSHOT.exists(),
        "stable_cycle_pass_present": stable_pass,
        "db_facts": facts,
        "manifest_preview_entries": entries,
        "hold": {
            "authority_mutation": "NO",
            "promotion": "HOLD",
            "program_alpha": "NO",
            "m3_m4_claim": "NO",
            "router_runner_claim": "NO",
            "external_model_tool_network_execution": "NO",
            "v1_snapshot_creation": "NO",
            "v0_snapshot_mutation": "NO",
            "schema_registry_mutation": "NO",
        },
    }
    write_receipt(result)
    print(result["verdict"])
    print("candidate_file_count=" + str(result["candidate_file_count"]))
    print("problem_count=" + str(result["problem_count"]))
    print("receipt=" + str(RECEIPT))
    print("export=" + str(EXPORT))
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
