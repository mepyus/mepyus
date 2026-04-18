from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional


BROAD_PRIMARY_FORBIDDEN = {
    "object.field.ai",
    "object.org.deepseek",
    "object.system.claude",
    "object.country.china",
}

ROW_PRIMARY_KEY_MAP = {
    "packet_texture": "semantic.row.packet_texture",
    "grounding_status": "semantic.row.grounding_status",
    "emergence_status": "semantic.row.emergence_status",
    "carryover_risk": "semantic.row.carryover_risk",
    "maturation_state": "semantic.row.maturation_state",
    "traceability_status": "semantic.row.traceability_status",
}

ROW_SUPPORT_KEYS = {
    "packet_texture": ["structural.role.definition"],
    "grounding_status": ["structural.role.definition"],
    "emergence_status": ["structural.role.bridge"],
    "carryover_risk": ["structural.role.background"],
    "maturation_state": ["structural.role.background"],
    "traceability_status": ["structural.role.definition"],
}

NORMALIZE_MAP = {
    "Claude": "object.system.claude",
    "claude": "object.system.claude",
    "MoE": "object.architecture.moe",
    "moe": "object.architecture.moe",
    "AlphaGo": "object.system.alphago",
    "Google DeepMind": "object.org.google_deepmind",
    "China": "object.country.china",
    "DeepSeek": "object.org.deepseek",
    "Mistral": "object.org.mistral",
    "Moonshot": "object.org.moonshot",
    "TensorFlow": "object.framework.tensorflow",
    "AI": "object.field.ai",
    "CLAUDE.md": "source.claude_md",
}


def project_candidate_rule_binding(
    candidate: Dict[str, Any],
    *,
    reading_context: Optional[Dict[str, Any]] = None,
    runtime_root: Optional[Path] = None,
) -> Dict[str, Any]:
    object_match = _match_first_pass_binding(
        runtime_root=runtime_root,
        source_pointer=str((reading_context or {}).get("object_source_pointer") or (reading_context or {}).get("source_pointer") or ""),
        paragraph_text=str((reading_context or {}).get("object_paragraph_text") or ""),
        prefer_anchor_type="object",
    )
    value_match = _match_first_pass_binding(
        runtime_root=runtime_root,
        source_pointer=str((reading_context or {}).get("value_source_pointer") or (reading_context or {}).get("source_pointer") or candidate.get("source_pointer") or ""),
        paragraph_text=str((reading_context or {}).get("value_paragraph_text") or candidate.get("original_preview") or ""),
        prefer_anchor_type=None,
    )

    object_key = object_match.get("primary_rule_key") or _project_object_key(candidate)
    value_key = value_match.get("primary_rule_key") or _project_value_key(candidate)
    value_status = _project_status(value_key)
    support_rule_keys = _merge_keys(
        list(value_match.get("support_rule_keys") or []),
        _project_support_keys(candidate, value_key=value_key),
    )
    scene = str(value_match.get("scene") or "").strip()
    flow = str(value_match.get("flow") or "").strip()
    if not scene or not flow:
        scene, flow = _project_axis(candidate)
    primary_rule_key = value_key if value_status == "primary_rule_key" else ""
    return {
        "object_key": object_key,
        "object_status": _project_status(object_key),
        "object_label": object_match.get("primary_label") or "",
        "value_key": value_key,
        "value_status": value_status,
        "value_label": value_match.get("primary_label") or "",
        "primary_rule_key": primary_rule_key,
        "support_rule_keys": support_rule_keys,
        "support_only": _merge_keys(
            list(object_match.get("support_only") or []),
            list(value_match.get("support_only") or []),
            [value_key] if value_status == "support_only" and value_key else [],
        ),
        "provenance_only": _merge_keys(
            list(object_match.get("provenance_only") or []),
            list(value_match.get("provenance_only") or []),
            [value_key] if value_status == "provenance_only" and value_key else [],
        ),
        "watchlist_only": _merge_keys(
            list(object_match.get("watchlist_only") or []),
            list(value_match.get("watchlist_only") or []),
            [value_key] if value_status == "watchlist_only" and value_key else [],
        ),
        "binding_source": "first_pass_canonical" if value_match.get("matched") else "provisional_row_fallback",
        "object_fragment_id": object_match.get("fragment_id") or "",
        "value_fragment_id": value_match.get("fragment_id") or "",
        "scene": scene,
        "flow": flow,
    }


