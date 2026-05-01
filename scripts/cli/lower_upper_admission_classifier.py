#!/usr/bin/env python3
"""Minimum lower-to-upper bridge admission classifier.

This is a conservative helper for Phase 1.14. It classifies how far a
lower artifact may travel into the upper CLI spine. It does not promote
readiness and does not modify artifacts.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


ADMISSIONS = ("reject_for_upper", "evidence_only", "ingest_ready", "packet_candidate")
READINESS_TO_ADMISSION = {
    "residue-only": "reject_for_upper",
    "evidence-ready": "evidence_only",
    "engine-ingest-ready": "ingest_ready",
    "packet-candidate": "packet_candidate",
}


def _workspace_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _infer_kind(path: str) -> str:
    name = Path(path).name.lower()
    full = path.lower()
    if "content_role_tags" in name or "line_seed_bundles" in name or "camera_support_bundles" in name:
        return "lower_support_layer"
    if "runtime/events/" in full or "runtime/receipts/" in full or name.endswith(".jsonl"):
        return "runtime_residue"
    if "source_manifest_" in name:
        return "source_manifest"
    if "split_units_" in name:
        return "split_units"
    if "processing_trace_" in name:
        return "processing_trace"
    if "operator_summary_" in name:
        return "operator_summary"
    if "preprocess_comparison" in name:
        return "preprocess_comparison"
    if "regroup_compare" in name or "regroup_" in name:
        return "preprocessed_material"
    if "gmd_native_read_" in name:
        return "gmd_native_read"
    if full.startswith("runtime/contracts/"):
        return "runtime_contract"
    if name.endswith(".json"):
        return "structured_json"
    if name.endswith((".md", ".txt")):
        return "readable_text"
    return "unknown"


def _kind_default(kind: str) -> str:
    if kind in {"runtime_residue"}:
        return "reject_for_upper"
    if kind in {"source_manifest", "split_units", "operator_summary", "processing_trace", "runtime_contract", "structured_json", "readable_text", "lower_support_layer"}:
        return "evidence_only"
    if kind in {"preprocessed_material"}:
        return "ingest_ready"
    if kind in {"preprocess_comparison", "gmd_native_read"}:
        return "packet_candidate"
    return "evidence_only"


def _rank(admission: str) -> int:
    return ADMISSIONS.index(admission)


def _min_admission(a: str, b: str) -> str:
    return a if _rank(a) <= _rank(b) else b


def classify(
    artifact_path: str,
    readiness_hint: str = "",
    artifact_kind: str = "",
    provenance_present: bool = False,
    trace_present: bool = False,
    routing_present: bool = False,
    packet_worthiness_present: bool = False,
) -> Dict[str, Any]:
    path = _workspace_path(Path(artifact_path))
    exists = Path(path).exists()
    kind = artifact_kind or _infer_kind(path)
    reasons: List[str] = []
    blocked: List[str] = []
    checklist = {
        "provenance_clarity": bool(exists or provenance_present),
        "trace_presence": bool(trace_present),
        "routing_clarity": bool(routing_present),
        "scope_boundedness": bool(path),
        "signal_usefulness": kind != "runtime_residue" and exists,
        "packet_worthiness": bool(packet_worthiness_present),
        "ambiguity_note": "",
    }

    admission = _kind_default(kind)
    reasons.append(f"kind default: {kind} -> {admission}")

    if readiness_hint:
        hinted = READINESS_TO_ADMISSION.get(readiness_hint)
        if hinted:
            admission = _min_admission(admission, hinted)
            reasons.append(f"readiness hint applied conservatively: {readiness_hint} -> {hinted}")
        else:
            checklist["ambiguity_note"] = f"Unknown readiness hint: {readiness_hint}"
            admission = _min_admission(admission, "evidence_only")
            reasons.append("unknown readiness hint; kept at evidence_only or lower")

    if not exists:
        admission = "reject_for_upper"
        reasons.append("artifact path does not exist")

    if kind == "runtime_residue":
        admission = "reject_for_upper"
        blocked.extend(["evidence_only", "ingest_ready", "packet_candidate"])
        reasons.append("runtime residue cannot become upper evidence or packet material")

    if admission == "packet_candidate":
        has_packet_basis = packet_worthiness_present or kind in {"preprocess_comparison", "gmd_native_read"}
        if not has_packet_basis:
            admission = "ingest_ready" if routing_present else "evidence_only"
            reasons.append("packet candidate blocked because packet-worthiness is not visible")
        if kind == "gmd_native_read" and not (provenance_present and trace_present):
            checklist["ambiguity_note"] = "GMD/native read should be paired with source/split/checklist support before packet use."
            reasons.append("packet candidate is cautious; supporting source/split evidence still needed")

    if admission == "ingest_ready" and not (routing_present or kind == "preprocessed_material"):
        admission = "evidence_only"
        reasons.append("ingest_ready downgraded because routing clarity is missing")

    if admission == "evidence_only":
        blocked.extend(["packet_candidate"])
    if admission == "ingest_ready":
        blocked.extend(["packet_candidate unless checklist supplies packet-worthiness"])
    if admission == "reject_for_upper":
        blocked.extend(["upper evidence use", "packet_candidate"])

    manual_note = ""
    if checklist["ambiguity_note"]:
        manual_note = checklist["ambiguity_note"]
    elif admission in {"evidence_only", "ingest_ready"}:
        manual_note = "Human/Codex interpretation may still be needed before forming an upper packet."
    elif admission == "packet_candidate":
        manual_note = "Packet candidate still requires normal upper interpretation; this is not baseline promotion."

    return {
        "artifact_path": path,
        "artifact_exists": exists,
        "artifact_kind": kind,
        "readiness_hint": readiness_hint,
        "upper_admission": admission,
        "classifier_confidence": "medium" if exists and kind != "unknown" else "low",
        "reasons": reasons,
        "blocked_higher_admission": sorted(set(blocked)),
        "checklist_signals": checklist,
        "manual_note": manual_note,
        "guardrail": {
            "readiness_not_promoted": True,
            "evidence_only_is_normal_landing_zone": True,
            "baseline_promotion": False,
            "final_naming_lock": False,
            "canonical_path_moved": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_path")
    parser.add_argument("--readiness-hint", choices=list(READINESS_TO_ADMISSION), default="")
    parser.add_argument("--artifact-kind", default="")
    parser.add_argument("--provenance-present", action="store_true")
    parser.add_argument("--trace-present", action="store_true")
    parser.add_argument("--routing-present", action="store_true")
    parser.add_argument("--packet-worthiness-present", action="store_true")
    args = parser.parse_args()
    result = classify(
        args.artifact_path,
        readiness_hint=args.readiness_hint,
        artifact_kind=args.artifact_kind,
        provenance_present=args.provenance_present,
        trace_present=args.trace_present,
        routing_present=args.routing_present,
        packet_worthiness_present=args.packet_worthiness_present,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
