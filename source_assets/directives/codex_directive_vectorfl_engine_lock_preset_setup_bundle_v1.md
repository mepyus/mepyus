[[DOCROLE:directive]]
[[RUNMODE:ingest_then_execute]]
[[PRIORITY:high]]

[[A]] [[OBJ:engine_lock_preset_docs]] [[SEM:declaration_baseline_directive_for_codex_execution]]

# VECTORFL Replica 엔진 잠금 전 사전 셋업 문서 묶음 v1

## 시나리오 기준: 새 회사/새 프로그램/공간 기반 관찰-설계-코드-재투입 루프

---

# 0. 이 문서의 목적

이 문서는 다음 시나리오를 기준으로,
`vectorfl_replica` 엔진을 잠그기 전에 **미리 세팅하면 좋은 것들**을
Codex가 실제 입력 후 실행 가능한 형태로 정리한 문서 묶음이다.

기준 시나리오:

- 내가 새로운 회사/새로운 업무 환경에 들어간다
- 내부 구조, 흐름, 병목, 장단점, 기존 프로그램 문제를 기록한다
- 그 재료를 공간에 넣는다
- 필요할 때 응결핵(효율, 병목, 정체, 책임이동, 반복수정 등)으로 관측한다
- 그 결과를 바탕으로 새 프로그램/서브 앱/보조 도구를 만든다
- ChatGPT/Gemini가 만든 코드와 문서를 다시 공간에 reference asset으로 넣는다
- Codex는 repo/공간을 탐색하고 수정/회수/연결/반복작업을 수행한다
- 나중에 리소스가 생기면 에이전트가 약한 연결과 부족한 이해를 이유를 남기며 보강한다

중요:
이 문서는 지금 당장 엔진을 크게 확장하자는 것이 아니다.
이 문서는 **미리 바닥을 잠가두면 나중 작업 속도와 확장성이 올라가는 셋업**을 정리한 것이다.

---

# 1. 선언문 v1

## 공간 본체 유지 · 입력 자유 · 기억 우선 · 관측 분리 선언

### 1-1. 최종 선언 한 줄

우리는 공간을 본체로 유지하고, 입력은 자유롭게 받되, 입력기 일관성과 기록/기억 경계를 먼저 잠근다. 관측/탐색/검색/코드/보강은 모두 상부 부품으로 다루며, 결과는 공간을 덮어쓰지 않고 별도 기억층에 append한다.

### 1-2. 공간 선언

- 공간은 특정 프로그램이나 특정 도구의 하위 저장소가 아니다.
- 공간은 모든 지류가 모이는 바다이며, raw input부터 관측 기억까지 받아내는 본체다.
- 공간은 지금 당장 한눈에 보이지 않아도 된다.
- 공간은 지금 당장 예쁘게 표현되지 않아도 된다.
- 공간은 먼저 살아 있어야 하며, 해석은 필요할 때만 수행한다.

### 1-3. 입력 선언

- 입력은 잠그지 않는다.
- 입력을 위해 재료를 매번 손질하도록 강제하지 않는다.
- 날것 메모, 대화, 정리문, Codex 실행 흔적, 코드, 수정 이유, 판단 메모 모두 raw lane으로 들어올 수 있다.
- 잠그는 것은 입력 자체가 아니라 입력기 흔들림을 점검하는 기준 참조셋이다.

### 1-4. 입력기 선언

- 현재 국면의 핵심은 더 똑똑한 의미판정이 아니라 입력기 일관성 확보다.
- 목표는 정확도 100%가 아니라 재현 가능한 축/라벨/앵커 결과다.
- 구조화 문서(선언문/기준문/지시서/정리문)는 공간 입력이기도 하지만 동시에 calibration reference가 될 수 있다.
- calibration reference는 입력 제한이 아니라 입력기 점검 기준이다.

### 1-5. 기억 선언

- 자연 숙성의 핵심은 무개입이 아니라 기록과 기억이다.
- 최소한 다음 기억층은 분리되어야 한다.
  - 입력 기억
  - 해석 기억
  - 관측 기억
  - 보강 기억
- 기억 없는 축적은 숙성이 아니라 적재다.

### 1-6. 관측 선언

