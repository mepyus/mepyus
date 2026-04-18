# post preprocess first pass probe v0

## Purpose

이 note는 transcript-aware regroup 뒤에
정리된 sidecar를 기준으로 bounded first pass를 읽는 마지막 점검면을 고정하기 위한 문서다.

## Stance

- read-only
- no main runtime mutation
- no promotion
- readability / flatness / caution만 본다

## What it reads

- dust count
- scene / flow flatness
- sample chunk readability
- human-read summary
- caution notes
- next read

## Meaning

이 probe는 전처리가 실제로 first-pass 품질을 올렸는지 확인하는 면이다.
좋아 보인다고 바로 ingest하는 결정면이 아니라,
`이제 probe_again_before_ingest 인가`, `아직 too flat 한가`를 읽는 면이다.
