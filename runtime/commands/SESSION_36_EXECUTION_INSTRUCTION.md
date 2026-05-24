# SESSION_36_EXECUTION_INSTRUCTION.md

## 1. Goal
Codex가 활성화된 Context Bundle 내에서 할당된 역할(구조 리뷰어)을 수행하여 표준 출력물(Digest, Evidence, Issue Log)을 생성하는지 검증.

## 2. Search First
- `SESSION_35_RESULTS_V0` (활성화된 Material Family 및 Evidence Pointers).
- `TOOL_ROLE_PROFILES_V0` (Codex 역할 지침).
- `SESSION_RETURN_FORMAT_V0` (표준 출력 규격).

## 3. Required Outputs (Artifacts)
- **Bounded Tool Work**: Codex가 생성한 제안 결과물.
- **Return Package**: Digest, Evidence Used, Not Inspected, Issue Log.
- **Containment Check**: 구현 시도나 시스템 스캔 드리프트 발생 여부.

## 4. Constraints
- **Role Containment**: Codex는 '구조 리뷰어' 역할에 한정됨.
- **Standard Return**: 명시된 포맷 이외의 언어(Ready/Verified 등) 사용 금지.
- **Run-First/Patch-Later**: 사소한 오류는 고치지 않고 로그로 남김.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_37_HANDOFF.md` for Return Recovery Review.
