# Integrated Engine Language Loop Harvest

- loop_id: `language_loop_20260416T114515Z`
- session_count: `10`
- extracted_row_count: `14`
- created_at: `2026-04-16T11:55:17Z`

## Reading

This harvest collects repeated internal-language signals from loop outputs and groups them into Koreanization data plus line / connection / axis material.
It is not UI copy, not a final glossary, and not a promotion gate.

## Top Axes

- `bridge preservation axis` (2)
- `readable-report-before-UI-copy axis` (1)
- `proposal material axis` (1)
- ``surface exposure axis`` (1)
- ``surface-density axis`` (1)
- ``readable-report-before-UI-copy axis`` (1)
- ``decision-state grammar`` (1)

## Top Koreanization Candidates

- `상태 -> 3면별 읽기 -> 열린/닫힌 route -> 마찰 -> 다음 작은 실행` (1)
- `디자인 점토 / 설계 원재료` (1)
- `평탄화 전 다리 놓기` (1)
- ``최신 반환`, `최근 반환`, `최근 판단 보조 기록`` (1)
- ``각 면의 정체성은 계속 보여야 함`` (1)
- ``평탄화 전 연결`, `단순화 전 브리지`` (1)
- ``화면 번역 전 보고 문법`, `UI copy 전 운영 보고 문법`` (1)
- ``보류 / 관찰 유지 / 이어 가져감 / 충돌로 거절`` (1)

## Top Risky Korean Flattening

- `요약`, `결론만`, `로드맵 나열` (1)
- `디자인 초안` (1)
- `쉽게 풀기, 간단히 말하기` (1)
- ``전체 기록`, `메모리`, `완전한 히스토리`` (1)
- ``통합 화면`, `하나의 작업판`` (1)
- ``쉽게 바꾸기`, `사용자 친화 표현`` (1)
- ``한국어로 바꾸기`, `번역 작업`, `UI 문구 작성`` (1)
- ``대기`, `유지`, `거절`만으로 단순화` (1)

## Top Connections

- `Codex report -> user judgment -> reread input` (1)
- `Gemini mock analysis, handoff artifact, explanation trial` (1)
- `friction terms, bridge work` (1)
- ``raw artifact reduction -> readable return -> still-not-ingestion`` (1)
- `shared language boundary / surface exposure density` (1)
- `friction terms collection, bridge wording boundary` (1)
- ``reread -> line extraction -> connection -> axis -> shared report -> next reread`` (1)
- `user decision / boundary-first exposure` (1)

## Axis Groups

### readable-report-before-UI-copy axis

- count: `1`

Koreanization candidates:
- 상태 -> 3면별 읽기 -> 열린/닫힌 route -> 마찰 -> 다음 작은 실행

Korean preservation requirements:
- Preserve order

Risky Korean flattening to avoid:
- 요약`, `결론만`, `로드맵 나열

Why this helps user operation:
- Lets user make a bounded decision

Next reread questions:
- Does this sequence reduce user judgment burden?

### unclassified

- count: `6`

Next reread questions:
- 실제 Codex run 1건을 이 문법으로 보고하면 사용자가 판단 부담을 덜 느끼는가?
- `지원`과 `보조` 중 어느 쪽이 중심-보조 관계를 더 잘 보존하는가
- `재료`가 내부 처리성을 충분히 보존하는가, 아니면 사용자에게 낯선가?

### proposal material axis

- count: `1`

Koreanization candidates:
- 디자인 점토 / 설계 원재료

Korean preservation requirements:
- visual strength와 structural authority 분리

Risky Korean flattening to avoid:
- 디자인 초안

Why this helps user operation:
- 사용자가 시각 강도를 core 권위로 오인하지 않음

Next reread questions:
- design clay가 너무 비공식적으로 들리지 않는가

### bridge preservation axis

- count: `2`

Koreanization candidates:
- 평탄화 전 다리 놓기
- `평탄화 전 연결`, `단순화 전 브리지`

Korean preservation requirements:
- 쉬운 말보다 보호 의미 우선
- bridge work가 내부 문법을 대체하지 않고 이후 layer임을 보존해야 함

Risky Korean flattening to avoid:
- 쉽게 풀기, 간단히 말하기
- `쉽게 바꾸기`, `사용자 친화 표현`

Why this helps user operation:
- 사용자가 용어 단순화로 운영 규칙을 잃지 않음
- 쉬워진 말 때문에 운영 권한이나 경로 의미가 사라지는 것을 막음

Next reread questions:
- 어떤 의미를 bridge에서 반드시 못 줄이는가
- `평탄화`가 내부 용어로 유지 가능한가, 아니면 `단순화`가 더 읽히는가

