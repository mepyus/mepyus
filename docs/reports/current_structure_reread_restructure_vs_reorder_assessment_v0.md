# current structure reread: restructure vs reorder assessment v0

## 0. verdict

현재 구조는 **전면 재편 대상이 아니라, 그대로 두고 정돈해야 하는 상태**에 더 가깝다.

즉 바닥 철학과 주요 레인은 이미 많이 맞다.
문제는 구조가 틀린 것보다,

- 읽기 순서가 흐려졌고
- 같은 의미가 여러 문서군에 퍼져 있고
- observation보다 lock/surface 문서가 더 두껍게 보이며
- 실제 reread loop 운영이 문서 밀도만큼 생활화되지 않았다는 점

에 있다.

---

## 1. what is already structurally right

### 1.1 top-level split is already good

현재 최상위 분리는 오히려 건강하다.

- `inputs/`
- `source_assets/`
- `docs/`
- `references/`
- `app/`
- `runtime/`

이 분리는
`재료 -> 기준 -> 엔진 -> trace/view`
를 나누는 데 충분하다.

즉 지금 문제는 top-level shape가 아니라
그 안에서 어떤 레인을 주 레인으로 읽게 할지의 문제다.

### 1.2 philosophy already points the right way

`CURRENT.md`는 아직 fragment 중심 언어가 강하지만,
`source_assets/baselines/*`, `references/*`, latent line 자료를 같이 읽으면
현재 공간의 바닥은 이미 아래 쪽을 향한다.

- preserve first
- hold/calibration lane
- reread before promotion
- delayed condensation
- space first, llm later

즉 철학은 많이 어긋나 있지 않다.
오히려 surface wording이 아직 그 철학을 전면에 올리지 못한 쪽이다.

### 1.3 runtime trace stack is already present

`runtime/receipts`, `runtime/manifests`, `runtime/views`, `runtime/events`,
`app/core/runtime/line_thickening.py`,
`runtime/manifests/latent_line_registry_v1.json`
을 보면
공간이 line / reread / observation / handoff를 저장할 수 있는 몸체는 이미 있다.

즉 “몸이 없다”가 아니라
“몸을 어떻게 반복적으로 돌릴지의 운영 시선이 아직 약하다”가 더 맞다.

---

## 2. what is structurally weak now

### 2.1 docs are too dense around lock/close-out

`docs/specs`, `docs/notes`, `docs/reports`에
좋은 재료가 많지만,
현재는 reread observation보다
spec lock / note / close-out 흔적이 훨씬 더 밀도 높게 보인다.

이건 구조 오류라기보다
운영의 무게중심이 잠금 쪽으로 기울었던 흔적이다.

### 2.2 line memory is split between rich latent docs and thin runtime registry

`runtime/manifests/line_registry.json`은 얇고,
`runtime/manifests/latent_line_registry_v1.json`은 더 풍부하다.

즉 현재 line memory가 한 표면에서 일관되게 두꺼워진 게 아니라,
문서군과 runtime이 약간 이중으로 나뉘어 있다.

이건 새 구조를 만들기보다
현재 어떤 registry를 실제 주 line memory로 읽을지 정돈이 필요하다는 신호다.

### 2.3 current reading order is not explicit enough

지금 repo는 읽을 것이 너무 많다.
특히 `docs/reports/today_handoff_index_v1.md` 같은 색인은 풍부하지만,
그 자체가 line-first reread loop의 생활화를 보장하지는 않는다.

즉 구조는 풍부한데,
어떤 재료를 먼저 읽고 어떤 것을 나중에 reread할지의
운영 reading order가 아직 과밀하다.

### 2.4 whole-space observer exists more as direction than habit

`space_wide_line_ecology_and_hub_growth_observer` 같은 기준은 잠겨 있지만,
실제 repo 전체에서
같은 line을 4~5번 돌려 목적어를 바꿔 읽는 습관은 아직 드물다.

이건 구조 결함보다
운영 습관 결핍에 가깝다.

---

## 3. restructure or reorder?

현재 판정은 분명하다.

### not now: full restructure

지금 전면 재편을 하면
오히려 이미 살아 있는 레인까지 다시 흐리게 만들 가능성이 크다.

특히 아래는 이미 꽤 맞는다.

- raw vs source asset split
- calibration/reference lane
- runtime trace lane
- observation/readout lane
- policy/spec/baseline lane

즉 지금은 갈아엎을 이유보다
살아 있는 레인을 더 선명하게 정돈할 이유가 더 크다.

### yes now: reorder / declutter / reread-oriented organization

지금 필요한 것은 재편보다 아래다.

1. 현재 주 레인을 더 명시적으로 읽기
2. line memory를 어디서 우선 읽을지 정하기
3. spec/note/close-out 과밀을 observation/reread 흐름 기준으로 다시 묶기
4. 같은 선을 반복 reread하는 관찰 루프를 실제 운영 습관으로 올리기

즉 구조를 다시 만드는 것이 아니라
**이미 있는 구조를 reread-first로 재정렬하는 일**이 먼저다.

---

## 4. what should be treated as the current main rails

현재 기준에서 main rail은 아래처럼 읽는 것이 맞다.

### rail 1. input / source material rail

- `inputs/`
- `source_assets/`

### rail 2. calibration / reference rail

- `references/`

### rail 3. line / reread observation rail

- `docs/reports/latent_line_*`
- `docs/reports/process_reread_*`
- `docs/reports/deep_internal_reread_*`
- `runtime/manifests/latent_line_registry_v1.json`
- `app/core/runtime/line_thickening.py`

### rail 4. runtime trace / surfaced rail

- `runtime/receipts`
- `runtime/manifests`
- `runtime/views`
- `app/core/runtime/*`
- `app/runtime/*`

### rail 5. lock / boundary rail

- `docs/specs`
- `docs/notes`
- `docs/policies`

지금 문제는 rail이 없는 것이 아니라,
rail 5가 너무 두껍게 보이고
rail 3의 생활 reread가 상대적으로 약하다는 것이다.

---

## 5. current recommendation

현재는 구조를 다시 만들지 말고
아래처럼 정돈하는 것이 맞다.

1. `line-first reread`를 주 운영 습관으로 올린다
2. 외부 자료 하나를 입구로 삼아 전체 공간 reread하는 실험을 반복한다
3. same line / different objective / different folder reread를 계속 돌린다
4. line registry 계열은 latent line registry를 우선 관찰면으로 읽는다
5. spec lock은 reread 관찰 뒤에만 붙인다

즉 지금의 올바른 움직임은
새 구조를 만드는 것이 아니라
**현재 구조를 reread-oriented living structure로 바꾸는 것**이다.

---

## 6. one-line summary

현재 repo는 갈아엎어야 할 정도로 틀린 구조가 아니다.
오히려 바닥 철학과 주요 레인은 이미 많이 맞다.
지금 필요한 것은 전면 재편이 아니라,
잠금 중심으로 두꺼워진 표면을 걷어내고
line-first reread가 실제로 자주 일어나는 쪽으로 구조를 다시 정돈하는 것이다.

