"""Bounded JSON/path helpers for Phase 1.8 structured evidence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

SALIENT_TERMS = (
    "evidence",
    "validation",
    "mode",
    "status",
    "required",
    "trigger",
    "learning",
    "summary",
    "chosen",
    "decision",
    "risk",
    "quality",
    "confidence",
    "grounding",
    "artifact",
    "refs",
)
MAX_STRUCTURED_UNITS = 6
MAX_VALUE_CHARS = 700


def is_structured_asset(path: str) -> bool:
    return Path(path).suffix.lower() == ".json"


def asset_kind_for_path(path: str) -> str:
    if path.startswith("runtime/contracts/"):
        return "runtime_contract"
    if path.startswith("runtime/"):
        return "runtime_artifact"
    if path.endswith(".json"):
        return "config_json"
    return "structured_note"


def _node_kind(value: Any) -> str:
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    return "scalar"


def _shape_summary(value: Any) -> str:
    if isinstance(value, dict):
        keys = list(value.keys())
        shown = ", ".join(keys[:8])
        suffix = "..." if len(keys) > 8 else ""
        return f"object keys: {shown}{suffix}"
    if isinstance(value, list):
        return f"array length: {len(value)}"
    return f"scalar type: {type(value).__name__}"


def _value_excerpt(value: Any) -> str:
    text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    if len(text) > MAX_VALUE_CHARS:
        return text[:MAX_VALUE_CHARS] + "..."
    return text


def _walk(value: Any, path: str = "$") -> Iterable[tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for idx, child in enumerate(value[:3]):
            yield from _walk(child, f"{path}[{idx}]")


def _salience_score(path: str, value: Any, reason: str) -> int:
    lowered = f"{path} {reason}".lower()
    score = sum(2 for term in SALIENT_TERMS if term in lowered)
    if not isinstance(value, (dict, list)):
        score += 1
    if path in {"$.contract_id", "$.contract_status", "$.extends"}:
        score -= 2
    return score


def extract_structured_evidence(path: str, reason: str = "", relation_type: str = "contextual_support") -> List[Dict[str, Any]]:
    source = Path(path)
    if not is_structured_asset(path) or not source.exists() or not source.is_file():
        return []
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return [
            {
                "source_ref": path,
                "asset_kind": asset_kind_for_path(path),
                "pointer": path,
                "path_ref": "$",
                "node_kind": "shape_summary",
                "shape_summary": "unreadable_json",
                "value_excerpt": "",
                "why_it_matters": reason,
                "relation_type": relation_type,
                "grounding_status": "pointer_only",
                "local_confidence": "low",
                "salience_reason": "JSON could not be parsed; pointer fallback preserved.",
                "comparison_hint": "structured_fallback",
                "structured_quality": "structured_fallback",
            }
        ]
    candidates = []
    for node_path, value in _walk(data):
        score = _salience_score(node_path, value, reason)
        if node_path == "$":
            score += 1
        if score > 0:
            candidates.append((score, node_path, value))
    candidates.sort(key=lambda item: (-item[0], item[1]))
    selected = candidates[:MAX_STRUCTURED_UNITS]
    if not selected:
        selected = [(0, "$", data)]
    units = []
    for score, node_path, value in selected:
        identity_only = node_path in {"$.contract_id", "$.contract_status", "$.extends"}
        quality = "identity_only" if identity_only else ("shape_only" if node_path == "$" else "salient_path")
        confidence = "low" if quality == "identity_only" else ("medium" if quality == "shape_only" else "high")
        status = "weak_grounded" if quality in {"identity_only", "shape_only"} else "direct_grounded"
        units.append(
            {
                "source_ref": path,
                "asset_kind": asset_kind_for_path(path),
                "pointer": f"{path}:{node_path}",
                "path_ref": node_path,
                "node_kind": _node_kind(value) if node_path != "$" else "shape_summary",
                "shape_summary": _shape_summary(value),
                "value_excerpt": _value_excerpt(value) if node_path != "$" else "",
                "why_it_matters": reason,
                "relation_type": relation_type,
                "grounding_status": status,
                "local_confidence": confidence,
                "salience_reason": "Selected by structured path salience terms and bounded JSON traversal.",
                "comparison_hint": "review_path_value" if quality == "salient_path" else quality,
                "structured_quality": quality,
            }
        )
    return units


def summarize_structured_units(units: List[Dict[str, Any]]) -> Dict[str, int]:
    return {
        "identity_only": sum(1 for unit in units if unit.get("structured_quality") == "identity_only"),
        "shape_only": sum(1 for unit in units if unit.get("structured_quality") == "shape_only"),
        "salient_path": sum(1 for unit in units if unit.get("structured_quality") == "salient_path"),
        "structured_fallback": sum(1 for unit in units if unit.get("structured_quality") == "structured_fallback"),
        "total": len(units),
    }
