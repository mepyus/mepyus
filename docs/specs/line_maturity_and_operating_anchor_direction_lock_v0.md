# line maturity and operating anchor direction lock v0

## verdict

- direction locked as document asset
- this turn does not implement new line behavior
- current line system remains a reading system first

## why this discussion matters

이 공간은 개념을 먼저 박아 넣는 방식이 아니라,
읽기 관측이 누적되며 line이 스스로 떠오르게 하는 역방향 온톨로지 구조를 따른다.

그래서 line의 장기 방향이 문서로 잠기지 않으면
입력기 보강, reread 방식, operating anchor 상상, 미래의 agent attachment가
한 층으로 섞여 버릴 수 있다.

이 note는 그 순서와 경계를 고정한다.

## technical summary

### what line is now

- line은 문서 하나의 단일 verdict를 고정하는 장치가 아니다.
- line은 같은 문서 안의 variation을 드러내는 reading lens다.
- 같은 문서 안에서도 살아나는 line, weak line, caution line이 함께 존재할 수 있다.
- line은 현재 해석 라벨이 아니라, 읽기 관측을 붙잡아 두는 축으로 다뤄야 한다.

### what line may become later

- line은 나중에 comparison memory가 될 수 있다.
- 그 다음에야 operating anchor 후보가 될 수 있다.
- 더 먼 미래에는 agent가 업무 종류만이 아니라 line 거점에 attach될 수 있다.
- 그러나 현재 line은 곧바로 agent station이 아니다.

### maturity stages

1. line as reading lens
   - 문서 하나를 단일 verdict로 닫지 않게 한다.
   - 같은 문서 안의 서로 다른 결을 동시에 드러낸다.

2. line as comparison memory
   - 여러 문서와 사례에서 line의 반복, 차이, caution을 비교 기억으로 남긴다.
   - line 이름보다 evidence grammar, caution, scope, maturity가 누적돼야 한다.

3. line as operating anchor
   - 반복되는 읽기와 비교가 쌓인 뒤에야 특정 작업이나 운영면이 line 위에서 붙을 수 있다.
   - 모든 line이 이 단계로 자동 승격되면 안 된다.

4. line as agent station
   - 미래상으로만 기록한다.
   - agent attachment는 line이 충분히 두터워진 뒤의 후속 가능성이지 현재 구현 대상이 아니다.

### known gaps

- 공간이 스스로 어디가 얇은가를 감지하는 루프가 아직 없다.
- line 간 관계가 없어 비슷한 line이 이름만 다르게 쌓일 수 있다.
- 새 line이 공간을 훑는 단방향은 있으나, 기존 line이 새 인풋을 역으로 읽는 루프가 없다.
- line이 충분히 두터워졌을 때 읽기를 줄이는 기준이 없다.
- 위 gap들은 이번 턴의 구현 대상이 아니라 인지 항목으로만 남긴다.

### next implementation order

1. `context_linked_segmentation_v0`
   - 입력기는 단순 분절기가 아니라 문맥이 끊긴 조각의 의미 연결을 복원하는 기계가 되어야 한다.
   - 이 단계가 없으면 같은 문서 안에서 어떤 line이 살아나는지조차 평평하게 눌린다.

2. `multi_lens_document_reading_v0`
   - segmentation이 의미 연결을 어느 정도 복원한 뒤에야 같은 문서를 여러 line lens로 읽는 것이 실제 의미를 가진다.
   - 이 순서가 뒤집히면 multi-lens는 flat shard 위의 이름 붙이기에 머문다.

### risks / non-goals

- 아직 모든 line을 operating anchor로 승격하지 말 것
- weak, local, caution line을 agent 거점처럼 쓰지 말 것
- 이름만 많은 line 체계로 가지 말 것
- line 이름보다 evidence grammar, caution, scope, maturity를 남길 것
- line 간 관계 없이 line 수만 늘리지 말 것
- 이번 note는 아래를 하지 않는다
- `context_linked_segmentation_v0` 코드 구현
- `multi_lens_document_reading_v0` 코드 구현
- line registry 구조 대개편
- agent framework 추가
- capability execution routing 확장
- broad refactor

## user-language summary

### what line is now

- line은 "이 문서의 정답은 이것"이라고 찍는 도장이 아니다.
- 한 문서 안에 여러 결이 동시에 살아날 수 있게 여는 읽기 축이다.
- 그래서 살아나는 line, weak line, caution line을 함께 봐야 한다.

### what line may become later

- 나중에는 여러 문서에서 반복되는 결을 비교 기억으로 쌓을 수 있다.
- 그보다 더 나중에야 어떤 line이 실제 운영 거점 후보인지 말할 수 있다.
- agent가 line 위에 붙는 그림은 그 다음 미래상이다.

### maturity stages

1. 먼저 line은 읽기 렌즈다.
2. 그 다음 line은 비교 기억이 된다.
3. 그 다음에야 operating anchor 후보가 된다.
4. agent station은 더 먼 미래 이야기다.

### known gaps

- 아직 공간은 스스로 "어디가 얇은가"를 잘 모른다.
- 비슷한 line끼리의 관계도 아직 없다.
- 기존 line이 새 문서를 거꾸로 다시 읽는 루프도 아직 없다.
- 충분히 두터워진 뒤 읽기를 줄이는 기준도 아직 없다.
- 하지만 이것들은 지금 당장 구현할 항목이 아니라, 알고 있어야 할 빈칸이다.

### next implementation order

1. `context_linked_segmentation_v0`
2. `multi_lens_document_reading_v0`

이 순서가 필요한 이유는 먼저 문서 조각의 의미 연결을 복원해야,
그 다음에 같은 문서를 여러 line으로 여는 읽기가 의미를 가지기 때문이다.

### risks / non-goals

- 지금은 line을 operating anchor처럼 과장하지 않는다.
- weak/local/caution line을 거점처럼 다루지 않는다.
- line 이름만 많이 만드는 방향으로 가지 않는다.
- 지금은 agent attachment 구현을 하지 않는다.

## user-language restatement

지금 잠근 핵심은 단순하다.

- line은 아직 operating anchor가 아니다.
- line은 먼저 reading lens로 살아야 한다.
- 그 다음 comparison memory가 되어야 한다.
- operating anchor는 그 다음이며, agent station은 미래상으로만 남긴다.
- 다음 구현 순서는 `context_linked_segmentation_v0 -> multi_lens_document_reading_v0`로 고정한다.

## one-line lock

- line maturity order is fixed as `reading lens -> comparison memory -> operating anchor -> agent station`
- next implementation order is fixed as `context_linked_segmentation_v0 -> multi_lens_document_reading_v0`
