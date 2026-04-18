# operating ui activity panel v1

## 1. verdict

- 구현 완료
- `ActivityPanel`은 adapter model만 받아 recent activity / lineage summary / diff hint를 read-only로 표시하는 최소 panel로 고정됐다.

## 2. created files

- [activity_panel.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/activity_panel.py)
- [run_activity_panel_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_activity_panel_demo.py)

## 3. component coverage

- 역할
  - recent activity list 표시
  - latest lineage summary 얇게 표시
  - diff hint helper 수준 표시

- props 요약
  - `items`
  - `historySummary`
  - `latestLineage`
  - `emptyLabel`
  - `onOpenHistoryItem`
  - `onOpenDiff`

- adapter model에서 소비하는 필드
  - `activityPanel.items[*].id`
  - `activityPanel.items[*].label`
  - `activityPanel.items[*].activityType`
  - `activityPanel.items[*].summary`
  - `activityPanel.items[*].timestamp`
  - `activityPanel.items[*].compareIndex`
  - `activityPanel.latestLineageSummary`
  - `activityPanel.latestTrigger`
  - `activityPanel.latestReason`
  - `activityPanel.latestUpdatedAt`

## 4. adapter dependency check

- raw payload 직접 참조 여부
  - 없음

- adapter model 사용 범위
  - demo에서 raw fixture -> adapter -> activity panel 순서만 허용
  - component 구현 자체는 adapter shape만 사용

## 5. fallback behavior check

- empty activity
  - `items=[]`면 `state=empty`
  - `no recent activity`

- history unavailable
  - `historySummary.state=history_unavailable`면 `state=history_unavailable`
  - `history unavailable`

- latestLineage absent
  - lineage summary 생략
  - panel은 정상 유지

- diff unavailable
  - `historySummary`에 diff hint가 없거나 `no_previous_state`면 CTA 비활성 또는 neutral helper

- state_unavailable와의 관계
  - selected asset가 없어도 activity items가 있으면 panel은 independent read-only panel로 유지 가능

## 6. boundary check

- modal/detail 역할 침범 여부
  - 없음

- 제한한 경계
  - full history explorer 아님
  - evidence drilldown 아님
  - detail modal 아님
  - action workflow 아님
  - recent activity reading surface까지만 담당

## 7. demo/check result

### command

```bash
python3 app/work/operating_ui/run_activity_panel_demo.py
python3 -m py_compile app/work/operating_ui/components/activity_panel.py app/work/operating_ui/run_activity_panel_demo.py
```

### 확인 포인트

- normal activity
  - item 1개 이상 표시
  - lineage + diff hint 병행

- empty activity with lineage
  - item 없이도 lineage summary 읽힘

- history unavailable
  - neutral fallback state

- latestLineage absent
  - lineage section 생략하고 activity item만 유지

## 8. limitations

- `historySummary`는 아직 adapter의 정식 sub-model로 고정되지 않았고 panel 수준에서 최소 힌트만 받는다.
- relative time formatting 없음
- diff CTA는 callback 가능 여부만 계산하고 실제 행동은 하지 않는다.
- long activity thread 축약/확장 없음

## 9. recommended next step

- 다음 구현 슬라이스는 `SelectedAssetDetailModal`이 아니라, 그 전에 `OperatingBoardPage` 없이도 함께 볼 수 있는 **read-only board + strip + activity panel composition demo**다.
- 이유:
  - 현재 조각들이 개별적으로 안정됐으므로, page shell 없이도 병렬 배치 연결을 먼저 확인하는 게 더 안전하다.
