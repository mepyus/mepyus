# operating ui layout refinement v1

## 1. verdict

- 구현 완료
- 기존 live operating UI composition을 유지한 채, 조각들을 더 읽기 쉬운 3영역 operating shell로 정리했다.

## 2. created/updated files

- 수정
  - [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

- 생성
  - [operating_ui_layout_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_layout_refinement_v1.md)

## 3. layout coverage

### before

- top header
- control bar
- strip
- left board
- right detail
- right activity

- 문제:
  - 상단 제어면과 상태 요약면이 분리되어 있었지만 같은 수준의 계층으로 읽혔다.
  - 본문 좌측 선택 / 우측 읽기 구조가 암묵적이었다.

### after

- 상단
  - `Live Control Bar`
  - `Derived State Strip`

- 본문 좌측
  - `Asset State Board`

- 본문 우측
  - `Selected Detail Summary`
  - `Activity Panel`

### 결과

- `운용 대상 선택`
- `선택 대상 읽기`
- `최근 활동 읽기`

이 세 역할이 시각적으로 더 명확해졌다.

## 4. reading logic

- `Live Control Bar`
  - 현재 무엇을 보고 있는지
  - 어떤 query 상태인지
  - 무엇으로 전환할 수 있는지

- `Derived State Strip`
  - 현재 선택 대상의 핵심 상태를 가장 먼저 요약
  - live 제어면 바로 아래 둬서 “대상 선택 -> 상태 확인” 순서를 고정

- `Asset State Board`
  - 운용 대상 선택면
  - 목록/선택/전환의 핵심 표면

- `Selected Detail Summary`
  - 선택 대상 읽기면
  - board보다 조금 더 풍부하게 현재 상태를 읽게 함

- `Activity Panel`
  - 최근 lineage / activity 읽기면
  - 상세 탐색이 아니라 현재 변화 흐름을 병렬로 읽게 함

### 왜 strip과 control bar를 상단에 두는가

- 현재 운용면에서 제일 먼저 필요한 건
  - 대상 전환 제어
  - 선택된 대상의 핵심 상태 요약
이기 때문이다.
- board를 먼저 보기 전에 “무엇을 보고 있고 어떤 상태인지”가 위에서 고정되면 전체 읽기 순서가 안정된다.

### 왜 지금은 lightweight refinement까지만 하는가

- 이번 단계의 목표는 새 기능이 아니라 **읽기 질서 정리**다.
- 지금 조각들은 이미 충분히 붙어 있으므로, full shell을 새로 만드는 대신 현재 composition의 reading order를 정리하는 쪽이 리스크가 적다.

## 5. fallback preservation check

- 유지된 fallback
  - `no_selected_asset`
  - `state_unavailable`
  - `no_previous_state`
  - `insufficient_attention_history`
  - `empty_board`
  - `partial activity/history`
  - `invalid_selected_asset_query`

- 확인 결과
  - layout refinement 이후에도 fallback 문구와 상태 흐름은 유지된다.
  - 특히 `missing_asset` 입력 시:
    - `selection_query_state = invalid_selected_asset_query`
    - board는 계속 읽힘
    - detail은 `state_unavailable`
    - activity는 `history_unavailable`
    - shell 자체는 깨지지 않음

## 6. run/check result

### command

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data, render_operating_ui_live_composition_html
runtime_root = Path('runtime').resolve()
for asset_id in [None, 'turboquant_youtube', 'choi_ai_classroom_cnn', 'missing_asset']:
    data = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    print({
        'requested': asset_id,
        'state': data.get('state'),
        'selection_query_state': data.get('selection_query_state'),
        'availability': data.get('live_availability'),
        'selected_asset_id': data.get('selected_asset_id'),
        'board_state': data.get('board',{}).get('state'),
        'detail_state': data.get('detail_summary',{}).get('state'),
        'activity_state': data.get('activity',{}).get('state'),
    })
html = render_operating_ui_live_composition_html(build_operating_ui_live_composition_data(runtime_root, asset_id='turboquant_youtube'))
checks = [
    'Live Control Bar' in html,
    'Derived State Strip' in html,
    'Asset State Board' in html,
    'Selected Detail Summary' in html,
    'Activity Panel' in html,
    'select operating target' in html,
    'read current target' in html,
    'recent lineage and activity hints' in html,
]
print(checks)
PY
```

### result

- default selected asset
  - `loaded / default_selected / live_ready`

- `turboquant_youtube`
  - `loaded / valid_asset_id / live_ready`

- `choi_ai_classroom_cnn`
  - `loaded / valid_asset_id / live_ready`

- `missing_asset`
  - `loaded / invalid_selected_asset_query`
  - detail/activity fallback 유지

- HTML section check
  - 모든 핵심 섹션 존재 확인
  - 상단 subheading까지 확인

## 7. limitations

- 여전히 SSR text-forward surface다.
- 우측 detail/activity 패널은 시각적으로만 분리됐고 collapse/expand 같은 refinement는 없다.
- invalid asset query에서 fallback selected asset는 유지되지만, availability label이 `state_unavailable`로 내려가는 현재 규칙은 이후 조정 여지가 있다.
- full shell이라기보다 read-only shell refinement 수준이다.

## 8. recommended next step

- 다음 구현 슬라이스는 **invalid query fallback semantics 정리 + selected fallback messaging refinement**다.
- 이유:
  - 현재 기능은 충분히 열렸고, 이제 작은 의미 차이, 특히 invalid query 시 availability/selected fallback이 어떻게 읽히는지 더 정밀하게 다듬을 필요가 있다.
