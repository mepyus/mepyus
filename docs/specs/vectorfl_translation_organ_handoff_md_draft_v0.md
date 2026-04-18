# Translation Organ HANDOFF.md Draft v0

## accepted inputs

- intake packet
- current surface excerpt
- source/context carry
- weakness/fallback carry
- optional trace/residue refs

## required packet fields

- `case_ref`
- `current_lane_ref`
- `current_surface_excerpt` or intake summary
- `relevant_input_refs`
- `weakness_note`
- `question_or_trigger`
- `expected_return_type=translation_summary`

## common triggers

- intake classified as `translation_first`
- current reading too raw for direct flow interpretation
- mixed material needs operating grammar shift
- presentation-like wording appears too early

## continuity / carry

- preserve prior grammar if still valid
- preserve unresolved edge when translation remains weak
- keep source evidence refs attached

## handoff target

주 대상:

- `flow interpretation organ`

보조 대상:

- `governance organ` when direct closure risk is already obvious

## handoff rule

Translation organ은 멋진 요약만 넘기지 않는다.  
어떤 grammar로 읽어야 하는지, 무엇이 아직 unresolved인지 같이 넘겨야 한다.

## final sentence

Translation organ handoff는 translated summary, lane hint, evidence refs, unresolved carry를 다음 기관이 바로 흐름 판독에 쓸 수 있게 넘기는 grammar-aware handoff여야 한다.
