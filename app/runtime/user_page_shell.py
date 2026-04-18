from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

from app.runtime.explore_candidate_extractor import extract_explore_candidates
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data
from app.runtime.operating_ui_phase1 import load_phase1_memory_stickers
from app.runtime.runtime_preflight import build_runtime_preflight
from app.runtime.rule_eligibility import project_candidate_rule_binding
from app.runtime.saved_connections import load_saved_connections
from app.runtime.segment_to_source_context_extractor import (
    extract_object_source_context,
    extract_segment_source_context,
)


CORE_NAV = [
    ("운용", "/operating"),
    ("탐색", "/explore"),
    ("찾기", "/search"),
    ("기억", "/memory"),
    ("비슷한 연결", "/similar"),
]


def render_user_operating_page(
    runtime_root: Path,
    *,
    asset_id: Optional[str] = None,
    selected_row_key: Optional[str] = None,
) -> str:
    source = _build_source(
        runtime_root,
        asset_id=asset_id,
        selected_row_key=selected_row_key,
        page_key="operating",
        mode_hint="space_reading",
    )
    selected = source["selected_asset"]
    left_list = _render_link_list(
        "어떤 입력을 볼지 고른다",
        "지금 읽을 원본 입력을 여기서 고른다.",
        [
            _link_item(
                label=item["title"],
                href=_page_href("/operating", asset_id=item["id"], selected_row_key=source["selected_row_key"]),
                note=item["note"],
                active=item["id"] == source["selected_asset_id"],
            )
            for item in source["asset_items"]
        ],
    )
    original_refs = selected.get("original_refs") or ["원본 단서가 아직 비어 있다."]
    segment_rows = selected.get("segment_rows") or []
    source_context = selected.get("source_context") or {}
    full_source_text = selected.get("full_source_text") or ""
    original_items = [f"<div class='source-chip'>{escape(ref)}</div>" for ref in original_refs]
    if source_context:
        original_items.extend(
            [
                f"<div class='body-copy'>{escape(source_context.get('paragraph_ref') or '원문 단락 위치를 아직 찾지 못했다.')}</div>",
                f"<div class='body-copy'>{escape(source_context.get('paragraph_text') or '원문 단락을 아직 찾지 못했다.')}</div>",
                f"<div class='body-copy'>{escape(source_context.get('surrounding_context') or '주변 문맥이 아직 없다.')}</div>",
            ]
        )
    else:
        original_items.append("<div class='body-copy'>지금은 분절값에서 바로 돌아갈 원문 단락을 아직 찾지 못했다.</div>")
    if full_source_text:
        original_items.append(
            _render_full_source_block(
                full_source_text=full_source_text,
                selected_paragraph=source_context.get("paragraph_text") or "",
            )
        )
    else:
        original_items.append("<div class='body-copy'>지금은 전체 원본을 아직 불러오지 못했다.</div>")
    segment_items = []
    if segment_rows:
        for row in segment_rows:
            row_href = _page_href(
                "/operating",
                asset_id=source["selected_asset_id"],
                selected_row_key=row.get("key") or "",
            )
            row_label = escape(row.get("label") or "분절")
            row_class = "segment-row active" if row.get("key") == source.get("selected_row_key") else "segment-row"
            segment_items.append(f"<a class='{row_class}' href='{escape(row_href)}'>{row_label}</a>")
            if row.get("paragraph_text"):
                row_ref = row.get("paragraph_ref") or ""
                row_text = row.get("paragraph_text") or ""
                segment_items.append(f"<div class='body-copy'>{escape(row_ref + ' / ' + row_text if row_ref else row_text)}</div>")
    else:
        segment_items = ["<div class='segment-row'>분절 구조가 아직 비어 있다.</div>"]
    main_html = _render_main_stack(
        "선택한 입력을 원본과 나뉜 흐름으로 읽는다",
        [
            _content_card(
                "원본에서 바로 확인할 자리",
                original_items,
            ),
            _content_card(
                "나뉜 흐름을 읽는 자리",
                segment_items,
            ),
            _content_card(
                "원본을 읽으며 남긴 메모",
                [f"<div class='body-copy'>{escape(selected.get('body_note') or '원본을 읽으며 남긴 메모가 아직 없다.')}</div>"],
            ),
        ],
    )
    right_html = _render_detail_stack(
        "지금 봐야 할 요점을 모아 본다",
        [
            _detail_block("짧은 요약", selected.get("summary") or "아직 짧게 모인 요약은 없다."),
            _detail_block("다음에 볼 연결 단서", selected.get("connection_hint") or "아직 이어서 볼 단서는 또렷하지 않다."),
            _detail_block("스티커 자리", selected.get("sticker_slot") or "필요한 연결을 남길 자리는 여기 둔다."),
        ],
    )
    return _render_shell(
        page_title="운용",
        page_heading="운용",
        page_subtitle="원본 입력을 읽으며 무엇이 어떻게 나뉘는지 먼저 파악하는 자리",
        active_key="운용",
        left_html=left_list,
        main_html=main_html,
        right_html=right_html,
    )


