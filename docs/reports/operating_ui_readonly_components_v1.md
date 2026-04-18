# operating ui readonly components v1

## 1. verdict

- 구현 완료
- 검증된 `OperatingUiPayloadAdapter` 위에 첫 read-only view 조각 2개가 안전하게 붙었다.
- raw process-console payload를 직접 참조하지 않고, adapter model만 입력으로 받는 경계가 유지된다.

## 2. created files

- [asset_state_card.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/asset_state_card.py)
- [derived_state_strip.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/derived_state_strip.py)
- [run_readonly_component_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_readonly_component_demo.py)

## 3. component coverage

### `AssetStateCard`

- 입력 props 요약
  - `item`
  - `selected`
  - `showCompareReason`
  - `showAttentionHint`
  - `onClick`
  - `onOpenDetail`

- 소비하는 adapter field
  - `id`
  - `title`
  - `packetTextureLabel`
  - `maturationLabel`
  - `traceabilityLabel`
  - `emergenceLabel`
  - `updatedAt`

- 구현 역할
  - 개별 asset의 packet/maturation/traceability/emergence 요약
  - selected 강조
  - helper text 표시
  - click/detail CTA 가능 여부 표시

### `DerivedStateStrip`

- 입력 props 요약
  - `selectedAsset`
  - `latestPreview`
  - `diffSummary`
  - `attentionSummary`
  - `memorySummary`
  - `compareHref`
  - `onOpenDiff`
  - `onOpenAttention`
  - `onOpenMemory`

- 소비하는 adapter field
  - `selectedAsset.title`
  - `selectedAsset.canonicalStateRows`
  - `latestPreview`
  - `diffSummary`
  - `attentionSummary`
  - `memorySummary`

- 구현 역할
  - selected asset 기준 latest/diff/attention/memory 요약
  - fallback state code를 read-first helper line으로 표현
  - diff/attention/memory CTA 활성 가능 여부 계산

## 4. adapter dependency check

- raw payload 직접 참조 여부
  - 없음
- adapter model 사용 범위
  - `run_readonly_component_demo.py`에서 raw fixture -> adapter -> readonly component 순서로만 연결
  - component 파일 내부에서는 raw payload field name을 전혀 사용하지 않음

## 5. fallback behavior check

### `no_previous_state`

- `DerivedStateStrip`
  - `compare to previous unavailable`
  - diff CTA 비활성

### `no_active_attention`

- `DerivedStateStrip`
  - `no active attention`
  - attention CTA 비활성

### `insufficient_attention_history`

- `DerivedStateStrip`
  - `insufficient attention history`
  - memory CTA 비활성

### `state_unavailable`

- `DerivedStateStrip`
  - `no canonical state yet`
  - 모든 CTA 비활성

### `no_selected_asset`

- `DerivedStateStrip`
  - state=`no_selected_asset`
- `AssetStateCard`
  - empty card state로 처리

## 6. demo/check result

### command

```bash
python3 app/work/operating_ui/run_readonly_component_demo.py
python3 -m py_compile app/work/operating_ui/components/asset_state_card.py app/work/operating_ui/components/derived_state_strip.py app/work/operating_ui/run_readonly_component_demo.py
```

### result summary

- case A
  - card 정상 요약
  - strip 정상 latest/diff/attention/memory 요약

- case B
  - strip이 `no_previous_state`를 neutral helper로 처리

- case C
  - strip이 `no_active_attention` + `insufficient_attention_history`를 분리 처리

- case D
  - card는 empty state
  - strip은 `no_selected_asset`

## 7. limitations

- 이 단계는 실제 React 컴포넌트가 아니라 Python work-level readonly renderer다.
- `AssetStateCard` v1은 grounding을 직접 surface하지 못한다.
  - 이유:
    - current adapter `boardItems` model에 grounding field가 없다.
  - 현재는 helper text로 `grounding not surfaced in board card v1`를 남긴다.
- click/detail CTA는 callback 존재 여부만 계산하고 동작은 수행하지 않는다.
- style system은 아직 없다.
- modal, board shell, activity panel full render는 아직 구현하지 않았다.

## 8. recommended next step

- 다음 구현 슬라이스는 `AssetStateBoard`의 read-only 최소 구현이다.
- 이유:
  - `AssetStateCard`가 안정됐으므로, 이제 grid/list 반복 렌더와 selection highlight를 붙이면 board main surface의 첫 실제 조각이 생긴다.
