# Existing Program Affordance Trial 3 (v0.1)

## 1. Target
- name: scripts/folder_status_sync.py (및 app/core/registry/folder_status_sync.py)
- source: scripts/folder_status_sync.py
- type: Folder Status & Inventory Synchronization System

## 2. Caller Shift Analysis
- **Human Caller Assumption**: 특정 파일이나 폴더를 수정한 후, 관련 인덱스를 최신화하기 위해 수동으로 실행함. 인자(`paths`)를 신중하게 선택하며, 대량의 쓰기 작업이 발생할 경우 그 영향을 예측하고 있음.
- **Agent Caller Risk**: 에이전트가 파일 하나를 고칠 때마다 이 스크립트를 습관적으로 호출하거나, `--child-depth`를 크게 잡아 의도치 않게 수많은 폴더의 `folder_status.md`를 동시에 수정(Write Storm)할 위험이 있음. 특히 JSONL 로그 파일에 대한 빈번한 Append 작업으로 인한 파일 락(Lock) 경합 및 I/O 부하 유발 가능성 존재.

## 3. Tool Affordance
- **Intended Caller**: `Relay Session` (작업 후 상태 동기화용), `Intake Session` (인덱스 갱신용).
- **Allowed Use Case**: 특정 폴더의 구조적 변화가 발생한 후, `folder_status.md`와 `inventory`를 일치시켜야 하는 상황.
- **Forbidden Use Case**: 전체 저장소(`/`)를 대상으로 대규모 `child_depth`와 함께 실행하여 소스 공간 전체에 '쓰기 노이즈'를 만드는 행위.
- **Preflight Stop Point**: 
  - `paths` 인자의 유효성 확인 (존재하지 않는 경로는 무시되지만, 에이전트의 실수 유도 가능성).
  - 쓰기 대상 경로 중 보호된 `baseline/`이나 `source-space` 핵심 폴더 포함 여부 확인.
  - `FOLDER_CHANGES_DIR` 및 `FOLDER_INVENTORY_DIR` 쓰기 권한 확인.

## 4. Risk Classification (v0.1)

### [Confirmed Risk] Massive File Overwrite (대규모 파일 쓰기)
- **Status**: CONFIRMED
- **Evidence**: `app/core/registry/folder_status_sync.py` 236행 (`status_path.write_text(...)`) 및 268-283행 (`sync_folder_status` 루프).
- **Description**: `paths`와 `child_depth` 설정에 따라 수많은 폴더의 `folder_status.md`를 동시에 덮어씀. 에이전트가 범위를 잘못 지정할 경우 대량의 Unstaged Changes를 발생시켜 형상 관리에 혼란을 초래함.

### [Confirmed Risk] Side-effect: Event Logging (이벤트 로그 누적)
- **Status**: CONFIRMED
- **Evidence**: `app/core/registry/folder_status_sync.py` 141행 (`append_jsonl_locked(...)`).
- **Description**: 실행 시마다 `folder_change_log.jsonl`에 레코드가 추가됨. 무분별한 호출은 로그 파일의 크기를 비정상적으로 키우고, 락 경합을 유발할 수 있음.

### [Risk Candidate] Logic Inconsistency (논리 불일치 위험)
- **Status**: CANDIDATE
- **Evidence**: `app/core/registry/folder_status_sync.py` 55-82행 (`guess_role` 함수).
- **Description**: 폴더의 역할을 '추측(Guess)'하여 기록함. 에이전트가 이 추측된 Role을 절대적인 진실로 믿고 후속 작업을 수행할 경우, 잘못된 컨텍스트에 기반한 오판이 발생할 수 있음. (Evidence-based Naming 원칙에 따라, '추측'임을 명시해야 함).

### [Refuted Claim] Shell Injection
- **Status**: REFUTED
- **Evidence**: 소스 코드 전반. `subprocess`, `os.system` 등을 통한 외부 명령 실행이 없으며, 모든 경로는 `Path` 객체로 안전하게 처리됨.
- **Description**: 사용자 입력을 쉘 명령으로 전달하지 않으므로 주입 위험 없음.

## 5. Evidence Source Mapping
- **Evidence A**: `app/core/registry/folder_status_sync.py` 141행 (Append-only 로그 쓰기 확인)
- **Evidence B**: `app/core/registry/folder_status_sync.py` 190행 (Atomic JSON 쓰기 확인)
- **Evidence C**: `app/core/registry/folder_status_sync.py` 236행 (Markdown 렌더링 결과 쓰기 확인)
- **Evidence D**: `app/core/registry/folder_status_sync.py` 245-266행 (`collect_target_dirs`의 재귀적 탐색 로직 확인)

## 6. Conclusion
- `folder_status_sync.py`는 단순한 인덱서를 넘어, 시스템의 '운영 이력(Change Log)'과 '현재 상태(Inventory)'를 관리하는 복잡한 상태 변이 도구임.
- 에이전트가 호출할 경우 **Massive File Overwrite**와 **Log Bloating**이 실재하는 위험임이 확인됨.
- 이 도구는 `Relay Session`의 '작업 마무리 단계'에서만 제한적으로 사용되어야 하며, 실행 전 대상 경로에 대한 `Preflight` 승인이 필수적임.

## 7. Next Action Recommendation
- **PASS**: 렌즈 v0.1이 복잡한 코드의 'Side-effect'와 'Role'을 식별하는 데 성공적으로 작동함.
- **HOLD**: 에이전트에 의한 자동 호출은 금지하며, 수동 호출 시에도 `user_judgment_route`를 거쳐 대상 범위를 확인받아야 함.
