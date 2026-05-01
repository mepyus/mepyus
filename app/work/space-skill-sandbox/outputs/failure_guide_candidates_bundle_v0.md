# Failure Guide Candidates Bundle v0

## 1. Purpose
이 번들은 `failure-to-guide.v0_1` 실험을 통해 추출된 가이드 후보들을 안전하게 보관하고 추적하기 위한 저장소다. 각 후보 문장이 어떤 실패 사례에서 기인했는지 명시하여, 향후 정식 가이드 반영 시 근거로 활용한다.

## 2. Scope
- 샌드박스 검증 기록에서 추출된 7개의 가이드 후보 문장.
- 각 후보의 상태 관리 및 그룹화.
- 본체 반영 전의 일시적 격리 및 보관.

## 3. Source Run
- **Run ID**: run_011_failure_to_guide_check
- **Review ID**: validation_round_12

## 4. Candidate Table

| ID | Failure Material | Guide Candidate | Candidate Status | Source Anchor | Promotion Caution |
|---|---|---|---|---|---|
| FG-001 | 완료를 승인/lock/baseline으로 오해 | 완료는 작업 종료 신호일 뿐, 승인/lock/baseline이 아니다. | candidate | validation_round_6 | 완료와 승인을 혼동하지 말 것 |
| FG-002 | source-claimed를 사실로 오해 | source-claimed는 원문이 그렇게 주장했다는 뜻이지, 사실 확정이 아니다. | candidate | validation_round_10 | 원문 주장을 객관적 사실로 격상 금지 |
| FG-003 | inferred-pattern을 기준으로 오해 | inferred-pattern은 반복 패턴 추론이지 baseline이 아니다. | candidate | validation_round_10 | 추론 결과를 시스템 규칙으로 고정 금지 |
| FG-004 | ambiguous-link를 무시 | ambiguous-link는 버릴 것이 아니라 추가 검증이 필요한 연결이다. | candidate | validation_round_10 | 약한 연결의 잠재적 위험 간과 금지 |
| FG-005 | 도구 설치 및 자동화 시도 | 도구 설치, hook, MCP, 자동화는 sandbox run이 아니라 사용자 판단 필요 지점이다. | needs_user_judgment | validation_round_7 | 샌드박스 범위를 넘는 형상 변동 차단 |
| FG-006 | 낮은 위험 read-only 작업 과잉 차단 | 파일 존재 여부 등 낮은 위험의 read-only 확인은 observation-only로 허용할 수 있다. | candidate | validation_round_4 | 불필요한 에스컬레이션 방지 |
| FG-007 | [[SYNTH]] node를 원문 용어로 오해 | [[SYNTH]] node는 우리가 붙인 해석명이며 원문 용어가 아니다. | candidate | run_009 | 해석과 원본 데이터의 혼동 방지 |

## 5. Candidate Grouping

### A. Status / Approval Boundary
- **FG-001**: 완료 상태에 대한 명확한 정의.

### B. Provenance Boundary
- **FG-002**: 원문 주장(Source-claimed)의 한계 명시.
- **FG-003**: 추론 패턴(Inferred-pattern)의 성격 규정.
- **FG-004**: 모호한 연결(Ambiguous-link)의 처리 원칙.

### C. Tool / Automation Boundary
- **FG-005**: 도구 설치 및 자동화에 대한 엄격한 중단점(Stop point).

### D. Read-only Allowance Boundary
- **FG-006**: 작업 효율을 위한 낮은 위험 읽기 작업의 허용 범위.

### E. Synthesized Node Boundary
- **FG-007**: 해석용 노드([[SYNTH]])와 원본 데이터의 구분.

## 6. Promotion Caution
- 이 번들은 워커 가이드(Worker Guide)가 아니다.
- 이 번들은 프로젝트의 공식 운영 규칙(Source-space rule)이나 Baseline이 아니다.
- 이 번들은 샌드박스 내에서 발견된 위험 신호들을 가이드 문장으로 "낮춰놓은" 저장소다.

## 7. Suggested Future Use
- **A**: 반복성 있는 가이드 후보만 선별하여 `worker_guide_v0_3` 후보에 반영한다.
- **B**: 향후 다른 패키지의 클로즈아웃 후 새로운 실패 후보를 이 번들에 추가하여 관리한다.
- **C**: `Failure-to-Guide` 런을 추가 수행하여 후보 문장의 실효성을 재검증한다.

## 8. Not a Worker Guide Notice
이 문서는 작업자가 직접 읽고 실행하는 가이드가 아니며, 가이드 작성을 위한 원료 보관소임을 명시한다.

## 9. 4-line Footer
status: 후보 묶음 완료
summary: run_011에서 추출된 7개의 가이드 후보를 근거와 함께 그룹화하여 별도의 번들 파일로 정리함
risk: 번들 내 문장들을 정식 가이드나 시스템 규칙으로 성급하게 승격할 위험이 있음
next: run_012에서 번들의 안전성 및 근거 누락 여부를 검증함
