# Internal Observer Architecture v0.1

목적:
- 외부 LLM을 매번 왕복 호출하지 않고도,
  지금까지 축적한 비교 데이터를 바탕으로
  `Codex-like / ChatGPT-like / Gemini-like` 내부 관측기를 구성한다.
- 이 관측기들은 실제 모델 복제가 아니라
  `관측 성향의 근사`를 목표로 한다.

## 1. 최상위 방향

현재까지의 결론:
- `Codex`는 보수적 기준선 후보
- `ChatGPT`는 메인 보조 관측기
- `Gemini`는 정밀 라벨러라기보다 보조 추상화 관측기

따라서 내부 구조는 아래처럼 간다.

1. 공통 입력기
2. 관측기 프로파일 3종
3. calibration / correction layer
4. merged output layer
5. 저장 / 비교 / 리포트 layer

## 2. 공통 입력기

공통 입력기는 profile과 분리한다.

공통 입력기의 역할:
- fragment 입력 수신
- evidence_text 후보 추출
- anchor 후보 추출
- scene / role / score 판정에 필요한 기초 feature 산출

이 레이어는 가능한 한 profile-neutral 해야 한다.

예시 feature:
- 비교 접속사 존재 여부
- 인용부 / 대화부 존재 여부
- 장면 증거성 문장 존재 여부
- 정의형 문장 비율
- 일반화 문장 비율
- 자기 성찰 어휘 비율
- 상반 신호 존재 여부

## 3. Observer Profiles

### 3.1 Codex-like

핵심 성향:
- 보수적
- 중간 granularity
- ambiguity 유지
- reflection / expansion threshold 높음
- scene / role schema 준수 우선

의도:
- 현재 내부 기준선
- 과도한 확신이나 메타화 방지

### 3.2 ChatGPT-like

핵심 성향:
- 구조 표면 신호 반영 강함
- comparison / contrast 민감도 높음
- support 유지 성향
- 문서 타입에 따라 segmentation 성향이 변동 가능

의도:
- Codex-like와 함께 메인 관측축 구성
- 비교 / 구조적 대조 / 논지 전개 감지 보조

### 3.3 Gemini-like

핵심 성향:
- overmerge prior 높음
- reflection / expansion prior 높음
- ambiguity baseline 낮음
- 상위 추상화 신호에 민감

의도:
- 최종 정밀 판정자 아님
- 상위 의미 이동, 과대추상화, 메타 상승 감지용 보조 관측기

## 4. Calibration Layer

관측기 출력은 바로 내보내지 않는다.

calibration layer의 역할:
- schema 강제
- score 범위 강제
- profile별 known drift 억제
- boundary case calibration에서 확인된 편향 보정

대표 보정:
- `gemini_like`
  - reflection 과상승 억제
  - expansion 과상승 억제
  - ambiguity 하한 보정
  - 0~1 수치 강제

- `chatgpt_like`
  - comparison 과상승 여부 재판정
  - example / evidence 과잉 판정 억제
  - 문자열 인용부 정합성 강제

- `codex_like`
  - 기준선 유지
  - 지나친 보정 금지

## 5. Merged Output Layer

최종 merged output은 단순 평균이 아니다.

기본 원칙:
- `Codex-like + ChatGPT-like`를 메인으로 사용
- `Gemini-like`는 보조 신호로 사용

병합 우선순위:

### scene
- Codex-like / ChatGPT-like 합의 우선
- 둘이 갈릴 때 Gemini-like는 tie-break가 아니라 참고 신호

### role
- Codex-like 우선
- ChatGPT-like 보조
- Gemini-like는 expansion / reflection 과상승 여부 감시

### confidence / ambiguity
- ambiguity를 너무 빨리 닫지 않는다
- merged ambiguity는 보수적으로 잡는다
- Gemini-like의 낮은 ambiguity는 그대로 수용하지 않는다

### stability
- overmerge 신호가 있으면 stability 상한을 낮춘다

## 6. 저장 구조

권장 출력:
- profile별 raw output 3개
- merged output 1개
- calibration signals 1개

예시:
- `observer_outputs/codex_like/...`
- `observer_outputs/chatgpt_like/...`
- `observer_outputs/gemini_like/...`
- `observer_outputs/merged/...`
- `observer_outputs/signals/...`

## 7. 운영 모드

### shadow mode
- 기존 외부 LLM 비교와 나란히 돌린다
- 내부 관측기가 얼마나 비슷한 drift를 재현하는지 본다

### assisted mode
- 내부 관측기를 기본 사용
- 일부 샘플만 외부 LLM로 검증

### primary mode
- 내부 관측기 3종 + merged output을 기본 입력층으로 사용
- 외부 LLM은 calibration 재점검용으로만 사용

## 8. 현재 권장 전략

현재 단계에서는 아래 전략을 쓴다.

1. `Codex-like`를 기준선으로 유지
2. `ChatGPT-like`를 메인 보조 관측기로 사용
3. `Gemini-like`는 서브 관측기만 담당
4. merged output은 `Codex-like + ChatGPT-like` 중심으로 구성
5. Gemini-like는 상위 추상화 보조 신호로만 반영

## 9. 잠금 문장

내부 관측기 구조의 목적은
외부 LLM을 복제하는 것이 아니라
이미 관찰된 추론 성향을 재현 가능한 규칙층으로 바꾸는 것이다.

메인 관측축은 `Codex-like + ChatGPT-like`,
`Gemini-like`는 보조 추상화 관측기로 둔다.
