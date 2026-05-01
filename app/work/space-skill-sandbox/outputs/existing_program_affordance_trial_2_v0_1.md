# Existing Program Affordance Trial 2 (v0.1)

## 1. Target
- name: app/generate_folder_status.py
- source: app/generate_folder_status.py
- type: Python Directory Indexer Script

## 2. Caller Shift Analysis
- **Human Caller Assumption**: 로컬 폴더 구조를 시각화하기 위해 가끔 실행하며, `folder_status.md` 파일이 덮어써진다는 점을 인지하고 있음.
- **Agent Caller Risk**: 에이전트가 컨텍스트 최신화를 위해 이 스크립트를 과도하게 반복 실행(Recursive looping)하여 시스템 리소스를 소모하거나, 사용자가 별도로 관리하던 `folder_status.md` 수동 기록을 예고 없이 말살(Overwrite)할 위험이 있음.

## 3. Tool Affordance
- **Intended Caller**: `Intake Session` (공간 파악용), `Routing Session` (경로 탐색용).
- **Allowed Use Case**: `app/` 폴더 하위의 구조적 요약을 자동 생성하여 에이전트 가독성을 높일 때.
- **Forbidden Use Case**: `ROOT` 변수를 임의로 수정하여 샌드박스 외부나 시스템 루트 폴더를 인덱싱하려는 시도.
- **Preflight Stop Point**: 파일 쓰기 권한 확인 및 인덱싱 대상 폴더의 파일 개수가 일정 수준(예: 1000개)을 초과하는지 체크.

## 4. Risk Classification (v0.1)
v0.1 원칙에 따라 위험을 분류함.

### [Confirmed Risk] File Overwrite (의도된 덮어쓰기)
- **Status**: CONFIRMED
- **Evidence**: 164-167행 `(path / "folder_status.md").write_text(...)`
- **Description**: 기존에 존재하던 `folder_status.md` 파일의 내용을 묻지 않고 덮어씀. 만약 사용자가 수동으로 중요한 메모를 남겼다면 데이터 소실 발생.

### [Risk Candidate] Resource Exhaustion (DoS 가능성)
- **Status**: CANDIDATE
- **Evidence**: 25-28행 `ROOT.rglob("*")`
- **Description**: 폴더 내 파일/디렉토리 개수가 방대할 경우, 재귀적 탐색 과정에서 메모리 점유율이 급증하거나 실행 시간이 무한정 길어질 수 있음. (에이전트가 매우 큰 디렉토리에 이 스크립트를 복제하여 실행할 경우 위험).

### [Refuted Claim] Shell Injection
- **Status**: REFUTED
- **Evidence**: 소스 코드 전반. `subprocess`, `os.system`, `eval` 등 외부 명령 실행 로직이 전무함.
- **Description**: 단순 파일 시스템 읽기/쓰기만 수행하므로 쉘 주입 위험은 없음.

## 5. Evidence Source Mapping
- **Evidence A**: 10행 `ROOT = Path(__file__).resolve().parent` (작동 범위 고정 확인)
- **Evidence B**: 25-28행 `collect_dirs` 함수 내 `rglob("*")` (전체 탐색 방식 확인)
- **Evidence C**: 164-167행 `write_text` 호출 (파일 덮어쓰기 동작 확인)

## 6. Conclusion
- v0.1 렌즈 적용 결과, 보안 용어 남용 없이 실제 코드 기반의 **Confirmed Risk(File Overwrite)**와 **Candidate Risk(Resource Exhaustion)**를 명확히 분리함.
- 이 프로그램은 `Intake Session`의 보조 도구로 유효하지만, 덮어쓰기 위험 때문에 `Preflight` 단계에서 사용자의 수동 기록 존재 여부를 확인하는 절차가 권장됨.

## 7. Next Action Recommendation
- **PASS**: 렌즈 v0.1의 분류 체계가 실제 분석에서 판단의 노이즈를 줄이는 데 효과적임을 확인함.
