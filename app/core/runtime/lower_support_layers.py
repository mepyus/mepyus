from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROLE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "definition": (
        "definition",
        "define",
        "means",
        "purpose",
        "scope",
        "what this is",
        "정의",
        "의미",
        "목적",
    ),
    "background": (
        "background",
        "context",
        "source identity",
        "input info",
        "profile",
        "origin",
        "배경",
        "맥락",
        "입력 정보",
    ),
    "main_claim": (
        "main gap",
        "missing",
        "need",
        "must",
        "core",
        "dominant gap",
        "핵심",
        "부족",
        "필요",
        "주요",
    ),
    "transition": (
        "next",
        "then",
        "after",
        "before",
        "proceed",
        "다음",
        "이후",
        "전환",
        "단계",
    ),
    "correction": (
        "instead",
        "rather",
        "correction",
        "fix",
        "보정",
        "수정",
        "바로잡",
    ),
    "objection": (
        "however",
        "but ",
        "risk",
        "problem",
        "issue",
        "objection",
        "한계",
        "문제",
        "리스크",
    ),
    "example": ("example", "for example", "예시", "사례"),
    "exception": ("except", "unless", "예외", "단,"),
    "connective": (
        "bridge",
        "link",
        "connect",
        "mapping",
        "handoff",
        "연결",
        "매핑",
        "bridge minimum",
    ),
    "axis_support_candidate": (
        "axis",
        "camera",
        "lens",
        "corridor",
        "arrival axis",
        "line seed",
        "축",
        "카메라",
        "렌즈",
        "라인",
    ),
}

SEED_DRIVER_ROLES = {
    "main_claim",
    "correction",
    "objection",
    "connective",
    "axis_support_candidate",
}

CHANGE_CUES = (
    "change",
    "changed",
    "shift",
    "move",
    "moved",
    "recast",
    "re-read",
    "scope",
    "revision",
    "delta",
    "regroup",
    "reduced",
    "moved down",
    "바뀌",
    "변화",
    "전환",
    "재정리",
)

BOUNDARY_CUES = (
    "hold",
    "not yet",
    "evidence_only",
    "thin",
    "weak",
    "unknown",
    "risk",
    "unclear",
    "spec-first",
    "light patch",
    "caution",
    "missing",
    "보류",
    "아직",
    "얇",
    "약",
    "주의",
    "부족",
    "still not",
    "should still be checked",
    "not direct-ingest-safe",
    "before mutation",
    "before any real ingest",
    "too strong",
    "too flat",
)

FLOW_CUES = (
    "sequence",
    "layer position",
    "handoff",
    "carry-forward",
    "carry forward",
    "between",
    "between-layer",
    "between layer",
    "insertion",
    "position",
    "chain",
    "순서",
    "레이어",
    "연결",
    "handoff chain",
)


def _normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def _tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_-]{2,}|[가-힣]{2,}", text.lower())
    return [
        token
        for token in tokens
        if token
        not in {
            "this",
            "that",
            "with",
            "from",
            "into",
            "then",
            "there",
            "input",
            "source",
            "path",
            "line",
            "note",
            "report",
            "stage",
            "bridge",
            "lower",
            "upper",
            "artifact",
            "bundle",
        }
    ]


def _score_roles(text: str) -> dict[str, int]:
    lowered = text.lower()
    scores: dict[str, int] = {}
    for role, keywords in ROLE_KEYWORDS.items():
        scores[role] = sum(1 for keyword in keywords if keyword.lower() in lowered)
    if "not " in lowered and " but " in lowered:
        scores["correction"] += 1
    if any(marker in lowered for marker in ("why ", "how ", "무엇", "왜 ", "어떻게")):
        scores["main_claim"] += 1
    return scores


