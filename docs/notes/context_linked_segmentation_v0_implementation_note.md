# context linked segmentation v0 implementation note

## Purpose

이 note는 `context_linked_segmentation_v0`의 첫 구현 범위를 좁게 기록한다.

목표는 계약에 잠긴 입력/출력 표면을 코드로 내리는 것이지,
고도화된 의미 복원 엔진을 여는 것이 아니다.

## Implemented decisions

- `Segment` dataclass를 입력 계약 필드 그대로 추가했다
- `LinkedSegment` dataclass를 출력 계약 필드 그대로 추가했다
- `ContextLinkedSegmenter.link()`는 순서 보존 입력을 받아 순차 병합으로 `LinkedSegment` 목록을 만든다
- adjacency window는 기본값 `2`로 고정했다
- linkage reason 판단은 LLM 없이 규칙 기반 휴리스틱으로 시작했다
- 묶이지 않는 조각은 단독 `LinkedSegment`로 남긴다
- probe 스크립트는 `/tmp/context_linked_segmentation_probe` 아래에만 결과를 쓴다

## Current heuristics

- 문장이 `:`, `;`, `,` 또는 일부 접속형 어미로 끝나면 `unfinished_claim` 후보
- 앞 조각이 질문으로 끝나고 다음 조각이 서술이면 `answer_completion` 후보
- 인접 조각의 `speaker_id`가 같으면 `speaker_continuation` 후보
- 다음 조각이 `예를 들면`, `즉`, `왜냐하면` 등으로 시작하면 `setup_to_mechanism` 후보
- 다음 조각이 `하지만`, `반면`, `그러나`로 시작하면 `contrast_pair` 후보
- 현재 조각 또는 다음 조각에 `그래서`, `때문에`, `따라서`, `결과적으로`가 있으면 `causal_chain` 후보

## TBD left intentionally

- scoring formula
- adjacency window size tuning beyond default `2`
- merge algorithm beyond simple sequential merge
- `segment_type` enum
- multiple linkage reason priority rule
- low-confidence auxiliary memo format

## What was not changed

- no main runtime wiring
- no `inputter.py` change
- no `labeler.py` change
- no `line_registry` change
- no `multi_lens_document_reading_v0` connection

## Next step

다음 단계는 probe fixture를 몇 가지 문서 유형으로 늘려
휴리스틱의 오탐과 누락 패턴만 확인하는 것이다.
