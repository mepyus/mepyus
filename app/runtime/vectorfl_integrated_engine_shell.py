from __future__ import annotations

from typing import Any, Dict, Iterable
import html
import json


def _esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""))


def _chip(value: Any, *, tone: str = "") -> str:
    cls = f"chip {tone}".strip()
    return f'<span class="{cls}">{_esc(value)}</span>'


def _chips(values: Iterable[Any]) -> str:
    items = list(values)
    if not items:
        return _chip("none")
    return "".join(_chip(item) for item in items)


def _select_options(items: Dict[str, Dict[str, Any]], selected: str = "") -> str:
    options = []
    for key, info in items.items():
        selected_attr = " selected" if key == selected else ""
        label = info.get("label") or key
        options.append(f'<option value="{_esc(key)}"{selected_attr}>{_esc(label)}</option>')
    return "".join(options)


def _current_run_freshness(
    *,
    operating_dialogue: Dict[str, Any],
    launch_draft: Dict[str, Any],
    worker_execution: Dict[str, Any],
) -> Dict[str, Any]:
    """Return conservative posture for whether the latest execution proves the current draft."""
    raw_status = str(worker_execution.get("status") or "").strip()
    dialogue_object_id = operating_dialogue.get("operating_object_id") or ""
    dialogue_fingerprint = operating_dialogue.get("content_fingerprint") or ""
    draft_object_id = launch_draft.get("operating_object_id") or ""
    draft_dialogue_fingerprint = launch_draft.get("source_operating_dialogue_fingerprint") or ""
    draft_is_current = bool(launch_draft) and (
        (not dialogue_object_id or draft_object_id == dialogue_object_id)
        and (not dialogue_fingerprint or draft_dialogue_fingerprint == dialogue_fingerprint)
    )
    current_object_id = dialogue_object_id or draft_object_id
    execution_object_id = worker_execution.get("operating_object_id") or ""
    current_draft_fingerprint = launch_draft.get("content_fingerprint") if draft_is_current else ""
    execution_source_fingerprint = worker_execution.get("source_worker_launch_draft_fingerprint") or ""
    selected_worker = operating_dialogue.get("selected_worker") or launch_draft.get("selected_worker") or ""
    execution_worker = worker_execution.get("worker") or ""

    object_matches = bool(current_object_id) and current_object_id == execution_object_id
    draft_matches = bool(current_draft_fingerprint) and current_draft_fingerprint == execution_source_fingerprint
    worker_matches = not selected_worker or not execution_worker or selected_worker == execution_worker
    is_current_execution = object_matches and draft_matches and worker_matches

    if raw_status == "completed":
        if is_current_execution:
            posture = "current_run_completed"
        elif draft_is_current:
            posture = "draft_created"
        else:
            posture = "completed_but_not_current"
    elif raw_status == "failed":
        posture = "execution_failed" if is_current_execution else "draft_created" if draft_is_current else "idle"
    elif raw_status == "timeout":
        posture = "execution_timeout" if is_current_execution else "draft_created" if draft_is_current else "idle"
    elif raw_status in {"running", "execution_running"}:
        posture = "execution_running" if is_current_execution else "draft_created" if draft_is_current else "idle"
    elif draft_is_current:
        posture = "draft_created"
    else:
        posture = "idle"

    return {
        "posture": posture,
        "is_current_execution": is_current_execution,
        "object_matches": object_matches,
        "draft_matches": draft_matches,
        "worker_matches": worker_matches,
        "draft_is_current": draft_is_current,
        "current_object_id": current_object_id,
        "current_draft_fingerprint": current_draft_fingerprint,
        "execution_source_fingerprint": execution_source_fingerprint,
        "raw_status": raw_status,
    }


def _execution_posture_label(posture: str) -> str:
    labels = {
        "current_run_completed": "현재 실행 완료",
        "completed_but_not_current": "완료 이력 있음",
        "execution_running": "현재 실행 중",
        "execution_failed": "현재 실행 실패",
        "execution_timeout": "현재 실행 시간초과",
        "draft_created": "실행 초안 생성됨",
        "idle": "실행 대기",
    }
    return labels.get(posture, posture or "실행 대기")


def _contract_rows(contracts: Dict[str, Dict[str, Any]]) -> str:
    rows = []
    for key, info in contracts.items():
        rows.append(
            f"""
            <div class="row">
              <div>
                <strong>{_esc(key)}</strong>
                <div class="mono">{_esc(info.get("path") or "")}</div>
              </div>
              {_chip("exists" if info.get("exists") else "missing", tone="" if info.get("exists") else "warn")}
            </div>
            """
        )
    return "".join(rows)


def _loop_rows(stages: list[Dict[str, Any]]) -> str:
    rows = []
    for index, stage in enumerate(stages, start=1):
        rows.append(
            f"""
            <section class="loop-row">
              <div class="loop-index">{index:02d}</div>
              <div class="loop-main">
                <div class="row-head">
                  <h3>{_esc(stage.get("label") or stage.get("stage_id"))}</h3>
                  {_chip(stage.get("status") or "unknown")}
                </div>
                <div class="muted">owner: {_esc(stage.get("owner") or "unknown")}</div>
                <div class="body">{_esc(stage.get("current_signal") or "")}</div>
                <div class="mono">return -> {_esc(stage.get("return_target") or "")}</div>
              </div>
            </section>
            """
        )
    return "".join(rows)


def _cell_cards(cells: list[Dict[str, Any]]) -> str:
    cards = []
    for cell in cells:
        contract_tone = "" if cell.get("contract_exists") else "warn"
        cards.append(
            f"""
            <article class="cell-card">
              <div class="row-head">
                <div>
                  <div class="kicker">{_esc(cell.get("cell_id") or "")}</div>
                  <h3>{_esc(cell.get("label") or "")}</h3>
                </div>
                {_chip(cell.get("managing_cli") or "unknown")}
              </div>
              <p>{_esc(cell.get("purpose") or "")}</p>
              <div class="mini-label">lens</div>
              <div class="chip-row">{_chips(cell.get("lens") or [])}</div>
              <div class="mini-label">outputs</div>
              <div class="chip-row">{_chips(cell.get("outputs") or [])}</div>
              <div class="row shallow">
                <span class="mono">{_esc(cell.get("md_contract") or "")}</span>
                {_chip("contract ok" if cell.get("contract_exists") else "contract pending", tone=contract_tone)}
              </div>
              <div class="mono">return -> {_esc(cell.get("return_slot") or "")}</div>
            </article>
            """
        )
    return "".join(cards)


def _team_cards(teams: list[Dict[str, Any]]) -> str:
    cards = []
    for team in teams:
        visual = team.get("visual") or {}
        cards.append(
            f"""
            <article class="team-card team-tone-{_esc(visual.get("tone") or "zinc")}">
              <div class="row-head">
                <div class="team-title">
                  <span class="team-mark">{_esc(visual.get("short") or "TM")}</span>
                  <div>
                    <div class="kicker">{_esc(team.get("team_id") or "")}</div>
                    <h3>{_esc(team.get("label") or "")}</h3>
                  </div>
                </div>
                {_chip(team.get("primary_cell") or "unknown")}
              </div>
              <div class="mini-label">{_esc(visual.get("rank") or "team")}</div>
              <p>{_esc(team.get("purpose") or "")}</p>
              <div class="mini-label">members</div>
              <div class="chip-row">{_chips(team.get("members") or [])}</div>
              <div class="mini-label">report slot</div>
              <div class="mono">{_esc(team.get("report_slot") or "")}</div>
            </article>
            """
        )
    return "".join(cards)


def _line_seed_cards(line_seeds: list[Dict[str, Any]]) -> str:
    if not line_seeds:
        return '<div class="muted">no line seeds yet</div>'
    cards = []
    for seed in line_seeds:
        cards.append(
            f"""
            <article class="cell-card">
              <div class="kicker">{_esc(seed.get("line_name") or "line_seed")}</div>
              <h3>{_esc(seed.get("core_claim") or "")}</h3>
              <div class="mini-label">evidence</div>
              <div class="chip-row">{_chips(seed.get("repeated_evidence") or [])}</div>
              <div class="mini-label">resists</div>
              <div class="muted">{_esc(seed.get("what_it_resists") or "")}</div>
              <div class="mini-label">enables</div>
              <div class="muted">{_esc(seed.get("what_it_enables") or "")}</div>
            </article>
            """
        )
    return "".join(cards)


def _line_surface_records(
    *,
    latest_internal_read_report: Dict[str, Any],
    latest_synthesis_report: Dict[str, Any],
    latest_work_packet: Dict[str, Any],
    latest_operating_dialogue: Dict[str, Any],
) -> list[Dict[str, Any]]:
    """Build a line-first surface without promoting engine manifests to the hero layer."""
    records: list[Dict[str, Any]] = []
    for index, seed in enumerate(latest_internal_read_report.get("line_seeds") or [], start=1):
        records.append(
            {
                "line_id": f"internal_seed_{index}",
                "name": seed.get("line_name") or seed.get("name") or f"internal line {index}",
                "purpose": seed.get("why_it_matters") or seed.get("summary") or seed.get("core_claim") or "내부 탐색에서 드러난 라인 후보",
                "health": "growing",
                "anchors": seed.get("evidence") or seed.get("repeated_evidence") or [],
                "relations": seed.get("relations") or seed.get("connected_to") or [],
                "weak_points": seed.get("unclear") or seed.get("weak_points") or [],
                "genealogy": ["operating dialogue", "internal read", "line seed"],
                "export": [seed.get("next_use") or "다음 supervisor 판단 재료"],
                "reflux": ["사용자 재지시", "구현/검증 결과 환류"],
                "note": seed.get("note") or "내부 읽기 결과에서 생성된 라인",
            }
        )
    for index, line in enumerate(latest_synthesis_report.get("confirmed_lines") or [], start=1):
        records.append(
            {
                "line_id": f"synthesis_line_{index}",
                "name": line.get("line_name") or f"confirmed line {index}",
                "purpose": line.get("reason") or line.get("summary") or "종합 보고에서 확인된 라인",
                "health": "strong",
                "anchors": line.get("evidence") or line.get("source_lines") or [],
                "relations": [latest_synthesis_report.get("recommendation") or "supervisor decision"],
                "weak_points": latest_synthesis_report.get("unresolved_tensions") or [],
                "genealogy": ["internal read", "synthesis", "supervisor report"],
                "export": ["감독 판단", "다음 구현 지시 후보"],
                "reflux": ["검증 결과", "사용자 hold/continue 판단"],
                "note": line.get("note") or "종합 보고에서 강해진 라인",
            }
        )
    if records:
        return records
    return [
        {
            "line_id": "current_operating_purpose_line",
            "name": "현재 운용 목적 라인",
            "purpose": latest_operating_dialogue.get("purpose")
            or latest_work_packet.get("directive")
            or "사용자 입력이 아직 라인 자산으로 충분히 두꺼워지지 않은 상태",
            "health": "thin",
            "anchors": latest_operating_dialogue.get("reference_md_files") or latest_work_packet.get("reference_md_files") or [],
            "relations": [latest_operating_dialogue.get("team_name") or "운용 지시 팀"],
            "weak_points": ["내부 탐색 line_seeds가 아직 없음"],
            "genealogy": ["user directive", "work packet pending", "line extraction pending"],
            "export": ["운영 데스크의 다음 지시"],
            "reflux": ["내부 탐색 보고", "작업자 실행 결과"],
            "note": "fallback line: 엔진 manifest가 아니라 사용자 목적을 표면 라인으로 읽기 위한 임시 표현",
        }
    ]


def _line_health_label(value: Any) -> str:
    return {
        "strong": "강한 라인",
        "growing": "자라는 라인",
        "thin": "얇은 라인",
    }.get(str(value or ""), str(value or "상태 미정"))


def _line_surface_cards(lines: list[Dict[str, Any]], selected_line: Dict[str, Any]) -> str:
    cards = []
    for line in lines:
        tone = "good" if line.get("health") == "strong" else "warn" if line.get("health") == "thin" else ""
        cards.append(
            f"""
            <article class="line-card{' selected' if line.get("line_id") == selected_line.get("line_id") else ''}">
              <div class="row-head">
                <div>
                  <div class="kicker">{_esc(line.get("line_id"))}</div>
                  <h3>{_esc(line.get("name"))}</h3>
                </div>
                {_chip(_line_health_label(line.get("health")), tone=tone)}
              </div>
              <p class="muted">{_esc(line.get("purpose"))}</p>
              <div class="chip-row">{_chips((line.get("anchors") or [])[:4])}</div>
            </article>
            """
        )
    return "".join(cards)


def _relation_rows(lines: list[Dict[str, Any]]) -> str:
    rows = []
    for line in lines:
        relations = line.get("relations") or []
        if not relations:
            rows.append(f'<div class="relation-row"><strong>{_esc(line.get("name"))}</strong><span class="muted">연결 대기</span></div>')
        for relation in relations[:3]:
            rows.append(
                f"""
                <div class="relation-row">
                  <strong>{_esc(line.get("name"))}</strong>
                  <span class="muted">→</span>
                  <span>{_esc(relation)}</span>
                </div>
                """
            )
    return "".join(rows)


def _line_event_rows(lines: list[Dict[str, Any]]) -> str:
    rows = []
    for line in lines[:6]:
        rows.append(
            f"""
            <div class="event-row compact">
              <strong>{_esc(_line_health_label(line.get("health")))}</strong>
              <span>{_esc(line.get("name"))}</span>
              <span class="mono">{_esc(line.get("line_id"))}</span>
            </div>
            """
        )
    return "".join(rows)


def _report_state_line(record: Dict[str, Any], *, exit_code: bool = False) -> str:
    if not record:
        return "no report return recorded yet"
    status = record.get("status") or "unknown"
    finished = record.get("finished_at") or record.get("returned_at") or ""
    if exit_code:
        return f"report_return={_esc(status)} / exit={_esc(record.get('exit_code'))} / {_esc(finished)}"
    return f"report_return={_esc(status)} / {_esc(record.get('worker') or 'worker')} / {_esc(finished)}"


OPERATING_GLOSSARY = [
    ("work packet", "작업 지시서", "사용자 입력/메모/지시를 다음 담당자가 읽을 수 있는 단위로 묶은 것"),
    ("assignment", "팀/담당 배치", "어떤 팀과 cell이 읽고 어떤 보고 슬롯으로 돌려줄지 정한 것"),
    ("worker report", "작업자 읽기 보고", "Codex/Gemini/내부 탐색이 돌려준 보고. 제품 완료가 아니라 판단 재료"),
    ("supervisor route", "감독 라우팅", "보고를 보고 다음 팀으로 보낼지 보류할지 정한 연결"),
    ("internal read", "내부 탐색", "외부 검색 전 내부 문서/코드/기록을 먼저 읽는 단계"),
    ("synthesis", "종합 보고", "내부 탐색 결과를 감독자가 판단할 수 있게 압축/번역한 보고"),
    ("supervisor gate", "감독 판단", "continue / hold / reopen / redirect 같은 다음 단계 결정"),
    ("implementation brief", "구현 지시서", "감독자가 승인한 line만 구현팀 입력으로 번역한 문서"),
    ("launch gate", "구현 실행 허가", "구현을 실제로 맡길 수 있는지 기록하는 허가. 실행 자체는 아님"),
]


def _glossary_rows() -> str:
    rows = []
    for internal, human, meaning in OPERATING_GLOSSARY:
        rows.append(
            f"""
            <div class="translation-row">
              <span class="mono">{_esc(internal)}</span>
              <strong>{_esc(human)}</strong>
              <span class="muted">{_esc(meaning)}</span>
            </div>
            """
        )
    return "".join(rows)


def _operator_flow_cards() -> str:
    steps = [
        ("01", "지시 작성", "상단 운용 도크에서 이번 작업의 지시/메모/참조 md/금지 범위를 적는다."),
        ("02", "팀/담당 배치", "작업을 어떤 팀과 cell이 읽을지 정하고 latest assignment로 남긴다."),
        ("03", "읽기 보고 받기", "Codex 또는 내부 탐색을 실행해 구현 전 판단 재료를 받는다."),
        ("04", "종합 보고", "내부 탐색 결과를 supervisor가 읽을 수 있는 보고로 압축한다."),
        ("05", "감독 판단", "보고를 보고 hold / reopen / implementation brief 승인 중 하나로 결정한다."),
        ("06", "구현 허가", "구현 지시서를 만들고 별도 실행 세션에 넘길 수 있는지 launch gate만 남긴다."),
    ]
    return "".join(
        f"""
        <article class="flow-card">
          <div class="loop-index">{number}</div>
          <div>
            <h3>{_esc(title)}</h3>
            <p class="muted">{_esc(description)}</p>
          </div>
        </article>
        """
        for number, title, description in steps
    )


