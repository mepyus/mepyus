# Evidence Merge Diff Hold Contract v0

## Purpose

공간 evidence와 Codex 자체 판단을 비교해 `merge`, `diff`, `hold` 중 하나로 정리한다.

## Execution

Merge/diff report minimum fields:

- `question_packet_ref`
- `exploration_result_ref`
- `space_position`
- `codex_position`
- `alignment_points`
- `difference_points`
- `unresolved_tensions`
- `chosen_mode`
- `final_reasoning_basis`
- `user_decision_required`
- `user_decision_reason_if_any`

Allowed `chosen_mode` values:

- `merge`
- `diff`
- `hold`

Mode rules:

- `merge`: 공간 근거와 Codex 판단이 같은 방향이며 차이가 보조 설명 수준이다.
- `diff`: 의미 있는 차이가 있지만 사용자 결정 없이 비교 결과로 남길 수 있다.
- `hold`: high-authority conflict, destructive migration, 운영 철학 충돌, user-only naming/meaning decision이 있다.

## Interpretation

Codex 판단과 공간 근거를 동일시하면 안 된다. Codex는 일반 추론과 구현 판단을 제공하지만, 공간이 이미 잠근 baseline과 current working baseline을 덮어쓸 권위는 없다. 반대로 공간 근거가 얇을 때 Codex 판단은 provisional improvement candidate로 남을 수 있다.

차이를 지우지 말고 구조화해야 하는 이유는 difference가 다음 숙성의 재료이기 때문이다. merge는 차이를 삭제하는 것이 아니라, 차이가 phase goal과 충돌하지 않을 때 함께 둘 수 있다는 판단이다.

authority ladder는 이 단계에서 conflict resolution 우선순위를 제공한다. 높은 권위가 직접 충돌하면 hold, 낮은 권위가 높은 권위의 빈틈을 보완하면 provisional merge, 최신 report가 baseline과 다르게 움직이면 diff로 남긴다.

## Validation

- merge 기준은 alignment와 차이의 성격을 둘 다 본다.
- diff는 차이 목록과 final reasoning basis를 요구한다.
- hold는 stop condition에 한정한다.
- 사용자 승인 없이 해결 가능한 차이와 아닌 차이를 분리한다.

## Stage 4 Closeout

- Verdict: `PASS`
- Files created: `docs/specs/evidence_merge_diff_hold_contract_v0.md`, `runtime/contracts/merge_diff_report_v0.json`, `docs/guides/alignment_resolution_rules_v0.md`
- Example merge report: `docs/reports/phase1_scenario_run_01_v0.md`
- Example diff report: `docs/reports/phase1_scenario_run_02_v0.md`
- Example hold report: `docs/reports/phase1_scenario_run_03_v0.md`
- Entry condition for next stage: chosen mode and reasoning basis can be packaged for return/reingress.
