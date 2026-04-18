# multi lens document reading v0 skeleton note

## Purpose

이 note는 `multi_lens_document_reading_v0`의 첫 skeleton 범위를 기록한다.

목표는 line lens 적용의 출력 구조를 세우는 것이지,
정교한 strength scoring이나 문서 집계를 완성하는 것이 아니다.

## Implementation scope

- `SegmentLineReading` dataclass를 출력 계약 필드에 맞춰 추가했다
- `DocumentLineLensingResult` dataclass를 최소 문서 결과 표면으로 추가했다
- `MultiLensDocumentReader`는 registry에서 lens를 로드하고
  stable/thick lens와 나머지 lens를 분리한다
- `read()`는 입력 `LinkedSegment`마다 각 lens를 적용해 reading 목록을 만든다

## Lens loading

- registry source: `runtime/manifests/line_registry.json`
- primary lens: `status=stable` and `thickness_level=thick`
- secondary lens: 그 외 candidate/thin 포함 전체
- skeleton에서는 primary/secondary를 모두 읽되, 결과에서 분리 상태를 남긴다

## Reading strength heuristic

- keyword match가 있으면 `strong`
- keyword match가 없고 `linkage_confidence=low`이면 `weak`
- keyword match가 없고 lens가 candidate/thin이면 `caution`
- 나머지는 `absent`
- 이 heuristic은 v0 skeleton용이며 scoring formula가 아니다

## Probe result

- probe는 regression guard fixture의 linked segment를 입력으로 사용한다
- 결과는 `/tmp/multi_lens_document_reading_probe/probe_result.json`에 기록한다
- fixture별 linked segment 수, lens 사용 목록, reading 결과를 함께 남긴다

## TBD left untouched

- lens selection cutoff
- max lens count
- strength scoring formula
- document-level aggregation algorithm
- conflict handling
- dynamic lens reduction rule

## Next step

다음 단계는 stable/thick lens에 한해 reading_basis를 더 설명적으로 만드는 bounded refinement다.
