# source_assets_creation_map_v1

이 문서는 앞으로 Codex가 새 문서를 만들 때
어느 폴더에 둬야 하는지 빠르게 확인하는 **배치 기준표**다.

핵심 원칙:
- raw 입력은 `inputs/`
- source asset 성격의 md는 `source_assets/`
- 해석/예시/정책/계약/리포트는 `docs/`
- 실행 기록과 판독 sidecar는 `runtime/`

## 1. Codex가 만드는 md는 어디에 두나

### 선언문
- 위치: [source_assets/declarations](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations)
- 예:
  - `vectorfl_declaration_*`
  - `codex_declaration_*`

### 기준문 / baseline
- 위치: [source_assets/baselines](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines)
- 예:
  - `codex_baseline_*`
  - `exploration_baseline_*`

### 지시서 / directive
- 위치: [source_assets/directives](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives)
- 예:
  - `codex_directive_*`
  - `thin_operation_rules_lock_v1.md`

### handoff
- 위치: [source_assets/handoffs](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs)
- 예:
  - `codex_handoff_*`

### 외부 사례 입력 source asset
- 위치: [source_assets/external_case_inputs](/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs)
- 예:
  - `external_case_first_pass_*_input_*.md`

### 세션 요약 / close note
- 위치: [source_assets/session_notes](/Users/sungsookim/universe/vectorfl_replica/source_assets/session_notes)
- 예:
  - `codex_summary_today_session_close_v1.md`

## 2. source asset이 아닌 문서는 어디에 두나

### 사용 설명서 / 운영 가이드
- 위치: [docs/guides](/Users/sungsookim/universe/vectorfl_replica/docs/guides)

### 계약 / 불변 기준
- 위치: [docs/contracts](/Users/sungsookim/universe/vectorfl_replica/docs/contracts)

### 구조 명세 / 폴더 역할표 / 배치 규칙
- 위치: [docs/specs](/Users/sungsookim/universe/vectorfl_replica/docs/specs)

### 운영 규정
- 위치: [docs/policies](/Users/sungsookim/universe/vectorfl_replica/docs/policies)

### 사례 readout / 리뷰 / 분석
- 위치: [docs/reports](/Users/sungsookim/universe/vectorfl_replica/docs/reports)
- 외부 사례 first-pass 설명 문서도 여기 성격이지만 현재는 예시 사용성이 높아 [docs/examples](/Users/sungsookim/universe/vectorfl_replica/docs/examples) 를 우선 사용

### 예제 문서
- 위치: [docs/examples](/Users/sungsookim/universe/vectorfl_replica/docs/examples)

## 3. runtime 쪽은 무엇을 두나

### exploration observation
- 위치:
  - [runtime/observer/exploration/json](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/exploration/json)
  - [runtime/observer/exploration/md](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/exploration/md)

### checklist / repeat-check / trigger reading
- 위치: [runtime/contracts](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts)

### receipt / board / commands
- 위치:
  - [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
  - [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
  - [runtime/commands](/Users/sungsookim/universe/vectorfl_replica/runtime/commands)

## 4. 제일 쉬운 규칙
- 네가 넣는 raw 파일: `inputs/`
- 내가 만드는 source md: `source_assets/`
- 내가 설명용으로 남기는 문서: `docs/`
- 엔진이 남기는 기록: `runtime/`

## 5. note
- 기존 루트 md는 과거 canonical asset이 많아서 바로 안 옮긴다.
- 앞으로 새로 만드는 Codex용 source md는 가능한 한 루트가 아니라 `source_assets/` 아래에서 시작한다.
