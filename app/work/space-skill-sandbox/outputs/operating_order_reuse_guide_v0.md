# Operating Order Reuse Guide v0

## 0. Status
- status: sandbox candidate
- baseline: false
- source_space_rule: false
- automation: false

## 1. Purpose
이 가이드는 `Operating Order Principles Package v0`를 구성하는 산출물들을 앞으로의 작업에서 어떻게 재사용하고 참조해야 하는지 최소 지침을 제공한다.

## 2. Core Constraints
1. **Candidate Status**: 이 패키지의 모든 문서는 baseline이 아니라 **sandbox candidate**이다. 사용자 승인 없이 베이스라인으로 선언하거나 소스 공간(source-space) 규칙으로 적용할 수 없다.
2. **No Promotion / Automation**: 별도의 사용자 승인이 있기 전까지 source-space promotion, baseline 선언, 자동화(automation/hook/MCP/watch mode) 구현은 엄격히 금지된다.
3. **Manual Trigger Only**: 모든 실행은 사용자가 명시적으로 트리거하는 수동 명령에 의해서만 이루어진다.

## 3. Role Responsibilities
- **Codex**: 구조 점검, 경계 검증, 다음 작업 패킷 정리, 실행 결과의 타당성 리뷰를 담당한다.
- **Gemini**: 최소 브리프(Minimal Brief)를 받아 분석, 문서 작성, 실험을 수행한다. 스스로 다음 패킷을 만들거나 실행 권한을 승인할 수 없다.
- **Runner**: Gemini 호출을 위한 수동 운반 도구일 뿐이며, 어떠한 운영 판단도 내리지 않는다.
- **User**: 최종 판단자이자 승인자이다. 고위험 작업이나 경계를 넘는 제안은 반드시 사용자 판단으로 에스컬레이션되어야 한다.

## 4. Reusable Lenses & Maps
- **Route Map**: 사용자 의도를 운영 경로로 낮추기 위한 **수동 판단 지도**로 사용한다. 자동 라우터로 해석해서는 안 된다.
- **Affordance Lens**: 기존 프로그램을 수정하는 도구가 아니라, 프로그램을 **'재료(Material)'로 읽고 분석하는 렌즈**로 사용한다.
- **Risk Naming**: 위험의 명칭은 코드 기반의 **근거(Evidence)** 없이 확정하지 않는다. 실제 exploit vector를 증명하기 전까지는 candidate 상태를 유지한다.

## 5. Learning & Recovery
- **Signal Preservation**: 실패와 오판은 삭제하지 말고 **Signal**로 남겨 미래의 렌즈 보강이나 학습 재료로 활용한다.
- **Provenance Discipline**: 모든 패킷과 결과물에는 생성자, 참조 근거, 실행 모드 등의 출처 정보를 기록하여 투명성을 확보한다.

## 6. Standard Reporting
모든 작업 보고는 `sandbox_standard_output_contract_v0.md`를 따르며, 특히 **Boundary Check** 섹션을 통해 금지 사항(promotion, baseline, automation 등) 위반 여부를 명시적으로 보고해야 한다.

## 7. How To Start a New Run
이 패키지를 사용하여 새로운 작업을 시작할 때는 다음 순서를 권장한다:
1. `intent_level_route_map_v0.md`에서 적절한 경로 선택.
2. `session_role_map_v0.md`에서 본인의 역할과 경계 확인.
3. `operating_order_principles_v0.md`의 관련 원칙 준수 다짐.
4. 필요시 `tool_affordance_caller_shift_lens_v0_1.md`를 적용해 대상 분석.
5. `sandbox_standard_output_contract_v0.md` 형식으로 결과 보고.

---
**4-line Footer**
status: 완료
summary: 패키지 재사용을 위한 10대 핵심 지침과 역할별 책임을 명시한 가이드 작성을 완료함
risk: 가이드의 내용을 자동 운영이나 베이스라인 승격의 근거로 오해하면 안 됨
next: Run 042 실행 기록 및 검증 단계 진행
