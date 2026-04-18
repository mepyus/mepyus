# operating ui live composition path v1

## 1. verdict

- 구현 완료
- fixture 기반 demo를 보존한 채, 실제 runtime process-console payload를 직접 읽는 read-only live composition path를 추가했다.

## 2. runtime source reading

- runtime selected asset payload source
  - [build_process_console_view_data](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)

- 확보되는 데이터
  - `header`
  - `asset_rail`
  - `state_panel`
  - `latest_state_preview`
  - `attention_queue`
  - `history_drilldown`
  - `compare_entry`
  - `summary`

- viewer_server가 현재 process console 데이터를 읽는 방식
  - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py) 에서
  - `/process-console` -> `build_process_console_view_data(...)` -> `render_process_console_view_html(...)`

- 이번 live composition에 재사용한 existing build path
  - 새 payload builder를 만들지 않고, 기존 `build_process_console_view_data(...)`를 그대로 재사용했다.

## 3. created/updated files

- 생성
  - [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
  - [operating_ui_live_composition_path_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_composition_path_v1.md)

- 수정
  - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

## 4. live route coverage

- HTML route
  - `/operating-ui-live`
  - `/operating-ui-live?asset_id=turboquant_youtube`

- JSON route
  - `/api/operating-ui-live`
  - `/api/operating-ui-live?asset_id=turboquant_youtube`

- 범위
  - strip / board / activity read-only composition
  - fixture demo와 별도 경로 유지

## 5. data flow check

- 흐름
  - runtime process-console payload source
  - [build_process_console_view_data](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
  - [operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
  - adapted ui model
  - readonly components
    - [derived_state_strip.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/derived_state_strip.py)
    - [asset_state_board.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/asset_state_board.py)
    - [activity_panel.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/activity_panel.py)
  - viewer render

- 핵심 확인
  - UI component는 runtime raw payload를 직접 읽지 않는다.
  - runtime raw는 live build helper와 adapter까지만 도달한다.

## 6. fallback behavior

- `live_unavailable`
  - process-console builder 예외 시 전체 fallback payload 반환

- `no_selected_asset`
  - adapter 결과에 따라 strip neutral fallback
  - board는 independent surface 유지

- `state_unavailable`
  - adapter guards 반영
  - strip은 `no canonical state yet`

- `empty_board`
  - board state=`empty`
  - `no assets available`

- `partial activity/history`
  - activity items 없어도 lineage summary나 neutral helper 유지
  - `history_unavailable`면 panel 자체는 깨지지 않음

## 7. run/check result

### build check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data
runtime_root = Path('runtime').resolve()
for asset_id in [None, 'turboquant_youtube', 'choi_ai_classroom_cnn']:
    data = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    print(asset_id, data.get('state'), data.get('live_availability'), data.get('selected_asset_id'), data.get('pageTitle'))
PY
```

### result

- default asset:
  - `loaded / live_ready / choi_ai_classroom_vlm`
- explicit asset:
  - `turboquant_youtube -> loaded / live_ready`
  - `choi_ai_classroom_cnn -> loaded / live_ready`

### render check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data, render_operating_ui_live_composition_html
runtime_root = Path('runtime').resolve()
data = build_operating_ui_live_composition_data(runtime_root, asset_id='turboquant_youtube')
html = render_operating_ui_live_composition_html(data, api_path='/api/operating-ui-live?asset_id=turboquant_youtube')
print('Operating UI Live' in html, 'Derived State Strip' in html, 'Asset State Board' in html, 'Activity Panel' in html)
PY
```

### syntax check

```bash
python3 -m py_compile app/runtime/operating_ui_live.py app/core/runtime/viewer_server.py
```

## 8. fixture demo와 live demo의 역할 차이

- fixture demo
  - 고정 case A/B/C/D 검증용
  - deterministic
  - adapter/fallback 회귀 점검용

- live demo
  - 실제 runtime process-console payload 읽기
  - 현재 runtime state 반영
  - read-only live composition 확인용

## 9. limitations

- 아직 selected asset 변경 interactivity는 없다.
- live route는 process-console summary에서 기본 선택된 asset 또는 query `asset_id`만 따른다.
- modal/feedback/full shell은 여전히 범위 밖이다.
- style system은 최소 SSR 수준이다.

## 10. recommended next step

- 다음 구현 슬라이스는 **selected asset switch가 가능한 minimal live control bar** 또는 **read-only shell composition 정리**다.
- 이유:
  - strip/board/activity live path는 이미 열렸고, 이제 실제 운용면처럼 asset 전환을 확인할 최소 제어면이 필요하다.
