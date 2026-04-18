# Program-grade workspace surface maintenance check

## 1. overall verdict
- status: STABLE_WITH_MINOR_FIX

## 2. checked assets
- engine_input_lane_baseline_v1: PASS
- codex_baseline_program_grade_workspace_upgrade_v1: PASS
- folder_role_table_v1: REVIEW_REQUIRED
- repo_shared_reality_pack_v1: PASS
- repo_shared_reality_pack_index_v1: REVIEW_REQUIRED
- current_asset_map_v1: REVIEW_REQUIRED
- repo_delta_log_latest_v1: REVIEW_REQUIRED
- program_grade_next_phase_declaration_v1: PASS
- program_grade_workspace_surface_maintenance_directive_v1: PASS

## 3. cross-check
- current_vs_delta: PASS
- pack_vs_index: REVIEW_REQUIRED
- active_guidance_freshness: PASS
- legacy_surface_separation: REVIEW_REQUIRED
- latest_surface_compactness: REVIEW_REQUIRED

## 4. must-fix now
- [folder_role_table_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md) 의 예시 경로를 실제 repo 기준으로 맞춘다.
  - `input/` -> `inputs/`
  - `runtime/temp/` -> `runtime/tmp/`
  - `docs/directives` / `docs/declarations`는 현재 실제 primary 위치가 아니라는 점을 정리한다.
- [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md) 를 recent 중심으로 압축한다.
  - latest surface로 보기엔 길이가 길고, “최근 변화”보다 “구축 연혁” 비중이 커졌다.

## 5. safe to defer
- [current_asset_map_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/current_asset_map_v1.md) 는 역할은 유지되고 있으나 길이가 길다. delta를 먼저 압축한 뒤 current도 한 번 더 얇게 줄이면 된다.
- [repo_shared_reality_pack_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_shared_reality_pack_index_v1.md) 와 [repo_shared_reality_pack_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repo_shared_reality_pack_v1.md) 의 중복 설명은 지금 당장 붕괴 수준은 아니다. 다음 짧은 정리 턴에서 줄이면 된다.
- legacy latest surface 분류는 현재 official read order가 이미 잠겨 있으므로, 명시적 `no-longer-primary` 표기는 후속 bounded cleanup으로 미뤄도 된다.

## 6. recommended next action
- update only [folder_role_table_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md)
- update only [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md)
- do not rewrite the whole repo explanation

## 7. one-line summary
- current surface discipline is mostly preserved, but folder spec path realism and delta compactness need bounded repair.

## 8. three-line summary
- **지금 상태:** 기준면 구조는 살아 있고 current/delta/shared reality 역할도 크게 섞이지 않았다.
- **당장 고칠 것:** [folder_role_table_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md) 경로 현실화, [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md) recent 중심 압축
- **건드리지 말 것:** 코어와 shared reality 정의 전체 재서술

## 9. bounded reasoning note
- `engine_input_lane_baseline_v1`은 실제 입력 흐름과 잘 맞고, 외부자료/canonical/unclassified 처리 원칙도 current 운용과 충돌하지 않는다.
- `codex_baseline_program_grade_workspace_upgrade_v1`와 `program_grade_next_phase_declaration_v1`은 현재 우선순위와 충돌하지 않는다.
- `current_asset_map_v1`는 active guidance 반영과 공식 read order 유지 측면에서 잘 작동한다.
- 다만 `folder_role_table_v1`는 실제 repo와 다른 예시 경로가 일부 남아 있어, 장기적으로 배치 판단 혼선을 만들 수 있다.
- `repo_delta_log_latest_v1`는 역할은 맞지만 latest라기엔 길어졌다.
