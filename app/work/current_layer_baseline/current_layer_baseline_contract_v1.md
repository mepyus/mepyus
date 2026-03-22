# Current Layer Baseline Contract v1

## 1. 역할 잠금
- 현재 레이어는 정답을 빠르게 확정하는 레이어가 아니다.
- 현재 레이어는 `조기 폐기 방지 + hold 이유 기록 + 재진입 가능성 보존 + observer-first 운영` 을 담당한다.

## 2. mixed hold 의미
- `mixed hold` 는 실패 더미가 아니다.
- `mixed hold` 는 `anchor_alive + bridge_alive + stable closure 미도달` 상태의 `productive hold corridor` 다.
- 즉 입력이 붕괴한 것이 아니라, 전환 corridor가 아직 closure까지 응축되지 않은 상태를 보존한다.

## 3. canonical / mixed / unreadable 경계
- `bridge 없음` -> `unreadable` 쪽
- `bridge 있음 + stable closure 없음` -> `mixed / confirmed_hold`
- `bridge 있음 + stable closure 도달` -> `canonical / stable_reading`

핵심:
- 경계는 `전환 존재 여부`가 아니라 `stable closure 도달 여부` 다.

## 4. mixed 반복 패턴
- `source_survival = kept`
- `translation_survival = formed`
- `repeated_anchor_support = sufficient`
- `join_closure = gap_dominant`
- `closure = transition-led`

핵심 병목:
- `anchor 부족` 이 아니라 `technical -> business/org transition closure weakness`

## 5. readable surface 계약
모든 mixed 카드/보드는 최소 아래를 보여줘야 한다.
- `transition_from`
- `transition_to`
- `hold_reason`
- `reading_status`
- `mixed_quality`
- `bridge fragments`
- `closure_gap`
- `why_not_canonical`

## 6. re-entry 잠금
- `mixed hold` 는 `dead-end` 가 아니다.
- `re-entry` 는 실제로 작동한다.
- 후속 입력에서
  - repeated anchor 강화
  - arrival axis 선명화
  - closure support 부분 강화
  가 나타날 수 있다.

하지만:
- `stable_closure_reached = 없음`
- `re-entry 있음 = canonical` 은 금지

현재 결론:
- `mixed hold = re-entry 가능한 productive hold corridor`
- promotion rule 논의는 아직 금지

## 7. specificity 잠금
- reinforcing / adjacent / off-axis 비교에서 corridor specificity는 실제로 보였다.
- 즉 corridor는 loose topic resonance가 아니라 `specific transition corridor` 에 가깝다.

하지만:
- annotation / source-family 착시는 약하게 남는다.
- 따라서 현재 specificity 판정은 `observer-only` 로 유지한다.

## 8. meaning vs noise 잠금
현재 clean baseline:
- `technical->organization::ai_business = mostly_meaning_driven`
- `technical->organization::harness_agent = mostly_meaning_driven`

현재 noisy focus corridor:
- `technical->business::ai_business = multi_axis_business_mix`

## 9. business corridor observer split
현재 `technical->business::ai_business` 는 코어 truth로 분할하지 않는다.

observer split candidate:
- `startup_thesis`
- `monetization_value_capture`
- `org_business_boundary`

보조 후보:
- `business_leverage`
- `software_value_shift`

현재 판정:
- `keep_as_one_corridor = observer_only_split_recommended`
- `observer_split_candidate = yes`

## 10. 금지 항목
### promotion 금지
- canonical 승격 규칙 추가
- re-entry 기반 승격
- stable closure 없는 상태에서 승격 논의

### 코어 변경 금지
- mixed / canonical 경계 규칙 변경
- business corridor 코어 분할
- organization corridor 재정의
- observer 결과를 코어 truth로 오인

### 해석 과잉 금지
- format noise가 있다고 corridor 전체 무효화
- partial echo를 완전 specificity 증거로 과장
- good hold를 구조 규칙으로 조기 승격

## 11. 다음 단계 진입 전제
다음 단계는 아래 순서로만 간다.
1. 현재 레이어 계약 유지
2. business 하위축 observer split ledger 누적
3. 다음 단계 진입 조건 문서화

stable closure 논의로 가기 전 최소 조건:
- repeated cross-input reinforcement 누적
- format/source-family noise 추가 분리
- observer split candidate 안정화
- `stable_closure_reached` 실제 증거

## 12. 한 줄 기준
- 현재 레이어는 `mixed를 버리지 않고 hold로 남기며, re-entry와 specificity를 observer layer에서 검증하고, stable_closure_reached 가 없으므로 promotion/코어 승격 논의는 금지한 채 business 내부 혼합을 분리 기록하는 기준선 레이어` 다.
