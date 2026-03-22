# transition mixed fix boundary note v2

## 1. 지금 바로 반영할 표현면 개선
- 카드 최상단에 transition_from / transition_to / hold_reason / reading_status 고정
- bridge fragments 역할별 표기
- closure_gap 한 줄 요약

## 2. 다음 관찰 후 판단할 것
- good_hold와 unclear_hold가 실제로 갈라지는지
- transition_to를 더 세분화할 필요가 있는지

## 3. 코어 수정 금지 영역
- mixed 판정 규칙 변경
- source_local_ref / translated_handles 생성 규칙 변경
- bridge admission 로직 변경
