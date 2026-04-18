[[A]] [[OBJ:history_compaction_policy_v1_report]] [[SEM:report_for_recent_full_plus_older_compacted_history_policy]]

# history_compaction_policy_v1_report

## 1. purpose

- 이번 report의 목적은 recent full lineage + older compacted summary 구조를 representative asset에서 어떻게 적용했는지 기록하는 것이다.

## 2. recent window

- current thin validation window:
  - recent `3` records full display

이 값은 representative 검증을 위한 얇은 surface 기준이며, raw history는 그대로 보존된다.

## 3. compaction strategy

- older provenance_only run은 summary node로 묶는다
- turning point는 anchor node로 남긴다
- raw jsonl history는 삭제하지 않는다

## 4. no-compaction anchors

- first record
- latest previous
- packet / grounding / traceability / blocker turning point
- manual correction

## 5. representative read

- `youtube_03_22`
  - recent full = `3`
  - older nodes = `2`
  - first older node = `summary`
- `openai_02_11`
  - recent full = `3`
  - older nodes = `2`
  - first older node = `summary`
- `knowledge_editing_youtube`
  - recent full = `3`
  - older nodes = `1`
  - first older node = `anchor`
- `gary_tan_brain`
  - recent full = `3`
  - older nodes = `1`
  - first older node = `anchor`

## 6. lineage safety

- raw history length은 그대로 유지된다
- compacted node는 summary-as-truth가 아니라 read aid로만 사용된다
- first/backfill anchor와 latest previous 연결은 끊기지 않는다

## 7. remaining limits

- representative asset history가 아직 길지 않아서 compaction 효과는 얇게 보이는 편이다
- current compacted node는 summary + anchor 수준이며, expanded raw access UI는 후속 보강 여지가 있다

## 8. one-line verdict

> history compaction policy는 raw lineage를 훼손하지 않으면서 recent full lineage를 우선 유지하고, older provenance-heavy 구간만 가볍게 summary/anchor로 읽게 만들어 process console의 시간축 가독성을 지킨다.
