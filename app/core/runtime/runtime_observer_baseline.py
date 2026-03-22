from __future__ import annotations

from typing import Dict, List

from app.work.processor_compare.observer_engine import run_internal_observers


def build_material_observer_baseline(text: str, *, generation_path: str) -> Dict[str, object]:
    observer_payload = run_internal_observers(text)
    profiles = {
        "codex_like": dict(observer_payload.get("codex_like", {}) or {}),
        "chatgpt_like": dict(observer_payload.get("chatgpt_like", {}) or {}),
        "gemini_like": dict(observer_payload.get("gemini_like", {}) or {}),
    }
    merged = dict(observer_payload.get("merged", {}) or {})
    scene_map = {
        name: str(payload.get("scene", "")).strip()
        for name, payload in profiles.items()
        if str(payload.get("scene", "")).strip()
    }
    role_map = {
        name: str(payload.get("role", "")).strip()
        for name, payload in profiles.items()
        if str(payload.get("role", "")).strip()
    }
    items: List[Dict[str, object]] = []
    if len(set(scene_map.values())) > 1:
        items.append(
            {
                "kind": "scene",
                "profiles": scene_map,
                "summary": "scene disagreement: " + " / ".join(f"{k}={v}" for k, v in scene_map.items()),
            }
        )
    if len(set(role_map.values())) > 1:
        items.append(
            {
                "kind": "role",
                "profiles": role_map,
                "summary": "role disagreement: " + " / ".join(f"{k}={v}" for k, v in role_map.items()),
            }
        )
    return {
        "available": True,
        "generation_path": generation_path,
        "profiles": profiles,
        "items": items,
        "merged": {
            "scene": merged.get("scene", ""),
            "role": merged.get("role", ""),
            "ambiguity": merged.get("ambiguity"),
            "confidence": merged.get("confidence"),
            "signals": list(merged.get("signals", []) or []),
            "direction": merged.get("direction"),
            "intensity": merged.get("intensity"),
            "stability": merged.get("stability"),
        },
        "unavailable_reason": "",
        "note": "runtime internal observer baseline",
    }


def apply_observer_baseline_to_metadata(metadata: Dict[str, object], trace: Dict[str, object]) -> Dict[str, object]:
    merged = dict(trace.get("merged", {}) or {})
    metadata["observer_or_ambiguity_trace"] = trace
    metadata["observer_role"] = merged.get("role", "")
    metadata["observer_ambiguity"] = merged.get("ambiguity")
    metadata["observer_confidence_numeric"] = merged.get("confidence")
    metadata["observer_signals"] = list(merged.get("signals", []) or [])
    return metadata
