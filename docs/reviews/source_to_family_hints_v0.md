# Source-to-Family Hints v0

## 목적

이 문서는
artifact가 classifier 이전에 직접 남길 수 있는
`candidate family/projection/route hints` 최소 구조를 정한다.

이건
[line_only_traceability_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/line_only_traceability_check_v0.md)
에서 나온 두 번째 개선 방향이다.

즉 entry를 매번 signal/classifier만으로 열지 않고,
source artifact 자체가
이미 어떤 family 쪽인지 약한 힌트를 남기게 한다.

## 핵심 원칙

### 1. hint는 판정이 아니라 bias다

artifact hint는 classifier를 대체하지 않는다.

이건 확정 classification이 아니라
entry bias를 주는 약한 단서다.

### 2. hint는 source와 같이 저장된다

가능하면 comparison result, probe output, state snapshot 같은 artifact 안에
직접 들어가거나,
artifact와 같은 manifest에 붙는다.

### 3. hint는 family-rooted여야 한다

signal보다 더 위쪽에서
same-root 감각을 열어야 한다.

## 최소 hint 필드

- `candidate_family_ids`
- `candidate_projection_ids`
- `candidate_route_ids`
- `hint_confidence`
- `hint_reason`
- `hint_source_fields`
- `residue_reentry_bias`

## 필드 설명

### candidate_family_ids

이 artifact가 직접 가리키는 family 후보 목록

예:

- `fam_input_to_reading`
- `fam_transition_thickening`

### candidate_projection_ids

family 내부에서 먼저 열릴 가능성이 큰 projection 후보

예:

- `proj_preprocess_shaping`
- `proj_transition_preflight_reread`

### candidate_route_ids

처음 진입 시 강하게 연결되는 route 후보

예:

- `route_preprocess_compare_first`
- `route_preflight_reread`

### hint_confidence

`low / medium / high`

artifact가 얼마나 직접적으로 family 구조를 가리키는지

### hint_reason

왜 이 family/projection/route로 보이는지에 대한 짧은 설명

### hint_source_fields

artifact 내부에서 이 hint를 만든 필드 이름

예:

- `before_gate.decision`
- `after_gate.decision`
- `checkpoints.pre_ingest_gate.status`

### residue_reentry_bias

이 artifact가 다음 재진입 때
어느 family bias를 더 강하게 남기는지

예:

- `preservation_before_flattening`
- `closure_before_presentation`

## builder_choi 예시

[builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
기준으로 v0 hint를 적으면 아래처럼 된다.

```json
{
  "candidate_family_ids": [
    "fam_input_to_reading"
  ],
  "candidate_projection_ids": [
    "proj_preprocess_shaping"
  ],
  "candidate_route_ids": [
    "route_preprocess_compare_first"
  ],
  "hint_confidence": "high",
  "hint_reason": [
    "before gate says preprocess_required",
    "after gate remains uncertain_needs_probe",
    "entry should preserve future reading quality before flattening"
  ],
  "hint_source_fields": [
    "before_gate.decision",
    "after_gate.decision",
    "after_gate.checkpoints.pre_ingest_gate.status"
  ],
  "residue_reentry_bias": "preservation_before_flattening"
}
```

## 어디에 붙일 것인가

v0에서는 두 방식이 가능하다.

### 1. artifact 내부에 직접 붙인다

generated result JSON 안에
`vectorfl_family_hints` 같은 필드로 넣는다.

장점:

- source와 hint가 붙어 있다

단점:

- 기존 artifact schema를 건드려야 한다

### 2. companion manifest로 둔다

artifact path를 key로 하는
별도 manifest를 둔다.

장점:

- 기존 artifact를 덜 건드린다

단점:

- source와 hint가 분리된다

v0에서는 companion manifest가 더 안전하다.

## classifier와의 관계

classifier는 앞으로 아래 순서로 읽을 수 있다.

1. source artifact
2. source-to-family hints
3. signal_kind
4. family_rooted_alias
5. classifier rule
6. priority policy

즉 hint가 생기면
entry는 조금 더 line-centered해진다.

## 한 줄 요약

source-to-family hints v0는
artifact가 classifier 이전에 직접 남기는 약한 family/projection/route bias 구조다.