def render_vectorfl_integrated_engine_shell(state: Dict[str, Any], *, page: str = "overview") -> str:
    payload = json.dumps(state, ensure_ascii=False).replace("<", "\\u003c")
    board = state.get("operating_board") or {}
    bridge = state.get("bridge_substrate") or {}
    guard = state.get("guard") or {}
    next_boundary = state.get("next_implementation_boundary") or {}
    worker_policy = state.get("session_worker_policy") or {}
    cli_host_control = state.get("cli_host_control") or {}
    worker_registry = state.get("worker_registry") or {}
    line_script_registry = state.get("line_script_candidate_registry") or []
    translation_material_baseline = state.get("translation_material_baseline") or []
    cells = state.get("cell_registry") or []
    teams = state.get("team_registry") or []
    stages = state.get("engine_loop") or []
    contracts = state.get("contracts") or {}
    latest_work_packet = state.get("latest_work_packet") or {}
    latest_assignment = state.get("latest_assignment") or {}
    latest_codex_run = state.get("latest_codex_run") or {}
    latest_supervisor_route = state.get("latest_supervisor_route") or {}
    latest_internal_read_report = state.get("latest_internal_read_report") or {}
    latest_internal_read_run = state.get("latest_internal_read_run") or {}
    latest_synthesis_report = state.get("latest_synthesis_report") or {}
    latest_synthesis_run = state.get("latest_synthesis_run") or {}
    latest_supervisor_gate = state.get("latest_supervisor_gate") or {}
    latest_implementation_brief = state.get("latest_implementation_brief") or {}
    latest_implementation_launch_gate = state.get("latest_implementation_launch_gate") or {}
    latest_worker_session = state.get("latest_worker_session") or {}
    latest_operating_dialogue = state.get("latest_operating_dialogue") or {}
    latest_worker_launch_draft = state.get("latest_worker_launch_draft") or {}
    latest_worker_execution = state.get("latest_worker_execution") or {}
    latest_cli_session = cli_host_control.get("latest_session") or {}
    latest_cli_return = cli_host_control.get("latest_structured_return") or {}
    latest_cli_readable = cli_host_control.get("latest_readable_return") or {}
    latest_cli_session_line = (
        f'{_esc(latest_cli_session.get("status"))} / {_esc(latest_cli_session.get("backend_kind"))} / '
        f'{_esc(latest_cli_session.get("task_type"))} / {_esc(latest_cli_session.get("ended_at") or latest_cli_session.get("started_at"))}'
        if latest_cli_session
        else "no CLI on-top session recorded yet"
    )
    latest_cli_result_summary = (
        latest_cli_return.get("result_summary")
        or latest_cli_session.get("result_summary")
        or "아직 VectorFL면에서 실행한 CLI on-top return이 없습니다."
    )
    latest_cli_session_id = str(latest_cli_session.get("session_id") or "")
    latest_cli_marks = ", ".join(latest_cli_readable.get("marks") or latest_cli_session.get("marks") or []) or "none"
    latest_cli_mark_history = " / ".join(
        f"{item.get('mark')}@{item.get('marked_at')}"
        for item in (latest_cli_readable.get("mark_history") or latest_cli_session.get("mark_history") or [])[-4:]
    ) or "none"
    latest_cli_deposit_preview = latest_cli_readable.get("deposit_candidate_preview") or cli_host_control.get("latest_deposit_candidate_preview") or ""
    active_team = next(
        (team for team in teams if team.get("team_id") == (latest_supervisor_route.get("target_team") or latest_assignment.get("team_id"))),
        {},
    )
    active_team_visual = active_team.get("visual") or {}
    codex_return = ((state.get("bridge_substrate") or {}).get("codex_return_status") or "unknown")
    codex_return_summary = bridge.get("codex_return_summary") or latest_codex_run.get("return_summary") or ""
    codex_next_recommendation = bridge.get("codex_next_recommendation") or ""
    page_label = {
        "operate": "사용자면",
        "vectorfl": "벡터플면",
        "engine": "엔진면",
        "team": "팀 관측면",
        "internal": "흐름·분석 관측면",
        "synthesis": "생산물·승인 관측면",
        "overview": "내부 심층 관측면",
    }.get(page, "내부 심층 관측면")
    hero_title = {
        "operate": "무엇을 시키고 누구에게 넘길지 정한다.",
        "vectorfl": "공간 표면에 생긴 라인과 결핍을 읽는다.",
        "engine": "공간 내부 재료 목록과 상태창은 다음 단계에서 별도 정비한다.",
        "team": "팀과 담당의 내부 배치 상태를 깊게 판독한다.",
        "internal": "내부 공간을 먼저 읽고 다음 증거선을 만든다.",
        "synthesis": "내부 읽기를 감독자 판단 재료로 번역한다.",
        "overview": "내부 상태와 흐름과 근거를 깊게 판독한다.",
    }.get(page, "내부 상태와 흐름과 근거를 깊게 판독한다.")
    stage_options = "".join(
        f'<option value="{_esc(stage.get("stage_id") or "")}">{_esc(stage.get("label") or stage.get("stage_id"))}</option>'
        for stage in stages
    )
    cell_options = "".join(
        f'<option value="{_esc(cell.get("cell_id") or "")}">{_esc(cell.get("label") or cell.get("cell_id"))}</option>'
        for cell in cells
    )
    team_options = "".join(
        f'<option value="{_esc(team.get("team_id") or "")}">{_esc(team.get("label") or team.get("team_id"))}</option>'
        for team in teams
    )
    route_team_options = "".join(
        f'<option value="{_esc(team.get("team_id") or "")}">{_esc(team.get("label") or team.get("team_id"))}</option>'
        for team in teams
        if team.get("team_id") not in {"supervisor_team"}
    )
    latest_packet_line = (
        f'{_esc(latest_work_packet.get("status"))} / {_esc(latest_work_packet.get("target_cell"))} / '
        f'{_esc(latest_work_packet.get("created_at"))}'
        if latest_work_packet
        else "no work packet recorded yet"
    )
    latest_assignment_line = (
        f'{_esc(latest_assignment.get("status"))} / {_esc(latest_assignment.get("team_id"))} / '
        f'{_esc(latest_assignment.get("assignee_cell"))} / {_esc(latest_assignment.get("created_at"))}'
        if latest_assignment
        else "no assignment recorded yet"
    )
    latest_codex_run_line = (
        _report_state_line(latest_codex_run, exit_code=True)
        if latest_codex_run
        else "no codex run recorded yet"
    )
    latest_route_line = (
        f'{_esc(latest_supervisor_route.get("decision"))} / {_esc(latest_supervisor_route.get("target_team"))} / '
        f'{_esc(latest_supervisor_route.get("decided_at"))}'
        if latest_supervisor_route
        else "no supervisor route recorded yet"
    )
    latest_internal_read_line = (
        _report_state_line(latest_internal_read_report)
        if latest_internal_read_report
        else "no internal read report recorded yet"
    )
    internal_read_run_line = (
        _report_state_line(latest_internal_read_run, exit_code=True)
        if latest_internal_read_run
        else "no internal read run recorded yet"
    )
    latest_synthesis_line = (
        _report_state_line(latest_synthesis_report)
        if latest_synthesis_report
        else "no synthesis report recorded yet"
    )
    synthesis_run_line = (
        _report_state_line(latest_synthesis_run, exit_code=True)
        if latest_synthesis_run
        else "no synthesis run recorded yet"
    )
    latest_gate_line = (
        f'{_esc(latest_supervisor_gate.get("decision"))} / {_esc(latest_supervisor_gate.get("target_team"))} / '
        f'{_esc(latest_supervisor_gate.get("decided_at"))}'
        if latest_supervisor_gate
        else "no supervisor gate recorded yet"
    )
    latest_implementation_brief_line = (
        f'{_esc(latest_implementation_brief.get("status"))} / {_esc(latest_implementation_brief.get("target_worker"))} / '
        f'{_esc(latest_implementation_brief.get("created_at"))}'
        if latest_implementation_brief
        else "no implementation brief recorded yet"
    )
    latest_implementation_launch_gate_line = (
        f'{_esc(latest_implementation_launch_gate.get("decision"))} / {_esc(latest_implementation_launch_gate.get("target_worker"))} / '
        f'{_esc(latest_implementation_launch_gate.get("decided_at"))}'
        if latest_implementation_launch_gate
        else "no implementation launch gate recorded yet"
    )
    latest_worker_session_line = (
        f'{_esc(latest_worker_session.get("status"))} / {_esc(latest_worker_session.get("secondary_worker"))} / '
        f'{_esc(latest_worker_session.get("secondary_model"))} / {_esc(latest_worker_session.get("updated_at"))}'
        if latest_worker_session
        else "no worker session recorded yet"
    )
    latest_operating_dialogue_line = (
        f'{_esc(latest_operating_dialogue.get("status"))} / {_esc(latest_operating_dialogue.get("selected_worker"))} / '
        f'{_esc(latest_operating_dialogue.get("selected_model"))} / {_esc(latest_operating_dialogue.get("created_at"))}'
        if latest_operating_dialogue
        else "no operating dialogue recorded yet"
    )
    latest_worker_launch_draft_line = (
        f'{_esc(latest_worker_launch_draft.get("status"))} / {_esc(latest_worker_launch_draft.get("selected_worker"))} / '
        f'{_esc(latest_worker_launch_draft.get("command_family"))} / {_esc(latest_worker_launch_draft.get("created_at"))}'
        if latest_worker_launch_draft
        else "no worker launch draft recorded yet"
    )
    latest_worker_execution_summary = (
        str(latest_worker_execution.get("stdout_tail") or latest_worker_execution.get("output_summary") or "")[:2400]
    )
    conversation_worker_reply = latest_worker_execution_summary or str(
        latest_worker_launch_draft.get("command_preview") or "아직 worker 응답이 없습니다. 대화 입력을 저장하고 호출 초안을 실행하면 이곳에 최신 응답이 붙습니다."
    )
    operating_purpose = latest_operating_dialogue.get("purpose") or latest_operating_dialogue.get("operator_message") or ""
    operating_team_name = latest_operating_dialogue.get("team_name") or "운용 지시 팀"
    operating_team_purpose = latest_operating_dialogue.get("team_purpose") or "사용자 기준면에서 작성한 운용 지시를 수행 가능한 작업자 입력으로 정리한다."
    operating_assignee_role = latest_operating_dialogue.get("assignee_role") or "지시 정리 담당"
    freshness = _current_run_freshness(
        operating_dialogue=latest_operating_dialogue,
        launch_draft=latest_worker_launch_draft,
        worker_execution=latest_worker_execution,
    )
    execution_posture = freshness["posture"]
    execution_posture_label = _execution_posture_label(execution_posture)
    freshness_caveat = (
        ""
        if freshness["is_current_execution"] or not latest_worker_execution
        else "latest execution is not proof of the current draft"
    )
    result_link_label = "현재 결과 보기" if freshness["is_current_execution"] else "결과 이력 보기"
    execution_event_worker_label = (
        latest_worker_launch_draft.get("selected_worker_label")
        or latest_operating_dialogue.get("selected_worker_label")
        or latest_worker_execution.get("worker_label")
        or "worker"
    )
    latest_worker_execution_line = (
        f'{execution_posture_label} / {_esc(latest_worker_execution.get("worker"))} / '
        f'exit={_esc(latest_worker_execution.get("exit_code"))} / {_esc(latest_worker_execution.get("finished_at"))}'
        if latest_worker_execution
        else "no worker execution recorded yet"
    )
    event_feed = [
        ("지시", "운용 지시문 기록됨" if latest_operating_dialogue else "운용 지시 대기", latest_operating_dialogue.get("created_at") or "", "/vectorfl-engine/team#work-packet"),
        ("팀", f"{operating_team_name} / {operating_assignee_role}", latest_worker_session.get("updated_at") or "", "/vectorfl-engine/team#team-board"),
        ("초안", "작업자 호출 초안 생성됨" if latest_worker_launch_draft else "호출 초안 대기", latest_worker_launch_draft.get("created_at") or "", "/vectorfl-engine/internal"),
        ("실행", f"{execution_event_worker_label} · {execution_posture_label}", latest_worker_execution.get("finished_at") or "", "/vectorfl-engine/synthesis"),
    ]
    event_feed_rows = "".join(
        f"""
        <a class="event-row" href="{_esc(href)}">
          <strong>{_esc(label)}</strong>
          <span>{_esc(text)}</span>
          <span class="mono">{_esc(time)}</span>
        </a>
        """
        for label, text, time, href in event_feed
    )
    latest_line_script_candidates = "\n".join(
        latest_worker_session.get("line_script_candidates")
        or [candidate.get("path") for candidate in line_script_registry if candidate.get("path")]
    )
    latest_translation_targets = "\n".join(
        latest_worker_session.get("translation_material_targets")
        or [item.get("path") for item in translation_material_baseline if item.get("path")]
    )
    operating_reference_md_files = "\n".join(
        latest_operating_dialogue.get("reference_md_files")
        or latest_worker_session.get("translation_material_targets")
        or []
    )
    operating_line_script_candidates = "\n".join(
        latest_operating_dialogue.get("line_script_candidates")
        or latest_worker_session.get("line_script_candidates")
        or [candidate.get("path") for candidate in line_script_registry if candidate.get("path")]
    )
    operating_forbidden_scope = "\n".join(
        latest_operating_dialogue.get("forbidden_scope")
        or latest_worker_session.get("forbidden_scope")
        or [
            "do not run CLI from this dialogue action",
            "do not replace current slot",
            "do not declare gate close",
        ]
    )
    active_team_label = (
        latest_assignment.get("operating_team_name")
        or latest_work_packet.get("operating_team_name")
        or operating_team_name
        or active_team.get("label")
        or latest_assignment.get("team_id")
        or "운용 지시 팀"
    )
    active_team_purpose = (
        latest_assignment.get("operating_team_purpose")
        or latest_work_packet.get("operating_team_purpose")
        or operating_team_purpose
        or active_team.get("purpose")
    )
    active_worker_label = (
        latest_worker_launch_draft.get("selected_worker_label")
        or latest_operating_dialogue.get("selected_worker_label")
        or latest_worker_execution.get("worker_label")
        or "worker 대기"
    )
    assignee_summary = (
        latest_assignment.get("assignee_text")
        or latest_work_packet.get("assignee_text")
        or operating_assignee_role
        or latest_assignment.get("assignee_cell")
        or "담당 대기"
    )
    footer_event_rows = "".join(
        f"""
        <a class="footer-event" href="{_esc(href)}">
          <strong>{_esc(label)}</strong>
          <span>{_esc(text)}</span>
        </a>
        """
        for label, text, _time, href in event_feed[-2:]
    )
    rear_summary_cards = f"""
        <div class="rear-summary-card">
          <div class="mini-label">팀</div>
          <h3>{_esc(active_team_label)}</h3>
          <p class="muted">{_esc(active_team_purpose)}</p>
        </div>
        <div class="rear-summary-card">
          <div class="mini-label">담당 / 세션</div>
          <h3>{_esc(assignee_summary)}</h3>
          <p class="muted">{_esc(active_worker_label)} · {_esc(execution_posture_label)}</p>
        </div>
        <div class="rear-summary-card">
          <div class="mini-label">흐름</div>
          <h3>{_esc(latest_supervisor_route.get("decision") or execution_posture)}</h3>
          <p class="muted">{_esc(freshness_caveat or latest_supervisor_route.get("next_instruction") or latest_worker_execution.get("output_summary") or "다음 내부 관측 대기")[:220]}</p>
        </div>
        <div class="rear-summary-card">
          <div class="mini-label">결과물</div>
          <h3>{_esc(latest_synthesis_report.get("status") or execution_posture_label)}</h3>
          <p class="muted">{_esc(latest_synthesis_report.get("current_status") or latest_worker_execution.get("result_return_slot") or "latest artifact 없음")[:220]}</p>
        </div>
    """
    primary_worker_options = _select_options(
        worker_registry,
        str(latest_worker_session.get("primary_worker") or "codex"),
    )
    secondary_worker_options = _select_options(
        worker_registry,
        str(latest_worker_session.get("secondary_worker") or "gemini"),
    )
    operating_worker_options = _select_options(
        worker_registry,
        str(latest_operating_dialogue.get("selected_worker") or latest_worker_session.get("primary_worker") or "codex"),
    )
    operating_assistant_options = _select_options(
        worker_registry,
        str(latest_operating_dialogue.get("assistant_worker") or latest_worker_session.get("secondary_worker") or "gemini"),
    )
    latest_reference_md_files = "\n".join(
        latest_assignment.get("reference_md_files") or latest_work_packet.get("reference_md_files") or []
    )
    synthesis_line_names = "\n".join(
        str(line.get("line_name") or "")
        for line in latest_synthesis_report.get("confirmed_lines") or []
        if str(line.get("line_name") or "")
    )
    vector_lines = _line_surface_records(
        latest_internal_read_report=latest_internal_read_report,
        latest_synthesis_report=latest_synthesis_report,
        latest_work_packet=latest_work_packet,
        latest_operating_dialogue=latest_operating_dialogue,
    )
    selected_vector_line = vector_lines[0] if vector_lines else {}
    strong_lines = [line for line in vector_lines if line.get("health") == "strong"]
    thin_lines = [line for line in vector_lines if line.get("health") == "thin"]
    growing_lines = [line for line in vector_lines if line.get("health") == "growing"]
    strongest_line = (strong_lines or growing_lines or vector_lines)[0] if vector_lines else {}
    weakest_line = (thin_lines or list(reversed(vector_lines)))[0] if vector_lines else {}

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>VectorFL {page_label}</title>
  <style>
    :root {{
      --bg: #09090b;
      --ink: #f4f4f5;
      --muted: #a1a1aa;
      --panel: #18181b;
      --panel-strong: #202024;
      --line: #27272a;
      --line-soft: #27272a;
      --accent: #3b82f6;
      --green: #10b981;
      --warn: #ef4444;
      --mono: #d4d4d8;
      --field: #0f0f12;
      --glow-blue: rgba(59, 130, 246, .34);
      --glow-green: rgba(16, 185, 129, .22);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at 78% 10%, rgba(59,130,246,.16), transparent 28%),
        radial-gradient(circle at 12% 18%, rgba(16,185,129,.08), transparent 30%),
        var(--bg);
      font-family: "Inter", "Geist", "Aptos", "IBM Plex Sans KR", "Noto Sans KR", ui-sans-serif, system-ui, sans-serif;
      padding-bottom: 118px;
    }}
    .shell {{ min-height: 100vh; display: grid; grid-template-columns: 250px minmax(0, 1fr) 340px; }}
    .rail, .inspector {{
      border-color: var(--line);
      background: rgba(9,9,11,.82);
      backdrop-filter: blur(12px);
    }}
    .rail {{ border-right: 1px solid var(--line); padding: 16px 12px; display: grid; align-content: start; gap: 12px; }}
    .inspector {{ border-left: 1px solid var(--line); padding: 16px 12px; display: grid; align-content: start; gap: 12px; }}
    .main {{ padding: 16px; display: grid; gap: 12px; max-width: 1180px; width: 100%; }}
    .panel {{
      border: 1px solid var(--line);
      border-radius: 12px;
      background: rgba(24,24,27,.92);
      box-shadow: none;
      padding: 16px;
      display: grid;
      gap: 12px;
    }}
    .panel.soft {{ border-color: var(--line-soft); background: rgba(24,24,27,.68); box-shadow: none; }}
    .kicker, .mini-label {{ font-size: 10px; font-weight: 900; letter-spacing: .12em; text-transform: uppercase; color: var(--accent); }}
    .mini-label {{ color: var(--muted); margin-top: 4px; }}
    h1, h2, h3, p {{ margin: 0; }}
    h1 {{ font-size: clamp(32px, 5vw, 72px); letter-spacing: -.06em; line-height: .9; max-width: 980px; }}
    h2 {{ font-size: 19px; letter-spacing: -.03em; }}
    h3 {{ font-size: 15px; letter-spacing: -.02em; }}
    p, .body {{ font-size: 13px; line-height: 1.62; }}
    .muted {{ color: var(--muted); font-size: 12px; line-height: 1.55; }}
    .mono {{ color: var(--mono); font: 11px/1.5 "JetBrains Mono", "Geist Mono", "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: -.02em; word-break: break-all; }}
    .chip-row {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .chip {{ display: inline-flex; align-items: center; border: 1px solid var(--line); background: #0f0f12; color: var(--ink); padding: 3px 8px; border-radius: 999px; font-size: 10px; font-weight: 800; }}
    .chip.warn {{ border-color: rgba(239,68,68,.6); color: #fecaca; background: rgba(239,68,68,.12); }}
    .row, .row-head {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; }}
    .row {{ border-top: 1px solid var(--line-soft); padding-top: 9px; }}
    .row.shallow {{ border-top: 0; padding-top: 0; align-items: start; }}
    .hero {{ min-height: 420px; align-content: end; background:
      linear-gradient(135deg, rgba(59,130,246,.12), transparent 44%),
      radial-gradient(circle at 78% 18%, rgba(16,185,129,.14), transparent 28%),
      rgba(24,24,27,.94);
    }}
    .hero .sub {{ max-width: 840px; font-size: 15px; line-height: 1.65; color: var(--muted); }}
    .board-grid {{ display: grid; grid-template-columns: 1.2fr .8fr; gap: 12px; }}
    .loop-list {{ display: grid; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: var(--panel); }}
    .loop-row {{ display: grid; grid-template-columns: 54px minmax(0, 1fr); border-bottom: 1px solid var(--line); }}
    .loop-row:last-child {{ border-bottom: 0; }}
    .loop-index {{ display: grid; place-items: center; border-right: 1px solid var(--line); font: 900 13px "JetBrains Mono", "Geist Mono", ui-monospace, monospace; color: var(--accent); background: var(--panel-strong); }}
    .loop-main {{ padding: 12px; display: grid; gap: 6px; }}
    .operator-flow {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }}
    .flow-card {{ border: 1px solid var(--line); border-radius: 10px; background: #111114; display: grid; grid-template-columns: 46px minmax(0, 1fr); overflow: hidden; min-height: 92px; }}
    .flow-card > div:last-child {{ padding: 12px; display: grid; align-content: center; gap: 6px; }}
    .translation-row {{ border-top: 1px solid var(--line); padding-top: 9px; display: grid; gap: 4px; }}
    .translation-row:first-child {{ border-top: 0; padding-top: 0; }}
    .cell-grid, .team-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .cell-card, .team-card {{ border: 1px solid var(--line); border-radius: 10px; background: #111114; padding: 12px; display: grid; gap: 8px; }}
    .team-title {{ display: inline-flex; align-items: center; gap: 10px; }}
    .team-mark {{
      width: 34px;
      height: 34px;
      border: 1px solid var(--line);
      border-radius: 10px;
      display: inline-grid;
      place-items: center;
      font: 900 11px/1 "JetBrains Mono", "Geist Mono", ui-monospace, monospace;
      background: #0f0f12;
      color: var(--ink);
    }}
    .team-tone-emerald .team-mark {{ border-color: rgba(16,185,129,.72); color: #a7f3d0; box-shadow: inset 0 0 18px rgba(16,185,129,.08); }}
    .team-tone-blue .team-mark {{ border-color: rgba(59,130,246,.72); color: #bfdbfe; box-shadow: inset 0 0 18px rgba(59,130,246,.08); }}
    .team-tone-amber .team-mark {{ border-color: rgba(245,158,11,.72); color: #fde68a; box-shadow: inset 0 0 18px rgba(245,158,11,.08); }}
    .team-tone-rose .team-mark {{ border-color: rgba(239,68,68,.72); color: #fecaca; box-shadow: inset 0 0 18px rgba(239,68,68,.08); }}
    .team-tone-cyan .team-mark {{ border-color: rgba(34,211,238,.72); color: #a5f3fc; box-shadow: inset 0 0 18px rgba(34,211,238,.08); }}
    .team-tone-violet .team-mark {{ border-color: rgba(139,92,246,.72); color: #ddd6fe; box-shadow: inset 0 0 18px rgba(139,92,246,.08); }}
    .nav-link {{ border: 1px solid var(--line); border-radius: 10px; padding: 10px; display: grid; gap: 4px; background: #111114; text-decoration: none; color: inherit; }}
    .nav-link:hover, .cell-card:hover, .team-card:hover {{ border-color: rgba(59,130,246,.7); }}
    body.page-overview .page-team-only,
    body.page-overview .page-internal-only,
    body.page-overview .page-synthesis-only,
    body.page-overview .page-operate-only,
    body.page-overview .page-vectorfl-only,
    body.page-overview .page-engine-only,
    body.page-team .page-overview-only,
    body.page-team .page-internal-only,
    body.page-team .page-synthesis-only,
    body.page-team .page-operate-only,
    body.page-team .page-vectorfl-only,
    body.page-team .page-engine-only,
    body.page-internal .page-overview-only,
    body.page-internal .page-team-only,
    body.page-internal .page-synthesis-only,
    body.page-internal .page-operate-only,
    body.page-internal .page-vectorfl-only,
    body.page-internal .page-engine-only,
    body.page-synthesis .page-overview-only,
    body.page-synthesis .page-team-only,
    body.page-synthesis .page-internal-only,
    body.page-synthesis .page-operate-only,
    body.page-synthesis .page-vectorfl-only,
    body.page-synthesis .page-engine-only,
    body.page-operate .page-overview-only,
    body.page-operate .page-team-only,
    body.page-operate .page-internal-only,
    body.page-operate .page-synthesis-only,
    body.page-operate .page-vectorfl-only,
    body.page-operate .page-engine-only,
    body.page-vectorfl .page-overview-only,
    body.page-vectorfl .page-team-only,
    body.page-vectorfl .page-internal-only,
    body.page-vectorfl .page-synthesis-only,
    body.page-vectorfl .page-operate-only,
    body.page-vectorfl .page-engine-only,
    body.page-engine .page-overview-only,
    body.page-engine .page-team-only,
    body.page-engine .page-internal-only,
    body.page-engine .page-synthesis-only,
    body.page-engine .page-operate-only,
    body.page-engine .page-vectorfl-only {{ display: none; }}
    body.page-operate .page-rear-only {{ display: none; }}
    body.page-operate .shell {{ grid-template-columns: 250px minmax(0, 1fr); }}
    body.page-operate .inspector {{ display: none; }}
    body.page-operate .main {{ max-width: 980px; }}
    body.page-vectorfl .page-rear-only,
    body.page-engine .page-rear-only {{ display: none; }}
    body.page-vectorfl .shell,
    body.page-engine .shell {{ grid-template-columns: 250px minmax(0, 1fr); }}
    body.page-vectorfl .inspector,
    body.page-engine .inspector {{ display: none; }}
    body.page-vectorfl .main,
    body.page-engine .main {{ max-width: 1180px; }}
    .surface-bridge {{ border-color: rgba(16,185,129,.44); background: linear-gradient(135deg, rgba(16,185,129,.08), transparent 45%), #111114; }}
    .rear-summary-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; }}
    .rear-summary-card {{ border: 1px solid var(--line); border-radius: 10px; background: #111114; padding: 12px; display: grid; gap: 6px; min-height: 118px; }}
    .command-slot {{ border: 1px dashed rgba(59,130,246,.55); border-radius: 10px; background: rgba(59,130,246,.06); padding: 10px; display: grid; gap: 6px; }}
    .operator-dock {{
      border-color: rgba(59,130,246,.7);
      background:
        linear-gradient(135deg, rgba(59,130,246,.12), transparent 38%),
        rgba(24,24,27,.96);
      box-shadow: 0 0 32px rgba(59,130,246,.08);
    }}
    .operator-dock textarea {{ min-height: 72px; }}
    .work-form {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .work-form label {{ display: grid; gap: 6px; font-size: 11px; font-weight: 900; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }}
    .work-form input, .work-form textarea, .work-form select {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: var(--field);
      color: var(--ink);
      padding: 9px;
      font: 13px/1.5 "Inter", "Geist", "IBM Plex Sans KR", "Noto Sans KR", ui-sans-serif, system-ui, sans-serif;
    }}
    .work-form input:focus, .work-form textarea:focus, .work-form select:focus {{ outline: 1px solid var(--accent); border-color: var(--accent); box-shadow: 0 0 0 3px rgba(59,130,246,.14); }}
    .work-form textarea {{ min-height: 96px; resize: vertical; }}
    .conversation-shell {{ display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 12px; align-items: start; }}
    .conversation-main {{ min-height: 540px; align-content: stretch; }}
    .message-stack {{ display: grid; gap: 10px; align-content: start; }}
    .message-bubble {{ border: 1px solid var(--line); border-radius: 12px; padding: 12px; display: grid; gap: 8px; background: #111114; }}
    .message-bubble.user {{ border-color: rgba(16,185,129,.55); background: linear-gradient(135deg, rgba(16,185,129,.10), transparent 48%), #111114; }}
    .message-bubble.worker {{ border-color: rgba(59,130,246,.55); background: linear-gradient(135deg, rgba(59,130,246,.12), transparent 48%), #111114; }}
    .message-bubble.system {{ border-style: dashed; }}
    .message-bubble .body {{ white-space: pre-wrap; }}
    .chat-composer {{ border: 1px solid rgba(59,130,246,.55); border-radius: 14px; background: #0f0f12; padding: 12px; display: grid; gap: 10px; }}
    .chat-composer textarea {{ min-height: 150px; border-radius: 12px; }}
    .config-drawer {{ display: grid; gap: 10px; }}
    .config-drawer .panel {{ padding: 12px; }}
    .drawer-fields {{ display: grid; gap: 8px; }}
    .drawer-fields textarea {{ min-height: 84px; }}
    .step-actions {{ display: grid; gap: 8px; }}
    .status-card {{ max-height: 260px; overflow: auto; }}
    .session-strip {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; }}
    .session-tab {{ border: 1px solid var(--line); border-radius: 10px; background: #111114; padding: 10px; color: inherit; text-decoration: none; display: grid; gap: 4px; min-height: 76px; }}
    .session-tab strong {{ font-size: 12px; }}
    .session-tab.active {{ border-color: rgba(16,185,129,.65); box-shadow: inset 0 0 18px rgba(16,185,129,.06); }}
    .chat-only-shell {{ display: grid; gap: 12px; }}
    .chat-only-shell .conversation-main {{ min-height: 620px; }}
    details.config-fold {{ border: 1px solid var(--line); border-radius: 12px; background: #111114; padding: 10px; }}
    details.config-fold summary {{ cursor: pointer; color: var(--muted); font-size: 12px; font-weight: 900; }}
    .directive-card {{ display: grid; gap: 12px; }}
    .directive-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .event-feed {{ display: grid; gap: 8px; }}
    .event-row {{ display: grid; grid-template-columns: 72px minmax(0, 1fr) 140px; gap: 8px; align-items: center; border-top: 1px solid var(--line); padding-top: 8px; font-size: 12px; color: inherit; text-decoration: none; }}
    .event-row:hover {{ color: var(--ink); }}
    .event-row:first-child {{ border-top: 0; padding-top: 0; }}
    .surface-switch {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; }}
    .surface-switch .nav-link {{ min-height: 76px; }}
    .surface-switch .active {{ border-color: rgba(16,185,129,.72); box-shadow: inset 0 0 18px rgba(16,185,129,.08); }}
    .line-dashboard {{ display: grid; grid-template-columns: 1.05fr .95fr; gap: 12px; align-items: start; }}
    .line-atlas {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .line-card {{ border: 1px solid var(--line); border-radius: 12px; background: #111114; padding: 12px; display: grid; gap: 8px; }}
    .line-card.selected {{ border-color: rgba(16,185,129,.72); box-shadow: inset 0 0 24px rgba(16,185,129,.07); }}
    .line-inspector {{ background: linear-gradient(135deg, rgba(59,130,246,.12), transparent 44%), #111114; }}
    .relation-row {{ border: 1px solid var(--line); border-radius: 10px; background: #111114; padding: 10px; display: grid; grid-template-columns: minmax(0, 1fr) 24px minmax(0, 1fr); gap: 8px; align-items: center; }}
    .event-row.compact {{ grid-template-columns: 130px minmax(0, 1fr) 160px; }}
    .engine-placeholder-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; }}
    .engine-footer {{
      position: fixed;
      left: 0;
      right: 0;
      bottom: 0;
      z-index: 20;
      border-top: 1px solid var(--line);
      background: rgba(9,9,11,.92);
      backdrop-filter: blur(12px);
      display: grid;
      grid-template-columns: 260px minmax(0, 1fr) 240px;
      gap: 10px;
      padding: 10px 14px;
    }}
    .footer-status, .footer-events, .footer-return {{ border: 1px solid var(--line); border-radius: 10px; background: rgba(24,24,27,.74); padding: 9px; display: grid; gap: 4px; min-height: 74px; }}
    .footer-events {{ grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; }}
    .footer-event {{ border: 1px solid var(--line); border-radius: 8px; padding: 7px; display: grid; gap: 3px; color: inherit; text-decoration: none; background: #111114; }}
    .footer-event span {{ color: var(--muted); font-size: 11px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .footer-return .mono {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .wide {{ grid-column: 1 / -1; }}
    .primary-button {{ border: 1px solid rgba(59,130,246,.7); border-radius: 10px; background: #2563eb; color: #f4f4f5; padding: 11px 14px; font-weight: 900; cursor: pointer; }}
    .primary-button:hover {{ background: #3b82f6; box-shadow: 0 0 24px var(--glow-blue); }}
    .primary-button:disabled {{ opacity: .5; cursor: wait; }}
    .status-line {{ color: var(--green); font: 12px/1.5 "JetBrains Mono", "Geist Mono", ui-monospace, monospace; }}
    .thinking {{
      border-color: rgba(59,130,246,.72);
      box-shadow: 0 0 0 1px rgba(59,130,246,.12), 0 0 28px var(--glow-blue);
      animation: borderPulse 1.8s ease-in-out infinite;
    }}
    @keyframes borderPulse {{
      0%, 100% {{ box-shadow: 0 0 0 1px rgba(59,130,246,.08), 0 0 18px rgba(59,130,246,.14); }}
      50% {{ box-shadow: 0 0 0 1px rgba(59,130,246,.28), 0 0 34px rgba(16,185,129,.16); }}
    }}
    @media (max-width: 1180px) {{
      .shell {{ grid-template-columns: 1fr; }}
      .rail, .inspector {{ border: 0; border-bottom: 2px solid var(--line); }}
      .board-grid, .cell-grid, .team-grid, .work-form, .operator-flow, .conversation-shell, .session-strip, .directive-grid, .event-row, .rear-summary-grid, .engine-footer, .footer-events, .surface-switch, .line-dashboard, .line-atlas, .relation-row, .engine-placeholder-grid {{ grid-template-columns: 1fr; }}
      body {{ padding-bottom: 260px; }}
      h1 {{ font-size: 42px; line-height: .92; }}
    }}
  </style>
</head>
<body class="page-{_esc(page)}">
  <script id="vectorfl-integrated-engine-state" type="application/json">{payload}</script>
  <div class="shell">
    <aside class="rail">
      <div>
        <div class="kicker">VectorFL</div>
        <h2>{page_label}</h2>
      </div>
      <a class="nav-link" href="/vectorfl-engine"><strong>운용 개요</strong><span class="muted">engine loop / posture</span></a>
      <a class="nav-link" href="/vectorfl-engine/operate"><strong>엔진면</strong><span class="muted">inventory / status / maintenance</span></a>
      <a class="nav-link" href="http://127.0.0.1:5174/"><strong>사용자면 / 벡터플면</strong><span class="muted">React surface app / runtime/views/vectorfl_dual_surface.tsx</span></a>
      <a class="nav-link" href="/vectorfl-engine/team"><strong>팀</strong><span class="muted">who owns the work</span></a>
      <a class="nav-link" href="/vectorfl-engine/internal"><strong>흐름·분석</strong><span class="muted">what changed / why</span></a>
      <a class="nav-link" href="/vectorfl-engine/synthesis"><strong>결과물·승인</strong><span class="muted">outputs / gate</span></a>
      <a class="nav-link page-team-only" href="#work-packet"><strong>작업 지시서</strong><span class="muted">input / select / route</span></a>
      <a class="nav-link page-team-only" href="#team-board"><strong>팀 배치</strong><span class="muted">place work into a team</span></a>
      <a class="nav-link page-overview-only" href="#substrate"><strong>기존 브릿지 재료</strong><span class="muted">Codex / Gemini / validation state</span></a>
      <div class="panel soft">
        <div class="kicker">Guard</div>
        <div class="chip-row">
          {_chip("no gate close", tone="warn" if guard.get("no_gate_close") else "")}
          {_chip("no slot replacement", tone="warn" if guard.get("no_slot_replacement") else "")}
          {_chip("no fake controls", tone="warn" if guard.get("no_fake_execution_controls") else "")}
        </div>
      </div>
    </aside>

    <main class="main">
      <section class="panel hero">
        <div class="kicker">Engine-Level Operating Surface</div>
        <h1>{hero_title}</h1>
        <p class="sub">{_esc(state.get("core_sentence") or "")}</p>
        <div class="chip-row">
          {_chip("posture=" + str(state.get("current_posture") or "unknown"))}
          {_chip("route=/vectorfl-engine/internal" if page == "internal" else ("route=/vectorfl-engine/synthesis" if page == "synthesis" else ("route=/vectorfl-engine/operate" if page == "operate" else ("route=/vectorfl-engine/vectorfl" if page == "vectorfl" else ("route=/vectorfl-engine/engine" if page == "engine" else ("route=/vectorfl-engine/team" if page == "team" else "route=/vectorfl-engine"))))))}
          {_chip("active_team=" + str(active_team.get("team_id") or "pending"))}
          {_chip("substrate=/vectorfl-paper")}
        </div>
      </section>

      <section id="surface-switch" class="surface-switch page-engine-only">
        <a class="nav-link" href="http://127.0.0.1:5174/">
          <strong>사용자면</strong>
          <span class="muted">React surface app에서 관리</span>
        </a>
        <a class="nav-link" href="http://127.0.0.1:5174/">
          <strong>벡터플면</strong>
          <span class="muted">React surface app에서 관리</span>
        </a>
        <a class="nav-link active" href="/vectorfl-engine/operate">
          <strong>엔진면</strong>
          <span class="muted">재료 목록 / 상태창 / script·md·json / 정비</span>
        </a>
      </section>

      <section id="operator-guide" class="panel page-overview-only">
        <div class="row-head">
          <div>
            <div class="kicker">사용 순서</div>
            <h2>이 페이지는 상태표가 아니라 지시를 배치하고 보고를 받아 다음 게이트를 정하는 운용면</h2>
          </div>
          {_chip("human-facing guide")}
        </div>
        <div class="operator-flow">{_operator_flow_cards()}</div>
        <p class="muted">아직 구현 실행기는 아닙니다. 현재 기준은 작업 지시서와 팀 배치를 만들고, 읽기/종합 보고를 받은 뒤, 구현 지시서와 구현 실행 허가를 기록하는 데 있습니다.</p>
      </section>

      <section id="deep-observation-role-lock" class="panel surface-bridge page-rear-only">
        <div class="row-head">
          <div>
            <div class="kicker">내부 심층 관측면 / Deep Observation Surface</div>
            <h2>이 면은 사용자 기준면의 복잡한 원본이 아니라 내부 상태와 근거를 깊게 판독하는 표면</h2>
          </div>
          {_chip("not a simplified/original pair")}
        </div>
        <p class="muted">사용자 기준면은 직접 지시하고 실행을 시작하는 전면이고, 이 내부면은 팀/담당/세션/라우팅/흐름/분석/생산물/감독 판단을 깊게 읽는 후면입니다. 사용자 친화성 때문에 근거 구조를 지우지 않고, 필요할 때만 다시 운영 데스크로 돌아가 다음 지시를 만듭니다.</p>
        <div class="chip-row">
          <a class="nav-link" href="/vectorfl-engine/operate"><strong>운영 데스크로 돌아가기</strong><span class="muted">new directive from current reading</span></a>
          {_chip("raw pointers preserved")}
          {_chip("deep evidence stays here")}
        </div>
      </section>

      <section id="rear-summary" class="panel page-rear-only">
        <div class="row-head">
          <div>
            <div class="kicker">후면 관측 요약</div>
            <h2>팀 / 흐름 / 분석 / 결과물을 먼저 한눈에 보고, 필요할 때 아래 상세로 내려간다</h2>
          </div>
          {_chip("compact rear board")}
        </div>
        <div class="rear-summary-grid">{rear_summary_cards}</div>
      </section>

      <section id="operating-dialogue" class="panel page-operate-only">
        <div class="row-head">
          <div>
            <div class="kicker">사용자 기준면 / User Operating Surface</div>
            <h2>CLI에게 넘길 구조화된 운용 지시문을 만든다</h2>
          </div>
          {_chip("directive surface")}
        </div>
        <p class="muted">이 면은 채팅방이 아니라 시키는 면입니다. 목적을 사람의 언어로 적고, 팀과 담당을 정한 뒤, 필요할 때만 실행 수단을 지정합니다. 팀/흐름/분석/생산물은 내부 심층 관측면에서 확인합니다.</p>
        <div class="panel soft surface-bridge">
          <div class="row-head">
            <div>
              <div class="kicker">표면 관계 고정</div>
              <h3>이곳은 기존 통합엔진의 간단판이 아니라 직접 운용을 시작하는 별도 전면</h3>
            </div>
            {_chip("front operation")}
          </div>
          <p class="muted">상세 session, raw payload, 전체 manifest, 깊은 라우팅 근거는 이 면에서 전면 노출하지 않습니다. 필요할 때 하단 흐름창이나 탭을 눌러 내부 심층 관측면으로 내려갑니다.</p>
        </div>
        <div class="session-strip">
          <a class="session-tab active" href="/vectorfl-engine/operate">
            <strong>사용자 기준면</strong>
            <span class="mono" id="latest-operating-dialogue-line">{latest_operating_dialogue_line}</span>
          </a>
          <a class="session-tab" href="/vectorfl-engine/team">
            <strong>팀</strong>
            <span class="mono" id="operate-worker-session-line">{latest_worker_session_line}</span>
          </a>
          <a class="session-tab" href="/vectorfl-engine/internal">
            <strong>흐름/분석</strong>
            <span class="mono" id="latest-worker-launch-draft-line">{latest_worker_launch_draft_line}</span>
          </a>
          <a class="session-tab" href="/vectorfl-engine/synthesis">
            <strong>생산물/승인</strong>
            <span class="mono" id="latest-worker-execution-line">{latest_worker_execution_line}</span>
          </a>
        </div>
        <div class="chat-only-shell">
          <div class="panel soft conversation-main directive-card">
            <div class="row-head">
              <div>
                <div class="kicker">운용 지시문</div>
                <h2>목적 / 팀 / 담당 / 실행</h2>
              </div>
              {_chip("human language first")}
            </div>
            <div class="message-stack">
              <div class="message-bubble system">
                <div class="mini-label">현재 지시 요약</div>
                <div class="body" id="conversation-user-message">{_esc(operating_purpose or "아직 입력한 운용 목적이 없습니다.")}</div>
              </div>
              <div class="message-bubble system">
                <div class="mini-label">팀 / 담당</div>
                <div class="body">{_esc(operating_team_name)} · {_esc(operating_assignee_role)} · {_esc(operating_team_purpose)}</div>
              </div>
              <div class="message-bubble worker">
                <div class="mini-label" id="conversation-worker-label">{_esc((latest_worker_execution.get("worker_label") or latest_operating_dialogue.get("selected_worker_label") or "Worker"))}</div>
                <div class="body" id="conversation-worker-message">{_esc(conversation_worker_reply)}</div>
              </div>
            </div>
            <form id="operating-dialogue-form" class="chat-composer">
              <label>현재 하려는 목적
                <textarea name="purpose" placeholder="예: 최근 로그와 스크립트 생산물을 읽고 번역용 데이터 후보를 만들어라">{_esc(operating_purpose)}</textarea>
              </label>
              <input type="hidden" name="operator_message" value="{_esc(latest_operating_dialogue.get("operator_message") or operating_purpose)}">
              <div class="directive-grid">
                <label>팀 이름
                  <input name="team_name" placeholder="예: 번역 재료 생산 팀" value="{_esc(operating_team_name)}">
                </label>
                <label>담당
                  <input name="assignee_role" placeholder="예: 라인 판독 담당" value="{_esc(operating_assignee_role)}">
                </label>
                <label class="wide">팀 목적
                  <input name="team_purpose" placeholder="예: 로그와 스크립트 생산물을 읽고 번역 후보를 생성한다" value="{_esc(operating_team_purpose)}">
                </label>
              </div>
              <details class="config-fold">
                <summary>실행 수단 / 모델 / 기준 파일 설정</summary>
                <div class="work-form">
                  <label>운영 주체
                    <select name="selected_worker">{operating_worker_options}</select>
                  </label>
                  <label>운영 모델/세션 메모
                    <input name="selected_model" placeholder="예: current codex session / codex model memo" value="{_esc(latest_operating_dialogue.get("selected_model") or latest_worker_session.get("primary_model") or "current codex session")}">
                  </label>
                  <label>보조 작업자
                    <select name="assistant_worker">{operating_assistant_options}</select>
                  </label>
                  <label>보조 모델/세션 메모
                    <input name="assistant_model" placeholder="예: gemini-cli default / claude session" value="{_esc(latest_operating_dialogue.get("assistant_model") or latest_worker_session.get("secondary_model") or "gemini-cli default")}">
                  </label>
                  <label>대화 의도
                    <select name="intent_mode">
                      <option value="configure_worker_session">worker-session 설정</option>
                      <option value="draft_work_packet">작업 지시서 초안</option>
                      <option value="ask_for_internal_read">내부 탐색 요청</option>
                      <option value="prepare_gemini_line_translation">Gemini 라인/번역 준비</option>
                    </select>
                  </label>
                  <label class="wide">기준 md / 참조 파일
                    <textarea name="reference_md_files" placeholder="docs/reports/...&#10;docs/specs/...">{_esc(operating_reference_md_files)}</textarea>
                  </label>
                  <label class="wide">라인 관련 스크립트 후보
                    <textarea name="line_script_candidates">{_esc(operating_line_script_candidates)}</textarea>
                  </label>
                  <label class="wide">금지 범위
                    <textarea name="forbidden_scope">{_esc(operating_forbidden_scope)}</textarea>
                  </label>
                  <label class="wide check-row">
                    <input type="checkbox" name="should_update_worker_session" value="true" checked>
                    <span>worker-session에도 반영</span>
                  </label>
                </div>
              </details>
              <div class="row-head">
                <button class="primary-button" type="submit">운용 지시문 저장</button>
                <span class="status-line" id="operating-dialogue-status">ready</span>
              </div>
            </form>
          </div>
          <div class="panel soft">
            <div class="row-head">
              <div>
                <div class="kicker">하단 흐름창</div>
                <h2>현재 운용 이벤트</h2>
              </div>
              {_chip("human event feed")}
            </div>
            <div class="event-feed">{event_feed_rows}</div>
          </div>
          <div id="launch" class="panel soft">
            <div class="row-head">
              <div>
                <div class="kicker">실행</div>
                <h3>{_esc(active_worker_label)}</h3>
                <p class="muted" id="latest-worker-launch-draft-summary">{_esc(latest_worker_launch_draft.get("command_preview") or "초안을 만든 뒤 선택한 CLI를 실행합니다.")}</p>
              </div>
              <span class="status-line" id="worker-launch-draft-status">ready</span>
            </div>
            <div class="chip-row">
              <button class="primary-button" id="create-worker-launch-draft-button" type="button">1. 실행 초안 생성</button>
              <button class="primary-button" id="run-worker-launch-draft-button" type="button">2. 선택한 CLI 실행</button>
            </div>
          </div>
          <div id="execution" class="panel soft status-card">
            <div class="kicker">실행 결과 요약</div>
            <p class="muted" id="latest-worker-execution-summary">{_esc(latest_worker_execution_summary or "아직 통합엔진 operate 경로에서 실행한 CLI 결과가 없습니다.")}</p>
          </div>
        </div>
      </section>

      <section id="vectorfl-surface" class="page-vectorfl-only">
        <section class="panel surface-bridge">
          <div class="row-head">
            <div>
              <div class="kicker">벡터플면 / VectorFL Surface</div>
              <h2>팀과 worker가 아니라 공간 표면의 라인 반응을 먼저 읽는다</h2>
            </div>
            {_chip("line-first surface")}
          </div>
          <p class="muted">이 면은 운영 패널이 아닙니다. 사용자면에서 지시한 일이 공간 표면에 어떤 line, relation, gap, genealogy, export/reflux로 나타났는지 읽는 표면입니다. 팀/담당/worker는 필요할 때 provenance 보조 정보로만 내려갑니다.</p>
          <div class="rear-summary-grid">
            <div class="rear-summary-card">
              <div class="mini-label">활성 라인</div>
              <h3>{len(vector_lines)}</h3>
              <p class="muted">현재 표면에서 읽히는 라인 후보</p>
            </div>
            <div class="rear-summary-card">
              <div class="mini-label">strongest</div>
              <h3>{_esc(strongest_line.get("name") or "없음")}</h3>
              <p class="muted">가장 두꺼운 출발 라인</p>
            </div>
            <div class="rear-summary-card">
              <div class="mini-label">weakest / gap</div>
              <h3>{_esc(weakest_line.get("name") or "없음")}</h3>
              <p class="muted">다음 보강 또는 외부 재료가 필요한 라인</p>
            </div>
            <div class="rear-summary-card">
              <div class="mini-label">next intervention</div>
              <h3>보강 / 환류 / 재지시</h3>
              <p class="muted">얇은 라인을 사용자면 지시 또는 내부 탐색으로 되돌린다</p>
            </div>
          </div>
        </section>
        <section id="cli-host-control" class="panel operator-dock">
          <div class="row-head">
            <div>
              <div class="kicker">CLI Host / Control Layer</div>
              <h2>기존 3면 위에서 Codex를 bounded tool로 실행하고 반환을 다시 읽는다</h2>
            </div>
            {_chip("on-top, not fourth surface")}
          </div>
          <p class="muted">이 패널은 새 표면이 아니라 VectorFL면에서 보는 CLI 조작층입니다. 실행 결과는 `runtime/cli_sessions/&lt;session_id&gt;` 아래에 남고, 이후 reread / validation / deposit 후보로 표시할 수 있습니다.</p>
          <div class="board-grid">
            <form id="cli-session-form" class="work-form">
              <label>backend
                <select name="backend_kind">
                  <option value="codex">Codex CLI</option>
                </select>
              </label>
              <label>task type
                <select name="task_type">
                  <option value="inspect">inspect</option>
                  <option value="reread">reread</option>
                  <option value="validate">validate</option>
                  <option value="summarize">summarize</option>
                  <option value="implement">implement</option>
                </select>
              </label>
              <label class="wide">purpose
                <textarea name="purpose_text" placeholder="VectorFL면에서 Codex에게 맡길 bounded task 목적을 적습니다">현재 라인/결핍/환류 상태를 읽고 다음 reread 또는 validation 후보를 요약한다.</textarea>
              </label>
              <label class="wide">bounded context refs
                <textarea name="bounded_context_refs" placeholder="docs/reports/...&#10;runtime/manifests/...">docs/reports/integrated_engine_working_interface_v1_candidate.md
runtime/views/vectorfl_dual_surface.tsx</textarea>
              </label>
              <label class="wide">prompt payload
                <textarea name="prompt_payload" placeholder="실행자가 봐야 할 세부 요청">Keep the 3-surface body fixed. Return only supervisor-readable findings and suggested next use.</textarea>
              </label>
              <label class="wide check-row">
                <input type="checkbox" name="dry_run" value="true">
                <span>dry run only: artifact path 검증만 수행</span>
              </label>
              <div class="wide row-head">
                <button class="primary-button" type="submit">Codex CLI 세션 실행</button>
                <span class="status-line" id="cli-session-status">ready</span>
              </div>
            </form>
            <div class="panel soft status-card">
              <div class="row-head">
                <div>
                  <div class="kicker">latest CLI return</div>
                  <h3 id="latest-cli-session-line">{latest_cli_session_line}</h3>
                </div>
                {_chip("session_root=" + str(cli_host_control.get("session_root") or CLI_SESSION_ROOT))}
              </div>
              <div class="rear-summary-grid">
                <div class="rear-summary-card">
                  <div class="mini-label">session id</div>
                  <h3 id="latest-cli-session-id">{_esc(latest_cli_session_id or "none")}</h3>
                  <p class="muted">canonical session folder key</p>
                </div>
                <div class="rear-summary-card">
                  <div class="mini-label">backend / task</div>
                  <h3><span id="latest-cli-backend">{_esc(latest_cli_session.get("backend_kind") or "none")}</span> / <span id="latest-cli-task">{_esc(latest_cli_session.get("task_type") or "none")}</span></h3>
                  <p class="muted">package 1.1 keeps Codex as the only enabled backend</p>
                </div>
                <div class="rear-summary-card">
                  <div class="mini-label">status</div>
                  <h3 id="latest-cli-status">{_esc(latest_cli_session.get("status") or "none")}</h3>
                  <p class="muted">queued / running / done / failed</p>
                </div>
                <div class="rear-summary-card">
                  <div class="mini-label">marks</div>
                  <h3 id="latest-cli-marks">{_esc(latest_cli_marks)}</h3>
                  <p class="muted" id="latest-cli-mark-history">{_esc(latest_cli_mark_history)}</p>
                </div>
              </div>
              <div class="mini-label">purpose</div>
              <p class="body" id="latest-cli-purpose">{_esc(latest_cli_session.get("purpose_text") or "no latest purpose")}</p>
              <div class="mini-label">structured return preview</div>
              <p class="body" id="latest-cli-result-summary">{_esc(str(latest_cli_result_summary)[:2400])}</p>
              <div class="mini-label">deposit candidate preview</div>
              <pre class="mono" id="latest-cli-deposit-preview">{_esc(str(latest_cli_deposit_preview)[:2200] or "no deposit candidate preview yet")}</pre>
              <div class="chip-row">
                <button class="primary-button" id="refresh-cli-return-button" type="button">refresh latest return</button>
                <button class="primary-button" id="mark-cli-reread-button" type="button">reread target</button>
                <button class="primary-button" id="mark-cli-implementation-button" type="button">implementation return</button>
                <button class="primary-button" id="mark-cli-validation-button" type="button">validation target</button>
                <button class="primary-button" id="mark-cli-deposit-button" type="button">send to engine deposit</button>
              </div>
              <p class="muted">표시는 session.json의 marks만 갱신합니다. package 1에서는 deposit 후보 파일을 준비하고, 실제 promotion / ingestion은 열지 않습니다.</p>
            </div>
          </div>
        </section>
        <div class="line-dashboard">
          <div class="panel">
            <div class="row-head">
              <div>
                <div class="kicker">Line Atlas</div>
                <h2>공간 표면에 드러난 라인 목록</h2>
              </div>
              {_chip("not team board")}
            </div>
            <div class="line-atlas">{_line_surface_cards(vector_lines, selected_vector_line)}</div>
          </div>
          <div class="panel line-inspector">
            <div class="row-head">
              <div>
                <div class="kicker">Selected Line Inspector</div>
                <h2>{_esc(selected_vector_line.get("name") or "선택 라인 없음")}</h2>
              </div>
              {_chip(_line_health_label(selected_vector_line.get("health")))}
            </div>
            <p class="body">{_esc(selected_vector_line.get("purpose") or "")}</p>
            <div>
              <div class="mini-label">anchors</div>
              <div class="chip-row">{_chips(selected_vector_line.get("anchors") or [])}</div>
            </div>
            <div>
              <div class="mini-label">weak points / gaps</div>
              <div class="chip-row">{_chips(selected_vector_line.get("weak_points") or [])}</div>
            </div>
            <div>
              <div class="mini-label">export to user</div>
              <div class="chip-row">{_chips(selected_vector_line.get("export") or [])}</div>
            </div>
            <div>
              <div class="mini-label">expected reflux</div>
              <div class="chip-row">{_chips(selected_vector_line.get("reflux") or [])}</div>
            </div>
            <p class="muted">{_esc(selected_vector_line.get("note") or "")}</p>
          </div>
        </div>
        <div class="board-grid">
          <section class="panel">
            <div class="row-head">
              <div>
                <div class="kicker">Line Genealogy</div>
                <h2>선택 라인이 어떤 흐름에서 자랐는지</h2>
              </div>
              {_chip("genealogy")}
            </div>
            <div class="loop-list">
              {''.join(f'<div class="loop-row"><div class="loop-index">{idx:02d}</div><div class="loop-main"><strong>{_esc(step)}</strong><span class="muted">selected line growth step</span></div></div>' for idx, step in enumerate(selected_vector_line.get("genealogy") or [], start=1))}
            </div>
          </section>
          <section class="panel">
            <div class="row-head">
              <div>
                <div class="kicker">Relation Web</div>
                <h2>라인 사이의 연결</h2>
              </div>
              {_chip("relation")}
            </div>
            <div class="event-feed">{_relation_rows(vector_lines)}</div>
          </section>
        </div>
        <section class="panel">
          <div class="row-head">
            <div>
              <div class="kicker">Line Event Stream</div>
              <h2>표면 이벤트를 라인 언어로 읽는다</h2>
            </div>
            {_chip("surface events")}
          </div>
          <div class="event-feed">{_line_event_rows(vector_lines)}</div>
        </section>
      </section>

      <section id="engine-surface-placeholder" class="panel page-engine-only">
        <div class="row-head">
          <div>
            <div class="kicker">엔진면 / Engine Surface</div>
            <h2>통합엔진의 내부 재료와 상태를 보는 정비 기준면</h2>
          </div>
          {_chip("engine-only")}
        </div>
        <p class="muted">이 페이지는 이제 사용자면이 아니라 엔진면입니다. 사용자면과 벡터플면은 `runtime/views/vectorfl_dual_surface.tsx` 기반 React surface app으로 분리하고, 이 면은 공간 내부 재료 목록, 상태창, script/md/json 접근, 유지보수 포인트를 다룹니다.</p>
        <div class="engine-placeholder-grid">
          <div class="rear-summary-card">
            <div class="mini-label">inventory</div>
            <h3>공간 내부 재료 목록</h3>
            <p class="muted">입력 자산, 생성 라인, 최근 결과물, 관련 파일 목록</p>
            <div class="chip-row">
              {_chip(f"manifests={len(state.get('latest_manifests') or {})}")}
              {_chip(f"contracts={len(contracts)}")}
            </div>
          </div>
          <div class="rear-summary-card">
            <div class="mini-label">space status</div>
            <h3>공간 상태창</h3>
            <p class="muted">활성 흐름, 오류/경고, 환류 대기, 출력 품질</p>
            <div class="chip-row">
              {_chip("posture=" + str(state.get("current_posture") or "unknown"))}
              {_chip(execution_posture_label)}
            </div>
          </div>
          <div class="rear-summary-card">
            <div class="mini-label">script access</div>
            <h3>script / md / json</h3>
            <p class="muted">내부 탐색과 라인 생성을 만든 실제 자산 접근</p>
            <div class="chip-row">
              {_chips([candidate.get("path") for candidate in line_script_registry if candidate.get("path")][:2])}
            </div>
          </div>
          <div class="rear-summary-card">
            <div class="mini-label">maintenance</div>
            <h3>정비 포인트</h3>
            <p class="muted">연료 부족, 내부 수정 포인트, 회귀 검증 후보</p>
            <div class="chip-row">
              {_chip("freshness regression fixture next", tone="warn")}
            </div>
          </div>
        </div>
      </section>

      <section id="operator-dock" class="panel operator-dock page-team-only">
        <div class="row-head">
          <div>
            <div class="kicker">운용 도크</div>
            <h2>상단에서 지시 / 팀 / 담당 / 기준 md를 먼저 고정한다</h2>
          </div>
          {_chip("creates work packet + assignment")}
        </div>
        <p class="muted">정상 동작이 잠기기 전까지 아래 구조 설명은 남깁니다. 하지만 실제 운용은 여기서 시작합니다. 이 도크는 work packet을 저장한 뒤 같은 입력으로 assignment까지 이어서 저장합니다.</p>
        <form id="quick-operating-form" class="work-form">
          <label class="wide">지시
            <textarea name="directive" placeholder="이번 세션에서 처리할 지시를 적습니다">{_esc(latest_work_packet.get("directive") or "")}</textarea>
          </label>
          <label class="wide">입력/메모
            <textarea name="memo" placeholder="배경, 사용자가 말한 압력, 내부에서 먼저 찾아야 할 재료">{_esc(latest_work_packet.get("memo") or "")}</textarea>
          </label>
          <label>팀 지정
            <select name="team_id">{team_options}</select>
          </label>
          <label>담당 cell
            <select name="assignee_cell">{cell_options}</select>
          </label>
          <label class="wide">기준 md / 참조 파일
            <textarea name="reference_md_files" placeholder="docs/specs/...&#10;docs/contracts/...&#10;docs/reports/...">{_esc(latest_reference_md_files)}</textarea>
          </label>
          <label>기대 보고
            <textarea name="expected_output">summary
evidence used
line candidates or confirmed lines
next routing recommendation</textarea>
          </label>
          <label>금지 범위
            <textarea name="forbidden_scope">do not replace current slot
do not declare gate close
do not run fake execution
do not jump to external search before internal line is shaped</textarea>
          </label>
          <div class="wide row-head">
            <button class="primary-button" type="submit">작업 지시서 + 팀 배치 저장</button>
            <span class="status-line" id="quick-operating-status">ready</span>
          </div>
        </form>
      </section>

      <section id="worker-session-dock" class="panel page-team-only">
        <div class="row-head">
          <div>
            <div class="kicker">작업자 세션 설정 / Worker Session</div>
            <h2>Gemini CLI를 내부 흐름 읽기와 번역 재료 생산 담당으로 지정한다</h2>
          </div>
          {_chip("records config only")}
        </div>
        <p class="muted">이 슬롯은 Gemini를 실행하지 않습니다. 지금 켜진 Gemini CLI 터미널이 어떤 모델/역할/스크립트 후보/번역 재료를 맡는지 화면 안에 남겨서, 사용자가 터미널과 페이지 사이에서 맥락을 잃지 않게 합니다.</p>
        <div class="panel soft">
          <div class="kicker">최근 작업자 세션</div>
          <div class="mono" id="latest-worker-session-line">{latest_worker_session_line}</div>
          <div class="muted" id="latest-worker-session-task">{_esc(latest_worker_session.get("active_task") or "Gemini에게 맡길 내부 읽기/라인/번역 작업을 아직 저장하지 않았습니다.")}</div>
        </div>
        <form id="worker-session-form" class="work-form">
          <label>주 운영자
            <select name="primary_worker">{primary_worker_options}</select>
          </label>
          <label>Codex 세션/모델 메모
            <input name="codex_model" value="{_esc(latest_worker_session.get("primary_model") or "current codex session")}">
          </label>
          <label>보조 작업자
            <select name="secondary_worker">{secondary_worker_options}</select>
          </label>
          <label>Gemini 모델/세션 메모
            <input name="gemini_model" placeholder="예: gemini-cli default / gemini-2.5-pro / session name" value="{_esc(latest_worker_session.get("secondary_model") or "gemini-cli default")}">
          </label>
          <label class="wide">Gemini 역할
            <textarea name="gemini_role">{_esc(latest_worker_session.get("gemini_role") or "내부 흐름을 읽고, 라인 관련 스크립트를 검토/실행 보조하며, 라인을 두텁게 만들 번역 재료를 생산한다. repo 수정은 하지 않는다.")}</textarea>
          </label>
          <label class="wide">현재 맡길 작업
            <textarea name="active_task" placeholder="예: line thickening scripts를 읽고 실행 후보를 정리한 뒤 번역 재료 후보를 보고하라">{_esc(latest_worker_session.get("active_task") or "")}</textarea>
          </label>
          <label class="wide">라인 관련 스크립트 후보
            <textarea name="line_script_candidates">{_esc(latest_line_script_candidates)}</textarea>
          </label>
          <label class="wide">번역 재료 후보 md/json
            <textarea name="translation_material_targets">{_esc(latest_translation_targets)}</textarea>
          </label>
          <label class="wide">감독자가 화면에서 봐야 할 상태
            <textarea name="operator_visibility">current worker
chosen model
active task
script candidates
latest return slot
blocked conditions</textarea>
          </label>
          <label class="wide">금지 범위
            <textarea name="forbidden_scope">do not modify repo without supervisor approval
do not replace current slot
do not declare gate close
do not treat Gemini as primary operating authority</textarea>
          </label>
          <div class="wide row-head">
            <button class="primary-button" id="auto-worker-session-button" type="button">현재 맥락으로 자동 세팅</button>
            <button class="primary-button" type="submit">작업자 세션 설정 저장</button>
            <span class="status-line" id="worker-session-status">ready</span>
          </div>
        </form>
      </section>

      <section id="worker-policy" class="panel page-overview-only">
        <div class="row-head">
          <div>
            <div class="kicker">Session Worker Policy</div>
            <h2>모델은 전역 기준이 아니라 이번 세션의 담당 역할로 고정한다</h2>
          </div>
          {_chip("script-first / CLI-interpret")}
        </div>
        <p class="body">{_esc(worker_policy.get("principle") or "")}</p>
        <div class="board-grid">
          <div class="panel soft">
            <div class="kicker">Primary Operator</div>
            <h3>{_esc((worker_policy.get("primary_operator") or {}).get("worker") or "codex")}</h3>
            <p class="muted">{_esc((worker_policy.get("primary_operator") or {}).get("role") or "")}</p>
          </div>
          <div class="panel soft">
            <div class="kicker">Secondary Operator</div>
            <h3>{_esc((worker_policy.get("secondary_operator") or {}).get("worker") or "gemini")}</h3>
            <p class="muted">{_esc((worker_policy.get("secondary_operator") or {}).get("role") or "")}</p>
          </div>
        </div>
        <div class="board-grid">
          <div>
            <div class="mini-label">script-first jobs</div>
            <div class="chip-row">{_chips(worker_policy.get("script_first_jobs") or [])}</div>
          </div>
          <div>
            <div class="mini-label">CLI worker jobs</div>
            <div class="chip-row">{_chips(worker_policy.get("cli_worker_jobs") or [])}</div>
          </div>
        </div>
      </section>

      <section id="board" class="panel page-overview-only">
        <div class="row-head">
          <div>
            <div class="kicker">Operating Board</div>
            <h2>{_esc(board.get("current_proof") or "")}</h2>
          </div>
          {_chip("supervisor entrypoint")}
        </div>
        <p class="body">{_esc(board.get("why_now") or "")}</p>
        <div class="board-grid">
          <div class="panel soft">
            <div class="kicker">Active Case</div>
            {''.join(f'<div class="row"><div><strong>{_esc(case.get("case_id"))}</strong><div class="muted">{_esc(case.get("current_line_pressure"))}</div><div class="body">{_esc(case.get("next_move"))}</div></div>{_chip(case.get("stage"))}</div>' for case in board.get("active_cases") or [])}
          </div>
          <div class="panel soft">
            <div class="kicker">Decision Queue</div>
            {''.join(f'<div class="row"><div><strong>{_esc(item.get("decision"))}</strong><div class="muted">{_esc(item.get("why_decision_is_needed"))}</div><div class="mono">{_esc(item.get("continue_gate"))}</div></div></div>' for item in board.get("decision_queue") or [])}
          </div>
        </div>
        <div>
          <div class="mini-label">remaining gates</div>
          <div class="chip-row">{_chips(board.get("remaining_gates") or [])}</div>
        </div>
      </section>

      <section id="work-packet" class="panel page-team-only">
        <div class="row-head">
          <div>
            <div class="kicker">작업 지시서 / Work Packet</div>
            <h2>사용자 입력을 다음 담당 cell에 넘길 실제 운영 재료로 저장한다</h2>
          </div>
          {_chip("writes latest work packet")}
        </div>
        <p class="muted">이 폼은 worker를 실행하지 않습니다. 감독자가 현재 주제/메모/지시를 정리해 다음 line generation 또는 internal-read handoff의 입력 artifact로 남깁니다.</p>
        <div class="panel soft">
          <div class="kicker">Latest Packet</div>
          <div class="mono" id="latest-work-packet-line">{latest_packet_line}</div>
          <div class="muted">{_esc(latest_work_packet.get("directive") or latest_work_packet.get("topic") or "")}</div>
        </div>
        <form id="work-packet-form" class="work-form">
          <label class="wide">topic
            <input name="topic" placeholder="지금 감독자가 다룰 주제">
          </label>
          <label class="wide">directive
            <textarea name="directive" placeholder="다음 담당자에게 넘길 실제 지시를 적습니다"></textarea>
          </label>
          <label class="wide">memo
            <textarea name="memo" placeholder="배경, 압력, 방금 교정한 관점, 참조해야 할 내부 재료"></textarea>
          </label>
          <label>selected stage
            <select name="selected_stage">{stage_options}</select>
          </label>
          <label>target cell
            <select name="target_cell">{cell_options}</select>
          </label>
          <label class="wide">requested action
            <textarea name="requested_action">translate the supervisor input into the next bounded operating handoff</textarea>
          </label>
          <label>expected output
            <textarea name="expected_output">line candidates
unclear points
next routing recommendation</textarea>
          </label>
          <label>forbidden scope
            <textarea name="forbidden_scope">do not replace current slot
do not declare gate close
do not run fake worker execution</textarea>
          </label>
          <label class="wide">supervisor note
            <textarea name="supervisor_note" placeholder="결정 이유나 다음 확인 조건"></textarea>
          </label>
          <div class="wide row-head">
            <button class="primary-button" type="submit">작업 지시서 저장</button>
            <span class="status-line" id="work-packet-status">ready</span>
          </div>
        </form>
        <div class="panel soft" id="codex-run-panel">
          <div class="row-head">
            <div>
              <div class="kicker">작업자 읽기 보고 / Worker Report</div>
              <h3>latest assignment를 read-only Codex report로 실행</h3>
            </div>
            {_chip("actual codex bridge")}
          </div>
          <div class="mono" id="latest-codex-run-line">{latest_codex_run_line}</div>
          <div class="muted" id="latest-codex-return-summary">{_esc(codex_return_summary or ("codex_return=" + str(codex_return)))}</div>
          <div class="row-head">
            <button class="primary-button" id="run-codex-assignment-button" type="button">Codex 읽기 보고 실행</button>
            <span class="status-line" id="codex-run-status">ready</span>
          </div>
          <div class="muted">이 액션은 latest assignment를 Codex handoff로 변환한 뒤 기존 read-only Codex bridge를 실행합니다. 제품 구현 완료가 아니라 worker report return 경로 검증입니다.</div>
        </div>
      </section>

      <section id="team-board" class="panel page-team-only">
        <div class="row-head">
          <div>
            <div class="kicker">팀/담당 배치 / Assignment</div>
            <h2>팀과 담당을 먼저 고정하고 보고 슬롯으로 되돌린다</h2>
          </div>
          {_chip(f"{len(teams)} teams")}
        </div>
        <p class="muted">팀은 탭 이름이 아니라 책임 단위입니다. 각 팀은 primary cell, members, report slot을 갖고 assignment는 latest artifact 하나로 남습니다.</p>
        <div class="panel soft">
          <div class="kicker">현재 운용 순서</div>
          <div class="chip-row">
            {_chip("1 작업 지시서")}
            {_chip("2 팀/담당 배치")}
            {_chip("3 작업자 읽기 보고")}
            {_chip("4 감독 판단")}
          </div>
          <p class="body">Paperclip의 issue/detail/properties/run 구조를 VectorFL식으로 줄이면, 지금 페이지는 작업 패킷을 만들고 팀에 배치한 뒤 worker report를 받아 supervisor gate로 되돌리는 선을 먼저 잠급니다.</p>
        </div>
        <div class="panel soft">
          <div class="kicker">최근 팀/담당 배치</div>
          <div class="mono" id="latest-assignment-line">{latest_assignment_line}</div>
          <div class="muted" id="latest-assignment-brief">{_esc(latest_assignment.get("brief") or latest_assignment.get("title") or "")}</div>
        </div>
        <div class="panel soft">
          <div class="row-head">
            <div>
              <div class="kicker">최근 작업자 보고</div>
              <h3>Codex return summary</h3>
            </div>
            {_chip("return_slot=line_candidates_latest")}
          </div>
          <p class="body">{_esc(codex_return_summary or "no worker report summary yet")}</p>
          <div class="mini-label">next recommendation</div>
          <div class="mono">{_esc(codex_next_recommendation or "pending")}</div>
        </div>
        <div class="panel soft" id="supervisor-route-panel">
          <div class="row-head">
            <div>
              <div class="kicker">감독 라우팅 / Supervisor Route</div>
              <h3>worker report를 다음 팀으로 보낼지 결정</h3>
            </div>
            {_chip("report gate")}
          </div>
          <div class="mono" id="latest-supervisor-route-line">{latest_route_line}</div>
          <form id="supervisor-route-form" class="work-form">
            <label>decision
              <select name="decision">
                <option value="accept_for_internal_read">accept for internal read</option>
                <option value="hold">hold</option>
                <option value="request_revision">request revision</option>
                <option value="route_to_synthesis">route to synthesis</option>
              </select>
            </label>
            <label>target team
              <select name="target_team">{route_team_options}</select>
            </label>
            <label class="wide">rationale
              <textarea name="rationale">Codex returned line candidates; route them to the next team without treating the bridge as gate close.</textarea>
            </label>
            <label class="wide">next instruction
              <textarea name="next_instruction">Use the Codex line candidates to inspect internal records and return evidence-backed line seeds.</textarea>
            </label>
            <div class="wide row-head">
              <button class="primary-button" type="submit">감독 라우팅 저장</button>
              <span class="status-line" id="supervisor-route-status">ready</span>
            </div>
          </form>
        </div>
        <div class="team-grid">{_team_cards(teams)}</div>
        <form id="assignment-form" class="work-form">
          <label>team
            <select name="team_id">{team_options}</select>
          </label>
          <label>assignee cell
            <select name="assignee_cell">{cell_options}</select>
          </label>
          <label class="wide">title
            <input name="title" placeholder="배치할 작업 제목">
          </label>
          <label class="wide">brief
            <textarea name="brief" placeholder="담당자가 무엇을 읽고 무엇을 요약해서 돌려줘야 하는지"></textarea>
          </label>
          <label>expected report
            <textarea name="expected_report">summary
evidence used
blockers
next routing recommendation</textarea>
          </label>
          <label>review focus
            <textarea name="review_focus" placeholder="특히 확인할 관점"></textarea>
          </label>
          <label class="wide">forbidden scope
            <textarea name="forbidden_scope">do not run fake worker execution
do not replace current slot
do not declare gate close</textarea>
          </label>
          <div class="wide row-head">
            <button class="primary-button" type="submit">팀/담당 배치 저장</button>
            <span class="status-line" id="assignment-status">ready</span>
          </div>
        </form>
      </section>

      <section id="internal-read" class="panel page-internal-only">
        <div class="row-head">
          <div>
            <div class="kicker">내부 탐색 / Internal Read</div>
            <h2>supervisor route를 받아 내부 기록/코드/잠금 문서를 먼저 읽는다</h2>
          </div>
          {_chip("internal_space_team")}
        </div>
        <p class="muted">이 면은 외부 검색보다 앞선 내부 검색 단계입니다. latest supervisor route와 Codex line-candidate return을 입력으로 삼아 stable / unclear / next questions / line seeds를 report artifact로 남깁니다.</p>
        <div class="board-grid">
          <div class="panel soft">
            <div class="kicker">Latest Supervisor Route</div>
            <div class="mono">{latest_route_line}</div>
            <div class="muted">{_esc(latest_supervisor_route.get("next_instruction") or "route instruction pending")}</div>
          </div>
          <div class="panel soft" id="internal-read-run-panel">
            <div class="kicker">Internal Read Run</div>
            <div class="mono" id="latest-internal-read-run-line">{internal_read_run_line}</div>
            <button class="primary-button" id="run-internal-read-button" type="button">내부 탐색 보고 실행</button>
            <span class="status-line" id="internal-read-run-status">ready</span>
          </div>
        </div>
        <div class="panel soft">
          <div class="row-head">
            <div>
              <div class="kicker">최근 내부 탐색 보고</div>
              <h3 id="latest-internal-read-line">{latest_internal_read_line}</h3>
            </div>
            {_chip("report_slot=internal_read_report_latest")}
          </div>
          <p class="body" id="latest-internal-read-summary">{_esc(latest_internal_read_report.get("summary") or "no internal read report summary yet")}</p>
          <div class="mini-label">stable</div>
          <div class="chip-row" id="latest-internal-read-stable">{_chips(latest_internal_read_report.get("stable") or [])}</div>
          <div class="mini-label">unclear</div>
          <div class="chip-row" id="latest-internal-read-unclear">{_chips(latest_internal_read_report.get("unclear") or [])}</div>
          <div class="mini-label">next questions</div>
          <div class="chip-row" id="latest-internal-read-questions">{_chips(latest_internal_read_report.get("next_questions") or [])}</div>
        </div>
        <div class="cell-grid" id="latest-line-seeds">{_line_seed_cards(latest_internal_read_report.get("line_seeds") or [])}</div>
      </section>

      <section id="synthesis" class="panel page-synthesis-only">
        <div class="row-head">
          <div>
            <div class="kicker">종합 보고 / Synthesis</div>
            <h2>내부 읽기 결과를 감독자 판단용 보고서로 압축한다</h2>
          </div>
          {_chip("synthesis_team")}
        </div>
        <p class="muted">이 단계는 외부 검색이나 구현으로 점프하지 않습니다. latest internal read report를 받아 confirmed lines, unresolved tensions, recommendation, next loop proposal로 번역합니다.</p>
        <div class="board-grid">
          <div class="panel soft">
            <div class="kicker">Input: Latest Internal Read</div>
            <div class="mono">{latest_internal_read_line}</div>
            <p class="body">{_esc(latest_internal_read_report.get("summary") or "no internal read report summary yet")}</p>
            <div class="mini-label">line seeds</div>
            <div class="chip-row">{_chips([seed.get("line_name") for seed in latest_internal_read_report.get("line_seeds") or []])}</div>
          </div>
          <div class="panel soft" id="synthesis-run-panel">
            <div class="kicker">Synthesis Run</div>
            <div class="mono" id="latest-synthesis-run-line">{synthesis_run_line}</div>
            <button class="primary-button" id="run-synthesis-button" type="button">종합 보고 실행</button>
            <span class="status-line" id="synthesis-run-status">ready</span>
          </div>
        </div>
        <div class="panel soft">
          <div class="row-head">
            <div>
              <div class="kicker">최근 종합 보고</div>
              <h3 id="latest-synthesis-line">{latest_synthesis_line}</h3>
            </div>
            {_chip("report_slot=supervisor_report_latest")}
          </div>
          <p class="body" id="latest-synthesis-status">{_esc(latest_synthesis_report.get("current_status") or "no synthesis report yet")}</p>
          <div class="mini-label">recommendation</div>
          <div class="mono" id="latest-synthesis-recommendation">{_esc((latest_synthesis_report.get("recommendation") or "pending") + " / " + (latest_synthesis_report.get("recommendation_reason") or ""))}</div>
          <div class="mini-label">confirmed lines</div>
          <div class="chip-row" id="latest-synthesis-lines">{_chips([line.get("line_name") for line in latest_synthesis_report.get("confirmed_lines") or []])}</div>
          <div class="mini-label">unresolved tensions</div>
          <div class="chip-row" id="latest-synthesis-tensions">{_chips(latest_synthesis_report.get("unresolved_tensions") or [])}</div>
          <div class="mini-label">next loop</div>
          <div class="mono" id="latest-synthesis-next-loop">{_esc(json.dumps(latest_synthesis_report.get("next_loop_proposal") or {}, ensure_ascii=False))}</div>
        </div>
        <div class="panel soft" id="supervisor-gate-panel">
          <div class="row-head">
            <div>
              <div class="kicker">감독 판단 / Supervisor Gate</div>
              <h3>합성 보고서를 보고 다음 단계 승인/보류/재개를 저장한다</h3>
            </div>
            {_chip("records decision only")}
          </div>
          <div class="mono" id="latest-supervisor-gate-line">{latest_gate_line}</div>
          <form id="supervisor-gate-form" class="work-form">
            <label>결정
              <select name="decision">
                <option value="approve_implementation_brief">approve implementation brief</option>
                <option value="hold">hold</option>
                <option value="reopen_internal_read">reopen internal read</option>
                <option value="redirect">redirect</option>
              </select>
            </label>
            <label>대상 팀
              <select name="target_team">{route_team_options}</select>
            </label>
            <label class="wide">승인할 line
              <textarea name="approved_line_names">{_esc(synthesis_line_names)}</textarea>
            </label>
            <label class="wide">이유
              <textarea name="rationale">{_esc(latest_synthesis_report.get("recommendation_reason") or "")}</textarea>
            </label>
            <label class="wide">다음 지시
              <textarea name="next_instruction">Create a bounded implementation brief from the approved synthesis lines. Do not run implementation yet.</textarea>
            </label>
            <label class="wide">계속 유지할 금지선
              <textarea name="guardrail_overrides">no gate close
no slot replacement
no external search
no broad orchestration
report return is not product completion</textarea>
            </label>
            <div class="wide row-head">
              <button class="primary-button" type="submit">감독 판단 저장</button>
              <span class="status-line" id="supervisor-gate-status">ready</span>
            </div>
          </form>
        </div>
        <div class="panel soft" id="implementation-brief-panel">
          <div class="row-head">
            <div>
              <div class="kicker">구현 지시서 / Implementation Brief</div>
              <h3>감독자가 승인한 line만 구현팀 입력으로 번역한다</h3>
            </div>
            {_chip("brief only")}
          </div>
          <div class="mono" id="latest-implementation-brief-line">{latest_implementation_brief_line}</div>
          <p class="muted">이 버튼은 구현을 실행하지 않습니다. 승인된 supervisor gate에서 구현팀에게 넘길 brief artifact만 만듭니다.</p>
          <div class="row-head">
            <button class="primary-button" id="create-implementation-brief-button" type="button">구현 지시서 만들기</button>
            <span class="status-line" id="implementation-brief-status">ready</span>
          </div>
        </div>
        <div class="panel soft" id="implementation-launch-gate-panel">
          <div class="row-head">
            <div>
              <div class="kicker">구현 실행 허가 / Implementation Launch Gate</div>
              <h3>구현 실행 여부를 따로 승인한다</h3>
            </div>
            {_chip("decision only")}
          </div>
          <div class="mono" id="latest-implementation-launch-gate-line">{latest_implementation_launch_gate_line}</div>
          <p class="muted">이 섹션도 구현을 실행하지 않습니다. 다음 세션이나 별도 worker run에서 Codex에게 구현을 맡길 수 있는지 승인 상태만 남깁니다.</p>
          <form id="implementation-launch-gate-form" class="work-form">
            <label>결정
              <select name="decision">
                <option value="approve_codex_run">approve codex run</option>
                <option value="hold">hold</option>
                <option value="reopen_brief">reopen brief</option>
                <option value="redirect">redirect</option>
              </select>
            </label>
            <label>worker
              <select name="target_worker">
                <option value="codex">codex</option>
                <option value="gemini">gemini review only</option>
              </select>
            </label>
            <label class="wide">실행 지시
              <textarea name="run_instruction">Use the latest implementation brief as input. Confirm target files before editing. Return changed files, blockers, and verification commands.</textarea>
            </label>
            <label class="wide">사전 확인
              <textarea name="preflight_checks">read implementation brief
confirm target files before editing
preserve current slot
do not declare gate close
return changed files and blockers</textarea>
            </label>
            <label class="wide">이유
              <textarea name="rationale">Implementation brief is ready for a separately supervised worker run, but this page records only launch approval.</textarea>
            </label>
            <div class="wide row-head">
              <button class="primary-button" type="submit">구현 실행 허가 저장</button>
              <span class="status-line" id="implementation-launch-gate-status">ready</span>
            </div>
          </form>
        </div>
      </section>

      <section id="loop" class="panel page-overview-only">
        <div class="row-head">
          <div>
            <div class="kicker">Engine Loop</div>
            <h2>입력 해석에서 검증 반환까지 책임 전이를 먼저 보인다</h2>
          </div>
          {_chip(f"{len(stages)} stages")}
        </div>
        <div class="loop-list">{_loop_rows(stages)}</div>
      </section>

      <section id="cells" class="panel page-overview-only">
        <div class="row-head">
          <div>
            <div class="kicker">Operating Cells</div>
            <h2>이름 목록이 아니라 계약 기반 작업 단위</h2>
          </div>
          {_chip(f"{len(cells)} cells")}
        </div>
        <div class="cell-grid">{_cell_cards(cells)}</div>
      </section>

      <section id="substrate" class="panel page-overview-only">
        <div class="row-head">
          <div>
            <div class="kicker">Bridge Substrate</div>
            <h2>기존 Paper proper / Codex / Gemini / validator 결과는 재료로만 사용</h2>
          </div>
          {_chip("read-only summary")}
        </div>
        <div class="chip-row">
          {_chip("codex handoff=" + str(bridge.get("codex_handoff_status") or "unknown"))}
          {_chip("codex return=" + str(bridge.get("codex_return_status") or "unknown"))}
          {_chip("gemini=" + str(bridge.get("gemini_review_status") or "unknown"))}
          {_chip("gate=" + str(bridge.get("gate_effect") or "unknown"))}
        </div>
      </section>
    </main>

    <footer class="engine-footer">
      <div class="footer-status">
        <div class="kicker">현재 엔진</div>
        <strong>{_esc(active_team_label)}</strong>
        <span class="muted">{_esc(assignee_summary)} · {_esc(active_worker_label)} · {_esc(execution_posture_label)}</span>
      </div>
      <div class="footer-events">{footer_event_rows}</div>
      <div class="footer-return">
        <div class="kicker">최근 반환</div>
        <div class="mono">{latest_worker_execution_line}</div>
        <a class="muted" href="/vectorfl-engine/synthesis">{_esc(result_link_label)}</a>
      </div>
    </footer>

    <aside class="inspector">
      <section class="panel soft">
        <div class="kicker">Assignment / Gate Inspector</div>
        <div class="team-title">
          <span class="team-mark">{_esc(active_team_visual.get("short") or "TM")}</span>
          <div>
            <div class="mini-label">{_esc(active_team_visual.get("rank") or "active team")}</div>
            <h3>{_esc(latest_assignment.get("title") or latest_work_packet.get("topic") or "no active packet")}</h3>
          </div>
        </div>
        <div class="row">
          <span class="muted">team</span>
          <span class="mono">{_esc(latest_assignment.get("team_id") or "pending")}</span>
        </div>
        <div class="row">
          <span class="muted">assignee</span>
          <span class="mono">{_esc(latest_assignment.get("assignee_cell") or latest_work_packet.get("target_cell") or "pending")}</span>
        </div>
        <div class="row">
          <span class="muted">return slot</span>
          <span class="mono">{_esc(latest_assignment.get("return_slot") or latest_supervisor_route.get("target_report_slot") or "pending")}</span>
        </div>
        <div class="row">
          <span class="muted">route</span>
          <span class="mono">{_esc(latest_supervisor_route.get("decision") or "pending")} -> {_esc(latest_supervisor_route.get("target_team") or "pending")}</span>
        </div>
        <div class="mini-label">latest recommendation</div>
        <div class="mono">{_esc((latest_synthesis_report.get("recommendation") or "pending") + " / " + (latest_synthesis_report.get("recommendation_reason") or ""))}</div>
        <div class="mini-label">guard</div>
        <div class="chip-row">
          {_chip("report return only")}
          {_chip("no gate close", tone="warn")}
          {_chip("no slot replacement", tone="warn")}
        </div>
        <div class="mini-label">session model rule</div>
        <div class="mono">{_esc((worker_policy.get("primary_operator") or {}).get("worker") or "codex")} primary / {_esc((worker_policy.get("secondary_operator") or {}).get("worker") or "gemini")} review / script-first internal collection</div>
      </section>
      <section class="panel soft">
        <div class="kicker">운용어 번역표</div>
        <h3>내부 이름을 화면 조작 언어로 읽는 기준</h3>
        {_glossary_rows()}
      </section>
      <section class="panel soft">
        <div class="kicker">Contract Readout</div>
        {_contract_rows(contracts)}
      </section>
      <section class="panel soft">
        <div class="kicker">Next Boundary</div>
        <h3>{_esc(next_boundary.get("first_real_object") or "work_packet")}</h3>
        <div class="mini-label">first real actions</div>
        <div class="chip-row">{_chips(next_boundary.get("first_real_actions") or [])}</div>
        <div class="mini-label">do not build yet</div>
        <div class="chip-row">{_chips(next_boundary.get("do_not_build_yet") or [])}</div>
      </section>
      <section class="panel soft">
        <div class="kicker">Command Slots</div>
        <div class="command-slot">
          <strong>line-generation handoff</strong>
          <span class="muted">disabled until explicit action route exists</span>
        </div>
        <div class="command-slot">
          <strong>internal-read return</strong>
          <span class="muted">must write a return artifact, not chat-only notes</span>
        </div>
        <div class="command-slot">
          <strong>verification route</strong>
          <span class="muted">must stay tied to supervisor decision gate</span>
        </div>
      </section>
    </aside>
  </div>
  <script>
    const engineState = JSON.parse(document.getElementById("vectorfl-integrated-engine-state").textContent);
    const workPacketForm = document.getElementById("work-packet-form");
    const workPacketStatus = document.getElementById("work-packet-status");
    const latestPacketLine = document.getElementById("latest-work-packet-line");
    const workPacketPanel = document.getElementById("work-packet");
    const quickOperatingForm = document.getElementById("quick-operating-form");
    const quickOperatingStatus = document.getElementById("quick-operating-status");
    const quickOperatingPanel = document.getElementById("operator-dock");
    const operatingDialogueForm = document.getElementById("operating-dialogue-form");
    const operatingDialogueStatus = document.getElementById("operating-dialogue-status");
    const operatingDialoguePanel = document.getElementById("operating-dialogue");
    const latestOperatingDialogueLine = document.getElementById("latest-operating-dialogue-line");
    const latestOperatingDialogueSummary = document.getElementById("latest-operating-dialogue-summary");
    const operateWorkerSessionLine = document.getElementById("operate-worker-session-line");
    const operateWorkerSessionTask = document.getElementById("operate-worker-session-task");
    const conversationUserMessage = document.getElementById("conversation-user-message");
    const conversationWorkerLabel = document.getElementById("conversation-worker-label");
    const conversationWorkerMessage = document.getElementById("conversation-worker-message");
    const createWorkerLaunchDraftButton = document.getElementById("create-worker-launch-draft-button");
    const runWorkerLaunchDraftButton = document.getElementById("run-worker-launch-draft-button");
    const workerLaunchDraftStatus = document.getElementById("worker-launch-draft-status");
    const latestWorkerLaunchDraftLine = document.getElementById("latest-worker-launch-draft-line");
    const latestWorkerLaunchDraftSummary = document.getElementById("latest-worker-launch-draft-summary");
    const latestWorkerExecutionLine = document.getElementById("latest-worker-execution-line");
    const latestWorkerExecutionSummary = document.getElementById("latest-worker-execution-summary");
    const workerSessionForm = document.getElementById("worker-session-form");
    const workerSessionStatus = document.getElementById("worker-session-status");
    const workerSessionPanel = document.getElementById("worker-session-dock");
    const latestWorkerSessionLine = document.getElementById("latest-worker-session-line");
    const latestWorkerSessionTask = document.getElementById("latest-worker-session-task");
    const autoWorkerSessionButton = document.getElementById("auto-worker-session-button");
    const assignmentForm = document.getElementById("assignment-form");
    const assignmentStatus = document.getElementById("assignment-status");
    const latestAssignmentLine = document.getElementById("latest-assignment-line");
    const latestAssignmentBrief = document.getElementById("latest-assignment-brief");
    const teamBoardPanel = document.getElementById("team-board");
    const codexRunPanel = document.getElementById("codex-run-panel");
    const codexRunButton = document.getElementById("run-codex-assignment-button");
    const codexRunStatus = document.getElementById("codex-run-status");
    const latestCodexRunLine = document.getElementById("latest-codex-run-line");
    const latestCodexReturnSummary = document.getElementById("latest-codex-return-summary");
    const supervisorRouteForm = document.getElementById("supervisor-route-form");
    const supervisorRoutePanel = document.getElementById("supervisor-route-panel");
    const supervisorRouteStatus = document.getElementById("supervisor-route-status");
    const latestSupervisorRouteLine = document.getElementById("latest-supervisor-route-line");
    const internalReadRunButton = document.getElementById("run-internal-read-button");
    const internalReadRunPanel = document.getElementById("internal-read-run-panel");
    const internalReadRunStatus = document.getElementById("internal-read-run-status");
    const latestInternalReadRunLine = document.getElementById("latest-internal-read-run-line");
    const latestInternalReadLine = document.getElementById("latest-internal-read-line");
    const latestInternalReadSummary = document.getElementById("latest-internal-read-summary");
    const synthesisRunButton = document.getElementById("run-synthesis-button");
    const synthesisRunPanel = document.getElementById("synthesis-run-panel");
    const synthesisRunStatus = document.getElementById("synthesis-run-status");
    const latestSynthesisRunLine = document.getElementById("latest-synthesis-run-line");
    const latestSynthesisLine = document.getElementById("latest-synthesis-line");
    const latestSynthesisStatus = document.getElementById("latest-synthesis-status");
    const latestSynthesisRecommendation = document.getElementById("latest-synthesis-recommendation");
    const supervisorGateForm = document.getElementById("supervisor-gate-form");
    const supervisorGatePanel = document.getElementById("supervisor-gate-panel");
    const supervisorGateStatus = document.getElementById("supervisor-gate-status");
    const latestSupervisorGateLine = document.getElementById("latest-supervisor-gate-line");
    const implementationBriefButton = document.getElementById("create-implementation-brief-button");
    const implementationBriefPanel = document.getElementById("implementation-brief-panel");
    const implementationBriefStatus = document.getElementById("implementation-brief-status");
    const latestImplementationBriefLine = document.getElementById("latest-implementation-brief-line");
    const implementationLaunchGateForm = document.getElementById("implementation-launch-gate-form");
    const implementationLaunchGatePanel = document.getElementById("implementation-launch-gate-panel");
    const implementationLaunchGateStatus = document.getElementById("implementation-launch-gate-status");
    const latestImplementationLaunchGateLine = document.getElementById("latest-implementation-launch-gate-line");
    const cliSessionForm = document.getElementById("cli-session-form");
    const cliSessionStatus = document.getElementById("cli-session-status");
    const latestCliSessionLine = document.getElementById("latest-cli-session-line");
    const latestCliResultSummary = document.getElementById("latest-cli-result-summary");
    const latestCliSessionId = document.getElementById("latest-cli-session-id");
    const latestCliBackend = document.getElementById("latest-cli-backend");
    const latestCliTask = document.getElementById("latest-cli-task");
    const latestCliStatus = document.getElementById("latest-cli-status");
    const latestCliPurpose = document.getElementById("latest-cli-purpose");
    const latestCliMarks = document.getElementById("latest-cli-marks");
    const latestCliMarkHistory = document.getElementById("latest-cli-mark-history");
    const latestCliDepositPreview = document.getElementById("latest-cli-deposit-preview");
    const refreshCliReturnButton = document.getElementById("refresh-cli-return-button");
    const markCliRereadButton = document.getElementById("mark-cli-reread-button");
    const markCliImplementationButton = document.getElementById("mark-cli-implementation-button");
    const markCliValidationButton = document.getElementById("mark-cli-validation-button");
    const markCliDepositButton = document.getElementById("mark-cli-deposit-button");

    function updateLatestCliReadable(readable, structured) {{
      readable = readable || {{}};
      structured = structured || {{}};
      const sessionId = readable.session_id || "";
      if (latestCliSessionId) latestCliSessionId.textContent = sessionId || "none";
      if (latestCliBackend) latestCliBackend.textContent = readable.backend_kind || "none";
      if (latestCliTask) latestCliTask.textContent = readable.task_type || "none";
      if (latestCliStatus) latestCliStatus.textContent = readable.status || "none";
      if (latestCliPurpose) latestCliPurpose.textContent = readable.purpose_text || "no latest purpose";
      if (latestCliMarks) latestCliMarks.textContent = (readable.marks || []).join(", ") || "none";
      if (latestCliMarkHistory) {{
        latestCliMarkHistory.textContent = (readable.mark_history || []).slice(-4).map((item) => `${{item.mark}}@${{item.marked_at}}`).join(" / ") || "none";
      }}
      if (latestCliResultSummary) {{
        latestCliResultSummary.textContent = readable.structured_return_preview || structured.result_summary || "";
      }}
      if (latestCliDepositPreview) {{
        latestCliDepositPreview.textContent = readable.deposit_candidate_preview || "no deposit candidate preview yet";
      }}
      if (latestCliSessionLine) {{
        latestCliSessionLine.textContent = `${{readable.status || "none"}} / ${{readable.backend_kind || "none"}} / ${{readable.task_type || "none"}} / ${{sessionId || "none"}}`;
      }}
    }}

    async function refreshLatestCliReadable() {{
      cliSessionStatus.textContent = "refreshing latest return...";
      try {{
        const response = await fetch("/api/vectorfl-engine/state");
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to refresh state");
        }}
        const cli = result.cli_host_control || {{}};
        updateLatestCliReadable(cli.latest_readable_return || {{}}, cli.latest_structured_return || {{}});
        cliSessionStatus.textContent = "refreshed latest return";
      }} catch (error) {{
        cliSessionStatus.textContent = `error: ${{error.message}}`;
      }}
    }}

    cliSessionForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = cliSessionForm.querySelector("button[type='submit']");
      submitter.disabled = true;
      cliSessionStatus.textContent = "running CLI session...";
      try {{
        const formData = new FormData(cliSessionForm);
        const payload = Object.fromEntries(formData.entries());
        payload.requested_by_surface = "vectorfl_surface";
        payload.requested_by_page = "/vectorfl-engine/vectorfl";
        payload.dry_run = formData.has("dry_run");
        const response = await fetch("/api/vectorfl-engine/actions/cli-session/run", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || result.detail || "failed to run CLI session");
        }}
        const session = result.session || {{}};
        const structured = result.structured_return || {{}};
        updateLatestCliReadable({{
          session_id: session.session_id,
          backend_kind: session.backend_kind,
          task_type: session.task_type,
          status: session.status,
          purpose_text: session.purpose_text,
          marks: session.marks || [],
          mark_history: session.mark_history || [],
          structured_return_preview: structured.result_summary || session.result_summary || "",
          deposit_candidate_preview: result.deposit_candidate_preview || "",
        }}, structured);
        cliSessionStatus.textContent = `${{result.ok ? "done" : "failed"}} -> ${{result.session_path}}`;
      }} catch (error) {{
        cliSessionStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
      }}
    }});

    async function markLatestCliSession(mark) {{
      const sessionId = latestCliSessionId?.textContent?.trim();
      if (!sessionId || sessionId === "none") {{
        cliSessionStatus.textContent = "no latest CLI session to mark";
        return;
      }}
      cliSessionStatus.textContent = `marking ${{mark}}...`;
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/cli-session/mark", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{ session_id: sessionId, mark }}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || result.detail || "failed to mark CLI session");
        }}
        updateLatestCliReadable({{
          session_id: result.session?.session_id,
          backend_kind: result.session?.backend_kind,
          task_type: result.session?.task_type,
          status: result.session?.status,
          purpose_text: result.session?.purpose_text,
          marks: result.session?.marks || [],
          mark_history: result.session?.mark_history || [],
          structured_return_preview: result.session?.result_summary || "",
          deposit_candidate_preview: latestCliDepositPreview?.textContent || "",
        }}, {{}});
        cliSessionStatus.textContent = `marked ${{mark}} -> runtime/cli_sessions/${{sessionId}}/session.json`;
      }} catch (error) {{
        cliSessionStatus.textContent = `error: ${{error.message}}`;
      }}
    }}

    refreshCliReturnButton?.addEventListener("click", refreshLatestCliReadable);
    markCliRereadButton?.addEventListener("click", () => markLatestCliSession("reread_target"));
    markCliImplementationButton?.addEventListener("click", () => markLatestCliSession("implementation_return"));
    markCliValidationButton?.addEventListener("click", () => markLatestCliSession("validation_target"));
    markCliDepositButton?.addEventListener("click", () => markLatestCliSession("deposit_candidate"));

    createWorkerLaunchDraftButton?.addEventListener("click", async () => {{
      createWorkerLaunchDraftButton.disabled = true;
      operatingDialoguePanel.classList.add("thinking");
      workerLaunchDraftStatus.textContent = "saving current directive...";
      try {{
        const formData = operatingDialogueForm ? new FormData(operatingDialogueForm) : new FormData();
        const payload = Object.fromEntries(formData.entries());
        payload.operator_message = payload.purpose || payload.operator_message || "";
        payload.should_update_worker_session = formData.has("should_update_worker_session");
        const dialogueResponse = await fetch("/api/vectorfl-engine/actions/operating-dialogue", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const dialogueResult = await dialogueResponse.json();
        if (!dialogueResponse.ok) {{
          throw new Error(dialogueResult.error || "failed to save current directive before draft");
        }}
        const dialogue = dialogueResult.operating_dialogue || {{}};
        if (latestOperatingDialogueLine) {{
          latestOperatingDialogueLine.textContent = `${{dialogue.status}} / ${{dialogue.selected_worker}} / ${{dialogue.selected_model}} / ${{dialogue.created_at}}`;
        }}
        if (conversationUserMessage) {{
          conversationUserMessage.textContent = dialogue.purpose || dialogue.operator_message || "";
        }}
        if (conversationWorkerLabel) {{
          conversationWorkerLabel.textContent = dialogue.selected_worker_label || dialogue.selected_worker || "Worker";
        }}
        workerLaunchDraftStatus.textContent = "drafting launch boundary...";
        const response = await fetch("/api/vectorfl-engine/actions/worker-launch-draft", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{
            selected_worker: payload.selected_worker,
            selected_model: payload.selected_model,
            operator_message: payload.operator_message,
          }}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to create worker launch draft");
        }}
        const draft = result.worker_launch_draft || {{}};
        if (latestWorkerLaunchDraftLine) {{
          latestWorkerLaunchDraftLine.textContent = `${{draft.status}} / ${{draft.selected_worker}} / ${{draft.command_family}} / ${{draft.created_at}}`;
        }}
        if (latestWorkerLaunchDraftSummary) {{
          latestWorkerLaunchDraftSummary.textContent = draft.command_preview || "";
        }}
        workerLaunchDraftStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `drafted -> ${{result.path}}`;
      }} catch (error) {{
        workerLaunchDraftStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        createWorkerLaunchDraftButton.disabled = false;
        operatingDialoguePanel.classList.remove("thinking");
      }}
    }});

    runWorkerLaunchDraftButton?.addEventListener("click", async () => {{
      if (!window.confirm("Run the latest worker launch draft as an actual CLI call? This uses the draft guard and read-only default.")) {{
        workerLaunchDraftStatus.textContent = "cancelled";
        return;
      }}
      runWorkerLaunchDraftButton.disabled = true;
      operatingDialoguePanel.classList.add("thinking");
      workerLaunchDraftStatus.textContent = "running worker CLI...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/run-worker-launch-draft", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{}}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to run worker launch draft");
        }}
        const execution = result.worker_execution || {{}};
        if (latestWorkerExecutionLine) {{
          latestWorkerExecutionLine.textContent = `${{execution.status}} / ${{execution.worker}} / exit=${{execution.exit_code}} / ${{execution.finished_at}}`;
        }}
        if (latestWorkerExecutionSummary) {{
          latestWorkerExecutionSummary.textContent = execution.output_summary || execution.stderr_tail || "";
        }}
        if (conversationWorkerLabel) {{
          conversationWorkerLabel.textContent = execution.worker_label || execution.worker || "Worker";
        }}
        if (conversationWorkerMessage) {{
          conversationWorkerMessage.textContent = execution.stdout_tail || execution.output_summary || execution.stderr_tail || "";
        }}
        workerLaunchDraftStatus.textContent = `${{result.ok ? "completed" : "failed"}} -> ${{result.path}}`;
      }} catch (error) {{
        workerLaunchDraftStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        runWorkerLaunchDraftButton.disabled = false;
        operatingDialoguePanel.classList.remove("thinking");
      }}
    }});

    operatingDialogueForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = operatingDialogueForm.querySelector("button[type='submit']");
      const formData = new FormData(operatingDialogueForm);
      const payload = Object.fromEntries(formData.entries());
      payload.operator_message = payload.purpose || payload.operator_message || "";
      payload.should_update_worker_session = formData.has("should_update_worker_session");
      submitter.disabled = true;
      operatingDialoguePanel.classList.add("thinking");
      operatingDialogueStatus.textContent = "recording dialogue...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/operating-dialogue", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to record operating dialogue");
        }}
        const dialogue = result.operating_dialogue || {{}};
        if (latestOperatingDialogueLine) {{
          latestOperatingDialogueLine.textContent = `${{dialogue.status}} / ${{dialogue.selected_worker}} / ${{dialogue.selected_model}} / ${{dialogue.created_at}}`;
        }}
        if (latestOperatingDialogueSummary) {{
          latestOperatingDialogueSummary.textContent = dialogue.operator_message || "";
        }}
        if (conversationUserMessage) {{
          conversationUserMessage.textContent = dialogue.purpose || dialogue.operator_message || "";
        }}
        if (conversationWorkerLabel) {{
          conversationWorkerLabel.textContent = dialogue.selected_worker_label || dialogue.selected_worker || "Worker";
        }}
        if (conversationWorkerMessage) {{
          conversationWorkerMessage.textContent = "메시지는 저장됐습니다. 호출 초안을 만들고 실행하면 worker 응답이 이곳에 표시됩니다.";
        }}
        const session = ((result.worker_session_result || {{}}).worker_session || {{}});
        if (session.status) {{
          if (operateWorkerSessionLine) {{
            operateWorkerSessionLine.textContent = `${{session.status}} / ${{session.secondary_worker}} / ${{session.secondary_model}} / ${{session.updated_at}}`;
          }}
          if (operateWorkerSessionTask) {{
            operateWorkerSessionTask.textContent = session.active_task || "";
          }}
          if (latestWorkerSessionLine) {{
            latestWorkerSessionLine.textContent = `${{session.status}} / ${{session.secondary_worker}} / ${{session.secondary_model}} / ${{session.updated_at}}`;
          }}
          if (latestWorkerSessionTask) {{
            latestWorkerSessionTask.textContent = session.active_task || "";
          }}
        }}
        operatingDialogueStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `saved -> ${{result.path}}`;
      }} catch (error) {{
        operatingDialogueStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        operatingDialoguePanel.classList.remove("thinking");
      }}
    }});

    quickOperatingForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = quickOperatingForm.querySelector("button[type='submit']");
      const formData = new FormData(quickOperatingForm);
      const payload = Object.fromEntries(formData.entries());
      const directive = (payload.directive || "").trim();
      const memo = (payload.memo || "").trim();
      const title = directive.split("\\n")[0] || "VectorFL operating packet";
      submitter.disabled = true;
      quickOperatingPanel.classList.add("thinking");
      quickOperatingStatus.textContent = "saving packet...";
      try {{
        const packetResponse = await fetch("/api/vectorfl-engine/actions/work-packet", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{
            topic: title,
            directive,
            memo,
            selected_stage: "line_generation",
            target_cell: payload.assignee_cell,
            requested_action: directive,
            expected_output: payload.expected_output,
            forbidden_scope: payload.forbidden_scope,
            reference_md_files: payload.reference_md_files,
            supervisor_note: "created from top operating dock",
          }}),
        }});
        const packetResult = await packetResponse.json();
        if (!packetResponse.ok) {{
          throw new Error(packetResult.error || "failed to save work packet");
        }}
        quickOperatingStatus.textContent = "saving assignment...";
        const assignmentResponse = await fetch("/api/vectorfl-engine/actions/assignment", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{
            team_id: payload.team_id,
            assignee_cell: payload.assignee_cell,
            title,
            brief: [directive, memo].filter(Boolean).join("\\n\\n"),
            expected_report: payload.expected_output,
            review_focus: payload.reference_md_files,
            forbidden_scope: payload.forbidden_scope,
            reference_md_files: payload.reference_md_files,
          }}),
        }});
        const assignmentResult = await assignmentResponse.json();
        if (!assignmentResponse.ok) {{
          throw new Error(assignmentResult.error || "failed to save assignment");
        }}
        const packet = packetResult.work_packet || {{}};
        const assignment = assignmentResult.assignment || {{}};
        if (latestPacketLine) {{
          latestPacketLine.textContent = `${{packet.status}} / ${{packet.target_cell}} / ${{packet.created_at}}`;
        }}
        if (latestAssignmentLine) {{
          latestAssignmentLine.textContent = `${{assignment.status}} / ${{assignment.team_id}} / ${{assignment.assignee_cell}} / ${{assignment.created_at}}`;
        }}
        if (latestAssignmentBrief) {{
          latestAssignmentBrief.textContent = assignment.brief || assignment.title || "";
        }}
        quickOperatingStatus.textContent = assignmentResult.created === false
          ? `unchanged -> ${{assignmentResult.path}}`
          : `saved -> ${{assignmentResult.path}}`;
      }} catch (error) {{
        quickOperatingStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        quickOperatingPanel.classList.remove("thinking");
      }}
    }});

    workerSessionForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = workerSessionForm.querySelector("button[type='submit']");
      const formData = new FormData(workerSessionForm);
      const payload = Object.fromEntries(formData.entries());
      submitter.disabled = true;
      workerSessionPanel.classList.add("thinking");
      workerSessionStatus.textContent = "saving worker session...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/worker-session", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to save worker session");
        }}
        const session = result.worker_session || {{}};
        latestWorkerSessionLine.textContent = `${{session.status}} / ${{session.secondary_worker}} / ${{session.secondary_model}} / ${{session.updated_at}}`;
        latestWorkerSessionTask.textContent = session.active_task || "";
        workerSessionStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `saved -> ${{result.path}}`;
      }} catch (error) {{
        workerSessionStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        workerSessionPanel.classList.remove("thinking");
      }}
    }});

    autoWorkerSessionButton?.addEventListener("click", async () => {{
      autoWorkerSessionButton.disabled = true;
      workerSessionPanel.classList.add("thinking");
      workerSessionStatus.textContent = "auto-configuring from current context...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/worker-session/from-current-context", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{}}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to auto-configure worker session");
        }}
        const session = result.worker_session || {{}};
        latestWorkerSessionLine.textContent = `${{session.status}} / ${{session.secondary_worker}} / ${{session.secondary_model}} / ${{session.updated_at}}`;
        latestWorkerSessionTask.textContent = session.active_task || "";
        if (workerSessionForm) {{
          workerSessionForm.elements.primary_worker.value = session.primary_worker || "codex";
          workerSessionForm.elements.codex_model.value = session.primary_model || "current codex session";
          workerSessionForm.elements.secondary_worker.value = session.secondary_worker || "gemini";
          workerSessionForm.elements.gemini_model.value = session.secondary_model || "gemini-cli default";
          workerSessionForm.elements.gemini_role.value = session.gemini_role || "";
          workerSessionForm.elements.active_task.value = session.active_task || "";
          workerSessionForm.elements.line_script_candidates.value = (session.line_script_candidates || []).join("\\n");
          workerSessionForm.elements.translation_material_targets.value = (session.translation_material_targets || []).join("\\n");
          workerSessionForm.elements.operator_visibility.value = (session.operator_visibility || []).join("\\n");
          workerSessionForm.elements.forbidden_scope.value = (session.forbidden_scope || []).join("\\n");
        }}
        workerSessionStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `auto-saved -> ${{result.path}}`;
      }} catch (error) {{
        workerSessionStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        autoWorkerSessionButton.disabled = false;
        workerSessionPanel.classList.remove("thinking");
      }}
    }});

    workPacketForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = workPacketForm.querySelector("button[type='submit']");
      const formData = new FormData(workPacketForm);
      const payload = Object.fromEntries(formData.entries());
      submitter.disabled = true;
      workPacketPanel.classList.add("thinking");
      workPacketStatus.textContent = "saving...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/work-packet", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to save work packet");
        }}
        const packet = result.work_packet || {{}};
        latestPacketLine.textContent = `${{packet.status}} / ${{packet.target_cell}} / ${{packet.created_at}}`;
        workPacketStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `saved -> ${{result.path}}`;
      }} catch (error) {{
        workPacketStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        workPacketPanel.classList.remove("thinking");
      }}
    }});

    assignmentForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = assignmentForm.querySelector("button[type='submit']");
      const formData = new FormData(assignmentForm);
      const payload = Object.fromEntries(formData.entries());
      submitter.disabled = true;
      teamBoardPanel.classList.add("thinking");
      assignmentStatus.textContent = "saving...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/assignment", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to save assignment");
        }}
        const assignment = result.assignment || {{}};
        latestAssignmentLine.textContent = `${{assignment.status}} / ${{assignment.team_id}} / ${{assignment.assignee_cell}} / ${{assignment.created_at}}`;
        latestAssignmentBrief.textContent = assignment.brief || assignment.title || "";
        assignmentStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `saved -> ${{result.path}}`;
      }} catch (error) {{
        assignmentStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        teamBoardPanel.classList.remove("thinking");
      }}
    }});

    codexRunButton?.addEventListener("click", async () => {{
      if (!window.confirm("Run read-only Codex report and overwrite the latest Codex return/run artifact?")) {{
        codexRunStatus.textContent = "cancelled";
        return;
      }}
      codexRunButton.disabled = true;
      codexRunPanel.classList.add("thinking");
      codexRunStatus.textContent = "running codex bridge...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/run-codex-assignment", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{}}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || (result.run && result.run.stderr_tail) || "codex bridge failed");
        }}
        const run = result.run || {{}};
        latestCodexRunLine.textContent = `report_return=${{run.status}} / exit=${{run.exit_code}} / ${{run.finished_at}}`;
        latestCodexReturnSummary.textContent = run.return_summary || "";
        codexRunStatus.textContent = `${{result.ok ? "completed" : "failed"}} -> ${{result.path}}`;
      }} catch (error) {{
        codexRunStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        codexRunButton.disabled = false;
        codexRunPanel.classList.remove("thinking");
      }}
    }});

    supervisorRouteForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = supervisorRouteForm.querySelector("button[type='submit']");
      const formData = new FormData(supervisorRouteForm);
      const payload = Object.fromEntries(formData.entries());
      submitter.disabled = true;
      supervisorRoutePanel.classList.add("thinking");
      supervisorRouteStatus.textContent = "saving...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/supervisor-route", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to save supervisor route");
        }}
        const route = result.route || {{}};
        latestSupervisorRouteLine.textContent = `${{route.decision}} / ${{route.target_team}} / ${{route.decided_at}}`;
        supervisorRouteStatus.textContent = `saved -> ${{result.path}}`;
      }} catch (error) {{
        supervisorRouteStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        supervisorRoutePanel.classList.remove("thinking");
      }}
    }});

    internalReadRunButton?.addEventListener("click", async () => {{
      if (!window.confirm("Run read-only internal read and overwrite the latest internal-read report?")) {{
        internalReadRunStatus.textContent = "cancelled";
        return;
      }}
      internalReadRunButton.disabled = true;
      internalReadRunPanel.classList.add("thinking");
      internalReadRunStatus.textContent = "running internal read...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/run-internal-read", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{}}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "internal read failed");
        }}
        const run = result.run || {{}};
        const report = result.report || {{}};
        latestInternalReadRunLine.textContent = `report_return=${{run.status}} / exit=${{run.exit_code}} / ${{run.finished_at}}`;
        latestInternalReadLine.textContent = `report_return=${{report.status}} / ${{report.worker}} / ${{report.returned_at}}`;
        latestInternalReadSummary.textContent = report.summary || "";
        internalReadRunStatus.textContent = `${{result.ok ? "completed" : "failed"}} -> ${{result.report_path}}`;
      }} catch (error) {{
        internalReadRunStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        internalReadRunButton.disabled = false;
        internalReadRunPanel.classList.remove("thinking");
      }}
    }});

    synthesisRunButton?.addEventListener("click", async () => {{
      if (!window.confirm("Run read-only synthesis and overwrite the latest synthesis report?")) {{
        synthesisRunStatus.textContent = "cancelled";
        return;
      }}
      synthesisRunButton.disabled = true;
      synthesisRunPanel.classList.add("thinking");
      synthesisRunStatus.textContent = "running synthesis...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/run-synthesis", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{}}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "synthesis failed");
        }}
        const run = result.run || {{}};
        const report = result.report || {{}};
        latestSynthesisRunLine.textContent = `report_return=${{run.status}} / exit=${{run.exit_code}} / ${{run.finished_at}}`;
        latestSynthesisLine.textContent = `report_return=${{report.status}} / ${{report.worker}} / ${{report.returned_at}}`;
        latestSynthesisStatus.textContent = report.current_status || "";
        latestSynthesisRecommendation.textContent = `${{report.recommendation || "pending"}} / ${{report.recommendation_reason || ""}}`;
        synthesisRunStatus.textContent = `${{result.ok ? "completed" : "failed"}} -> ${{result.report_path}}`;
      }} catch (error) {{
        synthesisRunStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        synthesisRunButton.disabled = false;
        synthesisRunPanel.classList.remove("thinking");
      }}
    }});

    supervisorGateForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = supervisorGateForm.querySelector("button[type='submit']");
      const formData = new FormData(supervisorGateForm);
      const payload = Object.fromEntries(formData.entries());
      submitter.disabled = true;
      supervisorGatePanel.classList.add("thinking");
      supervisorGateStatus.textContent = "saving gate...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/supervisor-gate", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to save supervisor gate");
        }}
        const gate = result.gate || {{}};
        latestSupervisorGateLine.textContent = `${{gate.decision}} / ${{gate.target_team}} / ${{gate.decided_at}}`;
        supervisorGateStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `saved -> ${{result.path}}`;
      }} catch (error) {{
        supervisorGateStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        supervisorGatePanel.classList.remove("thinking");
      }}
    }});

    implementationBriefButton?.addEventListener("click", async () => {{
      if (!window.confirm("Create an implementation brief from the latest approved supervisor gate? This will not run implementation.")) {{
        implementationBriefStatus.textContent = "cancelled";
        return;
      }}
      implementationBriefButton.disabled = true;
      implementationBriefPanel.classList.add("thinking");
      implementationBriefStatus.textContent = "creating brief...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/implementation-brief", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{}}),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to create implementation brief");
        }}
        const brief = result.brief || {{}};
        latestImplementationBriefLine.textContent = `${{brief.status}} / ${{brief.target_worker}} / ${{brief.created_at}}`;
        implementationBriefStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `created -> ${{result.path}}`;
      }} catch (error) {{
        implementationBriefStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        implementationBriefButton.disabled = false;
        implementationBriefPanel.classList.remove("thinking");
      }}
    }});

    implementationLaunchGateForm?.addEventListener("submit", async (event) => {{
      event.preventDefault();
      const submitter = implementationLaunchGateForm.querySelector("button[type='submit']");
      const formData = new FormData(implementationLaunchGateForm);
      const payload = Object.fromEntries(formData.entries());
      submitter.disabled = true;
      implementationLaunchGatePanel.classList.add("thinking");
      implementationLaunchGateStatus.textContent = "saving launch gate...";
      try {{
        const response = await fetch("/api/vectorfl-engine/actions/implementation-launch-gate", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload),
        }});
        const result = await response.json();
        if (!response.ok) {{
          throw new Error(result.error || "failed to save implementation launch gate");
        }}
        const gate = result.gate || {{}};
        latestImplementationLaunchGateLine.textContent = `${{gate.decision}} / ${{gate.target_worker}} / ${{gate.decided_at}}`;
        implementationLaunchGateStatus.textContent = result.created === false ? `unchanged -> ${{result.path}}` : `saved -> ${{result.path}}`;
      }} catch (error) {{
        implementationLaunchGateStatus.textContent = `error: ${{error.message}}`;
      }} finally {{
        submitter.disabled = false;
        implementationLaunchGatePanel.classList.remove("thinking");
      }}
    }});
  </script>
</body>
</html>"""
