# operating ui live control bar v1

## 1. verdict

- 구현 완료
- `operating-ui-live` 위에 selected asset을 query param 기반으로 전환할 수 있는 minimal live control bar를 추가했다.

## 2. asset source reading

- selectable asset source
  - live composition의 `available_assets`
  - 이 값은 [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py) 안에서 adapter 결과의 `boardItems`로부터 만든다.

- source chain
  - runtime process-console payload
  - [build_process_console_view_data](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
  - [operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
  - `boardItems`
  - `available_assets`

- 이유
  - 새 asset source를 만들 필요가 없다.
  - current live composition이 실제로 렌더하는 board와 같은 source를 써야 selection control과 board가 일치한다.

## 3. created/updated files

- 수정
  - [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

- 생성
  - [operating_ui_live_control_bar_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_control_bar_v1.md)

## 4. control bar coverage

- current selection 표시
  - `selected_asset_id`

- selector/link list
  - `available_assets[]` 기반 link list
  - `/operating-ui-live?asset_id=<id>`

- live meta
  - `mode=live`
  - `source_kind`
  - `selection_query_state`
  - current selected

- 범위 제한
  - modal 없음
  - inline edit 없음
  - feedback 없음
  - search/filter 없음
  - GET query 기반 전환만 지원

## 5. query behavior

### valid `asset_id`

- 해당 asset 기준으로 strip/board/activity 갱신
- `selection_query_state = valid_asset_id`

### invalid `asset_id`

- 기본 selected asset으로 fallback
- `selection_query_state = invalid_selected_asset_query`
- live render는 유지

### no `asset_id`

- process-console builder 기본 selected asset 사용
- `selection_query_state = default_selected`

### empty assets

- `available_assets = []`
- control bar는 `no assets available`
- `selection_query_state = empty_assets`

## 6. api/live route impact

- HTML route
  - `/operating-ui-live`
  - `/operating-ui-live?asset_id=...`

- JSON route
  - `/api/operating-ui-live`
  - `/api/operating-ui-live?asset_id=...`

- 추가된 live JSON 필드
  - `requested_asset_id`
  - `selected_asset_id`
  - `available_assets`
  - `selection_query_state`
  - `live_availability`

## 7. run/check result

### selection behavior check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data
runtime_root = Path('runtime').resolve()
for asset_id in [None, 'turboquant_youtube', 'missing_asset']:
    data = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    print({
        'requested': asset_id,
        'state': data.get('state'),
        'selection_query_state': data.get('selection_query_state'),
        'selected_asset_id': data.get('selected_asset_id'),
        'available_assets_count': len(data.get('available_assets', [])),
    })
PY
```

### result

- no `asset_id`
  - `default_selected`
- valid `asset_id=turboquant_youtube`
  - `valid_asset_id`
- invalid `asset_id=missing_asset`
  - `invalid_selected_asset_query`
  - fallback selected asset 유지

### render check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data, render_operating_ui_live_composition_html
runtime_root = Path('runtime').resolve()
data = build_operating_ui_live_composition_data(runtime_root, asset_id='turboquant_youtube')
html = render_operating_ui_live_composition_html(data, api_path='/api/operating-ui-live?asset_id=turboquant_youtube')
print('Live Control Bar' in html, 'mode=live' in html, '/operating-ui-live?asset_id=' in html)
PY
```

### result

- control bar title 존재
- live meta 존재
- asset switch links 존재

## 8. limitations

- selector는 link list 기반이다. dropdown/select UI는 아직 없다.
- asset list가 많아지면 지금 방식은 길어질 수 있다.
- persistent preference나 recent selection 기억은 없다.
- board 클릭과 live route selection은 아직 연결되지 않았다.

## 9. recommended next step

- 다음 구현 슬라이스는 **board card click -> asset_id query route 연결**이다.
- 이유:
  - 현재 control bar로는 전환 가능하지만, 실제 운용 흐름처럼 board에서 대상을 눌러 읽는 경험까지 열려면 link wiring이 필요하다.