- 관측기/탐색기/응결핵 테스트기는 공간 본체가 아니다.
- 이들은 공간에 질문을 던지는 detachable 부품이다.
- 관측 결과는 원본을 덮어쓰지 않는다.
- 관측 결과는 별도 append-only memory에 남긴다.
- 응결핵은 선언이 아니라 시험점이다.

### 1-7. 코드 선언

- 코드도 reference asset으로 들어올 수 있다.
- 단, 코드 자체만 저장하는 것은 불충분하다.
- 코드에는 목적, 배경 문제, 연결 앵커, 수정 이유, 적용 흐름이 같이 남아야 한다.
- 그래야 코드는 죽은 파일이 아니라 살아 있는 공간 reference가 된다.

### 1-8. Codex 선언

- Codex는 공간 본체를 재정의하는 존재가 아니다.
- Codex의 기본 역할은 탐색, 회수, 반복 수정, 패치, 비교, 연결 제안이다.
- Codex는 원본을 덮어쓰기보다 append와 patch proposal을 우선한다.

### 1-9. 에이전트 선언

- 에이전트는 나중에 약한 연결과 부족한 이해를 보강하는 존재다.
- 에이전트는 “왜 채웠는지”를 남겨야 한다.
- 보강은 overwrite가 아니라 reasoned append여야 한다.

### 1-10. 운영화면 선언

- 지금 필요한 것은 전체 공간 뷰어가 아니다.
- 지금 필요한 것은 read-only operation surface다.
- 운영화면은 질문/과정/예상 시나리오/결과물/기록 포인터를 보여주는 최소 추적면이어야 한다.

---

# 2. 기준문 v1

## 엔진 잠금 전 미리 세팅하면 좋은 것들

아래는 엔진을 잠그기 전에 미리 세팅해두면 좋은 항목들이다.
우선순위는 “지금 꼭 잠가야 하는 것” 기준으로 정리한다.

---

## 2-1. 최우선 기준선 P0

### append safety / provenance 무결성 / 동시성 안전화

이건 가장 먼저 잠가야 한다.

잠가야 하는 이유:

- 기억 구조의 바닥이다
- 나중에 검색/관측/병렬 탐색을 돌리면 append 충돌 가능성이 커진다
- registry/provenance가 깨지면 전체 공간 신뢰성이 흔들린다

미리 세팅할 것:

- append-only write policy
- atomic write 또는 temp file -> rename 방식
- job_id/run_id 부여
- idempotency key
- duplicate handling rule
- malformed tail recovery rule
- lock/queue/write serialization policy

잠금 완료 기준:

- 같은 registry/provenance 파일에 다중 실행이 걸려도 tail corruption이 없을 것
- 중복 append와 partial write를 탐지/회복할 수 있을 것

---

## 2-2. P1 기억층 분리 기준

### raw / interpretation / observation / enrichment / reference 분리

미리 세팅할 것:

#### A. raw_input_memory

- 원문
- 대화
- 정리 전 메모
- 실행 로그 원본
- 회사/업무 관찰 메모

#### B. interpretation_memory

- 축
- 라벨
- 앵커
- 위치값
- 입력기 버전
- 해석 timestamp

#### C. observation_memory

- 어떤 질문으로 봤는지
- 어떤 응결핵/관측기로 봤는지
- 무엇이 어디에 붙었는지
- confidence
- 반례/예외
- 원본 포인터

#### D. reference_memory

- 코드
- 설계안
- 문서 템플릿
- 예시 구현
- 레퍼런스 요약
- 연결된 문제/목적/앵커

#### E. enrichment_memory

- gap_type
- reason
- source/provenance
- attached_to
- effect_type
- confidence

잠금 완료 기준:

- 원본 입력과 해석 결과가 분리되어 있을 것
- 관측 결과가 원본처럼 저장되지 않을 것
- 보강 결과가 원래 입력처럼 위장되지 않을 것
- 코드 reference가 raw input과 섞이지 않을 것

---

## 2-3. P1 입력기 calibration 기준

### raw input 자유 + calibration reference 별도 유지

미리 세팅할 것:

#### raw input lane

- 자유 입력 허용
- 손질 전 입력 허용
- 최소 출처/시간/유형만 태깅

#### calibration reference set

