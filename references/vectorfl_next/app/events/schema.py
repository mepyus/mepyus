from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Tuple


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class EventRecord:
    event_id: str
    event_type: str
    subject_kind: str
    subject_id: str
    occurred_at: str = field(default_factory=utc_now_iso)
    payload: Dict[str, Any] = field(default_factory=dict)
    lineage_refs: Tuple[str, ...] = ()


def to_record(event: EventRecord) -> Dict[str, Any]:
    return asdict(event)
