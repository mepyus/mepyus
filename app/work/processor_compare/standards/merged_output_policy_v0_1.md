# Merged Output Policy v0.1

목적:
- observer profile 3종의 출력을 최종 입력층 출력으로 병합하는 기준을 고정한다.

## 1. 기본 원칙

- `Codex-like`를 기준선으로 본다.
- `ChatGPT-like`는 메인 보조 관측기다.
- `Gemini-like`는 정밀 판정자가 아니라 보조 추상화 관측기다.

## 2. scene 병합

우선순위:
1. Codex-like / ChatGPT-like 합의
2. Codex-like 우선
3. Gemini-like는 보조 해석

예:
- Codex=explanation, ChatGPT=explanation, Gemini=reflection
  - merged=explanation

- Codex=explanation, ChatGPT=comparison, Gemini=reflection
  - boundary signal 유지
  - merged는 Codex 우선 또는 explanation_with_comparison_signal 처리

## 3. role 병합

우선순위:
1. Codex-like
2. ChatGPT-like
3. Gemini-like

특별 규칙:
- Gemini-like의 expansion / reflection 과상승은 직접 반영하지 않는다.
- Codex-like와 ChatGPT-like가 모두 support / thesis / contrast 쪽이면 그쪽을 유지한다.

## 4. score 병합

### confidence
- 평균이 아니라 보수적 평균 또는 중간값 사용
- 과상승 방지

### ambiguity
- 낮은 쪽으로 닫지 않는다
- Codex-like 값을 하한이 아니라 기준값으로 본다
- Gemini-like의 낮은 ambiguity는 직접 수용하지 않는다

### stability
- overmerge signal 또는 mixed signal 있으면 하향 보정

## 5. signals 동시 저장

merged output만 남기지 않는다.

항상 같이 저장:
- observer agreement
- scene disagreement
- role disagreement
- ambiguity warning
- overmerge / oversegmentation warning

## 6. shadow validation

merged output은 바로 production에 올리지 않는다.

순서:
1. boundary case
2. calibration doc
3. long-form sample
4. 실제 pipeline 연결

## 7. 잠금 문장

merged output은 평균값이 아니다.
`Codex-like + ChatGPT-like`를 중심으로,
`Gemini-like`는 보조 추상화 신호만 제한적으로 반영한다.