def infer_content_role(
    text: str,
    *,
    ref_hint: str = "",
    source_ref: str = "",
) -> dict[str, Any]:
    normalized = _normalize_text(" ".join(part for part in [ref_hint, text] if part))
    scores = _score_roles(normalized)
    ranked = sorted(scores.items(), key=lambda item: (item[1], item[0]), reverse=True)
    top_role, top_score = ranked[0]
    second_role, second_score = ranked[1]

    if top_score <= 0:
        return {
            "content_role": "unknown",
            "secondary_role": "",
            "role_confidence": "low",
            "role_status": "weak",
            "role_basis_note": "No bounded lexical role signal was strong enough.",
            "why_this_role": "The chunk is still readable, but role should remain honest and weak.",
            "source_ref": source_ref,
        }

    mixed = second_score > 0 and top_score == second_score
    role_confidence = "high" if top_score >= 3 and not mixed else "medium"
    role_status = "mixed" if mixed else "bounded"
    content_role = top_role
    secondary_role = second_role if mixed or second_score > 0 else ""

    why = {
        "definition": "The chunk defines scope, purpose, or meaning-bearing terms.",
        "background": "The chunk situates source context or provenance-adjacent explanation.",
        "main_claim": "The chunk pushes a dominant gap, need, or claim-like pressure.",
        "transition": "The chunk moves the reader into a next stage or adjacent step.",
        "correction": "The chunk corrects, narrows, or redirects a prior reading.",
        "objection": "The chunk carries risk, limit, or pushback pressure.",
        "example": "The chunk exemplifies a broader point with a bounded case.",
        "exception": "The chunk limits the rule with an exception-style condition.",
        "connective": "The chunk links surfaces, routes, or handoff meaning across blocks.",
        "axis_support_candidate": "The chunk contains directional language but not enough support for promotion.",
    }.get(content_role, "The chunk carries a bounded local role.")

    return {
        "content_role": content_role,
        "secondary_role": secondary_role,
        "role_confidence": role_confidence,
        "role_status": role_status,
        "role_basis_note": f"Keyword-weighted lower role inference from local text and ref hint. top={top_role}:{top_score}",
        "why_this_role": why,
        "source_ref": source_ref,
    }