def render_user_explore_page(
    runtime_root: Path,
    *,
    object_id: Optional[str] = None,
    candidate_id: Optional[str] = None,
) -> str:
    source = _build_source(
        runtime_root,
        asset_id=object_id,
        page_key="explore",
        mode_hint="space_reading",
    )
    selected = source["selected_asset"]
    candidates = _build_explore_candidates(
        selected,
        raw_asset=source.get("raw_selected_asset") or {},
    )
    candidate_reading = {
        candidate["id"]: _build_explore_reading_context(
            asset_id=source["selected_asset_id"],
            raw_asset=source.get("raw_selected_asset") or {},
            candidate=candidate,
        )
        for candidate in candidates
    }
    selected_candidate = _pick_by_id(candidates, candidate_id) or (candidates[0] if candidates else {})
    reading_context = candidate_reading.get(selected_candidate.get("id") or "", {})
    left_html = (
        "<div class='panel-card'>"
        "<h3>어떤 객체를 볼지 적는다</h3>"
        "<div class='panel-note'>지금은 입력했던 객체를 다시 고르며 시작하고, 직접 적는 자리는 얇게만 열어둔다.</div>"
        "<form method='get' action='/explore' class='search-form'>"
        f"<input class='text-input' type='text' name='object_id' value='{escape(source['selected_asset_id']) if source.get('typed_object') else ''}' placeholder='객체 이름을 적어 다시 읽을 자리를 남긴다' />"
        "<button class='submit-button' type='submit'>불러오기</button>"
        "</form>"
        "</div>"
        + _render_link_list(
            "다시 읽을 객체를 고른다",
            "원본에서 다시 보고 싶은 객체를 여기서 고른다.",
            [
                _link_item(
                    label=item["title"],
                    href=_page_href("/explore", object_id=item["id"]),
                    note=item["note"],
                    active=item["id"] == source["selected_asset_id"],
                )
                for item in source["asset_items"]
            ],
        )
    )
    main_html = _render_main_stack(
        "객체를 기준으로 이어질 내용을 훑어본다",
        [
            _candidate_list_card(
                "이어 읽을 연결 목록",
                [
                    {
                        "label": candidate["title"],
                        "href": _page_href("/explore", object_id=source["selected_asset_id"], candidate_id=candidate["id"]),
                        "active": candidate["id"] == selected_candidate.get("id"),
                        "meta": f"층위 {candidate['layer']}",
                        "preview": candidate_reading.get(candidate["id"], {}).get("value_paragraph_text") or candidate["original_preview"],
                    }
                    for candidate in candidates
                ],
            )
        ],
    )
    right_html = _render_detail_stack(
        "선택한 연결을 읽는 자리",
        _build_explore_detail_blocks(selected_candidate=selected_candidate, reading_context=reading_context),
    )
    save_href = None
    if selected_candidate.get("id") and _can_save_explore_candidate(selected_candidate=selected_candidate, reading_context=reading_context):
        save_href = _page_href(
            "/actions/save-explore-candidate",
            asset_id=source["selected_asset_id"],
            candidate_id=selected_candidate.get("id"),
        )
    save_card = (
        "<div class='panel-card'>"
        "<h3>이 연결을 남긴다</h3>"
        + (
            f"<a class='link-item' href='{escape(save_href)}'><strong>기억에 연결 저장</strong><small>저장하면 기억 페이지에서 바로 다시 읽을 수 있다.</small></a>"
            if save_href
            else "<div class='panel-note'>아직 저장할 연결이 없어 이 자리는 비워 둔다.</div>"
        )
        + "</div>"
    )
    return _render_shell(
        page_title="탐색",
        page_heading="탐색",
        page_subtitle="객체를 중심에 두고 이어질 연결을 읽으며 원본과 층위를 함께 살피는 자리",
        active_key="탐색",
        left_html=left_html,
        main_html=main_html,
        right_html=right_html + save_card,
    )


def render_user_search_page(
    runtime_root: Path,
    *,
    q: str = "",
    mode: str = "object",
    result_id: Optional[str] = None,
) -> str:
    source = _build_source(
        runtime_root,
        page_key="search",
        mode_hint="space_reading",
    )
    options = [
        ("object", "객체"),
        ("original", "원본 단어"),
        ("label", "라벨"),
        ("anchor", "앵커"),
        ("axis", "축값"),
    ]
    results = _build_search_results(source)
    filtered = _filter_search_results(results, q=q, mode=mode)
    selected_result = _pick_by_id(filtered, result_id) or (filtered[0] if filtered else None)
    option_html = "".join(
        f"<option value='{escape(value)}' {'selected' if value == mode else ''}>{escape(label)}</option>"
        for value, label in options
    )
    left_html = (
        "<div class='panel-card'>"
        "<h3>무엇을 기준으로 찾을지 정한다</h3>"
        "<div class='panel-note'>원본과 이름표를 기준으로 바로 찾아 들어갈 수 있게, 지금은 얇은 기준만 둔다.</div>"
        f"<form method='get' action='/search' class='search-form'>"
        f"<input class='text-input' type='text' name='q' value='{escape(q)}' placeholder='원본 단어, 객체 이름, 라벨을 적는다' />"
        f"<select class='select-input' name='mode'>{option_html}</select>"
        "<button class='submit-button' type='submit'>찾기</button>"
        "</form>"
        "</div>"
    )
    main_html = _render_main_stack(
        "찾은 결과를 훑어보고 고른다",
        [
            _candidate_list_card(
                "바로 읽을 결과 목록",
                [
                    {
                        "label": item["title"],
                        "href": _page_href("/search", q=q, mode=mode, result_id=item["id"]),
                        "active": item["id"] == (selected_result or {}).get("id"),
                        "meta": f"{item['kind']} / {item['matched_by']}",
                        "preview": item["summary"],
                    }
                    for item in filtered
                ]
                or [
                    {
                        "label": "찾은 결과 없음",
                        "href": "#",
                        "active": False,
                        "meta": "지금 기준에서는 비어 있음",
                        "preview": "지금 찾은 결과가 없어도 이 자리는 그대로 둔다.",
                        "disabled": True,
                    }
                ],
            )
        ],
    )
    right_html = _render_detail_stack(
        "선택한 결과를 읽는 자리",
        [
            _detail_block("원본", (selected_result or {}).get("original") or "아직 읽을 결과를 고르지 않아 이 자리는 비워 둔다."),
            _detail_block("요약", (selected_result or {}).get("summary") or "아직 함께 읽을 요약은 없다."),
            _detail_block("이어 읽을 연결", (selected_result or {}).get("connection_hint") or "아직 이어 읽을 연결은 또렷하지 않다."),
        ],
    )
    return _render_shell(
        page_title="찾기",
        page_heading="찾기",
        page_subtitle="무엇을 기준으로 찾을지 정한 뒤, 바로 읽을 결과로 들어가는 자리",
        active_key="찾기",
        left_html=left_html,
        main_html=main_html,
        right_html=right_html,
    )


