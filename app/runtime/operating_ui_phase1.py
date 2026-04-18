from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import copy
import json

from app.runtime.file_store import JsonlEventStore
from app.runtime.operating_ui_phase1_adapter import adapt_runtime_payload_to_phase1_view_model
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data

WHY_MODES = [
    "relation_found",
    "perspective_shift",
    "resonance",
    "keep_for_later",
    "unclear_but_hold",
]


def build_operating_ui_phase1_shell_data(
    runtime_root: Path,
    *,
    asset_id: Optional[str] = None,
    sort_by: str = "updated_at",
    live_mode: Optional[str] = None,
    compare_mode: Optional[str] = None,
    history_snapshot_ref: Optional[str] = None,
    history_cluster_ref: Optional[str] = None,
    history_trace_ref: Optional[str] = None,
    history_reread_summary: Optional[str] = None,
    history_source_note: Optional[str] = None,
) -> Dict[str, Any]:
    live_data = build_operating_ui_live_composition_data(
        runtime_root,
        asset_id=asset_id,
        sort_by=sort_by,
        live_mode=live_mode,
        compare_mode=compare_mode,
    )
    memory_stickers = load_phase1_memory_stickers(runtime_root)
    path_residue = load_phase1_path_residue(runtime_root)
    runtime_binding = adapt_runtime_payload_to_phase1_view_model(
        live_data,
        memory_stickers=memory_stickers,
        path_residue=path_residue,
    )
    objects = (runtime_binding.get("explore_binding") or {}).get("objects") or []
    lenses = _build_lens_options()
    positions_by_lens = _build_position_options()
    quick_start_object_id = live_data.get("selected_asset_id") or (objects[0]["id"] if objects else None)
    quick_start_lens_id = lenses[0]["id"] if lenses else None
    quick_start_position_value = (
        positions_by_lens.get(quick_start_lens_id, [{}])[0].get("id")
        if quick_start_lens_id and positions_by_lens.get(quick_start_lens_id)
        else None
    )
    quick_start_preview = _build_preview_connection(
        quick_start_object_id,
        quick_start_lens_id,
        quick_start_position_value,
        objects,
        lenses,
        positions_by_lens,
    )
    return {
        "state": live_data.get("state"),
        "pageTitle": "main operating set",
        "live_data": live_data,
        "phase1_shell": {
            "surfaces": ["Operating", "Explore", "Search", "Memory", "Similar"],
            "objects": objects,
            "lenses": lenses,
            "positions_by_lens": positions_by_lens,
            "why_modes": [{"id": mode, "label": mode.replace("_", " ")} for mode in WHY_MODES],
            "memory_stickers": memory_stickers,
            "recent_sticker": memory_stickers[0] if memory_stickers else None,
            "path_residue": path_residue,
            "runtime_binding": runtime_binding,
            "history_reread_context": _build_history_reread_context(
                asset_id=asset_id,
                history_snapshot_ref=history_snapshot_ref,
                history_cluster_ref=history_cluster_ref,
                history_trace_ref=history_trace_ref,
                history_reread_summary=history_reread_summary,
                history_source_note=history_source_note,
            ),
            "quick_start_suggestion": {
                "object_id": quick_start_object_id,
                "lens_id": quick_start_lens_id,
                "position_value": quick_start_position_value,
                "preview_connection": quick_start_preview,
            },
            "shared_spine": {
                "selected_object_id": None,
                "selected_lens_id": None,
                "selected_position_value": None,
                "current_preview_connection": None,
                "selected_memory_sticker_id": None,
                "similar_seed_ref": None,
            },
        },
    }


def create_phase1_memory_sticker(
    runtime_root: Path,
    *,
    object_id: str,
    lens_id: str,
    position_value: str,
    preview_connection_summary: str,
    why_selected_short: Optional[str] = None,
    why_mode: Optional[str] = None,
    optional_note: Optional[str] = None,
    seed_ref: Optional[str] = None,
) -> Dict[str, str]:
    preview_summary = (preview_connection_summary or "").strip()
    if not object_id or not lens_id or not position_value or not preview_summary:
        raise ValueError("object_id, lens_id, position_value, and preview_connection_summary are required")
    normalized_mode = _normalize_why_mode(why_mode)
    normalized_short = (why_selected_short or _default_why_selected_short(normalized_mode)).strip()
    normalized_note = (optional_note or "").strip()
    combined_why = normalized_short
    if normalized_note:
        combined_why = f"{normalized_short} / {normalized_note}"
    record = {
        "sticker_id": f"stk_{_slug(object_id)}_{_slug(lens_id)}_{_slug(position_value)}_{int(datetime.now(timezone.utc).timestamp())}",
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "object_id": object_id.strip(),
        "lens_id": lens_id.strip(),
        "position_value": position_value.strip(),
        "preview_connection_summary": preview_summary,
        "why_selected": combined_why,
        "why_selected_short": normalized_short,
        "why_mode": normalized_mode,
        "optional_note": normalized_note,
        "seed_ref": (seed_ref or preview_summary).strip(),
    }
    _phase1_memory_store(runtime_root).append(record)
    return record


