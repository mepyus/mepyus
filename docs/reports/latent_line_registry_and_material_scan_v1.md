# latent line registry and material scan v1

## 1. 목적

이 문서는 잠복 선을 후보가 아니라 관찰 객체로 다루기 위한 얇은 도구 문서다.

목적은 현재 공간에 이미 있는 자료들을 다시 훑어,
어떤 선이 어디서 짙어지는지 앞으로 태그할 수 있게 만드는 것이다.

## 2. 무엇을 만들었는가

- registry:
  - `runtime/manifests/latent_line_registry_v1.json`
- scan report:
  - 이 문서

## 3. scan한 자료군

### 3.1 vectorfl internal formation materials

- `docs/reports/process_reread_map_v1.md`
- `docs/reports/deep_internal_reread_long_arc_map_v1.md`
- `docs/reports/latent_line_watchpoints_v1.md`

읽은 결과:
- `pre_read_eye`
- `raw_return_preservation`
- `transition_over_surface`
- `input_to_reading_organ`
이 이미 내부 형성사 안에서 살아 있다.

### 3.2 claude_code bridge materials

- `docs/reports/claude_code_latent_lines_bridge_v1.md`
- `docs/reports/youtube_03_29_claude_code_latent_lines_reread_v1.md`
- `docs/reports/youtube_03_29_and_claude_code_common_latent_lines_comparison_v1.md`

읽은 결과:
- `alignment_before_autonomy`
- `harness_over_model`
- `work_absorption_harness`
가 우리 공간의 `pre_read_eye`, `transition_over_surface`, `input_to_reading_organ`에 직접 접붙는다.

### 3.3 runtime evidence

- `runtime/preflight_last_decision.json`
- `runtime/breadcrumbs.jsonl`
- `runtime/manifests/pipeline_observation_registry.jsonl`
- `runtime/manifests/pipeline_candidate_scope_summary.json`
- `runtime/manifests/second_candidate_watch_rules.json`

읽은 결과:
- 잠복 선은 이미 단순 문장 해석이 아니라 실제 append-time / pre-read-time 판정에 붙고 있다.
- 특히 `pre_read_eye`는 preflight와 breadcrumbs로, `input_to_reading_organ`은 registry / summary / watch rule로 나타난다.

## 4. 지금 가장 강한 잠복 선

- `pre_read_eye`
- 이유:
  - preflight가 읽기 전에 mode / drift를 먼저 정한다.
  - append-time watch rule도 선행 판정으로 붙는다.

## 5. 지금 가장 얇지만 중요한 잠복 선

- `input_to_reading_organ`
- 이유:
  - 기록 / 관찰 / watch는 이미 있지만,
  - 아직 interpretation / lineage / multi-lens까지 완전 기관화되지는 않았다.

## 6. append-time tagging rule

새 observation이 들어오면 candidate를 먼저 만들지 말고,
먼저 latent line을 태그한다.

권장 태그 순서:
1. `pre_read_eye`
2. `raw_return_preservation`
3. `transition_over_surface`
4. `input_to_reading_organ`
5. `alignment_before_autonomy`
6. `harness_over_model`
7. `work_absorption_harness`

### 판정 기준

- `strong match`
  - line의 정의와 evidence가 직접 맞는다.
- `partial match`
  - line의 방향은 맞지만 아직 얇다.
- `boundary only`
  - 기존 선의 경계 설명으로만 접힌다.
- `no tag`
  - 억지로 선을 붙이면 안 된다.

## 7. 현재 evidence가 말하는 것

- `claude_code` 계열은 하네스 / 정렬 / 흡수 선을 운영형으로 보여준다.
- `youtube_03_29`는 그 선을 원칙층에서 먼저 세운다.
- 내부 vectorfl 자료는 그 선들이 실제 preflight / breadcrumb / registry로 응축된 결과를 보여준다.

## 8. 아직 부족한 것

- latent line registry가 아직 자동 갱신되는 시스템은 아니다.
- 이 문서는 수동 scan의 첫 버전이다.
- 하지만 선을 candidate보다 먼저 보는 기준면은 이미 생겼다.

## 9. 앞으로 이 문서로 다시 볼 수 있는 것

- 어떤 자료가 하네스 선을 강화하는지
- 어떤 자료가 정렬 우선 선을 강화하는지
- 어떤 자료가 입력 구조를 읽기 기관으로 자라게 하는지
- 새 observation이 들어왔을 때 candidate 이전에 어떤 latent line이 먼저 짙어지는지

## 10. 한 줄 결론

> 잠복 선은 더 많은 candidate를 만드는 문제가 아니라, 이미 있는 자료들을 선 단위로 다시 읽고 append-time에 태그하는 관찰면을 먼저 세우는 문제다.

