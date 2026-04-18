# operation_workflow

## 목적
이 문서는 User / Codex / Gemini CLI가 실제로 어떻게 협업하는지 운영 루틴으로 정리한 문서다.

## 역할 분리
- User = 방향 / 승인 / 최종 판단
- Codex = 수정 / 실행 / 구조 관리 / 검증
- Gemini = 후단 요약 / 비교 / 점검

## 기본 운영 루프
1. Codex로 작업한다
2. `gdiff`로 변경점 검사를 본다
3. 필요하면 Codex가 수정한다
4. 실행 또는 routing을 수행한다
5. `gsum`으로 현재 상태 브리핑을 본다
6. `gcheck`로 pointer 구조나 역할 혼선을 점검한다
7. 마지막 판단은 사용자가 한다

하루 운영 흐름 한 줄:

**작업 -> gdiff -> 수정 -> 실행 -> gsum -> gcheck -> 판단**

## 권장 alias 예시
- `gdiff`
  - Gemini로 diff 요약 / 위험 후보 점검
- `gsum`
  - latest board / provenance compacted 브리핑
- `gcheck`
  - latest / per-run / pointer 구조 검사

## 실전 사용 예

### A. 구조 변경 전후
- Codex가 수정
- `gdiff`로 코어 경로 touched 여부 확인
- 이상 징후가 있으면 Codex가 다시 조정

### B. structured doc 처리 후
- Codex가 routing 실행
- latest receipt / latest board 생성 확인
- `gsum`으로 빠른 상태 요약 확인
- `gcheck`로 pointer 구조가 유지되는지 검사

### C. 장기 유지 단계
- provenance compacted latest 확인
- manual-review 후보 확인
- 필요 시 Codex만 hygiene 반영

## 누가 무엇을 하지 않는가

### User가 하지 않는 것
- 코어 패치 직접 수행
- low-level write safety 정리

### Codex가 하지 않는 것
- 사용자 승인 없이 방향 최종 확정

### Gemini가 하지 않는 것
- 파일 수정
- 코어 write
- 최종 기준선 확정
- 삭제 / 병합 승인

## 어떤 문서를 먼저 보면 좋은가
- 구조를 이해하고 싶을 때:
  - [engine_overview.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/engine_overview.md)
- Gemini를 어떻게 써야 하는지 볼 때:
  - [gemini_usage.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/gemini_usage.md)
- 프롬프트를 바로 쓰고 싶을 때:
  - [prompts_usage.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/prompts_usage.md)
- 가장 빨리 다시 시작할 때:
  - [quick_start.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/quick_start.md)

## 한 줄 결론
Codex는 손을 대고, Gemini는 뒤에서 읽고 점검하고, 사용자가 방향과 승인을 잠근다.
