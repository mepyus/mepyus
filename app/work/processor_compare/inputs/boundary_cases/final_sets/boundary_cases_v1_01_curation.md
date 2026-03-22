# Boundary Cases v1_01 Curation

최종 세트: `boundary_cases_v1_01_final.json`

판단:
- `boundary_cases_v1_01.json`은 `chatgpt`와 `gemini` 생성본이 완전히 동일하다.
- 따라서 이 파일은 두 모델 비교 결과라기보다, 하나의 공통 생성 세트로 취급하는 것이 맞다.

성격:
- `v1`보다 형식이 더 깨끗하다.
- 축 분포가 정확하고 JSON 오류가 없다.
- 문체는 전반적으로 더 정제되고 추상적이다.
- 일상 장면보다는 설명문/비평문/개념문 비중이 높다.

권장 사용:
- `boundary_cases_v1_final.json`
  - 더 자연스럽고 현실적인 스트레스 테스트 세트
- `boundary_cases_v1_01_final.json`
  - 더 정제된 공통 calibration 세트

운영 제안:
1. 먼저 `v1_01`로 라벨기 규칙을 맞춘다.
2. 그다음 `v1`로 자연스러운 문단에서 drift가 다시 나는지 본다.

주의:
- `v1_01`은 두 생성기가 동일하므로, source 표기는 `shared_v1_01`로 통일했다.
