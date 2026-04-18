# transcript aware regroup v0

## Purpose

이 note는 `preprocess_required`로 판정된 transcript-like raw input을
바로 ingest하지 않고, 먼저 meaning chunk 쪽으로 다시 묶는
bounded preprocessor를 고정하기 위한 문서다.

## Stance

- no `inputter.py` patch
- no `labeler.py` patch
- no runtime mutation
- sidecar preprocess only

## Current behavior

전처리기는 아래를 수행한다.

- timestamp / chapter marker 약화
- simple speaker prefix 제거
- short interjection drop
- sentence-like normalize
- bounded chunk regroup

## Output

- preprocessed transcript sidecar text
- before gate vs after gate comparison json

## Meaning

이 layer는 transcript를 promotion-ready로 만들지 않는다.
목표는 자막 조각을 compare-ready meaning chunk 쪽으로 옮기는 것이다.
