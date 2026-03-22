from __future__ import annotations

from collections import Counter
from typing import Dict, List, Sequence, Tuple


MAX_DOMAIN_TERM_ANCHOR_FREQ = 12
MAX_FILE_ANCHOR_FREQ = 10
STRONG_ANCHOR_TYPES = {"tool", "code_symbol", "error", "project", "file"}


def normalize_anchor_list(raw_anchors: Sequence[object]) -> List[Dict[str, str]]:
    anchors: List[Dict[str, str]] = []
    for anchor in raw_anchors:
        if isinstance(anchor, dict):
            anchor_type = str(anchor.get("type", "")).strip()
            anchor_value = str(anchor.get("value", "")).strip()
        else:
            anchor_type = str(getattr(anchor, "type", "")).strip()
            anchor_value = str(getattr(anchor, "value", "")).strip()
        if not anchor_type or not anchor_value:
            continue
        anchors.append({"type": anchor_type, "value": anchor_value})
    return anchors


def anchor_is_candidate(anchor: Dict[str, str], anchor_frequency: Counter) -> bool:
    anchor_type = anchor["type"]
    count = anchor_frequency[(anchor_type, anchor["value"])]
    if anchor_type == "domain_term":
        return 1 < count <= MAX_DOMAIN_TERM_ANCHOR_FREQ
    if anchor_type == "file":
        return count <= MAX_FILE_ANCHOR_FREQ
    return anchor_type in STRONG_ANCHOR_TYPES


def build_relation_profile(left: Dict[str, object], right: Dict[str, object]) -> Dict[str, object]:
    shared_anchors = [
        anchor
        for anchor in left.get("candidate_anchors", left["anchors"])
        if any(
            anchor["type"] == other["type"] and anchor["value"] == other["value"]
            for other in right.get("candidate_anchors", right["anchors"])
        )
    ]
    anchor_score = min(1.0, 0.35 * len(shared_anchors))
    same_scene = left["scene"] == right["scene"]
    same_flow = left["flow"] == right["flow"]
    same_role = (
        bool(left.get("observer_role"))
        and bool(right.get("observer_role"))
        and str(left.get("observer_role")) == str(right.get("observer_role"))
    )
    scene_score = 1.0 if same_scene else 0.0
    flow_score = 1.0 if same_flow else 0.0
    role_score = 1.0 if same_role else 0.0
    direction_relation = direction_relation_for_values(float(left["D"]), float(right["D"]))
    time_score = 1.0 if same_day(str(left["time_in"]), str(right["time_in"])) else 0.4
    flow_conflict = 1.0 if flow_conflict_for_values(str(left["flow"]), str(right["flow"])) else 0.0
    direction_same_score = 1.0 if direction_relation == "same_pole" else 0.0
    direction_opposition_score = 1.0 if direction_relation == "opposed" else 0.0
    left_ambiguity = _observer_ambiguity(left)
    right_ambiguity = _observer_ambiguity(right)
    ambiguity_gap = abs(left_ambiguity - right_ambiguity)
    ambiguity_score = max(0.0, 1.0 - ambiguity_gap)
    return {
        "shared_anchors": shared_anchors,
        "anchor_score": anchor_score,
        "scene_score": scene_score,
        "flow_score": flow_score,
        "role_score": role_score,
        "ambiguity_score": ambiguity_score,
        "ambiguity_gap": ambiguity_gap,
        "direction_relation": direction_relation,
        "direction_same_score": direction_same_score,
        "direction_opposition_score": direction_opposition_score,
        "flow_conflict_score": flow_conflict,
        "time_score": time_score,
        "same_scene": same_scene,
        "same_flow": same_flow,
        "same_role": same_role,
    }


