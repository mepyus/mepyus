# Internal Observer Implementation Plan v0.1

목적:
- `internal_observer_architecture_v0_1.md`를 실제 구현 단위로 쪼갠다.
- 처음부터 완전한 모델을 만드는 것이 아니라,
  규칙 기반 observer prototype을 빠르게 세운 뒤 shadow mode로 검증한다.

## 1. 구현 목표

초기 구현 목표는 아래다.

1. 공통 feature extractor
2. observer profile 3종
3. merged output 생성기
4. boundary case shadow runner

이번 단계에서는
- 외부 LLM 호출 없음
- 규칙 기반 점수화
- scene / role / ambiguity 중심

## 2. 권장 파일 구조

```text
app/work/processor_compare/observer_engine/
  ├── __init__.py
  ├── feature_extractor.py
  ├── schema.py
  ├── runner.py
  ├── merger.py
  ├── profiles/
  │   ├── __init__.py
  │   ├── codex_like.py
  │   ├── chatgpt_like.py
  │   └── gemini_like.py
  └── rules/
      ├── scene_rules.py
      ├── role_rules.py
      ├── score_rules.py
      └── anchor_rules.py
```

## 3. 1단계 구현 범위

### feature_extractor
- 대조 접속사
- 인용부 존재
- 자기 성찰 표현
- 일반화 표현
- 장면/사례 표현
- 원인/근거 표현

### scene_rules
- explanation / reflection / comparison / evidence 우선 구현

### role_rules
- thesis / support / contrast / expansion / problem / definition 우선 구현

### score_rules
- confidence
- ambiguity
- stability

`direction`, `intensity`는 보조 구현으로 뒤에 붙여도 된다.

## 4. profile 차등 적용

### Codex-like
- explanation 유지 가중치 높음
- ambiguity 하한 높음
- reflection / expansion 상승 조건 엄격

### ChatGPT-like
- comparison / contrast 감지 가중치 높음
- support 유지 성향
- reflection 상승 조건은 Codex-like보다 약간 낮되, 여전히 엄격

### Gemini-like
- reflection / expansion prior 높음
- overmerge prior 높음
- calibration layer에서 하향 보정 필수

## 5. merger 구현

초기 merged rule:
- scene:
  - Codex-like / ChatGPT-like 합의면 채택
  - 갈리면 Codex-like 우선
- role:
  - Codex-like 우선
  - ChatGPT-like와 같으면 신뢰도 상승
- ambiguity:
  - Codex-like와 ChatGPT-like 중 더 높은 쪽에 가깝게 유지
- Gemini-like:
  - 최종값이 아니라 signal로만 저장

## 6. shadow mode

초기 검증 대상:
- `boundary_cases_codex_v1_retry12`

검증 방식:
- 내부 observer 3종 출력 생성
- 기존 ChatGPT/Gemini 라벨 결과와 drift 비교
- 어디가 비슷하고 어디가 다른지 본다

## 7. 잠금 문장

처음부터 거대한 추론 엔진을 만들지 않는다.
규칙 기반 observer prototype을 빠르게 세우고,
boundary case shadow mode로 calibration한다.
