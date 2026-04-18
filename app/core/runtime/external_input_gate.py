from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence
import re
from uuid import uuid4

from app.core.runtime.inputter import build_dust_inputs_from_source
from app.core.runtime.labeler import label_dust_inputs


TIMECODE_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b")
KOREAN_TIME_RE = re.compile(r"\b\d+분\s*\d+초\b")
TRANSCRIPT_MARKER_RE = re.compile(r"(?:챕터\s*\d+|\b\d+:\d{2,}초?)")
MARKDOWN_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+")
SHORT_INTERJECTION_SET = {
    "네",
    "네.",
    "음",
    "음.",
    "아",
    "아.",
    "어",
    "어.",
    "그죠?",
    "맞아요.",
    "맞아요",
    "그렇죠?",
    "그쵸?",
    "오",
    "오.",
}


@dataclass(frozen=True)
class GateDecision:
    decision: str
    decision_reason: str
    format_profile: str
    should_preprocess: bool
    preprocess_kind: str | None


def assess_external_input_gate(input_path: Path) -> Dict[str, object]:
    raw_text = input_path.read_text(encoding="utf-8").strip()
    created_at = _now_iso()
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

    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    stripped_lines = [_strip_transcript_noise(line) for line in lines]
    short_line_count = sum(1 for line in stripped_lines if 0 < len(line) <= 12)
    interjection_count = sum(1 for line in stripped_lines if line in SHORT_INTERJECTION_SET)
    timestamp_line_count = sum(
        1 for line in lines if TIMECODE_RE.search(line) or KOREAN_TIME_RE.search(line)
    )
    timestamp_token_count = sum(
        len(TIMECODE_RE.findall(line)) + len(KOREAN_TIME_RE.findall(line)) for line in lines
    )
    heading_count = sum(1 for line in lines if MARKDOWN_HEADING_RE.match(line))
    short_dust_count = sum(1 for row in labeled if len(_strip_transcript_noise(row.text)) <= 12)
    timestamp_dust_count = sum(
        1 for row in labeled if TIMECODE_RE.search(row.text) or KOREAN_TIME_RE.search(row.text)
    )
    transcript_marker_count = sum(1 for line in lines if TRANSCRIPT_MARKER_RE.search(line))
    transcript_marker_dust_count = sum(
        1 for row in labeled if TRANSCRIPT_MARKER_RE.search(row.text)
    )

    dust_count = len(labeled)
    line_count = max(1, len(lines))
    safe_dust_count = max(1, dust_count)
    avg_chars_per_dust = round(
        sum(len(_strip_transcript_noise(row.text)) for row in labeled) / safe_dust_count,
        2,
    )
    scene_counter = Counter(row.scene for row in labeled)
    flow_counter = Counter(row.flow for row in labeled)

    metrics = {
        "line_count": len(lines),
        "dust_count": dust_count,
        "timestamp_line_count": timestamp_line_count,
        "timestamp_density": round(timestamp_line_count / line_count, 3),
        "timestamp_token_count": timestamp_token_count,
        "markdown_heading_count": heading_count,
        "transcript_marker_count": transcript_marker_count,
        "transcript_marker_density": round(transcript_marker_count / line_count, 3),
        "short_line_count": short_line_count,
        "short_line_ratio": round(short_line_count / line_count, 3),
        "interjection_count": interjection_count,
        "interjection_ratio": round(interjection_count / line_count, 3),
        "short_dust_count": short_dust_count,
        "short_dust_ratio": round(short_dust_count / safe_dust_count, 3),
        "timestamp_dust_count": timestamp_dust_count,
        "timestamp_dust_ratio": round(timestamp_dust_count / safe_dust_count, 3),
        "transcript_marker_dust_count": transcript_marker_dust_count,
        "transcript_marker_dust_ratio": round(transcript_marker_dust_count / safe_dust_count, 3),
        "avg_chars_per_dust": avg_chars_per_dust,
        "top_scene_counts": dict(scene_counter.most_common(5)),
        "top_flow_counts": dict(flow_counter.most_common(5)),
        "sample_short_labels": [row.short_label for row in labeled[:10]],
    }

    decision = _decide_gate(input_path, metrics)
    return {
        "input_path": str(input_path).replace("\\", "/"),
        "decision": decision.decision,
        "decision_reason": decision.decision_reason,
        "format_profile": decision.format_profile,
        "should_preprocess": decision.should_preprocess,
        "preprocess_kind": decision.preprocess_kind,
        "metrics": metrics,
        "checkpoints": _build_checkpoint_reading(decision, metrics),
    }


