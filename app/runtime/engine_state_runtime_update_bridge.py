from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from app.core.runtime.file_store import JsonDirectoryStore
from app.core.state_store import EngineStateStore
from app.core.states import UpdateTriggerType
from app.runtime.engine_state_update_patch_builder import (
    build_runtime_state_patch_proposal,
    build_state_record_payload_from_patch,
    to_engine_state_record,
)
from app.runtime.state_change_attention_queue import write_state_change_attention_queue_surface


class EngineStateRuntimeUpdateBridge:
    def __init__(self, runtime_root: Path) -> None:
        self.runtime_root = runtime_root
        self.store = EngineStateStore(runtime_root)
        self.events_root = runtime_root / "views" / "engine_state_update_events"
        self.events_store = JsonDirectoryStore(self.events_root)

    def apply_runtime_evidence(
        self,
        *,
        asset_id: str,
        update_reason: str,
        evidence_type: str,
        evidence_summary: str,
        evidence_refs: List[Dict[str, Any]],
        proposed_changes: Dict[str, Any],
        experimental_namespace: Optional[Dict[str, Any]] = None,
        replace_array_fields: Optional[List[str]] = None,
        trigger_type: UpdateTriggerType = UpdateTriggerType.RUNTIME_EVIDENCE,
    ) -> Dict[str, Any]:
        latest_state = self.store.load_latest(asset_id)
        if latest_state is None:
            raise ValueError(f"no canonical latest state for asset_id={asset_id}")

        proposal = build_runtime_state_patch_proposal(
            asset_id=asset_id,
            update_reason=update_reason,
            evidence_type=evidence_type,
            evidence_summary=evidence_summary,
            evidence_refs=evidence_refs,
            proposed_changes=proposed_changes,
            experimental_namespace=experimental_namespace,
            trigger_type=trigger_type,
            replace_array_fields=replace_array_fields,
        )
        payload = build_state_record_payload_from_patch(latest_state, proposal)
        record = to_engine_state_record(payload)
        appended = self.store.append_state(
            record,
            trigger_type=trigger_type,
            update_reason=update_reason,
        )
        latest = self.store.load_latest(asset_id)
        event = self._build_event_record(
            previous_latest=latest_state,
            latest=latest or {},
            proposal=proposal,
            appended=appended,
        )
        self._write_update_event(event)
        write_state_change_attention_queue_surface(self.runtime_root)
        return {
            "proposal": proposal,
            "appended": appended,
            "latest": latest,
            "event": event,
        }

    def _build_event_record(
        self,
        *,
        previous_latest: Dict[str, Any],
        latest: Dict[str, Any],
        proposal: Dict[str, Any],
        appended: Dict[str, Any],
    ) -> Dict[str, Any]:
        changed_fields: List[str] = []
        for field in [
            "packet_texture",
            "grounding_status",
            "emergence_status",
            "carryover_risk",
            "maturation_state",
            "traceability_status",
            "comparison_memory_reason",
            "gate_blocker_summary",
        ]:
            if previous_latest.get(field) != latest.get(field):
                changed_fields.append(field)
        return {
            "asset_id": latest.get("asset_id"),
            "asset_name": latest.get("asset_name"),
            "update_trigger_type": proposal["update_trigger_type"],
            "update_reason": proposal["update_reason"],
            "evidence_type": proposal["evidence_type"],
            "evidence_summary": proposal["evidence_summary"],
            "changed_canonical_fields": changed_fields,
            "evidence_refs": proposal["evidence_refs"],
            "updated_at": appended["updated_at"],
            "latest_packet_texture": latest.get("packet_texture"),
            "latest_maturation_state": latest.get("maturation_state"),
            "latest_traceability_status": latest.get("traceability_status"),
        }

    def _write_update_event(self, event: Dict[str, Any]) -> None:
        asset_id = str(event["asset_id"])
        self.events_store.put(asset_id, event)
        self.events_store.put("index", {"items": self._build_event_index()})

    def _build_event_index(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for record in self.events_store.read_all():
            asset_id = record.get("asset_id")
            if not asset_id or asset_id == "index":
                continue
            rows.append(
                {
                    "asset_id": asset_id,
                    "asset_name": record.get("asset_name"),
                    "update_trigger_type": record.get("update_trigger_type"),
                    "update_reason": record.get("update_reason"),
                    "changed_canonical_fields": record.get("changed_canonical_fields", []),
                    "updated_at": record.get("updated_at"),
                }
            )
        rows.sort(key=lambda row: (row.get("updated_at", ""), row.get("asset_id", "")), reverse=True)
        return rows
