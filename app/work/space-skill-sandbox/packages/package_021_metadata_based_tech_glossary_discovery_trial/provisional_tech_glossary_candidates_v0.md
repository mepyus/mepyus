# Provisional Tech Glossary Candidates (v0)

## 개요
이 문서는 메타데이터 스캔을 통해 식별된 `Core Authored Doc Candidates`들로부터 추출된 잠정적인 기술 용어 및 개념적 키워드 리스트입니다. 이는 공식적인 정의가 아니며, 패키지 생태계 내에서 형성되고 있는 관찰된 신호(Observed signals)입니다.

- **상태:** 잠정적 후보 (Provisional Candidate)
- **근거:** Package 001~020 내의 Plan, Decision, Guard, Observation 문서들
- **Tone Guard:** 아래 용어들은 실험 단계이며, 확정된 베이스라인이나 표준이 아닙니다.

## 1. 패키지 아키텍처 및 루프 (Architecture & Loop)

- **Bounded Package (한정된 패키지):** 명확한 경계(Boundary)를 가진 분석/실행의 최소 단위.
- **Package Loop (패키지 루프):** Brief → Handoff → Execution → Collection → Validation → Closeout으로 이어지는 반복 주기.
- **Small Execution Unit (작은 실행 단위):** 검증 비용을 낮추기 위해 설계된, 상태가 없고(Stateless) 선형적인 추적(Linear trace)이 가능한 동작 단위.
- **Metadata-first Discovery (메타데이터 우선 발견):** 대량의 데이터를 읽기 전, 파일명/크기/헤더 등 메타데이터를 먼저 스캔하여 리뷰 범위를 좁히는 전략.

## 2. 리뷰 및 보정 (Review & Calibration)

- **Core Authored Doc (핵심 저작 문서):** 표준 프로세스 기록물 외에 패키지의 독특한 논리나 결정이 담긴 핵심 문서 후보.
- **Tone Guard (톤 가이드):** AI의 보고 표현이 과하게 확정적으로 흐르지 않도록 근거 수준에 맞춰 수위를 조절하는 인지적 안전장치.
- **Observed Signal (관찰된 신호):** 실험 데이터에서 포착된 잠정적인 현상이나 경향성. (Rule/Baseline과 대조됨)
- **Deep-Read Candidates (정밀 독해 후보):** 메타데이터 스캔 결과, 패키지의 핵심 Verdict 파악을 위해 우선적으로 읽어야 할 것으로 식별된 소수의 문서군.

## 3. 도구 및 데이터 (Tools & Data)

- **Tiny Script (작은 스크립트):** 발견 도구(Discovery tool)로서의 역할을 수행하는, 작고 단일 목적을 가진 샌드박스 내 스크립트. (예: `package_metadata_scan.sh`)
- **Loose Naming Pattern (느슨한 명칭 패턴):** 강제 규칙은 아니지만, 식별력을 높이기 위해 파일명에 포함되는 힌트 키워드들 (`_v0`, `_plan`, `_candidate` 등).
- **Intent Mapping (의도 매핑):** 패키지 간의 명시적/추정적 연결 고리를 '의도의 압축본'인 계획 문서를 통해 추적하는 행위.

---
*이 용어 사전은 잠정적이며, 사용자/Codex의 추가 검토가 필요(Needs review)합니다.*
