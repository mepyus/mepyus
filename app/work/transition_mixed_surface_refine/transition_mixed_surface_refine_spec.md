# transition mixed surface refine spec

## 1. 목적
- transition-led mixed를 코어 수정 없이 더 읽기 쉽게 보여주는 readable surface를 만든다.

## 2. 현재 진단
- anchor는 살아 있다
- bridge도 있다
- hold 가치도 있다
- 하지만 사용자는 어디서 전환이 일어났고 왜 stable closure가 안 됐는지 한눈에 보기 어렵다

## 3. 왜 코어 수정이 아닌 surface 강화인가
- 현재 반복 병목은 판독 실패보다 표시 해상도 부족에 가깝다
- mixed 반복 패턴은 이미 충분히 포착돼 있다
- 그래서 이번 턴은 표현면 개선만 수행한다

## 4. 카드 헤더 표준
- `transition_from`
- `transition_to`
- `hold_reason`
- `reading_status`

## 5. bridge fragment 표시 규칙
- fragment를 `technical_anchor / transition_bridge / business_anchor or org_anchor` 로 보이게 적는다
- 각 fragment 옆에 짧은 역할 문장을 붙인다

## 6. closure gap 한 줄 요약 규칙
- `closure_gap: ...`
- `why_not_canonical: ...`
- 길게 풀지 않고 즉시 판독 문장으로 쓴다

## 7. mixed_quality 시범 표기 기준
- `good_hold`: repeated anchor 충분, bridge fragment 명확, unreadable로 버리면 손실 큼
- `unclear_hold`: 위 조건이 약한 경우

## 8. operator summary 형식
- 전체 진단
- 가장 자주 반복된 전환
- mixed가 되는 직접 이유
- 지금 먼저 개선할 surface
- 아직 코어 수정으로 가면 안 되는 이유
- 한 줄 결론

## 9. 이번 턴 비목표
- 코어 규칙 변경
- mixed 재분류
- ontology 확장
- 새 ingest 규칙 추가
