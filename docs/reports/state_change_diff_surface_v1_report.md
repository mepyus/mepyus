[[A]] [[OBJ:state_change_diff_surface_v1_report]] [[SEM:report_for_adjacent_state_diff_surface_on_process_console]]

# state_change_diff_surface_v1_report

## 1. purpose

- 이번 report의 목적은 process console에 adjacent canonical state diff surface를 연결한 범위와 현재 representative diff 양상을 기록하는 것이다.

## 2. diff source and calculation

- authoritative diff source:
  - asset history jsonl
- pair selection:
  - latest vs previous
  - selected history item vs immediate previous
- changed field calculation:
  - canonical 8필드 기준
  - scalar field는 strict compare
  - array field는 set-like compare

## 3. provenance_only rule

- 아래 조건이면 `provenance_only`로 읽는다.
  - `changed_fields = []`
  - update trigger / reason / evidence refs는 달라도 canonical 8필드 변화 없음

이번 representative run의 latest runtime append는 모두 이 규칙에 해당했다.

## 4. connected UI points

- state panel:
  - `DiffSummaryStrip`
- history timeline item:
  - `compare to previous` link
- right panel:
  - `StateChangeDiffPanel`
  - diff class
  - changed field chips
  - field-level rows
  - evidence refs summary

## 5. representative read

### latest vs previous

- `youtube_03_22`
  - `diff_class = provenance_only`
  - `changed_fields = []`
- `openai_02_11`
  - `diff_class = provenance_only`
  - `changed_fields = []`
- `knowledge_editing_youtube`
  - `diff_class = provenance_only`
  - `changed_fields = []`
- `gary_tan_brain`
  - `diff_class = provenance_only`
  - `changed_fields = []`

### read

- 현재 latest runtime append는 canonical drift를 만들지 않고 provenance를 보강하는 adoption run이었기 때문에, diff surface에서 `provenance_only`로 읽히는 것이 맞다.
- 이 값은 실패가 아니라, canonical state 안정성을 유지한 채 evidence/provenance만 풍부해졌다는 뜻으로 읽는다.

### oldest boundary fallback

- `knowledge_editing_youtube`, `gary_tan_brain`에서 마지막 record를 기준으로 열면 `no_previous_state` fallback이 정상 동작했다.

## 6. canonical vs experimental separation

- diff 본문은 canonical 8필드만 직접 비교한다.
- experimental namespace는 기본 숨김이며 presence만 간접적으로 유지한다.
- naming-heavy 값은 canonical change처럼 보이지 않는다.

## 7. remaining limits

- representative history에는 아직 real canonical drift 사례가 적어서, current diff surface는 provenance-only와 no-previous fallback을 더 강하게 보여주는 상태다.
- old/new full snapshot dump는 expand형까지는 아니고 현재는 changed rows 중심이다.
- same-record neutral handling, malformed item warning UI는 후속 보강 여지가 있다.

## 8. one-line verdict

> 이번 diff surface로 process console은 단순 lineage를 넘어서, adjacent canonical state 사이에서 실제 변화와 무변화를 빠르게 읽는 얇은 변화면까지 갖추게 됐다. 현재 representative latest run은 모두 provenance_only로 읽히며, 이는 canonical 안정성을 유지한 adoption append라는 뜻이다.
