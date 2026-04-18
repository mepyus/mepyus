[[DOCROLE:directive]]
[[RUNMODE:ingest_only]]
[[PRIORITY:high]]

# CODEX HANDOFF — STRUCTURED DOC ROUTING STABILITY BASELINE LOCK + NEXT STEP DIRECTIVE

## 0. turn purpose
이번 턴의 목적은 기능 확장이 아니라 structured doc routing 경로의 운영 안정화를 기준선으로 잠그고,
다음 Codex가 바로 이어서 유지/정리 레이어 작업으로 들어갈 수 있게 하는 것이다.

현재 repo는 “더 똑똑한 해석 엔진”보다
“문서 입력 -> routing -> registry/provenance/event -> receipt/board/commands surface”의
운영 바닥을 덜 깨지게 만드는 방향으로 유의미하게 전진했다.

이 문서는 그 상태를 기준선으로 고정하고,
다음 턴의 우선순위를 흔들리지 않게 넘기기 위한 handoff directive다.

---

## 1. current locked reading
현재 repo의 올바른 해석은 다음과 같다.

- 이번 턴의 진전은 semantic intelligence 확장이 아니다.
- 이번 턴의 진전은 structured doc operating floor stability 강화다.
- 즉, 문서가 들어오고, routing 되고, 기록되고, 조회 surface로 남는 경로가 예전보다 덜 깨진다.
- 특히 반복 실행 / 병렬 실행 / malformed tail 상황에서의 복원력과 write 안정성이 올라갔다.
- 따라서 다음 단계의 중심은 “새 기능 추가”보다 “쌓이는 흔적을 어떻게 안전하게 유지하고 읽기 좋게 만들 것인가”다.

한 줄 요약:
**현재 repo는 structured-doc operating workspace로서의 바닥 안정성이 꽤 진전된 상태다.**

---

## 2. already reflected assets

### 2.1 structured doc input / execution
- `codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md`
- 처리 방식:
  - `directive`
  - `ingest_then_execute`
  - `high`
- receipt:
  - `runtime/receipts/doc_codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1_operation_receipt.md`

### 2.2 preset setup documents
- `docs/reports/append_safety_review.md`
- `docs/reports/append_safety_patch_plan.md`
- `docs/reports/memory_layer_separation_map_v1.md`
- `docs/reports/existing_assets_to_memory_layers_map_v1.md`
- `docs/policies/input_calibration_reference_policy_v1.md`
- `docs/reports/interpreter_drift_check_plan_v1.md`
- `docs/contracts/code_reference_asset_schema_v1.md`
- `docs/policies/code_reference_ingest_policy_v1.md`
- `docs/contracts/operation_surface_min_spec_v1.md`
- `docs/contracts/operation_surface_data_requirements_v1.md`
- `docs/contracts/observation_probe_contract_v1.md`
- `docs/policies/company_space_boundary_policy_v1.md`

---

## 3. stabilization patches

### 3.1 common atomic / lock helper
files:
- `app/core/registry/atomic_io.py`
- `app/core/registry/__init__.py`

introduced helpers:
- `atomic_write_json`
- `atomic_write_text`
- `file_lock`
- `make_idempotency_key`

role:
- registry / provenance / ticket / surface 계열 write를 atomic + lock 기반으로 정리하는 공용 바닥

### 3.2 event append guard + malformed tail recovery
file:
- `app/core/events/event_append_guard.py`

introduced helpers:
- `append_jsonl_locked`
- `load_jsonl_with_tail_recovery`
- `recover_jsonl_tail`

role:
- JSONL append 안정화
- malformed tail 감지 및 회복
- 정상 row 보존 복구

### 3.3 routing script stabilization
file:
- `scripts/process_structured_doc_with_routing.py`

applied:
- registry / ticket / provenance write에 lock + atomic rewrite 적용
- receipt / board / commands write에 atomic text write 적용
- `run_id` 도입
- `idempotency_key` 도입
- per-run commands / board artifact 생성
- malformed ledger tail recovery를 실행 초반에 시도
- routing run_id와 observer output run_id를 분리
- `timestamp + microseconds + uuid suffix` 기반 run_id 생성으로 병렬 충돌 방지

### 3.4 operation event recording alignment
file:
- `scripts/record_operation_event.py`

applied:
- guarded append helper 재사용
- event append 방식 일관화

---

## 4. verification assets / tests

### 4.1 unit tests
- `tests/unit/test_atomic_io.py`
- `tests/unit/test_event_append_guard.py`
- `tests/unit/test_structured_doc_stability_helpers.py`

package init:
- `tests/__init__.py`
- `tests/unit/__init__.py`

### 4.2 self-check scripts
- `scripts/run_structured_doc_stability_check.py`
- `scripts/run_structured_doc_parallel_stress_check.py`
- `scripts/run_jsonl_recovery_drill.py`

---

## 5. confirmed results

### 5.1 tests passed
executed:
- `python3 -m unittest tests.unit.test_atomic_io tests.unit.test_event_append_guard tests.unit.test_structured_doc_stability_helpers -v`

confirmed:
- atomic io helper 동작 확인
- event append guard 동작 확인
- structured doc stability helper 동작 확인

### 5.2 recovery drill success
executed:
- `python3 scripts/run_jsonl_recovery_drill.py`

confirmed:
- malformed tail 감지
- recovery 적용
- `.broken` 백업 생성
- 정상 row만 복구

### 5.3 parallel stress success
executed:
- `python3 scripts/run_structured_doc_parallel_stress_check.py`

confirmed:
- `successful_runs=4`
- `unique_run_ids=4`
- `same_idempotency_key_for_all_runs=true`
- registry / ticket에 `last_run_id` 존재
- latest receipt / board / commands가 실제 실행 run 중 하나를 가리킴
- manifest JSON parse 문제 없음

