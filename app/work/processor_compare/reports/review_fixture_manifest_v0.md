# review fixture manifest v0

## 1. purpose
- 이 문서는 current engine에서 `immutable regression fixture` 와 `mutable exploration control` 을 실제 manifest 형태로 고정한 첫 버전이다
- 목적은 control과 regression 기준을 같은 단어로 섞지 않기 위한 것이다

## 2. immutable regression fixture
- `fx_reg_canonical_doc004_doc005`
  - expected: `bridge_mode=canonical`, `review_state=not_applicable`
- `fx_reg_canonical_doc005_doc006`
  - expected: `bridge_mode=canonical`, `review_state=not_applicable`
- `fx_reg_canonical_live_sync`
  - expected: `bridge_mode=canonical`, `review_state=not_applicable`

이 셋은 현재 engine이 깨졌는지 확인하는 regression 기준이다.

## 3. mutable exploration control
- `fx_exp_probe_doc006`
  - expected current: `bridge_mode=possibility_candidate`, `review_state=candidate`
  - change allowed: yes
- `fx_exp_probe_doc005`
  - expected current: `bridge_mode=none`, `review_state=translation_missing`
  - change allowed: yes
- `fx_exp_probe_doc004`
  - expected current: `bridge_mode=none`, `review_state=translation_missing`
  - change allowed: yes

이 셋은 current engine의 한계와 전진을 추적하는 exploration 기준이다.

## 4. operating rule
- immutable fixture는 상태가 바뀌면 regression 경고 대상이다
- mutable control은 상태가 바뀌어도 된다
- mutable control의 변화는 다음 phase 개선의 결과일 수 있다

## 5. current reading
- 이제 `control` 이라는 단어 하나로 다루지 않는다
- 앞으로는
  - immutable regression fixture
  - mutable exploration control
를 분리해서 읽는다
