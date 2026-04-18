from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional
import json

from app.runtime.process_console_view.builder import build_process_console_view_data
from app.work.operating_ui.operating_ui_payload_adapter import (
    adapt_process_console_payload_to_operating_ui_model,
)
from app.work.operating_ui.components.derived_state_strip import (
    build_derived_state_strip_view,
    render_derived_state_strip_text,
)
from app.work.operating_ui.components.asset_state_board import (
    build_asset_state_board_view,
    render_asset_state_board_text,
)
from app.work.operating_ui.components.activity_panel import (
    build_activity_panel_view,
    render_activity_panel_text,
)
from app.work.operating_ui.components.selected_asset_detail_summary import (
    build_selected_asset_detail_summary_view,
    render_selected_asset_detail_summary_text,
)
from app.work.operating_ui.components.compare_candidate_panel import (
    build_compare_candidate_panel_view,
    render_compare_candidate_panel_text,
)


def build_operating_ui_live_composition_data(
    runtime_root: Path,
    *,
    asset_id: Optional[str] = None,
    sort_by: str = "updated_at",
    live_mode: Optional[str] = None,
    compare_mode: Optional[str] = None,
) -> Dict[str, Any]:
    validation = _resolve_validation_overrides(
        live_mode=live_mode,
        compare_mode=compare_mode,
    )

    if validation["live_mode"] == "unavailable":
        return _build_controlled_live_unavailable_payload(
            requested_asset_id=asset_id,
        )

    try:
        process_console_payload = _load_process_console_payload(
            runtime_root,
            asset_id=asset_id,
            sort_by=sort_by,
        )
    except Exception as error:
        return {
            "state": "live_unavailable",
            "source_kind": "process_console_payload",
            "selected_asset_id": asset_id,
            "error": str(error),
        }

    adapted = adapt_process_console_payload_to_operating_ui_model(
        process_console_payload,
        initial_asset_id=asset_id,
    )
    requested_asset_id = asset_id
    available_assets = _adapt_available_assets(adapted.get("boardItems", []))
    valid_asset_ids = {item["id"] for item in available_assets}
    selection_query_state = _derive_selection_query_state(
        requested_asset_id=requested_asset_id,
        selected_asset_id=adapted.get("selectedAssetId"),
        valid_asset_ids=valid_asset_ids,
    )

    if selection_query_state == "invalid_selected_asset_query" and adapted.get("selectedAssetId"):
        process_console_payload = _load_process_console_payload(
            runtime_root,
            asset_id=adapted.get("selectedAssetId"),
            sort_by=sort_by,
        )
        adapted = adapt_process_console_payload_to_operating_ui_model(
            process_console_payload,
            initial_asset_id=adapted.get("selectedAssetId"),
        )
        available_assets = _adapt_available_assets(adapted.get("boardItems", []))
        valid_asset_ids = {item["id"] for item in available_assets}

    derived_strip = build_derived_state_strip_view(
        selectedAsset=adapted.get("selectedAsset"),
        latestPreview=(adapted.get("derivedStrip") or {}).get("latestPreview"),
        diffSummary=(adapted.get("derivedStrip") or {}).get("diffSummary"),
        attentionSummary=(adapted.get("derivedStrip") or {}).get("attentionSummary"),
        memorySummary=(adapted.get("derivedStrip") or {}).get("memorySummary"),
        compareHref=(
            f"/process-console?asset_id={adapted.get('selectedAssetId')}"
            if adapted.get("selectedAssetId")
            else None
        ),
    )

    board = build_asset_state_board_view(
        adapted.get("boardItems", []),
        selectedAssetId=adapted.get("selectedAssetId"),
        sortLabel=sort_by,
        filterSummary=_build_filter_summary(process_console_payload),
        baseHref="/operating-ui-live",
    )

    activity_model = adapted.get("activityPanel") or {}
    selected_asset = adapted.get("selectedAsset") or {}
    history_summary = (selected_asset.get("historySummary") or {}) if isinstance(selected_asset, dict) else {}
    if not activity_model.get("items") and process_console_payload.get("history_drilldown", {}).get("state") == "history_unavailable":
        history_summary = {**history_summary, "state": "history_unavailable"}

    latest_lineage = {
        "summary": activity_model.get("latestLineageSummary"),
        "latestTrigger": activity_model.get("latestTrigger"),
        "latestReason": activity_model.get("latestReason"),
        "latestUpdatedAt": activity_model.get("latestUpdatedAt"),
    }
    activity = build_activity_panel_view(
        activity_model.get("items", []),
        historySummary=history_summary,
        latestLineage=latest_lineage,
    )
    availability = _derive_live_availability(adapted, board)
    detail_summary = build_selected_asset_detail_summary_view(
        selectedAsset=adapted.get("selectedAsset"),
        latestPreview=(adapted.get("derivedStrip") or {}).get("latestPreview"),
        diffSummary=(adapted.get("derivedStrip") or {}).get("diffSummary"),
        attentionSummary=(adapted.get("derivedStrip") or {}).get("attentionSummary"),
        memorySummary=(adapted.get("derivedStrip") or {}).get("memorySummary"),
        compareCandidates=adapted.get("compareCandidates"),
        guards=adapted.get("guards"),
        statusBadge=_build_selected_status_badge(selection_query_state),
    )
    compare_panel = _build_compare_panel_with_validation(
        compare_mode=validation["compare_mode"],
        selected_asset=adapted.get("selectedAsset"),
        compare_candidates=adapted.get("compareCandidates"),
        live_availability=availability,
        guards=adapted.get("guards"),
    )

    selection_notice = _build_selection_notice(
        selection_query_state=selection_query_state,
        requested_asset_id=requested_asset_id,
        selected_asset_id=adapted.get("selectedAssetId"),
        live_availability=availability,
    )
    multi_lens_supervisor_surface = _load_latest_multi_lens_supervisor_surface(runtime_root)
    return {
        "state": "loaded",
        "live_availability": availability,
        "source_kind": "process_console_payload",
        "selection_query_state": selection_query_state,
        "requested_asset_id": requested_asset_id,
        "selected_asset_id": adapted.get("selectedAssetId"),
        "selection_notice": selection_notice,
        "compare_mode": validation["compare_mode"],
        "available_assets": available_assets,
        "pageTitle": adapted.get("pageTitle"),
        "strip": derived_strip,
        "board": board,
        "detail_summary": detail_summary,
        "compare_panel": compare_panel,
        "activity": activity,
        "multi_lens_supervisor_surface": multi_lens_supervisor_surface,
        "adapted_model": adapted,
        "process_console_summary": process_console_payload.get("summary", {}),
        "debug_text": {
            "strip": render_derived_state_strip_text(derived_strip),
            "board": render_asset_state_board_text(board),
            "detail_summary": render_selected_asset_detail_summary_text(detail_summary),
            "compare_panel": render_compare_candidate_panel_text(compare_panel),
            "activity": render_activity_panel_text(activity),
        },
    }


