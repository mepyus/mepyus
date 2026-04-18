# Flow Interpretation Organ HANDOFF.md Draft v0

## accepted inputs

- translation summary
- lane hint update
- governance carry
- trace/residue/reentry carry
- current-reading question

## required packet fields

- `case_ref`
- `current_lane_ref`
- `flow_reading_input_summary`
- `governance_state`
- `trace_carry_refs`
- `question_or_trigger`
- `expected_return_type=flow_reading_summary`

## common triggers

- next hop remains ambiguous
- direct readout and explanation-first conflict
- unresolved edge still active
- reentry hint suggests reread before closure

## continuity / carry

- preserve next hop as candidate if not firm
- preserve unresolved edge note
- preserve reentry cue when flow depends on future trigger

## handoff target

주 대상:

- `governance organ`

보조 대상:

- `current-reading return surface`
- `translation organ` when reread requires grammar revision

## handoff rule

Flow interpretation organ은 단순 다음 단계 이름만 넘기지 않는다.  
왜 그쪽으로 읽히는지와 무엇이 아직 닫히지 않았는지 같이 넘겨야 한다.

## final sentence

Flow interpretation organ handoff는 next hop candidates, unresolved edge, reentry cue, caution carry를 governance와 current-reading이 바로 이어받을 수 있게 넘기는 progression-aware handoff여야 한다.
