# PROGRAM FRAME & EXTERNAL PATTERN MAP (V0)

## 1. Program Frame (Session 0)
- **Objective**: 샌드박스 실험을 종료하고, VectorFL 시스템을 외부 도구(Hermes, OmX 등)가 공간 기록을 활용하여 세션을 셋업할 수 있는 'Product-Attachable Pipeline' 구조로 전환.
- **Scope**: 공간 내 기존 기록의 검색, 활성화, 그리고 외부 도구 인터페이스 규격화.
- **Rules**:
    - **No Shadow-Work**: 모든 활동은 공간 내 기록으로 남음.
    - **Atomic Pipeline**: 검색 -> 활성화 -> 실행 -> 회수 -> 기록.
    - **No Unauthorized Automation**: 도구는 제안만 가능, 실행은 사용자/CLI 승인 체계 하에 진행.
- **Roles**:
    - **User**: 최종 의사결정권자, 승인자.
    - **Codex/CLI**: 공간 검색, 인터페이스 셋업, 실행 엔진.
    - **Gemini**: 패턴 분석, 메타-분석, 비교/증폭 지원.
    - **VectorFL Space**: 모든 작업의 근간이 되는 SSOT (Single Source of Truth).

## 2. External Program Pattern Map (Session 1)
- **OmX (Oh-My-Codex)**:
    - **Key Pattern**: Codex 기반 워크플로우 레이어, Read-only Exploration Harness.
    - **VectorFL Adoption**: Codex 호출을 감싸는 'Read-only Adapter'로 부착.
- **Hermes Agent**:
    - **Key Pattern**: Standing Memory와 Runtime Mission의 분리, Session Lineage, Compression.
    - **VectorFL Adoption**: 런타임 미션 패킷(Mission Packet) 기반 세션 인터페이스로 부착.
- **Codex**:
    - **Key Pattern**: 파일/문서 기반의 1차 작업자.
    - **VectorFL Adoption**: 공간 정보 활용을 위한 기본 실행기.
- **Gemini**:
    - **Key Pattern**: 외부 컨텍스트 분석 및 비교.
    - **VectorFL Adoption**: 작업 보조 및 메타-루프 정제.
- **OpenClaw (HOLD)**:
    - **Key Pattern**: Gateway 및 Multi-channel.
    - **VectorFL Adoption**: 미래 확장성(Gateway)으로 분류하여 현재는 참조만 수행.

## 3. Immediate Action Plan
- **Session 0/1 통합 완료**를 기점으로, 다음 세션에서 'Space Material Activation Map'을 수립함.
- 외부 도구는 직접 시스템을 변경하지 않으며, 오직 지정된 인터페이스를 통해서만 정보를 취득하고 작업을 제안함.