def _decide_gate(input_path: Path, metrics: Dict[str, object]) -> GateDecision:
    suffix = input_path.suffix.lower()
    timestamp_density = float(metrics["timestamp_density"])
    short_dust_ratio = float(metrics["short_dust_ratio"])
    timestamp_dust_ratio = float(metrics["timestamp_dust_ratio"])
    transcript_marker_dust_ratio = float(metrics["transcript_marker_dust_ratio"])
    interjection_ratio = float(metrics["interjection_ratio"])
    heading_count = int(metrics["markdown_heading_count"])
    avg_chars_per_dust = float(metrics["avg_chars_per_dust"])
    dust_count = int(metrics["dust_count"])

    if (
        suffix == ".txt"
        and (
            timestamp_density >= 0.08
            or timestamp_dust_ratio >= 0.12
            or transcript_marker_dust_ratio >= 0.12
            or interjection_ratio >= 0.05
        )
        and (short_dust_ratio >= 0.2 or avg_chars_per_dust <= 30 or dust_count >= 180)
    ):
        return GateDecision(
            decision="preprocess_required",
            decision_reason=(
                "timestamp/interjection-heavy transcript-like input; direct dust split is likely to "
                "produce subtitle-like units rather than meaning chunks"
            ),
            format_profile="raw_transcript_like",
            should_preprocess=True,
            preprocess_kind="transcript_aware_regroup",
        )
    if suffix == ".md" and heading_count > 0 and timestamp_density < 0.03 and short_dust_ratio < 0.2:
        return GateDecision(
            decision="direct_ingest_ok",
            decision_reason=(
                "structured markdown-like input with low transcript noise; direct intake is likely acceptable"
            ),
            format_profile="structured_markdown_like",
            should_preprocess=False,
            preprocess_kind=None,
        )
    return GateDecision(
        decision="uncertain_needs_probe",
        decision_reason=(
            "input shape is mixed; raw probe is useful first, then decide whether transcript-aware regroup is needed"
        ),
        format_profile="mixed_or_unclear",
        should_preprocess=False,
        preprocess_kind=None,
    )


def _build_checkpoint_reading(
    decision: GateDecision,
    metrics: Dict[str, object],
) -> Dict[str, object]:
    return {
        "pre_ingest_gate": {
            "status": decision.decision,
            "reason": decision.decision_reason,
            "focus": (
                "decide direct ingest vs preprocess before mutating runtime"
            ),
        },
        "preprocess_signals": {
            "timestamp_density": metrics["timestamp_density"],
            "timestamp_dust_ratio": metrics["timestamp_dust_ratio"],
            "transcript_marker_dust_ratio": metrics["transcript_marker_dust_ratio"],
            "interjection_ratio": metrics["interjection_ratio"],
            "short_dust_ratio": metrics["short_dust_ratio"],
            "avg_chars_per_dust": metrics["avg_chars_per_dust"],
            "sample_short_labels": metrics["sample_short_labels"],
        },
        "post_preprocess_checkpoints": [
            "dust count should fall toward meaning-sized units, not subtitle shards",
            "short interjection rows should be absorbed when they are only response tails",
            "timestamp tokens should stop dominating unit starts",
        ],
        "post_ingest_checkpoints": [
            "trace/cell formation should look like semantic regroup, not one coarse cell swallowing all rows",
            "scene/flow distribution should become less flat if segmentation quality improves",
            "sample material text should preserve a local claim + context together",
        ],
        "line_readiness_checkpoints": [
            "only after input quality stabilizes should line corroboration be read as meaningful",
            "path or breadth claims should not be made from subtitle-like shard accumulation",
        ],
    }


def _strip_transcript_noise(text: str) -> str:
    cleaned = TIMECODE_RE.sub("", text)
    cleaned = KOREAN_TIME_RE.sub("", cleaned)
    return cleaned.strip()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