def build_content_role_tags_for_split_units(
    source_ref: str,
    split_units: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for unit in split_units:
        inferred = infer_content_role(
            unit.get("text_excerpt", ""),
            ref_hint=f"{unit.get('start_ref', '')} {unit.get('end_ref', '')}",
            source_ref=source_ref,
        )
        rows.append(
            {
                "tag_id": f"role_{unit['unit_id']}",
                "source_ref": source_ref,
                "split_unit_ref": unit["unit_id"],
                "content_role": inferred["content_role"],
                "secondary_role": inferred["secondary_role"],
                "role_confidence": inferred["role_confidence"],
                "role_status": inferred["role_status"],
                "role_basis_note": inferred["role_basis_note"],
                "why_this_role": inferred["why_this_role"],
                "char_count": unit.get("char_count", 0),
                "excerpt_preview": unit.get("text_excerpt", "")[:160],
            }
        )
    return rows


def _dominant_tokens(texts: list[str]) -> list[str]:
    counter = Counter()
    for text in texts:
        counter.update(_tokenize(text))
    repeated = [token for token, count in counter.most_common(5) if count >= 2]
    return repeated[:3]


def _seed_question(roles: list[str]) -> str:
    if "correction" in roles:
        return "What misunderstanding is this local material trying to correct?"
    if "objection" in roles:
        return "What risk or resistance should later upper reading keep visible?"
    if "axis_support_candidate" in roles:
        return "Which later source keeps the same directional pull without promoting it yet?"
    return "What repeated local pressure makes these adjacent units worth rereading together?"


def _count_cues(texts: list[str], cues: tuple[str, ...]) -> list[str]:
    lowered = " ".join(texts).lower()
    return [cue for cue in cues if cue.lower() in lowered]


def _match_change_cues(texts: list[str]) -> list[str]:
    lowered = " ".join(texts).lower()
    matched: list[str] = []
    has_before = "before" in lowered or "이전" in lowered or "전 " in lowered
    has_after = "after" in lowered or "이후" in lowered or "후 " in lowered
    if has_before and has_after:
        matched.append("before_after_pair")
    matched.extend(_count_cues(texts, CHANGE_CUES))
    return list(dict.fromkeys(matched))


def _match_boundary_cues(texts: list[str]) -> list[str]:
    matched = _count_cues(texts, BOUNDARY_CUES)
    return list(dict.fromkeys(matched))


def _match_flow_cues(texts: list[str]) -> list[str]:
    lowered = " ".join(texts).lower()
    matched = _count_cues(texts, FLOW_CUES)
    if "between" in lowered and "layer" in lowered and "between-layer" not in matched:
        matched.append("between-layer")
    if "next checkpoint" in lowered:
        matched.append("next_checkpoint")
    if "support chain" in lowered or "bounded support chain" in lowered:
        matched.append("support_chain")
    return list(dict.fromkeys(matched))


def _slot(
    strength: str,
    summary: str,
    matched_cues: list[str],
    support_refs: list[str],
) -> dict[str, Any]:
    return {
        "strength": strength,
        "summary": summary,
        "matched_cues": matched_cues[:4],
        "support_refs": support_refs,
    }


def _bounded_summary(kind: str, strength: str) -> str:
    summaries = {
        "change": {
            "has_signal": "Local shift or before-after support is visible.",
            "thin": "Change-like support is present but thin.",
            "unclear": "Change-like support is mixed and still unclear.",
            "insufficient": "Change-like support is insufficient.",
        },
        "boundary": {
            "has_signal": "Hold or thinness support is visible.",
            "thin": "Boundary-like support is present but thin.",
            "unclear": "Boundary-like support is mixed and still unclear.",
            "insufficient": "Boundary-like support is insufficient.",
        },
        "flow": {
            "has_signal": "Sequence or handoff support is visible.",
            "thin": "Flow-like support is present but thin.",
            "unclear": "Flow-like support is mixed and still unclear.",
            "insufficient": "Flow-like support is insufficient.",
        },
    }
    return summaries[kind][strength]


def _camera_strength(
    *,
    matched_cues: list[str],
    roles: list[str],
    preferred_roles: set[str],
    text_count: int,
    cue_hits_for_signal: int = 2,
    require_role_for_single_cue_signal: bool = True,
    allow_role_only_thin: bool = False,
) -> str:
    role_hits = len([role for role in roles if role in preferred_roles])
    cue_hits = len(matched_cues)
    if cue_hits >= cue_hits_for_signal:
        return "has_signal"
    if cue_hits >= 1 and role_hits >= 1 and require_role_for_single_cue_signal:
        return "has_signal"
    if cue_hits >= 1 and not require_role_for_single_cue_signal:
        return "has_signal"
    if cue_hits == 1:
        return "thin"
    if allow_role_only_thin and role_hits >= 1:
        return "thin"
    if text_count > 0 and roles:
        return "insufficient"
    return "insufficient"


def _camera_summary(change_strength: str, boundary_strength: str, flow_strength: str) -> str:
    visible = [
        name
        for name, strength in (
            ("change", change_strength),
            ("boundary", boundary_strength),
            ("flow", flow_strength),
        )
        if strength in {"has_signal", "thin", "unclear"}
    ]
    if visible:
        return f"Lower support suggests {' + '.join(visible)} reread potential."
    return "Lower support remains too thin for camera-oriented reread beyond traceable context."


def _gap_summary(change_strength: str, boundary_strength: str, flow_strength: str) -> str:
    if all(strength == "insufficient" for strength in (change_strength, boundary_strength, flow_strength)):
        return "Support remains sparse; keep this as local traceable context only."
    if "thin" in {change_strength, boundary_strength, flow_strength}:
        return "At least one signal is thin; broader reread is still needed before stronger use."
    return "Signals are local and still need broader reread before any stronger organization."


def build_camera_support_bundles_for_split_units(
    source_ref: str,
    split_units: list[dict[str, Any]],
    role_tags: list[dict[str, Any]],
    line_seed_bundles: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    role_by_ref = {row["split_unit_ref"]: row for row in role_tags}
    unit_by_ref = {unit["unit_id"]: unit for unit in split_units}
    bundles: list[dict[str, Any]] = []

    seed_rows = line_seed_bundles or [
        {
            "bundle_id": "line_seed_fallback_001",
            "split_unit_refs": [unit["unit_id"] for unit in split_units[:2]],
            "provisional_role_mix": [
                role_by_ref[unit["unit_id"]]["content_role"]
                for unit in split_units[:2]
                if unit["unit_id"] in role_by_ref
            ],
            "repeated_pressure_note": "",
            "linkage_hint": "",
        }
    ]

    for index, seed in enumerate(seed_rows, start=1):
        refs = [ref for ref in seed.get("split_unit_refs", []) if ref in unit_by_ref]
        texts = [unit_by_ref[ref].get("text_excerpt", "") for ref in refs]
        roles = [
            role_by_ref.get(ref, {}).get("content_role", "unknown")
            for ref in refs
        ]
        seed_text = " ".join(
            [
                str(seed.get("repeated_pressure_note", "")),
                str(seed.get("linkage_hint", "")),
                str(seed.get("question_inducement", "")),
                str(seed.get("misunderstanding_correction", "")),
                str(seed.get("tension_marker", "")),
            ]
        ).strip()
        combined_texts = texts + ([seed_text] if seed_text else [])

        change_cues = _match_change_cues(combined_texts)
        boundary_cues = _match_boundary_cues(combined_texts)
        flow_cues = _match_flow_cues(combined_texts)

        change_strength = _camera_strength(
            matched_cues=change_cues,
            roles=roles,
            preferred_roles={"correction", "main_claim"},
            text_count=len(combined_texts),
            cue_hits_for_signal=1,
        )
        boundary_strength = _camera_strength(
            matched_cues=boundary_cues,
            roles=roles,
            preferred_roles={"objection"},
            text_count=len(combined_texts),
            cue_hits_for_signal=2,
        )
        flow_strength = _camera_strength(
            matched_cues=flow_cues,
            roles=roles,
            preferred_roles={"transition", "connective"},
            text_count=len(combined_texts),
            cue_hits_for_signal=2,
        )

        bundles.append(
            {
                "camera_support_id": f"camera_support_{index:03d}",
                "artifact_id": f"camera_support_{index:03d}",
                "source_ref": source_ref,
                "source_unit_refs": refs,
                "upstream_artifact_refs": [seed.get("bundle_id", "")] if seed.get("bundle_id") else [],
                "classification": "evidence_only",
                "camera_signal_summary": _camera_summary(change_strength, boundary_strength, flow_strength),
                "change_support": _slot(
                    change_strength,
                    _bounded_summary("change", change_strength),
                    change_cues,
                    refs,
                ),
                "boundary_support": _slot(
                    boundary_strength,
                    _bounded_summary("boundary", boundary_strength),
                    boundary_cues,
                    refs,
                ),
                "flow_support": _slot(
                    flow_strength,
                    _bounded_summary("flow", flow_strength),
                    flow_cues,
                    refs,
                ),
                "insufficiency_or_gap": _gap_summary(change_strength, boundary_strength, flow_strength),
                "carry_forward_handle": {
                    "reread_hint": "Use the upstream seed and source units for bounded upper reread.",
                    "upstream_seed_ref": seed.get("bundle_id", ""),
                    "source_unit_refs": refs,
                },
            }
        )
    return bundles


def build_line_seed_bundles_for_split_units(
    source_ref: str,
    split_units: list[dict[str, Any]],
    role_tags: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    bundles: list[dict[str, Any]] = []
    role_by_ref = {row["split_unit_ref"]: row for row in role_tags}
    for index in range(len(split_units) - 1):
        window = split_units[index : index + 2]
        if len(window) < 2:
            continue
        roles = [role_by_ref[unit["unit_id"]]["content_role"] for unit in window]
        non_unknown = [role for role in roles if role != "unknown"]
        if not any(role in SEED_DRIVER_ROLES for role in non_unknown):
            continue
        texts = [unit.get("text_excerpt", "") for unit in window]
        repeated = _dominant_tokens(texts)
        if not repeated and len(non_unknown) < 2:
            continue
        bundle_id = f"line_seed_{index + 1:03d}"
        correction_present = any(role == "correction" for role in roles)
        objection_present = any(role == "objection" for role in roles)
        axis_present = any(role == "axis_support_candidate" for role in roles)
        bundles.append(
            {
                "bundle_id": bundle_id,
                "source_ref": source_ref,
                "split_unit_refs": [unit["unit_id"] for unit in window],
                "repeated_pressure_note": (
                    f"Repeated local pressure around: {', '.join(repeated)}."
                    if repeated
                    else "Adjacent units keep a local claim/connective pressure alive."
                ),
                "linkage_hint": "Adjacent split units share local role pressure and should be reread together before upper evidence use.",
                "question_inducement": _seed_question(roles),
                "misunderstanding_correction": (
                    "A correction-like move is present across the bundle."
                    if correction_present
                    else ""
                ),
                "tension_marker": (
                    "Objection or risk pressure remains active in the bundle."
                    if objection_present
                    else ("Directional pull is visible but still locally bounded." if axis_present else "")
                ),
                "provisional_role_mix": non_unknown or ["unknown"],
                "why_line_seed": "The bundle preserves repeated pressure or connective movement that would harden too early if each unit were used alone.",
                "not_yet_axis_reason": "This bundle is source-local support only and lacks broader cross-source validation for axis promotion.",
                "seed_confidence": "medium" if repeated or len(set(non_unknown)) > 1 else "low",
            }
        )
    return bundles


def _preprocess_components(payload: dict[str, Any]) -> list[dict[str, str]]:
    comparison = payload.get("comparison", {})
    check_surface = comparison.get("check_surface", {})
    rows = [
        {
            "component_ref": "before_gate.decision_reason",
            "text": str(payload.get("before_gate", {}).get("decision_reason", "")),
        },
        {
            "component_ref": "after_gate.decision_reason",
            "text": str(payload.get("after_gate", {}).get("decision_reason", "")),
        },
        {
            "component_ref": "comparison.readiness_read.reason",
            "text": str(comparison.get("readiness_read", {}).get("reason", "")),
        },
        {
            "component_ref": "comparison.check_surface.what_improved",
            "text": " ".join(check_surface.get("what_improved", []) or []),
        },
        {
            "component_ref": "comparison.check_surface.what_is_still_missing",
            "text": " ".join(check_surface.get("what_is_still_missing", []) or []),
        },
        {
            "component_ref": "comparison.check_surface.next_checkpoint",
            "text": str(check_surface.get("next_checkpoint", "")),
        },
    ]
    return [row for row in rows if row["text"].strip()]


def build_support_layers_for_preprocess_comparison(
    payload: dict[str, Any],
) -> dict[str, Any]:
    source_ref = str(payload.get("input_path", ""))
    components = _preprocess_components(payload)
    role_tags: list[dict[str, Any]] = []
    for row in components:
        inferred = infer_content_role(row["text"], ref_hint=row["component_ref"], source_ref=source_ref)
        role_tags.append(
            {
                "tag_id": f"role_{row['component_ref'].replace('.', '_').replace('[', '_').replace(']', '')}",
                "source_ref": source_ref,
                "split_unit_ref": row["component_ref"],
                "content_role": inferred["content_role"],
                "secondary_role": inferred["secondary_role"],
                "role_confidence": inferred["role_confidence"],
                "role_status": inferred["role_status"],
                "role_basis_note": inferred["role_basis_note"],
                "why_this_role": inferred["why_this_role"],
                "excerpt_preview": row["text"][:160],
            }
        )

    bundles: list[dict[str, Any]] = []
    if components:
        texts = [row["text"] for row in components]
        roles = [row["content_role"] for row in role_tags if row["content_role"] != "unknown"]
        bundles.append(
            {
                "bundle_id": "line_seed_preprocess_001",
                "source_ref": source_ref,
                "split_unit_refs": [row["component_ref"] for row in components[:4]],
                "repeated_pressure_note": (
                    f"Preprocess comparison keeps returning: {', '.join(_dominant_tokens(texts))}."
                    if _dominant_tokens(texts)
                    else "The artifact repeatedly contrasts raw fragmentation with regrouped meaning support."
                ),
                "linkage_hint": "Gate reason, readiness read, and next checkpoint form one bounded support chain.",
                "question_inducement": "What local meaning pressure survives regroup strongly enough to support later evidence use?",
                "misunderstanding_correction": "The comparison is explicitly correcting a too-flat direct-ingest reading.",
                "tension_marker": "The artifact keeps the risk of over-flat ingest visible even after regroup.",
                "provisional_role_mix": roles or ["unknown"],
                "why_line_seed": "This comparison carries repeated correction pressure and a next-step question before any packet use.",
                "not_yet_axis_reason": "Preprocess comparison remains a lower support artifact and does not justify axis or packet promotion by itself.",
                "seed_confidence": "medium",
            }
        )

    camera_support_bundles: list[dict[str, Any]] = []
    texts = [row["text"] for row in components]
    roles = [row["content_role"] for row in role_tags if row["content_role"] != "unknown"]
    if components:
        change_cues = _match_change_cues(texts)
        boundary_cues = _match_boundary_cues(texts)
        flow_cues = _match_flow_cues(texts)
        change_strength = _camera_strength(
            matched_cues=change_cues,
            roles=roles,
            preferred_roles={"correction", "main_claim"},
            text_count=len(texts),
            cue_hits_for_signal=1,
        )
        boundary_strength = _camera_strength(
            matched_cues=boundary_cues,
            roles=roles,
            preferred_roles={"objection"},
            text_count=len(texts),
            cue_hits_for_signal=2,
        )
        flow_strength = _camera_strength(
            matched_cues=flow_cues,
            roles=roles,
            preferred_roles={"transition", "connective"},
            text_count=len(texts),
            cue_hits_for_signal=2,
        )
        camera_support_bundles.append(
            {
                "camera_support_id": "camera_support_preprocess_001",
                "artifact_id": "camera_support_preprocess_001",
                "source_ref": source_ref,
                "source_unit_refs": [row["component_ref"] for row in components[:4]],
                "upstream_artifact_refs": [bundles[0]["bundle_id"]] if bundles else [],
                "classification": "evidence_only",
                "camera_signal_summary": _camera_summary(change_strength, boundary_strength, flow_strength),
                "change_support": _slot(
                    change_strength,
                    _bounded_summary("change", change_strength),
                    change_cues,
                    [row["component_ref"] for row in components[:4]],
                ),
                "boundary_support": _slot(
                    boundary_strength,
                    _bounded_summary("boundary", boundary_strength),
                    boundary_cues,
                    [row["component_ref"] for row in components[:4]],
                ),
                "flow_support": _slot(
                    flow_strength,
                    _bounded_summary("flow", flow_strength),
                    flow_cues,
                    [row["component_ref"] for row in components[:4]],
                ),
                "insufficiency_or_gap": _gap_summary(change_strength, boundary_strength, flow_strength),
                "carry_forward_handle": {
                    "reread_hint": "Use gate reason, readiness read, and seed support for bounded upper reread.",
                    "upstream_seed_ref": bundles[0]["bundle_id"] if bundles else "",
                    "source_unit_refs": [row["component_ref"] for row in components[:4]],
                },
            }
        )

    return {
        "content_role_tags": role_tags,
        "line_seed_bundles": bundles,
        "camera_support_bundles": camera_support_bundles,
        "support_layer_note": "These support layers are additive and do not change lower readiness or upper admission.",
    }


def write_support_payload(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
