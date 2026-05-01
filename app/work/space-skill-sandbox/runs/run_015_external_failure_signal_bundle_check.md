# run_015_external_failure_signal_bundle_check

## 1. Run Declaration
`external_run_failure_signal_bundle_v0.md`가 `run_014`에서 발생한 1개의 실패 신호를 안전하게 후보 상태로 보관했는지, 그리고 출처 경계를 준수했는지 수동으로 검증함.

## 2. Input Files
- `outputs/external_run_failure_signal_bundle_v0.md`
- `runs/run_014_external_material_v0_3_routing_test.md`
- `outputs/failure_guide_candidates_bundle_v0.md`

## 3. Bundle File Checked
- **ID 부여**: ERFS-001 고유 ID가 부여됨.
- **Source Anchor**: `run_014` Section 11이 근거로 명시됨.
- **Candidate Status**: 'candidate' 상태로 격리 보관됨.

## 4. Signal Count Check
- `run_014`에서 식별된 1개의 신호가 누락 없이 기록됨 (1/1).

## 5. Source Boundary Check
- 기존 `failure_guide_candidates_bundle_v0`와 병합되지 않고 독립된 파일로 생성됨.
- 출처(Source)의 차이가 명확히 기술됨.

## 6. Promotion Drift Check
- `worker_guide_v0_3_candidate.md`를 수정하지 않음.
- `worker_guide_v0_4`를 생성하지 않음.
- 신호가 '규칙'이 아닌 '후보 신호'로 유지됨.

## 7. Risk Check
- **Risk**: 외부 자료 1개의 신호가 성급하게 전역적인 가드레일로 승격될 위험.
- **Mitigation**: Promotion Caution 섹션을 통해 '반복성 확인 전까지 선별 금지' 지침을 명시함.

## 8. 4-line Footer
status: 검증 필요
summary: run_014 실제 외부 자료 테스트에서 나온 failure guide signal 1개를 별도 bundle 후보로 보관했는지 확인함
risk: 외부 run에서 나온 단일 signal을 worker guide나 source-space rule로 과잉 반영할 수 있음
next: validation_round_16에서 기존 bundle과 병합되지 않았는지, promotion drift가 없는지 검증
