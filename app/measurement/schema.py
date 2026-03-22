from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Optional


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class MeasurementRecord:
    measurement_id: str
    fragment_id: str
    measurement_type: str
    column_key: str
    value: Dict[str, Any]
    basis: str = ""
    evidence_text: str = ""
    confidence: float = 0.0
    origin: str = "system"
    status: str = "active"
    provisional: bool = True
    related_source_path: str = ""
    related_material_id: str = ""
    recorded_at: str = field(default_factory=utc_now_iso)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_record(self) -> Dict[str, Any]:
        return asdict(self)
