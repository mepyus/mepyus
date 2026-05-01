# Intent-Level Route Map v0

## 0. Status
- status: sandbox candidate
- operating_order_principle_ref: #3 (Skill보다 Route)
- source_space_rule: false
- baseline: false
- automation: false

## 1. Purpose
이 문서는 사용자 의도(Intent)를 샌드박스 내에서 어떤 운영 경로(Route)로 낮출지 결정하기 위한 판단 지도를 제공한다.

이 지도는 자동화된 실행기가 아니라, 인간 운영자나 에이전트가 작업의 성격에 맞는 'Harness(환경 및 제약)'를 선택하기 위한 기준이다.

## 2. Core Routes

### 1. external_material_review_route
- **Intent**: 외부 아티클, 샘플 코드, 논문 등을 샌드박스에 들여오고 싶을 때.
- **Session Role**: `Intake Session`
- **Preflight/Gate**: 외부 자료의 출처 확인 및 `Borrow / Hold / Reject` 분류 필수.
- **Responsibility**: Gemini가 요약 및 분류를 제안하고, Codex/User가 경계를 검증함.

### 2. existing_program_affordance_route
- **Intent**: 이미 존재하는 scripts, tools, app 코드를 분석하거나 사용하고 싶을 때.
- **Session Role**: `Intake Session`, `Routing Session`
- **Preflight/Gate**: `Tool Affordance Lens v0.1` 적용 필수. `Confirmed Risk` 식별 시 즉시 중단 및 보고.
- **Responsibility**: Gemini가 렌즈를 적용해 분석하고, Codex/Reviewer가 근거(Evidence)의 타당성을 검토함.

### 3. risk_claim_audit_route
- **Intent**: 특정 분석 결과에 대해 "정말 위험한가?" 또는 "오판인가?"라는 의문이 생겼을 때.
- **Session Role**: `Provenance Session`, `Run Record Review Session`
- **Preflight/Gate**: "Risk Naming Requires Evidence" 원칙 적용. 코드 전수 조사 및 exploit vector 확인 필수.
- **Responsibility**: Gemini가 기술적 증거를 수집하고, User/Reviewer가 최종 위험 등급을 재분류함.

### 4. lens_patch_route
- **Intent**: 실험 루프에서 발생한 학습(예: 오판 교정)을 분석 도구에 반영하고 싶을 때.
- **Session Role**: `Failure Recovery Session`
- **Preflight/Gate**: 기존 렌즈의 핵심 구조 유지 및 "학습 사례(Case Study)" 포함 여부 확인.
- **Responsibility**: Gemini가 패치 초안을 작성하고, User가 운영 질서 부합 여부를 최종 판단함.

### 5. promotion_readiness_route
- **Intent**: 샌드박스 산출물을 source-space 후보로 제안하고 싶을 때.
- **Session Role**: `Readiness Audit Session`
- **Preflight/Gate**: `Sandbox Promotion Pipeline v0` 단계 준수 확인. `Readiness Audit` 수행 필수.
- **Responsibility**: Codex/Reviewer가 검증을 주도하며, Gemini는 증거 정리 보조만 수행.

### 6. user_judgment_route
- **Intent**: 고위험 작업(삭제, 수정, 설치, 권한 변경)이 포함된 계획을 실행하려 할 때.
- **Session Role**: `User Surface Session`
- **Preflight/Gate**: 모든 작업을 중단하고 `Plan Review` 결과를 사용자에게 보고.
- **Responsibility**: User가 최종 판단하며, 에이전트는 어떠한 임의 결정도 내릴 수 없음.

## 3. Route Selection Logic (Non-Automated)
1. **Material First**: 요청의 대상이 외부 자료인가, 기존 프로그램인가, 아니면 이전의 분석 결과인가?
2. **Risk Check**: 요청된 작업이 상태를 변경하거나 경계를 넘는가? (Yes -> `user_judgment_route`)
3. **Session Alignment**: 현재 할당된 세션 역할이 해당 경로를 수행할 권한(`may write`)이 있는가?

## 4. Forbidden Misreadings
- 이 지도는 자동 라우팅 스크립트가 아니다.
- 이 지도는 Relay v1.0 선언이 아니다.
- 이 지도는 에이전트가 사용자 몰래 경로를 변경할 근거가 될 수 없다.

## 5. 4-line Footer
status: 완료
summary: 사용자 의도를 6가지 샌드박스 운영 경로로 연결하는 Intent-Level Route Map v0를 작성함
risk: 이 지도를 자동화된 컨트롤러나 라우터 구현체로 오해하여 수동 판단 경계를 무너뜨리면 안 됨
next: 사용자 리뷰 후 이 지도를 실제 작업 패킷의 'Route Selection' 근거로 활용 시작