def edge_type_for_profile(profile: Dict[str, object]) -> Tuple[str | None, float]:
    direct_score = (
        0.35 * profile["anchor_score"]
        + 0.18 * profile["scene_score"]
        + 0.12 * profile["flow_score"]
        + 0.10 * profile["role_score"]
        + 0.10 * profile["direction_same_score"]
        + 0.10 * profile["time_score"]
        + 0.05 * profile["ambiguity_score"]
    )
    tension_score = (
        0.28 * profile["anchor_score"]
        + 0.22 * profile["scene_score"]
        + 0.18 * profile["direction_opposition_score"]
        + 0.12 * profile["flow_conflict_score"]
        + 0.10 * profile["time_score"]
        + 0.05 * profile["role_score"]
        + 0.05 * profile["ambiguity_score"]
    )
    weak_score = max(
        direct_score,
        tension_score,
        0.32 * profile["anchor_score"]
        + 0.22 * profile["scene_score"]
        + 0.18 * profile["flow_score"]
        + 0.10 * profile["role_score"]
        + 0.08 * profile["ambiguity_score"],
    )

    if direct_score >= 0.60:
        return "direct", direct_score
    if tension_score >= 0.55:
        return "tension", tension_score
    if weak_score >= 0.35:
        return "weak", weak_score
    return None, 0.0


def edge_reasons_for_profile(profile: Dict[str, object]) -> Dict[str, str]:
    return {
        "anchor_reason": anchor_reason(profile),
        "scene_reason": scene_reason(profile),
        "flow_reason": flow_reason(profile),
        "role_reason": role_reason(profile),
        "ambiguity_reason": ambiguity_reason(profile),
        "direction_reason": direction_reason(profile),
        "time_reason": time_reason(profile),
    }


def event_type_for_edge(edge_type: str) -> str:
    if edge_type == "tension":
        return "tension_detected"
    if edge_type == "weak":
        return "weaken"
    return "attach"


def direction_relation_for_values(left: float, right: float) -> str:
    if (left < 0.4 and right > 0.6) or (left > 0.6 and right < 0.4):
        return "opposed"
    if (left < 0.4 and right < 0.4) or (0.4 <= left <= 0.6 and 0.4 <= right <= 0.6) or (left > 0.6 and right > 0.6):
        return "same_pole"
    return "adjacent"


def flow_conflict_for_values(left_flow: str, right_flow: str) -> bool:
    return {left_flow, right_flow} in ({"run", "break"}, {"break", "fix"}, {"run", "compare"})


def same_day(left: str, right: str) -> bool:
    return left[:10] == right[:10]


def edge_color(edge_type: str) -> str:
    return {"direct": "#2563eb", "weak": "#94a3b8", "tension": "#b91c1c"}[edge_type]


def anchor_reason(profile: Dict[str, object]) -> str:
    shared = profile["shared_anchors"]
    if not shared:
        return "shared anchor 없음"
    first = shared[0]
    return "shared %s:%s" % (first["type"], first["value"])


def scene_reason(profile: Dict[str, object]) -> str:
    return "same scene" if profile["same_scene"] else "scene mismatch"


def flow_reason(profile: Dict[str, object]) -> str:
    if profile["same_flow"]:
        return "same flow"
    if profile["flow_conflict_score"] > 0:
        return "flow conflict"
    return "flow partial"


def role_reason(profile: Dict[str, object]) -> str:
    return "same observer_role" if profile["same_role"] else "observer_role mismatch"


def ambiguity_reason(profile: Dict[str, object]) -> str:
    gap = float(profile["ambiguity_gap"])
    if gap <= 0.15:
        return "observer ambiguity near"
    if gap <= 0.35:
        return "observer ambiguity partial"
    return "observer ambiguity far"


def direction_reason(profile: Dict[str, object]) -> str:
    return str(profile["direction_relation"])


def time_reason(profile: Dict[str, object]) -> str:
    return "same recent window" if profile["time_score"] >= 1.0 else "loose time proximity"


def _observer_ambiguity(node: Dict[str, object]) -> float:
    raw = node.get("observer_ambiguity", 0.5)
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return 0.5
    return max(0.0, min(1.0, value))