- 선언문
- 기준문
- 지시서
- 잘 정리된 정리문/요약문 일부
- 의미/맥락/흐름이 비교적 잘 살아 있는 문서군

#### calibration loop

- 입력기 version stamp
- same-reference rerun capability
- before/after diff report
- drift detection report
- 축/라벨/앵커 흔들림 표기

잠금 완료 기준:

- 입력기 수정 전/후 같은 reference 세트 결과를 비교할 수 있을 것
- “정확한지”보다 “얼마나 덜 흔들리는지”를 볼 수 있을 것

---

## 2-4. P1 코드 reference asset 기준

### 코드도 공간 reference로 재투입 가능하게 미리 포맷 고정

코드 reference 최소 필드:

- reference_id
- source_type(chatgpt/gemini/codex/manual/etc)
- purpose
- problem_context
- linked_company_flow_or_anchor
- related_docs
- related_runs
- change_reason
- result_status
- file_paths
- created_at
- updated_at

잠금 완료 기준:

- 코드가 단순 파일 보관이 아니라 문제/목적/맥락과 연결되어 조회 가능할 것
- 같은 기능의 여러 시도/폐기/수정 이력이 남을 것

---

## 2-5. P2 운영화면 기준

### 전체 공간 뷰어 말고 read-only operation surface 먼저

운영화면에서 보여야 하는 최소 항목:

- 입력/질문/지시 원문
- 실행 시각
- 관련 입력 문서/재료 포인터
- 예상 처리 시나리오
- 실제 산출물 경로
- 실패/보류/재시도 여부
- observation/ref/enrichment 포인터
- 다음 액션 후보

잠금 완료 기준:

- “무슨 작업이 지금 어떻게 흘렀는지”를 현재 기준으로 파악할 수 있을 것
- 공간 본체를 직접 열어 헤매지 않아도 운영 추적이 가능할 것

---

## 2-6. P2 관측기/응결핵 부품 기준

### read-only observation contract 고정

관측기 최소 계약:

- 원본 수정 금지
- read-only scan
- append-only result write
- 질문/핵/결과/신뢰도/예외 기록
- current view overwrite 금지
- raw/interpretation overwrite 금지

응결핵 최소 필드:

- nucleus_id
- nucleus_label
- scenario_domain
- purpose
- attached_query
- test_window
- output_pointer

잠금 완료 기준:

- 응결핵 테스트가 공간 본체를 덮어쓰지 않을 것
- “이번에 이렇게 보였다”가 “원래 이렇다”로 굳지 않을 것

---

## 2-7. P2 검색/탐색 기준

### 느슨한 search-first reference layer 먼저

미리 세팅할 것:

- 문서 검색 인덱스
- 코드 reference 검색 인덱스
- observation memory 검색 인덱스
- related anchor/label 기반 검색 포인트
- query log 저장

중요:

- 아직 full RAG 본체로 보지 않는다
- 검색 결과는 후보 문맥 공급기 역할만 한다
- 검색 결과가 공간 본체를 덮어쓰지 않게 한다

잠금 완료 기준:

- 필요한 reference/관측 결과/유사 코드/유사 문서를 회수할 수 있을 것
- 검색은 생성보다 먼저, 참조층으로 작동할 것

---

## 2-8. P3 회사/보안 경계 기준

### 회사 내부 정보 / 개인 공간 / 외부 LLM 분리

이건 실무상 매우 중요하다.

미리 세팅할 것:

- 회사별 파생 공간 또는 project namespace
- 외부 LLM 전송 가능 범위 규칙
- 민감정보 익명화/추상화 규칙
- 내부 코드/문서/메모 저장 레벨 구분
- 개인 장기 공간과 회사 민감 공간의 경계

잠금 완료 기준:

- 새 회사 시나리오에서도 민감정보가 개인 장기 공간/외부 LLM으로 무분별하게 넘어가지 않을 것
- company raw / public abstraction / private synthesis 층이 구분될 것

---

## 2-9. P3 역할 기준

### 의미 위계가 아니라 책임 경계만 먼저 고정

지금 미리 정하면 좋은 역할:

#### ingest

무엇을 받는가:

- raw input
- structured input
- execution trace
- code/reference asset

무엇을 하는가:

- 수신
- 기본 출처/시간/유형 기록

무엇을 하지 않는가:

