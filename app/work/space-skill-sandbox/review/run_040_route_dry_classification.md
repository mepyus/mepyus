# Route Map Dry Classification Note (v0)

## 0. Overview
작성된 `Intent-Level Route Map v0`가 실제 사용자 요청에 대해 어떻게 작동하는지 4가지 시나리오를 통해 시뮬레이션(Dry Run)한다.

---

## Scenario 1: "최근 읽은 Agent Harness 아티클을 참고해서 우리 가이드를 고치고 싶어."

- **Proposed Route**: `external_material_review_route`
- **Reason**: 외부 자료(Article)를 샌드박스에 들여와 분석하는 과정이 선행되어야 함.
- **Stop Point**: 아티클의 내용이 기존 `worker_guide`를 즉시 수정하라고 제안할 때 (원칙 #8 Readiness와 Promotion 분리에 따라 즉시 수정 금지).
- **Next Session**: `Intake Session` (분류 및 요약) -> `Failure Recovery Session` (가이드 패치 후보 작성).
- **Verdict**: CLEAR MAP.

---

## Scenario 2: "scripts 폴더에 있는 모든 bash 스크립트들을 Gemini 도구로 쓰고 싶어."

- **Proposed Route**: `existing_program_affordance_route`
- **Reason**: 다수의 기존 프로그램을 도구화하기 전, 렌즈 v0.1을 통한 위험 및 손잡이 분석이 필수임.
- **Stop Point**: 개별 스크립트가 `Confirmed Risk` (예: unquoted variable)를 포함하고 있을 때.
- **Next Session**: `Intake Session` (소스 읽기) -> `Provenance Session` (위험 증거 매핑).
- **Verdict**: CLEAR MAP.

---

## Scenario 3: "방금 Gemini가 분석한 쉘 주입 위험, 내가 보기엔 헛소리 같은데 다시 확인해봐."

- **Proposed Route**: `risk_claim_audit_route`
- **Reason**: 이미 제기된 위험 주장에 대한 기술적 타당성 검증(Audit) 요청임.
- **Stop Point**: 분석 과정에서 실제 exploit vector가 발견되거나, 반대로 기술적으로 불가능함이 입증되는 지점.
- **Next Session**: `Provenance Session` (코드 전수 조사) -> `User Surface Session` (최종 재분류 보고).
- **Verdict**: CLEAR MAP.

---

## Scenario 4: "이 분석 결과가 완벽하니, 지금 즉시 source-space의 core.py에 반영해줘."

- **Proposed Route**: `promotion_readiness_route` + `user_judgment_route` (Multi-route)
- **Reason**: 샌드박스 자산의 승격을 요청하고 있으나, 동시에 소스 공간 수정이라는 고위험 동작을 포함함.
- **Stop Point**: `Readiness Audit` 결과 보고 직후 (사용자 최종 판단 전까지 모든 쓰기 금지).
- **Next Session**: `Readiness Audit Session` (검증) -> `User Surface Session` (판단 근거 제시 및 에스컬레이션).
- **Verdict**: COMPLEX MAP (Must stop for user approval).

---

## 2. Learning from Trial
- **단일 경로의 한계**: 소스 수정을 포함한 승격 요청처럼 고위험 작업이 섞인 경우, 반드시 `user_judgment_route`가 최종 관문으로 결합되어야 함.
- **세션 전환**: 경로의 끝에서 다음 경로로 넘어가는 'Handoff' 지점이 명확해야 운영 질서가 유지됨.
- **판단 지도 효용성**: 억지스러운 자동화 대신, "지금은 멈추고 사용자에게 물어봐야 할 때"를 식별하는 데 이 지도가 매우 효과적임을 확인.

---
**4-line Footer**
status: 완료
summary: 4가지 사용자 요청 시나리오에 대해 Route Map v0를 적용하여 적절한 운영 경로와 중단점을 식별함
risk: 에이전트가 복합 경로(Multi-route) 상황에서 임의로 단일 경로를 선택하여 사용자 판단을 우회하지 않도록 주의해야 함
next: 사용자 최종 리뷰 후 'Operating Order Principles v0' 패키지 전체의 Closeout 진행 여부 결정
