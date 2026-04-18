from __future__ import annotations

from typing import Any, Dict, List, Optional


def adapt_runtime_payload_to_phase1_view_model(
    live_data: Dict[str, Any],
    *,
    memory_stickers: List[Dict[str, str]],
    path_residue: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    debug_text = live_data.get("debug_text") if isinstance(live_data.get("debug_text"), dict) else {}
    objects = _adapt_object_options(live_data)
    operating_observation = {
        "state": str(live_data.get("state") or "unknown"),
        "live_availability": str(live_data.get("live_availability") or "unknown"),
        "selected_asset_id": str(live_data.get("selected_asset_id") or "").strip() or None,
        "selection_query_state": str(live_data.get("selection_query_state") or "").strip() or "unknown",
        "current_run_text": _string_or_fallback(
            live_data.get("process_console_summary"),
            fallback="current run source unavailable",
        ),
        "detail_summary_text": _string_or_fallback(
            debug_text.get("detail_summary"),
            fallback="detail summary source unavailable",
        ),
        "recent_activity_text": _string_or_fallback(
            debug_text.get("activity"),
            fallback="recent activity source unavailable",
        ),
        "compare_hint_text": _string_or_fallback(
            debug_text.get("compare_panel"),
            fallback="compare hint source unavailable",
        ),
        "source_notice": str(
            live_data.get("selection_notice")
            or live_data.get("page_fallback_message")
            or ""
        ).strip(),
        "provenance_summary": (
            "live runtime observation"
            if live_data.get("state") == "loaded"
            else "degraded observation fallback"
        ),
        "multi_lens_supervisor_surface": _adapt_multi_lens_supervisor_surface(
            live_data.get("multi_lens_supervisor_surface"),
        ),
    }
    source_map = {
        "operating_current_run": {
            "state": _availability_state(live_data.get("process_console_summary")),
            "source": "live.process_console_summary",
        },
        "operating_recent_activity": {
            "state": _availability_state(debug_text.get("activity")),
            "source": "live.debug_text.activity",
        },
        "explore_objects": {
            "state": "available" if objects else "fallback",
            "source": "live.available_assets",
            "count": len(objects),
        },
        "search_candidates": {
            "state": "available" if objects or memory_stickers else "fallback",
            "source": "phase1.objects + saved_paths",
            "count": len(objects) + len(memory_stickers),
        },
        "saved_paths": {
            "state": "available" if memory_stickers else "fallback",
            "source": "phase1_memory_stickers.jsonl",
            "count": len(memory_stickers),
        },
        "path_residue": {
            "state": "available" if path_residue else "fallback",
            "source": "phase1_current_path_residue.json",
            "count": 1 if path_residue else 0,
        },
    }
    return {
        "operating_observation": operating_observation,
        "explore_binding": {
            "objects": objects,
            "object_source_state": source_map["explore_objects"]["state"],
            "object_source_note": (
                "runtime object options adapted from live available assets"
                if objects
                else "runtime object source missing / degraded fallback mode"
            ),
            "provenance_summary": (
                "live runtime options + scaffold support"
                if objects
                else "fallback runtime handle + scaffold support"
            ),
        },
        "search_binding": {
            "source_state": source_map["search_candidates"]["state"],
            "source_note": (
                "search candidates adapted from current runtime options and explicit saved paths"
                if (objects or memory_stickers)
                else "search candidate source sparse / degraded fallback mode"
            ),
            "provenance_summary": (
                "runtime options + stored saved paths"
                if objects
                else ("stored saved paths only" if memory_stickers else "degraded fallback candidates")
            ),
        },
        "memory_binding": {
            "saved_path_count": len(memory_stickers),
            "source_note": (
                "saved paths loaded from explicit sticker store"
                if memory_stickers
                else "no explicit saved paths yet / storage path still available"
            ),
            "provenance_summary": "stored saved paths",
        },
        "similar_binding": {
            "seed_ready_count": len(memory_stickers),
            "source_note": (
                "seed context can be activated from explicit saved paths"
                if memory_stickers
                else "no saved path seed context yet"
            ),
            "provenance_summary": (
                "stored seed context + local re-query"
                if memory_stickers
                else "stored seed context unavailable"
            ),
        },
        "source_map": source_map,
    }


def _adapt_object_options(live_data: Dict[str, Any]) -> List[Dict[str, str]]:
    raw_assets = live_data.get("available_assets") if isinstance(live_data.get("available_assets"), list) else []
    options: List[Dict[str, str]] = []
    for asset in raw_assets:
        asset_id = str((asset or {}).get("id") or "").strip()
        if not asset_id:
            continue
        options.append(
            {
                "id": asset_id,
                "label": str(asset.get("title") or asset_id).strip() or asset_id,
                "note": "runtime object option adapted for phase1 explore",
            }
        )
    if options:
        return options
    fallback_asset_id = str(
        live_data.get("selected_asset_id")
        or live_data.get("requested_asset_id")
        or ""
    ).strip()
    if fallback_asset_id:
        return [
            {
                "id": fallback_asset_id,
                "label": fallback_asset_id,
                "note": "fallback runtime object handle / live source sparse",
            }
        ]
    return []


def _availability_state(value: Any) -> str:
    if value in (None, "", [], {}):
        return "fallback"
    return "available"


def _string_or_fallback(value: Any, *, fallback: str) -> str:
    if isinstance(value, str):
        text = value.strip()
        return text or fallback
    if isinstance(value, dict):
        return str(value) if value else fallback
    return fallback


def _adapt_multi_lens_supervisor_surface(value: Any) -> Dict[str, Any]:
    if not isinstance(value, dict):
        return {
            "state": "unavailable",
            "source_note": "multi-lens supervisor surface unavailable",
            "artifact_path": None,
            "line_states": {},
            "parked_axes": [],
            "handoff_boundary": {},
            "readings": [],
        }
    primary_view = value.get("primary_view") if isinstance(value.get("primary_view"), dict) else {}
    return {
        "state": "available",
        "source_note": "multi-lens supervisor surfaced view",
        "artifact_path": str(value.get("artifact_path") or "").strip() or None,
        "line_states": primary_view.get("line_states") if isinstance(primary_view.get("line_states"), dict) else {},
        "parked_axes": value.get("parked_axes") if isinstance(value.get("parked_axes"), list) else [],
        "handoff_boundary": value.get("handoff_boundary") if isinstance(value.get("handoff_boundary"), dict) else {},
        "raw_output_reference": str(value.get("raw_output_reference") or "").strip() or None,
        "readings": primary_view.get("readings") if isinstance(primary_view.get("readings"), list) else [],
    }
