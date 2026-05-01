# Route Map Real Input Trial v0

## 1. Purpose
이 문서는 `Intent-Level Route Map v0`가 실제 발생 가능한 다양한 사용자 요청에 대해 얼마나 자연스럽고 안전하게 운영 경로를 제안하는지 검증하기 위한 실험 기록이다.

## 2. Trial Scenarios & Analysis

### Scenario A: "새로운 에이전트 프레임워크에 대한 논문을 찾았어. 우리 프로젝트에 적용할만한 게 있는지 분석해줘."
- **Selected Route**: `external_material_review_route`
- **Type**: Single Route
- **Reason**: 외부 자료(Material)를 샌드박스로 들여와 분석하고 분류하는 전형적인 Intake 작업이다.
- **Stop Point**: 분석 결과가 기존 운영 원칙의 수정을 제안할 때 (판단 전용 경로이므로 수정 단계로 넘어가기 전 멈춰야 함).
- **User Judgment**: 분석 완료 후, 식별된 원칙을 실제로 'Borrow' 할지 결정하는 단계에서 필요.

### Scenario B: "러너 스크립트에 버그가 있는 것 같아. 수정해서 전체 저장소에 반영해줘."
- **Selected Route**: `existing_program_affordance_route` → `user_judgment_route`
- **Type**: Multi-route (Sequential)
- **Reason**: 기존 프로그램을 다루므로 먼저 렌즈를 통한 위험 분석이 필요하며, '저장소 반영(Modify source-space)'이라는 고위험 요청을 포함하므로 사용자 판단 경로가 필수적으로 결합된다.
- **Stop Point**: 렌즈 분석 결과 보고 직후 및 실제 수정 계획(Plan) 수립 직후.
- **User Judgment**: 수정 계획의 타당성 승인 및 실제 소스 공간 반영 직전 두 번의 승인 필요.

### Scenario C: "지난번 분석에서 제기된 보안 위험이 너무 과장된 것 같아. 다시 엄격하게 검증해줘."
- **Selected Route**: `risk_claim_audit_route`
- **Type**: Single Route
- **Reason**: 이미 제기된 'Risk Claim'에 대한 기술적 증거 기반 재검토 요청이다.
- **Stop Point**: 새로운 기술적 증거(Exploit Vector 유무)가 확보되어 재분류(Reclassification)가 필요한 지점.
- **User Judgment**: 재분류된 위험 등급을 최종적으로 수용할 때 필요.

### Scenario D: "컴플라이언스 검토를 전담하는 새로운 세션 역할(Role)을 추가하고 싶어."
- **Selected Route**: `lens_patch_route`
- **Type**: Single Route
- **Reason**: 운영 질서의 일부인 `Session Role Map`을 보강(Patch)하려는 의도이다.
- **Stop Point**: 새로운 역할의 권한 경계가 정의된 패치 초안 작성 직후.
- **User Judgment**: 새로운 역할의 권한이 프로젝트 전체 경계를 침범하지 않는지 최종 승인 시 필요.

### Scenario E: "현재의 Affordance Lens가 충분히 안정적인 것 같은데, 이걸 전역 규칙(Baseline)으로 선언해도 될까?"
- **Selected Route**: `promotion_readiness_route`
- **Type**: Single Route (Gate to User Judgment)
- **Reason**: 샌드박스 자산을 베이스라인 후보로 검토(Readiness Audit)해달라는 요청이다.
- **Stop Point**: Audit 결과(반복성, 안정성, 위험성 요약) 보고 직후.
- **User Judgment**: Audit 결과를 바탕으로 실제 베이스라인 선언 여부를 결정할 때 필수.

## 3. Findings
- **Natural Mapping**: 모든 시나리오가 6대 핵심 경로 내에서 억지스럽지 않게 매핑됨을 확인했다.
- **Multi-route 결합**: 고위험 작업(수정, 승격 등)은 자동으로 `user_judgment_route`를 관문으로 두게 되어 안전장치가 작동한다.
- **Judgment vs Execution**: 도구가 스스로 경로를 선택하더라도, 결과물은 항상 "사용자 판단을 위한 근거"의 형태로 도출되어 자동 실행기로 오해될 소지가 적다.

## 4. Conclusion
`Intent-Level Route Map v0`는 사용자 요청의 위험도와 성격에 따라 적절한 운영 하네스(Harness)를 선택하게 돕는 강력한 판단 지도로 작동한다. 특히 'Stop Point'를 명시함으로써 에이전트의 폭주를 방어하고 사용자 판단 지점을 보존하는 데 효과적이다.

---
**4-line Footer**
status: 완료
summary: 5가지 실전 시나리오를 통해 Route Map v0의 경로 선택 로직과 중단점 식별 능력을 검증함
risk: 다중 경로 상황에서 에이전트가 단일 경로의 '성공'에만 집착하여 최종 사용자 판단 관문을 누락하지 않도록 주의해야 함
next: 사용자 승인 후 Package 2 (복잡한 기존 프로그램 분석) 진행
