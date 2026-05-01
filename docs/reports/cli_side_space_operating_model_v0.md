# CLI-side Space Operating Model v0

## 0. 운영 철학
- **공간은 관찰 대상:** 공간(Space)은 깊은 맥락을 유지하고, 관찰층(VectorFL)은 CLI의 실행 흐름을 얇게 판독한다.
- **실행은 터미널:** 모든 작업은 CLI/Codex에서 직접 실행하며, UI/Dashboards를 통한 자동 제어는 지양한다.
- **관찰은 비침투적(Ambient):** 관찰 화면은 명령기가 아니라, 작업의 상태(`Draft`, `Maturing`, `Canonical`)와 검토 필요성만을 알려주는 투명한 판독창이다.

## 1. 운영 층위 (Layering)
1. **깊은 층 (Deep Space):** 모든 Provenance, 기준 문서, 실패 흔적, 패턴 자산이 보존되는 곳.
2. **실행 층 (Light CLI):** 터미널에서 수행되는 즉각적이고 파괴적인 실행.
3. **판독 층 (Observer Surface):** 실행 결과를 `Packet` 단위로 분류하고 `Human Lock` 여부를 판단하는 얇은 막.

## 2. 패킷 흐름 (The Observation Loop)
- **Action:** CLI 작업 (예: 코드 수정, 파일 삭제).
- **Packetization:** 작업의 의도(`Intent`)와 결과(`Residue`)를 패킷화.
- **Triage:** 
  - `Observation-only`: 단순 실행 기록.
  - `Validation_Required`: 로직/기준 위반 여부 확인.
  - `Human_Review_Required`: 승인이 필요한 아키텍처/보안 영향.

## 3. 검증 규칙 (Guardrails)
- **Lock은 인간의 것:** AI는 후보를 제안할 뿐, 절대 스스로 Lock을 걸거나 Promotion할 수 없음.
- **Collapse evidence:** 모든 잔여 로그는 삭제하지 않고 Primary Event 밑에 Collapse 함.
- **No Schema-first:** 작업의 흔적을 즉시 태그/스키마화하지 않음.
