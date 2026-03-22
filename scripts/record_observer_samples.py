#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.fragment.store import FragmentStore
from app.measurement import MeasurementStore, build_connection_observation, build_revision_judgment


def _find(store: FragmentStore, fragment_id: str):
    fragment = store.get(fragment_id)
    if fragment is None:
        raise SystemExit(f"missing fragment: {fragment_id}")
    return fragment


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    runtime_root = runtime_root.resolve()
    fragment_store = FragmentStore(runtime_root)
    measurement_store = MeasurementStore(runtime_root)

    basic_001 = _find(fragment_store, "frag_basic_001")
    basic_005 = _find(fragment_store, "frag_basic_005")
    ytex_003 = _find(fragment_store, "frag_ytex_003")

    revision = build_revision_judgment(
        fragment_id=basic_001.fragment_id,
        source_id=basic_001.source_id,
        column_key="primary_anchor",
        previous_value={"key": "source.claude_md", "anchor_type": "source"},
        new_value={"key": "object.field.ai", "anchor_type": "object"},
        reason="document-like source currently overweights source.* anchors over object/semantic anchors",
        reason_family="source_anchor_overweight",
        operator="reviewer",
        batch_id=str(basic_001.metadata.get("ingest_batch_id", "")),
        session_id=str(basic_001.metadata.get("ingest_session_id", "")),
        notes="recorded as an observer-layer revision target, not auto-applied",
        confidence=0.83,
    )
    measurement_store.put(revision)

    deferred = build_connection_observation(
        fragment_id=basic_001.fragment_id,
        counterpart_fragment_id=basic_005.fragment_id,
        source_id=basic_001.source_id,
        counterpart_source_id=basic_005.source_id,
        relation_status="deferred_connection",
        reason="shared system/object vocabulary exists, but source-anchor overlap is still stronger than semantic overlap",
        reason_family="insufficient_semantic_alignment",
        shared_signals=["object.field.ai", "object.system.claude"],
        missing_signals=["strong structural match", "stable semantic overlap"],
        operator="reviewer",
        batch_id=str(basic_001.metadata.get("ingest_batch_id", "")),
        session_id=str(basic_001.metadata.get("ingest_session_id", "")),
        notes="keep as observation until anchor quality improves",
        confidence=0.48,
    )
    measurement_store.put(deferred)

    rejected = build_connection_observation(
        fragment_id=basic_001.fragment_id,
        counterpart_fragment_id=ytex_003.fragment_id,
        source_id=basic_001.source_id,
        counterpart_source_id=ytex_003.source_id,
        relation_status="rejected_connection",
        reason="surface technical vocabulary is not enough; workflow note and historical interview excerpt do not yet share stable semantic or structural anchors",
        reason_family="false_resonance",
        shared_signals=["technical vocabulary"],
        missing_signals=["shared semantic handle", "shared structural role"],
        operator="reviewer",
        batch_id=str(basic_001.metadata.get("ingest_batch_id", "")),
        session_id=str(basic_001.metadata.get("ingest_session_id", "")),
        notes="recorded to avoid over-connecting weak technical similarities",
        confidence=0.61,
    )
    measurement_store.put(rejected)

    print("recorded observer samples")
    print(revision.measurement_id)
    print(deferred.measurement_id)
    print(rejected.measurement_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
