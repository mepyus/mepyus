# line_thickening_third_primary_route_validation_v0

## what changed

- third primary route 후보를 survey했다.
- valid 후보는 `scripts/build_source_view.py` 하나뿐이었다.
- 이 route에 `--record-line-thickening --fragment-id <id>` bounded sink를 추가했다.
- 선택한 line은 `transition_over_surface`다.

## why this route

- `source_fragment_view`는 observer route와 다른 validation path다.
- 동시에 `fragment_id`, `source_range`, `paragraph_index`, `source_path`를 유지하는 pointer-bearing output을 이미 만든다.
- generated report reread가 아니라 stored fragment row를 source-sorted state surface로 다시 읽는다.

## classification

- validation_path_id: `source_fragment_view`
- evidence_mode: `source_linked`
- evidence_origin_kind: `primary_structured`
- independence_class: `primary`

이 분류를 택한 이유:

- concrete pointer는 있다.
- 그러나 route output은 raw span 자체가 아니라 stored fragment row surface다.
- 따라서 `direct_span`이 아니라 `source_linked`가 더 정직하다.

## verification

실행:

```bash
python3 scripts/apply_internal_observer.py runtime frag_basic3_002 --record-line-thickening --bounded-recurrence-validation
python3 scripts/build_source_view.py runtime --record-line-thickening --fragment-id frag_basic3_002
```

결과:

- observer route:
  - `validation_path_id=internal_observer`
  - `evidence_origin_kind=primary_raw`
- third route:
  - `validation_path_id=source_fragment_view`
  - `evidence_origin_kind=primary_structured`
  - `source_pointer=runtime/reports/source_fragment_view.json#fragment_id=frag_basic3_002;source_range=262-719;paragraph_index=2`

registry state:

- `transition_over_surface`
  - `status=stable`
  - `thickness_level=thick`
  - `promotion_scope=cross_family_candidate`
  - `distinct_path_count=3`
  - `distinct_independent_evidence_count=2`

핵심 해석:

- third route는 실제로 추가되었다.
- `distinct_independent_evidence_count`도 2가 되었다.
- 하지만 derived/self-referential support가 여전히 남아 있어서 global로는 가지 않는다.

## why still not global

- current support set에는 `structured_doc_routing`에서 온 `derived_report / self_referential_derived`가 남아 있다.
- 따라서 지금 상태는
  - cross-path 는 맞고
  - second independent primary route도 생겼지만
  - still mixed evidence ecology 이다.
- 그래서 `global_candidate` 또는 `global_operating`으로 읽으면 과장이다.

## remaining boundary

- 이번 턴은 third route 하나만 추가했다.
- source_view route는 valid하지만 `primary_structured`이며, raw-only corroboration은 아니다.
- 다음에 truly broader corroboration을 말하려면:
  - existing repo 안의 또 다른 primary route가 실제로 있어야 하고
  - derived/self-referential support 의존도가 더 낮아져야 한다.