def _project_object_key(candidate: Dict[str, Any]) -> str:
    raw = str(candidate.get("object_key") or candidate.get("object") or candidate.get("source_asset") or "").strip()
    if raw in NORMALIZE_MAP:
        return NORMALIZE_MAP[raw]
    if raw.startswith("object.") or raw.startswith("semantic.") or raw.startswith("structural.") or raw.startswith("source.") or raw.startswith("observer."):
        return raw
    return f"object.asset.{_slug(raw or 'unknown')}"


def _project_value_key(candidate: Dict[str, Any]) -> str:
    explicit = str(candidate.get("value_key") or "").strip()
    if explicit:
        if explicit in NORMALIZE_MAP:
            return NORMALIZE_MAP[explicit]
        return explicit
    source_kind = str(candidate.get("source_kind") or "").strip()
    candidate_kind = str(candidate.get("candidate_kind") or "").strip()
    row_key = str(candidate.get("row_key") or "").strip()
    support_row_key = str(candidate.get("support_row_key") or "").strip()
    source_pointer = str(candidate.get("source_pointer") or "").strip()
    if row_key and row_key in ROW_PRIMARY_KEY_MAP:
        return ROW_PRIMARY_KEY_MAP[row_key]
    if candidate_kind == "reason":
        return f"structural.role.bridge:{_slug(source_pointer or 'reason')}"
    if candidate_kind == "evidence" and source_kind == "source_file":
        if support_row_key and support_row_key in ROW_PRIMARY_KEY_MAP:
            return ROW_PRIMARY_KEY_MAP[support_row_key]
        return "source.document"
    if candidate_kind == "evidence":
        return f"source.{_slug(source_kind or 'evidence')}"
    if source_pointer.startswith("observer.semantic."):
        return source_pointer
    return ""


def _project_support_keys(candidate: Dict[str, Any], *, value_key: str) -> List[str]:
    keys: List[str] = []
    row_key = str(candidate.get("row_key") or "").strip()
    support_row_key = str(candidate.get("support_row_key") or "").strip()
    if row_key and row_key in ROW_SUPPORT_KEYS:
        keys.extend(ROW_SUPPORT_KEYS[row_key])
    if support_row_key and support_row_key in ROW_SUPPORT_KEYS:
        keys.extend(ROW_SUPPORT_KEYS[support_row_key])
    if str(candidate.get("candidate_kind") or "") == "reason":
        keys.append("structural.role.bridge")
    if value_key.startswith("source."):
        keys.append("structural.role.background")
    deduped: List[str] = []
    seen = set()
    for key in keys:
        normalized = NORMALIZE_MAP.get(key, key)
        if normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(normalized)
    return deduped


def _project_status(key: str) -> str:
    if not key:
        return "watchlist_only"
    normalized = NORMALIZE_MAP.get(key, key)
    if normalized.startswith("observer.semantic."):
        return "watchlist_only"
    if normalized.startswith("source."):
        return "provenance_only"
    if normalized.startswith("structural.role."):
        return "support_only"
    if normalized.startswith("object.asset."):
        return "support_only"
    if normalized in BROAD_PRIMARY_FORBIDDEN:
        return "support_only"
    if normalized.startswith("object.") or normalized.startswith("semantic."):
        return "primary_rule_key"
    return "watchlist_only"


def _project_axis(candidate: Dict[str, Any]) -> tuple[str, str]:
    kind = str(candidate.get("candidate_kind") or "").strip()
    source_kind = str(candidate.get("source_kind") or "").strip()
    if kind == "reason":
        return ("comparison", "bridge")
    if kind == "evidence" and source_kind == "source_file":
        return ("evidence", "bridge")
    if kind == "evidence":
        return ("evidence", "contract")
    if kind == "state":
        return ("explanation", "expand")
    return ("reflection", "contract")


