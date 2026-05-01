from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from uuid import uuid4

from app.core.runtime.external_input_gate import assess_external_input_gate
from app.core.runtime.external_transcript_preprocess import preprocess_transcript_file
from app.core.runtime.inputter import build_dust_inputs_from_source
from app.core.runtime.labeler import label_dust_inputs
from app.core.runtime.lower_support_layers import build_support_layers_for_preprocess_comparison


def build_transcript_preprocess_comparison(input_path: Path) -> Dict[str, object]:
    before_gate = assess_external_input_gate(input_path)
    before_probe = _build_probe_summary(input_path)

    preprocess = preprocess_transcript_file(input_path)
    preprocessed_text_path = _build_sidecar_path(input_path)
    preprocessed_text_path.parent.mkdir(parents=True, exist_ok=True)
    preprocessed_text_path.write_text(preprocess.normalized_text, encoding="utf-8")

    after_gate = assess_external_input_gate(preprocessed_text_path)
    after_probe = _build_probe_summary(preprocessed_text_path)

    comparison = {
        "dust_count_delta": after_probe["dust_count"] - before_probe["dust_count"],
        "short_dust_ratio_delta": round(
            float(after_probe["short_dust_ratio"]) - float(before_probe["short_dust_ratio"]),
            3,
        ),
        "avg_chars_per_dust_delta": round(
            float(after_probe["avg_chars_per_dust"]) - float(before_probe["avg_chars_per_dust"]),
            2,
        ),
        "regrouped_chunk_count": preprocess.regrouped_chunk_count,
        "dropped_interjection_count": preprocess.dropped_interjection_count,
        "readiness_read": _build_readiness_read(before_gate, after_gate, before_probe, after_probe),
        "check_surface": {
            "what_improved": _what_improved(before_probe, after_probe),
            "what_is_still_missing": _what_is_still_missing(after_gate, after_probe),
            "next_checkpoint": _next_checkpoint(after_gate),
        },
    }

    payload = {
        "comparison_name": "transcript_preprocess_comparison_v0",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "input_path": str(input_path).replace("\\", "/"),
        "preprocessed_path": str(preprocessed_text_path).replace("\\", "/"),
        "before_gate": before_gate,
        "after_gate": after_gate,
        "before_probe": before_probe,
        "after_probe": after_probe,
        "comparison": comparison,
    }
    payload["support_layers"] = build_support_layers_for_preprocess_comparison(payload)
    return payload


def _build_probe_summary(input_path: Path) -> Dict[str, object]:
    raw_text = input_path.read_text(encoding="utf-8").strip()
    created_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    source_ref = str(input_path).replace("\\", "/")
    source_id = f"src_{uuid4().hex[:12]}"
    dust_inputs = build_dust_inputs_from_source(
        source_id=source_id,
        source_type="text",
        source_ref=source_ref,
        raw_payload=raw_text,
        created_at=created_at,
    )
    labeled = label_dust_inputs(dust_inputs)
    dust_count = max(1, len(labeled))
    short_dust_count = sum(1 for row in labeled if len(row.text.strip()) <= 18)
    scene_counter: Counter[str] = Counter(row.scene for row in labeled)
    flow_counter: Counter[str] = Counter(row.flow for row in labeled)
    return {
        "dust_count": len(labeled),
        "short_dust_ratio": round(short_dust_count / dust_count, 3),
        "avg_chars_per_dust": round(sum(len(row.text.strip()) for row in labeled) / dust_count, 2),
        "top_scene_counts": dict(scene_counter.most_common(4)),
        "top_flow_counts": dict(flow_counter.most_common(4)),
        "sample_short_labels": [row.short_label for row in labeled[:8]],
    }


def _build_sidecar_path(input_path: Path) -> Path:
    repo_root = Path(__file__).resolve().parents[3]
    output_dir = repo_root / "app" / "work" / "external_input_preprocess" / "generated"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return output_dir / f"{input_path.stem}_transcript_regroup_compare_{stamp}.txt"


def _build_readiness_read(
    before_gate: Dict[str, object],
    after_gate: Dict[str, object],
    before_probe: Dict[str, object],
    after_probe: Dict[str, object],
) -> Dict[str, str]:
    if after_gate["decision"] == "direct_ingest_ok":
        status = "direct_ingest_more_plausible"
        reason = "post-preprocess shape is structured enough to consider direct intake"
    elif after_gate["decision"] == "uncertain_needs_probe":
        status = "probe_again_before_ingest"
        reason = "preprocess reduced transcript noise, but intake should still be checked before mutation"
    else:
        status = "preprocess_not_enough"
        reason = "subtitle-like fragmentation pressure still looks too strong after regroup"
    return {
        "status": status,
        "reason": reason,
        "before_dust_count": str(before_probe["dust_count"]),
        "after_dust_count": str(after_probe["dust_count"]),
    }


def _what_improved(before_probe: Dict[str, object], after_probe: Dict[str, object]) -> List[str]:
    rows: List[str] = []
    if int(after_probe["dust_count"]) < int(before_probe["dust_count"]):
        rows.append("dust count moved down toward larger meaning units")
    if float(after_probe["avg_chars_per_dust"]) > float(before_probe["avg_chars_per_dust"]):
        rows.append("average chars per dust increased, so each unit carries more local context")
    if float(after_probe["short_dust_ratio"]) < float(before_probe["short_dust_ratio"]):
        rows.append("short shard ratio decreased")
    return rows or ["no clear improvement signal at probe level"]


def _what_is_still_missing(after_gate: Dict[str, object], after_probe: Dict[str, object]) -> List[str]:
    rows: List[str] = []
    if after_gate["decision"] != "direct_ingest_ok":
        rows.append("post-preprocess state is still not direct-ingest-safe")
    if float(after_probe["short_dust_ratio"]) >= 0.2:
        rows.append("short shard ratio is still high enough to flatten local context")
    if after_probe["top_flow_counts"].get("compare", 0) == after_probe["dust_count"]:
        rows.append("flow reading still looks too flat")
    return rows or ["no major missing point surfaced in this bounded comparison"]


def _next_checkpoint(after_gate: Dict[str, object]) -> str:
    if after_gate["decision"] == "direct_ingest_ok":
        return "run bounded post-preprocess intake probe before any real ingest"
    if after_gate["decision"] == "uncertain_needs_probe":
        return "use the preprocessed sidecar for bounded first-pass/probe before runtime mutation"
    return "refine regroup rules before trying intake again"
