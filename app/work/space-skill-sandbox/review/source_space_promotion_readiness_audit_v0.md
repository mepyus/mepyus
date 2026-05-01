# Source-space Promotion Readiness Audit v0

## 1. Purpose
Space Skill Sandbox에서 검증된 Relay, Worker Guide, Skill 후보, Signal Bundle들이 source-space(본체)로 이식될 후보가 될 수 있는지, 아니면 샌드박스 내에서만 유지되어야 하는지 점검함.

## 2. Audit Method
- **평가 기준**: 반복성(Repeatability), 경계 유지(Boundary), 사용자 부담 감소(Usability), 과잉 일반화 위험(Overgeneralization).
- **분류**: 
  - `promotion_candidate_later`: 이식 후보.
  - `sandbox_keep`: 샌드박스 전용 유지.
  - `needs_more_runs`: 추가 검증 필요.
  - `user_judgment_required`: 사용자 판단 필요.
  - `reject_for_now`: 현재 이식 불가.

## 3. Asset Readiness Table

| Asset | Current Status | Evidence | Readiness | Risk if Promoted Too Early | Recommended Next |
|---|---|---|---|---|---|
| external-material-intake skill | candidate | 런 기록 2회 이상 | promotion_candidate_later | 외부 환경 의존성 오해 | 사용자 판단 후 이식 |
| preflight-guard skill | candidate | stop point 감지 능력 | promotion_candidate_later | 시스템 경직성 증가 | 가이드 문장 고도화 |
| structured-footer skill | candidate | footer 반환 성공 | promotion_candidate_later | 완료가 승인으로 오해됨 | Convention 반영 |
| graph-layer-evaluation skill | candidate |Provenance 분류 확인 | needs_more_runs | 그래프 결과의 절대적 신뢰 위험 | Provenance 기준 정립 |
| failure-to-guide skill | candidate | 실패 신호 회수 성공 | sandbox_keep | 실패를 규칙으로 굳힐 위험 | Bundle 누적 확인 |
| worker_guide_v0_3_candidate | sandbox candidate | 55줄 라우팅 검증 | promotion_candidate_later | 후보가 baseline으로 오해됨 | 릴레이 방식 고도화 |
| Sandbox Relay v0 | sandbox candidate | 파일 기반 flow 작동 | promotion_candidate_later | 자동화로 성급한 이행 | 템플릿 정교화 |
| Compact Relay v0.1b | sandbox candidate | 6개/8개 섹션 최적화 | promotion_candidate_later | 템플릿 부족으로 검증 누락 | 필수값 검증 보강 |
| Mini Graph Provenance Format | sandbox candidate | Provenance 분류 실습 | needs_more_runs | 샌드박스 탐색용을 스키마로 오해 | 표준 taxonomic 분류 |
| failure_guide_candidates_bundle_v0 | signal bundle | 신호 7개 보관 | sandbox_keep | 규칙으로의 성급한 승격 | 정기적 검토 |
| external_run_failure_signal_bundle_v0 | signal bundle | 신호 1개 보관 | sandbox_keep | 맥락 없는 규칙화 | 정기적 검토 |
| run_record_review_signal_bundle_v0 | signal bundle | 신호 2개 보관 | sandbox_keep | 메타 분석의 과잉 해석 | 정기적 검토 |
| signal_bundle_cross_review_matrix_v0 | review matrix | 매트릭스 분류 완료 | sandbox_keep | 병합에 따른 정보 혼선 | 관찰 지속 |

## 4. Source-space Interface Candidates
| Candidate | Why Useful | Required Evidence Before Promotion | User Judgment Needed |
|---|---|---|---|
| 4-line footer convention | 결과 요약 표준화 | 반복 성공 사례 누적 | yes |
| preflight-guard stop point language | 자동화 차단 방어막 | 설치 요구 시 실제 사례 | yes |
| file-based relay concept | 수동 복붙 병목 제거 | 장기 운영 안정성 검증 | yes |
| provenance label caution | 해석과 사실의 분리 | 신호 해석 시 발생 오해 데이터 | yes |
| failure signal bundle separation | 정보 원천의 맥락 보존 | 출처별 반복 신호 통계 | yes |

## 5. Sandbox-only Assets
- **전체 템플릿 전문(worker guide, relay prompt)**: 샌드박스 내부의 실험적 구조이며, 그대로 옮길 경우 본체 기준과 충돌함.
- **Signal Bundle 전체**: 연구용 보관소이며, 정식 문서화 시 재분류가 필요함.
- **Graph Evaluation 전체 구조**: 탐색 보조용이며 스키마/baseline이 아님.

## 6. User Judgment Boundaries
- 모든 후보 자산은 샌드박스에서 검증된 상태로 남겨두며, 정식 문서 반영은 사용자 판단이 필요함.

## 7. Recommended Next Steps
- **A. Compact Template 누락 보완**: `result_template_v0_1b_compact_checklist`에 누락된 검증값을 강제하는 새 후보를 작성.
- **B. 주기적 Signal Bundle 통합 검토**: 3개의 번들을 주기적으로 재검토하여 반복 신호 발견 시 승격 제안.
- **C. Relay v0.1b 정식 후보 운영**: 현 상태 유지하며 추가 Run 시도.

## 8. 4-line footer
status: 완료
summary: 샌드박스 자산들의 source-space 이식 가능성을 감사하고, 후보군과 보류군을 분리함
risk: 이식 후보를 성급하게 정식 문서로 반영하면 candidate/rule 경계가 붕괴될 수 있음
next: 사용자 검토 후 외부 자료 추가 테스트를 통해 릴레이 흐름 재검증
