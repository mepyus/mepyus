# Line-Only Traceability Check v0

## 목적

이 문서는
[loop_demo_case_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_v0.md)
를 기준으로
이번 구조가 정말 `line`만으로 추적 가능한지 점검한다.

핵심 질문은 하나다.

`source -> family -> projection -> route -> residue`
가 artifact나 policy 문서 도움 없이도 충분히 따라갈 수 있는가.

## 결론 먼저

현재 v0에서는
`완전한 line-only traceability` 는 아직 아니다.

더 정확히는:

- family 안에 들어간 뒤에는 line-only 추적력이 꽤 강하다
- 하지만 entry classification 단계는 아직 signal/classifier/artifact scaffolding에 의존한다

즉 지금 구조는
`entry 이전 = non-line scaffolding 필요`
`entry 이후 = line spine 중심 추적 가능`
상태에 가깝다.

## 1. line-only로 이미 강한 구간

아래 구간은 line만으로 추적력이 꽤 있다.

### 1-1. family grounding 이후

한 번 `fam_input_to_reading` 으로 들어가면
아래는 line 중심으로 유지된다.

- root invariant
- same-root 여부
- family purpose
- completion question

즉 이 단계부터는
“이게 어떤 line family인가”
가 비교적 안정적으로 유지된다.

### 1-2. projection 선택

projection은 line family 내부의 다른 투영면이라서
line-only 추적에 잘 맞는다.

예:

- `proj_input_ingest_visibility`
- `proj_preprocess_shaping`

이 둘의 차이는
절차 차이이기도 하지만,
더 근본적으로는 같은 family 안에서 어떤 facet를 바꾸는가의 차이다.

그래서 projection registry는
line-only 관점에서도 꽤 자연스럽다.

### 1-3. route 선택 이후

route는 line family/projection 위에서
현재 어떤 active route를 타는가를 보여준다.

예:

- `route_preprocess_compare_first`
- `route_input_direct_ingest`

이 단계에서는
`현재 같은 root family 안에서 어느 방향으로 읽고 있는가`
를 따라가기 쉬워진다.

### 1-4. residue return

residue는 line-only 추적의 강한 지점이다.

이번 케이스에서
`preprocess ambiguity residue`
는
다음에도 `preservation before flattening` 질문을 되살리는 방식으로 남는다.

즉 residue는 line history를 다시 family 안으로 되먹이는 매개다.

## 2. line-only가 아직 약한 구간

아래 구간은 아직 line만으로는 부족하다.

### 2-1. source/artifact 해석

실제 시작은 line이 아니라 artifact다.

이번 케이스도 출발점은
[builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
이다.

여기서

- `before_gate.decision = preprocess_required`
- `after_gate.decision = uncertain_needs_probe`

같은 신호를 읽어야
line entry가 열린다.

즉 line은 source를 대체하지 못한다.
source reading은 여전히 필요하다.

### 2-2. signal taxonomy

`preprocess_ambiguity`
같은 signal은
line 자체라기보다
artifact를 line family로 보내기 위한 translator vocabulary다.

이건 현재로서는 필수 scaffolding이다.

즉 signal taxonomy 없이
artifact를 바로 family로 보내기는 아직 어렵다.

### 2-3. classifier rule

이번 데모가

- `fam_input_to_reading`
- `proj_preprocess_shaping`
- `route_preprocess_compare_first`

로 들어간 것도
자연 발생이 아니라 classifier rule 덕분이다.

즉 same-root 감각만으로 entry를 결정하는 게 아니라,
rule-based entry grammar가 중간에 있다.

### 2-4. priority policy

signal이 겹칠 때는

- override beats default
- narrower signal beats broader signal

같은 policy가 필요하다.

이건 pure line object가 아니라
entry governance에 가깝다.

## 3. 지금 구조를 어떻게 읽는 것이 맞는가

현재 구조를 정직하게 읽으면 이렇다.

### 3-1. line-only system이 아니라 line-centered system

지금은
`line-only`
보다
`line-centered`
라는 표현이 더 맞다.

중심 spine은 line family/projection/route이지만,
입구에는 아래 보조 구조가 필요하다.

- source reading
- signal vocabulary
- classifier rules
- priority policy

### 3-2. entry 이후에 line성이 강해진다

한 번 family에 들어간 뒤부터는
line/facet/projection/route/residue 구조가 주도권을 가진다.

즉 지금 V0의 실제 강점은
`entry classification 이후의 line spine`
에 있다.

## 4. 그러면 무엇이 더 필요하나

line-only 추적력을 더 높이려면
아래 세 가지 중 하나 이상이 더 필요하다.

### 4-1. line-rooted signal grammar

signal을 artifact vocabulary가 아니라
family invariant vocabulary에 더 가깝게 바꾸는 일.

예:

- `preprocess_ambiguity`
를 단순 상태명이 아니라
`input family preservation conflict`
처럼 family-rooted하게 적는 방식.

### 4-2. source-to-family direct hints

artifact가 직접
`candidate_family_ids`
또는
`candidate_projection_ids`
를 남기게 만드는 방식.

그러면 classifier 의존도가 줄어든다.

### 4-3. residue-backed reentry

재진입 시에는 signal보다 residue/family history를 더 강하게 보게 만드는 방식.

그러면 첫 진입보다 두 번째 진입부터는 line-only 추적성이 강해진다.

## 5. v0 판단

현재 기준으로는 아래 판단이 가장 정확하다.

- line만으로 전체를 추적하는 단계는 아직 아니다
- 그러나 family 진입 이후에는 line spine이 꽤 강하다
- 지금 필요한 것은 line을 버리는 것이 아니라
  entry 쪽 scaffolding를 점점 family-rooted하게 바꾸는 일이다

## 한 줄 요약

현재 VectorFL v0는
`artifact와 signal이 entry를 열고, family/projection/route/residue가 그 이후를 추적하는 line-centered system`
으로 보는 것이 가장 정확하다.
