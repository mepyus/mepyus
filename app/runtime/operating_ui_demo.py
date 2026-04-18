from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import json

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


def build_operating_ui_composition_demo_data(runtime_root: Path, case: str = "a") -> Dict[str, Any]:
    fixture_root = runtime_root.parent / "app" / "work" / "operating_ui" / "fixtures"
    fixture_path = fixture_root / f"process_console_payload_case_{case.lower()}.json"
    if not fixture_path.exists():
        return {
            "state": "fixture_not_found",
            "requested_case": case,
            "available_cases": _available_cases(fixture_root),
        }

    raw_payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    model = adapt_process_console_payload_to_operating_ui_model(raw_payload)

    derived_strip = build_derived_state_strip_view(
        selectedAsset=model.get("selectedAsset"),
        latestPreview=(model.get("derivedStrip") or {}).get("latestPreview"),
        diffSummary=(model.get("derivedStrip") or {}).get("diffSummary"),
        attentionSummary=(model.get("derivedStrip") or {}).get("attentionSummary"),
        memorySummary=(model.get("derivedStrip") or {}).get("memorySummary"),
        compareHref="/compare" if ((model.get("derivedStrip") or {}).get("diffSummary") or {}).get("state") == "loaded" else None,
    )

    board = build_asset_state_board_view(
        model.get("boardItems", []),
        selectedAssetId=model.get("selectedAssetId"),
        sortLabel="updated_at",
        filterSummary="packet_texture=all",
    )

    activity_model = model.get("activityPanel") or {}
    diff_model = (model.get("derivedStrip") or {}).get("diffSummary") or {}
    history_summary = {
        "latestChangeKind": diff_model.get("diffClass") or diff_model.get("state"),
        "latestReason": ((model.get("selectedAsset") or {}).get("historySummary") or {}).get("latestReason"),
        "state": "history_unavailable" if activity_model.get("items") == [] and not activity_model.get("latestLineageSummary") and not model.get("selectedAsset") else None,
    }
    latest_lineage = {
        "summary": activity_model.get("latestLineageSummary"),
        "latestTrigger": activity_model.get("latestTrigger"),
        "latestReason": activity_model.get("latestReason"),
        "latestUpdatedAt": activity_model.get("latestUpdatedAt"),
    }
    activity_panel = build_activity_panel_view(
        activity_model.get("items", []),
        historySummary=history_summary,
        latestLineage=latest_lineage,
    )

    return {
        "state": "loaded",
        "requested_case": case.lower(),
        "available_cases": _available_cases(fixture_root),
        "pageTitle": model.get("pageTitle"),
        "strip": derived_strip,
        "board": board,
        "activity": activity_panel,
        "debug_text": {
            "strip": render_derived_state_strip_text(derived_strip),
            "board": render_asset_state_board_text(board),
            "activity": render_activity_panel_text(activity_panel),
        },
    }


def render_operating_ui_composition_demo_html(
    data: Dict[str, Any] | None = None,
    api_path: str = "/api/operating-ui-demo?case=a",
) -> str:
    payload_block = (
        f'<script id="operating-ui-demo-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('operating-ui-demo-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Operating UI Demo</title>
  <style>
    body { margin: 0; font-family: Georgia, serif; background: #f5f1e8; color: #1f2937; }
    .page { max-width: 1440px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .top { background: #fffaf2; border: 1px solid #d7cab7; border-radius: 18px; padding: 16px; }
    .nav { display: inline-block; padding: 7px 12px; border-radius: 999px; border: 1px solid #d7cab7; text-decoration: none; color: #6c4d2f; background: #fff; margin-right: 8px; }
    .layout { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 16px; }
    .panel { background: #fffaf2; border: 1px solid #d7cab7; border-radius: 18px; padding: 14px; }
    .section { margin-bottom: 12px; }
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
      top.innerHTML = `<a class="nav" href="/process-console">process-console</a><a class="nav" href="/operating-ui-demo?case=a">case a</a><a class="nav" href="/operating-ui-demo?case=b">case b</a><a class="nav" href="/operating-ui-demo?case=c">case c</a><a class="nav" href="/operating-ui-demo?case=d">case d</a><div><strong>${data.pageTitle || 'operating ui demo'}</strong> <span class="meta">fixture case=${data.requested_case || 'a'}</span></div>`;
      page.appendChild(top);

      if (data.state !== 'loaded') {
        const panel = document.createElement('div');
        panel.className = 'panel';
        panel.innerHTML = `<div class="empty">${data.state || 'fixture_not_found'}</div>`;
        page.appendChild(panel);
        app.appendChild(page);
        return;
      }

      const strip = document.createElement('div');
      strip.className = 'panel';
      strip.innerHTML = '<h3>Derived State Strip</h3>';
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
      page.appendChild(strip);

      const layout = document.createElement('div');
      layout.className = 'layout';

      const board = document.createElement('div');
      board.className = 'panel';
      board.innerHTML = '<h3>Asset State Board</h3>';
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
          card.innerHTML = `<strong>${item.title || item.assetId || 'asset'}</strong><div class="meta">${item.primarySummary || ''}</div><div class="meta">${item.secondarySummary || ''}</div><div class="meta">${item.helperText || ''}</div>`;
          board.appendChild(card);
        });
      }
      layout.appendChild(board);

      const activity = document.createElement('div');
      activity.className = 'panel';
      activity.innerHTML = '<h3>Activity Panel</h3>';
      const activityPre = document.createElement('pre');
      activityPre.textContent = data.debug_text.activity;
      activity.appendChild(activityPre);
      layout.appendChild(activity);

      page.appendChild(layout);
      app.appendChild(page);
    })();
  </script>
</body>
</html>"""


def _available_cases(fixture_root: Path) -> list[str]:
    return sorted(
        path.stem.split("_")[-1]
        for path in fixture_root.glob("process_console_payload_case_*.json")
    )
