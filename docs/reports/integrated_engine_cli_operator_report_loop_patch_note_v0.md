# Integrated Engine CLI Operator Report Loop Patch Note v0

Date: 2026-04-16

## 0. verdict

PASS

이번 라운드는 CLI run 직후 Codex가 사용할 shared operational language 문법으로 `operator_report.md`를 자동 생성하는 얇은 기록 루프를 추가했다.

이 패치는 UI 한국어 번역, final glossary, wording patch, Gemini adapter, deposit ingestion, automatic assignment, promotion/canonicalization을 열지 않는다.

## 1. round goal

사용자가 지적한 핵심은 "화면에 한국어를 붙이는 것"이 아니라, 우리가 만든 번역/문법 자료를 바탕으로 Codex가 먼저 사용할 수 있는 보고 문법을 만드는 것이었다.

따라서 이번 목표는:

- Codex run 결과를 단순 raw stdout / structured return으로만 남기지 않는다.
- run 직후 사용자 판단용 운영 리포트를 함께 남긴다.
- 그 리포트는 `상태 -> 3면별 읽기 -> route/authority -> friction -> 다음 작은 행동` 순서를 따른다.
- VectorFL page에서도 latest operator report preview를 볼 수 있게 한다.

## 2. files changed

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_cli_operator_report_loop_patch_note_v0.md`

생성된 검증 artifact:

- `runtime/cli_sessions/cli_20260416T110824Z_2226c8b1/operator_report.md`

## 3. what changed

### 3.1 session artifact

CLI session spec에 `operator_report_path`를 추가했다.

새로운 session artifact:

```text
runtime/cli_sessions/<session_id>/operator_report.md
```

### 3.2 operator report generation

Codex run이 끝나면 `_build_cli_operator_report`가 다음 구조로 report를 생성한다.

- Status First
- Surface Split
  - User Surface
  - VectorFL Surface
  - Engine Surface
- Route And Authority
- Friction Reading
- Source Material
- Result Summary Preview
- Next Smallest Action

이 보고서는 화면 문구 번역이 아니라, 내부 route signal을 사용자 판단 언어로 다시 읽는 기록이다.

### 3.3 mark update regeneration

session에 mark가 붙을 때도 `operator_report.md`를 다시 쓴다.

이유:

- `validation_target`, `deposit_candidate` 같은 mark는 route signal이다.
- mark가 바뀌면 operator report의 `current_marks`도 바뀌어야 한다.

### 3.4 API readable state

`build_cli_host_control_state`가 다음 값을 노출한다.

- `latest_operator_report_preview`
- `latest_readable_return.operator_report_preview`
- `recent_readable_returns[].operator_report_preview`
- `deposit_ready_returns[].operator_report_preview`
- 각 readable item의 `operator_report_path`

### 3.5 VectorFL UI preview

`CliHostControlPanel`에 `operator report preview` 영역을 추가했다.

이 영역은 UI 한국어 copy replacement가 아니다. 최신 session의 operator report를 VectorFL operating flow에서 바로 읽을 수 있게 하는 preview다.

## 4. validation

### 4.1 static checks

통과:

- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py`
- `npm run build` in `app/ui/integrated_engine`

### 4.2 server refresh

viewer server를 재시작해서 새 API code를 로드했다.

확인:

- `http://127.0.0.1:8421/api/vectorfl-engine/state` 응답 정상
- `cli_host_control.latest_readable_return.operator_report_path` 노출

### 4.3 real Codex run

실제 read-only Codex run을 실행했다.

- session id: `cli_20260416T110824Z_2226c8b1`
- task type: `reread`
- status: `done`
- exit code: `0`
- suggested next use: `validation_target`
- generated operator report: `runtime/cli_sessions/cli_20260416T110824Z_2226c8b1/operator_report.md`

### 4.4 mark regeneration

동일 session을 `validation_target`으로 mark했다.

확인:

- mark action succeeded
- session marks include `validation_target`
- `operator_report.md` regenerated with `current_marks: validation_target`
- API latest readable return includes operator report preview

## 5. why this is baseline-safe

- CLI는 여전히 4번째 surface가 아니다.
- VectorFL surface가 CLI operation / reread 중심이다.
- User surface와 Engine surface는 operator report 안에서 역할별 읽기로만 분리된다.
- report는 candidate/route signal을 설명하지만, 자동 assignment나 promotion을 만들지 않는다.
- deposit candidate는 여전히 official ingestion이 아니다.
- UI 문구를 한국어로 치환하지 않았다.
- Gemini adapter를 열지 않았다.

## 6. line / connection / axis feedback

강해진 line:

- `operator_report.md`는 raw output과 사용자 판단 사이의 bridge artifact다.
- mark가 붙으면 report도 route signal에 맞게 갱신되어야 한다.
- UI copy 이전에 session-level operator report가 먼저 안정되어야 한다.

강해진 connection:

```text
Codex run
-> structured return
-> operator_report.md
-> mark update
-> regenerated operator report
-> VectorFL latest preview
```

강해진 axis:

```text
run artifact must carry user-judgment grammar before UI language patch
```

## 7. watchpoints

1. Operator report가 final glossary처럼 굳으면 안 된다.
2. Operator report preview가 automatic validation/promotion처럼 읽히면 안 된다.
3. UI에서 보고서 preview가 너무 커져 VectorFL control flow를 밀어내면 안 된다.

## 8. next smallest step

다음 가장 작은 단계는 브라우저에서 VectorFL panel의 `operator report preview`가 실제로 보이는지 확인하는 것이다.

확인 기준:

- 최신 session `cli_20260416T110824Z_2226c8b1`가 보인다.
- operator report preview가 보인다.
- preview에서 `validation_target`이 완료가 아니라 route signal로 설명된다.
- raw file을 열지 않아도 1차 판단이 가능하다.

## 9. closeout

PASS.

CLI-on-top run 결과는 이제 raw artifact / structured return / deposit candidate에 더해, 사용자 판단용 shared language report까지 함께 남긴다. 이로써 UI 번역을 열기 전에 Codex가 사용할 보고 문법이 실제 session artifact 경로에 붙었다.
