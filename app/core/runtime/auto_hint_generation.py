from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Sequence


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_path_tokens(path_expr: str) -> List[str]:
    return [token for token in path_expr.split(".") if token]


def _descend_values(current: Any, token: str) -> List[Any]:
    if token.endswith("[]"):
        key = token[:-2]
        if not isinstance(current, dict):
            return []
        value = current.get(key)
        if not isinstance(value, list):
            return []
        return list(value)

    if isinstance(current, dict) and token in current:
        return [current[token]]
    return []


def extract_values(payload: Any, path_expr: str) -> List[Any]:
    values: List[Any] = [payload]
    for token in _normalize_path_tokens(path_expr):
        next_values: List[Any] = []
        for value in values:
            next_values.extend(_descend_values(value, token))
        values = next_values
        if not values:
            return []
    return values


def _match_exists(payload: Dict[str, Any], field_expr: str) -> bool:
    return bool(extract_values(payload, field_expr))


def _match_equals(payload: Dict[str, Any], field_expr: str, expected: str) -> bool:
    values = extract_values(payload, field_expr)
    return any(str(value) == expected for value in values)


def pattern_matches(payload: Dict[str, Any], pattern: str) -> bool:
    if pattern.endswith(" exists"):
        return _match_exists(payload, pattern[: -len(" exists")])
    if "=" in pattern:
        field_expr, expected = pattern.split("=", 1)
        return _match_equals(payload, field_expr, expected)
    return False


def _artifact_kind_matches(rule_artifact_kind: str, artifact_path: Path) -> bool:
    if rule_artifact_kind == "comparison_result":
        return "comparison" in artifact_path.name
    if rule_artifact_kind == "phase_surface":
        return "phase" in artifact_path.name or "preflight" in artifact_path.name
    if rule_artifact_kind == "engine_state_index":
        return artifact_path.name == "index.json" and "engine_state_latest" in str(artifact_path)
    return True


def generate_hint_candidates(
    artifact_path: Path,
    rules_path: Path,
) -> List[Dict[str, Any]]:
    payload = load_json(artifact_path)
    rules_payload = load_json(rules_path)
    candidates: List[Dict[str, Any]] = []
    for rule in rules_payload.get("rules", []):
        if not _artifact_kind_matches(str(rule.get("artifact_kind") or ""), artifact_path):
            continue
        match_all: Sequence[str] = rule.get("match_all") or []
        if not all(pattern_matches(payload, pattern) for pattern in match_all):
            continue
        generated_hint = dict(rule.get("generated_hint") or {})
        generated_hint["artifact_path"] = str(artifact_path)
        generated_hint["matched_rule_id"] = rule.get("rule_id")
        generated_hint["hint_source_fields"] = [
            pattern.replace(" exists", "").split("=", 1)[0] for pattern in match_all
        ]
        generated_hint["hint_reason"] = [
            f"matched {pattern}" for pattern in match_all
        ]
        candidates.append(generated_hint)
    return candidates


def save_hint_candidate(
    hints_manifest_path: Path,
    hint_candidate: Dict[str, Any],
) -> Dict[str, Any]:
    if hints_manifest_path.exists():
        manifest = load_json(hints_manifest_path)
    else:
        manifest = {
            "schema_version": "source_to_family_hints_v0",
            "updated_at": "",
            "hints": [],
        }

    hints = list(manifest.get("hints") or [])
    artifact_path = str(hint_candidate.get("artifact_path") or "")
    replaced = False
    for index, existing in enumerate(hints):
        if str(existing.get("artifact_path") or "") == artifact_path:
            hints[index] = hint_candidate
            replaced = True
            break
    if not replaced:
        hints.append(hint_candidate)

    manifest["schema_version"] = "source_to_family_hints_v0"
    manifest["updated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    manifest["hints"] = hints
    hints_manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "artifact_path": artifact_path,
        "saved": True,
        "replaced_existing": replaced,
        "hint_count": len(hints),
        "manifest_path": str(hints_manifest_path),
    }
