# line maturity discussion handoff v0

## verdict

- discussion locked as handoff note
- no new implementation was added in this turn
- line maturity direction is now document-fixed

## why this discussion matters

line을 읽기 라벨에서 operating anchor 후보로 키워가는 장기 방향이 잠기지 않으면,
앞단 입력기 보강과 중단 reread 확장, 그리고 더 먼 미래의 agent attachment 상상이
한 번에 섞여 구현 우선순위가 흔들릴 수 있다.

이번 handoff는 그 흔들림을 막기 위한 정리다.

## technical summary

### what line is now

- line is not a single-document verdict machine
- line must allow multiple live readings inside one document
- one fragment can support one line while an adjacent fragment stays weak or caution-only
- line should currently be treated as a reading lens, not as an operating station

### what line may become later

- line may later serve as comparison memory across documents and cases
- after enough repeated reading, some lines may become operating anchor candidates
- agent attachment remains a future-layer possibility only

### maturity stages

1. reading lens
2. comparison memory
3. operating anchor
4. agent station

### known gaps

- the space still lacks a loop for sensing where it is thin
- line-to-line relations are still missing, so near-duplicate lines may accumulate
- new line scans exist, but reverse rereading from existing lines into new input does not
- there is no clear basis yet for reading less once a line becomes thick enough
- these are recognition items, not implementation targets for this turn

### next implementation order

1. `context_linked_segmentation_v0`
   - meaning-poor shards still collapse too much reading into flat fragments
   - before multi-line reading becomes credible, fragment linkage has to improve

2. `multi_lens_document_reading_v0`
   - only after linkage improves does one document become meaningfully open to multiple lines
   - otherwise multi-lens reading becomes naming over flat material

### risks / non-goals

- do not promote all lines into operating anchors
- do not use weak, local, or caution lines as agent bases
- do not increase line count without evidence grammar, caution, scope, and maturity
- do not expand agent framework, execution routing, or registry structure in this turn
- no code implementation is included here

## user-language summary

### what line is now

- 지금 line은 "이 문서의 정답"을 박는 장치가 아니다.
- 한 문서 안에서 여러 line이 동시에 살아날 수 있게 하는 읽기 렌즈다.

### what line may become later

- 나중에는 그 line이 다른 문서에서도 반복되는지 비교 기억으로 쌓일 수 있다.
- 더 나중에야 operating anchor 후보가 될 수 있다.
- agent가 붙는 구조는 그 이후 미래상이다.

### maturity stages

1. reading lens
2. comparison memory
3. operating anchor
4. agent station

### known gaps

- 아직 공간은 어디가 얇은지 스스로 잘 감지하지 못한다.
- line끼리의 관계도 없다.
- 기존 line이 새 문서를 거꾸로 읽는 루프도 없다.
- 충분히 두터워지면 읽기를 줄이는 기준도 아직 없다.
- 하지만 이번 턴은 이 문제들을 구현하는 턴이 아니다.

### next implementation order

1. `context_linked_segmentation_v0`
2. `multi_lens_document_reading_v0`

먼저 문서 조각의 의미 연결을 살려야,
그 다음에 같은 문서를 여러 line으로 여는 읽기가 의미를 가진다.

### risks / non-goals

- 지금은 모든 line을 operating anchor처럼 다루지 않는다.
- weak/local/caution line을 agent 거점처럼 쓰지 않는다.
- line 이름만 늘리는 방향으로 가지 않는다.
- agent attachment 구현은 하지 않는다.
- broad implementation은 열지 않는다.

## user-language restatement

이번 턴에서 잠근 말은 이것이다.

- line은 먼저 reading lens다.
- 그 다음 comparison memory가 된다.
- operating anchor는 그 다음 단계다.
- agent station은 미래상으로만 남긴다.
- 다음 구현 순서는 `context_linked_segmentation_v0 -> multi_lens_document_reading_v0`다.

## reopen note

이 discussion은 아래 상황에서 다시 연다.

- `context_linked_segmentation_v0` 구현을 시작할 때
- `multi_lens_document_reading_v0` 구현을 시작할 때
- line을 operating anchor 후보로 실제 분류하려는 요구가 생길 때
- agent attachment를 현재형 설계처럼 말하려는 움직임이 생길 때
