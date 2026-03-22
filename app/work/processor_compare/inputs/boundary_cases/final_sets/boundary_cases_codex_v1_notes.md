# Boundary Cases Codex v1

목적:
- Codex가 직접 고정한 30개 경계 사례 세트
- `scene / role / confidence / ambiguity / stability` calibration용

분포:
- `explanation_vs_reflection`: 5
- `explanation_vs_evidence`: 4
- `explanation_vs_comparison`: 3
- `thesis_vs_expansion`: 4
- `support_vs_example`: 4
- `contrast_vs_expansion`: 3
- `problem_vs_support`: 3
- `confidence_vs_ambiguity`: 2
- `stability_vs_mixed`: 2

운영 원칙:
- 이 세트는 모델 생성본 혼선을 피하기 위한 기준 세트다.
- 이후 `Codex / ChatGPT / Gemini`가 모두 같은 `final_case_id`를 유지한 채 라벨링해야 한다.
- 고정 메타는 아래로 통일한다.
  - `input_doc_id = boundary_cases_codex_v1`
  - `input_bundle_id = bundle_boundary_calibration_codex_v1`
  - `source_type = calibration_case`
  - `fragment_version = v1`
