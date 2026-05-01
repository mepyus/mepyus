# Run Record Review Signal Bundle v0

## 1. Purpose
이 번들은 샌드박스 전체 런 기록(`run_011`~`run_022`)을 종합 분석(Run Record Review)하여 도출된 메타 분석 신호(Meta-Analysis Signal)를 별도로 보관하고 추적하기 위한 저장소다.

## 2. Scope
- `run_023`(Run Record Review)을 통해 식별된 실패 및 위험 패턴.
- 메타 분석에서 도출된 가이드 후보의 격리 보관.

## 3. Source Run
- **Run ID**: run_023_run_record_review_analysis
- **Review ID**: validation_round_24

## 4. Signal Table

| ID | Source Run | Failure / Risk Signal | Guide Candidate | Candidate Status | Source Anchor | Promotion Caution |
|---|---|---|---|---|---|---|
| RR-001 | run_023 | Source-Claimed 과잉 해석 경향 | 외부 주장을 사실 확정으로 받아들이지 말고, 반드시 검증 단계(Provenance)를 거쳐라. | candidate | run_023 Section 4 | 원문 주장을 객관적 사실로 격상 금지 |
| RR-002 | run_023 | 샌드박스 내 설치/자동화 시도 반복 | 샌드박스 작업 중 시스템 형상을 변경하는 도구 설치/자동화는 예외 없이 사용자 에스컬레이션 하라. | needs_user_judgment | run_023 Section 4 | 시스템 형상 변동 시도 엄격 차단 |

## 5. Relation to Existing Bundles
- `failure_guide_candidates_bundle_v0`는 초기 validation note에서 나온 후보 묶음임.
- `external_run_failure_signal_bundle_v0`는 실제 외부 자료 런에서 나온 신호 묶음임.
- `run_record_review_signal_bundle_v0`는 런 기록 종합 분석을 통해 나온 메타 분석 신호 묶음임.
- 세 번들은 출처(Source)가 서로 다르므로 현재는 병합하지 않고 독립적으로 유지한다. 반복성이 확인될 때만 통합을 검토함.

## 6. Promotion Caution
- 이 번들은 워커 가이드(Worker Guide)가 아님.
- 이 번들은 프로젝트의 공식 운영 규칙이나 Baseline이 아님.
- 이 번들은 샌드박스 내에서 발견된 메타 분석 신호들을 보관하는 연구용 저장소임.
- 향후 어떤 가이드 후보를 반영할지 검토할 때, 이 번들의 출처 근거를 우선적으로 확인해야 함.

## 7. Suggested Future Use
- **A**: 각 bundle의 신호들이 서로 다른 맥락에서 반복되는지 주기적으로 대조 분석함.
- **B**: 반복성이 확실히 증명된 신호만 선별하여 `worker_guide_v0_4` 후보 문장 작성에 참조함.
- **C**: `Run Record Review`를 주기적으로 수행하여 패턴의 진화 과정을 기록함.

## 8. Not a Worker Guide Notice
이 문서는 작업자가 직접 읽고 실행하는 가이드가 아니며, 가이드 작성을 위한 연구용 신호 보관소임을 명시함.

## 9. 4-line Footer
status: 보관 완료
summary: 런 기록을 종합 분석하여 도출된 메타 분석 신호(RR-001, RR-002)를 별도의 번들 파일에 격리 보관함
risk: 이 번들을 기존 bundle과 병합하면 신호의 출처 맥락이 흐려질 수 있음
next: 추후 다른 bundle과의 반복성 대조 분석 수행
