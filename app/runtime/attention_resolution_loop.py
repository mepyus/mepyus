from __future__ import annotations

from typing import Any, Dict, List, Optional


ACTIVE_STATUSES = {"new", "seen", "deferred", "reopened"}
STRICT_REASONS = {
    "traceability_shift",
    "grounding_shift",
    "blocker_added",
    "packet_texture_shift",
    "manual_correction_requires_attention",
}


def _trigger_family(trigger_type: Optional[str]) -> str:
    if trigger_type in {"runtime_evidence", "backfill", "recompute", "manual_correction"}:
        return str(trigger_type)
    return "unknown"


def build_attention_signature(item: Dict[str, Any]) -> str:
    changed = ",".join(sorted(item.get("changed_fields", []) or []))
    return "|".join(
        [
            str(item.get("asset_id") or ""),
            str(item.get("priority_level") or ""),
            str(item.get("diff_class") or ""),
            changed,
            str(item.get("attention_reason") or ""),
            _trigger_family(item.get("update_trigger_type")),
        ]
    )


def _resolved_entry(previous_item: Dict[str, Any], *, reason: str, resolved_at: Optional[str]) -> Dict[str, Any]:
    row = dict(previous_item)
    row["queue_status"] = "resolved"
    row["resolution_reason"] = reason
    row["resolved_at"] = resolved_at
    return row


def apply_attention_resolution_loop(
    *,
    previous_asset_view: Optional[Dict[str, Any]],
    current_item: Optional[Dict[str, Any]],
    background_summary: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    previous_latest = (
        (previous_asset_view or {}).get("latest_item")
        or (previous_asset_view or {}).get("background_summary")
        or {}
    )
    previous_resolved_items = list((previous_asset_view or {}).get("resolved_items") or [])

    previous_signature = previous_latest.get("attention_signature")
    previous_status = previous_latest.get("queue_status")
    current_signature = build_attention_signature(current_item) if current_item else None

    resolved_items: List[Dict[str, Any]] = previous_resolved_items[-5:]

    if current_item:
        current_item = dict(current_item)
        current_item["attention_signature"] = current_signature
        if previous_status in {"resolved", "suppressed"} and previous_signature == current_signature:
            current_item["queue_status"] = "reopened"
            current_item["lifecycle_note"] = "reopened_same_signature"
        elif previous_status in {"resolved", "suppressed"} and previous_signature and previous_signature != current_signature:
            current_item["queue_status"] = "reopened"
            current_item["lifecycle_note"] = "reopened_new_signature"
        elif previous_status in {"resolved", "suppressed"}:
            current_item["queue_status"] = "reopened"
            current_item["lifecycle_note"] = "reopened_after_suppressed_or_resolved"
        else:
            current_item["queue_status"] = current_item.get("queue_status") or "new"
            current_item["lifecycle_note"] = "active_attention"

        if previous_status in ACTIVE_STATUSES and previous_signature and previous_signature != current_signature:
            resolved_items.append(
                _resolved_entry(
                    previous_latest,
                    reason="superseded_by_newer_attention_signature",
                    resolved_at=current_item.get("latest_updated_at"),
                )
            )

    if background_summary:
        background_summary = dict(background_summary)
        background_summary["queue_status"] = "suppressed"
        background_summary["lifecycle_note"] = "background_summary_absorbed"
        if current_item is None and previous_status in ACTIVE_STATUSES:
            resolved_items.append(
                _resolved_entry(
                    previous_latest,
                    reason="absorbed_into_background_summary",
                    resolved_at=background_summary.get("latest_updated_at"),
                )
            )

    if current_item and current_item.get("attention_reason") in STRICT_REASONS:
        current_item["auto_resolve_policy"] = "strict"
    elif current_item:
        current_item["auto_resolve_policy"] = "normal"

    return {
        "latest_item": current_item,
        "background_summary": background_summary,
        "resolved_items": resolved_items[-10:],
    }
