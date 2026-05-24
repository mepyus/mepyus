#!/usr/bin/env python3
"""Create Phase 0.5 candidate baseline v1 only with explicit confirmation.

Default behavior is HOLD/no-op. To create the checkpoint, pass:
  --confirm-option-b

Local-only checkpoint creation. No authority mutation. No promotion.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
V0_SNAPSHOT = ROOT / "snapshots" / "phase0_5_candidate_baseline_v0"
V1_SNAPSHOT = ROOT / "snapshots" / "phase0_5_candidate_baseline_v1"
MANIFEST = V1_SNAPSHOT / "baseline_manifest.json"
CHECKSUMS = V1_SNAPSHOT / "baseline_checksums.tsv"
DB = ROOT / "data" / "vectorfl_ops_phase_0_5.sqlite"
PREFLIGHT_RECEIPT = ROOT / "receipts" / "phase0_5_candidate_baseline_v1_preflight_receipt.md"
STABLE_CYCLE_RECEIPT = REPO / "app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md"
RECEIPT = ROOT / "receipts" / "phase0_5_candidate_baseline_v1_snapshot_receipt.md"
EXPORT = ROOT / "exports" / "phase0_5_candidate_baseline_v1_snapshot_export.md"


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
    if path.is_dir():
        return False
    return True


def manifest_entries():
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if not should_include(path):
            continue
        entries.append(
            {
                "path": str(path),
                "relative_path": path.relative_to(ROOT).as_posix(),
                "exists": path.exists(),
                "kind": "file",
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return entries


def precheck():
    facts = db_facts()
    problems = []
    stable_text = STABLE_CYCLE_RECEIPT.read_text(encoding="utf-8") if STABLE_CYCLE_RECEIPT.exists() else ""
    preflight_text = PREFLIGHT_RECEIPT.read_text(encoding="utf-8") if PREFLIGHT_RECEIPT.exists() else ""
    if not V0_SNAPSHOT.exists():
        problems.append({"code": "V0_SNAPSHOT_MISSING", "path": str(V0_SNAPSHOT)})
    if V1_SNAPSHOT.exists():
        problems.append({"code": "V1_SNAPSHOT_ALREADY_EXISTS", "path": str(V1_SNAPSHOT)})
    if "PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD" not in stable_text:
        problems.append({"code": "STABLE_CYCLE_PASS_MISSING", "path": str(STABLE_CYCLE_RECEIPT)})
    if "PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD" not in preflight_text:
        problems.append({"code": "V1_PREFLIGHT_PASS_MISSING", "path": str(PREFLIGHT_RECEIPT)})
    if facts.get("fail_events") != 0:
        problems.append({"code": "FAIL_EVENTS_NONZERO", "detail": facts.get("fail_events")})
    if facts.get("authority_mutations") != 0:
        problems.append({"code": "AUTHORITY_MUTATIONS_NONZERO", "detail": facts.get("authority_mutations")})
    if facts.get("non_hold_reviews") != 0:
        problems.append({"code": "NON_HOLD_REVIEWS_NONZERO", "detail": facts.get("non_hold_reviews")})
    return facts, problems


def write_receipt(result):
    body = f"""# Phase 0.5 Candidate Baseline V1 Snapshot Receipt

classification: PIPELINE_PHASE0_5_CANDIDATE_BASELINE_V1_SNAPSHOT_V0
verdict: {result['verdict']}
created_at: {result['created_at']}
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO
phase1_production_readiness: NO

## Snapshot root
{V1_SNAPSHOT}

## Manifest
{MANIFEST}

## Checksums
{CHECKSUMS}

## Manifest sha256
{result.get('manifest_sha256', '')}

## DB facts
```json
{json.dumps(result['db_facts'], ensure_ascii=False, indent=2)}
```

## File count
{result.get('file_count', 0)}

## Preconditions

