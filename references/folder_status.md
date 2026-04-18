# folder_status / .

## 1. Folder Identity
- path: `.`
- role_guess: Top-level reference warehouse for internal repos, notes, derived materials, and comparison assets.
- one_line_definition: `references/` is the engine calibration memory.
- engine_position: calibration_memory
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `5`
- immediate_child_files: `2`
- file_types: `<no_ext>` x 1, `.py` x 1

## 3. Child Folders
- `md_maker`
- `vectorfl`
- `vectorfl_next`
- `vectorfl_next_gemini_session`
- `WashTank`

## 4. Notable Files
- scripts_or_commands: `generate_folder_status.py`
- other_files: `.DS_Store`

## 5. Quick Reading
- 이 폴더는 하위 폴더 중심으로 읽는 것이 맞다.
- 실행 스크립트 또는 코드 파일이 있어 행동 가능한 reference 로 쓸 수 있다.

## 6. Current Use Hint
- 이 문서는 first-pass folder index 이다.
- 세부 구조가 필요하면 이 폴더의 선언문/README/current 문서부터 읽고, 그 다음 코드/데이터를 연다.

## 7. Engine Position
- `references/` 는 단순 보관함이 아니다.
- 현재 엔진에서 이 폴더는 `calibration memory` 역할을 한다.
- 즉 과거 자산을 저장하는 동시에, 현재 입력기와 판독면을 교정하는 기준 창고다.

## 8. Important Folders Now

### first priority
- `WashTank`
  - 현재 가장 적극적으로 구조화된 reference family
  - observer / preprocessed / queue policy 까지 잠겨 있음
- `vectorfl`
  - 과거 vectorfl baseline / constitution / reports / runtime reference
- `vectorfl_next`
  - next-generation reference engine baseline

### second priority
- `vectorfl_next_gemini_session`
  - session-specific notes + mirrored engine reference
- `md_maker`
  - WashTank 관련 md 설명 자료

## 9. Folder-Level Summary
- 이 폴더는 reference source 와 calibration artifact 가 함께 있는 이중 레인 공간이다.
- 현재는 아래 두 레인을 동시에 읽는 것이 맞다.
  - `space material lane`
  - `input calibration lane`
- `WashTank/` 는 source -> observer -> preprocessed -> queue policy 까지 가장 구체적으로 잠긴 reference family 이다.
- `vectorfl*` 계열은 더 넓은 baseline / next baseline / session 비교 자산이다.

## 10. Key Files

### `generate_folder_status.py`
- current role: `references/` 전체의 first-pass `folder_status.md` 생성
- function: 주요 reference 폴더에 메타 인덱스 부여
- input/output: `references/` tree -> 각 reference 폴더의 `folder_status.md`
- execution context: reference 지도 생성
- engine position: reference self-description generator
- reuse potential: 높음
- caution: dependency/cache/generated run 폴더는 제외하는 보수적 스캔

## 11. Secondary Folders
- `vectorfl_next_gemini_session`
  - 세션 중심 비교/보조 자산
- `md_maker`
  - 사람 판독용 md 생성/정리 자산
- 이 둘은 중요하지만 현재 핵심 교정 레인보다는 후순위다.

## 12. Current Folder Flow
- `WashTank/` 에서 reference source / observer / preprocessed / queue policy 가 가장 구체적으로 잠김
- `vectorfl/`, `vectorfl_next/`, `vectorfl_next_gemini_session/` 은 더 넓은 비교/교정 자산
- `md_maker/` 는 WashTank 구조를 사람이 읽는 md 자산

즉 이 폴더는 엔진 외부 기억이 아니라, 현재 엔진을 안정화하는 교정 기억이다.

## 13. Recommended Read Order
1. `WashTank/`
2. `vectorfl/`
3. `vectorfl_next/`
4. `vectorfl_next_gemini_session/`
5. `md_maker/`

## 14. Current Reading
- 지금은 `references/` 를 archive 가 아니라 calibration memory 로 읽는 것이 맞다.
- 초반에는 `WashTank` 처럼 이미 observer/preprocessed/queue policy 가 잠긴 family 를 우선 보고, 그 다음 비교 자산으로 `vectorfl`, `vectorfl_next` 를 본다.
- 단순 보관물과 현재 교정 자산을 구분하지 않으면 reference lane 이 흐려진다.

## 15. Caution
- 모든 reference 를 같은 강도로 다루면 current calibration lane 과 later archive lane 이 섞인다.
- `references/` 는 현재 엔진 전용과 범용 교정 자산이 공존하므로, 현재 우선순위를 항상 같이 적어야 한다.
- 다음 보강은 `WashTank/preprocessed`, `vectorfl`, `vectorfl_next` 하위 status 의 per-file block 확장으로 이어지는 것이 맞다.

## 16. Operational Logging
- activity_log_path: [runtime/events/folder_activity/references.folder_activity_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/folder_activity/references.folder_activity_log.jsonl)
- expected_event_types:
  - `doc_registered`
  - `file_created`
  - `file_updated`
  - `status_compaction_needed`
  - `status_compacted`
- compaction_target: `yes`
- compaction_note:
  - reference 관련 사건은 먼저 append-only event 로 남기고, 이 문서는 교정 기억의 현재 상태를 나중에 압축 설명한다.