- 최종 의미 판정
- 승격 결정

#### normalize

무엇을 받는가:

- raw/structured input

무엇을 하는가:

- 축/라벨/앵커/위치값 생성
- version stamp 부여

무엇을 하지 않는가:

- 관측 결과 확정
- reference overwrite

#### record

무엇을 하는가:

- append-only write
- provenance/registry 관리

#### observe

무엇을 하는가:

- 질문 기반 read-only 탐색
- 응결핵 테스트
- observation memory 저장

#### enrich

무엇을 하는가:

- 부족한 연결 보강
- 이유와 출처를 남기며 append

#### render

무엇을 하는가:

- current operation surface 생성
- read-only summary 제공

잠금 완료 기준:

- 누가 받고, 해석하고, 기록하고, 관측하고, 보강하고, 보여주는지 섞이지 않을 것

---

# 3. 지시서 v1

## Codex 실행용 사전 셋업 우선 작업 지시서

이 지시서는 위 선언문/기준문을 실제 작업 순서로 내린 것이다.
목적은 “엔진 잠금 전 바닥 셋업”이다.
새 기능 추가보다 경계/기억/일관성/운영 추적을 우선한다.

---

## 3-1. 절대 원칙

이번 턴의 목적은 다음이 아니다.

- 공간 전체 뷰어 만들기
- 강한 의미 위계 확정
- 객체/군집 자동 승격기 만들기
- full RAG/agent 시스템 구축
- 에이전트 자동 보강 전면 구현

이번 턴의 목적은 오직 아래다.

**엔진 잠금 전 바닥 셋업**

- append safety
- 기억층 분리
- 입력기 calibration 루프
- 코드 reference 자산 포맷
- 운영화면 최소면
- 관측기 계약
- 보안/경계 슬롯 준비

---

## 3-2. 작업 우선순위

### STEP 1. append safety 잠금

Codex는 먼저 아래를 점검/정리하라.

- registry/provenance append 경로 식별
- atomic write 또는 temp write 후 rename 적용 가능 여부 점검
- write race 위험 파일 목록 작성
- job_id/run_id/idempotency key 필드 추가 가능 위치 점검
- malformed tail recovery 전략 문서화

산출물:

- append_safety_review.md
- append_safety_patch_plan.md
- 필요 시 관련 코드 패치

완료 기준:

- 병렬/연속 실행 시 registry/provenance가 깨지지 않도록 최소 패치 방향이 확정될 것

---

### STEP 2. 기억층 분리 스키마/폴더 기준 잠금

Codex는 최소 아래 층을 분리하는 기준 문서를 만들고,
이미 있는 파일/폴더 중 어디가 어떤 층인지 맵핑하라.

분리 대상:

- raw_input_memory
- interpretation_memory
- observation_memory
- reference_memory
- enrichment_memory

산출물:

- memory_layer_separation_map_v1.md
- existing_assets_to_memory_layers_map_v1.md

완료 기준:

- 현재 repo 자산을 어떤 기억층으로 읽어야 하는지 매핑될 것
- raw/interpretation/observation/reference/enrichment 혼선 구간이 식별될 것

---

### STEP 3. 입력기 calibration reference 슬롯 확보

Codex는 입력을 막는 구조를 만들지 말고,
입력기 흔들림 점검용 reference set 저장/비교 자리를 먼저 준비하라.

해야 할 일:

- calibration_reference 폴더/manifest 후보 정의
- reference set에 넣을 문서 유형 정의
- interpreter version stamp 저장 위치 정의
- rerun diff 리포트 형태 제안

산출물:

- input_calibration_reference_policy_v1.md
- interpreter_drift_check_plan_v1.md

완료 기준:

- raw input 자유가 유지되면서도 calibration reference를 별도 유지할 수 있을 것

---

### STEP 4. 코드 reference asset 포맷 고정

Codex는 코드/설계 초안/패치 결과가 나중에 공간 reference로 재투입될 수 있도록 최소 포맷을 정하라.

해야 할 일:

- code_reference_asset schema 초안 작성
- source_type, purpose, problem_context, related_anchor, change_reason 등 필드 잠금
- 기존 코드 산출물 중 reference로 보기 좋은 자산 유형 식별

산출물:

