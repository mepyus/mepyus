# run_reconstruction_supervisor_cycle_scope_note_v1

## purpose

- `scripts/run_reconstruction_supervisor_cycle.sh`는 reconstruction family의 기본 작업 루틴을 한 번에 실행하는 thin runner다.

## sequence

- builder 실행
- navigation surface sync 실행
- bounded fixture check 실행
- state-backed fixture check 실행

## out of scope

- runtime 본체 연결
- decision logic
- governing behavior
- state mutation

## guard

- matching receipt가 없는 scope는 이 runner에서 자동 fallback으로 섞지 않는다.
