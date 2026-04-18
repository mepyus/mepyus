# reconstruction_supervisor_process_line_v1

## verdict

- reconstruction supervisor 작업 과정 자체를 하나의 `line`으로 본다.
- 이 line은 일회성 구현 순서가 아니라 반복 가능한 operating line이다.
- 앞으로 이 family를 다시 열 때는 개별 스크립트보다 이 line 순서를 먼저 따른다.

## line identity

- line_name: `reconstruction_supervisor_process_line`
- line_role: bounded reconstruction family를 만들고 유지하고 검증하는 운영선
- line_kind: read-only reconstruction line

## line stages

### 1. family lock

- bounded family를 먼저 잠근다.
- 기준 문서:
  - [bounded_reconstruction_family_and_supervisor_entrypoint_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/bounded_reconstruction_family_and_supervisor_entrypoint_v1.md#L1)

의미:

- 무엇을 묶는지
- 무엇을 묶지 않는지
- 무엇이 non-governing인지
- latest가 왜 authoritative가 아닌지

를 먼저 잠근다.

### 2. builder draft

- packet builder를 만든다.
- 기준 스크립트:
  - [build_reconstruction_supervisor_surface.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_reconstruction_supervisor_surface.py#L1)

의미:

- receipt = lineage spine
- views = supervisor surface spine
- sidecar = bounded observation supplement

를 실제 output으로 내린다.

### 3. packet surfaces

- builder output을 surface family로 고정한다.
- 현재 표면:
  - [reconstruction_supervisor_latest.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/reconstruction_supervisor_latest.json#L1)
  - [index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/reconstruction_supervisor/index.json#L1)
  - [folder_status.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/reconstruction_supervisor/folder_status.md#L1)

의미:

- latest
- index
- folder-level read order

를 같이 유지한다.

### 4. fixture checks

- line은 반드시 fixture check를 가진다.
- 현재 체크:
  - [run_reconstruction_supervisor_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reconstruction_supervisor_fixture_check.py#L1)
  - [run_reconstruction_supervisor_state_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reconstruction_supervisor_state_fixture_check.py#L1)

의미:

- non-governing
- pointer-backed
- role separation
- state-backed explicit path

을 기계적으로 다시 확인한다.

### 5. sync maintenance

- line은 생성과 유지가 분리된다.
- 유지 스크립트:
  - [sync_reconstruction_supervisor_surfaces.py](/Users/sungsookim/universe/vectorfl_replica/scripts/sync_reconstruction_supervisor_surfaces.py#L1)

의미:

- existing packet을 다시 뽑지 않아도
- latest / index / folder_status를 맞출 수 있어야 한다.

### 6. cycle runners

- line은 operator entrypoint를 가진다.
- 현재 runner:
  - [run_reconstruction_supervisor_cycle.sh](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reconstruction_supervisor_cycle.sh#L1)
  - [run_reconstruction_supervisor_advanced_cycle.sh](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reconstruction_supervisor_advanced_cycle.sh#L1)
  - [run_reconstruction_supervisor_batch.sh](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reconstruction_supervisor_batch.sh#L1)

의미:

- single bounded cycle
- explicit advanced cycle
- bounded batch cycle

를 작업 루틴으로 고정한다.

### 7. operating memory

- line은 operator가 다시 읽을 메모를 가진다.
- 현재 메모:
  - [reconstruction_supervisor_operating_pattern_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/reconstruction_supervisor_operating_pattern_v1.md#L1)
  - [reconstruction_supervisor_operator_usage_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/notes/reconstruction_supervisor_operator_usage_note_v1.md#L1)

## current ordered checklist

1. family spec를 확인한다.
2. builder 또는 advanced builder를 고른다.
3. packet을 생성한다.
4. sync를 돌린다.
5. bounded fixture check를 돌린다.
6. 필요하면 state-backed fixture check를 돌린다.
7. latest -> index -> packet json -> packet md 순서로 읽는다.

## memory lock

- 이 과정은 단순 스크립트 묶음이 아니다.
- 이 과정 자체가 `reconstruction_supervisor_process_line`이다.
- 이후 변경은 이 line의 어느 stage를 바꾸는지 기준으로 설명해야 한다.

## non-goals

- no decision line
- no promotion line
- no governing line
- no mutation line

## one-line lock

> reconstruction supervisor의 builder, surfaces, checks, sync, runners, usage note는 따로 흩어진 자산이 아니라 하나의 `reconstruction_supervisor_process_line`을 이룬다.
