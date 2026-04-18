# user_facing_gloss_stability_and_residue_review_v1.md

## 1. checked cases

- `ai_future_segment_probe_v2`
- `ontology_vectorfl_layer_probe_v2`
- `middle_layer_interview_probe_20260328T002752Z.json`
- 추가 비교:
  - `interview_future_probe_v1`

이번 턴은 구조 수정이 아니라
현재 붙인 user-facing gloss의 반복 안정성과
residue 간섭 패턴을 보는 점검 턴이다.

---

## 2. case-by-case verdict

## 2-1. AI future probe v2
- verdict: `STABLE_ENOUGH_FOR_REPEAT_USE`
- why:
  - `설명/해석 층 중심, 비교/해석 흐름 우세, 주요 사용자 층위 힌트: 전망/방향, 구현/실행, 구조/연결`
  - 같은 internal axis를 유지하면서도 사용자 질문 근접 층위가 먼저 보인다
  - discourse residue는 존재하지만 top-level reading을 크게 훼손하지 않는다

## 2-2. ontology/vectorfl probe v2
- verdict: `STABLE_ENOUGH_FOR_REPEAT_USE`
- why:
  - `구조/연결` 힌트가 명확하게 앞에 선다
  - `설명/해석 층` 중심이라는 사실도 함께 보인다
  - source별로 `saltlux / ontology_youtube / graphrag`가 각각 구조/연결, 구현/실행 쪽 힌트를 비교 가능하게 드러낸다
- note:
  - discourse residue 비중은 AI future probe보다 조금 더 높다
  - 그래도 gloss가 읽기를 여는 데는 충분히 작동한다

## 2-3. middle-layer interview probe
- verdict: `USEFUL_BUT_CASE_SENSITIVE`
- why:
  - role gloss 자체는 분명하다
    - Dario: `핵심 메커니즘 역할 + 검증/평가 역할`
    - Andrej: `반성/갭 역할 + 문제/제약 역할`
    - Alex: `문제/제약 역할 + 운영/배치 역할`
  - dominant role mix 차이는 사용자에게도 읽히기 시작했다
- limit:
  - `anchor_bucket_counts` 기준으로 discourse residue가 여전히 지나치게 크다
    - Dario: discourse 239 vs core 12
    - Andrej: discourse 215 vs core 11
    - Alex: discourse 280 vs core 11
  - `user_facing_summary`는 좋아졌지만 아직 raw token이 일부 그대로 끼어든다

## 2-4. interview_future_probe_v1
- verdict: `STILL_ENGINE_INTERNAL_HEAVY`
- why:
  - 세 인터뷰에 동일한 concept probe를 적용하면 user-layer hint가 매우 약하다
  - overall user/core ratio도 낮다
    - `user/core_ratio = 0.007`
  - Dario, Alex는 `명확한 사용자 층위 힌트 없음`으로 읽힌다
- meaning:
  - concept-probe gloss는 broad thematic probe에는 안정적이지만
  - interview-like case에는 아직 직접 적용력이 약하다

---

## 3. repeated residue types

이번 턴에서 반복적으로 보인 residue는 아래다.

### 3-1. discourse connective residue
예:
- `그래서`
- `우리가`
- `우리는`
- `이렇게`
- `어떻게`

특징:
- concept probe에서는 크게 방해하지 않지만
- middle-layer interview에서는 여전히 중심 경쟁을 강하게 방해한다

### 3-2. speaker/source residue
예:
- 화자명
- source-specific proper noun

특징:
- concept probe에서는 비교적 잘 눌린다
- 하지만 interview packet에서는 여전히 case-specific signal 안으로 섞일 여지가 있다

### 3-3. generic abstraction residue
예:
- `모델이`
- `완벽히`
- `수많은`
- `기술적`

특징:
- topic-bearing처럼 보이지만
- 실제로는 사용자 질문의 층위를 직접 열지 못한다
- middle-layer summary를 아직 덜 사용자 친화적으로 보이게 만든다

### 3-4. misleading quasi-topic residue
예:
- `LRM`
- `Sector`

특징:
- case-specific signal로 잡히지만
- 그 자체만으로는 사용자 층위를 여는 힌트가 되지 않는다
- 후속 summary 단계에서 그대로 노출되면 engine wording이 다시 강해진다

---

## 4. what improved

- broad concept probe 계열에서는 gloss가 꽤 안정적으로 먹힌다
- `AI의 미래`, `ontology/vectorfl` 둘 다
  - `설명/해석 층`
  - `비교/해석 흐름`
  - `전망/방향`, `구조/연결`, `구현/실행`
  같은 user-layer wording이 반복 가능하게 보인다
- interview middle-layer에서는 role gloss가 확실히 도움이 된다
- 즉 current gloss는 최소한
  - broad thematic probe
  - role-based case comparison
  에서는 이미 유효하다

---

## 5. what still interferes

- discourse residue는 특히 interview packet에서 너무 강하다
- middle-layer summary의 case-specific signal은 아직 raw token leakage가 있다
- concept probe의 user-layer hint는 broad theme에는 먹히지만
  interview-like narrow slice에는 아직 약하다
- 즉 지금 단계에서 더 필요한 것은
  - gloss proliferation
  가 아니라
  - residue down-weighting review
  - signal-to-summary translation 개선
  쪽이다

---

## 6. cross-case reading

### 안정적인 gloss
- `설명/해석 층`
- `비교/해석 흐름`
- `구현/실행 층`
- `근거/검증 층`
- `구조/연결`
- role gloss 3종:
  - `핵심 메커니즘 역할`
  - `반성/갭 역할`
  - `운영/배치 역할`

이들은 여러 사례에서 비교적 일관되게 읽힌다.

### 아직 사례 민감한 gloss
- interview packet의 `user_facing_summary`
- user-layer hint가 아주 적은 source에서의 opening summary

이쪽은 케이스에 따라 좋아 보이기도 하고,
아직 engine wording이 남아 있기도 하다.

---

## 7. recommended next step

- 1차 추천:
  - `residue down-weighting heuristic` 추가 검토
- 2차 추천:
  - middle-layer summary에서 raw token leakage를 줄이는 bounded wording refinement
- 계속 보류:
  - 사전류/백과사전류 투입
  - axis refactor
  - generalized taxonomy lock

즉 다음 단계는
**gloss를 더 많이 붙이는 것보다,
이미 붙인 gloss를 방해하는 residue를 줄이는 쪽**
이 맞다.

---

## 8. final judgment

- status: `PASS_WITH_NOTE`

한 줄로 요약하면:

- user-facing gloss는 broad concept probe에서는 반복 사용 가능한 수준까지 안정화되었지만, interview-like case에서는 residue 간섭이 여전히 커서 다음 bounded step은 lexicon thickening이 아니라 residue interference reduction review 쪽이 맞다.