def render_user_memory_page(runtime_root: Path, *, connection_id: Optional[str] = None) -> str:
    source = _build_source(
        runtime_root,
        page_key="memory",
        mode_hint="reflection",
    )
    connections = _build_memory_connections(source["saved_connections"])
    selected = _pick_by_id(connections, connection_id) or (connections[0] if connections else None)
    left_html = _render_link_list(
        "쌓인 연결을 다시 고른다",
        "남겨 둔 연결이 여기 쌓이고, 다시 보고 싶은 연결을 여기서 고른다.",
        [
            _link_item(
                label=item["title"],
                href=_page_href("/memory", connection_id=item["id"]),
                note=item["summary"],
                active=item["id"] == (selected or {}).get("id"),
            )
            for item in connections
        ],
    )
    main_html = _render_main_stack(
        "선택한 연결을 원본에서 다시 읽는다",
        [
            _content_card(
                "원본을 다시 읽는 자리",
                [f"<div class='body-copy'>{escape((selected or {}).get('original') or '아직 쌓인 연결이 없어 원본을 다시 읽을 자리는 비워 둔다.')}</div>"],
            ),
            _content_card(
                "붙잡아 둔 연결 요약",
                [f"<div class='segment-row'>{escape((selected or {}).get('summary') or '아직 붙잡아 둔 연결 요약은 없다.')}</div>"],
            ),
        ],
    )
    right_html = _render_detail_stack(
        "선택한 연결을 읽는 자리",
        [
            _detail_block("층위", (selected or {}).get("layer") or "층위가 아직 없다."),
            _detail_block("요약", (selected or {}).get("summary") or "아직 함께 볼 요약은 없다."),
            _detail_block("남긴 시점", (selected or {}).get("created_at") or "아직 남긴 시점 단서는 없다."),
            _detail_block("출처 단서", (selected or {}).get("source_pointer") or "아직 출처 단서는 없다."),
            _detail_block("스티커", (selected or {}).get("sticker_note") or "남겨 둔 연결은 스티커와 함께 여기서 다시 본다."),
        ],
    )
    return _render_shell(
        page_title="기억",
        page_heading="기억",
        page_subtitle="남겨 둔 연결을 다시 꺼내 원본과 함께 읽는 자리",
        active_key="기억",
        left_html=left_html,
        main_html=main_html,
        right_html=right_html,
    )


def render_user_similar_page(
    runtime_root: Path,
    *,
    seed_id: Optional[str] = None,
    similar_id: Optional[str] = None,
) -> str:
    source = _build_source(
        runtime_root,
        page_key="similar",
        mode_hint="reflection",
    )
    seeds = _build_memory_connections(source["saved_connections"])
    selected_seed = _pick_by_id(seeds, seed_id) or (seeds[0] if seeds else None)
    similar_items = _build_similar_connections(selected_seed)
    selected_similar = _pick_by_id(similar_items, similar_id) or (similar_items[0] if similar_items else None)
    left_html = _render_link_list(
        "어떤 연결을 기준으로 볼지 고른다",
        "여기서 기준 연결을 잡고, 그 옆으로 닮은 흐름을 넓혀 읽는다.",
        [
            _link_item(
                label=item["title"],
                href=_page_href("/similar", seed_id=item["id"]),
                note=item["summary"],
                active=item["id"] == (selected_seed or {}).get("id"),
            )
            for item in seeds
        ],
    )
    main_html = _render_main_stack(
        "닮아 이어지는 흐름을 훑어본다",
        [
            _candidate_list_card(
                "기준 연결 옆으로 이어지는 흐름",
                [
                    {
                        "label": item["title"],
                        "href": _page_href("/similar", seed_id=(selected_seed or {}).get("id"), similar_id=item["id"]),
                        "active": item["id"] == (selected_similar or {}).get("id"),
                        "meta": f"층위 {item['layer']}",
                        "preview": item["summary"],
                    }
                    for item in similar_items
                ]
                or [
                    {
                        "label": "아직 기준으로 잡은 연결이 없다",
                        "href": "#",
                        "active": False,
                        "meta": "기억에 연결이 쌓이면 여기서 옆으로 넓혀 읽는다.",
                        "preview": "지금은 흐름을 읽을 자리를 먼저 세워 둔다.",
                        "disabled": True,
                    }
                ],
            )
        ],
    )
    right_html = _render_detail_stack(
        "선택한 연결을 읽는 자리",
        [
            _detail_block("원본", (selected_similar or {}).get("original") or "아직 읽을 연결을 고르지 않았다."),
            _detail_block("층위", (selected_similar or {}).get("layer") or "층위가 아직 없다."),
            _detail_block("요약", (selected_similar or {}).get("summary") or "아직 함께 읽을 요약은 없다."),
        ],
    )
    return _render_shell(
        page_title="비슷한 연결",
        page_heading="비슷한 연결",
        page_subtitle="기준 연결을 중심에 두고 닮아 이어지는 흐름을 옆으로 넓혀 읽는 자리",
        active_key="비슷한 연결",
        left_html=left_html,
        main_html=main_html,
        right_html=right_html,
    )


