# external input gate v0

## Purpose

이 note는 외부자료가 들어오기 전에
`바로 ingest 가능한지 / 전처리가 먼저 필요한지 / 아직 애매한지`
를 먼저 판정하는 front-door gate를 고정하기 위한 문서다.

핵심은 line 판독보다 앞단 품질을 먼저 잠그는 것이다.

## Why now

`builder_choi_interview.txt` 같은 transcript-like `.txt`는
현재 inputter에 바로 넣으면 의미문장보다 subtitle-like shard로 쪼개진다.

문제는 뒤에서 trace/cell이 생기더라도,
그것이 semantic regroup이 아니라 coarse aggregation일 수 있다는 점이다.

그래서 이제는 입력 전에 먼저 판다.

- `direct_ingest_ok`
- `preprocess_required`
- `uncertain_needs_probe`

## Current signals

gate는 최소한 아래를 본다.

- timestamp density
- short interjection ratio
- short dust ratio
- average chars per dust
- sample short labels

## Current meaning

- `preprocess_required`
  - transcript-aware regroup이 먼저 필요하다
- `direct_ingest_ok`
  - structured markdown-like input이라 direct ingest를 허용할 수 있다
- `uncertain_needs_probe`
  - mixed shape라 raw probe를 먼저 보고 결정한다

## Checkpoints

1. pre-ingest gate
- direct ingest vs preprocess를 runtime mutation 전에 결정한다

2. post-preprocess
- timestamp shard가 meaning chunk로 정리됐는지 본다
- 짧은 응답 꼬리가 흡수됐는지 본다

3. post-ingest
- trace/cell이 semantic regroup처럼 보이는지 본다
- one-cell absorption이면 아직 병목이 남은 것이다

4. line readiness
- 앞단 품질이 안정되기 전에는 line corroboration을 과장하지 않는다
