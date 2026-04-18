# operating ui fallback surface polish v1

## 1. change summary

이번 슬라이스는 fallback semantics를 바꾸지 않고,
invalid query + fallback-selected 상황이 더 조용하지만 더 분명하게 읽히도록
표면 표현만 미세 조정한 턴이다.

반영 내용:
- invalid query일 때만 `fallback-selected asset` badge 추가
- control bar helper line을 `requested / fallback applied / current shown` 관계가 읽히도록 정리
- valid/default 상태는 과한 설명 없이 더 짧게 유지

## 2. badge location decision

badge 위치는 `Selected Detail Summary`에만 두었다.

이유:
- 현재 실제로 읽고 있는 selected asset surface이기 때문이다.
- control bar는 query 상태 설명의 주 표면이고,
  detail summary는 실제 표시 대상의 주 표면이다.
- strip/activity까지 badge를 퍼뜨리면 의미가 과해지고 중복된다.

## 3. wording differences

### invalid_selected_asset_query
- control bar:
  - `requested='<id>' not found / fallback applied / showing='<id>'`
- detail summary:
  - `fallback-selected asset` badge 노출

### valid_asset_id
- control bar:
  - `showing requested asset '<id>'`
- badge:
  - 없음

### default_selected
- control bar:
  - `no asset query provided / showing default selection '<id>'`
- badge:
  - 없음

## 4. created / updated files

- updated:
  - [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
  - [app/work/operating_ui/components/selected_asset_detail_summary.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/selected_asset_detail_summary.py)

## 5. run / check

확인 경로:
- `/operating-ui-live`
- `/operating-ui-live?asset_id=turboquant_youtube`
- `/operating-ui-live?asset_id=missing_asset`

결과:
- default:
  - notice만 존재
  - badge 없음
- valid:
  - notice만 존재
  - badge 없음
- invalid:
  - notice 존재
  - `fallback-selected asset` badge 존재
  - strip/detail/activity는 fallback-selected asset 기준으로 그대로 loaded

syntax check:
- `python3 -m py_compile app/runtime/operating_ui_live.py app/work/operating_ui/components/selected_asset_detail_summary.py`

## 6. remaining limitations

- `live_unavailable`는 이번 턴에서 별도 fixture를 추가하지 않았다.
- control bar는 아직 텍스트 기반 status line 중심이다.
