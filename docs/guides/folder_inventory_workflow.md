# folder_inventory_workflow

이 문서는 새 폴더나 새 문서가 생겼을 때 전체를 다시 읽지 않고 어떻게 반영하는지 설명한다.

## flow
1. 변화가 생긴다.
2. change log에 사건을 append한다.
3. 해당 폴더 inventory와 부모 폴더 inventory를 갱신한다.
4. `folder_status.md`를 다시 렌더한다.

## note
핵심은 전체 재스캔이 아니라 변화분 반영이다.
