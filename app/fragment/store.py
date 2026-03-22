from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from app.core.runtime.file_store import JsonDirectoryStore
from app.fragment.schema import FragmentAnchor, FragmentRecord, PageRef, ProvenanceEntry, SourceRange


class FragmentStore:
    def __init__(self, runtime_root: Path) -> None:
        self.runtime_root = runtime_root
        self.store = JsonDirectoryStore(runtime_root / "fragments")

    def put(self, fragment: FragmentRecord) -> Path:
        return self.store.put(fragment.fragment_id, fragment.to_record())

    def get(self, fragment_id: str) -> Optional[FragmentRecord]:
        record = self.store.get(fragment_id)
        if record is None:
            return None
        return _fragment_from_record(record)

    def read_all(self) -> List[FragmentRecord]:
        return [_fragment_from_record(record) for record in self.store.read_all()]


def _fragment_from_record(record: dict) -> FragmentRecord:
    return FragmentRecord(
        fragment_id=record["fragment_id"],
        source_id=record["source_id"],
        source_type=record["source_type"],
        source_path=record["source_path"],
        raw_text=record["raw_text"],
        unit_scale=record["unit_scale"],
        created_at=record["created_at"],
        source_range=SourceRange(**record.get("source_range", {})),
        page_ref=PageRef(**record.get("page_ref", {})),
        paragraph_index=record.get("paragraph_index"),
        anchor=_anchor_from_record(record["anchor"]) if record.get("anchor") else None,
        anchors=[_anchor_from_record(entry) for entry in record.get("anchors", [])],
        D=float(record.get("D", 0.5)),
        I=float(record.get("I", 0.5)),
        S=float(record.get("S", 0.5)),
        scene=record.get("scene", "unknown"),
        flow=record.get("flow", "unknown"),
        time=record.get("time", ""),
        confidence=record.get("confidence", "mid"),
        provenance_log=[
            ProvenanceEntry(**entry) for entry in record.get("provenance_log", [])
        ],
        metadata=record.get("metadata", {}),
    )


def _anchor_from_record(record: dict) -> FragmentAnchor:
    payload = dict(record)
    if "key" not in payload:
        payload["key"] = payload.get("value", "")
    if "canonical_key" not in payload:
        payload["canonical_key"] = payload.get("key")
    if "evidence_text" not in payload:
        payload["evidence_text"] = payload.get("value", "")
    if "confidence" not in payload:
        payload["confidence"] = 0.0
    if "origin" not in payload:
        payload["origin"] = "ai"
    if "aliases" not in payload:
        payload["aliases"] = []
    if "status" not in payload:
        payload["status"] = "active"
    return FragmentAnchor(**payload)
