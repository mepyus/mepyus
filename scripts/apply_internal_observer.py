#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.fragment.schema import FragmentAnchor, FragmentRecord, ProvenanceEntry
from app.fragment.store import FragmentStore
from app.work.processor_compare.observer_engine import run_internal_observers


def _usage() -> int:
    print("usage: apply_internal_observer.py <runtime_root> [fragment_id ...]")
    return 1


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        return _usage()
    runtime_root = Path(argv[1]).resolve()
    store = FragmentStore(runtime_root)
    target_ids = set(argv[2:])
    fragments = store.read_all()
    if target_ids:
        fragments = [fragment for fragment in fragments if fragment.fragment_id in target_ids]

    updated_ids: List[str] = []
    for fragment in fragments:
        updated = _apply(fragment)
        store.put(updated)
        updated_ids.append(updated.fragment_id)

    print(json.dumps({"runtime_root": str(runtime_root), "updated_count": len(updated_ids), "fragment_ids": updated_ids}, ensure_ascii=False, indent=2))
    return 0


def _apply(fragment: FragmentRecord) -> FragmentRecord:
    observer_payload = run_internal_observers(fragment.raw_text)
    merged = observer_payload["merged"]
    observer_anchors = [
        FragmentAnchor(
            key=f"observer.{anchor['anchor_type']}.{anchor['label']}",
            canonical_key=f"observer.{anchor['anchor_type']}.{anchor['label']}",
            label=anchor["label"],
            value=anchor["label"],
            anchor_type=anchor["anchor_type"],
            evidence_text=anchor.get("evidence_text", ""),
            confidence=float(anchor.get("score", 0.0)),
            origin="internal_observer",
            aliases=[],
            status="active",
        )
        for anchor in merged.get("anchors", [])
    ]
    anchors = _merge_anchors(fragment.anchors, observer_anchors)
    metadata = dict(fragment.metadata)
    metadata["internal_observer"] = {
        "version": "v0_1",
        "profiles": {
            "codex_like": observer_payload["codex_like"],
            "chatgpt_like": observer_payload["chatgpt_like"],
            "gemini_like": observer_payload["gemini_like"],
        },
        "merged": merged,
    }
    metadata["observer_role"] = merged["role"]
    metadata["observer_ambiguity"] = float(merged["ambiguity"])
    metadata["observer_confidence_numeric"] = float(merged["confidence"])
    metadata["observer_signals"] = list(merged.get("signals", []))
    provenance = list(fragment.provenance_log)
    provenance.append(
        ProvenanceEntry(
            step="internal_observer",
            note="retrofit internal observer ensemble",
            payload={
                "scene": merged["scene"],
                "role": merged["role"],
                "confidence": merged["confidence"],
                "ambiguity": merged["ambiguity"],
                "signals": merged.get("signals", []),
            },
        )
    )
    return fragment.with_updates(
        anchor=anchors[0] if anchors else fragment.anchor,
        anchors=anchors,
        D=float(merged["direction"]),
        I=float(merged["intensity"]),
        S=float(merged["stability"]),
        scene=str(merged["scene"]),
        confidence=_confidence_bucket(float(merged["confidence"])),
        metadata=metadata,
        provenance_log=provenance,
    )


def _merge_anchors(existing: List[FragmentAnchor], observer: List[FragmentAnchor]) -> List[FragmentAnchor]:
    merged: List[FragmentAnchor] = []
    seen = set()
    for anchor in list(existing) + list(observer):
        key = (anchor.key, anchor.anchor_type)
        if key in seen:
            continue
        seen.add(key)
        merged.append(anchor)
    return merged[:8]


def _confidence_bucket(value: float) -> str:
    if value >= 0.8:
        return "high"
    if value >= 0.55:
        return "mid"
    return "low"


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
