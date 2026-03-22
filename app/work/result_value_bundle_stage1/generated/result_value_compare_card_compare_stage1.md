# result-value compare card compare stage1

## 1. one-line comparison
- canonical은 persisted closure 중심이고, mixed는 closure gap + derived support 중심이다.

## 2. four-way compare
- source
  - mixed: `source_local_ref left=missing`
  - canonical: `source_local_ref left=persisted`
- translation
  - mixed: `translated_handles left=missing`, `translation_join=right_present_left_missing`
  - canonical: `translated_handles left=persisted`, `translation_join=symmetric_or_unknown`
- join
  - mixed: `bridge=missing`, `closure=mixed_pair_explicit_bridge_missing`
  - canonical: `bridge=persisted`, `closure=pair_bridge_present`
- block
  - mixed: `source-side live material lacks source_local/translated layer and the current pair has no exact persisted bridge closure`
  - canonical: `canonical pair already closes through persisted bridge/local-space exposure`

## 3. conclusion
- compare card가 workbench 보조면으로 충분한가: `YES`
- 점/리본보다 먼저 card가 맞는가: `YES`
