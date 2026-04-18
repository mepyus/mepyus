[[A]] [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]

# codex_directive_core_input_layer_labeler_realization_v1

## 1. Purpose
이 문서는 core input-layer labeler 를 최소 실체화하고,
structured doc intake 에서 external routing labels 와 core intake labels 를
하나의 label packet 으로 조립하도록 만드는 실행 지시 원문이다.

## 2. Execution Target
- create `app/input_layer/labeler/labeler.py`
- update `app/input_layer/labeler/folder_status.md`
- connect structured doc routing wrapper to core input-layer label packet generation

## 3. Required Rule
- do not change ticket/event schema
- do not absorb anchorizer into labeler
- do not implement fragment retrieval/grouping labels
- keep the scope to core input-layer label normalization
