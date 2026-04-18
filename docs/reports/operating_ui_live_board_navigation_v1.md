# operating ui live board navigation v1

## 1. verdict

- 구현 완료
- live control bar에 이어, board card click으로도 selected asset 전환이 일어나도록 query-param 기반 navigation wiring을 추가했다.

## 2. created/updated files

- 수정
  - [asset_state_card.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/asset_state_card.py)
  - [asset_state_board.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/asset_state_board.py)
  - [run_board_component_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_board_component_demo.py)
  - [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

- 생성
  - [operating_ui_live_board_navigation_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_board_navigation_v1.md)

## 3. board link policy

- link 대상
  - v1에서는 **card title/wrapper render 영역**을 live route link로 연결한다.

- route policy
  - `/operating-ui-live?asset_id=<id>`

- selected card 처리
  - selected 여부와 무관하게 클릭 가능
  - selected card 재클릭도 허용
  - 동일 화면 재로드여도 문제 없음

- empty board 처리
  - `items=[]`면 링크 없음

- invalid/none_selected 상태
  - board item에 `id`가 있으면 link 유지
  - selection state만 `invalid_selected_asset` 또는 `none_selected`로 표기

## 4. query contract check

- control bar와 동일 정책 여부
  - 동일함
  - 둘 다 `asset_id` query param을 사용한다.

- valid `asset_id`
  - `selection_query_state = valid_asset_id`
  - strip / board / activity 함께 갱신

- invalid `asset_id`
  - `selection_query_state = invalid_selected_asset_query`
  - 기본 selected asset으로 fallback

- no `asset_id`
  - 기본 selected asset 사용
  - `selection_query_state = default_selected`

## 5. live render behavior

- board card click 후 기대 동작
  - GET 재요청
  - `asset_id` query 반영
  - selected asset 기준 strip 갱신
  - board selected highlight 갱신
  - activity panel도 selected asset 기준 데이터로 갱신

- 현재 구조 특징
  - board는 전체 asset rail 순서를 유지한다.
  - 따라서 “첫 카드”가 항상 현재 selected asset은 아니다.
  - selected asset highlight는 별도로 적용된다.

## 6. run/check result

### board view model check

```bash
python3 app/work/operating_ui/run_board_component_demo.py
```

- 결과
  - normal selected / invalid selected / none selected / empty board 모두 유지
  - 각 loaded card에 `href=/operating-ui-live?asset_id=<id>` 존재

### live composition check

```bash
python3 - <<'PY'
from pathlib import Path
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data, render_operating_ui_live_composition_html
runtime_root = Path('runtime').resolve()
data = build_operating_ui_live_composition_data(runtime_root, asset_id='turboquant_youtube')
print(data['board']['items'][0].get('href'))
html = render_operating_ui_live_composition_html(data, api_path='/api/operating-ui-live?asset_id=turboquant_youtube')
print('/operating-ui-live?asset_id=' in html)
PY
```

- 확인 결과
  - board item href 존재
  - live HTML 안에 board navigation link 존재

### syntax check

```bash
python3 -m py_compile app/work/operating_ui/components/asset_state_card.py app/work/operating_ui/components/asset_state_board.py app/work/operating_ui/run_board_component_demo.py app/runtime/operating_ui_live.py
```

## 7. limitations

- 현재 board link는 title/wrapper 수준의 서버 렌더 link다.
- selected asset가 board 첫 카드로 재정렬되지는 않는다.
- card 전체 clickable styling이나 hover affordance는 아직 최소 수준이다.
- control bar와 board click은 같은 contract를 쓰지만, query preserving sort/filter 확장은 아직 없다.

## 8. recommended next step

- 다음 구현 슬라이스는 **selected asset 기준 상세 summary side panel 또는 lightweight detail drawer의 read-only 최소 버전**이다.
- 이유:
  - 이제 대상을 바꾸어 읽는 흐름은 열렸고, 다음에는 선택 대상에 대한 더 풍부한 상태 요약을 같은 live route 안에서 보여줄 수 있어야 한다.
