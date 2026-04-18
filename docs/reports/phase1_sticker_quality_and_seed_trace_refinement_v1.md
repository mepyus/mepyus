# phase1 sticker quality and seed trace refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- [phase1_sticker_quality_and_seed_trace_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_sticker_quality_and_seed_trace_refinement_v1.md)

## 1. record shape change

The thin sticker record is now authored with:

- `why_selected_short`
- `why_mode`
- `optional_note`

The persisted record still keeps `why_selected` as a compatibility string, but phase1 UI now treats the structured fields as the primary readable memory unit.

The active `why_mode` set stays deliberately small:

- `relation_found`
- `perspective_shift`
- `resonance`
- `keep_for_later`
- `unclear_but_hold`

This keeps sticker quality guided without promoting a large taxonomy or schema.

## 2. backward compatibility

Existing JSONL records are still readable.

- If a legacy row already has `why_mode`, it is reused with safe normalization.
- If `why_selected_short` is missing, the loader falls back to legacy `why_selected`.
- If `optional_note` is missing but legacy `why_selected` contains a split form like `short / note`, the loader extracts the tail as `optional_note`.
- Missing fields safely fall back to `keep_for_later` and a default short reason.

No migration was added. The append-only path remains:

- `runtime/manifests/operating_ui_phase1/phase1_memory_stickers.jsonl`

## 3. Memory card readability

Memory cards were kept compact, but now read more like memory units than raw save logs.

Each card shows:

- object
- lens
- position
- preview summary
- `why_selected_short`
- `why_mode`
- `created_at`

Thin badges are also preserved:

- `selected`
- `active seed`
- `recent`

The selected Memory preview also surfaces the optional note separately instead of collapsing everything into one free string.

## 4. Similar seed trace visibility

Similar cards now foreground why each result touches the current seed.

Each result exposes:

- `matched_on`
- `trace_summary`
- `confidence_style`

UI-wise this appears as:

- small contact badges such as `same lens`, `same position`, `shared preview term`
- a one-line trace sentence
- restrained confidence language such as `thin-match`, `partial-overlap`, `low-confidence`

This was kept trace-first rather than score-first. No opaque numeric score was introduced.

## 5. how the loop is now easier to trust

The loop remains:

1. Explore selects an explicit interpretation path.
2. Sticker authoring now uses thin structured guidance instead of a fully loose reason string.
3. Memory displays the saved path as a compact readable card.
4. Similar shows why the seed touched a result instead of only showing a vague resonance result.

That improves trust without inflating the system into recommendation semantics.

## 6. weak / heuristic parts

The Similar derivation is still intentionally weak.

- `matched_on` is based on thin local heuristics around lens, position, object token, and preview terms.
- Confidence is a restrained presentation style, not a scientific similarity score.
- `why_mode` is intentionally small and should not be overread as ontology or workflow semantics.

## 7. next candidates

- tighten Similar derivation examples with slightly better seed-contact phrasing while staying local and non-recommendation
- add a thinner inline affordance for selecting `why_mode` defaults based on current preview context without expanding taxonomy
