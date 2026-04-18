# operating ui viewer server composition demo v1

## 1. verdict

- 구현 완료
- 기존 `viewer_server`를 재사용해, 현재까지 구현된 read-only operating UI 조각들을 한 화면에서 함께 보는 최소 composition demo를 붙였다.

## 2. viewer_server entry reading

- 사용한 진입점
  - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

- 기존 구조
  - `route -> build_*_data -> render_*_html`
  - HTML route와 JSON API route를 짝으로 유지

- 이번에 추가한 최소 경로
  - `/operating-ui-demo`
  - `/api/operating-ui-demo`

- 선택 이유
  - 기존 흐름을 그대로 따른다
  - `process-console`와 독립된 demo surface로 붙인다
  - main 구조를 뒤엎지 않고 work/demo 성격으로 제한할 수 있다

## 3. created/updated files

- 생성
  - [operating_ui_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_demo.py)
  - [operating_ui_viewer_server_composition_demo_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_viewer_server_composition_demo_v1.md)

- 수정
  - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

## 4. composition coverage

- 이번 demo에서 붙인 조각
  - `DerivedStateStrip`
  - `AssetStateBoard`
  - `ActivityPanel`

- 배치
  - 상단: `DerivedStateStrip`
  - 본문 좌측: `AssetStateBoard`
  - 본문 우측: `ActivityPanel`

- 의도
  - board / strip / activity가 **한 화면에서 병렬로 읽히는지**만 확인
  - modal, feedback, full shell은 아직 넣지 않음

## 5. data flow check

- 흐름
  - fixture raw payload
  - [operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
  - adapted ui model
  - readonly components
    - [derived_state_strip.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/derived_state_strip.py)
    - [asset_state_board.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/asset_state_board.py)
    - [activity_panel.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/activity_panel.py)
  - viewer render

- 핵심 확인
  - raw payload를 UI 조각이 직접 읽지 않는다
  - demo helper만 fixture raw를 adapter에 넘긴다

## 6. case support

- 지원 여부
  - case A: 지원
  - case B: 지원
  - case C: 지원
  - case D: 지원

- query param
  - `/operating-ui-demo?case=a`
  - `/operating-ui-demo?case=b`
  - `/operating-ui-demo?case=c`
  - `/operating-ui-demo?case=d`

## 7. run/check result

### build check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_demo import build_operating_ui_composition_demo_data
runtime_root = Path('runtime').resolve()
for case in ['a','b','c','d']:
    data = build_operating_ui_composition_demo_data(runtime_root, case=case)
    print(case, data.get('state'), data.get('pageTitle'))
PY
```

### render check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_demo import build_operating_ui_composition_demo_data, render_operating_ui_composition_demo_html
runtime_root = Path('runtime').resolve()
data = build_operating_ui_composition_demo_data(runtime_root, case='a')
html = render_operating_ui_composition_demo_html(data)
print('Operating UI Demo' in html, 'Derived State Strip' in html, 'Asset State Board' in html, 'Activity Panel' in html)
PY
```

### syntax check

```bash
python3 -m py_compile app/runtime/operating_ui_demo.py app/core/runtime/viewer_server.py
```

### 확인 결과

- case A/B/C/D 모두 `loaded`
- HTML render에 아래 섹션 모두 존재
  - `Derived State Strip`
  - `Asset State Board`
  - `Activity Panel`

## 8. limitations

- fixture 기반 demo다.
  - 실제 runtime payload live binding은 아직 아님
- strip/board/activity는 text-forward SSR 성격이다.
- selected asset 변경 interactivity는 아직 고정 demo 수준이다.
- modal/feedback/full page shell은 아직 없다.
- style language는 최소 수준이고 donor visual language를 본격 이식하지 않았다.

## 9. recommended next step

- 다음 구현 슬라이스는 `fixture source`를 넘어서 **runtime process-console payload를 직접 adapter에 연결하는 read-only live composition path**를 여는 것이다.
- 이유:
  - 현재 조각과 viewer route는 이미 있으므로, 이제 고정 fixture가 아니라 실제 selected asset payload를 같은 composition에 흘려보내는 단계로 넘어갈 수 있다.
