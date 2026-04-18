from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parent.parent
SLOT_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_actual_export_host_record_slot_v0.json"
RESULT_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_actual_export_gate_validation_latest_v0.json"
DRY_RUN_RESULT_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_actual_export_gate_validation_dry_run_v0.json"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _record_ref(slot: Dict[str, Any]) -> str:
    return (
        slot.get("current_validation_anchor_ref")
        or slot.get("current_placeholder_ref")
        or ""
    )


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _check_shape(record: Dict[str, Any]) -> List[str]:
    checks: List[str] = []
    issue = record.get("issues_row", {})
    run = record.get("heartbeat_runs_row", {})
    comments = record.get("issue_comments_rows", [])
    approval = record.get("approvals_row", {})
    if all(_has_text(issue.get(key)) for key in ("id", "title", "description", "status")):
        checks.append("issues_row has id/title/description/status")
    if all(_has_text(run.get(key)) for key in ("id", "status", "startedAt")) and isinstance(run.get("resultJson"), dict):
        checks.append("heartbeat_runs_row has id/status/startedAt/resultJson")
    if isinstance(comments, list) and comments and all(_has_text(item.get("body")) for item in comments if isinstance(item, dict)):
        checks.append("issue_comments_rows has at least one body-bearing comment")
    if all(_has_text(approval.get(key)) for key in ("id", "status", "decisionNote")) and isinstance(approval.get("payload"), dict):
        checks.append("approvals_row has id/status/decisionNote/payload")
    return checks


def _check_mapping(record: Dict[str, Any]) -> List[str]:
    checks: List[str] = []
    issue = record.get("issues_row", {})
    run = record.get("heartbeat_runs_row", {})
    comments = record.get("issue_comments_rows", [])
    approval = record.get("approvals_row", {})
    if _has_text(issue.get("title")) and _has_text(issue.get("description")):
        checks.append("issue -> line-guided work packet seam is readable")
    if _has_text(run.get("stdoutExcerpt")) or isinstance(run.get("contextSnapshot"), dict):
        checks.append("heartbeat_run -> execution trace seam is readable")
    if isinstance(run.get("resultJson"), dict) and comments:
        checks.append("result/comment -> result/residue reinjection seam is readable")
    if _has_text(approval.get("decisionNote")) and approval.get("payload"):
        checks.append("approvals_row -> governance gate seam is readable")
    return checks


def _honesty_class(slot: Dict[str, Any], record: Dict[str, Any], *, use_slot_boundary: bool = True) -> str:
    slot_items = (
        slot.get("current_state", ""),
        slot.get("validation_anchor_status", ""),
        slot.get("validation_anchor_note", ""),
    ) if use_slot_boundary else ()
    text = " ".join(
        str(item)
        for item in (*slot_items,
            record.get("source_kind", ""),
            record.get("honesty_note", ""),
        )
    ).lower()
    if "local fixture" in text or "fixture" in text or "waiting_for_actual_export" in text:
        return "local_fixture"
    if "actual" in text and "export" in text:
        return "actual_external_like"
    return "external_candidate"


def _resolve_record_path(record_ref: str) -> Path:
    record_path = Path(record_ref)
    if not record_path.is_absolute():
        record_path = REPO_ROOT / record_path
    return record_path


