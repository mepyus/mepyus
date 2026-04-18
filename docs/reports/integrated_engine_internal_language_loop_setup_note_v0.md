# Integrated Engine Internal Language Loop Setup Note v0

Date: 2026-04-16

## 0. verdict

PASS

내부 언어를 사용자 판단 가능한 line / connection / axis 재료로 옮기는 작은 반복 루프를 셋업했다.

이 루프는 UI 번역, final glossary, wording patch, Gemini adapter, deposit ingestion, automatic assignment, promotion/canonicalization을 열지 않는다.

## 1. purpose

목표는 현재 integrated engine 내부 언어를 바로 한국어 UI 문구로 바꾸는 것이 아니다.

목표는 반복적으로 다음 재료를 모으는 것이다.

```text
internal phrase or signal
-> human-readable line
-> repeated connection
-> emerging axis
-> surface exposure note
-> do-not-flatten boundary
-> next reread question
```

이 재료가 쌓이면 나중에 사용자면 / VectorFL면 / 엔진면 중 어디에 어떤 언어가 올라와야 하는지 더 정확히 판단할 수 있다.

## 2. implemented runner

추가한 runner:

```text
scripts/run_integrated_engine_language_loop.py
```

이 runner는 기존 CLI session 경로를 그대로 사용한다.

- `run_integrated_engine_cli_session`
- `mark_integrated_engine_cli_session`
- `runtime/cli_sessions/<session_id>/operator_report.md`

즉 새 agent system이나 새 surface가 아니다.

## 3. artifact layout

각 루프는 다음 위치에 기록된다.

```text
runtime/language_loops/<loop_id>/
  loop.json
  index.md
```

각 iteration은 기존 CLI session artifact를 만든다.

```text
runtime/cli_sessions/<session_id>/
  session.json
  prompt.md
  stdout.log
  stderr.log
  structured_return.json
  deposit_candidate.md
  operator_report.md
```

## 4. default context rotation

기본 context set은 4개 묶음으로 회전한다.

1. CLI-on-top shared language grammar + operator report grammar trial
2. current operating state + surface exposure boundary
3. line/connection/axis map + internal language grammar candidate
4. operator report loop patch note + shared operational language growth note

이렇게 한 이유:

- 한 문서만 반복하면 같은 표현만 재생산된다.
- 너무 많은 문서를 한 번에 주면 run이 무거워진다.
- 4개 묶음이면 10회/20회 루프에서 같은 축을 다른 문맥으로 반복 확인할 수 있다.

## 5. usage

1회 smoke:

```bash
python3 scripts/run_integrated_engine_language_loop.py --count 1 --timeout 90
```

10회 루프:

```bash
python3 scripts/run_integrated_engine_language_loop.py --count 10 --sleep 2 --timeout 120
```

20회 루프:

```bash
python3 scripts/run_integrated_engine_language_loop.py --count 20 --sleep 2 --timeout 120
```

주의:

- Codex CLI는 local `~/.codex` session 접근이 필요하다.
- Codex sandbox 안에서 직접 실행하면 session file permission 때문에 실패할 수 있다.
- 일반 터미널 또는 승인된 command path에서 실행해야 한다.

## 6. validation performed

### 6.1 script compile

통과:

```bash
python3 -m py_compile scripts/run_integrated_engine_language_loop.py
```

### 6.2 sandbox failure observed

처음 sandbox 내부 실행은 실패했다.

- loop_id: `language_loop_20260416T111317Z`
- session: `cli_20260416T111317Z_d57425f1`
- reason: Codex CLI could not access `/Users/sungsookim/.codex/sessions`

해석:

- runner 구조 실패가 아니라 Codex CLI local session file 접근 문제다.
- 실제 루프는 sandbox 밖에서 실행해야 한다.

### 6.3 real smoke pass

승인된 실행 경로로 1회 smoke를 통과했다.

- loop_id: `language_loop_20260416T111421Z`
- loop index: `runtime/language_loops/language_loop_20260416T111421Z/index.md`
- session: `cli_20260416T111421Z_ab9778e6`
- status: `done`
- mark: `validation_target`
- operator report: `runtime/cli_sessions/cli_20260416T111421Z_ab9778e6/operator_report.md`

## 7. what the first successful loop produced

첫 성공 loop에서 확인된 line:

- `engine material`은 최종 결과나 승인된 판단으로 줄이면 안 된다.
- `한국어 UI copy 전에 Codex 보고 문법`이 먼저 안정되어야 한다.
- repeated connection은 `internal reread -> shared reporting grammar -> user-readable report -> engine reread input`으로 읽힌다.
- 아직 실제 UI/runtime artifact와 대조가 더 필요하다.

강해진 axis:

```text
readable-report-before-UI-copy
```

## 8. operating boundary

이 루프가 하는 것:

- 내부 언어 번역 데이터 수집
- line / connection / axis 후보 수집
- surface exposure note 수집
- operator report artifact 생성

이 루프가 하지 않는 것:

- UI 문구 변경
- final glossary 확정
- manifest/read-map 변경
- Gemini adapter 실행
- deposit ingestion
- automatic assignment
- promotion/canonicalization

## 9. recommended loop use while second setup continues

두 번째 셋업 작업과 병행하려면 10회부터 시작하는 것이 적절하다.

추천:

```bash
python3 scripts/run_integrated_engine_language_loop.py --count 10 --sleep 2 --timeout 120
```

이유:

- 10회면 4개 context set을 2회 이상 돌며 반복 line을 볼 수 있다.
- 20회는 더 많은 재료를 주지만, 초반에는 중복/노이즈도 같이 늘 수 있다.
- 10회 결과를 먼저 읽고, 반복되는 line이 안정적이면 20회로 늘리는 것이 낫다.

## 10. next read target after loop

루프가 끝나면 먼저 읽을 것:

```text
runtime/language_loops/<latest_loop_id>/index.md
```

그 다음:

```text
runtime/cli_sessions/<session_id>/operator_report.md
runtime/cli_sessions/<session_id>/structured_return.json
```

## 11. closeout

PASS.

내부 언어를 즉석 한국어 번역으로 밀어붙이지 않고, 기존 통합엔진 CLI-on-top 경로 위에서 반복적으로 line / connection / axis 재료를 수집하는 작은 루프가 준비되었다.
