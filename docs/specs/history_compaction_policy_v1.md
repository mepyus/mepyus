[[A]] [[OBJ:history_compaction_policy_v1]] [[SEM:derived_compaction_policy_for_recent_full_lineage_and_older_summary]]

# history_compaction_policy_v1

## 1. purpose

- 이번 policy의 목적은 append-only raw history를 보존한 채, process console 표면에서는 recent full lineage와 older compacted summary를 함께 읽게 하는 것이다.

## 2. core rules

- raw history preserve
  - jsonl 원장은 삭제하지 않는다
- compacted view is derived
  - compacted node는 파생 read model이다
- recent full lineage
  - 현재 thin validation window는 recent `3`개 full record를 유지한다
- older summary
  - 그 이전 older history는 summary/anchor node로 읽는다

## 3. compaction targets

- 연속 provenance_only 구간
- same trigger family older run
- canonical change 없는 older segment

## 4. absolute no-compaction anchors

- first record
- latest previous record
- manual correction record
- packet texture shift record
- grounding / traceability shift record
- blocker shift record

## 5. summary node shape

- `asset_id`
- `summary_type`
- `covered_range_start`
- `covered_range_end`
- `covered_record_count`
- `trigger_types_included`
- `canonical_change_count`
- `provenance_only_count`
- `notable_shift_types`
- `representative_reasons`
- `representative_evidence_refs_count`

## 6. UI reading rule

- recent timeline:
  - full record
- older history:
  - compacted summary node
  - anchor node
- raw lineage 접근은 계속 가능해야 한다

## 7. one-line lock

> `history_compaction_policy_v1`는 raw history를 지우지 않은 채 recent full lineage를 우선 유지하고, older provenance-heavy 구간만 summary/anchor node로 얇게 만드는 derived surface policy다.