def _load_latest_multi_lens_supervisor_surface(runtime_root: Path) -> Dict[str, Any]:
    view_root = runtime_root / "views" / "multi_lens_document_reading"
    if not view_root.exists():
        return {}
    candidates = sorted(view_root.glob("*_multi_lens_supervisor_surface_*.json"))
    if not candidates:
        return {}
    latest = candidates[-1]
    try:
        payload = json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        return {}
    payload["artifact_path"] = str(latest.relative_to(runtime_root))
    return payload


def render_operating_ui_live_composition_html(
    data: Dict[str, Any] | None = None,
    api_path: str = "/api/operating-ui-live",
) -> str:
    payload_block = (
        f'<script id="operating-ui-live-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('operating-ui-live-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Operating UI Live</title>
  <style>
    body { margin: 0; font-family: Georgia, serif; background: #f5f1e8; color: #1f2937; }
    .page { max-width: 1440px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .top { background: #fffaf2; border: 1px solid #d7cab7; border-radius: 18px; padding: 16px; }
    .nav { display: inline-block; padding: 7px 12px; border-radius: 999px; border: 1px solid #d7cab7; text-decoration: none; color: #6c4d2f; background: #fff; margin-right: 8px; }
    .top-stack { display: grid; gap: 16px; }
    .layout { display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(320px, 0.75fr); gap: 16px; align-items: start; }
    .left-col { min-width: 0; }
    .right-col { display: grid; gap: 16px; align-content: start; min-width: 0; }
    .panel { background: #fffaf2; border: 1px solid #d7cab7; border-radius: 18px; padding: 14px; }
    .panel h3 { margin-top: 0; margin-bottom: 10px; }
    .subhead { margin-top: -4px; margin-bottom: 10px; color: #6b7280; font-size: 13px; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .chip { border-radius: 999px; padding: 5px 9px; font-size: 12px; background: #efe5d3; color: #5b422a; }
    .card { padding: 10px; border: 1px solid #e5dac8; border-radius: 14px; background: #fff; margin-bottom: 10px; }
    .card.selected { border-color: #6c4d2f; box-shadow: 0 0 0 2px rgba(108,77,47,0.15); }
    .meta { color: #6b7280; font-size: 13px; }
    .empty { color: #8b7355; font-style: italic; }
    pre { white-space: pre-wrap; word-break: break-word; background: #fff; border: 1px solid #e5dac8; border-radius: 12px; padding: 10px; }
  </style>
</head>
<body>
  """ + payload_block + """
  <div id="app"></div>
  <script>
    (async () => {
      """ + bootstrap + """
      const app = document.getElementById('app');
      const page = document.createElement('div');
      page.className = 'page';

      const top = document.createElement('div');
      top.className = 'top';
      top.innerHTML = `<a class="nav" href="/process-console">process-console</a><a class="nav" href="/operating-ui-demo?case=a">fixture demo</a><a class="nav" href="/operating-ui-live">live default</a><a class="nav" href="/operating-ui-phase1">main operating set</a><div><strong>${data.pageTitle || 'operating ui live'}</strong> <span class="meta">state=${data.state || 'unknown'} / selected=${data.selected_asset_id || 'none'} / availability=${data.live_availability || 'unknown'} / mode=live</span></div>`;
      page.appendChild(top);

      if (data.state !== 'loaded') {
        const control = document.createElement('div');
        control.className = 'panel';
        control.innerHTML = '<h3>Live Control Bar</h3>';
        const controlSub = document.createElement('div');
        controlSub.className = 'subhead';
        controlSub.textContent = 'select operating target';
        control.appendChild(controlSub);
        const controlMeta = document.createElement('div');
        controlMeta.className = 'meta';
        controlMeta.textContent = `current shown asset=${data.selected_asset_id || 'none'} / source=${data.source_kind || 'unknown'} / live=${data.live_availability || 'unknown'}`;
        control.appendChild(controlMeta);
        if (data.selection_notice) {
          const controlNotice = document.createElement('div');
          controlNotice.className = 'meta';
          controlNotice.textContent = data.selection_notice;
          control.appendChild(controlNotice);
        }
        const controlQuery = document.createElement('div');
        controlQuery.className = 'meta';
        controlQuery.textContent = `requested asset=${data.requested_asset_id || 'none'} / query_state=${data.selection_query_state || 'none'}`;
        control.appendChild(controlQuery);
        page.appendChild(control);

        const panel = document.createElement('div');
        panel.className = 'panel';
        panel.innerHTML = `<h3>Live Page Fallback</h3><div class="empty">${data.page_fallback_message || data.state || 'live_unavailable'}</div><pre>${JSON.stringify(data, null, 2)}</pre>`;
        page.appendChild(panel);
        app.appendChild(page);
        return;
      }

      const topStack = document.createElement('div');
      topStack.className = 'top-stack';

      const control = document.createElement('div');
      control.className = 'panel';
      control.innerHTML = '<h3>Live Control Bar</h3>';
      const controlSub = document.createElement('div');
      controlSub.className = 'subhead';
      controlSub.textContent = 'select operating target';
      control.appendChild(controlSub);
      const controlMeta = document.createElement('div');
      controlMeta.className = 'meta';
      controlMeta.textContent = `current shown asset=${data.selected_asset_id || 'none'} / source=${data.source_kind || 'unknown'} / live=${data.live_availability || 'unknown'}`;
      control.appendChild(controlMeta);
      if (data.selection_notice) {
        const controlNotice = document.createElement('div');
        controlNotice.className = 'meta';
        controlNotice.textContent = data.selection_notice;
        control.appendChild(controlNotice);
      }
      const controlQuery = document.createElement('div');
      controlQuery.className = 'meta';
      controlQuery.textContent = `requested asset=${data.requested_asset_id || 'none'} / query_state=${data.selection_query_state || 'default_selected'}`;
      control.appendChild(controlQuery);

      const selectorRow = document.createElement('div');
      selectorRow.className = 'chip-row';
      const assets = data.available_assets || [];
      if (!assets.length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no assets available';
        selectorRow.appendChild(empty);
      } else {
        assets.forEach((asset) => {
          const link = document.createElement('a');
          link.className = 'nav';
          link.href = `/operating-ui-live?asset_id=${encodeURIComponent(asset.id)}`;
          link.textContent = asset.id === data.selected_asset_id ? `${asset.title} [selected]` : asset.title;
          selectorRow.appendChild(link);
        });
      }
      control.appendChild(selectorRow);
      topStack.appendChild(control);

      const strip = document.createElement('div');
      strip.className = 'panel';
      strip.innerHTML = '<h3>Derived State Strip</h3>';
      const stripSub = document.createElement('div');
      stripSub.className = 'subhead';
      stripSub.textContent = 'selected asset state summary';
      strip.appendChild(stripSub);
      const stripChips = document.createElement('div');
      stripChips.className = 'chip-row';
      (data.strip.badges || []).forEach((badge) => {
        const chip = document.createElement('span');
        chip.className = 'chip';
        chip.textContent = badge;
        stripChips.appendChild(chip);
      });
      if (!(data.strip.badges || []).length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no canonical state yet';
        stripChips.appendChild(empty);
      }
      strip.appendChild(stripChips);
      const stripMeta = document.createElement('pre');
      stripMeta.textContent = data.debug_text.strip;
      strip.appendChild(stripMeta);
      topStack.appendChild(strip);
      page.appendChild(topStack);

      const layout = document.createElement('div');
      layout.className = 'layout';

      const leftCol = document.createElement('div');
      leftCol.className = 'left-col';
      const board = document.createElement('div');
      board.className = 'panel';
      board.innerHTML = '<h3>Asset State Board</h3>';
      const boardSub = document.createElement('div');
      boardSub.className = 'subhead';
      boardSub.textContent = 'choose operating target';
      board.appendChild(boardSub);
      if (data.board.state === 'empty') {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = data.board.emptyLabel || 'no assets available';
        board.appendChild(empty);
        } else {
            const meta = document.createElement('div');
            meta.className = 'meta';
            meta.textContent = `selection=${data.board.selectionState || 'none'} / sort=${data.board.sortLabel || 'n/a'} / filter=${data.board.filterSummary || 'n/a'}`;
            board.appendChild(meta);
            (data.board.items || []).forEach((item) => {
                const card = document.createElement('div');
                card.className = 'card' + (item.selected ? ' selected' : '');
                const title = item.href
                  ? `<a class="nav" href="${item.href}">${item.title || item.assetId || 'asset'}</a>`
                  : `<strong>${item.title || item.assetId || 'asset'}</strong>`;
          card.innerHTML = `${title}<div class="meta">${item.primarySummary || ''}</div><div class="meta">${item.secondarySummary || ''}</div><div class="meta">${item.helperText || ''}</div>`;
          board.appendChild(card);
        });
      }
      leftCol.appendChild(board);
      layout.appendChild(leftCol);

      const rightCol = document.createElement('div');
      rightCol.className = 'right-col';

      const detail = document.createElement('div');
      detail.className = 'panel';
      detail.innerHTML = '<h3>Selected Detail Summary</h3>';
      const detailSub = document.createElement('div');
      detailSub.className = 'subhead';
      detailSub.textContent = 'read current target';
      detail.appendChild(detailSub);
      if (data.detail_summary && data.detail_summary.statusBadge && data.detail_summary.statusBadge.label) {
        const detailBadgeRow = document.createElement('div');
        detailBadgeRow.className = 'chip-row';
        const detailBadge = document.createElement('span');
        detailBadge.className = 'chip';
        detailBadge.textContent = data.detail_summary.statusBadge.label;
        detailBadgeRow.appendChild(detailBadge);
        detail.appendChild(detailBadgeRow);
      }
      const detailPre = document.createElement('pre');
      detailPre.textContent = data.debug_text.detail_summary;
      detail.appendChild(detailPre);
      rightCol.appendChild(detail);

      const compare = document.createElement('div');
      compare.className = 'panel';
      compare.innerHTML = '<h3>Compare Candidates</h3>';
      const compareSub = document.createElement('div');
      compareSub.className = 'subhead';
      compareSub.textContent = 'read nearby comparison candidates';
      compare.appendChild(compareSub);
      const comparePre = document.createElement('pre');
      comparePre.textContent = data.debug_text.compare_panel;
      compare.appendChild(comparePre);
      rightCol.appendChild(compare);

      const activity = document.createElement('div');
      activity.className = 'panel';
      activity.innerHTML = '<h3>Activity Panel</h3>';
      const activitySub = document.createElement('div');
      activitySub.className = 'subhead';
      activitySub.textContent = 'recent lineage and activity hints';
      activity.appendChild(activitySub);
      const activityPre = document.createElement('pre');
      activityPre.textContent = data.debug_text.activity;
      activity.appendChild(activityPre);
      rightCol.appendChild(activity);

      layout.appendChild(rightCol);

      page.appendChild(layout);
      app.appendChild(page);
    })();
  </script>
</body>
</html>"""


def _build_filter_summary(process_console_payload: Dict[str, Any]) -> str:
    summary = process_console_payload.get("summary", {})
    filters = summary.get("filters", {})
    if not filters:
        return "all"
    return ", ".join(f"{key}={value}" for key, value in filters.items())


def _derive_live_availability(adapted: Dict[str, Any], board: Dict[str, Any]) -> str:
    if not adapted:
        return "live_unavailable"
    if board.get("state") == "empty":
        return "empty_board"
    if not adapted.get("selectedAssetId"):
        return "no_selected_asset"
    if adapted.get("guards", {}).get("stateUnavailable") and not adapted.get("selectedAsset"):
        return "state_unavailable"
    return "live_ready"


def _adapt_available_assets(board_items: list[Dict[str, Any]]) -> list[Dict[str, str]]:
    assets = []
    for item in board_items:
        asset_id = item.get("id")
        title = item.get("title") or asset_id
        if asset_id:
            assets.append({"id": asset_id, "title": title})
    return assets


def _derive_selection_query_state(
    *,
    requested_asset_id: Optional[str],
    selected_asset_id: Optional[str],
    valid_asset_ids: set[str],
) -> str:
    if not valid_asset_ids:
        return "empty_assets"
    if not requested_asset_id:
        return "default_selected" if selected_asset_id else "no_selected_asset"
    if requested_asset_id in valid_asset_ids:
        return "valid_asset_id"
    if selected_asset_id:
        return "invalid_selected_asset_query"
    return "no_selected_asset"


def _build_selection_notice(
    *,
    selection_query_state: str,
    requested_asset_id: Optional[str],
    selected_asset_id: Optional[str],
    live_availability: str,
) -> Optional[str]:
    if live_availability == "live_unavailable":
        return "live source unavailable"
    if selection_query_state == "empty_assets":
        return "no selectable assets in live source"
    if selection_query_state == "invalid_selected_asset_query":
        return (
            f"requested asset '{requested_asset_id}' not found / "
            f"current shown asset '{selected_asset_id or 'none'}' / "
            "fallback applied"
        )
    if selection_query_state == "valid_asset_id":
        return f"requested asset '{selected_asset_id or requested_asset_id}' shown"
    if selection_query_state == "default_selected":
        return f"no requested asset / current shown asset '{selected_asset_id or 'none'}'"
    if selection_query_state == "no_selected_asset":
        return "no selected asset available"
    return None


def _build_selected_status_badge(selection_query_state: str) -> Optional[Dict[str, str]]:
    if selection_query_state == "invalid_selected_asset_query":
        return {
            "kind": "fallback_selected",
            "label": "fallback-selected asset",
        }
    return None


def _load_process_console_payload(
    runtime_root: Path,
    *,
    asset_id: Optional[str],
    sort_by: str,
) -> Dict[str, Any]:
    return build_process_console_view_data(
        runtime_root,
        asset_id=asset_id,
        sort_by=sort_by,
    )


def _build_controlled_live_unavailable_payload(
    *,
    requested_asset_id: Optional[str],
) -> Dict[str, Any]:
    selection_notice = (
        f"live source unavailable / requested asset '{requested_asset_id}' not checked"
        if requested_asset_id
        else "live source unavailable / no current shown asset"
    )
    return {
        "state": "live_unavailable",
        "live_availability": "live_unavailable",
        "source_kind": "process_console_payload",
        "selection_query_state": "no_selected_asset",
        "requested_asset_id": requested_asset_id,
        "selected_asset_id": None,
        "selection_notice": selection_notice,
        "compare_mode": None,
        "available_assets": [],
        "pageTitle": "operating ui live unavailable",
        "page_fallback_message": "live source unavailable",
        "strip": None,
        "board": {"state": "empty", "items": [], "emptyLabel": "live source unavailable"},
        "detail_summary": {"state": "no_selected_asset", "helperText": "live source unavailable"},
        "activity": {"state": "history_unavailable", "items": [], "emptyLabel": "history unavailable"},
        "adapted_model": None,
        "process_console_summary": {},
        "debug_text": {},
    }


def _resolve_validation_overrides(
    *,
    live_mode: Optional[str],
    compare_mode: Optional[str],
) -> Dict[str, Optional[str]]:
    return {
        "live_mode": _normalize_live_mode(live_mode),
        "compare_mode": _normalize_compare_mode(compare_mode),
    }


def _normalize_live_mode(value: Optional[str]) -> Optional[str]:
    if value == "unavailable":
        return value
    return None


def _normalize_compare_mode(value: Optional[str]) -> Optional[str]:
    if value in {"empty", "no_selected", "state_unavailable"}:
        return value
    return None


def _build_compare_panel_with_validation(
    *,
    compare_mode: Optional[str],
    selected_asset: Optional[Dict[str, Any]],
    compare_candidates: Optional[list[Dict[str, Any]]],
    live_availability: str,
    guards: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    resolved = _resolve_compare_panel_validation(
        compare_mode=compare_mode,
        selected_asset=selected_asset,
        compare_candidates=compare_candidates,
        live_availability=live_availability,
        guards=guards,
    )
    return build_compare_candidate_panel_view(
        selectedAsset=resolved["selected_asset"],
        compareCandidates=resolved["compare_candidates"],
        liveAvailability=resolved["live_availability"],
        guards=resolved["guards"],
    )


def _resolve_compare_panel_validation(
    *,
    compare_mode: Optional[str],
    selected_asset: Optional[Dict[str, Any]],
    compare_candidates: Optional[list[Dict[str, Any]]],
    live_availability: str,
    guards: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    return {
        "selected_asset": _resolve_compare_panel_selected_asset(
            compare_mode=compare_mode,
            selected_asset=selected_asset,
        ),
        "compare_candidates": _resolve_compare_panel_candidates(
            compare_mode=compare_mode,
            compare_candidates=compare_candidates,
        ),
        "live_availability": _resolve_compare_panel_live_availability(
            compare_mode=compare_mode,
            live_availability=live_availability,
        ),
        "guards": _resolve_compare_panel_guards(
            compare_mode=compare_mode,
            guards=guards,
        ),
    }


def _resolve_compare_panel_selected_asset(
    *,
    compare_mode: Optional[str],
    selected_asset: Optional[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    if compare_mode in {"no_selected", "state_unavailable"}:
        return None
    return selected_asset


def _resolve_compare_panel_candidates(
    *,
    compare_mode: Optional[str],
    compare_candidates: Optional[list[Dict[str, Any]]],
) -> Optional[list[Dict[str, Any]]]:
    if compare_mode == "empty":
        return []
    return compare_candidates


def _resolve_compare_panel_live_availability(
    *,
    compare_mode: Optional[str],
    live_availability: str,
) -> str:
    return live_availability


def _resolve_compare_panel_guards(
    *,
    compare_mode: Optional[str],
    guards: Optional[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    guard_state = dict(guards or {})
    if compare_mode == "state_unavailable":
        guard_state["stateUnavailable"] = True
    return guard_state
