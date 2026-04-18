# phase2 history to phase1 reread handoff contract v1

## package status

complete for this turn

## files changed

- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- [run_phase1_interaction_invariant_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_phase1_interaction_invariant_probe.py)
- [phase2_history_to_phase1_reread_handoff_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase2_history_to_phase1_reread_handoff_contract_v1.md)

## 1. meaning lock

The handoff is now locked as:

- `open in phase1 with reread context`

Meaning:

- historical reread reference is attached
- current phase1 opens in current mode
- no saved path is created
- no memory selection is created
- no active seed is activated
- current path authoring ownership remains in phase1

## 2. payload boundary

History now passes only thin contextual reference fields:

- `asset_id`
- `history_snapshot_ref`
- `history_cluster_ref`
- `history_reread_summary`
- `history_source_note`

Still forbidden:

- `selected_memory_sticker_id` auto-set
- `similar_seed_ref` auto-set
- current path auto-filled
- phase1 authoring overwrite

## 3. phase1 visibility

Phase1 now reads history-origin context as a separate historical reread reference:

- Operating:
  - `historical reread context=...`
  - `historical reference only / not saved path / not active seed`
- Explore Preview:
  - `opened from history / reread context attached`
  - helper text clarifies it is not saved path, memory, seed, or authoring replacement
- Memory:
  - thin note that historical reread context remains separate from Memory

## 4. detach / clear scope

Phase1 now has:

- `clear history context`

This removes only the imported historical reread reference.

It does not change:

- current path
- saved path selection
- active seed

## 5. history-side wording

History-side wording was also tightened:

- `open in phase1 with reread context`

Avoided:

- replay in phase1
- rerun in phase1
- restore state in phase1
- load this state into phase1

## 6. probe update

The probe now additionally checks:

- history open attaches reread context
- history open does not set saved path
- history open does not activate seed
- history open does not overwrite blank authoring object
- history open keeps path ownership unchanged
- clear history context detaches only the reread reference

## 7. remaining watchpoints

- current history handoff passes snapshot/cluster summary but not a fuller trace-reference phrase yet
- wording still needs occasional manual walkthrough to ensure `reread context` does not drift toward `restore state`
- if future history surface gains richer trace selection, the payload boundary must stay thin

## 8. next candidates

- add one short manual walkthrough report for history-origin phase1 reading to confirm the new wording reads naturally
- if needed later, add a dedicated history-context badge style without strengthening it into a major banner
