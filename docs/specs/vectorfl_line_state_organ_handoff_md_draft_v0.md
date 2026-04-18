# Line State Organ HANDOFF.md Draft v0

## accepted inputs

- intake packet
- source/context carry
- current surface excerpt
- existing line/state refs
- trace/residue hints

## required packet fields

- `case_ref`
- `current_lane_ref`
- `relevant_input_refs`
- `existing_line_refs if any`
- `trace_carry_refs`
- `question_or_trigger`
- `expected_return_type=line_seed_proposal`

## common triggers

- new material may form a line
- existing line may thicken or be reused
- current reading lacks line/state anchor
- residue suggests recurrence but not closure

## continuity / carry

- preserve previous line refs when reuse is plausible
- keep candidate-only status when evidence is weak
- keep trace linkage to support later reread

## handoff target

주 대상:

- `translation organ`

보조 대상:

- `trace/memory organ`
- `current-reading return surface` for candidate-only visibility

## handoff rule

Line/state organ은 final line set만 넘기지 않는다.  
candidate / thickening / reuse / carry 구분을 같이 넘겨야 한다.

## final sentence

Line/state organ handoff는 line seed proposal과 thickening/reuse/carry 판단을 evidence와 함께 넘겨, 다음 기관이 그것을 grammar나 trace 쪽으로 이어받게 하는 formation-aware handoff여야 한다.