---

## 6. interpretation of current state
현재 운영 해석은 아래로 고정한다.

### 6.1 what improved
- structured doc routing repeatability improved
- concurrent execution durability improved
- event / registry / provenance write safety improved
- malformed ledger tail survivability improved
- latest surface와 per-run surface를 함께 운영할 수 있는 바닥이 생김

### 6.2 what did NOT improve
- semantic reading sophistication 자체를 확장한 것은 아님
- interpretation engine를 넓힌 것은 아님
- distributed system 수준 보장을 한 것은 아님
- long-horizon storage hygiene를 완결한 것은 아님

### 6.3 locked verdict
**이번 턴의 성과는 “의미 판정 강화”가 아니라 “운영 경로 안정화”다.**

---

## 7. remaining risks
아직 남은 리스크는 숨기지 말고 아래처럼 유지한다.

### 7.1 provenance accumulation risk
- provenance link는 계속 누적된다
- 장기적으로 dedupe / compaction 정책이 없으면 surface 가독성과 유지비가 나빠질 수 있다

### 7.2 lock scope limitation
- 현재 file lock 기반은 단일 머신 / 현재 환경에서는 유효하다
- 더 큰 분산 환경 보장으로 읽으면 안 된다

### 7.3 recovery visibility gap
- recovery helper는 존재한다
- 하지만 실제 운영 ledger / event / receipt에 recovery 발생 사실을 자동으로 얼마나 명시적으로 남길지 더 다듬을 수 있다

### 7.4 latest vs per-run surface ambiguity
- latest surface와 per-run surface는 둘 다 존재한다
- 둘의 관계를 더 얇고 명확한 pointer 구조로 정리할 여지가 있다

---

## 8. next priority lock
다음 Codex는 아래 우선순위로 바로 들어간다.

### 8.1 P1 — provenance dedupe / compaction
goal:
- provenance 누적 흔적을 무조건 지우는 것이 아니라
  중복과 장기 누적 노이즈를 안전하게 줄이는 정책/코드를 만든다

expected outputs:
- provenance dedupe / compaction policy doc
- bounded compaction script or helper
- before / after 영향 검토 문서
- rollback / no-destruction guard 명시

reading rule:
- append-only spirit를 훼손하지 않는 bounded hygiene여야 한다
- “정리”가 “증거 제거”로 변질되면 안 된다

### 8.2 P2 — latest board / commands pointer surface thinning
goal:
- latest surface를 실제 내용을 중복해서 많이 품는 덩어리보다
  “가장 최근 실행을 가리키는 얇은 pointer surface”로 정리한다

expected outputs:
- latest board pointer spec
- latest commands pointer spec
- per-run artifact와 latest artifact 관계 문서
- 필요시 pointer-only surface patch

reading rule:
- latest는 대표 surface
- per-run은 근거 surface
- 관계를 더 읽기 쉽게 분리

### 8.3 P3 — explicit recovery recording
goal:
- recovery가 발생했을 때
  operation receipt / event / board 등에서 그 사실이 더 명시적으로 드러나게 한다

expected outputs:
- recovery recording rule
- recovery event emission patch or hook
- receipt 내 recovery note format
- recovery visibility check

reading rule:
- recovery는 숨겨진 내부 복구가 아니라 운영 사실로 남아야 한다
- 단, 과도한 noise event 양산은 피한다

### 8.4 P4 — higher parallel stress only if needed
goal:
- 현재 성공한 parallel stress를 더 높은 병렬 수로 늘려 경계 확인

expected outputs:
- expanded stress plan
- higher concurrency result summary
- failure mode가 있으면 bounded note

reading rule:
- 이 작업은 P1~P3보다 우선이 아니다
- 이미 현 수준의 안정성은 확인되었으므로 필요할 때만 확장한다

---

## 9. do not do first
다음 Codex는 아래를 첫 작업으로 잡지 않는다.

- broad feature expansion
- interpretation-engine widening
- unnecessary schema redesign
- distributed abstraction jump
- major refactor unrelated to trace hygiene
- semantic layer generalization unrelated to current stability path

한 줄 금지:
**지금 턴 다음에 바로 새 기능을 열지 말 것.**

---

## 10. recommended next-turn objective
다음 턴의 한 줄 objective는 아래로 고정한다.

**Move from “prevent breaking” to “manage accumulated traces safely and readably”.**

한국어 표현:
**이제는 “덜 깨지게” 다음으로, “쌓인 흔적을 안전하고 읽기 좋게 유지하는 법”으로 넘어간다.**

---

## 11. execution posture for next codex
다음 Codex는 아래 posture로 작업한다.

### 11.1 correct posture
- maintenance-layer tightening first
- evidence-preserving hygiene
- pointer-surface clarification
- recovery visibility improvement
- bounded change with clear receipts

### 11.2 wrong posture
- 새 기능을 먼저 여는 것
- 지금 상태를 semantic engine 부족으로 오독하는 것
- append-only spirit를 무시하고 누적 흔적을 공격적으로 삭제하는 것
- distributed-grade guarantee가 이미 된 것처럼 과장하는 것

---

## 12. final locked summary
현재 repo는 structured doc -> routing -> registry/provenance/event -> receipt/board 경로의 안정화가 꽤 진전됐다.

다음 단계는
“더 안 깨지게 만들기” 자체보다
“이미 쌓이기 시작한 흔적을 어떻게 안전하게 정리하고 유지하며 읽기 좋게 만들 것인가”로 넘어가면 된다.

최종 한 줄:
**이번 턴은 operation-floor stability lock이 핵심 성과이며, 다음 턴은 trace hygiene와 surface clarification이 핵심이다.**
