from __future__ import annotations

from typing import Any, Dict
import html
import json


def _esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""))


def _chip(value: Any) -> str:
    return f'<span class="chip">{_esc(value)}</span>'


def _chips(values: Any) -> str:
    if not isinstance(values, list) or not values:
        return _chip("none")
    return "".join(_chip(item) for item in values)


def _textarea(label: str, value: Any, *, rows: int = 4) -> str:
    return f"""
    <label class="field wide">
      <span>{_esc(label)}</span>
      <textarea rows="{rows}" readonly>{_esc(value)}</textarea>
    </label>
    """


def _input(label: str, value: Any) -> str:
    return f"""
    <label class="field">
      <span>{_esc(label)}</span>
      <input value="{_esc(value)}" readonly>
    </label>
    """


def render_vectorfl_paper_operable_shell(state: Dict[str, Any]) -> str:
    current = state.get("current_ssot") or {}
    dry_run = state.get("dry_run_preview") or {}
    comparison = state.get("comparison_summary") or {}
    handoff = state.get("worker_handoff") or {}
    codex_return = state.get("codex_return") or {}
    gemini = state.get("gemini_review") or {}
    decision = state.get("supervisor_decision") or {}
    gate = state.get("gate_validation") or {}
    guard = state.get("guard") or {}
    data = json.dumps(state, ensure_ascii=False)
    codex_top_files_text = "\n".join(handoff.get("codex_top_files") or [])

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Paper / Engine Status Console</title>
  <style>
    :root {{
      --bg: #0a0b0d;
      --panel: #15171b;
      --panel-2: #101216;
      --line: #2c3038;
      --ink: #f3f1e8;
      --muted: #a9aaad;
      --accent: #d6b15f;
      --accent-2: #6db38b;
      --danger: #d66f5f;
      --chip: #20242b;
      --field: #0d0f13;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        linear-gradient(120deg, rgba(214,177,95,.10), transparent 32%),
        radial-gradient(circle at 85% 0%, rgba(109,179,139,.12), transparent 28%),
        var(--bg);
      font-family: "Aptos", "IBM Plex Sans KR", "Noto Sans KR", ui-sans-serif, system-ui, sans-serif;
    }}
    .page {{ max-width: 1520px; margin: 0 auto; padding: 18px; display: grid; gap: 14px; }}
    .hero, .panel {{ border: 1px solid var(--line); background: rgba(21,23,27,.94); border-radius: 14px; }}
    .hero {{ padding: 16px; display: grid; gap: 12px; }}
    .layout {{ display: grid; grid-template-columns: 280px minmax(0, 1fr); gap: 14px; align-items: start; }}
    .rail, .stack {{ display: grid; gap: 10px; }}
    .panel {{ padding: 14px; display: grid; gap: 12px; }}
    .kicker {{ color: var(--accent); font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: .12em; }}
    .muted {{ color: var(--muted); font-size: 13px; line-height: 1.55; }}
    h1, h2, h3 {{ margin: 0; }}
    h1 {{ font-size: clamp(24px, 4vw, 44px); letter-spacing: -.04em; line-height: .98; }}
    h2 {{ font-size: 18px; letter-spacing: -.02em; }}
    h3 {{ font-size: 14px; }}
    .head {{ display: flex; justify-content: space-between; gap: 12px; align-items: end; }}
    .flow {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 8px; }}
    .step {{ border: 1px solid var(--line); border-radius: 12px; background: var(--panel-2); padding: 10px; min-height: 92px; display: grid; gap: 7px; }}
    .step strong {{ font-size: 13px; }}
    .step .num {{ color: var(--accent); font: 700 11px ui-monospace, SFMono-Regular, Menlo, monospace; }}
    .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }}
    .card {{ border: 1px solid var(--line); border-radius: 12px; background: var(--panel-2); padding: 12px; display: grid; gap: 8px; }}
    .chip-row {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .chip {{ display: inline-flex; border: 1px solid var(--line); background: var(--chip); color: var(--ink); border-radius: 999px; padding: 4px 8px; font-size: 11px; }}
    .chip.warn {{ border-color: var(--danger); color: #ffd3cd; }}
    .mono {{ font: 12px/1.55 "IBM Plex Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; color: var(--muted); word-break: break-all; }}
    .body {{ font-size: 13px; line-height: 1.65; white-space: pre-wrap; }}
    .form {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
    .field {{ display: grid; gap: 6px; }}
    .field.wide {{ grid-column: 1 / -1; }}
    .field span {{ color: var(--muted); font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; }}
    input, textarea {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: var(--field);
      color: var(--ink);
      padding: 9px 10px;
      font: 12px/1.55 "IBM Plex Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    }}
    textarea {{ resize: vertical; }}
    .action {{
      border: 1px dashed var(--line);
      border-radius: 12px;
      background: rgba(214,177,95,.06);
      padding: 10px;
      display: grid;
      gap: 6px;
    }}
    .guard {{ border-color: var(--danger); background: rgba(214,111,95,.10); }}
    @media (max-width: 980px) {{
      .layout, .grid-2, .grid-3, .flow, .form {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <script type="application/json" id="vectorfl-paper-operable-state">{html.escape(data)}</script>
  <div class="page">
    <section class="hero">
      <div class="kicker">VectorFL Paper / engine status console</div>
      <div class="head">
        <div>
          <h1>이건 최종 통합 운용 페이지가 아니다.</h1>
          <div class="muted">이 페이지는 Paper proper / operable surface 결과물을 읽는 server-backed substrate console입니다. 최종 통합 운용 페이지는 Paperclip식 work board, work detail, inspector, organ detail, audit/governance 층위로 별도 상위 layer에 놓아야 합니다.</div>
        </div>
        <div class="chip-row">
          {_chip("posture=" + str(decision.get("decision") or "unknown"))}
          {_chip("ssot=" + str(current.get("state") or "unknown"))}
          {_chip("gate=" + str(gate.get("gate_effect") or "unknown"))}
        </div>
      </div>
      <div class="flow">
        <div class="step"><div class="num">01</div><strong>Input</strong><div class="muted">actual export 후보와 current SSOT 분리</div></div>
        <div class="step"><div class="num">02</div><strong>Select</strong><div class="muted">Codex handoff 입력 재료 고정</div></div>
        <div class="step"><div class="num">03</div><strong>Assign</strong><div class="muted">Codex/Gemini 역할과 top files 분리</div></div>
        <div class="step"><div class="num">04</div><strong>Confirm</strong><div class="muted">worker return과 cross-check 확인</div></div>
        <div class="step"><div class="num">05</div><strong>Supervise</strong><div class="muted">hold/reopen/continue gate 판단</div></div>
        <div class="step"><div class="num">06</div><strong>Return</strong><div class="muted">trace/inbox/memory로 귀속</div></div>
      </div>
    </section>

    <div class="layout">
      <aside class="rail">
        <section class="panel">
          <div class="kicker">Current SSOT</div>
          <h2>{_esc(current.get("state") or "unknown")}</h2>
          <div class="mono">{_esc(current.get("path") or "")}</div>
          <div class="chip-row">{_chip(current.get("honesty") or "unknown")}</div>
          <div class="body">{_esc(current.get("note") or "")}</div>
        </section>
        <section class="panel guard">
          <div class="kicker">Guard</div>
          <div class="chip-row">
            {_chip("gate_close=" + str(guard.get("gate_close") or "unknown"))}
            {_chip("slot_replacement=" + str(guard.get("slot_replacement") or "unknown"))}
            {_chip("candidate_promotion=" + str(guard.get("candidate_promotion") or "unknown"))}
            {_chip("fake_controls=" + str(guard.get("fake_controls") or "unknown"))}
          </div>
        </section>
        <section class="panel">
          <div class="kicker">API</div>
          <div class="mono">GET /api/vectorfl-paper/state</div>
          <div class="muted">다음 JSX shell의 첫 소비 지점입니다.</div>
        </section>
      </aside>

      <main class="stack">
        <section class="panel">
          <div class="kicker">Layer Correction</div>
          <h2>상위 operating layer는 Paperclip식 제품 구조로 다시 올라간다</h2>
          <div class="body">현재 shell은 내부 상태를 한 곳에 모으는 console입니다. 실제 통합 운용 페이지는 work intake, case/work board, work detail, right inspector, organ detail, audit/governance를 가지는 상위 제품 layer여야 합니다.</div>
          <div class="chip-row">{_chip("current_route=substrate_console")}{_chip("top_layer=paperclip_like_control_plane")}{_chip("do_not_expand_this_as_final_page")}</div>
        </section>

        <section class="panel">
          <div class="head"><div><div class="kicker">Operating Board</div><h2>current vs preview vs comparison</h2></div><div class="mono">top-down posture</div></div>
          <div class="grid-3">
            <div class="card"><div class="kicker">current SSOT</div><h3>{_esc(current.get("anchor") or "unknown")}</h3><div class="chip-row">{_chip(current.get("state") or "unknown")}</div></div>
            <div class="card"><div class="kicker">dry-run preview</div><h3>{_esc(dry_run.get("source_record") or "unknown")}</h3><div class="chip-row">{_chip(dry_run.get("honesty_class") or "unknown")}{_chip(dry_run.get("gate_effect") or "unknown")}</div></div>
            <div class="card"><div class="kicker">comparison</div><h3>reference candidate summary</h3><div class="chip-row">{_chip("repeatable=" + str(comparison.get("candidate_for_reopen_validation_repeatable")))}{_chip("gate_close=" + str(comparison.get("any_candidate_close_to_gate_close")))}</div></div>
          </div>
        </section>

        <section class="panel">
          <div class="head"><div><div class="kicker">Input / Select</div><h2>worker에게 넘길 재료를 먼저 고정한다</h2></div><div class="mono">handoff seam</div></div>
          <div class="form">
            {_input("handoff path", handoff.get("path") or "")}
            {_input("handoff status", handoff.get("status") or "")}
            {_textarea("requested action", handoff.get("requested_action") or "", rows=3)}
            {_textarea("codex top files", codex_top_files_text, rows=5)}
          </div>
        </section>

        <section class="panel">
          <div class="head"><div><div class="kicker">Assign / Confirm</div><h2>Codex 결과와 Gemini 검토를 같은 루프에서 본다</h2></div><div class="mono">worker return + review</div></div>
          <div class="grid-2">
            <div class="card">
              <div class="kicker">Codex return</div>
              <div class="chip-row">{_chip("status=" + str(codex_return.get("status") or "unknown"))}{_chip("changed=" + str(codex_return.get("changed_files_count") or 0))}{_chip("blockers=" + str(codex_return.get("blockers_count") or 0))}</div>
              <div class="body">{_esc(codex_return.get("summary") or "")}</div>
            </div>
            <div class="card">
              <div class="kicker">Gemini review</div>
              <div class="chip-row">{_chip("status=" + str(gemini.get("review_status") or "unknown"))}{_chip("agreement=" + str(gemini.get("agreement_assessment") or "unknown"))}{_chip("action=" + str(gemini.get("suggested_supervisor_action") or "unknown"))}</div>
              <div class="body">{_esc(gemini.get("recommendation") or "")}</div>
              <div class="kicker">Gemini top files</div>
              <div class="chip-row">{_chips(gemini.get("gemini_review_top_files") or [])}</div>
            </div>
          </div>
        </section>

        <section class="panel">
          <div class="head"><div><div class="kicker">Supervise</div><h2>지금 continue가 아니라 hold/reopen gate를 읽는다</h2></div><div class="mono">{_esc(decision.get("path") or "")}</div></div>
          <div class="grid-2">
            <div class="card">
              <div class="kicker">decision</div>
              <h2>{_esc(decision.get("decision") or "unknown")}</h2>
              <div class="body">{_esc(decision.get("rationale") or "")}</div>
              <div class="chip-row">{_chip("tension=" + str(decision.get("decision_tension") or "unknown"))}</div>
            </div>
            <div class="card">
              <div class="kicker">pending validations</div>
              <div class="chip-row">{_chips(decision.get("pending_validations") or [])}</div>
              <div class="kicker">continue gate</div>
              <div class="body">{_esc(decision.get("continue_gate") or "")}</div>
            </div>
          </div>
        </section>

        <section class="panel">
          <div class="head"><div><div class="kicker">Next Action Boundary</div><h2>다음부터는 POST를 하나씩 붙인다</h2></div><div class="mono">no fake control</div></div>
          <div class="grid-3">
            <div class="action"><strong>select candidate</strong><div class="mono">POST /api/vectorfl-paper/actions/select-candidate</div><div class="muted">아직 미구현. current slot 교체 금지.</div></div>
            <div class="action"><strong>emit handoff</strong><div class="mono">POST /api/vectorfl-paper/actions/emit-handoff</div><div class="muted">아직 미구현. latest handoff만 명시적으로 갱신.</div></div>
            <div class="action"><strong>run bridges</strong><div class="mono">POST /api/vectorfl-paper/actions/run-codex-bridge / run-gemini-review</div><div class="muted">아직 미구현. 실제 CLI 연결 전 fake 실행 금지.</div></div>
          </div>
        </section>
      </main>
    </div>
  </div>
</body>
</html>"""
