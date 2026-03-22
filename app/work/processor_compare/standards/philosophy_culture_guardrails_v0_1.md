# Philosophy / Culture Guardrails v0.1

목적:
- 철학사, 문화비평, 개념사 장문 문서를 비교할 때 입력기와 라벨기 drift를 줄인다.
- `doc_007`에서 드러난 차이를 다음 유사 문서 판정의 기준선으로 고정한다.

## 1. 문서 유형

이 guardrail은 아래 성격의 문서에 적용한다.

- 철학 개념 해설
- 사상가 비교 글
- 문화비평 장문
- 예술/영화 사례를 끼워 넣는 개념사 글
- 정의, 예시, 계보, 정조가 함께 섞인 텍스트

## 2. 입력기 경계 기준

### 패턴 A. 개념 정의 vs 사례 예시

- 개념의 직접 정의와 사례는 기본적으로 분리 후보다.
- `보드리야르 정의 -> 전쟁 예시 -> 화폐 예시`처럼 사례가 기능적으로 독립하면 separate fragment로 유지한다.
- 사례가 빠지면 개념의 작동 방식이 손실되므로, 대묶음으로 흡수하지 않는다.

### 패턴 B. 계보 전환 vs 철학자 본문

- `플라톤부터 들뢰즈까지` 같은 계보 선언은 별도 `bridge` 후보로 본다.
- 계보 전환문을 첫 철학자 설명에 흡수하면 이후 후매칭이 불안정해진다.

### 패턴 C. 철학자 내부 소단락 분절

- 한 철학자 섹션 안에서도 `핵심 개념 정의`, `확장 논의`, `대표 비유/인용`은 분리 가능성을 점검한다.
- 단, 모든 소단락을 기계적으로 쪼개지 않는다.
- `개념 정의 + 즉시 이어지는 핵심 해설`은 유지 가능하지만, `동굴의 비유`, `매트릭스`, `공포 이미지`처럼 사례 성격이 강하면 separate candidate로 본다.

### 패턴 D. 개념 논의 vs 정조/불안

- `실재/가상 논의`와 `공포/불안/거울 강박`은 기본적으로 다른 의미 움직임이다.
- 문화적 정조가 독립적이면 `reflection` 또는 `expansion` 후보로 본다.
- 단순 사례인지 메타적 정조 요약인지 판정 이유를 리포트에 남긴다.

## 3. scene / role 규칙

### 개념 정의

- scene = `explanation`
- role = `definition`

### 철학자 간 대비

- scene = `comparison`
- role = `contrast`

### 역사적 전환문

- scene = `transition`
- role = `bridge`

### 문화 사례

- scene = `explanation` 또는 `evidence`
- role = `example`

### 공포 / 불안 / 정조 요약

- scene = `reflection`
- role = `expansion`

주의:
- `definition`, `example`, `analysis`, `historical_context`, `technical_reflection`는 scene으로 쓰지 않는다.
- 철학 글이라고 해서 `reflection/meta`를 자동 부여하지 않는다.

## 4. 처리자별 drift 해석

### ChatGPT

- 철학자 내부 소단락을 과세분화하는 경향이 있다.
- 문화 사례를 별도 fragment로 독립시키는 경우가 많다.
- `scene=example`, `anchor_type=example` 같은 enum drift를 반복할 수 있다.

실무 해석:
- 잘게 쪼갠 조각은 `oversegmentation_candidate`로 점검한다.
- schema 위반은 normalize로 숨기지 말고 calibration 신호로 남긴다.

### Gemini

- 철학자 섹션을 큰 설명 블록으로 합치는 경향이 있다.
- 계보 전환, 화폐/매트릭스 같은 보조 사례, 공포 정조를 흡수하거나 누락시킬 수 있다.
- scene을 자체 범주로 재구성하는 경향이 강하다.

실무 해석:
- 누락되거나 흡수된 조각은 `overmerged_candidate`로 본다.
- 결론이 `reflection/expansion`으로 쉽게 이동하면 실제 메타인지 재판정한다.

### Codex

- 개념 정의, 전환, 사례, 정조를 중간 granularity로 분리하는 기준 후보로 쓴다.
- 절대 정답이 아니라 calibration 중간값으로 유지한다.

## 5. 리포트 우선 점검 항목

철학/문화 장문 비교에서는 아래를 먼저 본다.

1. 사례 fragment 누락 여부
2. 계보 전환 fragment 유지 여부
3. 철학자 내부 소단락의 과세분화 여부
4. 공포/불안 정조를 `example`으로 읽는지 `reflection`으로 읽는지
5. 들뢰즈 같은 결론부가 `contrast`에서 `reflection/meta`로 이동하는지

## 6. 잠금 문장

철학/문화 장문에서는
개념 정의, 사례, 계보 전환, 정조를 한 덩어리로 뭉개지 않는다.
또한 문화 사례를 만났다고 해서 scene enum을 임의 확장하지 않는다.
Codex는 중간 granularity 기준을 유지하고,
ChatGPT의 과세분화와 Gemini의 대묶음을 calibration 신호로 읽는다.
