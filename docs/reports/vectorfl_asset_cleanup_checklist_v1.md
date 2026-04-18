# vectorfl_asset_cleanup_checklist_v1

## 1. Purpose
이 문서는 현재 `vectorfl_replica` 안에서
`무엇을 지금 정리해야 하는지`, `무엇은 나중으로 미뤄도 되는지`,
`무엇은 아직 비어 있는 슬롯인지`를 체크리스트 형태로 고정한 문서다.

용도:
- 나중에 하나씩 확인하면서 처리
- 이미 확인한 자산과 아직 안 건드린 자산 구분
- 새 작업 전에 정리 상태 재점검

---

## 2. 지금 정리할 자산

### A. `app/core/runtime` dense bank
- [ ] [app/core/runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/folder_status.md) 다시 확인
- [ ] `connection / observer / reporting / approval / imported material` family 로 더 압축
- [ ] 현재 active layer 와 legacy bank 차이를 더 짧게 잠금
- [ ] 새 기능 재사용 시 먼저 볼 대표 파일 목록 확정

메모:
- 현재는 representative sampling 까지 됐고, family-level compression 이 더 필요함

### B. `runtime/manifests` 내부 family
- [ ] [runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/runtime/folder_status.md) 기준으로 manifests 재독해
- [ ] `operation manifests`
- [ ] `origin / provenance manifests`
- [ ] `view / result manifests`
- [ ] 내부 family 를 짧은 atlas 문장으로 분리

메모:
- 지금은 하나의 bank 처럼 보이지만 실제론 여러 계열이 섞여 있음

### C. `scripts/` specialized/backfill family
- [ ] [scripts/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/scripts/folder_status.md) 기준 재확인
- [ ] `backfill_*` family 정리
- [ ] `sync_*` family 정리
- [ ] `recover_* / refine_*` family 정리
- [ ] processor-compare/import bridge family 정리

메모:
- main operation scripts 는 이미 보임
- maintenance family 가 아직 압축 설명 부족

### D. `app/work` stage archive
- [ ] [app/work/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/folder_status.md) 재확인
- [ ] 현재 기준선 stage 와 과거 실험 stage 구분
- [ ] 재사용 가치 높은 stage 표시
- [ ] 지금은 읽지 않아도 되는 stage 표시

메모:
- 상위 구조는 잡혔지만 현재성/재사용성 표시가 더 필요함

### E. `references/vectorfl*` historical vs reusable split
- [ ] [references/vectorfl/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/vectorfl/folder_status.md) 재확인
- [ ] [references/vectorfl_next/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/vectorfl_next/folder_status.md) 재확인
- [ ] current reusable asset 표시
- [ ] historical comparison asset 표시
- [ ] 새 기능 만들 때 바로 참조할 위치 표시

메모:
- 지금은 baseline comparison memory 로는 읽히지만, 재사용성 구분은 더 필요함

---

## 3. 나중에 정리할 자산

### A. receipt / board / command surface
- [ ] [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts) later review
- [ ] [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views) later review
- [ ] [runtime/commands](/Users/sungsookim/universe/vectorfl_replica/runtime/commands) later review

메모:
- 지금은 작고 읽기 쉬워서 급하지 않음

### B. event layer
- [ ] [runtime/events](/Users/sungsookim/universe/vectorfl_replica/runtime/events) later compaction review

메모:
- 구조는 단순하고 append-only skeleton 도 이미 있음

### C. low-priority references
- [ ] [references/vectorfl_next_gemini_session/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/vectorfl_next_gemini_session/folder_status.md) later review
- [ ] [references/md_maker/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/md_maker/folder_status.md) later review

메모:
- 현재 핵심 calibration lane 은 아님

### D. low-priority app lanes
- [ ] `app/events` later review
- [ ] `app/models` later review

메모:
- 현재 엔진 핵심 탐색선은 아님

---

## 4. 아직 만들지 않은 슬롯

### A. input-layer `labeler`
- [ ] [app/input_layer/labeler/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/labeler/folder_status.md) 기준 slot 확인
- [ ] minimal label helper 필요 여부 확정
- [ ] input label 과 operation metadata label 관계 정리

메모:
- 현재 가장 명확한 빈 슬롯

### B. current preferred segmentation contract
- [ ] 현재 split truth 를 문서로 고정할지 결정
- [ ] experimental segmenter 와 preferred path 구분
- [ ] operator-facing split 과 core split 관계 정리

메모:
- segmenter 는 존재하지만 현행 truth note 는 없음

### C. wrapper / input-core link note
- [ ] structured doc routing wrapper 와 `app/input_layer` 관계 정리
- [ ] 무엇이 wrapper 책임이고 무엇이 core input 책임인지 잠금

메모:
- 현재는 개념적으로 연결되어 있지만 문서상으로 더 또렷해질 필요가 있음

---

## 5. Recommended Order
실제로는 아래 순서로 체크하는 것이 가장 효율적이다.

1. `app/core/runtime`
2. `runtime/manifests`
3. `scripts specialized/backfill`
4. `app/work`
5. `references/vectorfl*`
6. `labeler slot`
7. `segmentation contract`
8. `wrapper/core link note`

---

## 6. One-Line Conclusion
현재 `vectorfl_replica` 에서 가장 시급한 것은 새 자산을 더 만드는 것보다, 이미 있는 dense bank 와 historical asset 을 더 분류하고, 실제로 비어 있는 몇 개 슬롯만 선명하게 채울 준비를 하는 것이다.
