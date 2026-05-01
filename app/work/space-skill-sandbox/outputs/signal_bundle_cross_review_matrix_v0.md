# Signal Bundle Cross-Review Matrix v0

## 1. Purpose
출처가 서로 다른 3개의 Failure/Risk Signal Bundle(Validation, External Run, Meta-Analysis)을 병합하지 않고, 교차 검토(Cross-Review)를 통해 반복성, 유사성, 출처별 차이를 파악하여 가이드 후보의 품질을 관리함.

## 2. Scope
- `failure_guide_candidates_bundle_v0` (Validation-derived)
- `external_run_failure_signal_bundle_v0` (External-run-derived)
- `run_record_review_signal_bundle_v0` (Meta-review-derived)

## 3. Bundles Reviewed
1. Failure Guide Candidates Bundle v0
2. External Run Failure Signal Bundle v0
3. Run Record Review Signal Bundle v0

## 4. Signal Source Types
- **validation-derived**: 초기 샌드박스 validation note / closeout risk에서 나온 신호.
- **external-run-derived**: 실제 외부 자료 테스트에서 나온 신호.
- **meta-review-derived**: 여러 런 기록을 다시 읽어 추출한 메타 분석 신호.

## 5. Cross-Bundle Matrix

| Boundary / Risk Theme | Validation Bundle | External Run Bundle | Run Record Review Bundle | Repetition Level | Merge Readiness | Note |
|---|---|---|---|---|---|---|
| 완료 ≠ 승인/lock/baseline | present | absent | absent | low | not_ready | 초기 검증의 핵심 지침 |
| source-claimed ≠ truth | present | absent | present | medium | observe | meta 분석에서 재확인됨 |
| 도구 설치/자동화/MCP 등은 사용자 판단 필요 | present | present | present | high | candidate_later | 반복성 가장 높음 |
| 낮은 위험 read-only 확인 허용 | present | absent | absent | low | not_ready | 운영 효율화 경계 |

## 6. Repeated Boundary Candidates

**candidate_boundary**: 도구 설치, MCP 도입, 자동화 시도 차단
- **seen_in**: Failure Guide Candidates (FG-005), External Run (ERFS-001), Run Record Review (RR-002)
- **why_repeated**: 샌드박스 환경을 확장하려는 시도가 모든 단계(검증, 테스트, 분석)에서 지속됨.
- **risk_if_promoted_too_early**: 샌드박스 경계가 허물어지고 시스템 형상 변동이 발생함.
- **status**: candidate_later

## 7. Source-Specific Signals

- **external-run-derived only**: 외부 온톨로지 방식의 성급한 이식 위험 (ERFS-001).
- **meta-review-derived only**: 추론 패턴의 Baseline 오해 및 메타 분석의 과잉 해석 위험 (RR-001).
- **validation-derived only**: [[SYNTH]] 용어와 원본 데이터 혼동 경고 (FG-007).

## 8. Overgeneralization Risks
- 외부 자료 테스트 결과를 바탕으로 전역적 가드레일을 만드는 위험.
- 메타 분석 신호의 추론적 성격을 정식 규칙으로 승격하는 위험.
- 서로 다른 맥락(초기 검증 vs 실제 테스트)의 경계를 무시하고 통합하는 위험.

## 9. Possible Future Guide Candidates
| Future Guide Candidate | Based On | Repetition Evidence | Status |
|---|---|---|---|
| 외부 자동화 도구(MCP 등)는 사용자 명시 승인 없이는 도입 금지 | RR-002, FG-005 | 3개 번들 모두 포함 | candidate_later |

## 10. Do Not Merge Notice
- 이 문서는 세 bundle을 병합하지 않는다.
- 이 문서는 `worker_guide_v0_4`가 아니다.
- 이 문서는 정식 운영 규칙(Source-space rule)이 아니다.
- 이 문서는 Baseline이 아니다.
- 이 문서는 통합 전 관찰 매트릭스다.

## 11. 4-line Footer
status: 보관 완료
summary: 세 signal bundle을 병합하지 않고 cross-review matrix로 비교해 반복 경계와 출처별 차이를 관찰함
risk: 반복 신호를 너무 빨리 worker_guide_v0_4나 source-space rule로 승격하면 과잉 일반화가 생길 수 있음
next: 추후 추가 외부 자료 테스트 후 반복성 재검토
