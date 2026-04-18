# folder_status / measurement

## 1. Folder Identity
- path: `measurement`
- role_guess: Ambient measurement and observer-related support layer.
- one_line_definition: `app/measurement` is the observer-support and measurement layer.
- engine_position: body_measurement_support
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `6`
- file_types: `.py` x 6

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `__init__.py`, `ambient_probe.py`, `observer.py`, `schema.py`, `seed_bank.py`, `store.py`

## 6. Quick Reading
- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.
- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.

## 7. Folder-Level Summary
- 이 폴더는 observer-first 운영을 받쳐주는 측정 보조층이다.
- ambient probe, observer, seed bank, schema, store 가 함께 묶여 있다.
- `app/fragment` 와 root `runtime/measurements` 사이의 의미층 보조로 읽는 것이 맞다.

## 8. Key Files

### `observer.py`
- current role: measurement observer 보조
- function: 측정/판독 기록의 보조 해석
- input/output: fragment/runtime state -> measurement records
- engine position: observer support
- reuse potential: 중상
- caution: `app/runtime/observer.py` 와 혼동하지 말 것

### `ambient_probe.py`
- current role: 주변 측정/탐침 보조
- function: measurement 보조값 수집
- input/output: runtime/input context -> ambient measurement signals
- engine position: measurement probe
- reuse potential: 중상
- caution: 현재 엔진 전용 규약이 섞여 있을 수 있다

### `seed_bank.py`
- current role: seed bank 저장
- function: 측정/observer 관련 seed 재료 유지
- input/output: seed materials <-> banked records
- engine position: measurement memory
- reuse potential: 중상
- caution: later provenance/ledger 와의 연결이 남아 있다

## 9. Current Reading
- 지금은 `measurement/` 를 결과 분석이 아니라 observer support layer 로 읽는 것이 맞다.
- fragment 중심 읽기에서는 보조층이지만, mixed/hold/re-entry 판독을 생각하면 무시하면 안 된다.

## 10. Current Use Hint
- 이 문서는 measurement layer root index 이다.
- 다음 탐색에서는 `observer.py`, `ambient_probe.py`, `seed_bank.py` 를 먼저 보면 구조가 빠르게 잡힌다.

## 11. Caution
- 이름만 보면 보조 레이어처럼 보이지만, 현재 엔진 철학에서는 꽤 중요한 층이다.
- 다만 코어 state layer 와 동일 선상으로 읽으면 과대평가될 수 있다.