def _relative_ref(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _delta_vs_current_anchor(current: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    current_passed = set(current["passed_checks"])
    override_passed = set(override["passed_checks"])
    current_failed = set(current["failed_checks"])
    override_failed = set(override["failed_checks"])
    same_shape_checks = sorted(
        check for check in current_passed & override_passed if "surface" in check or "row has" in check
    )
    return {
        "same_shape_checks": same_shape_checks,
        "new_failed_checks": sorted(override_failed - current_failed),
        "lost_passed_checks": sorted(current_passed - override_passed),
        "honesty_boundary_change": f"{current['honesty_class']} -> {override['honesty_class']}",
        "gate_effect_change": f"{current['gate_effect']} -> {override['gate_effect']}",
        "still_missing_reopen_evidence": any("reopen_evidence" in item for item in override["uncertain_checks"]),
        "no_gate_close_change": override["gate_effect"] != "candidate_for_gate_close",
    }


def build_validation(*, override_record: str | None = None, schema_version: str | None = None) -> Dict[str, Any]:
    slot = _load_json(SLOT_PATH)
    record_ref = override_record or _record_ref(slot)
    if not record_ref:
        raise ValueError("actual export slot does not identify a current record ref")
    record_path = _resolve_record_path(record_ref)
    record = _load_json(record_path)

    required_surfaces = slot["expected_shape"]["required_surfaces"]
    present_surfaces = [surface for surface in required_surfaces if surface in record]
    missing_surfaces = [surface for surface in required_surfaces if surface not in record]
    shape_checks = _check_shape(record)
    mapping_checks = _check_mapping(record)
    honesty = _honesty_class(slot, record, use_slot_boundary=override_record is None)

    passed_checks = [
        f"required_surface_present:{surface}" for surface in present_surfaces
    ] + shape_checks + mapping_checks
    failed_checks = [f"required_surface_missing:{surface}" for surface in missing_surfaces]
    uncertain_checks: List[str] = []

    if honesty == "local_fixture":
        uncertain_checks.append("honesty_boundary: record preserves export shape but remains local fixture data")
    if not missing_surfaces and len(shape_checks) >= 4 and len(mapping_checks) >= 4 and honesty == "actual_external_like":
        validation_status = "pass"
        gate_effect = "candidate_for_gate_close"
        recommendation = "Treat this record as a candidate for gate close after supervisor-readable reopen validation."
    elif not missing_surfaces and len(shape_checks) >= 4 and len(mapping_checks) >= 4 and honesty == "external_candidate":
        validation_status = "partial"
        gate_effect = "candidate_for_reopen_validation"
        recommendation = "Use this record to test the mapping and reopen path, but keep hold until it is verified as a true host export for this gate."
    elif not missing_surfaces and len(shape_checks) >= 4 and len(mapping_checks) >= 4:
        validation_status = "partial"
        gate_effect = "narrowed_but_still_binding"
        recommendation = "Use this record as the current shape-complete validation anchor, but keep hold until it is replaced by a truly actual external export and reopen/gate evidence is exercised."
    else:
        validation_status = "fail"
        gate_effect = "no_change"
        recommendation = "Do not use this record to narrow actual_export_only until missing surfaces, shape gaps, or mapping seams are repaired."

    if "reopen" not in json.dumps(record, ensure_ascii=False).lower():
        uncertain_checks.append("reopen_evidence: no direct real reopen decision path in the record")

    return {
        "schema_version": schema_version or "vectorfl_paper_actual_export_gate_validation_latest_v0",
        "source_slot_artifact": str(SLOT_PATH.relative_to(REPO_ROOT)),
        "source_record_artifact": _relative_ref(record_path),
        "validation_status": validation_status,
        "passed_checks": passed_checks,
        "failed_checks": failed_checks,
        "uncertain_checks": uncertain_checks,
        "honesty_class": honesty,
        "gate_effect": gate_effect,
        "recommendation": recommendation,
        "validated_at": _now_iso(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the VectorFL Paper actual_export_only gate anchor.")
    parser.add_argument(
        "--override-record",
        help="Validate one candidate record as a dry-run without updating the current latest validation result.",
    )
    args = parser.parse_args()

    print(f"[actual-export-gate-validator] reading slot: {SLOT_PATH.relative_to(REPO_ROOT)}")
    if args.override_record:
        current = build_validation()
        result = build_validation(
            override_record=args.override_record,
            schema_version="vectorfl_paper_actual_export_gate_validation_dry_run_v0",
        )
        result["delta_vs_current_anchor"] = _delta_vs_current_anchor(current, result)
        DRY_RUN_RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
        DRY_RUN_RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"[actual-export-gate-validator] wrote dry-run result: {DRY_RUN_RESULT_PATH.relative_to(REPO_ROOT)}")
    else:
        result = build_validation()
        RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
        RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"[actual-export-gate-validator] wrote result: {RESULT_PATH.relative_to(REPO_ROOT)}")
    print(json.dumps({
        "validation_status": result["validation_status"],
        "honesty_class": result["honesty_class"],
        "gate_effect": result["gate_effect"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
