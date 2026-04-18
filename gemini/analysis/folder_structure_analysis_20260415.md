# vectorfl_replica Folder Structure Analysis (Gemini Judgment)

Date: 2026-04-15
Actor: Gemini-CLI
Reason: User request for full repository structure scan and organization judgment.

## 1. Architecture Overview
본 저장소는 "재료(Raw) -> 파편(Fragment) -> 숙성(Maturation) -> 투영(Projection)"의 수명주기를 가진 **repo-scale engine**입니다.

## 2. Directory Hierarchy and Roles

### A. The Engine Brain: `app/`
엔진의 핵심 로직과 실험 기록이 담긴 곳입니다.
- **`core/`**: 엔진 골격 (State, Model, Ingest, Registry).
- **`input_layer/`**: 입력을 Fragment로 변환 (Segmenter, Anchorizer, Source Locator).
- **`fragment/`**: 중심 객체(Fragment) 관리 (Schema, Store, Projector).
- **`runtime/`**: 엔진 실행 계층 (Inputter, Observer, Reporting, Viewer).
- **`work/`**: 사고 실험 및 정책 수립 공간. (현재 가장 중요한 '사고의 기록'들이 쌓이는 곳)

### B. The Output Surface: `runtime/` (Root)
엔진이 실행된 결과와 현재의 '표면'을 보여주는 곳입니다.
- **`events/`**: 사건 원장 (Engine Event Ledger).
- **`manifests/`**: 운영 메타데이터 (Document/Ticket Registry).
- **`views/` & `reports/`**: 가시화된 결과 (Latest Board, Fragment View).
- **`logs/`**: 물리적 로그 (Repo Delta Log, Work Sessions).

### C. Tools and Automation: `scripts/`
엔진 운영 및 유틸리티 스크립트 모음입니다.
- **`process_structured_doc_with_routing.py`**: 문서 라우팅 및 티켓화.
- **`folder_status_sync.py`**: 프로젝트 상태 정합성 유지.
- **`run_*` 계열**: 각종 검증 및 실험 실행기.

### D. Governing Documents: `docs/` & Root MDs
프로젝트의 헌법과 정책입니다.
- **`CONSTITUTION.md`**: 최상위 원칙.
- **`CURRENT.md`**: 현재 런타임/정책 베이스라인.
- **`vectorfl_status.md`**: 통합 엔진 진행 상황 인덱스.

### E. Agent Workspace: `gemini/`
에이전트(Gemini)와 사용자 간의 대화 기록 및 전용 지침 공간입니다.
- **`session_update_20260415.md`**: 오늘의 업데이트 보고서.
- **`vectorfl_structure_summary_for_gemini.md`**: 에이전트용 구조 요약.

### F. Reference & Calibration: `references/`
과거 자산 및 비교 기준입니다.
- **`WashTank/`**: 핵심 참조 아키텍처.
- **`vectorfl_next/`**: 이전 실험 데이터.

## 3. Core Operational Flow (Interpretation)
1. **Intake**: `inputs/` -> `app/input_layer/`
2. **Processing**: `app/runtime/` (managed by `scripts/`)
3. **Recording**: `runtime/events/` & `RUNLOG.jsonl`
4. **Surfacing**: `runtime/views/` & `runtime/reports/`

---
**Note**: 본 분석은 사용자님의 "업데이트 및 구조 정리" 요청에 의해 수행되었으며, `gemini/` 폴더 외의 어떠한 파일도 수정하지 않았습니다.
