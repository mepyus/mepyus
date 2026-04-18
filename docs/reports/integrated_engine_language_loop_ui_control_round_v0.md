# Integrated Engine Language Loop UI Control Round v0

Date: 2026-04-16

## 0. verdict

PASS_WITH_NOTE

통합엔진 위에서 내부 언어 수집 루프를 실행하고 수확할 수 있는 최소 VectorFL control path를 추가했다.

이 라운드는 terminal-only 루프를 넘어서, 사용자가 VectorFL면에서 loop를 실행하고 harvest 결과를 확인할 수 있게 하는 셋업이다.

Note: 실행은 아직 synchronous 방식이다. 10회 루프 동안 버튼 호출은 완료될 때까지 기다린다. background runner / progress streaming은 아직 열지 않았다.

## 1. user intent reread

사용자의 목표는 단순히 루프 스크립트를 만드는 것이 아니었다.

진짜 목표는:

```text
통합엔진 위에서
-> 내부 데이터와 방향을 보고
-> 나에게 지시하고
-> 내가 Codex/CLI를 운영하고
-> 그 결과가 다시 통합엔진 화면과 runtime artifact로 돌아오는 상태
```

이다.

따라서 이번 라운드는 terminal script 사용법 설명에서 멈추지 않고, VectorFL면에 loop control을 붙였다.

## 2. files changed

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/core/runtime/viewer_server.py`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `scripts/harvest_integrated_engine_language_loop.py`
- `docs/reports/integrated_engine_language_loop_ui_control_round_v0.md`

Related existing loop runner:

- `scripts/run_integrated_engine_language_loop.py`

## 3. API additions

### 3.1 state

`build_vectorfl_integrated_engine_state` now includes:

```text
language_loop_control
```

It exposes:

- latest loop
- recent loops
- loop index preview
- harvest preview
- loop artifact paths
- boundary guard

### 3.2 actions

Added endpoints:

```text
POST /api/vectorfl-engine/actions/language-loop/run
POST /api/vectorfl-engine/actions/language-loop/harvest
```

These call the existing loop and harvest scripts through the integrated-engine API server path.

## 4. VectorFL UI additions

Added `Internal Language Loop` panel inside the VectorFL surface.

The panel can:

- choose loop count: `1`, `10`, `20`
- run the loop
- harvest latest loop
- refresh state
- show latest loop id / status / progress
- show loop index preview
- show harvest preview

This panel is explicitly marked as:

```text
translation data only
not UI copy
not final glossary
not deposit ingestion
not automatic promotion
```

## 5. validation

### 5.1 static checks

Passed:

```bash
python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py scripts/run_integrated_engine_language_loop.py scripts/harvest_integrated_engine_language_loop.py
npm run build
```

### 5.2 server refresh

Viewer server restarted.

State endpoint confirmed:

- `language_loop_control.schema_version = integrated_engine_language_loop_control_state_v0`
- latest loop visible
- harvest path visible

### 5.3 harvest endpoint

Endpoint passed:

```text
POST /api/vectorfl-engine/actions/language-loop/harvest
```

### 5.4 10-loop run through API path

Executed through integrated-engine API path:

```text
POST /api/vectorfl-engine/actions/language-loop/run
payload: count=10, sleep=2, timeout=120
```

Result:

- loop id: `language_loop_20260416T112603Z`
- completed: `10 / 10`
- status: `completed`
- index: `runtime/language_loops/language_loop_20260416T112603Z/index.md`

### 5.5 harvest result

Harvested:

- harvest: `runtime/language_loops/language_loop_20260416T112603Z/harvest.md`
- extracted rows after parser hardening: `24`

Parser note:

- Initial harvest extracted only `10` rows because several Codex returns used markdown table format.
- Harvest parser was hardened to parse table rows too.
- Re-harvest extracted `24` rows.

## 6. strongest axes from 10-loop harvest

Current top repeated axes:

1. `readable-report-before-visible-translation axis`
2. `surface gravity axis`
3. `bridge preservation axis`

Other useful candidates:

- `candidate-not-authority axis`
- `human-operating view`
- `boundary-first terms`
- `axis-derived interface`
- `proposal material axis`
- `summary layer before glossary/canonical copy`

## 7. current interpretation

The 10-loop result confirms the earlier direction.

Strongest current reading:

```text
UI Korean copy should not be opened first.
The next stable layer is a bounded operating summary / operator report grammar.
That summary must preserve surface gravity, route signal, authority boundary, and candidate-not-authority state.
```

This directly supports the user's larger goal:

```text
통합엔진 위에서 내가 보고 판단하고 지시할 수 있어야 한다.
터미널 Codex가 혼자 처리하는 것이 아니라, VectorFL면이 운영 위치가 되어야 한다.
```

## 8. watchpoints

1. Synchronous 10-loop run takes several minutes and blocks the request until done.
2. `Internal Language Loop` panel could become too large if previews grow.
3. Harvest grouping is useful but still text-pattern based, not semantic canonicalization.
4. Loop output must not be treated as glossary, UI copy, or promotion evidence by itself.

## 9. next smallest step

Next should not be Gemini adapter yet.

Next should be:

```text
VectorFL면에서 latest harvest를 읽고,
그 harvest에서 "사용자가 지금 봐야 할 운영 요약"만 얇게 올리는 summary strip 후보를 만든다.
```

This is not final UI copy. It is a small operating summary layer derived from harvested axes.

## 10. closeout

PASS_WITH_NOTE.

The integrated engine can now run the internal-language data loop and harvest it from the VectorFL surface path. The remaining note is that loop execution is synchronous; if this becomes painful in real use, background/progress support becomes a real bottleneck rather than speculative architecture.