def save_phase1_path_residue(
    runtime_root: Path,
    *,
    object_id: Optional[str],
    lens_id: Optional[str],
    position_value: Optional[str],
    preview_ready: bool,
) -> Dict[str, Any]:
    payload = {
        "object_id": (object_id or "").strip(),
        "lens_id": (lens_id or "").strip(),
        "position_value": (position_value or "").strip(),
        "preview_ready": bool(preview_ready),
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path = _phase1_path_residue_file(runtime_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def load_phase1_path_residue(runtime_root: Path) -> Optional[Dict[str, Any]]:
    path = _phase1_path_residue_file(runtime_root)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(payload, dict):
        return None
    return {
        "object_id": str(payload.get("object_id") or "").strip(),
        "lens_id": str(payload.get("lens_id") or "").strip(),
        "position_value": str(payload.get("position_value") or "").strip(),
        "preview_ready": bool(payload.get("preview_ready")),
        "updated_at": str(payload.get("updated_at") or "").strip(),
    }


def load_phase1_memory_stickers(runtime_root: Path) -> List[Dict[str, str]]:
    rows = _phase1_memory_store(runtime_root).read_all()
    normalized: List[Dict[str, str]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        sticker_id = str(row.get("sticker_id") or "").strip()
        if not sticker_id:
            continue
        why_mode = _normalize_legacy_why_mode(row)
        why_short = _normalize_legacy_why_selected_short(row, why_mode)
        optional_note = _normalize_legacy_optional_note(row, why_short)
        why_selected = str(row.get("why_selected") or "").strip()
        if not why_selected:
            why_selected = why_short
            if optional_note:
                why_selected = f"{why_short} / {optional_note}"
        normalized.append(
            {
                "sticker_id": sticker_id,
                "created_at": str(row.get("created_at") or "").strip(),
                "object_id": str(row.get("object_id") or "").strip(),
                "lens_id": str(row.get("lens_id") or "").strip(),
                "position_value": str(row.get("position_value") or "").strip(),
                "preview_connection_summary": str(row.get("preview_connection_summary") or "").strip(),
                "why_selected": why_selected,
                "why_selected_short": why_short,
                "why_mode": why_mode,
                "optional_note": optional_note,
                "seed_ref": str(row.get("seed_ref") or "").strip(),
            }
        )
    normalized.sort(key=lambda item: item.get("created_at") or "", reverse=True)
    return normalized


def render_operating_ui_phase1_shell_html(
    data: Dict[str, Any] | None = None,
    api_path: str = "/api/operating-ui-phase1",
) -> str:
    payload_block = (
        f'<script id="operating-ui-phase1-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('operating-ui-phase1-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>main operating set</title>
  <style>
    :root {
      --bg: #f4efe7;
      --panel: #fffaf2;
      --line: #d7cab7;
      --line-strong: #8b6b44;
      --text: #1f2937;
      --muted: #6b7280;
      --ink: #5b422a;
      --chip: #efe5d3;
      --accent: #efe2c2;
      --accent-strong: #7a5631;
      --shadow: 0 12px 30px rgba(91, 66, 42, 0.08);
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: radial-gradient(circle at top, #fbf6ee 0%, var(--bg) 55%, #efe7d8 100%); color: var(--text); font-family: Georgia, serif; }
    .page { max-width: 1500px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 20px; padding: 16px; box-shadow: var(--shadow); }
    .top { display: grid; gap: 12px; }
    .nav-row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .nav { display: inline-flex; align-items: center; gap: 6px; padding: 8px 12px; border-radius: 999px; border: 1px solid var(--line); text-decoration: none; color: var(--ink); background: #fff; }
    .title { display: grid; gap: 6px; }
    .title strong { font-size: 24px; }
    .meta { color: var(--muted); font-size: 13px; }
    .surface-tabs { display: flex; flex-wrap: wrap; gap: 8px; }
    .tab { border: 1px solid var(--line); background: #fff; color: var(--ink); border-radius: 999px; padding: 8px 14px; cursor: pointer; font: inherit; }
    .tab.active { background: var(--accent); border-color: var(--line-strong); color: #3f2a13; }
    .shell-layout { display: grid; grid-template-columns: minmax(260px, 320px) minmax(0, 1fr); gap: 16px; align-items: start; }
    .spine-card { display: grid; gap: 10px; }
    .spine-row { display: grid; gap: 4px; padding: 10px; border-radius: 14px; border: 1px solid #eadfcf; background: #fff; }
    .spine-row strong { color: var(--ink); font-size: 13px; }
    .spine-row span { color: var(--muted); font-size: 13px; }
    .surface { display: none; gap: 14px; }
    .surface.active { display: grid; }
    .surface-head { display: grid; gap: 6px; }
    .surface-grid { display: grid; grid-template-columns: minmax(220px, 320px) minmax(0, 1fr); gap: 14px; align-items: start; }
    .stack { display: grid; gap: 12px; }
    .subpanel { border: 1px solid #eadfcf; background: #fff; border-radius: 16px; padding: 14px; }
    .subpanel h3 { margin: 0 0 8px 0; font-size: 17px; color: var(--ink); }
    .subhead { color: var(--muted); font-size: 13px; margin-bottom: 10px; }
    .list { display: grid; gap: 8px; }
    .token, .action, .mode-button { width: 100%; text-align: left; border: 1px solid var(--line); background: #fff; color: var(--text); border-radius: 14px; padding: 10px 12px; cursor: pointer; font: inherit; }
    .token.active, .action.active, .mode-button.active { border-color: var(--line-strong); background: var(--accent); color: #352211; }
    .action:disabled { opacity: 0.55; cursor: not-allowed; }
    .token small, .action small, .mode-button small { display: block; color: var(--muted); margin-top: 3px; }
    .preview-card { display: grid; gap: 8px; padding: 14px; border-radius: 18px; background: linear-gradient(180deg, #fff9ef 0%, #f9f0df 100%); border: 1px solid #e6d5b8; }
    .preview-title { font-size: 18px; color: #3f2a13; }
    .preview-note { color: var(--muted); font-size: 13px; }
    .empty { color: #8b7355; font-style: italic; }
    .result-card { display: grid; gap: 6px; padding: 12px; border: 1px solid #eadfcf; background: #fff; border-radius: 16px; }
    .result-card strong { color: var(--ink); }
    .result-card .meta { font-size: 12px; }
    .btn-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .primary { background: var(--accent); border-color: var(--line-strong); color: #3f2a13; }
    .secondary { background: #fff; }
    .search-box, .note-box { width: 100%; border-radius: 14px; border: 1px solid var(--line); padding: 12px; font: inherit; background: #fff; color: var(--text); }
    .search-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .pill { display: inline-flex; align-items: center; gap: 6px; border-radius: 999px; padding: 3px 9px; background: #f0eadf; color: var(--ink); font-size: 12px; }
    .pill.live { background: #e7f1e7; color: #35553a; }
    .pill.fallback { background: #f5ead8; color: #7b5b2d; }
    .pill.stored { background: #ece7f6; color: #51446f; }
    .pill.degraded { background: #f7e6e2; color: #7a4338; }
    .chip-button { border: 1px solid var(--line); background: #fff; color: var(--ink); border-radius: 999px; padding: 7px 11px; cursor: pointer; font: inherit; }
    .chip-button.active { background: var(--accent); border-color: var(--line-strong); color: #352211; }
    .chip-button.subtle { background: #faf6ef; }
    .status-strip { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 8px; margin: 10px 0; }
    .status-card { border: 1px solid #eadfcf; background: #fff; border-radius: 14px; padding: 10px; display: grid; gap: 4px; }
    .status-card strong { font-size: 12px; color: var(--ink); }
    .status-card span { font-size: 12px; color: var(--muted); }
    .status-card.ready { background: #f7f0e2; border-color: #d8bf94; }
    .status-card.missing { background: #fffaf5; border-color: #e7d8c0; }
    .soft-note { color: var(--muted); font-size: 12px; }
    .callout { border: 1px dashed #d6c2a0; background: #fff8ed; color: var(--ink); border-radius: 14px; padding: 10px 12px; font-size: 13px; }
    .page-map { display: grid; gap: 8px; margin-top: 8px; }
    .page-map-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .map-chip { display: inline-flex; align-items: center; gap: 6px; border-radius: 999px; padding: 6px 10px; border: 1px solid var(--line); background: #fff; color: var(--ink); font-size: 12px; }
    .map-chip.companion { background: #faf4ea; border-style: dashed; }
    .modal-backdrop { position: fixed; inset: 0; background: rgba(32, 24, 12, 0.42); display: none; align-items: center; justify-content: center; padding: 20px; }
    .modal-backdrop.open { display: flex; }
    .modal { max-width: 760px; width: 100%; background: var(--panel); border: 1px solid var(--line); border-radius: 22px; box-shadow: 0 24px 80px rgba(0,0,0,0.22); padding: 20px; display: grid; gap: 12px; }
    pre { margin: 0; white-space: pre-wrap; word-break: break-word; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: #304050; background: #fff; border: 1px solid #eadfcf; border-radius: 14px; padding: 12px; }
    @media (max-width: 980px) {
      .shell-layout, .surface-grid, .search-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  """ + payload_block + """
  <div id="app"></div>
  <div id="modal-backdrop" class="modal-backdrop">
    <div class="modal">
      <div class="btn-row"><button id="modal-close" class="action secondary">close detail</button></div>
      <div id="modal-content"></div>
    </div>
  </div>
  <script>
    (async () => {
      """ + bootstrap + """
      const app = document.getElementById('app');
      const shell = data.phase1_shell || {};
      const live = data.live_data || {};
      const objects = shell.objects || [];
      const lenses = shell.lenses || [];
      const whyModes = shell.why_modes || [];
      const positionsByLens = shell.positions_by_lens || {};
      const runtimeBinding = shell.runtime_binding || {};
      const operatingObservation = runtimeBinding.operating_observation || {};
      const multiLensObservation = operatingObservation.multi_lens_supervisor_surface || {};
      const exploreBinding = runtimeBinding.explore_binding || {};
      const searchBinding = runtimeBinding.search_binding || {};
      const memoryBinding = runtimeBinding.memory_binding || {};
      const similarBinding = runtimeBinding.similar_binding || {};
      const sourceMap = runtimeBinding.source_map || {};
      const pathResidue = shell.path_residue || null;
      const initialHistoryRereadContext = shell.history_reread_context || null;
      const quickStartSuggestion = shell.quick_start_suggestion || null;
      const modalBackdrop = document.getElementById('modal-backdrop');
      const modalContent = document.getElementById('modal-content');
      document.getElementById('modal-close').addEventListener('click', () => modalBackdrop.classList.remove('open'));
      modalBackdrop.addEventListener('click', (event) => {
        if (event.target === modalBackdrop) modalBackdrop.classList.remove('open');
      });

      const page = document.createElement('div');
      page.className = 'page';
      const top = document.createElement('div');
      top.className = 'panel top';
      const navRow = document.createElement('div');
      navRow.className = 'nav-row';
      navRow.innerHTML = `<a class="nav" href="/process-console">process-console</a>
        <a class="nav" href="/operating-ui-live">operating live</a>
        <a class="nav" href="/operating-ui-phase1">main operating set</a>`;
      top.appendChild(navRow);
      const title = document.createElement('div');
      title.className = 'title';
      title.innerHTML = `<strong>${data.pageTitle || 'main operating set'}</strong>
        <div class="meta">core pages / state=${live.state || 'unknown'} / selected=${live.selected_asset_id || 'none'} / availability=${live.live_availability || 'unknown'}</div>
        <div class="meta">Operating / Explore / Search / Memory / Similar</div>`;
      const pageMap = document.createElement('div');
      pageMap.className = 'page-map';
      pageMap.innerHTML = `<div class="page-map-row">
        <span class="map-chip">Operating: observe now</span>
        <span class="map-chip">Explore: build path</span>
        <span class="map-chip">Search: direct access</span>
        <span class="map-chip">Memory: saved paths</span>
        <span class="map-chip">Similar: local re-query</span>
      </div>
      <div class="page-map-row">
        <a class="map-chip companion" href="/operating-ui-history">History Companion: time-axis read</a>
      </div>`;
      title.appendChild(pageMap);
      top.appendChild(title);
      page.appendChild(top);

      const spine = Object.assign({}, shell.shared_spine || {});
      let activeSurface = 'Operating';
      let searchQuery = '';
      let lastSearchQuery = '';
      let lastSearchDirectHits = 0;
      let currentJumpTargetHint = 'none';
      let memoryStickers = (shell.memory_stickers || []).slice();
      let pathState = 'blank';
      let importContext = null;
      let historyRereadContext = initialHistoryRereadContext;
      let stickerDraft = {
        why_mode: whyModes[0] ? whyModes[0].id : 'keep_for_later',
        why_selected_short: 'keep this path for later rereading',
        optional_note: '',
      };
      let residueState = pathResidue;

      function getObjectById(id) { return objects.find((item) => item.id === id) || null; }
      function getLensById(id) { return lenses.find((item) => item.id === id) || null; }
      function getPositionList(lensId) { return positionsByLens[lensId] || []; }
      function getPositionById(lensId, id) { return getPositionList(lensId).find((item) => item.id === id) || null; }
      function buildStarterObjects() {
        const preferred = [];
        const selected = getObjectById(live.selected_asset_id);
        if (selected) preferred.push(selected);
        objects.forEach((item) => {
          if (preferred.find((candidate) => candidate.id === item.id)) return;
          if (preferred.length < 5) preferred.push(item);
        });
        return preferred.slice(0, 5);
      }
      function buildPreviewConnection(objectId, lensId, positionId) {
        const objectItem = getObjectById(objectId);
        const lensItem = getLensById(lensId);
        const positionItem = getPositionById(lensId, positionId);
        if (!objectItem || !lensItem || !positionItem) return null;
        return {
          id: `preview:${objectItem.id}:${lensItem.id}:${positionItem.id}`,
          object_id: objectItem.id,
          lens_id: lensItem.id,
          position_value: positionItem.id,
          label: `${objectItem.label} -> ${lensItem.label} -> ${positionItem.label}`,
          preview_note: `${lensItem.note} / ${positionItem.note}`,
        };
      }
      function syncCurrentPreview() {
        spine.current_preview_connection = buildPreviewConnection(
          spine.selected_object_id,
          spine.selected_lens_id,
          spine.selected_position_value
        );
      }
      async function persistPathResidue() {
        const payload = {
          object_id: spine.selected_object_id || '',
          lens_id: spine.selected_lens_id || '',
          position_value: spine.selected_position_value || '',
          preview_ready: !!spine.current_preview_connection,
        };
        const response = await fetch('/api/operating-ui-phase1/path-residue', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        if (!response.ok) return null;
        residueState = await response.json();
        shell.path_residue = residueState;
        return residueState;
      }
      function selectExplorePath(objectId, lensId, positionId) {
        if (objectId !== undefined) spine.selected_object_id = objectId;
        if (lensId !== undefined) spine.selected_lens_id = lensId;
        if (positionId !== undefined) spine.selected_position_value = positionId;
        syncCurrentPreview();
        pathState = 'manually progressed';
        persistPathResidue();
        render();
      }
      function setImportContext(source, destination, summary) {
        importContext = { source, destination, summary };
      }
      function clearImportContext() {
        importContext = null;
        currentJumpTargetHint = 'none';
        render();
      }
      function clearHistoryRereadContext() {
        historyRereadContext = null;
        render();
      }
      function clearActiveSeed() {
        spine.similar_seed_ref = null;
        if (importContext && importContext.destination === 'Similar') {
          importContext = null;
        }
        render();
      }
      function applyQuickStartPath() {
        if (!quickStartSuggestion) return;
        spine.selected_object_id = quickStartSuggestion.object_id || null;
        spine.selected_lens_id = quickStartSuggestion.lens_id || null;
        spine.selected_position_value = quickStartSuggestion.position_value || null;
        syncCurrentPreview();
        pathState = 'quick-start applied';
        setImportContext('Explore quick-start', 'Explore', 'quick-start path applied');
        persistPathResidue();
        render();
      }
      function resetToBlankPath() {
        spine.selected_object_id = null;
        spine.selected_lens_id = null;
        spine.selected_position_value = null;
        syncCurrentPreview();
        pathState = 'blank';
        if (importContext && importContext.destination === 'Explore') {
          importContext = null;
        }
        persistPathResidue();
        render();
      }
      function restoreResiduePath() {
        if (!residueState) return;
        spine.selected_object_id = residueState.object_id || null;
        spine.selected_lens_id = residueState.lens_id || null;
        spine.selected_position_value = residueState.position_value || null;
        syncCurrentPreview();
        pathState = 'residue restored';
        setImportContext('Residue', 'Explore', 'resumed from residue');
        render();
      }
      function getSelectedSticker() {
        return memoryStickers.find((item) => item.sticker_id === spine.selected_memory_sticker_id) || null;
      }
      function buildCurrentPathSummary() {
        const objectItem = getObjectById(spine.selected_object_id);
        const lensItem = getLensById(spine.selected_lens_id);
        const positionItem = getPositionById(spine.selected_lens_id, spine.selected_position_value);
        const parts = [
          objectItem ? objectItem.label : 'blank',
          lensItem ? lensItem.label : 'blank',
          positionItem ? positionItem.label : 'blank',
        ];
        const ready = !!spine.current_preview_connection;
        return {
          summary: parts.join(' -> '),
          status: ready ? 'preview ready' : 'preview incomplete',
        };
      }
      function buildPathStatusRows() {
        const objectItem = getObjectById(spine.selected_object_id);
        const lensItem = getLensById(spine.selected_lens_id);
        const positionItem = getPositionById(spine.selected_lens_id, spine.selected_position_value);
        const previewReady = !!spine.current_preview_connection;
        return [
          { key: 'object', label: 'object', value: objectItem ? objectItem.label : 'missing', ready: !!objectItem },
          { key: 'lens', label: 'lens', value: lensItem ? lensItem.label : 'missing', ready: !!lensItem },
          { key: 'position', label: 'position', value: positionItem ? positionItem.label : 'missing', ready: !!positionItem },
          { key: 'preview', label: 'preview', value: previewReady ? 'ready' : 'incomplete', ready: previewReady },
          { key: 'sticker', label: 'sticker', value: previewReady ? 'can be saved' : 'not eligible yet', ready: previewReady },
        ];
      }
      function getNextIncompleteStep() {
        if (!spine.selected_object_id) return 'object';
        if (!spine.selected_lens_id) return 'lens';
        if (!spine.selected_position_value) return 'position';
        if (!spine.current_preview_connection) return 'preview';
        return 'sticker';
      }
      function getPathStateLabel() {
        if (!spine.selected_object_id && !spine.selected_lens_id && !spine.selected_position_value) return 'blank';
        return pathState;
      }
      function hasResumableResidue() {
        return !!(residueState && (residueState.object_id || residueState.lens_id || residueState.position_value));
      }
      function renderAvailabilityPill(label) {
        const normalized = (label || '').toLowerCase();
        let tone = 'fallback';
        if (normalized.includes('live')) tone = 'live';
        else if (normalized.includes('stored')) tone = 'stored';
        else if (normalized.includes('degraded')) tone = 'degraded';
        return `<span class="pill ${tone}">${label || 'fallback'}</span>`;
      }
      function getStickerSaveReason() {
        if (!spine.selected_object_id) return 'choose object first';
        if (!spine.selected_lens_id) return 'choose lens first';
        if (!spine.selected_position_value) return 'choose position first';
        if (!spine.current_preview_connection) return 'preview becomes available after object + lens + position';
        return '';
      }
      function openDetail(title, payload) {
        modalContent.innerHTML = `<h3>${title}</h3><pre>${payload}</pre>`;
        modalBackdrop.classList.add('open');
      }
      async function saveSticker(payload, nextSurface) {
        const response = await fetch('/api/operating-ui-phase1/stickers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        if (!response.ok) {
          openDetail('sticker save failed', await response.text());
          return null;
        }
        const sticker = await response.json();
        memoryStickers = [sticker].concat(memoryStickers.filter((item) => item.sticker_id !== sticker.sticker_id));
        shell.recent_sticker = sticker;
        spine.selected_memory_sticker_id = sticker.sticker_id;
        if (nextSurface === 'Memory') {
          setImportContext('Explore', 'Memory', 'explicit sticker saved');
        }
        if (nextSurface) activeSurface = nextSurface;
        return sticker;
      }
      async function promoteCurrentPreviewToSticker() {
        if (!spine.current_preview_connection) return;
        const preview = spine.current_preview_connection;
        if (memoryStickers.some((item) => item.preview_connection_summary === preview.label)) {
          activeSurface = 'Memory';
          render();
          return;
        }
        const sticker = await saveSticker(
          {
            object_id: preview.object_id,
            lens_id: preview.lens_id,
            position_value: preview.position_value,
            preview_connection_summary: preview.label,
            why_selected_short: stickerDraft.why_selected_short,
            why_mode: stickerDraft.why_mode,
            optional_note: stickerDraft.optional_note,
            seed_ref: preview.label,
          },
          'Memory'
        );
        if (sticker) render();
      }
      function buildSearchIndex() {
        return {
          object: objects.map((item) => ({ type: 'object', id: item.id, label: item.label, note: item.note })),
          lens: lenses.map((item) => ({ type: 'lens', id: item.id, label: item.label, note: item.note })),
          position: Object.values(positionsByLens).flat().map((item) => ({ type: 'position', id: item.id, label: item.label, note: item.note })),
          connection: memoryStickers.map((item) => ({
            type: 'connection',
            id: `${item.sticker_id}:connection`,
            label: item.preview_connection_summary,
            note: item.why_selected_short || item.why_selected,
          })),
          memory: memoryStickers.map((item) => ({
            type: 'memory',
            id: item.sticker_id,
            label: item.preview_connection_summary,
            note: item.why_selected_short || item.why_selected,
          })),
        };
      }
      function buildThinMatchMeta(objectItem, sticker, index) {
        const objectTokens = `${objectItem.id} ${objectItem.label}`.toLowerCase();
        const matchedOn = [];
        if (objectTokens.includes((sticker.lens_id || '').toLowerCase())) matchedOn.push('same lens');
        if (objectTokens.includes((sticker.position_value || '').toLowerCase())) matchedOn.push('same position');
        const previewTerms = (sticker.preview_connection_summary || '').toLowerCase().split(/[^a-z0-9가-힣_]+/).filter(Boolean);
        if (previewTerms.some((term) => term.length > 2 && objectTokens.includes(term))) matchedOn.push('shared preview term');
        if (!matchedOn.length) matchedOn.push('object token proximity');
        const traceSummary = matchedOn[0] === 'object token proximity'
          ? (index === 0 ? 'kept as nearest local match around the seed path' : 'low-confidence thin match around the seed path')
          : `touches seed through ${matchedOn.join(' + ')}`;
        return {
          matched_on: matchedOn.slice(0, 3),
          trace_summary: traceSummary,
          confidence_style: index === 0 ? 'thin-match' : (matchedOn.length > 1 ? 'partial-overlap' : 'low-confidence'),
        };
      }
      function formatWhyMode(mode) {
        return (mode || 'keep_for_later').replaceAll('_', ' ');
      }
      function buildSimilarResults() {
        const sticker = getSelectedSticker() || memoryStickers.find((item) => item.seed_ref === spine.similar_seed_ref) || memoryStickers[0] || null;
        if (!sticker) return [];
        return objects
          .filter((item) => item.id !== sticker.object_id)
          .slice(0, 4)
          .map((item, index) => {
            const trace = buildThinMatchMeta(item, sticker, index);
            return {
              id: `similar:${sticker.sticker_id}:${item.id}:${index}`,
              object_id: item.id,
              lens_id: sticker.lens_id,
              position_value: sticker.position_value,
              title: `${item.label} with ${sticker.preview_connection_summary}`,
            note: 'local re-query output / not recommendation / not ranked answer',
              matched_on: trace.matched_on,
              trace_summary: trace.trace_summary,
              confidence_style: trace.confidence_style,
              seed_ref: sticker.seed_ref || sticker.sticker_id,
            };
          });
      }
      async function promoteSimilarResult(result) {
        const sticker = await saveSticker(
          {
            object_id: result.object_id,
            lens_id: result.lens_id,
            position_value: result.position_value,
            preview_connection_summary: result.title,
            why_selected_short: stickerDraft.why_selected_short,
            why_mode: stickerDraft.why_mode,
            optional_note: stickerDraft.optional_note || `selected again after local similarity re-query / ${result.trace_summary}`,
            seed_ref: result.seed_ref,
          },
          'Memory'
        );
        if (sticker) render();
      }
      function buildSearchGroups(queryText) {
        const normalizedQuery = (queryText || '').trim().toLowerCase();
        const groups = {
          objects: [],
          lenses: [],
          positions: [],
          stickers: [],
          seed_relevant: [],
        };
        if (!normalizedQuery) {
          return { groups, direct_hits: 0, partial_hits: 0 };
        }
        let directHits = 0;
        let partialHits = 0;
        function classifyMatch(directFields, partialFields) {
          const directField = (directFields || []).find((value) => (value || '').toLowerCase().includes(normalizedQuery));
          if (directField) return { level: 'direct', matched_in: directField };
          const partialField = (partialFields || []).find((value) => (value || '').toLowerCase().includes(normalizedQuery));
          if (partialField) return { level: 'partial', matched_in: partialField };
          return null;
        }
        objects.forEach((item) => {
          const match = classifyMatch(['object id', 'object label'], [item.note ? 'object note' : ''].filter(Boolean));
          const hayId = `${item.id}`.toLowerCase();
          const hayLabel = `${item.label}`.toLowerCase();
          const hayNote = `${item.note || ''}`.toLowerCase();
          const actual = hayId.includes(normalizedQuery) ? { level: 'direct', matched_in: 'object id' }
            : hayLabel.includes(normalizedQuery) ? { level: 'direct', matched_in: 'object label' }
            : hayNote.includes(normalizedQuery) ? { level: 'partial', matched_in: 'object note' }
            : null;
          if (!actual) return;
          if (actual.level === 'direct') directHits += 1; else partialHits += 1;
          groups.objects.push({
            id: item.id,
            label: item.label,
            note: item.note,
            match_level: actual.level,
            matched_in: actual.matched_in,
            jump_target: 'Explore',
              on_jump: () => {
              selectExplorePath(item.id, undefined, undefined);
              activeSurface = 'Explore';
              currentJumpTargetHint = `Explore:${item.id}`;
              setImportContext('Search', 'Explore', `object import ${item.id}`);
              render();
            },
          });
        });
        lenses.forEach((item) => {
          const hayId = `${item.id}`.toLowerCase();
          const hayLabel = `${item.label}`.toLowerCase();
          const hayNote = `${item.note || ''}`.toLowerCase();
          const actual = hayId.includes(normalizedQuery) ? { level: 'direct', matched_in: 'lens id' }
            : hayLabel.includes(normalizedQuery) ? { level: 'direct', matched_in: 'lens label' }
            : hayNote.includes(normalizedQuery) ? { level: 'partial', matched_in: 'lens note' }
            : null;
          if (!actual) return;
          if (actual.level === 'direct') directHits += 1; else partialHits += 1;
          groups.lenses.push({
            id: item.id,
            label: item.label,
            note: item.note,
            match_level: actual.level,
            matched_in: actual.matched_in,
            jump_target: 'Explore',
            on_jump: () => {
              selectExplorePath(undefined, item.id, undefined);
              activeSurface = 'Explore';
              currentJumpTargetHint = `Explore:${item.id}`;
              setImportContext('Search', 'Explore', `lens import ${item.id}`);
              render();
            },
          });
        });
        Object.entries(positionsByLens).forEach(([lensId, positionItems]) => positionItems.forEach((item) => {
          const hayId = `${item.id}`.toLowerCase();
          const hayLabel = `${item.label}`.toLowerCase();
          const hayNote = `${item.note || ''}`.toLowerCase();
          const actual = hayId.includes(normalizedQuery) ? { level: 'direct', matched_in: 'position id' }
            : hayLabel.includes(normalizedQuery) ? { level: 'direct', matched_in: 'position label' }
            : hayNote.includes(normalizedQuery) ? { level: 'partial', matched_in: 'position note' }
            : null;
          if (!actual) return;
          if (actual.level === 'direct') directHits += 1; else partialHits += 1;
          groups.positions.push({
            id: item.id,
            label: item.label,
            note: item.note,
            lens_id: lensId,
            match_level: actual.level,
            matched_in: actual.matched_in,
            jump_target: 'Explore',
            on_jump: () => {
              selectExplorePath(undefined, lensId, item.id);
              activeSurface = 'Explore';
              currentJumpTargetHint = `Explore:${lensId}/${item.id}`;
              setImportContext('Search', 'Explore', `position import ${lensId}/${item.id}`);
              render();
            },
          });
        }));
        memoryStickers.forEach((item) => {
          const summary = `${item.preview_connection_summary || ''}`.toLowerCase();
          const whyShort = `${item.why_selected_short || ''}`.toLowerCase();
          const whyMode = `${item.why_mode || ''}`.toLowerCase();
          const actual = summary.includes(normalizedQuery) ? { level: 'direct', matched_in: 'sticker summary' }
            : whyShort.includes(normalizedQuery) ? { level: 'partial', matched_in: 'why_selected_short' }
            : whyMode.includes(normalizedQuery) ? { level: 'partial', matched_in: 'why_mode' }
            : null;
          if (!actual) return;
          if (actual.level === 'direct') directHits += 1; else partialHits += 1;
          groups.stickers.push({
            id: item.sticker_id,
            label: item.preview_connection_summary,
            note: item.why_selected_short || item.why_selected,
            match_level: actual.level,
            matched_in: actual.matched_in,
            jump_target: 'Memory',
            on_jump: () => {
              spine.selected_memory_sticker_id = item.sticker_id;
              activeSurface = 'Memory';
              currentJumpTargetHint = `Memory:${item.sticker_id}`;
              setImportContext('Search', 'Memory', `selected sticker ${item.sticker_id}`);
              render();
            },
          });
          groups.seed_relevant.push({
            id: `${item.sticker_id}:seed`,
            label: item.preview_connection_summary,
            note: 'related to saved path / seed-relevant only',
            match_level: actual.level,
            matched_in: actual.matched_in === 'sticker summary' ? 'saved path summary' : actual.matched_in,
            jump_target: 'Similar',
            on_jump: () => {
              spine.similar_seed_ref = item.seed_ref || item.sticker_id;
              activeSurface = 'Similar';
              currentJumpTargetHint = `Similar:${item.sticker_id}`;
              setImportContext('Search', 'Similar', `seed import ${item.sticker_id}`);
              render();
            },
          });
        });
        return { groups, direct_hits: directHits, partial_hits: partialHits };
      }
      function renderSpineSidebar() {
        const sidebar = document.createElement('div');
        sidebar.className = 'panel spine-card';
        sidebar.innerHTML = '<strong>Shared Interaction Spine</strong><div class="meta">Explore owns current path / Memory owns selected sticker / Similar owns active seed / Search only offers explicit jumps</div>';
        [
          ['selected_object_id', spine.selected_object_id],
          ['selected_lens_id', spine.selected_lens_id],
          ['selected_position_value', spine.selected_position_value],
          ['current_preview_connection', spine.current_preview_connection ? spine.current_preview_connection.label : null],
          ['selected_memory_sticker_id', spine.selected_memory_sticker_id],
          ['similar_seed_ref', spine.similar_seed_ref],
        ].forEach(([key, value]) => {
          const row = document.createElement('div');
          row.className = 'spine-row';
          row.innerHTML = `<strong>${key}</strong><span>${value || 'none'}</span>`;
          sidebar.appendChild(row);
        });
        return sidebar;
      }
      function renderTabs() {
        const wrap = document.createElement('div');
        wrap.className = 'panel tabs-shell';
        const row = document.createElement('div');
        row.className = 'surface-tabs';
        (shell.surfaces || []).forEach((label) => {
          const tab = document.createElement('button');
          tab.className = 'tab' + (activeSurface === label ? ' active' : '');
          tab.textContent = label;
          tab.addEventListener('click', () => {
            activeSurface = label;
            render();
          });
          row.appendChild(tab);
        });
        wrap.appendChild(row);
        return wrap;
      }
      function renderOperatingSurface(container) {
        const surface = document.createElement('div');
        surface.className = 'surface' + (activeSurface === 'Operating' ? ' active' : '');
        surface.innerHTML = `<div class="surface-head"><strong>Operating</strong><div class="meta">readiness -> line status -> observation -> boundary -> close-out</div></div>`;
        const grid = document.createElement('div');
        grid.className = 'surface-grid';
        const left = document.createElement('div');
        left.className = 'stack';
        const readiness = document.createElement('div');
        readiness.className = 'subpanel';
        const currentRunAvailable = (sourceMap.operating_current_run || {}).state === 'available';
        const observationReadyState = multiLensObservation.state === 'available'
          ? ((multiLensObservation.readings || []).length ? 'ready' : 'partially ready')
          : 'unavailable';
        const linkedReadinessLabel = multiLensObservation.state === 'available'
          ? (((multiLensObservation.readings || []).length ? 'direct linked observation available' : 'linked artifact available but surfaced readings are empty'))
          : 'linked observation not attached in current payload';
        readiness.innerHTML = `<h3>Input Readiness</h3><div class="subhead">check whether material is ready, partially ready, or unavailable before reading observation output</div><div class="chip-row">${renderAvailabilityPill(operatingObservation.provenance_summary || 'degraded observation fallback')}${renderAvailabilityPill(currentRunAvailable ? 'live source visible' : 'live source degraded')}${renderAvailabilityPill(`readiness: ${observationReadyState}`)}</div><div class="meta">source handle=${operatingObservation.selected_asset_id || 'none'} / query state=${operatingObservation.selection_query_state || 'none'} / live availability=${operatingObservation.live_availability || 'unknown'}</div>`;
        readiness.innerHTML += `<div class="meta">direct field: current run source=${currentRunAvailable ? 'available' : 'degraded or unavailable'}</div>`;
        readiness.innerHTML += `<div class="meta">proxy field: split status=not attached in current payload</div>`;
        readiness.innerHTML += `<div class="meta">proxy field: linked status=${linkedReadinessLabel}</div>`;
        readiness.innerHTML += `<div class="meta">receipt / provenance pointer=${operatingObservation.provenance_summary || 'unknown'}</div>`;
        readiness.innerHTML += `<div class="meta">readiness reading=${observationReadyState} / observational only / not a decision or maturity permission</div>`;
        readiness.innerHTML += `<pre>${operatingObservation.current_run_text || 'current run source unavailable'}</pre>`;
        readiness.innerHTML += `<details><summary>selected asset + state</summary><pre>${operatingObservation.detail_summary_text || 'detail summary source unavailable'}</pre>${operatingObservation.source_notice ? `<div class="meta">${operatingObservation.source_notice}</div>` : '<div class="meta">no extra source notice</div>'}</details>`;
        left.appendChild(readiness);
        const lineStatusPanel = document.createElement('div');
        lineStatusPanel.className = 'subpanel';
        lineStatusPanel.innerHTML = '<h3>Line Status</h3><div class="subhead">read line operating state before reading surfaced observation</div>';
        if (multiLensObservation.state !== 'available') {
          lineStatusPanel.innerHTML += '<div class="empty">line status unavailable until multi-lens supervisor surface is available</div>';
        } else {
          const lineStates = multiLensObservation.line_states || {};
          const parkedAxes = multiLensObservation.parked_axes || [];
          const activeLines = Object.entries(lineStates).filter(([, value]) => value === 'active').map(([key]) => key);
          const parkedLines = Object.entries(lineStates).filter(([, value]) => value === 'parked').map(([key]) => key);
          const candidateLines = Object.entries(lineStates).filter(([, value]) => value === 'candidate').map(([key]) => key);
          lineStatusPanel.innerHTML += `<div class="meta">active lines=${activeLines.join(', ') || 'none'}</div>`;
          lineStatusPanel.innerHTML += `<div class="meta">parked lines=${parkedLines.join(', ') || parkedAxes.join(', ') || 'none'}</div>`;
          lineStatusPanel.innerHTML += `<div class="meta">candidate lines=${candidateLines.join(', ') || 'not attached in current payload'}</div>`;
          lineStatusPanel.innerHTML += '<div class="meta">current non-goal=decision / maturity / promotion behavior not enabled here</div>';
          lineStatusPanel.innerHTML += '<div class="meta">reopen gate=document/supervisor-side only / not triggered from this panel</div>';
        }
        left.appendChild(lineStatusPanel);
        const multiLensPanel = document.createElement('div');
        multiLensPanel.className = 'subpanel';
        multiLensPanel.innerHTML = '<h3>Multi-Lens Observation</h3><div class="subhead">explanation-first surfaced view only / not a decision or maturity panel</div>';
        multiLensPanel.innerHTML += `<div class="chip-row">${renderAvailabilityPill(multiLensObservation.state === 'available' ? 'available' : 'unavailable')}${renderAvailabilityPill('observation only')}${renderAvailabilityPill('raw secondary')}</div>`;
        if (multiLensObservation.state !== 'available') {
          multiLensPanel.innerHTML += `<div class="meta">${multiLensObservation.source_note || 'multi-lens supervisor surface unavailable'}</div>`;
        } else {
          const lineStates = multiLensObservation.line_states || {};
          const parkedAxes = multiLensObservation.parked_axes || [];
          const handoff = multiLensObservation.handoff_boundary || {};
          const readings = Array.isArray(multiLensObservation.readings) ? multiLensObservation.readings : [];
          multiLensPanel.innerHTML += `<div class="meta">line_states=${Object.entries(lineStates).map(([k,v]) => `${k}:${v}`).join(' / ') || 'none'}</div>`;
          multiLensPanel.innerHTML += `<div class="meta">parked_axes=${parkedAxes.join(', ') || 'none'} / runtime_stops_after=${handoff.runtime_stops_after || 'unknown'} / next_owner=${handoff.next_owner || 'unknown'}</div>`;
          if (multiLensObservation.artifact_path) {
            multiLensPanel.innerHTML += `<div class="meta">surface artifact=${multiLensObservation.artifact_path}</div>`;
          }
          if (multiLensObservation.raw_output_reference) {
            multiLensPanel.innerHTML += `<details><summary>raw reference</summary><div class="meta">${multiLensObservation.raw_output_reference}</div></details>`;
          }
          if (!readings.length) {
            multiLensPanel.innerHTML += '<div class="empty">no surfaced multi-lens readings available</div>';
          } else {
            const rows = document.createElement('div');
            rows.className = 'stack';
            readings.slice(0, 6).forEach((reading) => {
              const row = document.createElement('div');
              row.className = 'card';
              row.innerHTML = `<div><strong>${reading.line_name || reading.line_id || 'line'}</strong> <span class="meta">state=${reading.operating_state || 'unknown'} / strength=${reading.reading_strength || 'unknown'}</span></div><div class="meta">segment=${reading.linked_segment_id || 'unknown'} / primary=${String(Boolean(reading.is_primary_lens))}</div><pre>${reading.reading_basis || 'basis unavailable'}</pre>`;
              rows.appendChild(row);
            });
            if (readings.length > 6) {
              const more = document.createElement('div');
              more.className = 'meta';
              more.textContent = `showing 6 of ${readings.length} surfaced readings`;
              rows.appendChild(more);
            }
            multiLensPanel.appendChild(rows);
          }
        }
        left.appendChild(multiLensPanel);
        const boundaryPanel = document.createElement('div');
        boundaryPanel.className = 'subpanel';
        boundaryPanel.innerHTML = '<h3>Boundary / Guard</h3><div class="subhead">read where observation stops before asking for any decision meaning</div>';
        const handoff = multiLensObservation.handoff_boundary || {};
        boundaryPanel.innerHTML += '<div class="meta">observation only / not a decision surface / not a maturity surface</div>';
        boundaryPanel.innerHTML += '<div class="meta">no promotion signal / no reopen trigger from display alone</div>';
        boundaryPanel.innerHTML += `<div class="meta">runtime_stops_after=${handoff.runtime_stops_after || 'unknown'} / next_owner=${handoff.next_owner || 'unknown'}</div>`;
        boundaryPanel.innerHTML += `<div class="meta">decision_logic_in_runtime=${String(Boolean(handoff.decision_logic_in_runtime))}</div>`;
        left.appendChild(boundaryPanel);
        const closeOutPanel = document.createElement('div');
        closeOutPanel.className = 'subpanel';
        closeOutPanel.innerHTML = '<h3>Close-out / Next Branch</h3><div class="subhead">close the current scope here unless a new bounded package is explicitly opened</div>';
        closeOutPanel.innerHTML += '<div class="meta">current scope complete=status not attached in current payload</div>';
        closeOutPanel.innerHTML += '<div class="meta">what changed=multi-lens observation now appears in the operating observation chain</div>';
        closeOutPanel.innerHTML += '<div class="meta">what did not change=runtime decision / maturity / promotion behavior remains out of scope</div>';
        closeOutPanel.innerHTML += '<div class="meta">prohibition=no reopen from display alone / no hidden decision logic</div>';
        closeOutPanel.innerHTML += '<div class="meta">next branch=document/supervisor-side bounded package only</div>';
        left.appendChild(closeOutPanel);
        grid.appendChild(left);
        const right = document.createElement('div');
        right.className = 'stack';
        const activity = document.createElement('div');
        activity.className = 'subpanel';
        activity.innerHTML = `<h3>Recent Activity</h3><div class="subhead">recent lineage / activity hint only</div><div class="chip-row">${renderAvailabilityPill((sourceMap.operating_recent_activity || {}).state === 'available' ? 'live' : 'degraded')}</div><pre>${operatingObservation.recent_activity_text || 'recent activity source unavailable'}</pre>`;
        right.appendChild(activity);
        const compare = document.createElement('div');
        compare.className = 'subpanel';
        compare.innerHTML = `<h3>Compare Hint</h3><div class="subhead">kept thin / parked compare track not resumed</div><pre>${operatingObservation.compare_hint_text || 'compare hint source unavailable'}</pre>`;
        right.appendChild(compare);
        const stickerHint = document.createElement('div');
        stickerHint.className = 'subpanel';
        stickerHint.innerHTML = '<h3>Path / Saved Path Hint</h3><div class="subhead">minimal operating linkage only / residue is not memory</div>';
        const pathSummary = buildCurrentPathSummary();
        stickerHint.innerHTML += `<div class="meta">current path state=${getPathStateLabel()}</div><div class="meta">current path readiness=${pathSummary.status}</div>`;
        if (hasResumableResidue()) {
          stickerHint.innerHTML += `<div class="meta">resumable path available=${residueState.updated_at || 'yes'}</div>`;
        }
        if (historyRereadContext) {
          stickerHint.innerHTML += `<div class="meta">historical reference attached=${historyRereadContext.summary || 'attached'}</div><div class="meta">reference only / not saved path / not active seed</div>`;
        }
        if (getPathStateLabel() === 'quick-start applied') {
          stickerHint.innerHTML += '<div class="meta">quick-start active=true</div>';
        }
        if (shell.recent_sticker) {
          stickerHint.innerHTML += `<div class="meta">recent saved path created=${shell.recent_sticker.created_at || 'unknown'}</div><div class="meta">recent why_mode=${shell.recent_sticker.why_mode || 'keep_for_later'}</div><div class="meta">memory selection=${spine.selected_memory_sticker_id || 'none'}</div><div class="meta">active seed context=${spine.similar_seed_ref || 'none'}</div><div class="meta">${shell.recent_sticker.preview_connection_summary || ''}</div>`;
        } else {
          const empty = document.createElement('div');
          empty.className = 'empty';
          empty.textContent = 'phase1 has no stickers yet / operating stays thin until Explore creates the first explicit path';
          stickerHint.appendChild(empty);
        }
        right.appendChild(stickerHint);
        const searchHint = document.createElement('div');
        searchHint.className = 'subpanel';
        searchHint.innerHTML = '<h3>Search Hint</h3><div class="subhead">minimal search linkage only</div>';
        searchHint.innerHTML += `<div class="meta">last search query=${lastSearchQuery || 'none'}</div>`;
        searchHint.innerHTML += `<div class="meta">direct hits=${String(lastSearchDirectHits)}</div>`;
        searchHint.innerHTML += `<div class="meta">current jump target=${currentJumpTargetHint}</div>`;
        searchHint.innerHTML += `<div class="meta">import context=${importContext ? importContext.source : 'none'}</div>`;
        right.appendChild(searchHint);
        grid.appendChild(right);
        surface.appendChild(grid);
        container.appendChild(surface);
      }
      function renderExploreSurface(container) {
        const surface = document.createElement('div');
        surface.className = 'surface' + (activeSurface === 'Explore' ? ' active' : '');
        surface.innerHTML = `<div class="surface-head"><strong>Explore</strong><div class="meta">path-centered / object -> lens -> position -> preview -> explicit sticker -> optional detail</div></div>`;
        const grid = document.createElement('div');
        grid.className = 'surface-grid';
        const left = document.createElement('div');
        left.className = 'stack';
        const startModePanel = document.createElement('div');
        startModePanel.className = 'subpanel';
        startModePanel.innerHTML = '<h3>Start Mode</h3><div class="subhead">blank authoring entry and quick-start scaffold are separate</div>';
        const startButtons = document.createElement('div');
        startButtons.className = 'btn-row';
        const blankButton = document.createElement('button');
        blankButton.className = 'chip-button subtle';
        blankButton.textContent = 'start blank path';
        blankButton.addEventListener('click', resetToBlankPath);
        startButtons.appendChild(blankButton);
        if (quickStartSuggestion && quickStartSuggestion.object_id && quickStartSuggestion.lens_id && quickStartSuggestion.position_value) {
          const quickButton = document.createElement('button');
          quickButton.className = 'chip-button';
          quickButton.textContent = 'apply quick-start path';
          quickButton.addEventListener('click', applyQuickStartPath);
          startButtons.appendChild(quickButton);
          const quickNote = document.createElement('div');
          quickNote.className = 'soft-note';
          quickNote.textContent = `optional scaffold path=${quickStartSuggestion.object_id} -> ${quickStartSuggestion.lens_id} -> ${quickStartSuggestion.position_value}`;
          startModePanel.appendChild(quickNote);
        }
        startModePanel.appendChild(startButtons);
        if (hasResumableResidue()) {
          const resume = document.createElement('div');
          resume.className = 'soft-note';
          resume.textContent = `residue restore remains separate / updated=${residueState.updated_at || 'unknown'}`;
          startModePanel.appendChild(resume);
        }
        left.appendChild(startModePanel);
        const objectPanel = document.createElement('div');
        objectPanel.className = 'subpanel';
        objectPanel.innerHTML = '<h3>Object</h3><div class="subhead">step 1 / select starting object</div>';
        objectPanel.innerHTML += `<div class="chip-row">${renderAvailabilityPill(exploreBinding.provenance_summary || 'fallback runtime handle + scaffold support')}${renderAvailabilityPill(exploreBinding.object_source_state === 'available' ? 'live' : 'fallback')}</div><div class="soft-note">${exploreBinding.object_source_note || 'runtime object source unavailable'}</div>`;
        const objectPresetNote = document.createElement('div');
        objectPresetNote.className = 'callout';
        objectPresetNote.textContent = 'optional starter picks / quick-start scaffold only / not the full runtime object list';
        objectPanel.appendChild(objectPresetNote);
        const starterObjects = buildStarterObjects();
        if (starterObjects.length) {
          const starterRow = document.createElement('div');
          starterRow.className = 'chip-row';
          starterObjects.forEach((item) => {
            const chip = document.createElement('button');
            chip.className = 'chip-button' + (item.id === spine.selected_object_id ? ' active' : '');
            chip.textContent = item.label;
            chip.addEventListener('click', () => {
              selectExplorePath(item.id, undefined, undefined);
            });
            starterRow.appendChild(chip);
          });
          objectPanel.appendChild(starterRow);
        }
        const objectList = document.createElement('div');
        objectList.className = 'list';
        objects.forEach((item) => {
          const button = document.createElement('button');
          button.className = 'token' + (item.id === spine.selected_object_id ? ' active' : '');
          button.innerHTML = `${item.label}<small>${item.note}</small>`;
          button.addEventListener('click', () => {
            selectExplorePath(item.id, undefined, undefined);
          });
          objectList.appendChild(button);
        });
        objectPanel.appendChild(objectList);
        left.appendChild(objectPanel);
        const lensPanel = document.createElement('div');
        lensPanel.className = 'subpanel';
        lensPanel.innerHTML = '<h3>Camera / Lens</h3><div class="subhead">step 2 / interpretation lens, not fixed field</div>';
        const lensPresetNote = document.createElement('div');
        lensPresetNote.className = 'soft-note';
        lensPresetNote.textContent = 'phase1 presets / quick start scaffold / runtime list remains below';
        lensPanel.appendChild(lensPresetNote);
        const lensPresetRow = document.createElement('div');
        lensPresetRow.className = 'chip-row';
        lenses.forEach((item) => {
          const chip = document.createElement('button');
          chip.className = 'chip-button' + (item.id === spine.selected_lens_id ? ' active' : '');
          chip.textContent = item.label;
          chip.addEventListener('click', () => {
            selectExplorePath(undefined, item.id, (getPositionList(item.id)[0] || {}).id || null);
          });
          lensPresetRow.appendChild(chip);
        });
        lensPanel.appendChild(lensPresetRow);
        const lensList = document.createElement('div');
        lensList.className = 'list';
        lenses.forEach((item) => {
          const button = document.createElement('button');
          button.className = 'token' + (item.id === spine.selected_lens_id ? ' active' : '');
          button.innerHTML = `${item.label}<small>${item.note}</small>`;
          button.addEventListener('click', () => {
            selectExplorePath(undefined, item.id, (getPositionList(item.id)[0] || {}).id || null);
          });
          lensList.appendChild(button);
        });
        lensPanel.appendChild(lensList);
        left.appendChild(lensPanel);
        const positionPanel = document.createElement('div');
        positionPanel.className = 'subpanel';
        positionPanel.innerHTML = '<h3>Position / Value</h3><div class="subhead">step 3 / preview only becomes explicit after this choice</div>';
        const positionPresetNote = document.createElement('div');
        positionPresetNote.className = 'soft-note';
        positionPresetNote.textContent = 'quick position presets for the current lens / not locked field taxonomy';
        positionPanel.appendChild(positionPresetNote);
        const positionPresetRow = document.createElement('div');
        positionPresetRow.className = 'chip-row';
        getPositionList(spine.selected_lens_id).forEach((item) => {
          const chip = document.createElement('button');
          chip.className = 'chip-button' + (item.id === spine.selected_position_value ? ' active' : '');
          chip.textContent = item.label;
          chip.addEventListener('click', () => {
            selectExplorePath(undefined, undefined, item.id);
          });
          positionPresetRow.appendChild(chip);
        });
        positionPanel.appendChild(positionPresetRow);
        const positionList = document.createElement('div');
        positionList.className = 'list';
        getPositionList(spine.selected_lens_id).forEach((item) => {
          const button = document.createElement('button');
          button.className = 'token' + (item.id === spine.selected_position_value ? ' active' : '');
          button.innerHTML = `${item.label}<small>${item.note}</small>`;
          button.addEventListener('click', () => {
            selectExplorePath(undefined, undefined, item.id);
          });
          positionList.appendChild(button);
        });
        positionPanel.appendChild(positionList);
        left.appendChild(positionPanel);
        grid.appendChild(left);
        const main = document.createElement('div');
        main.className = 'stack';
        const preview = document.createElement('div');
        preview.className = 'subpanel';
        preview.innerHTML = '<h3>Preview</h3><div class="subhead">step 4 / explicit sticker only when current interpretation path is present</div>';
        const pathSummary = buildCurrentPathSummary();
        preview.innerHTML += `<div class="meta">current path=${pathSummary.summary}</div><div class="meta">path state=${getPathStateLabel()} / ${pathSummary.status} / next step=${getNextIncompleteStep()}</div>`;
        if (historyRereadContext) {
          preview.innerHTML += `<div class="callout">Historical Reference Attached / ${historyRereadContext.summary || 'prior state slice reference'}${historyRereadContext.source_note ? ` / ${historyRereadContext.source_note}` : ''}<div class="soft-note">reference only / not saved path / not memory / not active seed / does not replace current path authoring</div></div>`;
        }
        if (importContext && importContext.destination === 'Explore') {
          preview.innerHTML += `<div class="meta">import context=${importContext.source} / ${importContext.summary}</div>`;
        }
        if (hasResumableResidue()) {
          preview.innerHTML += `<div class="meta">in-progress residue available / updated=${residueState.updated_at || 'unknown'}</div>`;
        }
        const statusStrip = document.createElement('div');
        statusStrip.className = 'status-strip';
        buildPathStatusRows().forEach((item) => {
          const card = document.createElement('div');
          card.className = 'status-card ' + (item.ready ? 'ready' : 'missing');
          card.innerHTML = `<strong>${item.label}</strong><span>${item.value}</span>`;
          statusStrip.appendChild(card);
        });
        preview.appendChild(statusStrip);
        if (spine.current_preview_connection) {
          preview.innerHTML += `<div class="preview-card"><div class="preview-title">${spine.current_preview_connection.label}</div><div class="preview-note">${spine.current_preview_connection.preview_note}</div></div>`;
          const authoring = document.createElement('div');
          authoring.className = 'stack';
          const modeWrap = document.createElement('div');
          modeWrap.className = 'subpanel';
          modeWrap.innerHTML = '<h3>Why Mode</h3><div class="subhead">thin structured authoring / no giant taxonomy</div>';
          const modeRow = document.createElement('div');
          modeRow.className = 'list';
          whyModes.forEach((mode) => {
            const button = document.createElement('button');
            button.className = 'mode-button' + (mode.id === stickerDraft.why_mode ? ' active' : '');
            button.textContent = mode.label;
            button.addEventListener('click', () => {
              stickerDraft.why_mode = mode.id;
              if (!stickerDraft.why_selected_short.trim()) {
                stickerDraft.why_selected_short = mode.label;
              }
              render();
            });
            modeRow.appendChild(button);
          });
          modeWrap.appendChild(modeRow);
          authoring.appendChild(modeWrap);
          const shortWrap = document.createElement('div');
          shortWrap.className = 'subpanel';
          shortWrap.innerHTML = '<h3>Why Short</h3><div class="subhead">one-line sticker reason</div>';
          const shortInput = document.createElement('input');
          shortInput.className = 'search-box';
          shortInput.value = stickerDraft.why_selected_short;
          shortInput.placeholder = 'keep this path for later rereading';
          shortInput.addEventListener('input', (event) => {
            stickerDraft.why_selected_short = event.target.value || '';
          });
          shortWrap.appendChild(shortInput);
          const noteInput = document.createElement('textarea');
          noteInput.className = 'note-box';
          noteInput.rows = 3;
          noteInput.placeholder = 'optional note';
          noteInput.value = stickerDraft.optional_note;
          noteInput.addEventListener('input', (event) => {
            stickerDraft.optional_note = event.target.value || '';
          });
          shortWrap.appendChild(noteInput);
          authoring.appendChild(shortWrap);
          preview.appendChild(authoring);
          const actions = document.createElement('div');
          actions.className = 'btn-row';
          const promote = document.createElement('button');
          promote.className = 'action primary';
          promote.textContent = 'save explicit sticker';
          promote.addEventListener('click', promoteCurrentPreviewToSticker);
          actions.appendChild(promote);
          const detail = document.createElement('button');
          detail.className = 'action secondary';
          detail.textContent = 'open detail / modal';
          detail.addEventListener('click', () => openDetail('explore detail', JSON.stringify(spine.current_preview_connection, null, 2)));
          actions.appendChild(detail);
          preview.appendChild(actions);
          preview.innerHTML += '<div class="meta">after saving, this path appears in Memory and may later be activated as a Similar seed.</div>';
        } else {
          const empty = document.createElement('div');
          empty.className = 'empty';
          empty.textContent = getPathStateLabel() === 'blank'
            ? 'blank authoring entry / choose object, lens, and position or apply quick-start'
            : `first sticker path starts here / ${getStickerSaveReason()}`;
          preview.appendChild(empty);
          const actions = document.createElement('div');
          actions.className = 'btn-row';
          const promote = document.createElement('button');
          promote.className = 'action primary';
          promote.textContent = 'save explicit sticker';
          promote.disabled = true;
          actions.appendChild(promote);
          preview.appendChild(actions);
        }
        if (hasResumableResidue()) {
          const residueCallout = document.createElement('div');
          residueCallout.className = 'callout';
          residueCallout.innerHTML = `current path residue / object=${residueState.object_id || 'none'} / lens=${residueState.lens_id || 'none'} / position=${residueState.position_value || 'none'} / preview_ready=${residueState.preview_ready ? 'yes' : 'no'}`;
          const restoreRow = document.createElement('div');
          restoreRow.className = 'btn-row';
          const restore = document.createElement('button');
          restore.className = 'chip-button subtle';
          restore.textContent = 'restore last path';
          restore.addEventListener('click', restoreResiduePath);
          restoreRow.appendChild(restore);
          residueCallout.appendChild(restoreRow);
          preview.appendChild(residueCallout);
        }
        const saveReason = getStickerSaveReason();
        if (saveReason) {
          preview.innerHTML += `<div class="meta">save disabled reason=${saveReason}</div>`;
        }
        if (historyRereadContext) {
          const historyDetachRow = document.createElement('div');
          historyDetachRow.className = 'btn-row';
          const historyDetach = document.createElement('button');
          historyDetach.className = 'chip-button subtle';
          historyDetach.textContent = 'Clear History Context';
          historyDetach.addEventListener('click', clearHistoryRereadContext);
          historyDetachRow.appendChild(historyDetach);
          preview.appendChild(historyDetachRow);
        }
        if (importContext && importContext.destination === 'Explore') {
          const detachRow = document.createElement('div');
          detachRow.className = 'btn-row';
          const detach = document.createElement('button');
          detach.className = 'chip-button subtle';
          detach.textContent = 'clear imported context';
          detach.addEventListener('click', clearImportContext);
          detachRow.appendChild(detach);
          preview.appendChild(detachRow);
        }
        main.appendChild(preview);
        const boundary = document.createElement('div');
        boundary.className = 'subpanel';
        boundary.innerHTML = '<h3>Explore Boundary</h3><div class="subhead">thin trace stays transient unless explicitly stickered</div><div class="meta">connection preview is a result of object + lens + position, not the start point.</div>';
        if (!memoryStickers.length) {
          boundary.innerHTML += '<div class="meta">first-sticker guide: choose object -> choose lens -> choose position -> inspect preview -> save explicit sticker -> open Memory or Similar.</div>';
        }
        boundary.innerHTML += '<div class="meta">blank start is a real empty path. quick-start is optional and must be applied explicitly.</div>';
        boundary.innerHTML += '<div class="meta">preset-first support is only a phase1 scaffold, not final taxonomy or ontology.</div>';
        boundary.innerHTML += '<div class="meta">residue is an in-progress path snapshot only. It is not Memory and it does not create a sticker.</div>';
        main.appendChild(boundary);
        grid.appendChild(main);
        surface.appendChild(grid);
        container.appendChild(surface);
      }
      function renderSearchSurface(container) {
        const surface = document.createElement('div');
        surface.className = 'surface' + (activeSurface === 'Search' ? ' active' : '');
        surface.innerHTML = `<div class="surface-head"><strong>Search</strong><div class="meta">purpose-centered / direct access / no explore flow reuse</div></div>`;
        const grid = document.createElement('div');
        grid.className = 'stack';
        const panel = document.createElement('div');
        panel.className = 'subpanel';
        panel.innerHTML = `<h3>Search Input</h3><div class="subhead">object / lens / position / connection / memory without pre-forcing one category</div><div class="chip-row">${renderAvailabilityPill(searchBinding.provenance_summary || 'degraded fallback candidates')}${renderAvailabilityPill(searchBinding.source_state === 'available' ? 'live' : 'degraded')}</div><div class="meta">${searchBinding.source_note || 'search candidate source unavailable'}</div>`;
        const input = document.createElement('input');
        input.className = 'search-box';
        input.placeholder = 'search object, lens, position, connection, or memory';
        input.value = searchQuery;
        input.addEventListener('input', (event) => {
          searchQuery = event.target.value || '';
          lastSearchQuery = searchQuery.trim();
          render();
        });
        panel.appendChild(input);
        const searchState = buildSearchGroups(searchQuery);
        lastSearchDirectHits = searchState.direct_hits;
        if (!searchQuery.trim()) {
          const idle = document.createElement('div');
          idle.className = 'meta';
          idle.textContent = 'search is idle until you ask for direct access / empty search is normal';
          panel.appendChild(idle);
        } else if (searchState.direct_hits === 0 && searchState.partial_hits > 0) {
          const partial = document.createElement('div');
          partial.className = 'meta';
          partial.textContent = `partial matches only / direct hits=0 / partial hits=${searchState.partial_hits}`;
          panel.appendChild(partial);
        } else if (searchState.direct_hits === 0 && searchState.partial_hits === 0) {
          const none = document.createElement('div');
          none.className = 'meta';
          none.textContent = 'no direct matches / no partial matches';
          panel.appendChild(none);
        } else {
          const hits = document.createElement('div');
          hits.className = 'meta';
          hits.textContent = `direct hits=${searchState.direct_hits} / partial hits=${searchState.partial_hits}`;
          panel.appendChild(hits);
        }
        grid.appendChild(panel);
        const results = document.createElement('div');
        results.className = 'search-grid';
        const groupOrder = [
          ['objects', 'objects'],
          ['lenses', 'lenses'],
          ['positions', 'positions'],
          ['stickers', 'saved paths / memory'],
          ['seed_relevant', 'seed-related paths'],
        ];
        groupOrder.forEach(([groupKey, label]) => {
          const sub = document.createElement('div');
          sub.className = 'subpanel';
          const items = (searchState.groups[groupKey] || []).slice(0, 6);
          const directCount = items.filter((item) => item.match_level === 'direct').length;
          const partialCount = items.filter((item) => item.match_level === 'partial').length;
          sub.innerHTML = `<h3>${label}</h3><div class="subhead">direct access result group / direct=${directCount} / partial=${partialCount}</div>`;
          const list = document.createElement('div');
          list.className = 'list';
          items.forEach((item) => {
            const card = document.createElement('div');
            card.className = 'result-card';
            const provenanceLabel = groupKey === 'stickers' || groupKey === 'seed_relevant' ? 'stored' : 'live';
            card.innerHTML = `<strong>${item.label}</strong><div class="meta">${item.note || ''}</div><div class="chip-row"><div class="pill">${item.match_level} match</div><div class="pill">matched in ${item.matched_in}</div><div class="pill">${item.jump_target}</div>${renderAvailabilityPill(provenanceLabel)}</div>`;
            const actions = document.createElement('div');
            actions.className = 'btn-row';
            const jump = document.createElement('button');
            jump.className = 'action secondary';
            jump.textContent = item.jump_target === 'Similar' ? 'activate in Similar' : `open in ${item.jump_target}`;
            jump.addEventListener('click', item.on_jump);
            actions.appendChild(jump);
            card.appendChild(actions);
            list.appendChild(card);
          });
          if (!list.children.length) {
            const empty = document.createElement('div');
            empty.className = 'empty';
            empty.textContent = !searchQuery.trim()
              ? 'no query yet / direct access starts when you ask for something'
              : (searchState.direct_hits === 0 && searchState.partial_hits > 0 ? 'no direct matches in this group / partial-only or no local group hit' : 'no direct matches in this group');
            sub.appendChild(empty);
          } else {
            sub.appendChild(list);
          }
          results.appendChild(sub);
        });
        grid.appendChild(results);
        surface.appendChild(grid);
        container.appendChild(surface);
      }
      function renderMemorySurface(container) {
        const surface = document.createElement('div');
        surface.className = 'surface' + (activeSurface === 'Memory' ? ' active' : '');
        surface.innerHTML = `<div class="surface-head"><strong>Memory</strong><div class="meta">compact readable sticker cards / not large memory document view</div></div>`;
        const grid = document.createElement('div');
        grid.className = 'surface-grid';
        const left = document.createElement('div');
        left.className = 'subpanel';
        left.innerHTML = `<h3>Explicit Saved Paths</h3><div class="subhead">saved explicitly from Explore or Similar only</div><div class="chip-row">${renderAvailabilityPill(memoryBinding.provenance_summary || 'stored saved paths')}</div><div class="meta">${memoryBinding.source_note || 'saved path source unavailable'}</div>`;
        const list = document.createElement('div');
        list.className = 'list';
        memoryStickers.forEach((item) => {
          const button = document.createElement('button');
          button.className = 'token' + (item.sticker_id === spine.selected_memory_sticker_id ? ' active' : '');
          const badges = [];
          if (item.sticker_id === spine.selected_memory_sticker_id) badges.push('selected');
          if ((item.seed_ref || item.sticker_id) === spine.similar_seed_ref) badges.push('active seed');
          if (shell.recent_sticker && shell.recent_sticker.sticker_id === item.sticker_id) badges.push('recent');
          button.innerHTML = `${item.preview_connection_summary}<small>object=${item.object_id} / lens=${item.lens_id} / position=${item.position_value}</small><small>${item.why_selected_short || item.why_selected}</small><small>${formatWhyMode(item.why_mode)} / ${item.created_at}</small>${badges.length ? `<small>${badges.join(' / ')}</small>` : ''}`;
          button.addEventListener('click', () => {
            spine.selected_memory_sticker_id = item.sticker_id;
            setImportContext('Memory', 'Memory', `selected sticker ${item.sticker_id}`);
            activeSurface = 'Memory';
            render();
          });
          list.appendChild(button);
        });
        if (!list.children.length) {
          const empty = document.createElement('div');
          empty.className = 'empty';
          empty.textContent = 'no explicit interpretation path has been stickered yet / click logs do not appear here';
          left.appendChild(empty);
        } else {
          left.appendChild(list);
        }
        grid.appendChild(left);
        const right = document.createElement('div');
        right.className = 'subpanel';
        right.innerHTML = '<h3>Selected Sticker</h3><div class="subhead">compact but readable memory unit</div>';
        if (historyRereadContext) {
          right.innerHTML += `<div class="meta">historical reference remains separate from Memory / ${historyRereadContext.summary || 'attached'}</div>`;
        }
        const sticker = getSelectedSticker();
        if (sticker) {
          if (importContext && importContext.destination === 'Memory') {
          right.innerHTML += `<div class="meta">import context=${importContext.source} / ${importContext.summary}</div>`;
          }
          right.innerHTML += `<div class="preview-card"><div class="preview-title">${sticker.preview_connection_summary}</div><div class="preview-note">${sticker.why_selected_short || sticker.why_selected}</div><div class="chip-row"><div class="pill">${formatWhyMode(sticker.why_mode)}</div>${shell.recent_sticker && shell.recent_sticker.sticker_id === sticker.sticker_id ? '<div class="pill">recent</div>' : ''}${(sticker.seed_ref || sticker.sticker_id) === spine.similar_seed_ref ? '<div class="pill">active seed</div>' : ''}</div><div class="meta">object=${sticker.object_id} / lens=${sticker.lens_id} / position=${sticker.position_value}</div><div class="meta">created_at=${sticker.created_at}</div>${sticker.optional_note ? `<div class="meta">note=${sticker.optional_note}</div>` : ''}</div>`;
          const actions = document.createElement('div');
          actions.className = 'btn-row';
          const activateSeed = document.createElement('button');
          activateSeed.className = 'action secondary';
          activateSeed.textContent = 'activate seed in Similar';
          activateSeed.addEventListener('click', () => {
            spine.similar_seed_ref = sticker.seed_ref || sticker.sticker_id;
            setImportContext('Memory', 'Similar', `seed activated from sticker ${sticker.sticker_id}`);
            activeSurface = 'Similar';
            currentJumpTargetHint = `Similar:${sticker.sticker_id}`;
            render();
          });
          actions.appendChild(activateSeed);
          if (importContext && importContext.destination === 'Memory') {
            const detach = document.createElement('button');
            detach.className = 'chip-button subtle';
            detach.textContent = 'clear imported context';
            detach.addEventListener('click', clearImportContext);
            actions.appendChild(detach);
          }
          right.appendChild(actions);
        } else {
          const empty = document.createElement('div');
          empty.className = 'empty';
          empty.textContent = memoryStickers.length ? 'select a sticker to inspect its saved path' : 'Memory wakes up after the first explicit sticker is saved from Explore';
          right.appendChild(empty);
        }
        grid.appendChild(right);
        surface.appendChild(grid);
        container.appendChild(surface);
      }
      function renderSimilarSurface(container) {
        const surface = document.createElement('div');
        surface.className = 'surface' + (activeSurface === 'Similar' ? ' active' : '');
        surface.innerHTML = `<div class="surface-head"><strong>Similar</strong><div class="meta">active seed context -> thin local re-query / trace first, not score first</div></div>`;
        const grid = document.createElement('div');
        grid.className = 'surface-grid';
        const left = document.createElement('div');
        left.className = 'subpanel';
        left.innerHTML = `<h3>Seed Context</h3><div class="subhead">explicit saved paths are the only seeds in this turn</div><div class="chip-row">${renderAvailabilityPill(similarBinding.provenance_summary || 'stored seed context unavailable')}</div><div class="meta">${similarBinding.source_note || 'seed context source unavailable'}</div>`;
        if (importContext && importContext.destination === 'Similar') {
          left.innerHTML += `<div class="meta">import context=${importContext.source} / ${importContext.summary}</div>`;
        }
        const list = document.createElement('div');
        list.className = 'list';
        memoryStickers.forEach((item) => {
          const button = document.createElement('button');
          button.className = 'token' + ((item.seed_ref || item.sticker_id) === spine.similar_seed_ref ? ' active' : '');
          button.innerHTML = `${item.preview_connection_summary}<small>${item.why_selected_short || item.why_selected}</small><small>${formatWhyMode(item.why_mode)}</small>`;
          button.addEventListener('click', () => {
            spine.similar_seed_ref = item.seed_ref || item.sticker_id;
            setImportContext('Similar', 'Similar', `seed switched to ${item.sticker_id}`);
            render();
          });
          list.appendChild(button);
        });
        if (spine.similar_seed_ref) {
          const clearRow = document.createElement('div');
          clearRow.className = 'btn-row';
          const clearSeed = document.createElement('button');
          clearSeed.className = 'chip-button subtle';
          clearSeed.textContent = 'clear active seed';
          clearSeed.addEventListener('click', clearActiveSeed);
          clearRow.appendChild(clearSeed);
          if (importContext && importContext.destination === 'Similar') {
            const detach = document.createElement('button');
            detach.className = 'chip-button subtle';
            detach.textContent = 'clear imported context';
            detach.addEventListener('click', clearImportContext);
            clearRow.appendChild(detach);
          }
          left.appendChild(clearRow);
        }
        if (!list.children.length) {
          const empty = document.createElement('div');
          empty.className = 'empty';
          empty.textContent = 'no seed context yet / Similar needs an explicit saved path before local re-query can start';
          left.appendChild(empty);
        } else {
          left.appendChild(list);
        }
        grid.appendChild(left);
        const main = document.createElement('div');
        main.className = 'subpanel';
        main.innerHTML = '<h3>Local Similar Structures</h3><div class="subhead">matched_on + trace_summary + confidence_style only</div>';
        const results = buildSimilarResults();
        if (!results.length) {
          const empty = document.createElement('div');
          empty.className = 'empty';
          empty.textContent = memoryStickers.length ? 'activate one saved path as seed context to start local re-query' : 'Similar is empty because there is no saved path seed context yet';
          main.appendChild(empty);
        } else if (results.every((item) => item.confidence_style === 'low-confidence')) {
          const thin = document.createElement('div');
          thin.className = 'meta';
          thin.textContent = 'seed is active, but current local re-query is thin and low-confidence';
          main.appendChild(thin);
        } else {
          const cards = document.createElement('div');
          cards.className = 'list';
          results.forEach((item) => {
            const card = document.createElement('div');
            card.className = 'result-card';
            const badges = (item.matched_on || []).slice(0, 3).map((token) => `<div class="pill">${token}</div>`).join('');
            card.innerHTML = `<strong>${item.title}</strong><div class="meta">${item.note}</div><div class="chip-row">${badges}<div class="pill">${item.confidence_style}</div></div><div class="meta">trace: ${item.trace_summary}</div>`;
            const actions = document.createElement('div');
            actions.className = 'btn-row';
            const detail = document.createElement('button');
            detail.className = 'action secondary';
            detail.textContent = 'open detail';
            detail.addEventListener('click', () => openDetail('similar structure detail', JSON.stringify(item, null, 2)));
            actions.appendChild(detail);
            const sticker = document.createElement('button');
            sticker.className = 'action primary';
            sticker.textContent = 'save explicit sticker';
            sticker.addEventListener('click', () => promoteSimilarResult(item));
            actions.appendChild(sticker);
            card.appendChild(actions);
            cards.appendChild(card);
          });
          main.appendChild(cards);
        }
        grid.appendChild(main);
        surface.appendChild(grid);
        container.appendChild(surface);
      }
      function render() {
        syncCurrentPreview();
        page.querySelectorAll('.tabs-shell, .surface-shell').forEach((node) => node.remove());
        page.appendChild(renderTabs());
        const shellLayout = document.createElement('div');
        shellLayout.className = 'shell-layout surface-shell';
        shellLayout.appendChild(renderSpineSidebar());
        const content = document.createElement('div');
        content.className = 'panel';
        renderOperatingSurface(content);
        renderExploreSurface(content);
        renderSearchSurface(content);
        renderMemorySurface(content);
        renderSimilarSurface(content);
        shellLayout.appendChild(content);
        page.appendChild(shellLayout);
      }

      app.appendChild(page);
      render();
    })();
  </script>
</body>
</html>"""


def _build_lens_options() -> List[Dict[str, str]]:
    return [
        {"id": "structure", "label": "Structure Lens", "note": "read internal form and arrangement"},
        {"id": "ai", "label": "AI Lens", "note": "read synthetic or machine-adjacent positioning"},
        {"id": "memory", "label": "Memory Lens", "note": "read what may survive as selective promotion"},
    ]


def _build_position_options() -> Dict[str, List[Dict[str, str]]]:
    return {
        "structure": [
            {"id": "anchor", "label": "Anchor", "note": "place the object as a stabilizing anchor"},
            {"id": "bridge", "label": "Bridge", "note": "place the object as a connector"},
            {"id": "surface", "label": "Surface", "note": "place the object where form becomes visible"},
        ],
        "ai": [
            {"id": "hologram", "label": "Hologram", "note": "read the object as projected presence"},
            {"id": "assistant", "label": "Assistant", "note": "read the object as helper role"},
            {"id": "mirror", "label": "Mirror", "note": "read the object as reflective value"},
        ],
        "memory": [
            {"id": "residue", "label": "Residue", "note": "read what remains after first pass"},
            {"id": "sticker", "label": "Sticker", "note": "read what may deserve selective promotion"},
            {"id": "condensation", "label": "Condensation", "note": "read whether a path can condense"},
        ],
    }


def _build_preview_connection(
    object_id: Optional[str],
    lens_id: Optional[str],
    position_value: Optional[str],
    objects: List[Dict[str, str]],
    lenses: List[Dict[str, str]],
    positions_by_lens: Dict[str, List[Dict[str, str]]],
) -> Optional[Dict[str, str]]:
    if not object_id or not lens_id or not position_value:
        return None
    object_item = next((item for item in objects if item["id"] == object_id), None)
    lens_item = next((item for item in lenses if item["id"] == lens_id), None)
    position_item = next((item for item in positions_by_lens.get(lens_id, []) if item["id"] == position_value), None)
    if not object_item or not lens_item or not position_item:
        return None
    return {
        "id": f"preview:{object_id}:{lens_id}:{position_value}",
        "object_id": object_id,
        "lens_id": lens_id,
        "position_value": position_value,
        "label": f"{object_item['label']} -> {lens_item['label']} -> {position_item['label']}",
        "preview_note": f"{lens_item['note']} / {position_item['note']}",
    }


# Sticker persistence is append-only because explicit saved interpretation paths
# should remain distinct from lighter in-progress traces.
def _phase1_memory_store(runtime_root: Path) -> JsonlEventStore:
    return JsonlEventStore(runtime_root / "manifests" / "operating_ui_phase1" / "phase1_memory_stickers.jsonl")


# Residue persistence is a latest-snapshot file because it only preserves the
# most recent in-progress path and must not be confused with Memory stickers.
def _phase1_path_residue_file(runtime_root: Path) -> Path:
    return runtime_root / "manifests" / "operating_ui_phase1" / "phase1_current_path_residue.json"


def _slug(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value.lower()).strip("_") or "seed"


def _normalize_why_mode(value: Optional[str]) -> str:
    if value in WHY_MODES:
        return value
    return "keep_for_later"


def _default_why_selected_short(why_mode: str) -> str:
    defaults = {
        "relation_found": "found a relation worth keeping",
        "perspective_shift": "this changed the reading perspective",
        "resonance": "this path resonated enough to keep",
        "keep_for_later": "keep this path for later rereading",
        "unclear_but_hold": "not fully clear yet, but worth holding",
    }
    return defaults.get(why_mode, "keep this path for later rereading")


def _normalize_legacy_why_mode(row: Dict[str, Any]) -> str:
    value = str(row.get("why_mode") or "").strip()
    if value:
        return _normalize_why_mode(value)
    return "keep_for_later"


def _normalize_legacy_why_selected_short(row: Dict[str, Any], why_mode: str) -> str:
    value = str(row.get("why_selected_short") or "").strip()
    if value:
        return value
    legacy = str(row.get("why_selected") or "").strip()
    return legacy or _default_why_selected_short(why_mode)


def _normalize_legacy_optional_note(row: Dict[str, Any], why_short: str) -> str:
    value = str(row.get("optional_note") or "").strip()
    if value:
        return value
    legacy = str(row.get("why_selected") or "").strip()
    if not legacy or legacy == why_short:
        return ""
    if " / " in legacy:
        head, tail = legacy.split(" / ", 1)
        if head.strip() == why_short and tail.strip():
            return tail.strip()
    return ""


# Validation helpers below mirror the phase1 ownership contract without
# depending on browser automation. They should stay aligned with the UI event
# semantics for Search / Explore / Memory / Similar jumps.
def build_phase1_probe_state(shell_data: Dict[str, Any]) -> Dict[str, Any]:
    shell = shell_data.get("phase1_shell") or {}
    return {
        "shared_spine": copy.deepcopy(shell.get("shared_spine") or {}),
        "quick_start_suggestion": copy.deepcopy(shell.get("quick_start_suggestion") or {}),
        "path_residue": copy.deepcopy(shell.get("path_residue")),
        "history_reread_context": copy.deepcopy(shell.get("history_reread_context")),
        "import_context": None,
        "path_state": "blank",
    }


def phase1_probe_apply_quick_start(state: Dict[str, Any]) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    suggestion = next_state.get("quick_start_suggestion") or {}
    spine = next_state["shared_spine"]
    spine["selected_object_id"] = suggestion.get("object_id")
    spine["selected_lens_id"] = suggestion.get("lens_id")
    spine["selected_position_value"] = suggestion.get("position_value")
    spine["current_preview_connection"] = copy.deepcopy(suggestion.get("preview_connection"))
    next_state["path_state"] = "quick-start applied"
    next_state["import_context"] = {"source": "Explore quick-start", "destination": "Explore"}
    return next_state


def phase1_probe_select_explore_path(
    state: Dict[str, Any],
    *,
    object_id: Optional[str] = None,
    lens_id: Optional[str] = None,
    position_value: Optional[str] = None,
) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    spine = next_state["shared_spine"]
    if object_id is not None:
        spine["selected_object_id"] = object_id
    if lens_id is not None:
        spine["selected_lens_id"] = lens_id
    if position_value is not None:
        spine["selected_position_value"] = position_value
    spine["current_preview_connection"] = {
        "object_id": spine.get("selected_object_id"),
        "lens_id": spine.get("selected_lens_id"),
        "position_value": spine.get("selected_position_value"),
    } if spine.get("selected_object_id") and spine.get("selected_lens_id") and spine.get("selected_position_value") else None
    next_state["path_state"] = "manually progressed"
    return next_state


def phase1_probe_search_open_in_explore(
    state: Dict[str, Any],
    *,
    object_id: Optional[str] = None,
    lens_id: Optional[str] = None,
    position_value: Optional[str] = None,
) -> Dict[str, Any]:
    next_state = phase1_probe_select_explore_path(
        state,
        object_id=object_id,
        lens_id=lens_id,
        position_value=position_value,
    )
    next_state["import_context"] = {"source": "Search", "destination": "Explore"}
    return next_state


def phase1_probe_search_open_in_memory(state: Dict[str, Any], sticker_id: str) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["shared_spine"]["selected_memory_sticker_id"] = sticker_id
    next_state["import_context"] = {"source": "Search", "destination": "Memory"}
    return next_state


def phase1_probe_search_use_in_similar(state: Dict[str, Any], seed_ref: str) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["shared_spine"]["similar_seed_ref"] = seed_ref
    next_state["import_context"] = {"source": "Search", "destination": "Similar"}
    return next_state


def phase1_probe_memory_select_sticker(state: Dict[str, Any], sticker_id: str) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["shared_spine"]["selected_memory_sticker_id"] = sticker_id
    next_state["import_context"] = {"source": "Memory", "destination": "Memory"}
    return next_state


def phase1_probe_activate_seed_from_memory(state: Dict[str, Any], seed_ref: str) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["shared_spine"]["similar_seed_ref"] = seed_ref
    next_state["import_context"] = {"source": "Memory", "destination": "Similar"}
    return next_state


def phase1_probe_clear_active_seed(state: Dict[str, Any]) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["shared_spine"]["similar_seed_ref"] = None
    if (next_state.get("import_context") or {}).get("destination") == "Similar":
        next_state["import_context"] = None
    return next_state


def phase1_probe_restore_residue(state: Dict[str, Any], residue: Dict[str, Any]) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    spine = next_state["shared_spine"]
    spine["selected_object_id"] = residue.get("object_id") or None
    spine["selected_lens_id"] = residue.get("lens_id") or None
    spine["selected_position_value"] = residue.get("position_value") or None
    spine["current_preview_connection"] = {
        "object_id": spine.get("selected_object_id"),
        "lens_id": spine.get("selected_lens_id"),
        "position_value": spine.get("selected_position_value"),
    } if residue.get("preview_ready") else None
    next_state["path_state"] = "residue restored"
    next_state["import_context"] = {"source": "Residue", "destination": "Explore"}
    return next_state


def phase1_probe_reset_blank(state: Dict[str, Any]) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["shared_spine"]["selected_object_id"] = None
    next_state["shared_spine"]["selected_lens_id"] = None
    next_state["shared_spine"]["selected_position_value"] = None
    next_state["shared_spine"]["current_preview_connection"] = None
    next_state["path_state"] = "blank"
    if (next_state.get("import_context") or {}).get("destination") == "Explore":
        next_state["import_context"] = None
    return next_state


def phase1_probe_open_from_history(
    state: Dict[str, Any],
    *,
    asset_id: Optional[str],
    snapshot_ref: Optional[str],
    cluster_ref: Optional[str],
    trace_ref: Optional[str],
    summary: str,
    source_note: Optional[str] = None,
) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["history_reread_context"] = {
        "asset_id": asset_id,
        "snapshot_ref": snapshot_ref,
        "cluster_ref": cluster_ref,
        "trace_ref": trace_ref,
        "summary": summary,
        "source_note": source_note or "",
    }
    return next_state


def phase1_probe_clear_history_reread_context(state: Dict[str, Any]) -> Dict[str, Any]:
    next_state = copy.deepcopy(state)
    next_state["history_reread_context"] = None
    return next_state


def _build_history_reread_context(
    *,
    asset_id: Optional[str],
    history_snapshot_ref: Optional[str],
    history_cluster_ref: Optional[str],
    history_trace_ref: Optional[str],
    history_reread_summary: Optional[str],
    history_source_note: Optional[str],
) -> Optional[Dict[str, str]]:
    if not any(
        [
            history_snapshot_ref,
            history_cluster_ref,
            history_trace_ref,
            history_reread_summary,
            history_source_note,
        ]
    ):
        return None
    return {
        "asset_id": str(asset_id or "").strip(),
        "snapshot_ref": str(history_snapshot_ref or "").strip(),
        "cluster_ref": str(history_cluster_ref or "").strip(),
        "trace_ref": str(history_trace_ref or "").strip(),
        "summary": str(history_reread_summary or "prior state slice reference").strip(),
        "source_note": str(history_source_note or "").strip(),
    }
