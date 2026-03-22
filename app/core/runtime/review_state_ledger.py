from __future__ import annotations

from pathlib import Path
from typing import Dict
import json


DEFAULT_LEDGER_PATH = (
    Path(__file__).resolve().parents[3]
    / "runtime"
    / "review_ledgers"
    / "review_state_ledger.json"
)


def load_review_state_ledger(path: Path | None = None) -> Dict[str, object]:
    ledger_path = path or DEFAULT_LEDGER_PATH
    if not ledger_path.exists():
        return {
            "ledger_kind": "review_state_ledger",
            "version": "v0",
            "entries": {},
        }
    with ledger_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        return {
            "ledger_kind": "review_state_ledger",
            "version": "v0",
            "entries": {},
        }
    payload.setdefault("ledger_kind", "review_state_ledger")
    payload.setdefault("version", "v0")
    payload.setdefault("entries", {})
    return payload


def write_review_state_ledger(payload: Dict[str, object], path: Path | None = None) -> Path:
    ledger_path = path or DEFAULT_LEDGER_PATH
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    with ledger_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=True, indent=2, sort_keys=True)
    return ledger_path


def get_review_state_entry(
    fixture_id: str,
    *,
    path: Path | None = None,
) -> Dict[str, object]:
    payload = load_review_state_ledger(path)
    entries = dict(payload.get("entries", {}) or {})
    return dict(entries.get(fixture_id, {}) or {})


def update_review_state_entry(
    fixture_id: str,
    *,
    last_reviewed_at: str,
    last_state_signature: str,
    last_bridge_mode: str,
    last_review_state: str,
    last_trace_temperature: str,
    last_lifecycle_stage: str,
    path: Path | None = None,
) -> Dict[str, object]:
    payload = load_review_state_ledger(path)
    entries = dict(payload.get("entries", {}) or {})
    previous = dict(entries.get(fixture_id, {}) or {})
    review_count = int(previous.get("review_count", 0) or 0) + 1
    entries[fixture_id] = {
        "fixture_id": fixture_id,
        "last_reviewed_at": last_reviewed_at,
        "last_state_signature": last_state_signature,
        "last_bridge_mode": last_bridge_mode,
        "last_review_state": last_review_state,
        "last_trace_temperature": last_trace_temperature,
        "last_lifecycle_stage": last_lifecycle_stage,
        "review_count": review_count,
    }
    payload["entries"] = entries
    write_review_state_ledger(payload, path)
    return dict(entries[fixture_id])


def summarize_review_state_entry(entry: Dict[str, object]) -> Dict[str, object]:
    lifecycle_stage = str(entry.get("last_lifecycle_stage", "")).strip()
    trace_temperature = str(entry.get("last_trace_temperature", "")).strip()
    review_count = int(entry.get("review_count", 0) or 0)
    revisit_recommended = lifecycle_stage in {"blocked_waiting_revisit", "deferred_review_asset"}
    warm_downgrade_candidate = trace_temperature == "warm" and review_count >= 1
    return {
        "lifecycle_stage": lifecycle_stage,
        "trace_temperature": trace_temperature,
        "review_count": review_count,
        "revisit_recommended": revisit_recommended,
        "warm_downgrade_candidate": warm_downgrade_candidate,
    }
