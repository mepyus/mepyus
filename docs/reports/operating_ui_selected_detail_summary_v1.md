# operating ui selected detail summary v1

## 1. verdict

- 구현 완료
- `selected asset` 기준의 read-only detail summary panel v1을 추가했고, live composition 안에서 board 옆에서 함께 갱신되도록 연결했다.

## 2. created/updated files

- 생성
  - [selected_asset_detail_summary.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/selected_asset_detail_summary.py)
  - [run_selected_detail_summary_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_selected_detail_summary_demo.py)
  - [operating_ui_selected_detail_summary_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_selected_detail_summary_v1.md)

- 수정
  - [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

## 3. panel coverage

- 보여주는 정보
  - selected asset title / subtitle
  - canonical state summary rows
  - latest summary
  - diff summary
  - attention summary
  - memory summary
  - compare candidate 요약
  - updated meta / helper text

- 의도적으로 제외한 것
  - full detail explorer
  - evidence drilldown
  - write/action UI
  - modal 수준의 확장 정보

## 4. adapter dependency check

- 사용하는 adapter model 필드
  - `selectedAsset.title`
  - `selectedAsset.subtitle`
  - `selectedAsset.updatedAt`
  - `selectedAsset.canonicalStateRows`
  - `selectedAsset.scopeLabel`
  - `selectedAsset.stateNotes`
  - `derivedStrip.latestPreview`
  - `derivedStrip.diffSummary`
  - `derivedStrip.attentionSummary`
  - `derivedStrip.memorySummary`
  - `compareCandidates`
  - `guards.stateUnavailable`

- raw payload 직접 참조 여부
  - 없음

## 5. fallback behavior check

- `no_selected_asset`
  - panel state=`no_selected_asset`
  - helper: `select an asset to open detail`

- `state_unavailable`
  - panel state=`state_unavailable`
  - helper: `no canonical state yet`

- `no_previous_state`
  - diff summary: `compare to previous unavailable`

- `no_active_attention`
  - attention summary: `no active attention`

- `insufficient_attention_history`
  - memory summary: `insufficient attention history`

- 일부 필드 없음
  - 누락 필드는 생략 또는 neutral 처리
  - panel 전체는 유지

## 6. boundary check

- board/card 역할 침범 여부
  - 없음
  - board는 목록/선택 강조만 맡고, summary panel은 selected asset 한 개의 richer summary만 담당

- modal 역할 침범 여부
  - 없음
  - evidence drilldown, full compare explorer, action section을 넣지 않았다

## 7. live composition behavior

- 배치 방식
  - 상단: `DerivedStateStrip`
  - 본문 좌측: `AssetStateBoard`
  - 본문 우측 상단: `Selected Detail Summary`
  - 본문 우측 하단: `Activity Panel`

- selected asset 전환 시 함께 갱신되는지
  - 됨
  - `asset_id` query 전환 후 `strip / board / detail summary / activity`가 같은 selected asset 기준으로 함께 갱신된다

## 8. run/check result

### detail summary demo

```bash
python3 app/work/operating_ui/run_selected_detail_summary_demo.py
python3 -m py_compile app/work/operating_ui/components/selected_asset_detail_summary.py app/work/operating_ui/run_selected_detail_summary_demo.py app/runtime/operating_ui_live.py
```

### 확인된 상태

- `normal_selected`
  - full summary loaded

- `no_previous_state`
  - diff helper 정상

- `insufficient_attention_history`
  - memory helper 정상

- `state_unavailable`
  - neutral fallback 정상

- `no_selected_asset`
  - empty helper 정상

### live composition check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data
runtime_root = Path('runtime').resolve()
for asset_id in ['turboquant_youtube','choi_ai_classroom_cnn', None]:
    data = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    print(asset_id, data['detail_summary']['state'], data['selected_asset_id'], data['detail_summary'].get('title'))
PY
```

### 결과

- `turboquant_youtube`
  - `loaded / turboquant_youtube`
- `choi_ai_classroom_cnn`
  - `loaded / choi_ai_classroom_cnn`
- default selection
  - current default selected asset 기준 `loaded`

## 9. limitations

- 현재 panel은 text-forward SSR summary다.
- compare candidate는 top 3 summary까지만 노출한다.
- canonical rows는 최대 6개만 요약한다.
- selected asset이 없는 실제 live path는 현재 board가 비지 않는 한 드물어서, `no_selected_asset`는 demo로만 별도 확인했다.

## 10. recommended next step

- 다음 구현 슬라이스는 **read-only composition 전체를 더 명확한 3영역 operating shell로 정리하는 lightweight layout refinement**다.
- 이유:
  - 개별 조각은 충분히 생겼고, 다음에는 이 조각들이 실제 운용화면처럼 더 읽기 쉽게 배치되는지 확인해야 한다.
