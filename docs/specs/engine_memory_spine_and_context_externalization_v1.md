# engine_memory_spine_and_context_externalization_v1.md

## 1. purpose

이 문서는 현재 엔진에서
무엇을 어떤 층에 외부화하여 기억할지,
그리고 컨텍스트가 흔들릴 때 어떤 순서로 다시 복귀할지를 고정한다.

핵심 목적은 두 가지다.

- 유한한 메모리를 보호한다
- 중요한 과정 기억과 철학 방향성을 파일 시스템 안에서 복원 가능하게 만든다

---

## 2. top principle

기억은 한 군데에 몰아넣지 않는다.

엔진 기억은 아래처럼 나뉜다.

- 철학 방향성 기억
- 사용자 문제 인식 방식 기억
- 기능/기술/운영/철학 피드백 기억
- 자원 능력 차이 기억
- run별 에피소드 기억
- current operating reality 기억

즉 기억은 단일 노트가 아니라
**spine을 가진 다층 external memory**로 본다.

---

## 3. memory spine layers

## 3-1. philosophical directionality memory

역할:

- 모든 처리의 상위 방향성 보존
- 결과보다 차이/층위/과정 기억을 우선하게 만드는 기준

대표 문서:

- `docs/specs/engine_philosophical_directionality_checklist_v1.md`

---

## 3-2. operator problem-recognition memory

역할:

- 사용자가 문제를 어떻게 인식하는지
- 어떤 작은 간극을 중요하게 보는지
- 어떤 과정을 통해 문제를 푸는지
를 기억

위치:

- `runtime/memory/problem_recognition/`

대표 문서:

- `runtime/memory/problem_recognition/operator_problem_recognition_basis_v1.md`

---

## 3-3. resource capability boundary memory

역할:

- Codex와 외부 자원의 능력 차이
- 실패 위험
- delegation 확장 조건
을 기억

위치:

- `gemini/`
- 향후 다른 자원 폴더도 동일 원칙

대표 문서:

- `gemini/resource_capability_boundary_memory_v1.md`
- `gemini/gemini_task_dispatch_policy_v1.md`

---

## 3-4. feedback memory

역할:

- 기능적 / 기술적 / 운영적 / 철학적 피드백 누적
- 이후 판단 / 위임 / 확장 gate에서 반복 재사용할 기준 저장
- Codex 자신의 미래 판단 품질을 위한 memory 축적

위치:

- `runtime/memory/feedback/`

대표 문서:

- `docs/specs/engine_feedback_memory_loop_v1.md`
- `runtime/memory/feedback/feedback_capture_basis_v1.md`

---

## 3-5. episodic operation memory

역할:

- 특정 run에서 무엇이 일어났는지
- 어떤 판단이 내려졌는지
- 어떤 결과가 나왔는지
를 에피소드 단위로 보존

위치:

- `docs/reports/`
- `runtime/receipts/`
- `runtime/views/repo_delta_log_latest_v1.md`
- `runtime/logs/repo_delta_log.jsonl`

---

## 3-6. current reality memory

역할:

- 지금 기준으로 무엇이 active인가
- 무엇이 authoritative한가
- 어떤 surface를 먼저 읽어야 하는가
를 현재 시점 관점에서 보존

위치:

- `runtime/views/current_asset_map_v1.md`
- `runtime/views/repo_shared_reality_pack_index_v1.md`
- `runtime/views/engine_operating_layer_manifest_v1.json`

---

## 4. externalization rule

새로운 기억이 생기면 먼저 그 종류를 판단한다.

### A. directionality-level memory

예:

- 철학 방향성
- 처리 원칙
- 결과보다 과정을 우선해야 한다는 기준

저장 위치:

- `docs/specs/`

### B. user-thinking/process memory

예:

- 사용자가 문제를 보는 방식
- 작은 차이를 중요하게 여기는 방식
- 쉽게 납작하게 만들지 말아야 할 이유

저장 위치:

- `runtime/memory/problem_recognition/`

### C. resource-boundary memory

예:

- Gemini는 어디까지 맡길 수 있는가
- 외부 자원의 failure risk는 무엇인가

저장 위치:

- 해당 자원 폴더

### D. run-specific memory

예:

- 특정 live run
- 특정 cohort compare
- 특정 validation

저장 위치:

- `docs/reports/`
- `runtime/receipts/`
- delta log

---

## 5. context recovery order

메모리 부족, 컨텍스트 회전, 긴 작업 이후 복귀 시
아래 순서로 다시 읽는다.

1. `runtime/views/repo_shared_reality_pack_index_v1.md`
2. `runtime/views/current_asset_map_v1.md`
3. `runtime/views/repo_delta_log_latest_v1.md`
4. `docs/specs/engine_philosophical_directionality_checklist_v1.md`
5. `runtime/memory/problem_recognition/operator_problem_recognition_basis_v1.md`
6. `runtime/memory/feedback/feedback_capture_basis_v1.md`
7. 필요 시 `gemini/resource_capability_boundary_memory_v1.md`
8. 현재 작업과 직접 연결된 latest report/receipt

---

## 6. practical rule

새 문서를 만들 때는
“무슨 내용을 쓸까”보다 먼저
“이 기억은 어느 층에 속하는가”를 판단한다.

이 판단이 선행되면,

- 철학 기억은 흩어지지 않고
- 문제 인식 기억은 사라지지 않고
- feedback 기억은 다음 판단에 다시 재사용되고
- run 기억은 나중에 비교 가능한 형태로 남고
- 자원 위임 기준도 오염되지 않는다

---

## 7. one-line lock

엔진 기억은 단일 메모가 아니라 spine을 가진 다층 external memory여야 하며, 철학 방향성, 사용자 문제 인식 방식, feedback 기억, 자원 경계, run 에피소드, current reality를 각기 다른 층에 기록해야 한다.
