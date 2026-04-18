from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTRACTS_DIR = REPO_ROOT / "runtime" / "contracts"
MANIFESTS_DIR = REPO_ROOT / "runtime" / "manifests"


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _required_surface_keys(template: Dict[str, Any]) -> set[str]:
    return set((template.get("required_surfaces") or {}).keys())


def validate_actual_export_record(record: Dict[str, Any], template: Dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = sorted(_required_surface_keys(template) - set(record.keys()))
    if missing:
        errors.append(f"missing required surfaces: {', '.join(missing)}")
    for key in _required_surface_keys(template) & set(record.keys()):
        if record.get(key) in (None, "", [], {}):
            errors.append(f"surface {key} is empty")
    return errors


def materialize_v4_packet(actual_record: Dict[str, Any], packet_stub: Dict[str, Any]) -> Dict[str, Any]:
    packet = deepcopy(packet_stub)
    issue = actual_record["issues_row"]
    run = actual_record["heartbeat_runs_row"]
    comments = actual_record["issue_comments_rows"]
    approval = actual_record["approvals_row"]
    packet["status"] = "materialized_from_actual_export"
    packet["source_assignment"].update(
        {
            "assignment_id": issue["id"],
            "company_ref": issue["companyId"],
            "project_ref": issue["projectId"],
            "goal_ref": issue["goalId"],
            "parent_ref": issue.get("parentId"),
            "title": issue["title"],
            "description": issue.get("description") or "",
            "assignee_ref": issue.get("assigneeAgentId") or "",
            "source_status": issue.get("status") or "unknown",
        }
    )
    packet["line_translation"]["translation_confidence"] = "high"
    packet["context_refs"]["source_record_ref"] = str(
        MANIFESTS_DIR / "vectorfl_paper_actual_export_host_record_slot_v0.json"
    )
    packet["context_refs"]["actual_export_refs"] = [
        "issues_row",
        "heartbeat_runs_row",
        "issue_comments_rows[0]",
        "approvals_row",
    ]
    packet["actual_export_summary"] = {
        "issue_identifier": issue.get("identifier") or issue["id"],
        "run_id": run["id"],
        "comment_count": len(comments),
        "approval_status": approval.get("status") or "unknown",
        "result_summary": ((run.get("resultJson") or {}).get("summary")) or "",
    }
    return packet


def main() -> None:
    slot = _load_json(MANIFESTS_DIR / "vectorfl_paper_actual_export_host_record_slot_v0.json")
    template = _load_json(CONTRACTS_DIR / "vectorfl_paper_actual_export_host_record_template_v0.json")
    packet_stub = _load_json(CONTRACTS_DIR / "vectorfl_paper_weekend_live_translated_work_packet_v4_stub.json")
    placeholder = _load_json(REPO_ROOT / slot["current_placeholder_ref"])

    errors = validate_actual_export_record(placeholder, template)
    materialized = materialize_v4_packet(placeholder, packet_stub) if not errors else None

    out = {
      "slot_state": slot["current_state"],
      "placeholder_ref": slot["current_placeholder_ref"],
      "validation_passed": not errors,
      "errors": errors,
      "materialized_packet_preview": materialized,
    }
    out_path = MANIFESTS_DIR / "vectorfl_paper_actual_export_swap_dry_run_v0.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"dry_run_path": str(out_path), "validation_passed": not errors}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
