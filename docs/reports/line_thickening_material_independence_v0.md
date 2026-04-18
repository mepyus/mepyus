# line_thickening_material_independence_v0

## what changed

- observation packet에 material anchor 계열을 추가했다.
  - `material_anchor_id`
  - `material_anchor_kind`
  - `material_source_path`
  - `material_anchor_summary`
- registry / promotion log에 material basis 축을 추가했다.
  - `distinct_material_anchor_count`
  - `distinct_primary_material_anchor_count`
  - `distinct_source_document_count`
  - `material_independence_summary`
- duplicate observation이어도 derived registry와 promotion basis를 다시 계산할 수 있게 refresh path를 추가했다.

## material anchor decision

- 이 repo에서는 `fragment_id`가 있으면 그걸 material anchor의 1급 기준으로 본다.
- 이유:
  - `internal_observer`와 `source_fragment_view`가 같은 fragment를 다른 path로 다시 보더라도 같은 underlying material임을 가장 안정적으로 보여주기 때문이다.
- `fragment_id`가 없으면 `source_path + source_range`, 그다음 row/source pointer를 쓴다.

## verification

실행:

```bash
python3 scripts/build_source_view.py runtime --record-line-thickening --fragment-id frag_basic4_003
```

이 실행은 duplicate append였지만, registry/promotion basis refresh를 통해 latest interpretation을 다시 계산했다.

같은 material across multiple paths 예시:

- `frag_basic3_002`
  - `internal_observer`
  - `source_fragment_view`
- `frag_basic4_003`
  - historical direct-span row
  - `source_fragment_view`

즉 current state는 path-wise로는 richer해졌지만, material axis를 따로 보면 same-material reread가 섞여 있다.

## current read

`transition_over_surface`

- `status=stable`
- `thickness_level=thick`
- `promotion_scope=cross_family_candidate`
- `distinct_path_count=3`
- `distinct_independent_evidence_count=2`
- `distinct_material_anchor_count=4`
- `distinct_primary_material_anchor_count=2`

핵심 해석:

- route diversity는 실제로 늘어났다.
- independent primary route도 2개다.
- 하지만 primary material breadth는 2로 읽는 것이 맞다.
- 즉 same material을 여러 path가 다시 본 부분이 있어, path diversity를 곧바로 material breadth로 읽으면 안 된다.

## why this matters

- current strongness를 깎으려는 작업이 아니다.
- 오히려 strong line을 더 정직하게 읽기 위한 작업이다.
- 지금 상태는:
  - cross-path = yes
  - cross-material = limited
  - therefore broader corroboration breadth is still bounded

## next condition

- 진짜 corroboration breadth를 더 넓히려면:
  - existing primary routes 위에
  - another distinct material anchor가 더 반복되어야 한다.
- 즉 다음 기준은 route를 더 붙이는 것이 아니라, same-material 재확인이 아닌 distinct material corroboration이 실제로 늘어나는가다.
