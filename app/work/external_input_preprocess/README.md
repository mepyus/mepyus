# External Input Preprocess

이 폴더는 외부 transcript를 바로 코어로 넣기 전에
비교, regroup, post-preprocess pass를 읽는 emergent line belt다.

왜 root에 남기나:

- transcript preprocess line의 현재 작업면이다.
- `scripts/run_transcript_preprocess_comparison.py`
- `scripts/run_transcript_aware_regroup.py`
- `scripts/run_post_preprocess_first_pass_probe.py`
  가 모두 이 generated 결과를 직접 쓴다.
- 따라서 아직 `archive_review` 로 내리지 않는다.

현재 구성:

- `generated/`
  - transcript regroup 결과
  - preprocess comparison 결과
  - post-preprocess first-pass probe 결과

정리 규칙:

- raw cache처럼 취급하지 않는다.
- 반복 generated가 과도하게 쌓이면 family별 대표본 정책을 먼저 세운다.
- 코어 line으로 승격되기 전까지는 emergent line support belt로 유지한다.