- stable cycle PASS before snapshot: {result['stable_cycle_pass_present']}
- v1 preflight PASS before snapshot: {result['preflight_pass_present']}
- v0 preserved: {result['v0_preserved']}
- frozen v0 replay may remain FAIL: YES

## Problems
```json
{json.dumps(result['problems'], ensure_ascii=False, indent=2)}
```

## Boundary

This is a local candidate checkpoint only. It is not authority, not promotion, not Program Alpha evidence, not M3/M4 confirmation, not router/runner implementation, and not Phase 1 production readiness.

## Next executable lane

Run live-safety after snapshot creation and keep v1 as candidate evidence only.
"""
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    EXPORT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(body, encoding="utf-8")
    EXPORT.write_text(body.replace("Receipt", "Export", 1), encoding="utf-8")


def create_snapshot():
    facts, problems = precheck()
    stable_pass = STABLE_CYCLE_RECEIPT.exists() and "PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD" in STABLE_CYCLE_RECEIPT.read_text(encoding="utf-8")
    preflight_pass = PREFLIGHT_RECEIPT.exists() and "PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD" in PREFLIGHT_RECEIPT.read_text(encoding="utf-8")
    if problems:
        result = {
            "classification": "PIPELINE_PHASE0_5_CANDIDATE_BASELINE_V1_SNAPSHOT_V0",
            "verdict": "FAIL_PHASE0_5_CANDIDATE_BASELINE_V1_SNAPSHOT_PRECHECK",
            "created_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "db_facts": facts,
            "problems": problems,
            "stable_cycle_pass_present": stable_pass,
            "preflight_pass_present": preflight_pass,
            "v0_preserved": V0_SNAPSHOT.exists(),
        }
        write_receipt(result)
        return result
    entries = manifest_entries()
    V1_SNAPSHOT.mkdir(parents=True, exist_ok=False)
    manifest = {
        "classification": "PIPELINE_PHASE0_5_CANDIDATE_BASELINE_V1_SNAPSHOT_V0",
        "verdict": "PASS_PHASE0_5_CANDIDATE_BASELINE_V1_SNAPSHOT_CREATED_WITH_HOLD",
        "created_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "root": str(ROOT),
        "snapshot_dir": str(V1_SNAPSHOT),
        "file_count": len(entries),
        "manifest_entries": entries,
        "db_facts": facts,
        "hold": {
            "promotion": "HOLD",
            "authority_mutation": "NO",
            "program_alpha": "NO",
            "m3_m4_claim": "NO",
            "router_runner_claim": "NO",
            "external_model_tool_network_execution": "NO",
            "phase1_production_readiness": "NO",
            "v0_snapshot_mutation": "NO",
        },
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    CHECKSUMS.write_text(
        "\n".join(f"{e['sha256']}\t{e['relative_path']}" for e in entries) + "\n",
        encoding="utf-8",
    )
    result = {
        **manifest,
        "manifest_sha256": sha256(MANIFEST),
        "problems": [],
        "stable_cycle_pass_present": stable_pass,
        "preflight_pass_present": preflight_pass,
        "v0_preserved": V0_SNAPSHOT.exists(),
    }
    write_receipt(result)
    return result


def main():
    parser = argparse.ArgumentParser(description="Guarded Phase 0.5 v1 candidate checkpoint creator.")
    parser.add_argument("--confirm-option-b", action="store_true", help="Explicitly approve creation of candidate baseline v1.")
    args = parser.parse_args()
    if not args.confirm_option_b:
        print("HOLD_CONFIRM_OPTION_B_REQUIRED")
        print("v1_snapshot_creation=NO")
        print("required_flag=--confirm-option-b")
        return 2
    result = create_snapshot()
    print(result["verdict"])
    print("file_count=" + str(result.get("file_count", 0)))
    print("problem_count=" + str(len(result.get("problems", []))))
    print("snapshot_dir=" + str(V1_SNAPSHOT))
    print("receipt=" + str(RECEIPT))
    return 0 if not result.get("problems") else 1


if __name__ == "__main__":
    raise SystemExit(main())
