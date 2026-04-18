# line_thickening_primary_material_breadth_validation_v0

## cohort

observer cohort:

- `frag_basic3_002`
- `frag_basic4_003`
- `frag_ytex_001`
- `frag_ytex_002`
- `frag_basic_003`
- `frag_basic3_003`

source view cohort:

- `frag_basic3_002`
- `frag_basic4_003`

이 조합을 고른 이유:

- `frag_ytex_001`, `frag_ytex_002`는 same document / different fragment control이다.
- `frag_basic_003`, `frag_basic3_003`는 different document primary anchors다.
- `frag_basic3_002`, `frag_basic4_003`는 `transition_over_surface`용 known control이다.
- source view는 현재 `transition_over_surface`만 bounded sink로 내리므로 contrast anchors만 다시 본다.

## execution

```bash
python3 scripts/run_primary_material_breadth_validation.py runtime
```

## read

### transition_over_surface

- current state:
  - `status=stable`
  - `thickness_level=thick`
  - `promotion_scope=cross_family_candidate`
- key basis:
  - `distinct_path_count=3`
  - `distinct_independent_evidence_count=2`
  - `distinct_primary_material_anchor_count=2`

해석:

- path diversity는 실제로 열려 있다.
- 하지만 primary material breadth는 `2`에서 더 넓어지지 않는다.
- 즉 current strongness는 real이지만, corroboration breadth는 아직 bounded하다.

### input_to_reading_organ

- current state:
  - observer route 안에서 strong line
- key basis:
  - `distinct_primary_material_anchor_count`가 `transition_over_surface`보다 넓다
  - 하지만 source view 쪽 corroboration은 아직 없다

해석:

- 이 line은 current repo에서 `observer-local strong line`으로 읽는 것이 맞다.
- 즉 route breadth는 좁지만, primary material breadth는 비교적 넓다.

### pre_read_eye / raw_return_preservation

- 여전히 summary-level weak line이다.
- current breadth validation turn에서도 strong material line으로 오르지 않는다.

## why not broader/global

- `transition_over_surface`는 cross-path strong line이지만,
  current primary material breadth는 아직 `2`다.
- `input_to_reading_organ`은 material breadth가 더 넓어도,
  아직 observer route 중심이다.
- 따라서 둘 다 global breadth로 읽으면 과장이다.

## conclusion

- 이번 턴은 route 확장이 아니라 primary material breadth validation이었다.
- 결과는 다음처럼 읽는 편이 맞다.
  - `transition_over_surface` = cross-path strong, but still materially bounded
  - `input_to_reading_organ` = broader observer-local primary material line
  - `pre_read_eye`, `raw_return_preservation` = weak summary lines
