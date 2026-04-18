from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


READING_RESULT = "reading_result"
CAPABILITY_RESULT = "capability_result"
WINDOWED_READING_LIMIT = 8
WINDOWED_CAPABILITY_LIMIT = 6


def search_internal_assets(
    runtime_root: Path | str,
    *,
    query: str,
    reading_limit: int = WINDOWED_READING_LIMIT,
    capability_limit: int = WINDOWED_CAPABILITY_LIMIT,
) -> List[Dict[str, Any]]:
    runtime_root = Path(runtime_root)
    query = str(query or "").strip()
    if not query:
        return []

    reading_results = _search_reading_candidates(runtime_root, query=query, limit=reading_limit)
    capability_results = _search_capability_candidates(runtime_root, query=query, limit=capability_limit)
    return reading_results + capability_results


def build_internal_search_panel_payload(
    runtime_root: Path | str,
    *,
    query: str,
    selected_candidate_id: Optional[str] = None,
    reading_limit: int = WINDOWED_READING_LIMIT,
    capability_limit: int = WINDOWED_CAPABILITY_LIMIT,
) -> Dict[str, Any]:
    results = search_internal_assets(
        runtime_root,
        query=query,
        reading_limit=reading_limit,
        capability_limit=capability_limit,
    )
    selected = _resolve_selected_result(results, selected_candidate_id)
    summary = _build_path_diversity_summary(results)
    return {
        "query": query,
        "results": results,
        "selectedCandidateId": selected.get("candidate_id") if selected else None,
        "selectedResult": selected,
        "summary": summary,
    }


def _search_reading_candidates(runtime_root: Path, *, query: str, limit: int) -> List[Dict[str, Any]]:
    registry_by_line = _load_line_registry_by_name(runtime_root)
    scored: List[Tuple[int, Dict[str, Any]]] = []
    seen_ids: set[str] = set()

    for row in _iter_observation_rows(runtime_root):
        candidate = _build_reading_result(query=query, row=row, registry_by_line=registry_by_line)
        if candidate is None:
            continue
        candidate_id = str(candidate.get("candidate_id") or "")
        if not candidate_id or candidate_id in seen_ids:
            continue
        seen_ids.add(candidate_id)
        scored.append((int(candidate.pop("_score", 0)), candidate))

    scored.sort(
        key=lambda item: (
            -item[0],
            _evidence_rank(item[1].get("evidence_kind")),
            item[1].get("title") or "",
        )
    )
    return [item[1] for item in scored[:limit]]


def _search_capability_candidates(runtime_root: Path, *, query: str, limit: int) -> List[Dict[str, Any]]:
    registry = _load_json(runtime_root / "manifests" / "executable_capability_registry_v0.json")
    capabilities = registry.get("capabilities") if isinstance(registry, dict) else []
    scored: List[Tuple[int, Dict[str, Any]]] = []

    for capability in capabilities if isinstance(capabilities, list) else []:
        if not isinstance(capability, dict):
            continue
        candidate = _build_capability_result(query=query, capability=capability)
        if candidate is None:
            continue
        scored.append((int(candidate.pop("_score", 0)), candidate))

    scored.sort(key=lambda item: (-item[0], item[1].get("title") or ""))
    return [item[1] for item in scored[:limit]]


