# user_friendly_label_anchor_surface_refinement_v1.md

## 1. scope

- axis change: 없음
- scene/flow/role 체계 수정: 없음
- core engine 수정: 없음
- target:
  - label surface refinement
  - anchor bucket refinement
  - user-facing interpretation layer 추가

수정 대상은 아래로 제한했다.

- `scripts/run_concept_segment_probe.py`
- `scripts/run_middle_layer_interview_probe.py`

---

## 2. what changed

### concept probe 쪽
- scene/flow 값은 그대로 유지했다
- 대신 display label을 추가했다
  - `review` -> `설명/해석 층`
  - `impl` -> `구현/실행 층`
  - `evidence` -> `근거/검증 층`
  - `spec` -> `규칙/형식 힌트 층`
  - `compare` -> `비교/해석 흐름`
  - `run` -> `작동/실행 흐름`
- anchor를 아래 bucket으로 나눴다
  - `core_topic_anchor`
  - `user_layer_hint_anchor`
  - `discourse_residue_anchor`
  - `speaker_or_source_residue_anchor`
- source별 / overall 기준으로
  - `opening_summary`
  - `user_layer_hints`
  를 추가했다

### middle-layer probe 쪽
- 기존 dominant/secondary/observer role은 유지했다
- 대신 role gloss를 추가했다
  - `핵심 메커니즘 역할`
  - `검증/평가 역할`
  - `문제/제약 역할`
  - `운영/배치 역할`
  - `반성/갭 역할`
  - `전환/관찰 역할`
- packet에 아래 필드를 추가했다
  - `dominant_role_gloss`
  - `secondary_role_gloss`
  - `observer_role_gloss`
  - `anchor_bucket_counts`
  - `user_layer_hint_signals`
  - `user_facing_summary`

즉 이번 refinement는
분류 체계를 바꾼 것이 아니라,
**같은 분류를 사용자가 읽기 쉬운 표면으로 재번역한 것**
이다.

---

## 3. verification snapshots

## 3-1. AI future probe v2
- generated:
  - `app/work/archive_review/probe_support/concept_segment_probe/generated/ai_future_segment_probe_v2_20260328T002753Z.json`
- overall opening summary:
  - `설명/해석 층 중심, 비교/해석 흐름 우세, 주요 사용자 층위 힌트: 전망/방향, 구현/실행, 구조/연결`

이전에는 주로
- review
- compare
같은 내부값 중심으로 읽혔다면,
지금은
- 전망/방향
- 구현/실행
- 구조/연결
같은 사용자 질문 근접 힌트가 바로 보인다.

## 3-2. ontology/vectorfl probe v2
- generated:
  - `app/work/archive_review/probe_support/concept_segment_probe/generated/ontology_vectorfl_layer_probe_v2_20260328T002753Z.json`
- overall opening summary:
  - `설명/해석 층 중심, 비교/해석 흐름 우세, 주요 사용자 층위 힌트: 구조/연결, 구현/실행, 전망/방향`

즉 이 축은 여전히 explanatory review가 중심이지만,
사용자 친화 표면에서는
- 구조/연결
- 구현/실행
이 바로 읽히도록 바뀌었다.

## 3-3. interview middle-layer probe v1 surface
- generated:
  - `app/work/archive_review/interview_support/middle_layer_experiments/generated/middle_layer_interview_probe_20260328T002752Z.json`

case별 user-facing summary는 아래처럼 읽힌다.

### Dario
- `핵심 메커니즘 역할, 검증/평가 역할 중심`

### Andrej
- `반성/갭 역할, 문제/제약 역할 중심`

### Alex
- `문제/제약 역할, 운영/배치 역할 중심`

즉 내부 role code만이 아니라,
사용자 친화적 역할 해석명이 packet 단계에서 바로 보이기 시작했다.

---

## 4. what improved

- topic-bearing anchor visibility: 개선됨
- user-layer hint visibility: 개선됨
- label readability: 개선됨
- axis untouched: 유지됨

특히 concept probe 쪽은
`review / compare` 같은 내부값만 보던 상태에서,
`전망/방향`, `구현/실행`, `구조/연결`, `근거/검증`
같은 해석 힌트가 먼저 보이게 됐다.

---

## 5. what still remains

- middle-layer probe에서는 discourse residue 비중이 아직 높다
- user-layer hint anchor는 생겼지만 아직 충분히 두껍지 않다
- 일부 case-specific signal은 여전히 사용자 친화적 표현보다 raw token에 가깝다
- 즉 표면은 좋아졌지만 아직 완전히 user-layer translation이 닫힌 것은 아니다

따라서 이번 상태는
- `PASS_WITH_NOTE`
로 읽는 편이 맞다.

---

## 6. why dictionary/encyclopedia input stays later

지금 바로 사전류를 대량 넣지 않는 이유는 분명하다.

- 아직 표면 번역 구조가 완전히 안정화되지 않았다
- 지금은 label/anchor 출력이 사용자 층위를 여는 방향으로 가는지 먼저 봐야 한다
- 이 상태에서 사전류를 넣으면 내부 언어만 더 복잡해질 위험이 있다

즉 순서는 계속 아래다.

1. user-facing label/anchor surface 정렬
2. 공간 형성 확인
3. 그다음 사전류/백과사전류 투입

---

## 7. result

- status: PASS_WITH_NOTE

한 줄로 요약하면:

- 이번 refinement는 axis를 바꾸지 않고도 label/anchor 출력면을 사용자 질문 친화적인 표면으로 한 단계 이동시켰지만, residue 억제와 user-layer hint 두께는 아직 더 체득이 필요하다.