def _render_shell(
    *,
    page_title: str,
    page_heading: str,
    page_subtitle: str,
    active_key: str,
    left_html: str,
    main_html: str,
    right_html: str,
) -> str:
    nav_html = "".join(
        f"<a class='nav-link {'active' if label == active_key else ''}' href='{href}'>{escape(label)}</a>"
        for label, href in CORE_NAV
    )
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(page_title)}</title>
  <style>
    :root {{
      --bg: #f2ede4;
      --panel: #fffaf1;
      --line: #dbcdb8;
      --ink: #2f2418;
      --muted: #756a5b;
      --accent: #c77f38;
      --accent-soft: #f1dfc8;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: linear-gradient(180deg, #f8f2e9 0%, var(--bg) 100%); color: var(--ink); font-family: "Iowan Old Style", "Palatino Linotype", serif; }}
    .page {{ max-width: 1500px; margin: 0 auto; padding: 24px; display: grid; gap: 16px; }}
    .topbar {{ display: grid; gap: 12px; padding: 16px 18px; background: var(--panel); border: 1px solid var(--line); border-radius: 22px; }}
    .nav-row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .nav-link {{ text-decoration: none; color: var(--ink); background: #fff; border: 1px solid var(--line); border-radius: 999px; padding: 8px 12px; font-size: 14px; }}
    .nav-link.active {{ background: var(--accent-soft); border-color: #b97631; }}
    .nav-link.companion {{ border-style: dashed; }}
    .title-row strong {{ display: block; font-size: 28px; }}
    .title-row span {{ color: var(--muted); font-size: 14px; }}
    .shell {{ display: grid; grid-template-columns: 280px minmax(0, 1fr) 320px; gap: 16px; align-items: start; }}
    .column {{ background: var(--panel); border: 1px solid var(--line); border-radius: 22px; padding: 16px; display: grid; gap: 14px; min-height: 70vh; }}
    .column h2 {{ margin: 0; font-size: 20px; }}
    .panel-card {{ border: 1px solid #e9dcc8; border-radius: 16px; background: #fff; padding: 14px; display: grid; gap: 10px; }}
    .panel-card h3 {{ margin: 0; font-size: 17px; }}
    .panel-note {{ color: var(--muted); font-size: 13px; }}
    .link-list {{ display: grid; gap: 8px; }}
    .link-item {{ display: block; text-decoration: none; color: var(--ink); border: 1px solid #e7dbc8; border-radius: 14px; background: #fff; padding: 12px; }}
    .link-item.active {{ border-color: #b97631; background: #fff4e8; }}
    .link-item.disabled {{ pointer-events: none; opacity: 0.75; }}
    .link-item strong {{ display: block; margin-bottom: 4px; }}
    .link-item small {{ display: block; color: var(--muted); }}
    .content-card {{ border: 1px solid #e7dbc8; border-radius: 18px; background: #fff; padding: 16px; display: grid; gap: 10px; }}
    .content-card h3 {{ margin: 0; font-size: 18px; }}
    .segment-row, .body-copy {{ border: 1px solid #efe4d3; border-radius: 12px; background: #fffcf7; padding: 10px 12px; }}
    .segment-row {{ display: block; text-decoration: none; color: var(--ink); }}
    .segment-row.active {{ border-color: #b97631; background: #fff4e8; }}
    .source-full {{ white-space: pre-wrap; line-height: 1.55; }}
    .source-highlight {{ background: #fff1c9; border-radius: 6px; padding: 1px 2px; }}
    .source-chip {{ display: inline-flex; align-items: center; margin: 0 8px 8px 0; padding: 7px 10px; border-radius: 999px; background: #f4ead8; color: #6d5437; font-size: 12px; }}
    .detail-block {{ border: 1px solid #e7dbc8; border-radius: 16px; background: #fff; padding: 14px; display: grid; gap: 6px; }}
    .detail-block strong {{ font-size: 14px; color: #5d4a35; }}
    .detail-block span {{ color: var(--ink); line-height: 1.5; }}
    .text-input, .select-input {{ width: 100%; border: 1px solid var(--line); border-radius: 12px; padding: 10px 12px; font: inherit; background: #fff; }}
    .search-form {{ display: grid; gap: 10px; }}
    .submit-button {{ border: 1px solid #b97631; border-radius: 12px; padding: 10px 12px; background: var(--accent-soft); color: #3f2a13; font: inherit; cursor: pointer; }}
    @media (max-width: 1100px) {{
      .shell {{ grid-template-columns: 1fr; }}
      .column {{ min-height: auto; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="topbar">
      <div class="nav-row">
        {nav_html}
        <a class="nav-link companion" href="/operating-ui-history">히스토리 보조</a>
      </div>
      <div class="title-row">
        <strong>{escape(page_heading)}</strong>
        <span>{escape(page_subtitle)}</span>
      </div>
    </div>
    <div class="shell">
      <aside class="column">{left_html}</aside>
      <main class="column">{main_html}</main>
      <aside class="column">{right_html}</aside>
    </div>
  </div>
</body>
</html>"""


def _build_source(
    runtime_root: Path,
    *,
    asset_id: Optional[str] = None,
    selected_row_key: Optional[str] = None,
    page_key: Optional[str] = None,
    mode_hint: Optional[str] = None,
) -> Dict[str, Any]:
    live = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    stickers = load_phase1_memory_stickers(runtime_root)
    preflight = build_runtime_preflight(
        runtime_root,
        requested_mode=mode_hint,
        requested_artifact_ref=asset_id,
        page_key=page_key,
    )
    raw_assets = live.get("available_assets") or []
    asset_items: List[Dict[str, str]] = []
    for asset in raw_assets:
        asset_items.append(
            {
                "id": str(asset.get("id") or ""),
                "title": str(asset.get("title") or asset.get("id") or "이름 없는 입력"),
                "note": "원본에서 다시 읽을 수 있다.",
            }
        )
    selected_asset = ((live.get("adapted_model") or {}).get("selectedAsset") or {}) if live.get("state") == "loaded" else {}
    typed_object = False
    known_asset_ids = {item["id"] for item in asset_items}
    selected_asset_id = str(live.get("selected_asset_id") or asset_id or (asset_items[0]["id"] if asset_items else ""))
    unknown_requested_object = bool(asset_id and asset_id not in known_asset_ids)
    if unknown_requested_object:
        selected_asset_id = str(asset_id)
        selected_asset = {}
    if not selected_asset and asset_id:
        typed_object = True
        selected_asset = {
            "id": asset_id,
            "title": asset_id,
            "stateNotes": "새로 적은 객체라 아직 연결 단서는 얇다.",
            "evidenceRefs": [],
            "canonicalStateRows": [],
            "compareReasons": [],
        }
    elif not selected_asset and asset_items:
        selected_asset = {
            "title": asset_items[0]["title"],
            "stateNotes": "원본 메모는 다음 연결에서 더 채워진다.",
            "evidenceRefs": [],
            "canonicalStateRows": [],
            "compareReasons": [],
        }
    return {
        "live": live,
        "preflight": preflight,
        "asset_items": asset_items or [{"id": "sample-input", "title": "예시 입력", "note": "레이아웃 확인용 입력"}],
        "selected_asset_id": selected_asset_id or "sample-input",
        "typed_object": typed_object,
        "selected_row_key": selected_row_key or "packet_texture",
        "selected_asset": _normalize_asset(
            selected_asset,
            fallback_id=selected_asset_id or "sample-input",
            selected_row_key=selected_row_key or "packet_texture",
        ),
        "raw_selected_asset": selected_asset,
        "saved_connections": load_saved_connections(runtime_root),
        "stickers": stickers,
    }


def _normalize_asset(asset: Dict[str, Any], *, fallback_id: str, selected_row_key: str) -> Dict[str, Any]:
    evidence_refs = asset.get("evidenceRefs") or []
    source_pointer = _find_source_pointer(evidence_refs)
    original_refs = [
        _readable_original_ref(str(ref.get("label") or ref.get("id") or "원본 단서"))
        for ref in evidence_refs[:4]
        if isinstance(ref, dict)
    ]
    if not original_refs:
        original_refs = [f"{fallback_id} 원본 자리"]
    segments = [
        str(row.get("label") or row.get("key") or "분절")
        for row in (asset.get("canonicalStateRows") or [])[:6]
        if isinstance(row, dict)
    ]
    segment_rows = _build_operating_segment_rows(
        asset_id=fallback_id,
        canonical_rows=asset.get("canonicalStateRows") or [],
        source_pointer=source_pointer,
    )
    source_context = _build_operating_source_context(
        asset_id=fallback_id,
        canonical_rows=asset.get("canonicalStateRows") or [],
        source_pointer=source_pointer,
        selected_row_key=selected_row_key,
    )
    full_source_text = _read_full_source_text(source_pointer)
    return {
        "id": fallback_id,
        "title": str(asset.get("title") or fallback_id or "이름 없는 입력"),
        "original_refs": original_refs,
        "segments": segments,
        "segment_rows": segment_rows,
        "source_context": source_context,
        "full_source_text": full_source_text,
        "body_note": str(asset.get("stateNotes") or "원본 메모가 아직 짧다."),
        "summary": " / ".join(segments[:3]) if segments else "선택 입력 요약이 아직 짧다.",
        "connection_hint": ", ".join(_readable_connection_hint(str(item)) for item in (asset.get("compareReasons") or [])[:3]) or "다음에 이어 볼 단서는 뒤에서 더 또렷해진다.",
        "sticker_slot": "이 입력에서 살아남는 연결만 이후 스티커로 남긴다.",
    }


def _build_explore_candidates(asset: Dict[str, Any], *, raw_asset: Optional[Dict[str, Any]] = None) -> List[Dict[str, str]]:
    raw = raw_asset or {}
    candidates = extract_explore_candidates(
        raw_asset=raw,
        fallback_object=str(asset.get("title") or "선택 객체"),
        readable_original_refs=list(asset.get("original_refs") or []),
    )
    row_order = {
        str(row.get("key") or ""): index
        for index, row in enumerate(raw.get("canonicalStateRows") or [])
        if isinstance(row, dict)
    }
    projected: List[Dict[str, Any]] = []
    for candidate in candidates:
        merged = dict(candidate)
        merged.update(project_candidate_rule_binding(candidate))
        projected.append(merged)
    return sorted(projected, key=lambda candidate: _explore_candidate_sort_key(candidate, row_order=row_order))


def _build_search_results(source: Dict[str, Any]) -> List[Dict[str, str]]:
    results: List[Dict[str, str]] = []
    for item in source["asset_items"]:
        results.append(
            {
                "id": f"object:{item['id']}",
                "title": item["title"],
                "kind": "객체 결과",
                "matched_by": "객체 기준",
                "original": f"{item['title']} 원본 자리",
                "summary": "원본을 기준으로 바로 다시 읽을 수 있는 결과",
                "connection_hint": "탐색으로 이어 읽을 수 있다",
                "object": item["title"],
                "original_token": item["title"],
                "label": "입력 객체",
                "anchor": item["id"],
                "axis": "원본축",
            }
        )
    for sticker in source["stickers"]:
        title = sticker.get("preview_connection_summary") or sticker.get("sticker_id") or "저장 연결"
        results.append(
            {
                "id": f"memory:{sticker.get('sticker_id')}",
                "title": title,
                "kind": "저장된 연결",
                "matched_by": "라벨 기준",
                "original": sticker.get("object_id") or "원본 자리",
                "summary": sticker.get("why_selected_short") or "저장된 연결 요약",
                "connection_hint": sticker.get("lens_id") or "연결축",
                "object": sticker.get("object_id") or "",
                "original_token": title,
                "label": sticker.get("why_selected_short") or "",
                "anchor": sticker.get("seed_ref") or "",
                "axis": sticker.get("position_value") or "",
            }
        )
    return results


def _filter_search_results(results: List[Dict[str, str]], *, q: str, mode: str) -> List[Dict[str, str]]:
    query = (q or "").strip().lower()
    if not query:
        return results[:8]
    field_map = {
        "object": "object",
        "original": "original_token",
        "label": "label",
        "anchor": "anchor",
        "axis": "axis",
    }
    field = field_map.get(mode, "object")
    filtered = [item for item in results if query in str(item.get(field) or "").lower()]
    if filtered:
        return filtered
    return [item for item in results if query in " ".join(str(item.get(key) or "") for key in field_map.values()).lower()]


def _build_memory_connections(saved_connections: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if saved_connections:
        return [
            {
                "id": connection["id"],
                "title": _memory_connection_title(connection),
                "original": connection.get("value_paragraph_text") or connection.get("object_paragraph_text") or "원본 자리",
                "layer": connection.get("value_label") or connection.get("primary_rule_key") or "층위 자리",
                "summary": connection.get("relation_summary") or "남겨 둔 연결 요약",
                "created_at": _readable_saved_at(connection.get("created_at") or ""),
                "source_pointer": connection.get("value_source_pointer") or connection.get("object_source_pointer") or "",
                "sticker_note": str((connection.get("sticker") or {}).get("note") or "남겨 둔 연결 기준으로 붙잡아 둔 자리"),
                "object_paragraph_text": connection.get("object_paragraph_text") or "",
                "object_paragraph_ref": connection.get("object_paragraph_ref") or "",
                "value_paragraph_ref": connection.get("value_paragraph_ref") or "",
                "scene": connection.get("scene") or "",
                "flow": connection.get("flow") or "",
                "primary_rule_key": connection.get("primary_rule_key") or "",
                "support_rule_keys": ", ".join(connection.get("support_rule_keys") or []),
            }
            for connection in saved_connections
        ]
    return [
        {
            "id": "sample-connection",
            "title": "예시 연결",
            "original": "원본 자리 예시",
            "layer": "층위 자리 예시",
            "summary": "아직 남겨 둔 연결이 없을 때 자리만 보여주는 예시",
            "created_at": "",
            "source_pointer": "",
            "sticker_note": "예시 자리일 뿐 실제로 남겨 둔 연결은 아님",
        }
    ]


def _build_similar_connections(seed: Optional[Dict[str, str]]) -> List[Dict[str, str]]:
    if not seed:
        return []
    base_title = seed.get("title") or "기준 연결"
    base_original = seed.get("original") or "원본 자리"
    return [
        {
            "id": f"{seed['id']}:near",
            "title": f"{base_title} / 인접 흐름",
            "original": base_original,
            "layer": "인접층",
            "summary": "원본 결을 크게 바꾸지 않고 가까운 흐름부터 다시 읽는다.",
        },
        {
            "id": f"{seed['id']}:bridge",
            "title": f"{base_title} / 다리 흐름",
            "original": base_original,
            "layer": "연결층",
            "summary": "기준 연결에서 다른 쪽으로 얇게 이어지는 흐름이다.",
        },
        {
            "id": f"{seed['id']}:echo",
            "title": f"{base_title} / 반향 흐름",
            "original": base_original,
            "layer": "반향층",
            "summary": "요약보다 원본 결을 남기며 닮은 흐름을 다시 읽는다.",
        },
    ]


def _render_link_list(title: str, note: str, items: List[Dict[str, Any]]) -> str:
    return (
        f"<div class='panel-card'><h3>{escape(title)}</h3><div class='panel-note'>{escape(note)}</div>"
        + "<div class='link-list'>"
        + "".join(_render_link_item(item) for item in items)
        + "</div></div>"
    )


def _render_link_item(item: Dict[str, Any]) -> str:
    classes = ["link-item"]
    if item.get("active"):
        classes.append("active")
    if item.get("disabled"):
        classes.append("disabled")
    return (
        f"<a class='{' '.join(classes)}' href='{escape(item.get('href') or '#')}'><strong>{escape(item.get('label') or '')}</strong>"
        f"<small>{escape(item.get('note') or '')}</small></a>"
    )


def _link_item(*, label: str, href: str, note: str, active: bool = False) -> Dict[str, Any]:
    return {"label": label, "href": href, "note": note, "active": active}


def _render_main_stack(title: str, cards: List[str]) -> str:
    return f"<h2>{escape(title)}</h2>" + "".join(cards)


def _content_card(title: str, body_items: List[str]) -> str:
    return f"<div class='content-card'><h3>{escape(title)}</h3>{''.join(body_items)}</div>"


def _candidate_list_card(title: str, items: List[Dict[str, Any]]) -> str:
    rendered = []
    for item in items:
        classes = ["link-item"]
        if item.get("active"):
            classes.append("active")
        if item.get("disabled"):
            classes.append("disabled")
        rendered.append(
            f"<a class='{' '.join(classes)}' href='{escape(item.get('href') or '#')}'><strong>{escape(item.get('label') or '')}</strong>"
            f"<small>{escape(item.get('meta') or '')}</small><small>{escape(item.get('preview') or '')}</small></a>"
        )
    return f"<div class='content-card'><h3>{escape(title)}</h3><div class='link-list'>{''.join(rendered)}</div></div>"


def _render_detail_stack(title: str, blocks: List[str]) -> str:
    return f"<h2>{escape(title)}</h2>" + "".join(blocks)


def _detail_block(title: str, body: str) -> str:
    return f"<div class='detail-block'><strong>{escape(title)}</strong><span>{escape(body)}</span></div>"


def _pick_by_id(items: List[Dict[str, Any]], item_id: Optional[str]) -> Optional[Dict[str, Any]]:
    if not item_id:
        return None
    for item in items:
        if item.get("id") == item_id:
            return item
    return None


def _page_href(path: str, **query: Optional[str]) -> str:
    clean = {key: value for key, value in query.items() if value not in (None, "")}
    if not clean:
        return path
    return f"{path}?{urlencode(clean)}"


def _readable_original_ref(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return "원본 단서"
    prefixes = {
        "source_file: ": "원문이 담긴 파일 ",
        "probe_output: ": "살펴본 기록 ",
    }
    for prefix, replacement in prefixes.items():
        if text.startswith(prefix):
            return replacement + text[len(prefix):]
    return text.replace("_", " ")


def _readable_connection_hint(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    mapping = {
        "breathing_contrast": "호흡 대비",
    }
    return mapping.get(text, text.replace("_", " "))


def _readable_saved_at(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    return text.replace("T", " ").replace("+00:00", " UTC")


def _find_source_pointer(evidence_refs: List[Dict[str, Any]]) -> str:
    for ref in evidence_refs:
        if not isinstance(ref, dict):
            continue
        if ref.get("kind") == "source_file":
            return str(ref.get("id") or "")
    return ""


def _build_operating_source_context(
    *,
    asset_id: str,
    canonical_rows: List[Dict[str, Any]],
    source_pointer: str,
    selected_row_key: str,
) -> Dict[str, str]:
    if not source_pointer:
        return {}
    selected_row = next(
        (row for row in canonical_rows if isinstance(row, dict) and str(row.get("key") or "") == selected_row_key),
        None,
    )
    if not selected_row:
        return {}
    try:
        context = extract_segment_source_context(
            asset_id=asset_id,
            state_row_key=selected_row_key,
            source_pointer=source_pointer,
        )
        if context.get("match_confidence") == "low":
            return {}
        return context
    except Exception:
        return {}


def _build_operating_segment_rows(
    *,
    asset_id: str,
    canonical_rows: List[Dict[str, Any]],
    source_pointer: str,
) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for row in canonical_rows[:6]:
        if not isinstance(row, dict):
            continue
        row_key = str(row.get("key") or "")
        item = {
            "key": row_key,
            "label": str(row.get("label") or row_key or "분절"),
            "paragraph_ref": "",
            "paragraph_text": "",
        }
        if source_pointer and row_key:
            try:
                context = extract_segment_source_context(
                    asset_id=asset_id,
                    state_row_key=row_key,
                    source_pointer=source_pointer,
                )
                if context.get("match_confidence") in {"high", "medium"}:
                    item["paragraph_ref"] = context.get("paragraph_ref") or ""
                    item["paragraph_text"] = context.get("paragraph_text") or ""
            except Exception:
                pass
        rows.append(item)
    return rows


def _read_full_source_text(source_pointer: str) -> str:
    if not source_pointer:
        return ""
    try:
        return Path(source_pointer).read_text(encoding="utf-8").strip()
    except Exception:
        return ""


def _build_explore_reading_context(
    *,
    asset_id: str,
    raw_asset: Dict[str, Any],
    candidate: Dict[str, Any],
) -> Dict[str, str]:
    source_pointer = _find_source_pointer(raw_asset.get("evidenceRefs") or [])
    if not source_pointer:
        return {}

    context: Dict[str, str] = {}
    try:
        object_context = extract_object_source_context(source_pointer=source_pointer)
        context["source_pointer"] = source_pointer
        context["object_source_pointer"] = source_pointer
        context["object_paragraph_ref"] = object_context.get("paragraph_ref") or ""
        context["object_paragraph_text"] = object_context.get("paragraph_text") or ""
        context["object_surrounding_context"] = object_context.get("surrounding_context") or ""
    except Exception:
        pass

    if str(candidate.get("candidate_kind") or "") == "evidence" and str(candidate.get("source_kind") or "") != "source_file":
        return context

    row_key = _resolve_candidate_row_key(candidate=candidate)
    if not row_key:
        return context

    try:
        value_context = extract_segment_source_context(
            asset_id=asset_id,
            state_row_key=row_key,
            source_pointer=source_pointer,
        )
        if value_context.get("match_confidence") in {"high", "medium"}:
            context["value_paragraph_ref"] = value_context.get("paragraph_ref") or ""
            context["value_paragraph_text"] = value_context.get("paragraph_text") or ""
            context["value_surrounding_context"] = value_context.get("surrounding_context") or ""
            context["value_source_pointer"] = source_pointer
    except Exception:
        pass
    return context


def _resolve_candidate_row_key(*, candidate: Dict[str, Any]) -> str:
    row_key = str(candidate.get("row_key") or "").strip()
    if row_key:
        return row_key
    row_key = str(candidate.get("support_row_key") or "").strip()
    return row_key


def _build_explore_detail_blocks(*, selected_candidate: Dict[str, Any], reading_context: Dict[str, str]) -> List[str]:
    blocks = [
        _detail_block("읽는 기준", _explore_reading_basis(selected_candidate)),
        _detail_block("객체 문장", reading_context.get("object_paragraph_text") or "아직 객체 쪽에서 바로 읽을 문장을 찾지 못했다."),
        _detail_block("객체 문맥", reading_context.get("object_surrounding_context") or "아직 객체 쪽 주변 문맥을 찾지 못했다."),
        _detail_block("값 문장", reading_context.get("value_paragraph_text") or "아직 값 쪽에서 바로 읽을 문장을 찾지 못했다."),
        _detail_block("값 문맥", reading_context.get("value_surrounding_context") or "아직 값 쪽 주변 문맥을 찾지 못했다."),
        _detail_block("원본", selected_candidate.get("original_preview") or "아직 원본을 바로 읽을 부분이 없다."),
        _detail_block("층위", selected_candidate.get("layer") or "층위가 아직 없다."),
    ]
    if str(selected_candidate.get("candidate_kind") or "") == "reason":
        blocks.append(_detail_block("비교 단서", _readable_compare_reason(str(selected_candidate.get("source_pointer") or "")) or "아직 비교 단서가 또렷하지 않다."))
        blocks.append(_detail_block("이 단서를 읽는 층위", selected_candidate.get("layer") or "아직 이 단서를 읽는 층위가 또렷하지 않다."))
    blocks.extend(
        [
            _detail_block("의미", selected_candidate.get("meaning") or "아직 이 연결에서 읽히는 뜻이 또렷하지 않다."),
            _detail_block("스티커", selected_candidate.get("sticker_slot") or "남겨 둘 연결만 스티커로 붙인다."),
        ]
    )
    return blocks


def _readable_compare_reason(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    return text.replace("_", " ")


def _explore_reading_basis(candidate: Dict[str, Any]) -> str:
    kind = str(candidate.get("candidate_kind") or "")
    source_kind = str(candidate.get("source_kind") or "")
    if kind == "state":
        return "이 후보는 객체가 어떤 층위로 읽히는지 먼저 본다."
    if kind == "evidence" and source_kind == "source_file":
        return "이 후보는 원문 단서에서 연결을 다시 읽는다."
    if kind == "evidence":
        return "이 후보는 남아 있는 기록 단서를 다시 확인한다."
    if kind == "reason":
        return "이 후보는 새 연결을 더 낳을 수 있는 단서를 읽는다."
    return "이 후보에서 이어 읽을 연결 가능성을 먼저 본다."


def _explore_candidate_sort_key(candidate: Dict[str, Any], *, row_order: Dict[str, int]) -> tuple[int, int, str]:
    kind = str(candidate.get("candidate_kind") or "")
    source_kind = str(candidate.get("source_kind") or "")
    if kind == "state":
        priority = 0
    elif kind == "evidence" and source_kind == "source_file":
        priority = 1
    elif kind == "evidence":
        priority = 2
    elif kind == "reason":
        priority = 3
    else:
        priority = 4
    row_key = str(candidate.get("row_key") or "")
    row_position = row_order.get(row_key, 999)
    return (priority, row_position, str(candidate.get("title") or ""))


def _memory_connection_title(connection: Dict[str, Any]) -> str:
    object_label = str(connection.get("object_label") or "").strip()
    value_label = str(connection.get("value_label") or "").strip()
    if object_label and value_label:
        return f"{object_label} -> {value_label}"
    return str(connection.get("title") or connection.get("id") or "저장 연결").strip()


def _can_save_explore_candidate(*, selected_candidate: Dict[str, Any], reading_context: Dict[str, str]) -> bool:
    if not selected_candidate.get("id"):
        return False
    if not reading_context.get("object_paragraph_text"):
        return False
    if not reading_context.get("value_paragraph_text"):
        return False
    return True


def _render_full_source_block(*, full_source_text: str, selected_paragraph: str) -> str:
    escaped_source = escape(full_source_text)
    if selected_paragraph:
        escaped_paragraph = escape(selected_paragraph)
        if escaped_paragraph in escaped_source:
            escaped_source = escaped_source.replace(
                escaped_paragraph,
                f"<span class='source-highlight'>{escaped_paragraph}</span>",
                1,
            )
    return f"<div class='body-copy source-full'>{escaped_source}</div>"
