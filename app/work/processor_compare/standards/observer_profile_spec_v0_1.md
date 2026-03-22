# Observer Profile Spec v0.1

## 1. 공통 출력 스키마

모든 observer는 아래 필드를 생성한다.

- anchors
- direction
- intensity
- stability
- scene
- role
- semantic_tags
- structural_tags
- confidence
- ambiguity
- evidence_text
- why_short
- processor_notes

## 2. Codex-like Spec

성향:
- conservative
- ambiguity_preserving
- schema_strict

권장 기본값 경향:
- confidence: 중간 또는 중상
- ambiguity: 중간 이상 허용
- reflection threshold: 높음
- expansion threshold: 높음
- comparison threshold: 중간

강조 feature:
- 구조 보존
- 과잉 일반화 억제
- mixed signal 감지

## 3. ChatGPT-like Spec

성향:
- surface_structure_sensitive
- comparison_ready
- support_retaining

권장 기본값 경향:
- confidence: 중간~중상
- ambiguity: Codex-like보다 약간 낮게 시작 가능
- reflection threshold: 높음
- comparison threshold: Codex-like보다 낮음
- contrast threshold: 낮음

강조 feature:
- 병렬 구조
- 대조 문장
- 장면/사례의 논지 기능

주의 drift:
- comparison 과상승
- evidence/example 과상승

## 4. Gemini-like Spec

성향:
- abstraction_prone
- overmerge_prone
- reflection_expansion_prone

권장 기본값 경향:
- confidence: 높게 치우치지 않게 clamp 필요
- ambiguity: 하한 보정 필요
- reflection threshold: 높게 재설정 필요
- expansion threshold: 높게 재설정 필요

강조 feature:
- 상위 의미 도약
- 메타화
- 큰 의미 블록 통합

주의 drift:
- reflection 과상승
- expansion 과상승
- 수치 schema drift

## 5. Merged Spec

병합 원칙:
- scene: Codex-like / ChatGPT-like 다수결 또는 합의
- role: Codex-like 우선, ChatGPT-like 보조
- ambiguity: 보수적으로 높게 유지
- stability: mixed signal 있으면 하향

Gemini-like 반영 원칙:
- 상위 추상화 신호만 부분 반영
- 최종 판정자 역할 금지
