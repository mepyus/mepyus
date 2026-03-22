from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.live_input_space import evaluate_mixed_path_pair
from app.core.runtime.review_fixture_manifest import load_review_fixture_entries
from app.core.runtime.review_state_ledger import (
    DEFAULT_LEDGER_PATH,
    get_review_state_entry,
    summarize_review_state_entry,
    update_review_state_entry,
)


def main() -> None:
    repo_root = REPO_ROOT
    runtime_root = repo_root / "runtime"
    reports_root = repo_root / "app" / "work" / "processor_compare" / "reports"
    previous_report_json = reports_root / "review_fixture_check_round1.json"
    report_md = reports_root / "review_fixture_check_round3.md"
    report_json = reports_root / "review_fixture_check_round3.json"
    ledger_path = DEFAULT_LEDGER_PATH

    service = FormationService(runtime_root)
    entries = load_review_fixture_entries()
    previous_payload = {}
    if previous_report_json.exists():
        with previous_report_json.open("r", encoding="utf-8") as handle:
            previous_payload = json.load(handle)
    previous_signature_map = {
        str(row.get("fixture_id", "")).strip(): str(row.get("state_signature", "")).strip()
        for row in list(previous_payload.get("rows", []) or [])
        if str(row.get("fixture_id", "")).strip()
    }
    rows = []
    immutable_pass = 0
    mutable_match = 0
    lifecycle_match_count = 0
    unchanged_signature_count = 0
    changed_signature_count = 0
    unchanged_ledger_signature_count = 0
    changed_ledger_signature_count = 0
    for entry in entries:
        previous_ledger_entry = get_review_state_entry(entry.fixture_id, path=ledger_path)
        result = evaluate_mixed_path_pair(
            service,
            left_local_space_id=entry.left_local_space_id,
            right_local_space_id=entry.right_local_space_id,
        )
        review = dict(result.get("promotion_review", {}) or {})
        actual_bridge_mode = str(result.get("bridge_mode", "")).strip()
        actual_review_state = str(review.get("review_state", "")).strip()
        matches_expected = (
            actual_bridge_mode == entry.expected_bridge_mode
            and actual_review_state == entry.expected_review_state
        )
        actual_trace_temperature = str(result.get("trace_temperature", "")).strip()
        actual_lifecycle_stage = str(result.get("lifecycle_stage", "")).strip()
        lifecycle_matches_expected = (
            actual_trace_temperature == entry.expected_lifecycle_temperature
            and actual_lifecycle_stage == entry.expected_lifecycle_stage
        )
        if lifecycle_matches_expected:
            lifecycle_match_count += 1
        if not entry.mutable and matches_expected:
            immutable_pass += 1
        if entry.mutable and matches_expected:
            mutable_match += 1
        state_signature = str(result.get("state_signature", "")).strip()
        previous_signature = previous_signature_map.get(entry.fixture_id, "")
        state_signature_unchanged = bool(previous_signature) and previous_signature == state_signature
        state_signature_changed = bool(previous_signature) and previous_signature != state_signature
        if state_signature_unchanged:
            unchanged_signature_count += 1
        if state_signature_changed:
            changed_signature_count += 1
        previous_ledger_signature = str(previous_ledger_entry.get("last_state_signature", "")).strip()
        ledger_signature_unchanged = bool(previous_ledger_signature) and previous_ledger_signature == state_signature
        ledger_signature_changed = bool(previous_ledger_signature) and previous_ledger_signature != state_signature
        if ledger_signature_unchanged:
            unchanged_ledger_signature_count += 1
        if ledger_signature_changed:
            changed_ledger_signature_count += 1
        updated_ledger_entry = update_review_state_entry(
            entry.fixture_id,
            last_reviewed_at=str(result.get("evaluated_at", "")).strip(),
            last_state_signature=state_signature,
            last_bridge_mode=actual_bridge_mode,
            last_review_state=actual_review_state,
            last_trace_temperature=actual_trace_temperature,
            last_lifecycle_stage=actual_lifecycle_stage,
            path=ledger_path,
        )
        ledger_summary = summarize_review_state_entry(updated_ledger_entry)
        rows.append(
            {
                "fixture_id": entry.fixture_id,
                "fixture_kind": entry.fixture_kind,
                "mutable": entry.mutable,
                "allowed_drift": entry.allowed_drift,
                "expected_bridge_mode": entry.expected_bridge_mode,
                "expected_review_state": entry.expected_review_state,
                "expected_lifecycle_temperature": entry.expected_lifecycle_temperature,
                "expected_lifecycle_stage": entry.expected_lifecycle_stage,
                "actual_bridge_mode": actual_bridge_mode,
                "actual_review_state": actual_review_state,
                "evaluated_at": str(result.get("evaluated_at", "")).strip(),
                "state_signature": state_signature,
                "previous_state_signature": previous_signature,
                "state_signature_unchanged": state_signature_unchanged,
                "state_signature_changed": state_signature_changed,
                "previous_ledger_last_reviewed_at": str(previous_ledger_entry.get("last_reviewed_at", "")).strip(),
                "previous_ledger_state_signature": previous_ledger_signature,
                "ledger_state_signature_unchanged": ledger_signature_unchanged,
                "ledger_state_signature_changed": ledger_signature_changed,
                "persisted_last_reviewed_at": str(updated_ledger_entry.get("last_reviewed_at", "")).strip(),
                "persisted_review_count": int(updated_ledger_entry.get("review_count", 0) or 0),
                "trace_temperature": actual_trace_temperature,
                "lifecycle_stage": actual_lifecycle_stage,
                "lifecycle_matches_expected": lifecycle_matches_expected,
                "ledger_revisit_recommended": bool(ledger_summary.get("revisit_recommended")),
                "ledger_warm_downgrade_candidate": bool(ledger_summary.get("warm_downgrade_candidate")),
                "matches_expected": matches_expected,
                "description": entry.description,
            }
        )

    payload = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "manifest_fixture_count": len(entries),
        "immutable_regression_fixture_count": len([entry for entry in entries if not entry.mutable]),
        "mutable_exploration_control_count": len([entry for entry in entries if entry.mutable]),
        "immutable_pass_count": immutable_pass,
        "mutable_match_count": mutable_match,
        "lifecycle_match_count": lifecycle_match_count,
        "previous_signature_fixture_count": len(previous_signature_map),
        "unchanged_signature_count": unchanged_signature_count,
        "changed_signature_count": changed_signature_count,
        "ledger_path": str(ledger_path),
        "unchanged_ledger_signature_count": unchanged_ledger_signature_count,
        "changed_ledger_signature_count": changed_ledger_signature_count,
        "rows": rows,
    }
    report_json.parent.mkdir(parents=True, exist_ok=True)
    with report_json.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=True, indent=2, sort_keys=True)

    lines = [
        "# review fixture check round3",
        "",
        "## 1. summary",
        f"- manifest_fixture_count: `{payload['manifest_fixture_count']}`",
        f"- immutable_regression_fixture_count: `{payload['immutable_regression_fixture_count']}`",
        f"- mutable_exploration_control_count: `{payload['mutable_exploration_control_count']}`",
        f"- immutable_pass_count: `{payload['immutable_pass_count']}`",
        f"- mutable_match_count: `{payload['mutable_match_count']}`",
        f"- lifecycle_match_count: `{payload['lifecycle_match_count']}`",
        f"- previous_signature_fixture_count: `{payload['previous_signature_fixture_count']}`",
        f"- unchanged_signature_count: `{payload['unchanged_signature_count']}`",
        f"- changed_signature_count: `{payload['changed_signature_count']}`",
        f"- ledger_path: `{payload['ledger_path']}`",
        f"- unchanged_ledger_signature_count: `{payload['unchanged_ledger_signature_count']}`",
        f"- changed_ledger_signature_count: `{payload['changed_ledger_signature_count']}`",
        "",
        "## 2. results",
    ]
    for row in rows:
        lines.extend(
            [
                f"- `{row['fixture_id']}`",
                f"  - kind: `{row['fixture_kind']}`",
                f"  - expected: `{row['expected_bridge_mode']} / {row['expected_review_state']}`",
                f"  - actual: `{row['actual_bridge_mode']} / {row['actual_review_state']}`",
                f"  - expected_lifecycle: `{row['expected_lifecycle_temperature']} / {row['expected_lifecycle_stage']}`",
                f"  - lifecycle: `{row['trace_temperature']} / {row['lifecycle_stage']}`",
                f"  - lifecycle_matches_expected: `{str(row['lifecycle_matches_expected']).lower()}`",
                f"  - evaluated_at: `{row['evaluated_at']}`",
                f"  - state_signature: `{row['state_signature']}`",
                f"  - previous_state_signature: `{row['previous_state_signature']}`",
                f"  - state_signature_unchanged: `{str(row['state_signature_unchanged']).lower()}`",
                f"  - previous_ledger_last_reviewed_at: `{row['previous_ledger_last_reviewed_at']}`",
                f"  - previous_ledger_state_signature: `{row['previous_ledger_state_signature']}`",
                f"  - ledger_state_signature_unchanged: `{str(row['ledger_state_signature_unchanged']).lower()}`",
                f"  - persisted_last_reviewed_at: `{row['persisted_last_reviewed_at']}`",
                f"  - persisted_review_count: `{row['persisted_review_count']}`",
                f"  - ledger_revisit_recommended: `{str(row['ledger_revisit_recommended']).lower()}`",
                f"  - ledger_warm_downgrade_candidate: `{str(row['ledger_warm_downgrade_candidate']).lower()}`",
                f"  - matches_expected: `{str(row['matches_expected']).lower()}`",
            ]
        )
    with report_md.open("w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
