# workbench compare mixed vs canonical stage1.5

## 1. one-line verdict
- canonical closes source -> translation -> bridge more cleanly, while mixed keeps a source-local / translation gap and depends more on derived join readout.

## 2. comparison
- source
  - mixed: `left_source_local_ref=missing`, `right_source_local_ref=persisted`
  - canonical: `left_source_local_ref=persisted`, `right_source_local_ref=persisted`
- translation
  - mixed: `left_translated_handles=missing`, `right_translated_handles=persisted`
  - canonical: `left_translated_handles=persisted`, `right_translated_handles=persisted`
- join
  - mixed: `bridge_trace_ref=missing`, `review_focus="cross_path_corroboration"`
  - canonical: `bridge_trace_ref=persisted`, `review_focus=""`
- block
  - mixed: `"live_side_family_present_but_not_canonicalized"`
  - canonical: `""`
- bridge/local_space
  - mixed: `"mixed_pair_explicit_bridge_missing"`
  - canonical: `"pair_bridge_present"`
- derived dependence
  - mixed: best-local and blocker-led
  - canonical: persisted bridge-led
- reading mode
  - mixed: `confirmed_hold`
  - canonical: `stable_reading`

## 3. conclusion
- current workbench is sufficient to expose the structural difference between mixed and canonical: `YES`
