# line thickening second grounded route note v0

## 목적
`line_thickening`의 첫 grounded route는 `scripts/apply_internal_observer.py`였다.
이번 노트는 그 다음 단계로, 실제로 다른 validation path 하나를 추가할 때 어떤 경로를 고르고 어떤 anchor를 붙였는지 정리한다.

## 선택한 second route
- `scripts/process_structured_doc_with_routing.py`

## 왜 이 경로인가
- 기존 fragment observer route와 path-wise로 다르다.
- structured doc routing은 `observer_ingest_min`을 호출해 `source_manifest`, `split_units`, `processing_trace`, `readable_input_board`, `operator_summary`를 만든다.
- 이 출력에는 `split_units_<run_id>.json#unit_id=...;start_ref=...;end_ref=...` 같은 concrete pointer가 있다.
- 따라서 summary echo가 아니라 concrete row/span anchor를 가진 grounded feed를 만들 수 있다.

## evidence mode
- `direct_span`을 우선 사용했다.
- pointer는 `split_units` row와 그 row의 `start_ref/end_ref`를 조합해 만들었다.
- 실제 역추적이 약했으면 `source_linked`로 낮추는 것이 맞지만, 이번 경로는 row pointer가 살아 있어 `direct_span`으로 기록했다.

## line 선택
- second route는 `transition_over_surface`에 붙였다.
- 이유: observer route와 structured doc routing 모두 surface transition / readable split 성격을 갖고, `distinct_path_count=2`를 열기 좋은 강하지만 전역화하기 어려운 라인이다.

## 경계
- 새 entrypoint는 만들지 않는다.
- observer route 본체와 structured doc routing 본체를 바꾸지 않는다.
- line_thickening은 sink로만 붙인다.
- global label은 열지 않는다.
