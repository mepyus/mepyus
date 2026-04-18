# Input Organ HANDOFF.md Draft v0

## accepted inputs

- raw source material
- normalized source material
- source locator or source ref
- provisional context hints
- weak/ambiguous ingest signals

## required packet fields

- `source_ref`
- `source_kind`
- `matched_context_layers`
- `provenance/origin`
- `intake_classification`
- `split_units or intake_blocks`
- `weakness_note`
- `fallback_used`
- `next_lane_hint`

## common triggers

- new external material arrived
- runtime surface snapshot entered
- operator note or mixed material attached
- re-read requested on previously weak intake

## continuity / carry

- preserve same source family if already known
- preserve prior weakness/fallback if unresolved
- keep provenance chain intact across retries

## handoff target

주 대상:

- `translation organ`

보조 대상:

- `line/state organ`
- `governance organ` when intake is blocked or highly weak

## handoff rule

Input organ은 후속 기관에 깔끔한 입력만 넘기지 않는다.  
약함, fallback, provenance까지 같이 넘겨야 한다.

## final sentence

Input organ handoff는 source/context/provenance와 weakness/fallback를 잃지 않은 intake packet을 다음 기관에 넘기는 준비 handoff여야 한다.
