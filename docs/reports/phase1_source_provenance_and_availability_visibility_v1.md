# phase1 source provenance and availability visibility v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1_adapter.py)
- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [run_phase1_interaction_invariant_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_phase1_interaction_invariant_probe.py)
- [phase1_source_provenance_and_availability_visibility_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_source_provenance_and_availability_visibility_v1.md)

## 1. provenance / availability distinctions now exposed

The UI now exposes thin provenance and availability distinctions for:

- live runtime source
- fallback scaffold support
- stored phase1 path data
- degraded / unavailable source

The surface language stays phase1-native rather than dumping raw source paths or field names.

## 2. where the visibility was added

### Operating

- `Current Run`
  - provenance pill for `live runtime observation` or degraded observation
  - availability pill for `live` or `degraded`
- `Recent Activity`
  - availability pill for `live` or `degraded`
- `Path / Saved Path Hint`
  - still phase1-semantic, not raw source-centric

### Explore

- object section now shows:
  - provenance summary such as `live runtime options + scaffold support`
  - availability pill `live` or `fallback`
- preset area remains scaffold-only and is not reframed as source of truth

### Search

- search input panel now shows:
  - provenance summary such as `runtime options + stored saved paths`
  - availability pill `live` or `degraded`
- result cards now include a thin provenance pill:
  - `live` for runtime options
  - `stored` for saved-path and seed-related results

### Memory / Similar

- Memory now shows `stored saved paths`
- Similar now shows `stored seed context + local re-query`
- both keep ownership semantics intact while making stored provenance visible

## 3. how raw source naming was kept from colliding with phase1 semantics

The UI does not expose raw keys like:

- `available_assets`
- `debug_text.activity`
- `phase1_memory_stickers.jsonl`

Instead it uses phase1-facing summaries such as:

- `live runtime observation`
- `runtime options + scaffold support`
- `stored saved paths`
- `stored seed context + local re-query`

This preserves phase1 semantics first and provenance second.

## 4. internal source detail still intentionally hidden

Still hidden:

- raw source-map dump
- exact adapter source key inventory in the UI
- internal runtime path details for each section

Reason:

- phase1 needs source transparency, not a debugging console
- too much raw provenance detail would drown the semantic surface roles

## 5. probe update

The invariant probe now also checks provenance wording/mode mapping:

- loaded mode exposes live operating provenance summary
- loaded mode exposes runtime option provenance summary
- memory provenance summary uses stored wording
- unavailable mode exposes degraded operating provenance wording
- unavailable mode keeps fallback explore provenance wording

## 6. remaining watchpoints

- provenance pills are intentionally thin, so future wording changes could still weaken the distinction without breaking structure
- `stored` is now visible in Search cards; this helps, but it should not drift into a heavier records-management feel
- Similar provenance is still summary-level only; if future runtime assist grows, the wording will need another audit

## 7. next candidates

- run one short manual walkthrough in `live_ready` and `live_unavailable` modes to confirm the new provenance notes read naturally
- keep provenance wording aligned with the interaction invariant probe whenever adapter summaries change