### `surface exposure axis`

- count: `1`

Koreanization candidates:
- `최신 반환`, `최근 반환`, `최근 판단 보조 기록`

Korean preservation requirements:
- 기억 전체가 아니라 대화 지속과 판단 보조용 artifact라는 한계

Risky Korean flattening to avoid:
- `전체 기록`, `메모리`, `완전한 히스토리`

Why this helps user operation:
- raw artifact를 직접 열지 않고도 다음 판단에 필요한 맥락을 회수함

Next reread questions:
- latest/recent card가 내부 기록 카드처럼만 보이고 실제 대화 흐름으로는 약한가?

### `surface-density axis`

- count: `1`

Koreanization candidates:
- `각 면의 정체성은 계속 보여야 함`

Korean preservation requirements:
- user operation, VectorFL mediation, engine processing 구분 유지

Risky Korean flattening to avoid:
- `통합 화면`, `하나의 작업판`

Why this helps user operation:
- 어디서 결정하고 어디서 처리하고 어디서 중재하는지 잃지 않게 함

Next reread questions:
- 각 surface에서 동일 phrase가 다른 밀도로 나타날 때 어떤 표기가 필요한가?

### `readable-report-before-UI-copy axis`

- count: `1`

Koreanization candidates:
- `화면 번역 전 보고 문법`, `UI copy 전 운영 보고 문법`

Korean preservation requirements:
- 즉석 번역이 아니라 내부 문법을 보존한 운영 보고라는 점.

Risky Korean flattening to avoid:
- `한국어로 바꾸기`, `번역 작업`, `UI 문구 작성`

Why this helps user operation:
- 사용자가 구조 상태, 열린 route, 닫힌 route, 다음 작은 단계를 판단 가능하게 됨.

Next reread questions:
- 실제 Codex run 반환 1건에 이 문법을 적용했을 때 사용자가 판단 가능한가?

### `decision-state grammar`

- count: `1`

Koreanization candidates:
- `보류 / 관찰 유지 / 이어 가져감 / 충돌로 거절`

Korean preservation requirements:
- action과 state를 구분해야 함

Risky Korean flattening to avoid:
- `대기`, `유지`, `거절`만으로 단순화

Why this helps user operation:
- 당장 결정, 지켜보기, 다음 묶음으로 넘기기, 충돌 차단을 구분함

Next reread questions:
- carry-forward와 hold의 실제 운영 차이는 어떤 return에서 드러나는가?

## Sessions

- `cli_20260416T114515Z_125ce536` iteration `1` status `done` extracted `1`
  - operator_report: `runtime/cli_sessions/cli_20260416T114515Z_125ce536/operator_report.md`
- `cli_20260416T114609Z_0e7f1b54` iteration `2` status `done` extracted `1`
  - operator_report: `runtime/cli_sessions/cli_20260416T114609Z_0e7f1b54/operator_report.md`
- `cli_20260416T114724Z_f6aaedcc` iteration `3` status `done` extracted `2`
  - operator_report: `runtime/cli_sessions/cli_20260416T114724Z_f6aaedcc/operator_report.md`
- `cli_20260416T114819Z_3a7e6e4d` iteration `4` status `done` extracted `1`
  - operator_report: `runtime/cli_sessions/cli_20260416T114819Z_3a7e6e4d/operator_report.md`
- `cli_20260416T114911Z_63fee852` iteration `5` status `done` extracted `2`
  - operator_report: `runtime/cli_sessions/cli_20260416T114911Z_63fee852/operator_report.md`
- `cli_20260416T115006Z_160a9a36` iteration `6` status `done` extracted `1`
  - operator_report: `runtime/cli_sessions/cli_20260416T115006Z_160a9a36/operator_report.md`
- `cli_20260416T115112Z_d1256d58` iteration `7` status `done` extracted `2`
  - operator_report: `runtime/cli_sessions/cli_20260416T115112Z_d1256d58/operator_report.md`
- `cli_20260416T115217Z_c9eb3c72` iteration `8` status `done` extracted `1`
  - operator_report: `runtime/cli_sessions/cli_20260416T115217Z_c9eb3c72/operator_report.md`
- `cli_20260416T115313Z_48de88e6` iteration `9` status `done` extracted `2`
  - operator_report: `runtime/cli_sessions/cli_20260416T115313Z_48de88e6/operator_report.md`
- `cli_20260416T115405Z_a05be783` iteration `10` status `done` extracted `1`
  - operator_report: `runtime/cli_sessions/cli_20260416T115405Z_a05be783/operator_report.md`

## Boundary

- Harvest only.
- No UI copy patch.
- No final glossary.
- No automatic promotion.
