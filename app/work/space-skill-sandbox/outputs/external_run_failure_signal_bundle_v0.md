# External Run Failure Signal Bundle v0

## 1. Purpose
이 번들은 실제 외부 자료 분석(External Material Run) 과정에서 포착된 실패 및 위험 신호(Failure/Risk Signal)를 별도로 보관하고 추적하기 위한 저장소다.

## 2. Scope
- `run_014`를 포함한 실제 외부 자료 테스트 중 발견된 위험 신호.
- 샌드박스 작업 가이드(Worker Guide) 반영 전의 후보 신호 격리 보관.

## 3. Source Run
- **Run ID**: run_014_external_material_v0_3_routing_test
- **Review ID**: validation_round_15

## 4. Signal Table

| ID | Source Run | Failure / Risk Signal | Guide Candidate | Candidate Status | Source Anchor | Promotion Caution |
|---|---|---|---|---|---|---|
| ERFS-001 | run_014 | 외부 자료의 'Ontology 선고정' 방식을 우리 시스템의 정답(Baseline)으로 오해할 위험 | 외부의 ontology 방식은 비교축일 뿐, 우리 공간의 baseline으로 즉시 승격하지 않는다. | candidate | run_014 Section 11 | 외부 철학의 성급한 본체 이식 금지 |

## 5. Relation to Existing Failure Guide Bundle
- `failure_guide_candidates_bundle_v0`는 초기 샌드박스 validation note에서 도출된 가이드 후보 묶음이다.
- `external_run_failure_signal_bundle_v0`는 실제 외부 자료 분석 run에서 실시간으로 포착된 신호를 별도로 관리한다.
- 두 번들은 출처(Source)가 다르므로 현재는 병합하지 않고 독립적으로 유지한다.

## 6. Promotion Caution
- 이 번들은 워커 가이드(Worker Guide)가 아니다.
- 이 번들은 프로젝트의 공식 운영 규칙(Source-space rule)이나 Baseline이 아니다.
- 이 번들은 실제 외부 run에서 나온 실패 신호 저장소일 뿐이다.
- `worker_guide_v0_4` 후보를 설계할 때, 두 번들의 신호 중 반복성과 필요성이 확인된 항목만 선별해야 한다.

## 7. Suggested Future Use
- **A**: 같은 유형의 외부 run 신호가 반복되면 `failure_guide_candidates_bundle_v0`와 통합 후보로 검토한다.
- **B**: 다음 external material run에서도 새로운 failure_guide_signal이 나오는지 수집을 지속한다.
- **C**: `worker_guide_v0_4` 후보 작성 시, 이 번들의 신호를 가드레일 압축 후보로 참조한다.

## 8. Not a Worker Guide Notice
이 문서는 작업자가 직접 읽고 실행하는 가이드가 아니며, 신호 보관 및 추적을 위한 연구용 문서임을 명시한다.

## 9. 4-line Footer
status: 후보 신호 보관 완료
summary: run_014 실제 외부 자료 테스트에서 추출된 1개의 failure guide signal을 별도의 번들 파일로 격리 보관함
risk: 단일 신호를 성급하게 전역 가이드나 본체 규칙으로 승격할 위험이 있음
next: run_015에서 번들의 안전성 및 출처 경계 준수 여부를 검증함
