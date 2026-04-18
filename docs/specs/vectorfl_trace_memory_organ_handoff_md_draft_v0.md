# Trace Memory Organ HANDOFF.md Draft v0

## accepted inputs

- recent return summaries
- residue notes
- reentry hints
- governance fragments
- current case/lane refs

## required packet fields

- `case_ref`
- `current_lane_ref`
- `summary_return_refs`
- `governance_refs if any`
- `trace_candidate_refs`
- `expected_return_type=trace_return`

## common triggers

- bounded organ run completed
- unresolved edge should be preserved
- next reread trigger emerged
- governance produced a caution worth carrying

## continuity / carry

- preserve trace ordering
- preserve reentry hint linkage to case/lane
- keep prior residue visible when not superseded

## handoff target

주 대상:

- `history / trace surface`

보조 대상:

- `flow interpretation organ`
- `governance organ`
- `current-reading return surface`

## handoff rule

Trace/memory organ은 과거를 저장만 하지 않는다.  
다음 기관이 다시 읽을 수 있는 residue/reentry 단서를 같이 넘겨야 한다.

## final sentence

Trace/memory organ handoff는 append-only trace, residue, reentry, decision anchor를 history 면과 다음 reread 기관이 함께 읽을 수 있게 넘기는 continuity-aware handoff여야 한다.
