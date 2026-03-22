# Label / Score Focus v0.1

목적:
- 현재 calibration 단계에서 `입력기 경계`보다 `라벨기 값`과 `축값`을 우선 관찰하는 기준을 고정한다.
- scene / role / confidence / ambiguity / stability drift를 우선 신호로 읽는다.

## 1. 최상위 원칙

지금 단계에서는 fragment boundary도 중요하지만,
직접적인 조정 근거는 아래 값들에서 먼저 나온다.

- scene
- role
- direction
- intensity
- stability
- confidence
- ambiguity

이유:
- fragment 경계는 문서 타입에 따라 흔들릴 여지가 크다.
- 반면 라벨기 값과 축값은 처리자 고유 성향이 더 직접적으로 드러난다.
- 따라서 현재는 입력기보다 라벨기와 점수기를 먼저 제련하는 편이 실용적이다.

## 2. 우선 관찰 순서

문서를 비교할 때는 아래 순서로 본다.

1. scene disagreement
2. role disagreement
3. confidence / ambiguity
4. stability
5. direction / intensity
6. fragment boundary

즉 절단 차이보다 먼저
`무엇으로 읽었는가`, `얼마나 확신했는가`, `얼마나 애매함을 남겼는가`
를 본다.

## 3. scene 우선 규칙

### 가장 먼저 보는 질문

- explanation으로 둘 것을 comparison / reflection으로 올렸는가
- 사례를 explanation / evidence로 두지 않고 scene drift를 일으켰는가
- 문서 타입별로 반복되는 scene 오용 패턴이 있는가

### 주의할 drift

- ChatGPT:
  - role 값을 scene으로 밀어 넣는 경향
  - 예: `scene=definition`, `scene=example`

- Gemini:
  - 비표준 scene을 새로 만드는 경향
  - 예: `process`, `analysis`, `historical_context`, `technical_reflection`

### 운영 규칙

- scene drift는 normalize로 숨기지 않는다.
- 먼저 `scene_schema_violation` 또는 `scene_disagreement`로 리포트에 남긴다.
- scene이 흔들리는 문서는 라벨기 조정 후보로 우선 본다.

## 4. role 우선 규칙

### 가장 먼저 보는 질문

- 결론부를 thesis로 읽는가, expansion으로 읽는가
- 대비를 contrast로 읽는가, meta/reflection으로 올리는가
- 문제 제기를 problem으로 두는가, support나 thesis로 밀어버리는가

### 중요 구간

- 결론
- 해석 확장
- 문제/해법 전환
- 철학자/관점 비교

### 운영 규칙

- role disagreement가 반복되면 scene보다 더 깊은 해석 차이로 본다.
- 같은 텍스트에서 `thesis / expansion / support`가 계속 갈리면 role 가이드를 조이는 쪽을 우선 검토한다.

## 5. confidence / ambiguity 우선 규칙

### 기본 해석

- 높은 confidence는 곧 좋은 것이 아니다.
- 낮은 ambiguity도 곧 좋은 것이 아니다.

### 가장 먼저 보는 질문

- 설명문이라는 이유만으로 confidence를 과하게 높였는가
- 문서가 해석적임에도 ambiguity를 너무 빨리 닫았는가
- 큰 덩어리로 묶고도 confidence를 높게 줬는가

### 처리자별 기준

- Codex:
  - 보수적 기준 후보
  - 상대적으로 ambiguity를 남기는 편

- ChatGPT:
  - 최근 문서에서는 압축형/유보형으로 움직일 수도 있음
  - 하지만 여전히 문서에 따라 고확신으로 기울 수 있으므로 계속 점검

- Gemini:
  - 큰 블록으로 묶으면서 confidence를 높이고 ambiguity를 낮추는 경향이 강함

### 운영 규칙

- `confidence high + ambiguity low + overmerged` 조합은 위험 신호로 본다.
- `confidence low + ambiguity high`가 무조건 나쁜 것이 아니라, 해석 여지를 정직하게 남긴 결과일 수 있음을 인정한다.

## 6. stability 우선 규칙

### 가장 먼저 보는 질문

- 실제로는 여러 논지나 화제가 섞였는데 stability를 높게 줬는가
- 큰 덩어리로 묶은 결과를 안정적이라고 과대평가했는가

### 운영 규칙

- `stability high + fragment count low`는 overmerged 여부와 같이 본다.
- stability는 단독으로 보지 않고 fragment granularity와 함께 읽는다.

## 7. direction / intensity 보조 규칙

### direction

- 논지 축이 얼마나 분명한가를 보지만,
  대화 기록이나 철학 텍스트에서는 낮다고 해서 곧 나쁜 것이 아니다.

### intensity

- 응집 압력과 밀도를 보지만,
  압축 요약형 처리자는 intensity를 인위적으로 높이거나 낮출 수 있다.

### 운영 규칙

- direction / intensity는 scene / role / confidence / ambiguity보다 후순위다.
- 이 값들은 보조적 drift 신호로 사용한다.

## 8. 문서 타입별 우선 체크

### 기술 / 구조 장문

- scene: explanation / instruction / reflection drift
- role: definition / support / thesis drift
- 점수: confidence 과상승, ambiguity 과소평가

### 철학 / 문화 장문

- scene: explanation / comparison / reflection drift
- role: contrast / expansion / meta drift
- 점수: ambiguity 과소평가 여부

### 문학비평 장문

- scene: explanation / reflection drift
- role: thesis / expansion / problem drift
- 점수: 논증 압축에 따른 stability 과대평가 여부

### 대화 기록 장문

- scene: explanation / evidence / reflection drift
- role: thesis / problem / support drift
- 점수: 압축 요약형 처리자가 confidence를 높게 주는지 여부

## 9. 리포트 작성 규약

현재 단계의 비교 메모는 아래 순서로 쓴다.

1. fragment count
2. scene 패턴
3. role 패턴
4. confidence / ambiguity 패턴
5. stability 패턴
6. 마지막에 boundary 보조 해석

즉 리포트도 라벨기와 축값을 먼저 말하고,
입력기 경계는 후순위 설명으로 붙인다.

## 10. 잠금 문장

현재 calibration 단계에서는
입력기 경계보다 라벨기와 축값을 먼저 제련한다.
우선 보는 것은 scene, role, confidence, ambiguity, stability다.
fragment boundary는 그 다음에 보조 해석으로 읽는다.
