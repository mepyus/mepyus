# transition mixed compare board v2

## 1. 반복된 transition pattern
- `technical->organization`: `5`
- `technical->business`: `1`

## 2. round1 / round2 공통 mixed 구조
- repeated anchor는 충분하다
- bridge fragment도 보인다
- 하지만 closure는 transition-led라 spread된 상태로 남는다

## 3. strongest surviving bridge 유형
- `Counter({'transition_bridge': 18, 'technical_anchor': 6, 'org_anchor': 5, 'business_anchor': 1})`

## 4. 반복 closure weakness 유형
- `Counter({'transition_overextension': 6, 'join_gap': 6, 'closure_spread': 6})`

## 5. canonical과 mixed의 경계 차이
- canonical은 straight flow가 길고 bridge가 closure까지 닫힌다
- mixed는 bridge가 있으나 closure가 hold 상태로 남는다

## 6. 지금 손대도 되는 설명면 강화 항목
- hold_reason을 카드 최상단에 고정
- bridge fragment를 역할별로 바로 보이게 표기
- closure_gap을 한 줄로 요약

## 7. 아직 코어로 올리면 안 되는 항목
- source_local_ref/translated handle 세분 원인을 mixed transcript 전체 규칙으로 일반화하는 것
- mixed를 곧바로 재분류 규칙으로 바꾸는 것