def _build_reading_result(
    *,
    query: str,
    row: Dict[str, Any],
    registry_by_line: Dict[str, Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    haystack_parts = [
        row.get("line_name"),
        row.get("evidence"),
        row.get("source_path_or_ref"),
        row.get("source_pointer"),
        " ".join(_string_list(row.get("support_points"))),
        " ".join(_string_list(row.get("weakness_points"))),
        " ".join(_string_list(row.get("contradiction_points"))),
        " ".join(_string_list(row.get("caution_points"))),
        " ".join(_string_list(row.get("resistance_or_counterexample"))),
    ]
    score = _match_score(query, haystack_parts)
    if score <= 0:
        return None

    pointer_info = _extract_pointer_info(row)
    line_name = _clean_text(row.get("line_name"))
    line_state = registry_by_line.get(line_name or "", {})
    matched_preview = _matched_preview(query=query, text=_clean_text(row.get("evidence")))
    surrounding_context = _build_surrounding_context_preview(row, pointer_info=pointer_info)
    evidence_kind = _normalize_evidence_kind(row.get("evidence_mode"))
    candidate_id = _build_reading_candidate_id(row, pointer_info)
    original_path_origin = _clean_text(row.get("validation_path_id")) or _clean_text(row.get("source_kind")) or "unknown_path"
    normalized_path = _normalize_path_origin(row=row, line_name=line_name, original_path_origin=original_path_origin)
    user_language = _build_user_language_interpretation(
        normalized_path_origin=normalized_path["normalized_path_origin"],
        path_diversity_eligible=normalized_path["path_diversity_eligible"],
        legacy_carryover_hint=normalized_path["legacy_carryover_hint"],
        validation_profile=_clean_text(line_state.get("validation_profile")),
        next_missing_axis=_clean_text(line_state.get("next_missing_axis")),
    )

    return {
        "query": query,
        "result_type": READING_RESULT,
        "candidate_id": candidate_id,
        "title": line_name or pointer_info.get("fragment_id") or "reading candidate",
        "why_selected": _build_reading_why_selected(query=query, row=row, path_origin=normalized_path["normalized_path_origin"]),
        "candidate_type": "line_observation",
        "line_name": line_name,
        "source_ref": _clean_text(row.get("source_path_or_ref")) or pointer_info.get("source_ref"),
        "fragment_id": pointer_info.get("fragment_id"),
        "source_range": pointer_info.get("source_range"),
        "paragraph_index": pointer_info.get("paragraph_index"),
        "evidence_kind": evidence_kind,
        "matched_text_preview": matched_preview,
        "surrounding_context_preview": surrounding_context,
        "validation_profile": line_state.get("validation_profile"),
        "primary_only_validation_profile": line_state.get("primary_only_validation_profile"),
        "support_ecology_bias": line_state.get("support_ecology_bias"),
        "next_missing_axis": line_state.get("next_missing_axis"),
        "path_signature": normalized_path["normalized_path_origin"],
        "path_origin": original_path_origin,
        "normalized_path_origin": normalized_path["normalized_path_origin"],
        "path_origin_classification_reason": normalized_path["path_origin_classification_reason"],
        "path_diversity_eligible": normalized_path["path_diversity_eligible"],
        "legacy_carryover_hint": normalized_path["legacy_carryover_hint"],
        "user_language_summary": user_language["user_language_summary"],
        "user_language_caution": user_language["user_language_caution"],
        "user_language_next_read": user_language["user_language_next_read"],
        "next_actions": _build_reading_next_actions(pointer_info=pointer_info, evidence_kind=evidence_kind),
        "_score": score,
    }


def _build_capability_result(*, query: str, capability: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    haystack_parts = [
        capability.get("capability_id"),
        capability.get("label"),
        " ".join(_string_list(capability.get("intent_aliases"))),
        " ".join(_string_list(capability.get("entrypoint_refs"))),
        " ".join(_string_list(capability.get("output_surfaces"))),
        capability.get("capability_class"),
    ]
    score = _match_score(query, haystack_parts)
    if score <= 0:
        return None

    safety_mode = _clean_text(capability.get("safety_mode")) or "unknown"
    runtime_scope = _runtime_scope_from_safety_mode(safety_mode)
    entrypoints = _string_list(capability.get("entrypoint_refs"))
    primary_refs = _string_list(capability.get("primary_impl_refs"))
    linked_scripts = _dedupe_strings(entrypoints + primary_refs)

    return {
        "query": query,
        "result_type": CAPABILITY_RESULT,
        "candidate_id": _clean_text(capability.get("capability_id")) or "capability",
        "title": _clean_text(capability.get("label")) or _clean_text(capability.get("capability_id")) or "capability",
        "why_selected": _build_capability_why_selected(query=query, capability=capability),
        "capability_type": _clean_text(capability.get("capability_class")) or "unknown",
        "intent_aliases": _string_list(capability.get("intent_aliases")),
        "entrypoint": entrypoints[0] if entrypoints else None,
        "linked_scripts": linked_scripts,
        "output_surfaces": _string_list(capability.get("output_surfaces")),
        "runtime_scope": runtime_scope,
        "capability_summary": _build_capability_summary(capability),
        "invocation_hint": _build_invocation_hint(entrypoints[0] if entrypoints else None, capability_type=_clean_text(capability.get("capability_class"))),
        "safety_note": _build_safety_note(safety_mode),
        "related_assets": primary_refs if primary_refs else None,
        "next_actions": _build_capability_next_actions(
            entrypoint=entrypoints[0] if entrypoints else None,
            runtime_scope=runtime_scope,
            output_surfaces=_string_list(capability.get("output_surfaces")),
        ),
        "_score": score,
    }


def _load_line_registry_by_name(runtime_root: Path) -> Dict[str, Dict[str, Any]]:
    payload = _load_json(runtime_root / "manifests" / "line_registry.json")
    lines = payload.get("lines") if isinstance(payload, dict) else []
    results: Dict[str, Dict[str, Any]] = {}
    for row in lines if isinstance(lines, list) else []:
        if not isinstance(row, dict):
            continue
        line_name = _clean_text(row.get("line_name"))
        if line_name:
            results[line_name] = row
    return results


def _iter_observation_rows(runtime_root: Path) -> Iterable[Dict[str, Any]]:
    path = runtime_root / "logs" / "reread_observation_log.jsonl"
    if not path.exists():
        return []
    rows: List[Dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for raw in handle:
            raw = raw.strip()
            if not raw:
                continue
            try:
                row = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict):
                rows.append(row)
    return rows


def _extract_pointer_info(row: Dict[str, Any]) -> Dict[str, Any]:
    source_pointer = _clean_text(row.get("source_pointer"))
    source_ref = _clean_text(row.get("source_path_or_ref"))
    fragment_id = _clean_text(row.get("fragment_id"))
    source_range = row.get("source_range")
    paragraph_index = row.get("paragraph_index")

    if source_pointer:
        match = re.search(r"/(frag_[^/#]+)\.json", source_pointer)
        if match and not fragment_id:
            fragment_id = match.group(1)

        range_match = re.search(r"source_range=(\d+)-(\d+)", source_pointer)
        if range_match and not source_range:
            source_range = {"start": int(range_match.group(1)), "end": int(range_match.group(2))}

        paragraph_match = re.search(r"paragraph_index=(\d+)", source_pointer)
        if paragraph_match and paragraph_index is None:
            paragraph_index = int(paragraph_match.group(1))

        page_match = re.search(r"page_ref=([^;#]+)", source_pointer)
        if page_match and not source_range:
            source_range = {"page_ref": page_match.group(1)}

    return {
        "fragment_id": fragment_id,
        "source_range": source_range,
        "paragraph_index": paragraph_index,
        "source_ref": source_ref,
        "source_pointer": source_pointer,
    }


def _build_surrounding_context_preview(row: Dict[str, Any], *, pointer_info: Dict[str, Any]) -> str:
    fragment_id = pointer_info.get("fragment_id")
    if fragment_id:
        fragment_path = Path("runtime/fragments") / f"{fragment_id}.json"
        if fragment_path.exists():
            fragment = _load_json(fragment_path)
            raw_text = _clean_text(fragment.get("raw_text"))
            if raw_text:
                return _truncate(raw_text, 320)
    evidence = _clean_text(row.get("evidence"))
    return _truncate(evidence, 320)


def _build_reading_why_selected(*, query: str, row: Dict[str, Any], path_origin: str) -> str:
    reasons = []
    line_name = _clean_text(row.get("line_name"))
    if _match_score(query, [line_name]) > 0:
        reasons.append(f"query matched line {line_name}")
    evidence = _clean_text(row.get("evidence"))
    if evidence and _match_score(query, [evidence]) > 0:
        reasons.append("query matched grounded evidence text")
    pointer = _clean_text(row.get("source_pointer"))
    if pointer and _match_score(query, [pointer]) > 0:
        reasons.append("query matched source pointer")
    reasons.append(f"path={path_origin}")
    return "; ".join(reasons[:3])


def _normalize_path_origin(*, row: Dict[str, Any], line_name: str, original_path_origin: str) -> Dict[str, Any]:
    evidence_kind = _normalize_evidence_kind(row.get("evidence_mode"))
    source_pointer = _clean_text(row.get("source_pointer"))
    source_kind = _clean_text(row.get("source_kind"))
    validation_path_id = _clean_text(row.get("validation_path_id"))
    fragment_source = _extract_fragment_source(row)

    if validation_path_id == "internal_observer":
        return {
            "normalized_path_origin": "observer_derived_path",
            "path_origin_classification_reason": "validation_path_id=internal_observer on observer-derived reread path",
            "path_diversity_eligible": True,
            "legacy_carryover_hint": None,
        }

    if validation_path_id:
        return {
            "normalized_path_origin": "true_primary_path",
            "path_origin_classification_reason": f"explicit validation_path_id={validation_path_id}",
            "path_diversity_eligible": True,
            "legacy_carryover_hint": None,
        }

    if (
        line_name == "input_to_reading_organ"
        and source_kind == "raw_surface"
        and evidence_kind in {"direct_span", "source_linked"}
        and fragment_source
    ):
        return {
            "normalized_path_origin": "legacy_raw_surface_carryover",
            "path_origin_classification_reason": (
                "legacy observation rows carry source_kind=raw_surface without explicit validation_path_id; "
                "do not count as a new path by themselves"
            ),
            "path_diversity_eligible": False,
            "legacy_carryover_hint": f"fragment_source={fragment_source}; pointer={source_pointer or 'n/a'}",
        }

    if source_kind in {"preflight_decision", "raw_surface"}:
        return {
            "normalized_path_origin": "unknown_or_mixed",
            "path_origin_classification_reason": f"source_kind={source_kind} without explicit path identity",
            "path_diversity_eligible": False,
            "legacy_carryover_hint": source_pointer or None,
        }

    return {
        "normalized_path_origin": "unknown_or_mixed",
        "path_origin_classification_reason": "insufficient path evidence for true path classification",
        "path_diversity_eligible": False,
        "legacy_carryover_hint": source_pointer or None,
    }


def _build_reading_candidate_id(row: Dict[str, Any], pointer_info: Dict[str, Any]) -> str:
    pointer = pointer_info.get("source_pointer")
    parts = [
        _clean_text(row.get("line_name")) or "line",
        pointer_info.get("fragment_id") or pointer or "nopointer",
        _normalize_evidence_kind(row.get("evidence_mode")),
    ]
    return "::".join(parts)


def _extract_fragment_source(row: Dict[str, Any]) -> str:
    for value in _string_list(row.get("support_points")):
        if value.startswith("fragment_source="):
            return value.split("=", 1)[1]
    return ""


def _build_user_language_interpretation(
    *,
    normalized_path_origin: str,
    path_diversity_eligible: bool,
    legacy_carryover_hint: Optional[str],
    validation_profile: str,
    next_missing_axis: str,
) -> Dict[str, str]:
    if normalized_path_origin == "true_primary_path" and path_diversity_eligible:
        return {
            "user_language_summary": "이 결과는 새 경로 후보로 볼 수 있는 쪽이다.",
            "user_language_caution": "그래도 path 하나만으로 line 병목이 풀렸다고 읽으면 안 된다.",
            "user_language_next_read": _next_read_sentence(next_missing_axis, fallback="새 경로인지 유지되는지와 현재 병목 축을 같이 봐야 한다."),
        }

    if normalized_path_origin == "observer_derived_path" and path_diversity_eligible:
        return {
            "user_language_summary": "이 결과는 observer 재적용 경로에서 나온 읽기다.",
            "user_language_caution": "원문을 다시 본 경로이긴 하지만, 이것만으로 broad path opening 이라고 단정하면 안 된다.",
            "user_language_next_read": _next_read_sentence(next_missing_axis, fallback="observer 경로 외에 다른 true primary path가 더 있는지 같이 봐야 한다."),
        }

    if normalized_path_origin == "legacy_raw_surface_carryover":
        carryover_tail = legacy_carryover_hint or "legacy raw_surface carryover"
        return {
            "user_language_summary": "새 경로를 찾은 게 아니라 예전 raw_surface 꼬리가 다시 보이는 상태다.",
            "user_language_caution": "겉보기엔 다른 path 같아 보여도 diversity 근거로 세면 안 된다.",
            "user_language_next_read": f"{_next_read_sentence(next_missing_axis, fallback='새 path 여부보다 carryover 여부를 먼저 확인해야 한다.')} ({carryover_tail})",
        }

    return {
        "user_language_summary": "지금은 경로 성격이 섞여 있어 단정하기 어려운 결과다.",
        "user_language_caution": "이 상태를 바로 새 path 나 새로운 diversity로 읽으면 과장이다.",
        "user_language_next_read": _next_read_sentence(next_missing_axis, fallback="먼저 path 정체를 더 분명히 확인해야 한다."),
    }


def _next_read_sentence(next_missing_axis: str, *, fallback: str) -> str:
    if next_missing_axis == "path":
        return "다음 읽기에서는 새 material보다 진짜 다른 path인지 먼저 확인해야 한다."
    if next_missing_axis == "primary_material":
        return "다음 읽기에서는 새 path보다 다른 primary material에서 다시 잡히는지를 봐야 한다."
    if next_missing_axis == "multiple":
        return "다음 읽기에서는 한 축만 보지 말고 path와 material을 함께 봐야 한다."
    return fallback


def _build_reading_next_actions(*, pointer_info: Dict[str, Any], evidence_kind: str) -> List[Dict[str, str]]:
    actions: List[Dict[str, str]] = []
    fragment_id = pointer_info.get("fragment_id")
    source_pointer = pointer_info.get("source_pointer")

    if fragment_id:
        actions.append(
            {
                "action_type": "reread_entry",
                "label": "reread fragment",
                "target": f"python3 scripts/apply_internal_observer.py runtime {fragment_id}",
            }
        )
        actions.append(
            {
                "action_type": "observer_reapply_entry",
                "label": "observer reapply",
                "target": f"python3 scripts/apply_internal_observer.py runtime {fragment_id} --record-line-thickening",
            }
        )
        actions.append(
            {
                "action_type": "source_reopen_entry",
                "label": "source reopen",
                "target": source_pointer or fragment_id,
            }
        )
    elif evidence_kind == "summary_echo":
        actions.append(
            {
                "action_type": "source_reopen_entry",
                "label": "open summary source",
                "target": pointer_info.get("source_ref") or "summary source unavailable",
            }
        )
    return actions


def _build_capability_why_selected(*, query: str, capability: Dict[str, Any]) -> str:
    reasons = []
    label = _clean_text(capability.get("label"))
    aliases = _string_list(capability.get("intent_aliases"))
    if _match_score(query, [label]) > 0:
        reasons.append("query matched capability label")
    if _match_score(query, aliases) > 0:
        reasons.append("query matched intent alias")
    reasons.append(f"class={_clean_text(capability.get('capability_class')) or 'unknown'}")
    return "; ".join(reasons[:3])


def _build_capability_summary(capability: Dict[str, Any]) -> str:
    capability_type = _clean_text(capability.get("capability_class")) or "unknown"
    input_kinds = ", ".join(_string_list(capability.get("input_kinds"))[:3])
    outputs = ", ".join(_string_list(capability.get("output_surfaces"))[:2])
    if input_kinds and outputs:
        return f"{capability_type} for {input_kinds}; outputs to {outputs}"
    if outputs:
        return f"{capability_type} with outputs {outputs}"
    return capability_type


def _build_invocation_hint(entrypoint: Optional[str], *, capability_type: Optional[str]) -> Optional[str]:
    if not entrypoint:
        return None
    if entrypoint.endswith(".py"):
        if capability_type == "loop":
            return f"python3 {entrypoint} runtime --limit 5"
        return f"python3 {entrypoint} ..."
    return entrypoint


def _build_safety_note(safety_mode: str) -> str:
    mapping = {
        "main_runtime_mutating": "writes to main runtime surfaces",
        "sandbox_only": "sandbox only; main runtime should stay untouched",
        "plan_only_default": "defaults to plan-first; execution must be opened explicitly",
        "stdout_only": "read/probe oriented; stdout only",
        "embedded_component": "component capability; invoked through another runner",
    }
    return mapping.get(safety_mode, safety_mode)


def _build_capability_next_actions(
    *,
    entrypoint: Optional[str],
    runtime_scope: str,
    output_surfaces: List[str],
) -> List[Dict[str, str]]:
    actions: List[Dict[str, str]] = []
    if entrypoint:
        actions.append(
            {
                "action_type": "entrypoint_check",
                "label": "entrypoint",
                "target": entrypoint,
            }
        )
    actions.append(
        {
            "action_type": "runtime_scope_check",
            "label": "runtime scope",
            "target": runtime_scope,
        }
    )
    if output_surfaces:
        actions.append(
            {
                "action_type": "output_surface_check",
                "label": "output surfaces",
                "target": ", ".join(output_surfaces[:3]),
            }
        )
    return actions


def _resolve_selected_result(results: List[Dict[str, Any]], selected_candidate_id: Optional[str]) -> Optional[Dict[str, Any]]:
    if not results:
        return None
    if selected_candidate_id:
        for result in results:
            if result.get("candidate_id") == selected_candidate_id:
                return result
    return results[0]


def _build_path_diversity_summary(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    reading_results = [row for row in results if row.get("result_type") == READING_RESULT]
    normalized_counts = {
        "true_primary_path": 0,
        "observer_derived_path": 0,
        "legacy_raw_surface_carryover": 0,
        "unknown_or_mixed": 0,
    }
    eligible_paths: set[str] = set()
    carryover_count = 0
    unknown_count = 0
    next_missing_axis = ""

    for row in reading_results:
        normalized = _clean_text(row.get("normalized_path_origin")) or "unknown_or_mixed"
        if normalized not in normalized_counts:
            normalized = "unknown_or_mixed"
        normalized_counts[normalized] += 1

        if row.get("line_name") == "input_to_reading_organ" and not next_missing_axis:
            next_missing_axis = _clean_text(row.get("next_missing_axis"))

        if row.get("path_diversity_eligible"):
            eligible_paths.add(_clean_text(row.get("normalized_path_origin")) or _clean_text(row.get("path_origin")))
        elif normalized == "legacy_raw_surface_carryover":
            carryover_count += 1
        elif normalized == "unknown_or_mixed":
            unknown_count += 1

    summary_language = _build_summary_user_language(
        eligible_distinct_path_count=len([value for value in eligible_paths if value]),
        non_eligible_carryover_count=carryover_count,
        unknown_or_mixed_count=unknown_count,
        next_missing_axis=next_missing_axis,
    )

    return {
        "normalized_path_summary": normalized_counts,
        "eligible_distinct_path_count": len([value for value in eligible_paths if value]),
        "non_eligible_carryover_count": carryover_count,
        "unknown_or_mixed_count": unknown_count,
        "summary_path_caution": summary_language["summary_path_caution"],
        "summary_user_language_summary": summary_language["summary_user_language_summary"],
        "summary_user_language_caution": summary_language["summary_user_language_caution"],
        "summary_user_language_next_read": summary_language["summary_user_language_next_read"],
    }


def _build_summary_user_language(
    *,
    eligible_distinct_path_count: int,
    non_eligible_carryover_count: int,
    unknown_or_mixed_count: int,
    next_missing_axis: str,
) -> Dict[str, str]:
    if eligible_distinct_path_count <= 1 and non_eligible_carryover_count > 0:
        return {
            "summary_path_caution": "겉보기보다 실제 새 path 는 적고 carryover 가 섞여 있다.",
            "summary_user_language_summary": "겉보기에는 path 가 여러 개처럼 보여도, 실제로 새 path 로 셀 수 있는 건 아직 적다.",
            "summary_user_language_caution": "예전 raw_surface 꼬리를 path 다양성으로 세면 과장이다.",
            "summary_user_language_next_read": _next_read_sentence(next_missing_axis, fallback="새 path 라벨보다 진짜 path 근거를 먼저 확인해야 한다."),
        }
    if unknown_or_mixed_count > 0:
        return {
            "summary_path_caution": "일부 결과는 아직 성격이 섞여 있어 단정하면 안 된다.",
            "summary_user_language_summary": "지금 summary 는 path 구성이 일부 정리됐지만 아직 섞인 결과가 남아 있다.",
            "summary_user_language_caution": "unknown_or_mixed 를 억지로 새 path 나 carryover 로 밀면 안 된다.",
            "summary_user_language_next_read": _next_read_sentence(next_missing_axis, fallback="먼저 섞인 항목의 정체를 더 분명히 봐야 한다."),
        }
    return {
        "summary_path_caution": "새 path 후보가 보여도 path 병목이 풀렸다고 바로 읽으면 안 된다.",
        "summary_user_language_summary": "지금 summary 는 path 구성을 비교적 정직하게 보여주지만, 병목이 해소됐다는 뜻은 아니다.",
        "summary_user_language_caution": "eligible path 수만 보고 broad opening 이라고 읽으면 과장이다.",
        "summary_user_language_next_read": _next_read_sentence(next_missing_axis, fallback="다음에는 path 근거가 더 늘어나는지 먼저 봐야 한다."),
    }


def _match_score(query: str, values: Iterable[Any]) -> int:
    tokens = _query_tokens(query)
    if not tokens:
        return 0
    corpus = " ".join(_clean_text(value).lower() for value in values if _clean_text(value))
    if not corpus:
        return 0
    score = 0
    for token in tokens:
        if token in corpus:
            score += 2
    joined_query = _clean_text(query).lower()
    if joined_query and joined_query in corpus:
        score += 3
    return score


def _query_tokens(query: str) -> List[str]:
    return [token for token in re.split(r"[\s_/\-]+", _clean_text(query).lower()) if token]


def _matched_preview(*, query: str, text: str) -> str:
    text = _clean_text(text)
    if not text:
        return ""
    lower_text = text.lower()
    tokens = _query_tokens(query)
    start = 0
    for token in tokens:
        index = lower_text.find(token)
        if index >= 0:
            start = max(0, index - 60)
            end = min(len(text), index + 180)
            return text[start:end].strip()
    return _truncate(text, 220)


def _normalize_evidence_kind(value: Any) -> str:
    cleaned = _clean_text(value)
    if cleaned in {"summary_echo", "source_linked", "direct_span"}:
        return cleaned
    return "summary_echo"


def _runtime_scope_from_safety_mode(safety_mode: str) -> str:
    if safety_mode == "sandbox_only":
        return "sandbox"
    if safety_mode == "main_runtime_mutating":
        return "main"
    return "mixed"


def _evidence_rank(evidence_kind: Any) -> int:
    mapping = {"direct_span": 0, "source_linked": 1, "summary_echo": 2}
    return mapping.get(_normalize_evidence_kind(evidence_kind), 3)


def _load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _string_list(values: Any) -> List[str]:
    if not isinstance(values, list):
        return []
    return [_clean_text(value) for value in values if _clean_text(value)]


def _dedupe_strings(values: List[str]) -> List[str]:
    seen: set[str] = set()
    result: List[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _truncate(text: str, limit: int) -> str:
    text = _clean_text(text)
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)].rstrip() + "..."
