"""Bounded JSON diff helpers for Phase 1.9 diff salience."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from structured_helpers import asset_kind_for_path
from pairing_helpers import pair_json_assets_with_metadata

MAX_DIFF_UNITS = 8
MAX_VALUE_CHARS = 500
TRIVIAL_TERMS = ("created_at", "record_id", "question_packet_ref", "exploration_result_ref", "merge_diff_report_ref")
SALIENT_TERMS = (
    "chosen_mode",
    "mode",
    "status",
    "validation",
    "evidence_depth",
    "excerpt_quality",
    "structured_evidence",
    "diff_evidence",
    "confidence",
    "grounding",
    "risk",
    "hold",
    "decision",
)


def _walk(value: Any, path: str = "$") -> Iterable[Tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for idx, child in enumerate(value[:5]):
            yield from _walk(child, f"{path}[{idx}]")


def _load(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _excerpt(value: Any) -> str:
    text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return text if len(text) <= MAX_VALUE_CHARS else text[:MAX_VALUE_CHARS] + "..."


def _change_type(path: str, before: Any, after: Any, base: str) -> str:
    lowered = path.lower()
    if base == "added":
        return "added"
    if base == "removed":
        return "removed"
    if "chosen_mode" in lowered or lowered.endswith(".mode"):
        return "mode_shift"
    if "status" in lowered:
        return "status_change"
    if "evidence_depth" in lowered or "cross_supported" in lowered or "pointer_only" in lowered:
        return "evidence_depth_change"
    if isinstance(before, (int, float)) and isinstance(after, (int, float)):
        return "count_change"
    return "modified"


def _salience(path: str, change_type: str, reason: str) -> Tuple[int, bool]:
    lowered = f"{path} {change_type} {reason}".lower()
    trivial = any(term in lowered for term in TRIVIAL_TERMS)
    score = sum(3 for term in SALIENT_TERMS if term in lowered)
    if change_type in {"mode_shift", "status_change", "evidence_depth_change"}:
        score += 5
    if change_type in {"added", "removed"}:
        score += 2
    if trivial:
        score -= 6
    return score, trivial


def _unit(before_path: str, after_path: str, path_ref: str, before: Any, after: Any, change_type: str, reason: str, trivial: bool) -> Dict[str, Any]:
    before_excerpt = "" if change_type == "added" else _excerpt(before)
    after_excerpt = "" if change_type == "removed" else _excerpt(after)
    delta_summary = f"{path_ref} {change_type}: {before_excerpt} -> {after_excerpt}"
    return {
        "source_ref_before": before_path,
        "source_ref_after": after_path,
        "asset_kind": asset_kind_for_path(after_path),
        "path_ref": path_ref,
        "change_type": change_type,
        "before_excerpt": before_excerpt,
        "after_excerpt": after_excerpt,
        "delta_summary": delta_summary[:900],
        "salience_reason": "Selected by changed-path salience ranking." if not trivial else "Trivial path retained only as low-salience comparison context.",
        "why_it_matters": reason,
        "relation_type": "contrast",
        "grounding_status": "direct_grounded" if not trivial else "weak_grounded",
        "local_confidence": "high" if not trivial else "low",
        "comparison_hint": "salient_delta" if not trivial else "trivial_delta",
        "diff_quality": "salient_diff" if not trivial else "trivial_diff",
    }


def diff_json_pair(before_path: str, after_path: str, reason: str = "") -> List[Dict[str, Any]]:
    try:
        before = _load(before_path)
        after = _load(after_path)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return [
            {
                "source_ref_before": before_path,
                "source_ref_after": after_path,
                "asset_kind": asset_kind_for_path(after_path),
                "path_ref": "$",
                "change_type": "modified",
                "before_excerpt": "",
                "after_excerpt": "",
                "delta_summary": "Comparison fallback: one or both JSON files could not be parsed.",
                "salience_reason": "Diff fallback preserved.",
                "why_it_matters": reason,
                "relation_type": "weak_candidate",
                "grounding_status": "pointer_only",
                "local_confidence": "low",
                "comparison_hint": "comparison_fallback",
                "diff_quality": "comparison_fallback",
            }
        ]
    before_map = dict(_walk(before))
    after_map = dict(_walk(after))
    paths = sorted(set(before_map) | set(after_map))
    candidates = []
    for path_ref in paths:
        if path_ref == "$":
            continue
        if path_ref not in before_map:
            change = "added"
            before_value = None
            after_value = after_map[path_ref]
        elif path_ref not in after_map:
            change = "removed"
            before_value = before_map[path_ref]
            after_value = None
        elif before_map[path_ref] != after_map[path_ref]:
            before_value = before_map[path_ref]
            after_value = after_map[path_ref]
            change = "modified"
        else:
            continue
        change_type = _change_type(path_ref, before_value, after_value, change)
        score, trivial = _salience(path_ref, change_type, reason)
        candidates.append((score, path_ref, before_value, after_value, change_type, trivial))
    candidates.sort(key=lambda item: (-item[0], item[1]))
    return [
        _unit(before_path, after_path, path_ref, before_value, after_value, change_type, reason, trivial)
        for score, path_ref, before_value, after_value, change_type, trivial in candidates[:MAX_DIFF_UNITS]
    ]


def summarize_diff_units(units: List[Dict[str, Any]]) -> Dict[str, int]:
    keys = ["added", "removed", "modified", "mode_shift", "count_change", "status_change", "evidence_depth_change"]
    summary = {key: sum(1 for unit in units if unit.get("change_type") == key) for key in keys}
    summary["trivial"] = sum(1 for unit in units if unit.get("diff_quality") == "trivial_diff")
    summary["comparison_fallback"] = sum(1 for unit in units if unit.get("diff_quality") == "comparison_fallback")
    summary["salient_diff"] = sum(1 for unit in units if unit.get("diff_quality") == "salient_diff")
    summary["total"] = len(units)
    return summary


def pair_json_assets(paths: List[str]) -> List[Tuple[str, str]]:
    return [
        (unit["source_ref_before"], unit["source_ref_after"])
        for unit in pair_json_assets_with_metadata(paths)
    ]
