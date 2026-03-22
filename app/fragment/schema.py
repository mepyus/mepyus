from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class SourceRange:
    start: Optional[int] = None
    end: Optional[int] = None


@dataclass(frozen=True)
class PageRef:
    page_index: Optional[int] = None
    page_label: Optional[str] = None


@dataclass(frozen=True)
class FragmentAnchor:
    key: str
    label: str
    value: str
    anchor_type: str = "semantic"
    evidence_text: str = ""
    confidence: float = 0.0
    origin: str = "ai"
    canonical_key: Optional[str] = None
    aliases: List[str] = field(default_factory=list)
    status: str = "active"


@dataclass(frozen=True)
class ProvenanceEntry:
    step: str
    note: str
    recorded_at: str = field(default_factory=utc_now_iso)
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class FragmentRecord:
    fragment_id: str
    source_id: str
    source_type: str
    source_path: str
    raw_text: str
    unit_scale: str
    created_at: str = field(default_factory=utc_now_iso)
    source_range: SourceRange = field(default_factory=SourceRange)
    page_ref: PageRef = field(default_factory=PageRef)
    paragraph_index: Optional[int] = None
    anchor: Optional[FragmentAnchor] = None
    anchors: List[FragmentAnchor] = field(default_factory=list)
    D: float = 0.5
    I: float = 0.5
    S: float = 0.5
    scene: str = "unknown"
    flow: str = "unknown"
    time: str = ""
    confidence: str = "mid"
    provenance_log: List[ProvenanceEntry] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_record(self) -> Dict[str, Any]:
        return asdict(self)

    def with_updates(self, **changes: Any) -> "FragmentRecord":
        payload = self.to_record()
        payload.update(changes)
        return FragmentRecord(
            fragment_id=payload["fragment_id"],
            source_id=payload["source_id"],
            source_type=payload["source_type"],
            source_path=payload["source_path"],
            raw_text=payload["raw_text"],
            unit_scale=payload["unit_scale"],
            created_at=payload["created_at"],
            source_range=SourceRange(**payload.get("source_range", {}))
            if isinstance(payload.get("source_range"), dict)
            else payload["source_range"],
            page_ref=PageRef(**payload.get("page_ref", {}))
            if isinstance(payload.get("page_ref"), dict)
            else payload["page_ref"],
            paragraph_index=payload.get("paragraph_index"),
            anchor=FragmentAnchor(**payload["anchor"])
            if isinstance(payload.get("anchor"), dict)
            else payload.get("anchor"),
            anchors=[
                FragmentAnchor(**entry) if isinstance(entry, dict) else entry
                for entry in payload.get("anchors", [])
            ],
            D=float(payload.get("D", 0.5)),
            I=float(payload.get("I", 0.5)),
            S=float(payload.get("S", 0.5)),
            scene=payload.get("scene", "unknown"),
            flow=payload.get("flow", "unknown"),
            time=payload.get("time", ""),
            confidence=payload.get("confidence", "mid"),
            provenance_log=[
                ProvenanceEntry(**entry) if isinstance(entry, dict) else entry
                for entry in payload.get("provenance_log", [])
            ],
            metadata=payload.get("metadata", {}),
        )
