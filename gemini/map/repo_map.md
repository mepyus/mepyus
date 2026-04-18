# Repository Structure Map

This document provides a compressed structural summary of the repository, adhering to the global scan output compression rules. The folder tree depth is limited to 3, and key files are highlighted.

## Top-Level Folder Tree (Depth 3)

```
.
├── app/                  # Core application logic, modules, and experiments
│   ├── core/             # Fundamental engine components, states, schemas
│   ├── events/           # Event schemas and handling
│   ├── fragment/         # Fragment processing and storage
│   ├── input_layer/      # Input processing, anchorization, labeling, segmentation
│   ├── measurement/      # Measurement probes, observers, and schemas
│   ├── models/           # Data models and entities
│   ├── runtime/          # Runtime environment, UI components, various operational modules
│   └── work/             # AI's experimental playground, scenarios, and generated outputs
├── data/                 # Data storage: exports, inbox, processed data
├── docs/                 # Project documentation, architecture, policies, guides
│   ├── architecture/     # System architecture documents
│   ├── contracts/        # Contract definitions and agreements
│   └── policies/         # Operational policies and rules
├── gemini/               # Gemini CLI specific files, reports, maps (write scope for AI)
│   └── map/              # Repository maps and structural summaries
├── gpt_run/              # GPT-related scripts and outputs
├── inputs/               # Raw input data, external cases, internal notes
│   ├── external_cases/   # External case studies and inputs
│   └── reference_docs/   # Reference documentation
├── references/           # Reference materials for various projects
│   └── WashTank/         # WashTank project specific references
├── runtime/              # Runtime configuration, logs, manifests, and state
│   ├── logs/             # System and operation logs
│   ├── memory/           # Runtime memory components
│   └── tmp/              # Temporary runtime files
├── scripts/              # Automation scripts, utilities, validation, probes
│   ├── validate/         # Validation scripts (implicit, based on context)
│   └── run_*.py          # Various execution entrypoints and probes
├── source_assets/        # Source assets, baselines, declarations, directives
│   ├── baselines/        # Core baseline documents (AI Read-Only)
│   ├── declarations/     # System declarations
│   └── directives/       # Operational directives
├── tests/                # Unit and integration tests
│   ├── integration/      # Integration tests
│   └── unit/             # Unit tests
└── ... (생략)
```

## 핵심 폴더 역할 요약

*   **app/**: Vectorfl 엔진의 핵심 로직 및 모듈을 포함합니다.
*   **app/core/**: 엔진의 기본 구성 요소, 상태 관리, 스키마 정의가 이루어집니다.
*   **app/input_layer/**: 외부 입력 데이터의 처리, 태깅, 분할 등 입력 전처리 로직을 담당합니다.
*   **app/runtime/**: 엔진의 실행 환경 및 운영 관련 UI, 모듈들이 위치합니다.
*   **app/work/**: AI의 실험적 작업 공간으로, 시나리오, 프로브 실행 결과 등이 저장됩니다.
*   **data/**: 시스템에서 생성, 수신, 처리되는 모든 데이터를 관리합니다.
*   **docs/**: 프로젝트의 아키텍처, 계약, 정책 등 다양한 문서가 포함됩니다.
*   **gemini/**: Gemini CLI가 작업 결과를 기록하는 유일한 공간입니다.
*   **inputs/**: 외부 및 내부에서 유입되는 원시 입력 자료들이 보관됩니다.
*   **references/**: 다양한 프로젝트와 관련된 참조 자료들을 모아둡니다.
*   **runtime/**: 시스템 런타임에 필요한 구성, 로그, 임시 파일 등을 관리합니다.
*   **scripts/**: 각종 자동화, 유틸리티, 검증 스크립트가 포함되어 있습니다.
*   **source_assets/**: 프로젝트의 기준선, 선언, 지시문 등 원본 자산이 저장됩니다.
*   **tests/**: 코드의 기능 검증을 위한 단위 및 통합 테스트 코드입니다.

## 핵심 스크립트 (예시)

-   `app/generate_folder_status.py`: 폴더 상태를 생성하는 유틸리티.
-   `app/core/formation_service.py`: 핵심 엔진의 구성 서비스.
-   `app/input_layer/anchorizer/anchorizer.py`: 입력 데이터 앵커링 로직.
-   `app/input_layer/labeler/labeler.py`: 입력 데이터 라벨링 로직.
-   `app/input_layer/segmenter/experimental_segmenter.py`: 실험적 세그먼트 분할.
-   `scripts/sync_folder_status.py`: 폴더 상태 동기화 스크립트.
-   `scripts/run_ai_future_segment_probe.py`: AI 미래 세그먼트 프로브 실행.
-   `scripts/run_structured_doc_stability_check.py`: 구조화된 문서 안정성 검사.

## Entrypoint 후보 (예시)

-   `scripts/run_viewer_server.py`: 로컬 개발 서버 실행.
-   `scripts/run_ai_future_segment_probe.py`: 특정 AI 프로브 실행.
-   `scripts/build_dust_field_view.py`: 데이터 뷰 빌드.
-   `app/core/runtime/bootstrap.py`: 엔진 부트스트랩.

## 점검 포인트 및 불확실성 메모

-   `app/work/` 폴더 내의 `generated/` 하위 폴더들은 실험 결과물로, 주기적인 정리 또는 아카이브 정책이 필요합니다.
-   다수의 `folder_status.md` 파일들이 존재하며, 이들의 역할과 최신화 여부 점검이 필요합니다. `sync_folder_status.py` 스크립트와 연관될 것으로 추정됩니다.
-   `__pycache__` 디렉토리는 파이썬 컴파일된 바이트코드 파일을 포함하며, 버전 관리에서는 일반적으로 무시됩니다.
-   `app/work/dialogue_loop_test/generated` 및 유사한 `generated` 폴더들은 대량의 테스트 결과 또는 임시 데이터를 포함할 가능성이 높으므로, 스토리지 사용량에 주의해야 합니다.

## 수정 금지 핵심 경로

-   **baseline/**: 프로젝트의 헌법 및 기준선을 포함하므로 AI는 절대 수정 금지. (GEMINI.md 에 명시)
-   `CONSTITUTION.md`, `ENGINE_BASELINE.md`, `rule.md`, `TRANSFORM_RULES.md`, `VERSION.md` 등 프로젝트의 핵심 규범 문서들.
-   모든 `__pycache__/` 디렉토리와 그 내용. (자동 생성 파일)

---
**참고:** 이 요약은 제한된 깊이와 파일 수로 압축된 정보입니다. 요청 시 "full inventory available on request" (전체 인벤토리 요청 시 제공) 가능합니다.
