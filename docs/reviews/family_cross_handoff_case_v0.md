# Family Cross Handoff Case v0

## 목적

이 문서는
[family_cross_handoff_demo_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/family_cross_handoff_demo_v0.md)
의 원칙을
실제 사례 하나로 고정한다.

이번 v0는 가장 자연스러운
`input -> transition`
handoff case를 쓴다.

## case 선택

source side:

- [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)

handoff target side:

- [runtime/current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [runtime/preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)

이 조합을 고른 이유는 아래와 같다.

- source 쪽은 entry ambiguity residue가 분명하다
- target 쪽은 transition blockage/thickening condition이 분명하다
- 두 쪽 모두 이미 hint/prebias/loop demo가 존재한다

## 1. source family state

source family는
`fam_input_to_reading`
이다.

source projection/route:

- `proj_preprocess_shaping`
- `route_preprocess_compare_first`

source observed status:

- `uncertain_needs_probe`

source residue:

- `preprocess ambiguity residue`
- `preservation_before_flattening`

이 상태의 의미는 명확하다.

- 입력은 아직 바로 canonical ingest로 닫히지 않았다
- line readiness는 input quality stabilization 이후에만 읽어야 한다
- 지금 질문은 아직 entry shaping question에 가깝다

## 2. handoff trigger

handoff는 source artifact 자체가 target artifact로 변해서 생기는 것이 아니다.

핵심 trigger는 아래와 같다.

- entry shaping question이 어느 정도 정리된다
- downstream에서 이제 `왜 여기서 막히는가` 또는 `현재 closure-ready인가` 질문이 열린다
- 질문의 중심이 input quality에서 transition condition으로 이동한다

즉 handoff 기준은
artifact change보다
question shift다.

## 3. target family entry

target family는
`fam_transition_thickening`
이다.

target source hint:

- [source_to_family_hints_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_to_family_hints_v0.json)
  의 `runtime/current_phase.json`
  또는 `runtime/preflight_last_decision.json` entry

target signal:

- `transition_blockage`

target projection/route:

- `proj_transition_preflight_reread`
- `route_preflight_reread`

target observed status:

- `thickening_active_not_closure_ready`

즉 handoff 이후 질문은 아래로 바뀐다.

- input family 질문:
  어떻게 넣을까
- transition family 질문:
  왜 아직 closure-ready가 아닌가

## 4. what actually moves across the handoff

handoff에서 실제로 넘어가는 것은
artifact 자체보다
question pressure와 residue bias다.

이번 케이스에서 넘어가는 것은 아래다.

- source residue:
  `preservation_before_flattening`
- handoff question shift:
  `entry shaping` -> `transition condition`
- target entry bias:
  `closure_before_presentation`

즉 input family residue는
“성급히 닫지 말라”는 bias를 남기고,
transition family는 그 bias를 더 좁은 형태로 받아
“closure-ready가 아님”을 reread하는 쪽으로 들어간다.

## 5. trace form

이번 handoff를 한 줄 trace로 적으면 아래다.

`builder_choi preprocess ambiguity residue -> question shifts from entry shaping to blockage/closure -> current_phase/preflight phase surface opens -> transition_blockage -> fam_transition_thickening -> proj_transition_preflight_reread -> route_preflight_reread`

## 6. why this matters

이 케이스가 중요한 이유는
family 간 이동이 임의 점프가 아니라는 점을 보여주기 때문이다.

- source family residue가 남는다
- 질문이 바뀐다
- target family artifact가 열린다
- target family hint가 생긴다
- new entry가 classifier에 의해 다시 고정된다

즉 handoff도
line-centered entry grammar 안에서 일어난다.

## 7. current limit

이 case는 아직
runtime engine이 자동으로 source residue를 읽어
target family를 연 것은 아니다.

현재는

- source-side interpretation
- target-side interpretation
- handoff reasoning

을 사람이 이어서 적은 것이다.

즉 다음 단계는
이 reasoning을 actual handoff policy나 residue-backed reentry rule로 내리는 일이다.

## 한 줄 요약

family cross handoff case v0는
`input family residue`가 바로 target artifact를 만들지는 않더라도,
질문을 `entry shaping`에서 `transition blockage/closure`로 이동시키며
`fam_transition_thickening` entry를 여는 concrete trace를 보여준다.
