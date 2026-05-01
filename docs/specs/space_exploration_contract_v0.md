# Space Exploration Contract v0

## Purpose

question interpretation packet을 기반으로 공간 자산을 찾아 evidence bundle을 만드는 규약이다.

## Execution

Exploration result minimum fields:

- `question_packet_ref`
- `searched_paths`
- `selected_assets`
- `selected_asset_reasons`
- `discarded_assets`
- `evidence_units`
- `supporting_links`
- `tension_or_conflict_assets`
- `missing_gaps`
- `confidence`
- `next_probe_candidates`

Evidence unit minimum fields:

- `source_ref`
- `excerpt_or_pointer`
- `why_it_matters`
- `relation_type`
- `confidence`

Allowed `relation_type` values:

- `direct_support`
- `contextual_support`
- `tension`
- `contrast`
- `weak_candidate`

## Interpretation

단일 정답 회수보다 evidence bundle이 중요한 이유는 공간의 자산이 하나의 결론보다 여러 층의 위치값으로 존재하기 때문이다. 같은 질문도 baseline, current pointer, report, runtime artifact가 서로 다른 역할로 답한다.

discard와 gap을 기록해야 하는 이유는 찾지 않은 것과 찾았지만 쓰지 않은 것이 다음 질문의 판단 재료가 되기 때문이다. conflict 자료도 버리지 않고 tension으로 남겨야 Codex 판단과 공간 판단을 안전하게 비교할 수 있다.

질문은 여러 라인/축을 동시에 건드릴 수 있다. 따라서 exploration result는 파일 목록이 아니라 관계가 붙은 근거 묶음이어야 한다.

## Validation

- 탐색 결과는 selected/discarded/gap/conflict를 분리한다.
- 자료 부족은 실패가 아니라 `missing_gaps`로 기록한다.
- confidence는 근거 강도와 권위층을 반영한다.
- 다음 단계 merge/diff/hold가 바로 사용할 수 있다.

## Stage 3 Closeout

- Verdict: `PASS`
- Files created: `docs/specs/space_exploration_contract_v0.md`, `runtime/contracts/space_exploration_result_v0.json`, `docs/guides/evidence_selection_rules_v0.md`, `docs/guides/exploration_failure_and_gap_handling_v0.md`
- Example exploration result: `docs/reports/phase1_scenario_run_01_v0.md`
- Weak points: automated excerpt extraction은 skeleton 수준이다.
- Entry condition for next stage: evidence와 Codex 판단을 분리 비교할 수 있다.
