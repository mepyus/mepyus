# multi lens document reading v0 contract spec

## verdict

- contract draft locked as document asset
- this turn does not implement reading code
- this spec defines only the minimum input/output contract for `multi_lens_document_reading_v0`

## purpose

`multi_lens_document_reading_v0`는 문서 하나를 단일 verdict로 닫는 모듈이 아니다.

목적은 `linked_segment` 위에 여러 line lens를 병렬 적용해,
같은 문서 안에서도 어떤 조각은 특정 line이 강하게 살아나고,
어떤 조각은 weak 또는 caution으로 남는 variation을 드러내는 것이다.

이 계약은 그 입력과 출력의 최소 형태를 고정한다.

## input contract

### input unit

- input unit is `linked_segment`
- `linked_segment`는 `context_linked_segmentation_v0`의 출력 단위다
- 이 단위는 하나 이상의 segment가 의미 연결 복원 근거를 바탕으로 다시 묶인 읽기 surface다

### required linked_segment fields

- `linked_segment_id`
- `source_id`
- `segment_ids`
- `linked_text`
- `linkage_reason`
- `linkage_confidence`
- `provenance`

### optional linked_segment fields

- `secondary_linkage_reasons`
- `boundary_notes`
- `open_questions`
- `context_window_segment_ids`
- `metadata`

### line lens source

- 적용할 line lens 목록은 `runtime/manifests/line_registry.json`에서 읽는다
- 기본 우선 대상은 `status=stable` 이고 `thickness_level=thick` 인 line이다
- `candidate` 또는 `thin` line을 lens로 사용할 경우 별도 표시가 필요하다
- lens selection cutoff, max lens count, fallback selection rule은 `TBD`

### input preconditions

- 입력 `linked_segment` 목록은 같은 `source_id` 안에서 순서가 보존되어야 한다
- 각 `linked_segment_id`는 같은 입력 배치 안에서 유일해야 한다
- 각 `linked_segment`는 `segment_ids`, `linkage_reason`, `linkage_confidence`, `provenance`를 포함해야 한다
- line lens 목록은 최소한 `line_id`, `line_name`, `status`, `thickness_level`을 제공해야 한다
- 서로 다른 source를 하나의 reading pass에서 섞는 방식은 `TBD`

## output contract

### output unit

- output unit is `segment_line_reading`
- `segment_line_reading`은 하나의 `linked_segment`와 하나의 line lens가 만났을 때의 읽기 결과다
- 이 단위는 verdict가 아니라 line별 읽기 상태 기록이다

### required output fields

- `linked_segment_id`
  - 어떤 linked segment에 대한 결과인지
- `source_id`
  - 원본 문서 또는 입력 surface 식별자
- `line_id`
  - 적용한 line 식별자
- `line_name`
  - 적용한 line 이름
- `reading_strength`
  - `strong / weak / caution / absent`
- `reading_basis`
  - 왜 이 strength로 읽혔는지에 대한 최소 근거
- `provenance`
  - 이 reading이 어느 pass, 어떤 lens source, 어떤 입력 surface에서 나왔는지의 최소 출처 정보

### conditional output fields

- `caution_reason`
  - `reading_strength=caution`일 때만 명시
- `lens_maturity_note`
  - `candidate` 또는 `thin` line을 lens로 썼을 때 명시

### optional output fields

- `basis_spans`
- `competing_lines`
- `open_questions`
- `metadata`

### output preconditions

- 하나의 `segment_line_reading`은 정확히 하나의 `linked_segment_id`와 하나의 `line_id`에만 대응해야 한다
- `reading_strength`는 반드시 `strong`, `weak`, `caution`, `absent` 중 하나여야 한다
- `reading_basis` 없이 non-absent 결과를 내는 것은 유효하지 않다
- `caution_reason`은 `caution`일 때만 채우고, 나머지 경우는 비워 두거나 생략한다
- `provenance`는 사람이 사후에 어떤 lens 적용이었는지 추적할 수 있을 정도의 최소 설명을 포함해야 한다

## reading strength taxonomy

- `strong`
  - 이 `linked_segment`에서 해당 line이 강하게 살아난다
- `weak`
  - line은 살아나지만 증거가 얇거나 제한적이다
- `caution`
  - line은 살아나지만 overread, local-only, summary echo 같은 위험이 함께 붙는다
- `absent`
  - 이 `linked_segment`에서는 해당 line이 살아나지 않는다

strength 판정 기준의 세부 점수식은 `TBD`다.

## document-level variation map

- 한 문서의 `segment_line_reading` 전체를 모으면 `document_line_variation_map`을 구성할 수 있다
- 이 map의 최소 역할은 문서 내부에서 어떤 line이 어디서 strong, weak, caution, absent인지 펼쳐 보이는 것이다
- 최소 집계 단위는 `source_id` 기준 전체 reading collection이다
- 최소 집계 필드는 아래를 포함한다
- `source_id`
- `linked_segment_ids`
- `segment_line_readings`
- `used_line_ids`
- `aggregation_provenance`
- 집계 알고리즘, 요약 방식, 우선순위 규칙은 `TBD`

## connection to context_linked_segmentation_v0

- `context_linked_segmentation_v0`의 출력 필드가 이 모듈의 입력 필드로 그대로 들어온다
- 필수 매핑은 아래와 같다
- `linked_segment_id -> linked_segment_id`
- `source_id -> source_id`
- `segment_ids -> segment_ids`
- `linked_text -> reading surface text`
- `linkage_reason -> reading context signal`
- `linkage_confidence -> linkage confidence input`
- `provenance -> input provenance`
- 실제 런타임 배선, 함수 시그니처, 호출 순서는 이 문서 범위 밖이다

## connection to line_registry

- line lens 후보는 `runtime/manifests/line_registry.json`에서 읽는다
- 기본 우선 순위는 `status=stable` 이고 `thickness_level=thick` 인 line이다
- `candidate` 또는 `thin` line을 lens로 쓸 때는 `lens_maturity_note` 등으로 별도 표기해야 한다
- line registry의 구조 변경은 이 문서 범위 밖이다
- 어떤 line을 제외할지, 몇 개까지 읽을지, 동적 lens 축소 규칙은 `TBD`

## what this is not

- this is not a code implementation
- this is not a promise that one document will collapse into a single correct line
- this is not a line registry schema change
- this is not a line-to-line relation spec
- this is not a document aggregation algorithm spec
- scoring formula, conflict handling, and lens selection policy remain `TBD`

## one-line lock

`multi_lens_document_reading_v0` takes ordered `linked_segment` inputs and returns per-line `segment_line_reading` outputs so document-internal line variation stays visible instead of collapsing into one verdict.
