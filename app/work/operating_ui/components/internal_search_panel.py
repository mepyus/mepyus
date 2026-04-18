from __future__ import annotations

from typing import Any, Dict, List, Optional


def build_internal_search_panel_view(
    *,
    query: str,
    results: Optional[List[Dict[str, Any]]],
    selectedResult: Optional[Dict[str, Any]],
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    normalized_results = [_adapt_result_row(item) for item in results or [] if isinstance(item, dict)]
    normalized_results = [item for item in normalized_results if item.get("candidateId")]

    if not query.strip():
        return {
            "state": "idle",
            "title": "Internal Search",
            "query": "",
            "count": 0,
            "items": [],
            "selected": None,
            "summary": None,
            "helperText": "enter a query to search reading and capability candidates",
        }

    if not normalized_results:
        return {
            "state": "empty",
            "title": "Internal Search",
            "query": query,
            "count": 0,
            "items": [],
            "selected": None,
            "summary": None,
            "helperText": "no internal search matches",
        }

    selected = _adapt_selected_result(selectedResult or normalized_results[0])
    return {
        "state": "loaded",
        "title": "Internal Search",
        "query": query,
        "count": len(normalized_results),
        "items": normalized_results,
        "selected": selected,
        "summary": _adapt_summary(summary or {}),
        "helperText": None,
    }


def render_internal_search_panel_text(view: Dict[str, Any]) -> str:
    state = view.get("state")
    if state != "loaded":
        return f"InternalSearchPanel[state={state}] | {view.get('helperText') or 'unavailable'}"

    lines = [
        f"InternalSearchPanel[query={view.get('query')!r} count={view.get('count', 0)}]",
    ]
    summary = view.get("summary") or {}
    if summary:
        lines.append(
            "Summary | "
            + " | ".join(
                part
                for part in [
                    f"eligible_paths={summary.get('eligibleDistinctPathCount')}",
                    f"carryover={summary.get('nonEligibleCarryoverCount')}",
                    f"unknown={summary.get('unknownOrMixedCount')}",
                    summary.get("userLanguageSummary"),
                ]
                if part not in (None, "")
            )
        )
    for item in view.get("items", []):
        lines.append(
            "- "
            + " | ".join(
                part
                for part in [
                    item.get("resultType"),
                    item.get("title"),
                    item.get("subtitle"),
                    item.get("whySelected"),
                ]
                if part
            )
        )

    selected = view.get("selected") or {}
    if selected:
        lines.append("")
        lines.append(f"Selected[{selected.get('resultType')}] {selected.get('title')}")
        if selected.get("detailRows"):
            for row in selected.get("detailRows", []):
                lines.append(f"* {row.get('label')}: {row.get('value')}")
        if selected.get("nextActions"):
            lines.append("NextActions:")
            for action in selected.get("nextActions", []):
                lines.append(f"  - {action.get('label')}: {action.get('target')}")
    return "\n".join(lines)


def _adapt_result_row(item: Dict[str, Any]) -> Dict[str, Any]:
    result_type = item.get("result_type")
    if result_type == "capability_result":
        subtitle = " | ".join(
            part
            for part in [
                item.get("capability_type"),
                item.get("runtime_scope"),
                ", ".join(item.get("intent_aliases") or []) if item.get("intent_aliases") else None,
            ]
            if part
        )
    else:
        subtitle = " | ".join(
            part
            for part in [
                item.get("evidence_kind"),
                item.get("path_origin") or item.get("path_signature"),
                item.get("line_name"),
            ]
            if part
        )

    return {
        "candidateId": item.get("candidate_id"),
        "title": item.get("title") or item.get("candidate_id"),
        "resultType": result_type,
        "subtitle": subtitle,
        "whySelected": item.get("why_selected"),
    }


def _adapt_selected_result(item: Dict[str, Any]) -> Dict[str, Any]:
    result_type = item.get("result_type")
    if result_type == "capability_result":
        detail_rows = [
            {"label": "capability type", "value": item.get("capability_type")},
            {"label": "intent aliases", "value": ", ".join(item.get("intent_aliases") or [])},
            {"label": "entrypoint", "value": item.get("entrypoint")},
            {"label": "runtime scope", "value": item.get("runtime_scope")},
            {"label": "output surfaces", "value": ", ".join(item.get("output_surfaces") or [])},
            {"label": "linked scripts", "value": ", ".join(item.get("linked_scripts") or [])},
            {"label": "safety note", "value": item.get("safety_note")},
        ]
    else:
        pointer = item.get("source_ref")
        if item.get("fragment_id"):
            pointer = " | ".join(
                part
                for part in [
                    item.get("fragment_id"),
                    item.get("source_ref"),
                    _format_source_range(item.get("source_range"), item.get("paragraph_index")),
                ]
                if part
            )
        detail_rows = [
            {"label": "matched preview", "value": item.get("matched_text_preview")},
            {"label": "surrounding context", "value": item.get("surrounding_context_preview")},
            {"label": "source pointer", "value": pointer},
            {"label": "evidence kind", "value": item.get("evidence_kind")},
            {"label": "original path origin", "value": item.get("path_origin")},
            {"label": "normalized path origin", "value": item.get("normalized_path_origin")},
            {"label": "path diversity eligible", "value": str(item.get("path_diversity_eligible")).lower() if item.get("path_diversity_eligible") is not None else None},
            {"label": "path classification reason", "value": item.get("path_origin_classification_reason")},
            {"label": "legacy carryover hint", "value": item.get("legacy_carryover_hint")},
            {"label": "validation profile", "value": item.get("validation_profile")},
            {"label": "primary-only profile", "value": item.get("primary_only_validation_profile")},
            {"label": "support ecology bias", "value": item.get("support_ecology_bias")},
            {"label": "next missing axis", "value": item.get("next_missing_axis")},
            {"label": "path signature", "value": item.get("path_signature")},
            {"label": "user-language summary", "value": item.get("user_language_summary")},
            {"label": "user-language caution", "value": item.get("user_language_caution")},
            {"label": "user-language next read", "value": item.get("user_language_next_read")},
        ]

    return {
        "candidateId": item.get("candidate_id"),
        "title": item.get("title") or item.get("candidate_id"),
        "resultType": result_type,
        "detailRows": [row for row in detail_rows if row.get("value") not in (None, "", [])],
        "nextActions": item.get("next_actions") or [],
    }


def _adapt_summary(summary: Dict[str, Any]) -> Dict[str, Any]:
    normalized = summary.get("normalized_path_summary") if isinstance(summary, dict) else {}
    return {
        "normalizedPathSummary": normalized if isinstance(normalized, dict) else {},
        "eligibleDistinctPathCount": summary.get("eligible_distinct_path_count"),
        "nonEligibleCarryoverCount": summary.get("non_eligible_carryover_count"),
        "unknownOrMixedCount": summary.get("unknown_or_mixed_count"),
        "summaryPathCaution": summary.get("summary_path_caution"),
        "userLanguageSummary": summary.get("summary_user_language_summary"),
        "userLanguageCaution": summary.get("summary_user_language_caution"),
        "userLanguageNextRead": summary.get("summary_user_language_next_read"),
    }


def _format_source_range(source_range: Any, paragraph_index: Any) -> Optional[str]:
    if isinstance(source_range, dict):
        if "start" in source_range and "end" in source_range:
            base = f"{source_range.get('start')}-{source_range.get('end')}"
        elif "page_ref" in source_range:
            base = str(source_range.get("page_ref"))
        else:
            base = None
    else:
        base = str(source_range) if source_range not in (None, "") else None
    if base and paragraph_index not in (None, ""):
        return f"{base}; paragraph={paragraph_index}"
    return base
