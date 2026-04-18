## feature change reason as space material spec v0

### 0. purpose

이 문서의 목적은
기능 추가/수정 자체만이 아니라
그 변경의 이유, 처음 그렇게 만들었던 이유, 지금 바꾸려는 이유까지
공간 안의 재료로 다시 넣는 기준을 잠그는 것이다.

핵심은 아래다.

- 기능 결과만 남기지 않는다
- 변경 이유도 남긴다
- 그 이유를 line 관점에서 다시 읽는다
- 그 결과를 다음 reread와 다음 구현의 재료로 쓴다

즉 기능 개발은 끝점이 아니라
새 재료를 생산하는 공간 행위로 본다.

---

### 1. why this layer is needed

기능만 남기면 공간에는 결과만 쌓인다.
하지만 실제로 다음 구현과 다음 해석에 더 중요한 것은
왜 그렇게 만들었는지,
왜 지금 바꾸는지,
무엇을 지키려 했는지,
무엇을 포기했는지다.

따라서 공간이 자기 자신을 더 잘 읽으려면
다음도 남겨야 한다.

- 최초 설계 이유
- 당시의 제약
- 현재 변경 이유
- 변경이 건드리는 line
- 변경 이후 새로 생긴 tension

이 층이 없으면 기능 변화는 코드 diff로만 남고,
공간은 자기 변경의 의미를 충분히 다시 읽지 못한다.

---

### 2. basic rule

기능 변경은 아래 두 층으로 동시에 남겨야 한다.

1. implementation change
2. reason trace

`implementation change`는
무엇이 바뀌었는지를 남긴다.

`reason trace`는
왜 바뀌었는지,
왜 처음엔 그렇게 안 했는지,
무엇과 무엇 사이의 tension이 있었는지를 남긴다.

공간은 두 번째 층까지 있어야
변경을 line material로 다시 읽을 수 있다.

---

### 3. minimum reason material

기능 변경이 space material로 다시 들어오려면
최소 아래가 남아야 한다.

- changed object
  - 무엇을 바꿨는가
- original reason
  - 처음엔 왜 그렇게 만들었는가
- current change reason
  - 지금 왜 바꾸는가
- preserved constraint
  - 이번 변경에서도 지키는 것은 무엇인가
- released constraint
  - 이번 변경에서 느슨하게 한 것은 무엇인가
- line interpretation
  - 이 변경이 어떤 line을 두껍게 하거나 약하게 하는가
- next reread question
  - 이 변경 뒤에 무엇을 다시 봐야 하는가

---

### 4. line-oriented reading

기능 변경 이유는 단순 설명문으로 끝나면 안 된다.
반드시 line reread 재료가 되어야 한다.

예:

- 안전 line
- 운영 line
- 자동화 line
- calibration-before-ingest line
- preservation-before-promotion line
- reading-environment-before-full-automation line

어떤 변경이 일어났을 때
질문은 아래 순서로 가야 한다.

1. 이 기능은 처음 무엇을 지키려 했는가
2. 지금 무엇 때문에 수정되는가
3. 이 수정은 어떤 기존 line을 다시 흔드는가
4. 어떤 line은 두꺼워지고 어떤 line은 얇아지는가
5. 이 변경은 새 hub를 만들 가능성이 있는가
6. 다음 reread에서 무엇을 다시 확인해야 하는가

---

### 5. example direction

`inspection`에서
검사 시작 후 일정 시간 안에 산소/유해가스 측정을 강제하는 기능이 있었다고 하자.

이걸 바꿀 때 공간이 남겨야 하는 것은
버튼 로직 diff만이 아니다.

남겨야 하는 것은 예를 들어 아래다.

- original reason
  - 법적/안전 규정 때문에 시간 제약을 강하게 걸었다
- current change reason
  - 실제 현장 workflow와 장치 입력 순서가 달라 기존 제약이 오히려 오류를 유발한다
- preserved constraint
  - 안전성과 규정 준수 자체는 유지해야 한다
- released constraint
  - 측정 시작 타이밍을 UI 클릭 시점 하나에 고정하는 방식은 완화한다
- line interpretation
  - 안전 line은 유지
  - 운영 흡수 line은 강화
  - rigid enforcement line은 일부 약화
- next reread question
  - 이 변경이 실제로 안전을 더 잘 지키는가, 아니면 운영 편의만 키우는가

즉 코드 변경은 끝이 아니라
안전/운영/규정/현장 흐름 사이 긴장을 다시 드러내는 space material이 된다.

---

### 6. what this changes in space reading

이 층이 들어오면 공간을 보는 층위가 달라진다.

이전:

- 기능이 있다
- 기능을 바꿨다
- 결과가 나왔다

이후:

- 왜 이 기능이 처음 생겼는가
- 왜 지금 바꾸는가
- 이 변경은 어떤 line을 다시 흔드는가
- 어떤 제약은 유지되고 어떤 제약은 재배치되는가
- 이 이유가 다음 구현의 재료가 되는가

즉 기능 변경은 소비되는 일이 아니라
공간 안의 새 line material을 생산하는 일이 된다.

---

### 7. non-goals

이 문서는 아래를 하지 않는다.

- runtime heuristic 추가
- 자동 scoring 추가
- 자동 promotion 판정
- 변경 이유의 즉시 일반화
- line 확정 엔진 도입
- LLM이 근거 없이 이유를 예쁘게 써주는 구조

즉 이 문서는
기능 변경 이유를 space material로 다시 넣는 기준을 다룰 뿐,
자동 판정 엔진을 여는 문서가 아니다.

---

### 8. rule of order

순서는 아래여야 한다.

1. 기능 변경 발생
2. 변경 이유 trace 기록
3. reason trace를 line 관점으로 reread
4. 그 결과를 다시 공간 재료로 저장
5. 이후 다른 기능/문서/코드 reread에서 재사용

즉 reason trace는 patch 뒤의 부속 설명이 아니라
다음 reread를 여는 입력물이다.

---

### 9. one-line summary

기능 변경이 공간을 키우려면
코드 diff만 남기면 안 된다.
왜 바꿨는지, 무엇을 지키려 했는지, 어떤 line이 흔들렸는지까지
다시 공간 재료로 넣어야 한다.

즉 기능 변경의 이유는 설명문이 아니라
공간이 다음번에 다시 읽을 수 있어야 하는 line material이다.

