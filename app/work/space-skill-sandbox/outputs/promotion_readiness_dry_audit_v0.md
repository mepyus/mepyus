# Promotion Readiness Dry Audit v0

## 0. Status
- status: sandbox candidate
- operating_order_principle_ref: #8 (Readiness와 Promotion 분리)
- source_space_rule: false
- baseline: false
- promotion_executed: false

## 1. Purpose
이 문서는 현재 샌드박스(app/work/space-skill-sandbox)에서 생성된 산출물들이 실제 소스 공간(source-space)의 인터페이스 후보(`source-space interface candidate`)로 승격될 준비가 되었는지 드라이 오디트(Dry Audit)한 기록이다.

실제 승격은 수행하지 않으며, 오직 '준비도'만을 측정한다.

---

## 2. Audit Targets

### Target 1: Tool Affordance Lens v0.1
- **반복 사용 근거**: Run 034(Runner 분석), Run 037(Indexer 분석), Run 045(Sync 도구 분석)를 통해 3회 이상 실제 프로그램 분석에 적용되어 위험 식별 및 오판 교정 능력을 증명함.
- **샌드박스 잔류 사유**: 아직 DB 연동이나 네트워크 호출이 포함된 '초고위험 도구'에 대한 분석 사례가 부족함. 렌즈의 보편성을 더 확인해야 함.
- **Interface Candidate 가능성**: **HIGH**. 이미 `v0.1` 패치를 통해 '근거 기반 명명' 원칙을 갖추었으므로, 소스 공간의 `scripts/` 분석 가이드 후보로 손색없음.
- **Promotion Stop Point**: 소스 공간의 기존 `README.md`나 `CONTRIBUTING.md`를 직접 수정하려 할 때 멈춰야 함.
- **User Judgment**: 실제 소스 공간의 '공식 분석 절차'로 채택할 때 최종 승인 필요.

### Target 2: Intent-Level Route Map v0
- **반복 사용 근거**: Run 040(Dry Classification)과 Run 044(Real Input Trial)를 통해 사용자 의도를 안전한 운영 경로로 매핑하는 논리적 정당성을 2회 이상 검증함.
- **샌드박스 잔류 사유**: 경로 선택 과정에서 에이전트 간의 '세션 전환(Handoff)'이 실제 물리적 파일 쓰기 없이 시뮬레이션으로만 이루어짐. 실제 루프에서의 안정성 확인 필요.
- **Interface Candidate 가능성**: **MEDIUM**. 운영 '좌표계'로서의 가치는 높으나, 실제 소스 공간의 `RUNLOG`나 `control/` 계층과 직접 연결되기에는 아직 구조가 샌드박스 지향적임.
- **Promotion Stop Point**: 자동 라우팅 스크립트로 구현되어 시스템 제어권을 가져가려 할 때 멈춰야 함.
- **User Judgment**: 이 지도를 기반으로 실제 작업 패킷의 '표준 경로'를 강제할 때 필요.

### Target 3: Minimal Brief Discipline v0
- **반복 사용 근거**: Run 044 이후의 모든 Package 브리프 작성 시 이 원칙(5대 항목 제한 등)을 적용하여 도구의 판단 공간을 성공적으로 확보함.
- **샌드박스 잔류 사유**: 감독자(Supervisor)가 지시를 내리는 방식에 대한 규약이므로, 더 많은 '감독자 변화' 시나리오에서 지속 가능성을 봐야 함.
- **Interface Candidate 가능성**: **HIGH**. 협업 규약(Convention)으로서 매우 명확하며, 소스 공간의 `PROMPT_GUIDE` 후보로 즉시 활용 가능함.
- **Promotion Stop Point**: 모든 자유 양식의 요청을 차단하고 오직 5개 항목만 받도록 시스템적으로 제한(Schema 강제)하려 할 때 멈춰야 함.
- **User Judgment**: 팀 전체의 '프롬프트 표준'으로 승격할 때 최종 승인 필요.

---

## 3. Overall Findings
- **Readiness vs Promotion**: 모든 대상이 높은 '준비도'를 보이고 있으나, 'Readiness와 Promotion 분리' 원칙에 따라 샌드박스 내에서 변동성(Edge Cases)을 더 흡수해야 함.
- **Interface Candidate Definition**: 이제 위 3개 자산은 단순 sandbox candidate를 넘어 **source-space interface candidate**로 호칭할 수 있는 자격을 갖춘 것으로 판단됨.

## 4. 4-line Footer
status: 완료
summary: 3개 샌드박스 자산(Lens, Route Map, Minimal Brief)에 대해 승격 준비도를 오디트하고 '인터페이스 후보' 자격을 부여함
risk: '인터페이스 후보' 자격 부여가 실제 소스 공간 수정을 허용하는 '승격(Promotion)'으로 오해받지 않도록 주의해야 함
next: 사용자 판단 후 실제 소스 공간 인터페이스 지점(예: docs/guides)에 후보 문서를 노출하는 실험 진행
