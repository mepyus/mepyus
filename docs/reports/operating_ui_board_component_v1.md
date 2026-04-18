# operating ui board component v1

## 1. verdict

- 구현 완료
- `AssetStateBoard`는 adapter model의 `boardItems`만 받아 반복 렌더, selection highlight, empty state를 처리하는 read-only board 최소 구현으로 고정됐다.

## 2. created files

- [asset_state_board.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/asset_state_board.py)
- [run_board_component_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_board_component_demo.py)

## 3. component coverage

- 역할
  - `boardItems` 반복 렌더
  - `selectedAssetId` 기준 선택 강조 전달
  - `emptyLabel`, `sortLabel`, `filterSummary`를 얇은 board metadata로 유지

- props 요약
  - `items`
  - `selectedAssetId`
  - `emptyLabel`
  - `sortLabel`
  - `filterSummary`
  - `onSelectAsset`

- `AssetStateCard` 연결 방식
  - board가 각 `item`을 `build_asset_state_card_view(...)`에 넘긴다
  - selected 여부만 board가 계산하고, 카드 자체는 read-only summary 역할만 유지한다

## 4. selection behavior check

- selected
  - `selectedAssetId`가 valid면 해당 카드만 `selected=True`

- invalid selected
  - `selectedAssetId`가 board items에 없으면 전부 unselected
  - board `selectionState = invalid_selected_asset`

- empty board
  - `items=[]`면 board `state=empty`
  - selection helper 대신 empty message만 노출

- none selected
  - `selectedAssetId=None`이면 전부 unselected
  - board `selectionState = none_selected`

## 5. adapter dependency check

- raw payload 직접 참조 여부
  - 없음

- adapter model 사용 범위
  - `boardItems[*].id`
  - `boardItems[*].title`
  - `boardItems[*].packetTextureLabel`
  - `boardItems[*].maturationLabel`
  - `boardItems[*].traceabilityLabel`
  - `boardItems[*].emergenceLabel`
  - `boardItems[*].updatedAt`

## 6. grounding decision

- A안: v1 board/card는 grounding 생략 유지

### 이유

- 현재 adapter `boardItems` 모델은 board main surface를 가볍게 유지하기 위해 최소 summary만 담고 있다.
- grounding은 strip/detail에서 더 안전하게 읽히는 정보고, board card에 억지로 올리려면 adapter와 fixture를 다시 확장해야 한다.
- 이번 턴 목적은 board 반복 렌더 경계를 세우는 것이므로, grounding은 v1 board/card에서 생략 유지가 더 보수적이다.

## 7. demo/check result

### command

```bash
python3 app/work/operating_ui/run_board_component_demo.py
python3 -m py_compile app/work/operating_ui/components/asset_state_board.py app/work/operating_ui/run_board_component_demo.py
```

### 확인 포인트

- normal selected
  - 선택 카드 1개 강조

- invalid selected
  - 전부 unselected
  - `selectionState=invalid_selected_asset`

- none selected
  - 전부 unselected
  - `selectionState=none_selected`

- empty board
  - `state=empty`
  - `no assets available`

## 8. limitations

- 아직 실제 grid/layout/style system은 없다.
- `sortLabel`, `filterSummary`는 요약 텍스트만 지원하고 동작은 하지 않는다.
- card CTA는 callback 존재 여부만 반영한다.
- grounding은 board layer에 아직 표면화하지 않는다.

## 9. recommended next step

- 다음 구현 슬라이스는 `ActivityPanel`의 read-only 최소 구현이다.
- 이유:
  - board main surface가 생겼으니, 이제 selected asset modal 없이도 history/activity 읽힘 조각을 병렬로 붙일 수 있다.
