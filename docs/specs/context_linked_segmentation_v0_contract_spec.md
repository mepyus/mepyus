# context linked segmentation v0 contract spec

## verdict

- contract draft locked as document asset
- this turn does not implement segmentation code
- this spec defines only the minimum input/output contract for `context_linked_segmentation_v0`

## purpose

`context_linked_segmentation_v0`는 단순 분절기가 아니다.

목적은 이미 잘린 segment들을 다시 길게 늘이는 것이 아니라,
혼자 두면 의미가 약한 조각들이 앞뒤 문맥과 다시 묶이며
여러 line이 살아날 수 있는 linked segment surface를 만드는 것이다.

이 계약은 그 입력과 출력의 최소 형태를 고정한다.

## input contract

### input unit

- input unit is `segment`
- `segment`는 한 번의 초기 분절 이후 남은 최소 읽기 조각이다
- 이 조각은 독립 의미 단위일 수도 있고, 혼자 두면 약한 의미 조각일 수도 있다

### required input fields

- `segment_id`
  - segment의 안정 식별자
- `source_id`
  - 이 segment가 나온 문서 또는 입력 surface 식별자
- `text`
  - 원문 조각 텍스트
- `order_index`
  - 원문 안에서의 순서
- `start_anchor`
  - 원문 기준 시작 위치 정보
- `end_anchor`
  - 원문 기준 끝 위치 정보
- `speaker_id`
  - 화자 기반 자료인 경우 화자 식별자, 아니면 `TBD`
- `segment_type`
  - 입력 조각의 1차 분절 유형, enum은 `TBD`
- `provenance`
  - 이 조각이 어떤 분절 경로를 통해 생성됐는지의 최소 출처 정보

### optional input fields

- `section_id`
- `paragraph_id`
- `previous_segment_id`
- `next_segment_id`
- `language`
- `metadata`

### input preconditions

- 입력은 같은 `source_id` 안에서 순서가 보존된 `segment` 목록이어야 한다
- 각 `segment_id`는 같은 입력 배치 안에서 유일해야 한다
- `text`는 빈 문자열이면 안 된다
- `start_anchor`와 `end_anchor`는 원문 위치를 재구성할 수 있을 정도의 최소 정보여야 한다
- 인접성 판단에 필요한 `order_index` 누락 입력은 계약 위반으로 본다
- 서로 다른 source를 하나의 linkage pass에서 섞는 방식은 `TBD`

## output contract

### output unit

- output unit is `linked_segment`
- `linked_segment`는 하나 이상의 인접 또는 준인접 segment가
  의미 연결 복원 근거를 바탕으로 다시 묶인 읽기 단위다
- `linked_segment`는 line verdict가 아니라, 이후 읽기를 열기 위한 재구성 surface다

### required output fields

- `linked_segment_id`
  - 출력 단위 식별자
- `source_id`
  - 원본 문서 또는 입력 surface 식별자
- `segment_ids`
  - 묶인 조각 id 목록
- `linked_text`
  - 묶인 조각을 순서대로 재구성한 텍스트
- `linkage_reason`
  - 왜 이 조각들이 묶였는가를 나타내는 주 reason
- `linkage_confidence`
  - `high / medium / low`
- `provenance`
  - 이 연결이 어느 pass, 어느 규칙, 어느 입력 경로에서 왔는가에 대한 최소 출처 정보

### optional output fields

- `secondary_linkage_reasons`
- `boundary_notes`
- `open_questions`
- `context_window_segment_ids`
- `metadata`

### output preconditions

- `segment_ids`는 비어 있으면 안 된다
- `segment_ids`의 순서는 원문 순서를 따라야 한다
- 하나의 `linked_segment`는 단일 `source_id` 안에서만 구성된다
- `linkage_reason` 없이 묶인 출력은 유효하지 않다
- `linkage_confidence`는 반드시 `high`, `medium`, `low` 중 하나여야 한다
- `provenance`는 사람이 사후에 왜 묶였는지 추적할 수 있을 정도의 최소 설명을 포함해야 한다

## linkage reason taxonomy

아래 taxonomy는 v0 최소 집합이다.

- `unfinished_claim`
  - 앞 조각의 주장이 미완성이고 다음 조각이 그 뜻을 완료한다
- `answer_completion`
  - 질문, 문제 제기, 설정 이후 다음 조각이 직접 답하거나 닫는다
- `speaker_continuation`
  - 같은 화자의 발화가 인위적 분절로 끊겼고 이어 붙여야 의미가 살아난다
- `setup_to_mechanism`
  - 배경 설명 뒤에 작동 방식, 절차, 구조가 이어져 하나의 의미 덩어리를 이룬다
- `causal_chain`
  - 원인과 결과, 조건과 귀결이 분리돼 있어 다시 묶어야 한다
- `contrast_pair`
  - 대비, 반전, before/after, 그러나/반면 등이 짝을 이루며 함께 읽혀야 한다

추가 taxonomy는 `TBD`다.

## boundary conditions

### when not to link

- 조각이 이미 독립 의미 단위로 충분히 서 있을 때
- 인접해 있어도 주제 전환이 명확할 때
- 화자가 같아도 의미 연결 근거가 약할 때
- 단순 길이 확장을 위해 묶는 경우

### when forced linkage is not allowed

- linkage reason이 텍스트 근거 없이 추정에만 의존할 때
- 서로 다른 의미 방향을 하나로 눌러 line variation을 지워 버릴 때
- weak segment를 살리기보다 unrelated segment를 끌어와 덮어버릴 때
- linkage가 오히려 이후 multi-lens reading을 좁히는 경우

### when linkage reason is unclear

- 기본 동작은 억지로 묶지 않는 쪽에 둔다
- 필요하면 단일 segment를 그대로 통과시킬 수 있다
- `linkage_confidence`를 `low`로 두고 보조 메모를 남기는 방식은 `TBD`
- 복수 reason 경쟁 시 우선순위 결정 규칙은 `TBD`

## connection to multi_lens_document_reading_v0

- `context_linked_segmentation_v0`의 출력 `linked_segment` 목록은
  `multi_lens_document_reading_v0`의 입력 surface 후보가 된다
- 여기서 중요한 접점은 다음뿐이다
- multi-lens reading은 raw flat segment 대신 linked segment를 읽는다
- 각 linked segment는 `segment_ids`, `linkage_reason`, `linkage_confidence`, `provenance`를 함께 전달해야 한다
- 이를 통해 이후 읽기 단계는 어떤 의미 연결이 복원된 상태인지 알고 여러 line을 열 수 있다
- 실제 런타임 연결 방식, 함수 시그니처, 파이프라인 배선은 이 문서 범위 밖이다

## what this is not

- this is not a code implementation
- this is not a promise that segmentation ambiguity is automatically resolved
- this is not a line registry change
- this is not a `multi_lens_document_reading_v0` spec
- this is not a broad input pipeline refactor
- scoring formula, adjacency window size, and merge algorithm remain `TBD`

## one-line lock

`context_linked_segmentation_v0` takes ordered `segment` inputs and returns reasoned `linked_segment` outputs so weak fragments can be context-restored before multi-lens reading begins.
