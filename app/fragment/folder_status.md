# folder_status / fragment

## 1. Folder Identity
- path: `fragment`
- role_guess: Fragment storage and projection layer.
- one_line_definition: `app/fragment` is the fragment persistence and projection layer.
- engine_position: body_fragment_storage
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `4`
- file_types: `.py` x 4

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `__init__.py`, `projector.py`, `schema.py`, `store.py`

## 6. Quick Reading
- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.
- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.

## 7. Folder-Level Summary
- 이 폴더는 fragment schema, 저장, projection 을 담당하는 핵심 저장층이다.
- 엔진 중심 객체가 fragment 이므로, 이 폴더는 현재 엔진 정의와 직접 연결된다.
- `app/input_layer` 의 결과를 받고, `app/runtime` 과 root `runtime/` 으로 이어진다.

## 8. Key Files

### `schema.py`
- current role: fragment 구조 정의
- function: fragment minimum shape / slots 정의
- input/output: schema definitions for fragment layer
- engine position: fragment contract base
- reuse potential: 높음
- caution: 앞으로 `fragment_min_contract_v1` 와 맞물려 읽어야 한다

### `store.py`
- current role: fragment 저장 레이어
- function: fragment persistence 관리
- input/output: fragment materials <-> stored fragment records
- engine position: fragment persistence
- reuse potential: 높음
- caution: 실제 runtime artifact 와의 연결도 함께 봐야 한다

### `projector.py`
- current role: fragment projection 레이어
- function: fragment 를 다른 표면/출력으로 투사
- input/output: fragment records -> projected views/structures
- engine position: fragment projection bridge
- reuse potential: 중상
- caution: view/report code와 구분해서 읽어야 한다

## 9. Current Reading
- 지금은 `fragment/` 를 단순 저장 코드가 아니라 엔진 중심 객체를 붙드는 층으로 읽는 것이 맞다.
- `schema -> store -> projector` 순으로 보면 구조가 가장 잘 보인다.

## 10. Current Use Hint
- 이 문서는 fragment layer root index 이다.
- 다음 탐색에서는 `schema.py`, `store.py`, `projector.py` 를 우선 읽으면 된다.

## 11. Caution
- fragment 를 단순 split 결과로 읽으면 이 폴더의 의미가 줄어든다.
- 이 폴더는 이후 fragment 최소 계약과 직접 연결될 가능성이 높다.
