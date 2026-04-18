# Agent Collaboration Protocol (Gemini & Codex) v1

본 문서는 VECTORFL 프로젝트 내에서 Gemini(추론/전략 에이전트)와 Codex(실행/변환 에이전트)가 상호 간섭 없이 협업하기 위한 표준 운영 절차(SOP)를 정의합니다.

## 1. 역할 분담 (Role Division: Why/How vs. What)

### 1.1 Gemini (Strategic Orchestrator)
- **영역**: `app/work/`, `docs/`, `gemini/`
- **책임**: "Why"와 "How"의 결정.
- **주요 작업**:
    - 시나리오 설계 및 숙성 (Maturation).
    - 헌법(Constitution) 및 정책(Policy) 수립.
    - Codex의 실행 결과물에 대한 정합성 검토(Review).
    - 복잡한 문제의 근본 원인 분석(Root Cause Analysis).

### 1.2 Codex (Mechanical Transformer)
- **영역**: `app/refac/`, `app/main/`, `scripts/`
- **책임**: "What"의 기계적 구현.
- **주요 작업**:
    - Gemini가 확정한 시나리오의 코드 변환.
    - 대량의 파일 리팩토링 및 포맷팅.
    - 단위 테스트(Unit Test) 작성 및 실행.
    - 물리적 파일 이동 및 구조 정리.

## 2. 작업 점유 및 잠금 규칙 (Workspace Locking)

### 2.1 의도 선언 (Log Before Action)
- 모든 에이전트는 작업을 시작하기 전 `RUNLOG.jsonl`에 자신의 `runlog_id`와 함께 작업 대상(Workspace)을 명시해야 합니다.
- **예시**: `{ "actor": "gemini", "workspace": "app/work/scenario_A", "operation_kind": "maturation" }`

### 2.2 상호 배제 (Mutual Exclusion)
- 특정 에이전트가 점유한 폴더나 파일에 대해 다른 에이전트는 수정 권한을 가질 수 없습니다.
- Codex는 Gemini가 `status: "confirmed"`로 마킹하지 않은 `app/work/` 내의 자산을 `app/main/`으로 옮길 수 없습니다.

## 3. 통신 및 핸드오프 (Handoff Protocol)

### 3.1 Gemini -> Codex (지시)
- Gemini는 `app/work/` 내에 명확한 '구현 명세서(Implementation Spec)'를 생성하고 이를 Codex에게 전달합니다.
- 명세서에는 헌법 제4조(4-Layer Standard) 준수 여부가 포함되어야 합니다.

### 3.2 Codex -> Gemini (보고)
- Codex는 작업을 완료한 후 `runtime/receipts/` 또는 `runtime/review_ledgers/`에 실행 결과 보고서를 남깁니다.
- Gemini는 이 보고서를 읽고 최종 승인(`approve`) 여부를 결정합니다.

## 4. 헌법적 가드레일 (Constitutional Guardrails)

- **Baseline 보호**: 어떤 에이전트도 사용자의 `UNLOCK` 명령 없이 `baseline/` 폴더를 수정할 수 없습니다.
- **유래 보존 (Provenance)**: 모든 코드 변경은 반드시 그 근거가 되는 시나리오(`app/work/`)나 문서(`docs/`)와 연결되어야 합니다.
- **충돌 해결**: 두 에이전트 간의 논리적 충돌 발생 시, 모든 작업을 즉시 중단하고 사용자에게 판단을 요청(Ask User)합니다.

## 5. 단계별 협업 흐름 (Step-by-Step Flow)

1. **Step 1 (Gemini)**: `app/work/`에서 가설 수립 및 시나리오 숙성.
2. **Step 2 (Gemini)**: 헌법 정합성 검토 후 `status: "ready_for_impl"` 선언.
3. **Step 3 (Codex)**: 명세서를 읽고 `app/refac/` 또는 `app/main/`에 코드 구현.
4. **Step 4 (Codex)**: `tests/` 실행 및 결과 기록.
5. **Step 5 (Gemini)**: 최종 결과물이 헌법과 시나리오에 부합하는지 검토 후 `status: "closed"`.

---
*Note: 본 규약은 에이전트 간의 충돌을 방지하고 시스템의 무결성을 유지하기 위한 최소한의 물리적/논리적 장치입니다.*
