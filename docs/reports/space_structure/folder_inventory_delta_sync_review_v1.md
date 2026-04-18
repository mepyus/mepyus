# folder_inventory_delta_sync_review_v1

## purpose
변화분 기반 폴더 운용 레이어의 최소 구성을 기록한다.

## added layers
- `runtime/manifests/folder_changes/folder_change_log.jsonl`
- `runtime/manifests/folder_inventory/*.json`
- delta-based `folder_status.md` renderer

## current reading
- change layer: append-only 사건 기록
- inventory layer: 폴더 현재 상태 구조화
- render layer: 사람이 읽는 `folder_status.md`

## event class note
- 초기 inventory가 없던 폴더를 처음 sync 할 때는 `event_class=bootstrap_seed`
- 이후 같은 폴더에 생기는 실제 변화는 `event_class=delta_update`

## first applied folders
- `docs/guides`
- `runtime/observer/gemini`

## note
이 레이어는 전체 repo 재스캔을 기본으로 하지 않는다.
변화가 생긴 폴더와 부모 폴더만 갱신하는 최소 프로그램 운용 레이어다.