def _match_first_pass_binding(
    *,
    runtime_root: Optional[Path],
    source_pointer: str,
    paragraph_text: str,
    prefer_anchor_type: Optional[str],
) -> Dict[str, Any]:
    if runtime_root is None:
        return {}
    paragraph_text = (paragraph_text or "").strip()
    if not paragraph_text:
        return {}
    fragments = _load_first_pass_fragments(runtime_root.resolve())
    scored: List[tuple[int, Dict[str, Any]]] = []
    source_name = Path(source_pointer).name if source_pointer else ""
    normalized_paragraph = _normalize_text(paragraph_text)
    for fragment in fragments:
        score = 0
        fragment_source = str(fragment.get("source_path") or "")
        if source_name and Path(fragment_source).name == source_name:
            score += 3
        raw_text = str(fragment.get("raw_text") or "")
        normalized_raw = _normalize_text(raw_text)
        if normalized_raw and normalized_paragraph:
            if normalized_raw in normalized_paragraph or normalized_paragraph in normalized_raw:
                score += 8
            else:
                overlap = _token_overlap(normalized_raw, normalized_paragraph)
                score += min(overlap, 4)
        if score > 0:
            scored.append((score, fragment))
    if not scored:
        return {}
    scored.sort(key=lambda item: item[0], reverse=True)
    best_score, fragment = scored[0]
    if best_score < 4:
        return {}
    return _project_fragment_binding(fragment, prefer_anchor_type=prefer_anchor_type)


def _project_fragment_binding(fragment: Dict[str, Any], *, prefer_anchor_type: Optional[str]) -> Dict[str, Any]:
    anchors = [anchor for anchor in (fragment.get("anchors") or []) if isinstance(anchor, dict)]
    projected = []
    for anchor in anchors:
        key = str(anchor.get("canonical_key") or anchor.get("key") or "").strip()
        if key in NORMALIZE_MAP:
            key = NORMALIZE_MAP[key]
        status = _project_status(key)
        projected.append(
            {
                "key": key,
                "label": str(anchor.get("label") or anchor.get("value") or "").strip(),
                "anchor_type": str(anchor.get("anchor_type") or "").strip(),
                "status": status,
            }
        )
    primary = _pick_primary_anchor(projected, prefer_anchor_type=prefer_anchor_type)
    return {
        "matched": True,
        "fragment_id": str(fragment.get("fragment_id") or "").strip(),
        "scene": str(fragment.get("scene") or "").strip(),
        "flow": str(fragment.get("flow") or "").strip(),
        "primary_rule_key": primary.get("key") or "",
        "primary_label": primary.get("label") or "",
        "support_rule_keys": [item["key"] for item in projected if item["status"] == "support_only"],
        "provenance_only": [item["key"] for item in projected if item["status"] == "provenance_only"],
        "watchlist_only": [item["key"] for item in projected if item["status"] == "watchlist_only"],
        "support_only": [item["key"] for item in projected if item["status"] == "support_only"],
    }


def _pick_primary_anchor(projected: List[Dict[str, Any]], *, prefer_anchor_type: Optional[str]) -> Dict[str, Any]:
    primary = [item for item in projected if item["status"] == "primary_rule_key"]
    if prefer_anchor_type:
        typed = [item for item in primary if item["anchor_type"] == prefer_anchor_type]
        if typed:
            return typed[0]
    if primary:
        return primary[0]
    if prefer_anchor_type:
        typed_support = [item for item in projected if item["anchor_type"] == prefer_anchor_type and item["status"] == "support_only"]
        if typed_support:
            return typed_support[0]
    support = [item for item in projected if item["status"] == "support_only"]
    if support:
        return support[0]
    return {}


@lru_cache(maxsize=4)
def _load_first_pass_fragments(runtime_root: Path) -> List[Dict[str, Any]]:
    fragment_dir = runtime_root / "fragments"
    rows: List[Dict[str, Any]] = []
    if not fragment_dir.exists():
        return rows
    for path in sorted(fragment_dir.glob("*.json")):
        try:
            rows.append(json.loads(path.read_text(encoding="utf-8")))
        except Exception:
            continue
    return rows


def _normalize_text(value: str) -> str:
    return " ".join((value or "").replace("\n", " ").split()).strip().lower()


def _token_overlap(left: str, right: str) -> int:
    left_tokens = {token for token in left.split() if len(token) > 1}
    right_tokens = {token for token in right.split() if len(token) > 1}
    return len(left_tokens & right_tokens)


def _merge_keys(*groups: List[str]) -> List[str]:
    merged: List[str] = []
    seen = set()
    for group in groups:
        for item in group:
            normalized = NORMALIZE_MAP.get(item, item)
            if not normalized or normalized in seen:
                continue
            seen.add(normalized)
            merged.append(normalized)
    return merged


def _slug(value: str) -> str:
    lowered = value.strip().lower()
    cleaned = []
    for char in lowered:
        cleaned.append(char if char.isalnum() else "_")
    collapsed = "".join(cleaned).strip("_")
    while "__" in collapsed:
        collapsed = collapsed.replace("__", "_")
    return collapsed or "item"
