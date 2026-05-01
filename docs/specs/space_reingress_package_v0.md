# Space Reingress Package v0

## Purpose

작업 결과와 과정 흔적을 다시 공간에 넣는 형식을 고정한다.

## Execution

Reingress minimum fields:

- `original_user_request`
- `interpreted_goal`
- `searched_assets_summary`
- `space_position_summary`
- `codex_position_summary`
- `chosen_mode`
- `final_return_summary`
- `unresolved_notes`
- `new_line_or_axis_candidate`
- `future_probe_note`

Reingress destinations:

- contract/template: `runtime/contracts/space_reingress_record_v0.json`
- concrete records: `runtime/reingress_records/`
- human-readable validation report: `docs/reports/`

## Interpretation

과정 흔적은 공간 숙성의 핵심 재료다. 특히 difference와 unresolved는 단순 미완료가 아니라 다음 질문이 더 나은 위치에서 시작하게 하는 pointer다.

재유입 패키지는 메모장이 아니라 운영 흔적이다. 따라서 원질문, 해석 목표, 근거 요약, 공간 위치, Codex 위치, 선택된 mode가 함께 있어야 한다.

## Validation

- 다음 질문에서 재사용 가능한 최소 context가 남는다.
- 결과뿐 아니라 이유와 차이도 남는다.
- future probe가 남아 Phase 2 후보로 이어질 수 있다.

## Stage 5 Closeout

- Verdict: `PASS`
- Files created: `docs/specs/space_return_package_v0.md`, `docs/specs/space_reingress_package_v0.md`, `runtime/contracts/space_reingress_record_v0.json`, `docs/guides/reingress_minimum_fields_v0.md`
- Example return package: Stage 6 scenario reports
- Example reingress package: Stage 6 scenario reports
- Entry condition for next stage: three scenarios can run through interpretation -> exploration -> merge/diff/hold -> return -> reingress.
