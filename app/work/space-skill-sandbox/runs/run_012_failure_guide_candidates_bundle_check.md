# run_012_failure_guide_candidates_bundle_check

## 1. Run Declaration
`failure_guide_candidates_bundle_v0.md`가 이전 실험에서 도출된 7개의 가이드 후보를 누락 없이 안전하게 보관하고 있는지, 그리고 워커 가이드나 본체 기준으로 오염되지 않았는지 수동으로 검증함.

## 2. Input Files
- app/work/space-skill-sandbox/outputs/failure_guide_candidates_bundle_v0.md
- app/work/space-skill-sandbox/runs/run_011_failure_to_guide_check.md

## 3. Bundle File Checked
- **ID 부여**: FG-001 ~ FG-007까지 고유 ID가 부여됨.
- **Source Anchor**: 각 후보 문장마다 근거가 되는 검증 회차(validation_round_*)가 명시됨.
- **Promotion Caution**: 본체 기준이나 가이드가 아님을 명확히 경고함.

## 4. Candidate Count Check
- `run_011`에서 생성된 7개의 후보가 모두 포함되었음을 확인함. (7/7)

## 5. Grouping Check
- Status, Provenance, Tool, Read-only, Synthesized Node 등 5가지 범주로 적절히 그룹화됨.

## 6. Promotion Drift Check
- 워커 가이드(`worker_guide_v0_2_candidate.md`)를 직접 수정하지 않음.
- `worker_guide_v0_3`을 생성하지 않음.
- 후보 문장을 '규칙'이 아닌 '후보'로 유지함.

## 7. Risk Check
- **Risk**: 번들 내의 경고문들이 실제 시스템 운영을 제약하는 공식 문서로 오해될 수 있음.
- **Mitigation**: 문서 서두와 Section 6, 8에 'Not a Worker Guide' 및 'Sandbox Candidate'임을 중복 명시함.

## 8. 4-line Footer
status: 검증 필요
summary: failure-to-guide run에서 생성된 7개 guide candidate를 bundle 후보 파일로 보관했는지 확인함
risk: 후보 문장이 worker guide나 source-space rule처럼 굳어질 수 있음
next: validation_round_13에서 promotion drift와 source anchor 누락 여부를 검증
