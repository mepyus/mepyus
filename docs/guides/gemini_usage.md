# gemini_usage

## 목적
이 문서는 Gemini CLI를 어디까지 쓸 수 있고 어디부터 금지인지 사용자 기준으로 설명하는 문서다.

중요:
- [gemini/gemini.md](/Users/sungsookim/universe/vectorfl_replica/gemini/gemini.md) = 역할 헌법
- 이 문서 = 실제 사용 설명서

## 한 줄 정의
**Gemini는 엔진을 바꾸는 손이 아니라 결과를 읽고 점검하는 눈이다.**

## Gemini가 해도 되는 일

### 요약
- receipt 요약
- latest board 브리핑
- provenance compacted 결과 설명
- per-run 결과 짧은 정리

### 비교
- diff 리뷰
- 지난 run vs 이번 run 비교
- latest vs per-run 관계 비교
- policy 문서 vs 산출 비교

### 점검
- latest가 pointer형을 유지하는지 검사
- per-run이 상세를 유지하는지 검사
- raw / compacted / latest 역할 혼선 확인
- 경로 존재 여부 확인

### 운영 설명 보조
- 운영 화면 문구 초안
- 상태 카드 문안
- manual-review 설명문

## Gemini가 하면 안 되는 일

### 절대 금지
- 파일 수정
- registry / provenance / event write
- routing core 수정
- atomic / lock / recovery 경로 수정
- 기준선 확정
- 삭제 / 병합 판단
- 코어 구조 재정의

한 줄로:

**Gemini는 절대로 수정 주체가 아니다.**

## Gemini 출력 규칙
- 확정 판단하지 않는다
- 후보 / 의심 / 확인 필요 포인트로 제시한다
- 근거 파일 경로를 포함한다
- 불확실하면 불확실하다고 적는다
- 가능하면 체크리스트형으로 정리한다

## 기본 호출 태도
- 수정하지 마라
- 판단 확정하지 마라
- 후보만 제시하라
- 근거를 적어라
- 불확실하면 표시하라

## 언제 유용한가
- Codex가 큰 패치를 한 직후
- latest board가 너무 무거워졌는지 보고 싶을 때
- quick status briefing이 필요할 때
- pointer 구조가 깨졌는지 의심될 때

## 먼저 읽으면 좋은 기준 문서
- [gemini/gemini.md](/Users/sungsookim/universe/vectorfl_replica/gemini/gemini.md)
- [operation_workflow.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/operation_workflow.md)
- [prompts_usage.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/prompts_usage.md)

## 한 줄 결론
Gemini는 후단 보조 판독기다. 읽고, 비교하고, 점검하되, 손대지는 않는다.
