# Material Input Baseline

## Decision

`vectorfl_next`에서 입력은 먼저 종류별 객체로 나뉘는 것이 아니라, 모두 `material`로 들어온다.
입력 기준선은 `source_type`보다 `formation role`을 먼저 본다.

## Core rule

- 모든 입력은 먼저 `material`이다.
- `material`은 raw payload를 유지한다.
- source는 `source_type`, `source_ref`로만 느슨하게 기록한다.
- 형성 경로 차이는 나중에 pressure, trace, reentry, lineage에서 드러나게 둔다.

## Formation roles

현재 최소 역할 구분은 아래 네 가지다.

### 1. fresh material

- 새로운 공간 재료
- 아직 기존 family나 lineage에 강하게 묶이지 않은 유입

예:

- human note
- new note batch
- external text input

### 2. reentry material

- 기존 family 또는 lineage를 가진 재유입 재료
- 같은 material family가 다른 pressure 아래 다시 들어오는 경우

예:

- revisited note
- repeated claim
- prior run artifact reintroduced

### 3. observer material

- observer, report, probe, manifest, runtime report 같은 관찰 산출물
- 공간을 직접 만들기보다 이미 생긴 공간을 다시 읽은 결과

예:

- workspace report
- reactive observer output
- probe summary

### 4. engine-self material

- Codex worklog, engine runtime summary, internal audit 같은 자기기록
- 엔진 자신의 형성 흔적을 다시 재료로 삼는 입력

예:

- codex worklog
- migration report
- internal audit note

## source_type posture

`source_type`은 ontology가 아니라 출처 tag다.

가능 예시:

- `note`
- `report`
- `worklog`
- `observer_output`
- `llm_output`
- `code_run`
- `manifest`

중요:

- `source_type` 이름을 먼저 정교하게 늘리지 않는다.
- formation role보다 source_type taxonomy가 앞서면 다시 분류 엔진으로 회귀한다.

## Why

- 지금 엔진은 입력 종류를 빨리 판정하는 엔진이 아니라 공간 형성 엔진이다.
- 입력의 본질은 이름보다도, 재유입과 압력 변화 아래 어떤 형성 역할을 하느냐에 있다.

## Follow-up risk

- formation role 판정은 아직 코드에 박지 않았다.
- 현재는 ingest helper에서 optional metadata로만 기록한다.
- 다음 단계에서 intake policy로 이어질 수 있다.
