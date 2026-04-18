# latent line first reread rule v1

## 1. 목적

이 문서는 공간 전체를 먼저 뒤지는 규칙이 아니다.

목적은 먼저 latent line을 입구로 잡고, 그 선을 따라 관련 자료를 다시 읽는 순서를 고정하는 것이다.

즉:

1. latent line이 먼저 보인다
2. 그 선을 따라 관련 자료를 다시 읽는다
3. 재독해 속에서 새 의미 / 새 연결 / 새 질문을 본다
4. 그 과정을 다시 흔적으로 남긴다

## 2. 이번 reread에서 먼저 잡은 latent line

- `pre_read_eye`

### 왜 지금 이 선인가

이 선은 읽기 전에 mode / phase / drift를 먼저 세우는 선이다.

지금 공간에서 가장 먼저 작동하는 장치가 preflight gate와 breadcrumb 연결이기 때문에,
이번 재독해는 content-first가 아니라 line-first로 들어가는 것이 맞다.

### line-first의 의미

- 전체 내용을 먼저 훑지 않는다
- 선을 먼저 입구로 잡는다
- 그 선을 따라 관련 자료만 다시 읽는다

## 3. 다시 읽은 자료

- `control/space_kernel.json`
- `control/turn_router.json`
- `control/drift_guard.json`
- `runtime/current_phase.json`
- `runtime/preflight_last_decision.json`
- `runtime/breadcrumbs.jsonl`
- `docs/reports/process_reread_map_v1.md`
- `docs/reports/deep_internal_reread_long_arc_map_v1.md`

## 4. 다시 보인 것

### 4.1 preflight가 실제로 읽기 전에 먼저 작동한다

- `space_kernel`은 이 공간이 무엇인지와 무엇이 아닌지를 잠근다.
- `turn_router`는 질문을 mode로 먼저 라우팅한다.
- `drift_guard`는 immediate solution / implementation jump / summary shortcut / widening jump를 경계한다.
- `current_phase`는 현재 읽기 프레임을 고정한다.
- `preflight_last_decision`은 selected_mode / selected_artifact_group / first_read_ref를 먼저 정한다.

이 조합은 설명문이 아니라 pre-read gate로 읽혀야 한다.

### 4.2 breadcrumbs가 판단 이동을 남긴다

`breadcrumbs.jsonl`은 단순 로그가 아니라,
왜 읽었는지 / 무엇을 봤는지 / 다음으로 왜 이동했는지를 남긴다.

즉 preflight decision이 content 읽기보다 먼저 있고,
breadcrumb는 그 decision의 흔적을 남긴다.

### 4.3 mode-first reading이 content-first보다 앞선다

이번 재독해에서 다시 확인된 것은,
이 공간이 내용을 먼저 뒤지는 곳이 아니라는 점이다.

- 먼저 mode가 정해지고
- 그 다음 first_read_ref가 정해지고
- 그 다음 자료를 읽고
- 그 다음에야 새 연결이 보인다

## 5. 새롭게 강해진 것

- `pre_read_eye`는 단순 잠복 선이 아니라 실제 재독해 입구로 강화되었다.
- preflight와 breadcrumb가 실제로 연결되면서, 읽기 전에 먼저 분기하는 구조가 더 선명해졌다.
- latent line은 기록 대상이면서 동시에 재독해 입구라는 점이 더 분명해졌다.

## 6. 아직 부족한 것

- 아직 전체 공간을 이 규칙으로 자동 순회하는 것은 아니다.
- 아직 latent line registry가 새 observation마다 자동 갱신되는 시스템은 아니다.
- 아직 `pre_read_eye` 이외의 선들이 같은 강도로 반복 검증된 것은 아니다.

## 7. 앞으로 새 observation을 볼 때의 얇은 판정 기준

새 observation이 들어오면 먼저 candidate를 만들지 않고,
어느 latent line이 먼저 짙어졌는지 본다.

이번 규칙에서는 특히 다음을 먼저 본다.

- mode / phase / drift가 읽기 전에 먼저 정해졌는가
- first_read_ref가 전이 전에 명확한가
- breadcrumb가 preflight decision과 연결되는가
- content보다 선이 먼저 입구가 되었는가

## 8. 한 줄 결론

> latent line은 기록 대상이기 전에, 재독해의 입구다.

