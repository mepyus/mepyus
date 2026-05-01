# Question Mode Examples For Codex v0

## Purpose

질문을 interpretation packet으로 바꾸는 예시를 제공한다.

## Execution

## Example A: Exploration

User request:

> 지금 이 공간에서 Codex가 먼저 읽어야 할 자산을 찾아줘.

Packet summary:

- `task_mode`: `exploration`
- `interpreted_goal`: Codex first-read assets identify.
- `search_targets`: `CURRENT.md`, `vectorfl_status.md`, `docs/guides/vectorfl_space_asset_access_map_v0.md`, `source_assets/baselines/folder_status.md`
- `merge_mode_candidate`: `merge`
- `ambiguity_notes`: `none`

## Example B: Comparison

User request:

> 현재 baseline과 최근 report가 충돌하는지 봐줘.

Packet summary:

- `task_mode`: `comparison`
- `search_targets`: baseline docs first, then reports.
- `merge_mode_candidate`: `diff`
- `ambiguity_notes`: `provisional`, because exact baseline/report may need narrowing.

## Example C: Merge

User request:

> 이 판단을 기존 공간 운영 원칙에 맞춰 합쳐줘.

Packet summary:

- `task_mode`: `merge`
- `search_targets`: source authority ladder, relevant baseline, given judgment.
- `merge_mode_candidate`: `merge`
- `hold_reason_if_any`: empty unless high-authority conflict appears.

## Example D: Verification

User request:

> Phase 1이 UI 없이 돌아가는지 검증해줘.

Packet summary:

- `task_mode`: `verification`
- `search_targets`: Phase 1 contracts, runtime packet skeletons, scenario reports.
- `expected_output_shape`: validation report.
- `merge_mode_candidate`: `merge` or `diff` depending on gaps.

## Example E: Reflection Support

User request:

> 이 방향이 왜 translation/handoff 문제인지 정리해줘.

Packet summary:

- `task_mode`: `reflection_support`
- `search_targets`: Phase 1 goal, connection/user-layer translation baseline, current status.
- `external_reasoning_needed`: true only for Codex general reasoning, not external web lookup.
- `merge_mode_candidate`: `merge`

## Interpretation

이 예시들은 질문을 answer target이 아니라 operating packet으로 바꾸는 훈련 자산이다. Codex는 질문을 받으면 먼저 이 예시와 계약을 통해 목표/권위/탐색 경로/산출형을 분리한다.

## Validation

- exploration, comparison, merge, verification, reflection_support가 구분된다.
- 애매한 비교 대상은 hard hold가 아니라 provisional로 시작할 수 있다.
- destructive action이나 authority inversion은 packet 단계에서 stop condition으로 남긴다.
