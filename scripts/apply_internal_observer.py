#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.fragment.schema import FragmentAnchor, FragmentRecord, ProvenanceEntry
from app.fragment.store import FragmentStore
from app.core.runtime.line_thickening import RereadObservation, record_reread_observation
from app.work.processor_compare.observer_engine import run_internal_observers


def _usage() -> int:
    print(
        "usage: apply_internal_observer.py <runtime_root> [fragment_id ...] "
        "[--record-line-thickening] [--bounded-recurrence-validation]"
    )
    return 1


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply the internal observer to stored fragments.")
    parser.add_argument("runtime_root")
    parser.add_argument("fragment_id", nargs="*")
    parser.add_argument(
        "--record-line-thickening",
        action="store_true",
        help="append a bounded grounded line_thickening observation for the fragment reread path",
    )
    parser.add_argument(
        "--bounded-recurrence-validation",
        action="store_true",
        help="preserve the supplied fragment order, including duplicates, for recurrence validation",
    )
    return parser.parse_args(argv[1:])


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        return _usage()
    args = _parse_args(argv)
    runtime_root = Path(args.runtime_root).resolve()
    store = FragmentStore(runtime_root)
    if args.bounded_recurrence_validation:
        if not args.fragment_id:
            return _usage()
        fragments = []
        for fragment_id in args.fragment_id:
            fragment = store.get(fragment_id)
            if fragment is None:
                raise SystemExit(f"fragment not found: {fragment_id}")
            fragments.append(fragment)
    else:
        target_ids = set(args.fragment_id)
        fragments = store.read_all()
        if target_ids:
            fragments = [fragment for fragment in fragments if fragment.fragment_id in target_ids]

    updated_ids: List[str] = []
    thickening_results: List[dict] = []
    for fragment in fragments:
        updated = _apply(fragment)
        store.put(updated)
        updated_ids.append(updated.fragment_id)
        if args.record_line_thickening:
            thickening_results.append(_record_line_thickening(runtime_root, updated))

    print(
        json.dumps(
            {
                "runtime_root": str(runtime_root),
                "updated_count": len(updated_ids),
                "fragment_ids": updated_ids,
                "bounded_recurrence_validation": bool(args.bounded_recurrence_validation),
                "line_thickening_results": thickening_results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
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


def _record_line_thickening(runtime_root: Path, fragment: FragmentRecord) -> dict:
    merged = dict(fragment.metadata.get("internal_observer", {})).get("merged", {})
    range_start = getattr(fragment.source_range, "start", None)
    range_end = getattr(fragment.source_range, "end", None)
    has_direct_span = range_start is not None and range_end is not None
    has_source_link = bool(fragment.source_path or fragment.page_ref.page_label)
    evidence_mode = "direct_span" if has_direct_span else "source_linked" if has_source_link else "summary_echo"
    source_pointer = f"runtime/fragments/{fragment.fragment_id}.json"
    if has_direct_span:
        source_pointer = f"{source_pointer}#source_range={range_start}-{range_end}"
        if fragment.paragraph_index is not None:
            source_pointer = f"{source_pointer};paragraph_index={fragment.paragraph_index}"
    elif fragment.paragraph_index is not None:
        source_pointer = f"{source_pointer}#paragraph_index={fragment.paragraph_index}"
    elif fragment.page_ref.page_label:
        source_pointer = f"{source_pointer}#page_ref={fragment.page_ref.page_label}"

    line_name = "input_to_reading_organ"
    if merged.get("role") == "contrast" and has_direct_span:
        line_name = "transition_over_surface"

    observation = RereadObservation(
        run_id=f"internal_observer:{fragment.fragment_id}",
        asset_or_surface=fragment.source_path or fragment.fragment_id,
        view_type=str(merged.get("role") or fragment.scene or "observer"),
        line_name=line_name,
        evidence=str(merged.get("why_short") or fragment.raw_text[:180]).strip(),
        grounding_type="direct" if evidence_mode == "direct_span" else "fallback" if evidence_mode == "source_linked" else "inferred",
        support_points=[
            f"observer_role={merged.get('role') or fragment.scene or 'unknown'}",
            f"fragment_source={fragment.fragment_id}",
            f"source_pointer={source_pointer}",
        ],
        weakness_points=[
            "single fragment reread only",
            "needs a later reread surface to confirm recurrence",
        ],
        contradiction_points=[],
        caution_points=[
            "summary-only reread would erase the fragment pointer",
            "single-run evidence is not recurrence",
        ],
        next_probe_surface=source_pointer,
        thickness_before="thin",
        thickness_after="thin",
        observed_at=fragment.created_at,
        source_kind="raw_surface",
        source_path_or_ref=fragment.source_path,
        source_run_id_or_event_id=str(fragment.metadata.get("ingest_batch_id") or fragment.fragment_id),
        source_pointer=source_pointer,
        evidence_mode=evidence_mode,
        validation_path_id="internal_observer",
        evidence_origin_kind="primary_raw" if evidence_mode == "direct_span" else "primary_structured",
        independence_class="primary",
    )
    return record_reread_observation(runtime_root, observation)


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
