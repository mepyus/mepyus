# mixed corridor format disentangle stage4 spec

## 1. 목적

- corridor 반응이 진짜 transition meaning 때문인지, 아니면 format/source-family 껍질이 일부 밀어주는지 분리 관찰한다.

## 2. 현재 baseline

- strongest mixed corridors는 stage3 boundary challenge를 통과했다.
- off-axis에서도 annotation/source-family 기반 weak resonance가 남았다.
- `stable_closure_reached` 는 아직 없다.

## 3. 왜 format/source-family disentangle가 필요한가

- stage3는 specificity를 보여줬지만, 같은 family/format이 weak echo를 만드는지까지는 분리하지 못했다.
- 이번 단계는 meaning-driven / format-assisted / family-assisted / format-noisy 를 observer layer에서 구분하는 단계다.

## 4. 4개 입력 그룹 정의

- `same_meaning_different_format`
- `same_format_different_meaning`
- `same_family_shifted_axis`
- `cross_family_same_corridor`

## 5. match type 정의

- `corridor_specific_reentry`
- `arrival_axis_match`
- `bridge_partial_echo`
- `anchor_only_echo`
- `format_resonance_only`
- `no_meaningful_match`

## 6. disentangle judgment 정의

- `meaning_driven`
- `format_assisted`
- `family_assisted`
- `format_noisy`
- `unclear`

## 7. 비목표

- 코어 수정
- promotion rule 추가
- mixed/canonical 경계 변경
- observer evidence를 core truth로 승격

## 8. 성공 조건

- 4개 입력 그룹이 분리 등록된다.
- strongest corridors에서 meaning vs format 반응 차이가 보인다.
- annotation/source-family 착시가 별도로 기록된다.
- `stable_closure_reached` 없음이 다시 확인된다.
