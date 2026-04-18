[[A]] [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]

# codex_directive_label_family_separation_contract_v1

## 1. Purpose
이 문서는 `label family separation contract v1` 을 잠그고,
`app/input_layer/labeler` 를 contract-first core slot 으로 다시 읽히게 만들기 위한 실행 지시 원문이다.

## 2. Current Reading
- labeling exists
- core labeler is not yet consolidated

## 3. Execution Target
- create `docs/contracts/label_family_separation_contract_v1.md`
- update `app/input_layer/labeler/folder_status.md`

## 4. Required Rule
- do not implement `labeler.py`
- do not modify routing, registry, event, or anchor logic
- lock family boundaries only
