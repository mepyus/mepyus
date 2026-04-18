from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.core.events.event_append_guard import append_jsonl_locked, load_jsonl_with_tail_recovery
from app.core.models.entities import EngineStateRecord
from app.core.runtime.file_store import JsonDirectoryStore
from app.core.state_store.engine_state_update_policy import prepare_state_update
from app.core.states import UpdateTriggerType


CANONICAL_TOP_LEVEL_FIELDS = {
    "asset_id",
    "asset_name",
    "source_type",
    "schema_version",
    "update_trigger_type",
    "update_reason",
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
    "experimental_namespace",
    "updated_at",
}

FORBIDDEN_CANONICAL_FIELDS = {
    "context_unit_name",
    "paragraph_role_name",
    "pivot_label",
    "compression_label",
    "business_power_shift",
    "orchestration",
}

SCHEMA_VERSION = "engine_state_schema_v1"


class EngineStateStore:
    def __init__(self, runtime_root: Path) -> None:
        self.runtime_root = runtime_root
        self.history_root = runtime_root / "state" / "engine_state_history"
        self.latest_root = runtime_root / "views" / "engine_state_latest"
        self.latest_store = JsonDirectoryStore(self.latest_root)
        self.history_root.mkdir(parents=True, exist_ok=True)
        self.latest_root.mkdir(parents=True, exist_ok=True)

    def history_path(self, asset_id: str) -> Path:
        return self.history_root / f"{asset_id}.jsonl"

    def load_latest(self, asset_id: str) -> Optional[Dict[str, Any]]:
        return self.latest_store.get(asset_id)

    def load_history(self, asset_id: str) -> List[Dict[str, Any]]:
        rows, _recovered = load_jsonl_with_tail_recovery(self.history_path(asset_id))
        return rows

    def list_latest_states(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for record in self.latest_store.read_all():
            if not record.get("asset_id"):
                continue
            rows.append(record)
        return rows

    def append_state(
        self,
        record: EngineStateRecord,
        *,
        trigger_type: UpdateTriggerType = UpdateTriggerType.RUNTIME_EVIDENCE,
        update_reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        previous_latest = self.load_latest(record.asset_id)
        payload = prepare_state_update(
            asdict(record),
            previous_latest=previous_latest,
            trigger_type=trigger_type,
            update_reason=update_reason,
            schema_version=SCHEMA_VERSION,
        )
        payload = self._sanitize_record(payload)
        append_jsonl_locked(self.history_path(payload["asset_id"]), payload)
        self.write_latest_view(self._latest_projection(payload))
        return payload

    def write_latest_view(self, record: Dict[str, Any]) -> None:
        asset_id = str(record["asset_id"])
        self.latest_store.put(asset_id, record)
        self.latest_store.put("index", {"schema_version": SCHEMA_VERSION, "items": self._build_index_rows()})

    def _build_index_rows(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for record in self.latest_store.read_all():
            asset_id = record.get("asset_id")
            if not asset_id or asset_id == "index":
                continue
            rows.append(
                {
                    "asset_id": asset_id,
                    "asset_name": record["asset_name"],
                    "packet_texture": record["packet_texture"],
                    "grounding_status": record["grounding_status"],
                    "emergence_status": record["emergence_status"],
                    "carryover_risk": record["carryover_risk"],
                    "maturation_state": record["maturation_state"],
                    "traceability_status": record["traceability_status"],
                    "updated_at": record["updated_at"],
                }
            )
        rows.sort(key=lambda row: (row["updated_at"], row["asset_id"]), reverse=True)
        return rows

    def _sanitize_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(record)
        payload["schema_version"] = SCHEMA_VERSION
        experimental = dict(payload.get("experimental_namespace") or {})
        for key in list(payload.keys()):
            if key in FORBIDDEN_CANONICAL_FIELDS:
                experimental[key] = payload.pop(key)
        unknown_keys = [key for key in payload.keys() if key not in CANONICAL_TOP_LEVEL_FIELDS]
        for key in unknown_keys:
            experimental[key] = payload.pop(key)
        payload["experimental_namespace"] = experimental
        return payload

    def _latest_projection(self, record: Dict[str, Any]) -> Dict[str, Any]:
        projection = dict(record)
        projection.pop("update_reason", None)
        projection.pop("update_trigger_type", None)
        return projection
