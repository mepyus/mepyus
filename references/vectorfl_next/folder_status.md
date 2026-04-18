# folder_status / vectorfl_next

## 1. Folder Identity
- path: `vectorfl_next`
- role_guess: Next-generation reference engine repository with app, docs, runtime, and tests.
- one_line_definition: `references/vectorfl_next` is the next-baseline comparison memory.
- engine_position: calibration_reference_next
- current_priority: medium_high

## 2. Snapshot
- immediate_child_dirs: `7`
- immediate_child_files: `15`
- file_types: `.md` x 13, `<no_ext>` x 1, `.toml` x 1

## 3. Child Folders
- `app`
- `docs`
- `logs`
- `references`
- `runtime`
- `scripts`
- `tests`

## 4. Notable Files
- declarations_or_governance: `CONSTITUTION.md`, `CURRENT.md`, `README.md`
- docs_or_data: `memo1.md`, `memo10.md`, `memo2.md`, `memo3.md`, `memo4.md`, `memo5.md`, `memo6.md`, `memo7.md`, `memo8.md`, `memo9.md`, `pyproject.toml`
- other_files: `.DS_Store`

## 5. Quick Reading
- 이 폴더는 하위 폴더 중심으로 읽는 것이 맞다.
- 선언문/현재 상태 문서가 있어 폴더 역할을 빠르게 파악할 수 있다.

## 6. Folder-Level Summary
- 이 폴더는 next-generation reference engine baseline 이다.
- 현재 repo 와 직접 연결된 실행면은 아니지만, 다음 단계 구조 비교와 calibration 에 유효하다.
- 지금은 아래 세 축으로 나눠 읽는 것이 맞다.
  - `historical compare asset`
  - `current reusable asset`
  - `partial bridge / calibration asset`
- `CURRENT.md`, `CONSTITUTION.md`, `docs/`, `runtime/`, `scripts/` 는 historical compare 와 partial bridge 가치가 크고, 일부 `app/`, `references/`, `tests/` 는 current reusable candidate 를 찾을 때만 좁혀 보는 편이 맞다.

## 7. Important Areas Now

### historical compare asset
- `CURRENT.md`
- `CONSTITUTION.md`
- `docs`
- `runtime`
- `scripts`

### current reusable asset
- `app`
- `references`
- `tests`

### partial bridge / calibration asset
- `docs`
- `runtime`
- `scripts`

### later reference asset
- `logs`
- `memo*.md`

## 8. Current Reading
- 지금은 `references/vectorfl_next` 를 “다음 방향의 비교 기준” 으로 읽는 것이 맞다.
- 먼저 historical compare asset 으로 현재 repo-scale engine 과 무엇이 가까운지, 무엇이 아직 덜 잠겼는지 본다.
- 그 다음 partial bridge asset 으로 현재 구조에 바로 힌트를 줄 수 있는 docs/runtime/scripts 를 좁혀 읽는다.
- current reusable asset 은 필요할 때만 한 단계 더 내려가서 찾는 편이 맞다.

## 9. Current Use Hint
- 이 문서는 vectorfl_next reference root index 이다.
- 먼저 `CURRENT.md`, `CONSTITUTION.md`, `docs/`, `runtime/`, `scripts/` 순으로 보며 compare + partial bridge 힌트를 잡는다.
- 새 프로그램/기능에 가져다 쓸 단서를 찾을 때만 `app/`, `references/`, `tests/` 로 내려가는 것이 효율적이다.

## 10. Caution
- next baseline 이라고 해서 현재 엔진보다 우위의 truth 로 읽으면 안 된다.
- memo 문서가 많으므로 핵심 선언/현재 상태 문서를 먼저 잡지 않으면 구조가 흐려진다.
- historical compare 와 current reusable candidate 를 섞어 읽으면 과장된 재사용 판단이 생길 수 있다.
