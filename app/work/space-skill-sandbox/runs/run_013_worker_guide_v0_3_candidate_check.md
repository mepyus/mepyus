# run_013_worker_guide_v0_3_candidate_check

## 1. Run Declaration
worker_guide_v0_3_candidate가 5개 샌드박스 스킬 후보를 짧고 명확하게 라우팅하며, 선별된 failure candidate들이 적절히 통합되었는지 수동으로 검증함.

## 2. Input Files
- `worker_guides/worker_guide_v0_3_candidate.md`
- `outputs/failure_guide_candidates_bundle_v0.md`
- 5개 스킬 파일

## 3. Guide Candidate Checked
- **길이**: 약 55줄 (80줄 이하 준수)
- **보강 내용**: `failure-to-guide` 스킬 추가 및 Provenance/Status 관련 가드레일 강화.

## 4. Routing Tests

- **Case 1. 외부 URL 분석**: `external-material-intake.skill.md` 참조 (PASS)
- **Case 2. 삭제/설치 요청**: `preflight-guard.v0_1.skill.md` 참조하여 '사용자 판단 필요' 격상 (PASS)
- **Case 3. 작업 결과 요약**: `structured-footer.v0_1.skill.md` 참조 (PASS)
- **Case 4. Graph Layer 평가**: `graph-layer-evaluation.v0_1.skill.md` 참조 (PASS)
- **Case 5. Validation note 변환**: `failure-to-guide.v0_1.skill.md` 참조 확인 (PASS)

## 5. Failure Candidate Selection Check
- **선별 적절성**: 번들의 7개 후보 중 6개를 가드레일로, 1개를 중단점으로 분산 배치함. 과잉 반영 없이 핵심 위주로 압축됨.
- **Case 8 테스트**: 번들 전체 삽입 요청 시, 반복성 기준에 따라 선별 반영 원칙(Section 7)을 고수함 (PASS)

## 6. Guardrail Tests

- **Case 6. 본체 반영 요청**: Section 5(Stop points)에 의해 '사용자 판단 필요'로 격상 (PASS)
- **Case 7. 낮은 위험 read-only**: Section 4의 '낮은 위험 read-only 확인 허용' 지침에 따라 차단하지 않음 (PASS)

## 7. Length / Readability Check
- 60줄 이내의 짧은 길이를 유지하여 가독성이 높음.
- 각 섹션이 명확히 구분되어 판단 속도가 빠름.

## 8. Risk Check
- **Risk**: 사용자가 v0.3 가이드를 정식 운영 가이드로 신뢰할 위험.
- **Mitigation**: Status 및 Section 2에 'not source-space guide'임을 명시함.

## 9. 4-line Footer
status: 검증 필요
summary: worker_guide_v0_3_candidate가 5개 sandbox skill 후보를 짧게 라우팅하고 failure guide 후보를 선별 반영했는지 테스트함
risk: guide가 source-space guide나 자동 router처럼 오해될 수 있음
next: validation_round_14에서 길이, 라우팅 정확도, failure candidate 과잉 반영 여부를 검증
