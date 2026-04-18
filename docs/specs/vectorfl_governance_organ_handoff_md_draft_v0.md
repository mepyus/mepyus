# Governance Organ HANDOFF.md Draft v0

## accepted inputs

- flow reading summary
- next hop candidates
- current-reading surface
- trace/residue/reentry carry
- existing governance state

## required packet fields

- `case_ref`
- `current_lane_ref`
- `governance_state or hold_candidate`
- `flow_summary`
- `trace_carry_refs`
- `expected_return_type=governance_caution`

## common triggers

- direct presentation risk detected
- observer-only or promotion-forbidden needs carry
- release condition still absent
- next check trigger must be surfaced

## continuity / carry

- preserve active restriction flags unless explicit release condition is met
- preserve release condition history when still pending
- preserve trace-linked caution when unresolved edge remains

## handoff target

주 대상:

- `current-reading return surface`

보조 대상:

- `history / trace surface`
- `programs / connections surface` when restriction affects external action request

## handoff rule

Governance organ은 yes/no 승인만 넘기지 않는다.  
hold, restriction, release condition, next check trigger를 current-reading과 trace에 같이 남겨야 한다.

## final sentence

Governance organ handoff는 restriction set과 release/next-check 정보를 current-reading, trace, external connection boundary가 함께 읽을 수 있게 넘기는 protection-aware handoff여야 한다.
