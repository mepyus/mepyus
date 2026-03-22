# Local Constitution

이 저장소의 로컬 헌법은 [`docs/contracts/ADJACENT_SPACE_CONTRACT.md`](/Users/sungsookim/universe/vectorfl_next/docs/contracts/ADJACENT_SPACE_CONTRACT.md)를 구현 관점에서 다시 고정한 것이다.

## Authority order

1. `docs/contracts/ADJACENT_SPACE_CONTRACT.md`
2. `docs/contracts/CODEX_TASK.md`
3. `docs/contracts/GEMINI_TASK.md`
4. architecture / decision / checklist 문서
5. code

## Hard rules

- `../vectorfl` 수정 금지
- stage 구조 복제 금지
- point/cluster/promotion 중심 회귀 금지
- reader/control vocabulary의 core 침범 금지
- append-only event log 원칙 훼손 금지

## Build posture

- 먼저 경계와 불변조건을 만든다.
- 나중에 들어올 시간, 감정, 환류 압력을 위한 자리를 남긴다.
- 애매한 경우 더 똑똑한 알고리즘보다 더 명확한 기록을 우선한다.

## Review posture

- 새 파일이나 서비스가 생길 때마다 아래를 묻는다.
- 이것이 formation-first인가?
- 이것이 anti-collapse인가?
- 이것이 cell integrity를 지키는가?
- 이것이 core/reader separation을 지키는가?
