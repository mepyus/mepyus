# folder_status_render_contract_v1

## purpose
`folder_status.md`를 원장이 아니라 읽기면으로 고정한다.

## lock
- `folder_status.md`는 append-only 원장이 아니다.
- 원장은 `runtime/manifests/folder_changes/`와 `runtime/manifests/folder_inventory/`다.
- `folder_status.md`는 inventory manifest를 기반으로 렌더된다.
- 변화는 먼저 change log에 append되고, 그 다음 inventory가 갱신되며, 마지막에 `folder_status.md`가 재렌더된다.

## consequences
- `folder_status.md`를 직접 사실 원장처럼 관리하지 않는다.
- 새 폴더/새 문서/새 자산은 change log와 inventory에 먼저 반영한다.
- status 문서는 국소 갱신의 결과물로만 읽는다.

## one line
`folder_status.md` is a rendered reading surface, not the ledger of truth.
