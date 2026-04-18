# engine_feedback_memory_loop_v1

## 1. purpose

이 문서는 엔진 운용 중 생기는 피드백을
기능적 / 기술적 / 운영적 / 철학적 층으로 분리해
별도 memory로 누적하는 기준을 잠근다.

핵심 목적:

- 중요한 해석과 방향성을 흩어지지 않게 남긴다
- 같은 실수와 같은 통찰을 다시 처음부터 재발견하지 않게 한다
- Codex가 이후 판단과 위임과 자동화 설계에서
  자기 자신에게 도움이 되는 자료를 스스로 축적하게 만든다

---

## 2. top principle

피드백은 대화 속에만 남겨두지 않는다.

반복적으로 쓸 가치가 있는 피드백은
run report와 별도로,
**feedback memory layer**에 따로 올린다.

즉:

- run report는 사건 기록
- feedback memory는 해석과 방향성 축적

이다.

---

## 3. feedback layers

## 3-1. functional feedback

역할:

- 현재 기능이 무엇을 잘 하고 무엇을 못 하는지
- 어떤 표면이 충분하고 어떤 표면이 빈약한지
- 어떤 사용자 경험 공백이 있는지

예:

- compare candidate panel은 아직 없다
- invalid query fallback은 의미적으로 안정화되었다
- live unavailable path는 controlled path로만 검증 가능하다

---

## 3-2. technical feedback

역할:

- 계약 경계
- adapter / builder / viewer 구조
- 리스크가 있는 coupling
- 구현 시 주의해야 할 기술적 포인트

예:

- raw payload direct read 금지
- adapter contract touch는 guarded extension이다
- selection_query_state와 live_availability는 분리 유지해야 한다

---

## 3-3. operational feedback

역할:

- 실제 운용 중 무엇이 리스크였는지
- 어디서 의미 충돌이 났는지
- fallback / unavailable / selection 흐름에서 무엇을 먼저 봐야 하는지

예:

- invalid query와 unavailable은 섞이면 안 된다
- control bar가 query 설명의 주 표면이어야 한다
- strip/detail/activity는 자기 책임 밖 설명을 하지 않아야 한다

---

## 3-4. philosophical feedback

역할:

- 엔진 철학과 방향성에 관한 피드백
- 무엇을 더 많이 만드는 것보다 무엇을 덜 섞이게 만드는 게 중요한지
- 작은 차이가 왜 리스크가 되는지

예:

- 기능 추가보다 의미 충돌 방지가 더 중요해진 구간이다
- 상태 축, 표면 책임, 용어 경계가 본질이다
- 자동화도 변화 관찰 장치여야 한다

---

## 4. storage rule

위치:

- `runtime/memory/feedback/`

파일 구조:

- `README.md`
- `feedback_capture_basis_v1.md`
- 필요 시 주제별 log 또는 snapshot 문서

권장 기록 단위:

- `functional`
- `technical`
- `operational`
- `philosophical`

---

## 5. what should be recorded

다음 중 하나에 해당하면 feedback memory에 올린다.

- 반복해서 다시 써야 할 해석
- 이후 확장 gate를 판단할 때 기준이 되는 포인트
- 실패를 막아 주는 경계 인식
- user 철학과 직접 닿아 있는 운영 관찰
- Codex 자신이 이후 더 잘 판단하기 위해 필요한 메모

다음은 올리지 않는다.

- 단순 결과 요약만 있는 run report
- 일회성 구현 메모
- 이미 delta log와 receipt만으로 충분한 단순 작업 흔적

---

## 6. practical capture rule

새 피드백이 생기면 먼저 아래를 판단한다.

1. 이건 run-specific인가?
2. 아니면 반복 가치가 있는가?
3. 기능/기술/운영/철학 중 어느 층인가?
4. 이후 Codex 자신에게 다시 필요할 가능성이 큰가?

반복 가치가 크면
feedback memory layer에 올린다.

---

## 7. relation to memory spine

feedback memory는 기존 spine의 보조층이 아니라,
실제 운용 과정에서 반복 판단을 돕는
**cross-cutting memory layer**다.

즉:

- problem_recognition memory는 사용자의 사고 구조를 복원하고
- feedback memory는 엔진 운용 과정에서 드러난 해석과 리스크를 축적한다

둘은 다르지만 함께 읽혀야 한다.

---

## 8. one-line lock

반복 가치가 있는 기능적/기술적/운영적/철학적 피드백은 대화에 흘려보내지 말고, runtime/memory/feedback 레이어에 별도 축적하여 이후 판단과 위임과 확장 gate의 기준으로 재사용해야 한다.
