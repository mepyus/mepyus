from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from app.core.state_store import EngineStateStore
from app.core.state_store.engine_state_update_policy import FIELD_ALLOWED_VALUES, FORBIDDEN_CANONICAL_FIELDS


def load_expected_fixtures(expected_root: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for path in sorted(expected_root.glob("*.json")):
        rows.append(json.loads(path.read_text(encoding="utf-8")))
    return rows


def validate_fixture(expected: Dict[str, Any], runtime_root: Path) -> Dict[str, Any]:
    store = EngineStateStore(runtime_root)
    asset_id = expected["asset_id"]
    latest = store.load_latest(asset_id) or {}
    history = store.load_history(asset_id)
    latest_from_history = _latest_from_history(history)

    result: Dict[str, Any] = {
        "asset_id": asset_id,
        "expected_state_match": [],
        "acceptable_drift": [],
        "policy_violation": [],
        "latest_history_consistency": False,
        "schema_valid": False,
        "store_valid": bool(latest and history),
        "policy_consistency": False,
        "experimental_leakage": [],
        "notes": [],
    }

    result["schema_valid"] = _validate_schema_like(latest, result["policy_violation"])
    result["latest_history_consistency"] = latest == latest_from_history
    if not result["latest_history_consistency"]:
        result["policy_violation"].append("latest_history_mismatch")

    if history:
        last_history = history[-1]
        if last_history.get("schema_version") and last_history.get("update_trigger_type") and last_history.get("evidence_refs"):
            result["policy_consistency"] = True
        else:
            result["policy_violation"].append("missing_policy_provenance")

    _check_expected_fields(expected, latest, result)
    _check_leakage(latest, result)
    return result


def _validate_schema_like(record: Dict[str, Any], policy_violations: List[str]) -> bool:
    required = {
        "asset_id",
        "asset_name",
        "source_type",
        "schema_version",
        "packet_texture",
        "grounding_status",
        "emergence_status",
        "carryover_risk",
        "maturation_state",
        "traceability_status",
        "comparison_memory_reason",
        "gate_blocker_summary",
        "state_notes",
        "evidence_refs",
        "updated_at",
    }
    missing = sorted(field for field in required if field not in record)
    if missing:
        policy_violations.append(f"missing_required:{','.join(missing)}")
        return False
    for field, allowed in FIELD_ALLOWED_VALUES.items():
        value = record.get(field)
        if field in {"comparison_memory_reason", "gate_blocker_summary"}:
            if not isinstance(value, list):
                policy_violations.append(f"invalid_list_field:{field}")
                return False
            invalid = [entry for entry in value if entry not in allowed]
            if invalid:
                policy_violations.append(f"invalid_enum:{field}:{','.join(invalid)}")
                return False
            continue
        if value not in allowed:
            policy_violations.append(f"invalid_enum:{field}:{value}")
            return False
    return True


def _latest_from_history(history: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not history:
        return {}
    latest = dict(history[-1])
    latest.pop("update_trigger_type", None)
    latest.pop("update_reason", None)
    return latest


def _check_expected_fields(expected: Dict[str, Any], latest: Dict[str, Any], result: Dict[str, Any]) -> None:
    for field, expected_value in expected.get("expected", {}).items():
        actual = latest.get(field)
        if actual == expected_value:
            result["expected_state_match"].append(field)
        else:
            result["policy_violation"].append(f"expected_mismatch:{field}:{actual}")

    for field, expected_values in expected.get("expected_contains", {}).items():
        actual_values = set(latest.get(field, []))
        wanted = set(expected_values)
        if wanted.issubset(actual_values):
            result["expected_state_match"].append(f"{field}_contains")
        else:
            result["acceptable_drift"].append(f"{field}:missing_expected_subset")


def _check_leakage(latest: Dict[str, Any], result: Dict[str, Any]) -> None:
    for forbidden in FORBIDDEN_CANONICAL_FIELDS:
        if forbidden in latest:
            result["experimental_leakage"].append(forbidden)
    if result["experimental_leakage"]:
        result["policy_violation"].append("experimental_namespace_leakage")