- code_reference_asset_schema_v1.md
- code_reference_ingest_policy_v1.md

완료 기준:

- 코드가 목적/맥락/문제와 연결된 자산으로 읽힐 수 있을 것

---

### STEP 5. read-only 운영화면 최소 스펙 잠금

Codex는 전체 공간 뷰어를 만들지 말고, operation surface 최소 스펙만 문서화하라.

운영화면 최소 항목:

- 질문/지시
- 관련 입력
- 실행 과정
- 예상 시나리오
- 산출물 포인터
- 실패/보류/재시도
- 관련 reference/observation 포인터

산출물:

- operation_surface_min_spec_v1.md
- operation_surface_data_requirements_v1.md

완료 기준:

- “무슨 작업이 진행되었고 무엇이 남았는지”만 추적 가능한 최소면이 정의될 것

---

### STEP 6. 관측기/응결핵 계약 문서화

Codex는 관측기를 본체가 아닌 detachable read-only 부품으로 고정하는 계약을 문서화하라.

포함할 것:

- observation query
- nucleus/probe metadata
- result record format
- confidence/exception handling
- raw overwrite 금지
- interpretation overwrite 금지

산출물:

- observation_probe_contract_v1.md

완료 기준:

- 나중에 응결핵/관측기를 붙여도 공간 본체를 덮어쓰지 않게 할 것

---

### STEP 7. 회사 보안/경계 슬롯 정의

Codex는 회사 시나리오를 고려해 민감 경계 슬롯을 문서화하라.

포함할 것:

- company raw
- company abstracted
- private synthesis
- external llm safe subset
- code sharing boundary
- anonymization rule placeholder

산출물:

- company_space_boundary_policy_v1.md

완료 기준:

- 새 회사 시나리오에서 어떤 레벨의 정보가 어디까지 갈 수 있는지 틀이 마련될 것

---

## 3-3. 하지 말 것

Codex는 이번 턴에 아래를 하지 말 것.

- 공간 전체 시각화 구현
- 클러스터/객체/핵 자동 승격 규칙 확정
- full agent orchestration 구현
- 외부 검색/LLM API 무분별 연결
- 의미 위계 ontology 스타일 고정
- raw input 입력 게이트 강화
- 구조 정리 전에 기능 확장

---

## 3-4. 보고 방식

Codex는 각 단계마다 아래 형식으로 보고하라.

1. 현재 상태
2. 문제점/혼선 지점
3. 최소 수정안
4. 파일/폴더/문서 영향 범위
5. 패치 여부
6. 아직 남은 리스크
7. 다음 단계 추천

---

## 3-5. 최종 완료 상태 정의

이번 사전 셋업 작업이 완료되었다고 볼 수 있는 조건은 다음과 같다.

- append/provenance 경로의 위험 파일이 식별되고 안전화 방향이 확정됨
- 기억층 분리 기준이 문서화됨
- raw input 자유와 calibration reference 분리가 고정됨
- 코드 reference asset 포맷이 정해짐
- read-only 운영화면 최소 스펙이 잠김
- 관측기/응결핵 계약이 문서화됨
- 회사/외부 경계 슬롯이 마련됨

즉 이번 완료는 기능 확장이 아니라,
**나중의 회사 시나리오/프로그램 제작/공간 탐색 루프가 흔들리지 않게 만드는 바닥 셋업 완료**를 뜻한다.

---

# 4. 아주 짧은 압축판

## 선언

공간은 본체로 두고, 입력은 자유롭게 받되, 입력기 일관성과 기록/기억 경계를 먼저 잠근다.

## 기준

먼저 잠글 것은 append safety, 기억층 분리, calibration reference, 코드 reference 포맷, read-only 운영면, 관측 계약, 보안 경계다.

## 지시

Codex는 새 기능보다 바닥 셋업을 먼저 하라. 원본을 덮어쓰지 말고, 경계를 문서화하고, append-only 구조를 먼저 안전화하라.

---

# 5. 최종 한 줄

**지금 엔진을 잠그기 전에 미리 세팅해야 할 것은 더 많은 의미판정기가 아니라, 나중의 회사 관찰-공간 축적-코드 재투입-탐색-수정 루프를 안전하게 굴릴 수 있게 만드는 기억 경계와 운영 바닥이다.**
