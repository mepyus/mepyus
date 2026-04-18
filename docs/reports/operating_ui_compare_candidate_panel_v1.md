# operating ui compare candidate panel v1

## 1. verdict

구현 완료.

이번 구현은
`right-column secondary read-only compare candidate panel`의
**guarded extension first pass**다.

중요:
- baseline semantics는 바꾸지 않았다
- adapter contract는 건드리지 않았다
- route/query contract는 건드리지 않았다
- compare panel은 recommendation surface가 아니라
  selected asset reading aid로만 구현했다

## 2. modified files

- [app/work/operating_ui/components/compare_candidate_panel.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/compare_candidate_panel.py)
- [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

## 3. panel placement

배치:
- 우측 column
  - `Selected Detail Summary`
  - `Compare Candidates`
  - `Activity Panel`

즉 compare panel은:
- detail 아래
- activity 위
에 놓이는 right-column secondary panel로 고정했다.

이유:
- board 전역면이 아니라 selected asset 보조 읽기층이기 때문이다
- detail/activity와의 reading order가 자연스럽다

## 4. first-pass content

표시:
- panel title
- compare candidate count
- candidate rows
  - asset id 또는 title
  - reason
- quiet helper

제한:
- full diff 없음
- evidence drilldown 없음
- ranking/recommendation wording 없음
- clickable action 없음
- deep workflow 없음

## 5. state behavior summary

### loaded

- `count`
- simple candidate rows
- `assetId/title`
- `reason`

### empty

- helper:
  - `no compare candidates`

### no_selected_asset

- helper:
  - `select an asset to inspect compare candidates`

### state_unavailable

- helper:
  - `compare candidates unavailable`

### live_unavailable

- helper:
  - `compare candidates unavailable`

주의:
- live unavailable의 주 설명은 여전히 control bar / page fallback이 담당한다
- unavailable path에서 compare panel은 조용히 내려오는 helper 성격만 가진다

## 6. boundary preservation

### detail와의 관계

- detail summary는 selected asset 자체를 요약한다
- compare panel은 compare candidate만 보조적으로 읽게 한다
- detail summary의 canonical/diff/attention/memory 책임은 건드리지 않았다

### activity와의 관계

- activity panel은 lineage/history hint를 담당한다
- compare panel은 compare candidate hint만 담당한다
- activity vocabulary를 가져오지 않았다

## 7. verification

runtime live 확인:
- `/operating-ui-live`
- `/operating-ui-live?asset_id=<valid>`
- `/operating-ui-live?asset_id=missing_asset`
- `/operating-ui-live?live_mode=unavailable`

확인 결과:
- default selected asset
  - compare panel `loaded`
  - count `4`
- valid asset
  - compare panel `loaded`
  - count `4`
- invalid query fallback-selected
  - compare panel `loaded`
  - fallback-selected asset 기준으로 그대로 읽힘
- live unavailable
  - page fallback이 우선
  - compare panel은 별도 interactive surface로 확장되지 않음

component state 확인:
- `empty` -> `no compare candidates`
- `no_selected_asset` -> `select an asset to inspect compare candidates`
- `state_unavailable` -> `compare candidates unavailable`
- `live_unavailable` -> `compare candidates unavailable`

syntax:
- `python3 -m py_compile app/work/operating_ui/components/compare_candidate_panel.py app/runtime/operating_ui_live.py`

## 8. remaining limitations

- first pass는 existing `compareCandidates`만 쓰므로 title richness가 낮다
- runtime 기준으로 현재 compareCandidates empty 케이스는 직접 관찰되지 않았고 component state check로 보완했다
- live unavailable path에서는 page fallback이 우선이라 compare panel의 visual 존재감은 최소다

## 9. next note

이번 구현은 baseline 변경이 아니라
guarded extension first pass다.

다음 확장을 고려한다면:
- 먼저 compare panel이 recommendation처럼 읽히지 않는지 검토해야 하고
- 그 다음에야 richer title/meta 또는 minimal navigation 여부를 검토할 수 있다
