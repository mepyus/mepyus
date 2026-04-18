# feedback_capture_basis_v1

## 1. purpose

현재까지 대화와 구현 과정에서 확인된
의미 있는 기능적/기술적/운영적/철학적 피드백의
첫 기준 snapshot을 남긴다.

---

## 2. functional feedback

- operating UI는 지금 단계에서 기능 추가보다
  읽힘 경계와 fallback 의미 정리가 더 중요하다.
- compare candidate panel 같은 새 panel은
  쉽게 “새 해석면”으로 비대해질 수 있으므로
  read-only aid로 제한해야 한다.
- unavailable path는 문서 정의만으로는 부족했고,
  controlled path로 재현 가능해져야 실제 기준선이 된다.

---

## 3. technical feedback

- raw payload direct read는 계속 금지해야 한다.
- adapter는 UI와 runtime payload 사이의 핵심 경계다.
- selection_query_state와 live_availability를 섞는 순간
  상태 체계가 빠르게 오염된다.
- guarded extension 여부는 주로
  builder/adapter contract touch 여부에서 갈린다.

---

## 4. operational feedback

- invalid query와 unavailable은 운용상 완전히 다른 문제다.
- control bar는 query/fallback/live 설명의 주 표면이어야 한다.
- strip/detail/activity가 query 오류까지 설명하기 시작하면
  표면 책임이 무너진다.
- 지금 operating UI는 “정보를 더 붙이는 단계”보다
  “의미 충돌을 줄이는 단계”에 더 가깝다.

---

## 5. philosophical feedback

- 이 엔진은 기능을 추가하는 것보다
  작은 차이와 의미 경계를 기록하는 쪽이 더 중요하다.
- 확장보다 경계 관리가 더 중요한 시점이 분명히 존재한다.
- Codex 자신에게 도움이 되는 기록을 따로 쌓지 않으면
  이후 비슷한 판단을 매번 다시 하게 된다.
- 피드백 memory는 사용자를 위한 보고가 아니라
  Codex 자신의 미래 판단 품질을 위한 자산이다.

---

## 6. use rule

앞으로 의미 있는 피드백이 생기면
이 문서를 덮어쓰는 방식보다,
주제별 snapshot 또는 추가 문서로 누적하는 편이 좋다.

예:

- `operating_ui_feedback_snapshot_v2.md`
- `delegation_feedback_snapshot_v1.md`
- `state_axis_feedback_snapshot_v1.md`
