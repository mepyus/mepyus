# reference selective adoption and deferred memory spec v0

## 0. purpose

이 문서의 목적은 외부 reference를

- 지금 바로 가져올 것
- 지금은 두지 않고 `references/`에 남길 것
- 왜 아직 안 가져오는지
- 나중에 어떤 조건이 생기면 다시 열 수 있는지

를 처음 평가 시점부터 같이 기록하는 구조를 고정하는 것이다.

핵심은:
reference는 전량 도입 대상이 아니다.
하지만 지금 안 쓰는 것도 버리지 않고,
`왜 아직 안 쓰는가`와 `나중에 다시 볼 조건`까지 기억해야 한다.

---

## 1. role of references

`references/`는 archive가 아니라 `calibration memory`다.

즉 reference는 아래 셋 중 하나 이상으로 남아야 한다.

- 현재 line을 선명하게 하는 비교 재료
- 지금은 안 맞지만 나중에 재열릴 수 있는 deferred 재료
- 현재 공간이 무엇을 아직 받아들이지 않는지 보여주는 negative calibration 재료

---

## 2. evaluation principle

reference를 볼 때는 먼저 아래를 분리한다.

1. reference 전체를 받아들일지 묻지 않는다
2. 어떤 line/조각만 가져올지 본다
3. 왜 아직 안 가져오는지 남긴다
4. 나중에 어떤 공간 성숙 조건이 오면 다시 열 수 있는지 남긴다

즉 평가는 `adopt vs discard` 이분법이 아니라
`selective adoption + deferred memory` 구조여야 한다.

---

## 3. reference intake decision classes

### 3.1 adopt_now

지금 공간 안으로 가져와도 되는 것.

조건:

- 현재 line reread를 선명하게 한다
- 현재 philosophy와 충돌하지 않는다
- premature closure를 강제하지 않는다
- construction / reading / inspection loop에 바로 도움 된다

### 3.2 keep_as_calibration_reference

당장 도입하지 않지만 계속 비교 기준으로 유지할 것.

조건:

- 현재 공간과 긴장을 만든다
- 지금은 안 맞아도 line inspection에 유효하다
- 우리 구조가 무엇을 보류하는지 보여준다

### 3.3 defer_with_reason_memory

지금은 안 쓰지만,
왜 안 쓰는지와 나중에 열 조건을 함께 남길 것.

조건:

- 현재 space-first 방향과 충돌한다
- 아직 line이 충분히 두꺼워지지 않았다
- 지금 가져오면 외부 구조가 공간을 덮을 위험이 있다

### 3.4 reject_for_now_but_preserve_trace

현재 운영에는 넣지 않지만,
reference entry와 비채택 이유는 남길 것.

핵심:
reject도 삭제가 아니다.
나중에 다시 볼 수 있도록 trace를 남겨야 한다.

---

## 4. minimum intake memory fields

각 reference family 또는 intake case는 최소 아래를 남긴다.

- `reference_id`
- `reference_path`
- `entry_material`
- `first_seen_date`
- `brought_lines`
- `adopt_now`
- `keep_as_calibration_reference`
- `defer_with_reason_memory`
- `not_now_reason`
- `future_reopen_conditions`
- `current_philosophy_fit`
- `next_reread_question`

---

## 5. why not-needed reasons must be remembered

지금 필요 없는 이유도 현재 공간 이해의 일부다.

예:

- 지금은 closure가 너무 빠르다
- 지금은 PRD-first 분해가 line 숙성을 죽인다
- 지금은 business surface가 너무 앞선다
- 지금은 execution harness가 line thickening보다 앞선다

이런 이유를 남겨야,
나중에 공간이 커졌을 때
“왜 예전엔 안 썼고, 지금은 왜 다시 볼 수 있는가”가 보인다.

즉 비채택 이유는 부정 메모가 아니라
future reread의 재료다.

---

## 6. relation to three-axis loop

reference intake 평가는 아래 순서를 따른다.

1. `construction`
   - reference를 `references/`에 넣고 provenance를 남긴다
2. `line reading`
   - reference가 들고 온 line을 뽑는다
3. `human-language meaning reread`
   - 왜 이 reference가 우리 공간을 흔드는지 사용자 언어로 푼다
4. `line inspection`
   - 지금 도입이 premature한지 본다
5. `reference intake memory`
   - adopt/defer/not-now 이유와 reopen 조건을 기록한다

즉 intake memory는 loop 바깥 부속물이 아니라
three-axis loop의 기록면이다.

---

## 7. operational rule

앞으로 새 reference를 넣을 때는:

- 전체를 도입하려 하지 않는다
- line 단위로 가져올 것을 뽑는다
- 안 가져오는 것도 이유와 함께 남긴다
- future reopen 조건을 처음부터 기록한다

즉:
`reference import`가 아니라
`reference evaluation memory`를 같이 만든다.

---

## 8. one-line summary

앞으로 reference는
지금 필요한 것만 선택적으로 가져오고,
지금 필요 없는 것도 이유와 future reopen 조건을 기록한 채
`references/`의 calibration memory로 유지한다.
