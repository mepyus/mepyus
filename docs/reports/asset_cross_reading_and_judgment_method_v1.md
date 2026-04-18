# asset cross reading and judgment method v1

## 0. why this record exists

- 이번 기록의 목적은 repo 전체를 다시 inventory 하는 것이 아니다.
- 자산 3개를 실제로 따라가며, 공간 안에서 어떤 데이터가 어떤 방식으로 살아남았는지와 그 판단 방식이 재사용 가능한지를 교차 판독하는 것이다.
- 또한 이번 턴에서 Codex가 무엇을 읽고 어떤 근거로 판단했는지도 복원 가능하게 남긴다.

## 1. codex observation scope

이번 턴에서 직접 읽은 축:

- `runtime/fragments/frag_active_choi_ai_classroom_vlm_object.json`
- `runtime/fragments/frag_active_choi_ai_classroom_vlm_grounding_status.json`
- `runtime/manifests/user_pages/saved_connections.jsonl`
- `runtime/receipts/doc_connection_meaning_and_user_layer_translation_baseline_v1_operation_receipt.md`
- `app/work/observer_ingest_min/generated/source_manifest_connection_meaning_and_user_layer_translation_baseline_v1_20260328_092001.json`
- `app/work/observer_ingest_min/generated/split_units_connection_meaning_and_user_layer_translation_baseline_v1_20260328_092001.json`
- `app/work/observer_ingest_min/generated/processing_trace_connection_meaning_and_user_layer_translation_baseline_v1_20260328_092001.json`
- `docs/reports/entry_gate_not_passed_common_bottleneck_integration_v1.md`
- `docs/reports/domain_specific_vs_reusable_split_note_v1.md`
- `app/work/dialogue_loop_test/generated/claude_code_index_segmentation_probe_v1_w6_s3_20260328T100910Z.json`

선정 자산 3개:

1. `choi_ai_classroom_vlm`
   - 이유: 현재 `/operating -> /explore -> saved_connection` 루프와 가장 가깝고, canonical onboarding 성공이 실제로 발생한 active asset이다.
2. `connection_meaning_and_user_layer_translation_baseline_v1`
   - 이유: 선언/기준문이 문장으로만 머무르지 않고 routing/observer ingest/receipt로 실제 처리된 대표 structured doc다.
3. `claude_code_index`
   - 이유: probe와 비교 읽기에서 풍부한 signal이 나오지만, reusable institution이 아닌 scaffold dependence가 같이 드러나는 대표 자산이다.

---

## 2. asset 1 — choi_ai_classroom_vlm

### A. 입력 / 출발점

- 출발 재료:
  - `inputs/external_cases/choi_ai_classroom_vlm.txt`
- active asset raw shape:
  - `evidenceRefs.kind=source_file`
  - `canonicalStateRows`
- surface entry:
  - `/operating`
  - `/explore`

### B. 중간 변환

실제로 작동한 단계:

1. `canonicalStateRows -> 원문 단락 복귀`
2. `active asset first-pass fragment generation`
3. `fragment anchor enrichment`
4. `paragraph/source 기반 canonical match`
5. `saved_connection 저장`
6. `canonical-better dedupe upgrade`

남은 산출물:

- `runtime/fragments/frag_active_choi_ai_classroom_vlm_object.json`
- `runtime/fragments/frag_active_choi_ai_classroom_vlm_grounding_status.json`
- `runtime/manifests/user_pages/saved_connections.jsonl`

### C. 살아남은 데이터

단순 존재가 아니라 실제로 살아남은 데이터:

- object fragment:
  - `object.model.vision_language_model`
  - `scene=explanation`
  - `flow=expand`
- grounding_status row fragment:
  - `semantic.contrastive_learning`
  - `scene=comparison`
  - `flow=contract`
- traceability_status saved connection:
  - `semantic.embedding_space_distance`
  - `scene=evidence`
  - `flow=bridge`

즉 이 자산에서 살아남은 것은 row label 자체가 아니라,
- 원문 단락으로 복귀된 값
- canonical anchor
- scene/flow binding
- 그 결과가 saved_connection으로 남은 상태
다.

### D. 발견 방식

이 데이터는 아래 방식으로 발견/승격됐다.

- `reread from paragraph`
  - row를 직접 저장하지 않고 원문 단락으로 복귀
- `active asset first-pass fragment generation`
  - active asset용 fragment를 새로 생성
- `fragment anchor enrichment`
  - 한국어 단락에서 canonical anchor 부착
- `paragraph/source canonical match`
  - object/value paragraph text와 source_pointer를 기준으로 first-pass fragment match
- `canonical-better dedupe upgrade`
  - 기존 provisional save가 있어도 canonical binding이 더 좋으면 upgrade

사람 수동 판단 개입:

- row별 `scene/flow` 기본 매핑은 현재는 사람이 잠근 `DEFAULT_ROW_SCENE_FLOW`에 기대고 있다.
- 즉 완전 자동 institution이 아니라, 부분 자동 + bounded human choice다.

### E. 방식의 정체

- 단순 추출이 아니다.
- `분절값 -> 원문 복귀 -> canonical anchor binding -> 점진 승격` 방식이다.
- 더 정확히는:
  - 관계 복원
  - 의미 폭 복귀
  - 더 좋은 binding이 생길 때 upgrade
의 혼합이다.

### F. 재사용 가능성

- 재사용 가능: `yes`
- 최소 조건:
  - `asset_id`
  - `source_file`
  - `canonicalStateRows`
  - 해당 단락에서 canonical anchor를 만들 수 있는 anchorizer coverage
- 병목:
  - active asset raw payload 부재
  - canonical row 없음
  - anchorizer rule 미커버리지

---

## 3. asset 2 — connection_meaning_and_user_layer_translation_baseline_v1

### A. 입력 / 출발점

- 출발 재료:
  - `source_assets/baselines/connection_meaning_and_user_layer_translation_baseline_v1.md`
- 처리 시작점:
  - `scripts/process_structured_doc_with_routing.py`

### B. 중간 변환

실제로 작동한 단계:

1. routing normalize
2. label packet 생성
3. structured doc registry 등록
4. observer ingest 실행
5. `source_manifest / split_units / processing_trace` 생성
6. receipt 기록

남은 산출물:

- `runtime/receipts/doc_connection_meaning_and_user_layer_translation_baseline_v1_operation_receipt.md`
- `app/work/observer_ingest_min/generated/source_manifest_connection_meaning_and_user_layer_translation_baseline_v1_20260328_092001.json`
- `app/work/observer_ingest_min/generated/split_units_connection_meaning_and_user_layer_translation_baseline_v1_20260328_092001.json`
- `app/work/observer_ingest_min/generated/processing_trace_connection_meaning_and_user_layer_translation_baseline_v1_20260328_092001.json`

### C. 살아남은 데이터

이 자산에서 살아남은 데이터는 “개별 의미 anchor”보다 아래에 가깝다.

- 문서가 `structured_internal_doc`로 등록된 사실
- `heading` 기준으로 `30개 unit`이 잘렸다는 사실
- 이 문서를 처리한 run identity / receipt / generated files / command lineage

즉 여기서 살아남은 것은 문서 내용 자체보다,
`문서가 처리 가능한 구조 자산으로 들어왔다는 운영 기억`
이다.

### D. 발견 방식

- `routing normalize`
- `observer ingest`
- `split_units`
- `processing_trace`
- `receipt/provenance`

사람 수동 판단 개입:

- 문서에 routing marker가 비어 있어도 `memo / ingest_only / normal`로 normalize 됐다.
- 즉 문서 정체성 판정에는 여전히 bounded human rule이 개입한다.

### E. 방식의 정체

- 단순 텍스트 저장이 아니다.
- `문서 -> 처리 run -> traceable receipt`로 바꾸는 운영 기관이다.
- 더 정확히는:
  - intake normalization
  - 처리 사건화
  - provenance 추적 가능화
다.

### F. 재사용 가능성

- 재사용 가능: `yes`
- 최소 조건:
  - file path
  - doc text
  - routing normalize rule
  - observer ingest path
- 병목:
  - 문서는 잘 들어오지만, 그 결과가 나중 page/surface와 직접 닿는 연결은 아직 약할 수 있다.

---

## 4. asset 3 — claude_code_index

### A. 입력 / 출발점

- 출발 재료:
  - `inputs/external_cases/claude_code_index.txt`
- probe 시작점:
  - `app/work/dialogue_loop_test/generated/claude_code_index_segmentation_probe_v1_w6_s3_20260328T100910Z.json`
- 해석 report:
  - `docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md`

### B. 중간 변환

실제로 작동한 단계:

1. segmentation probe
2. window/block 비교
3. object/layer/relation/residue counting
4. purpose-aligned reread report 생성
5. 다른 자산과의 blocker integration

남은 산출물:

- segmentation probe json
- purpose reset reading report
- `entry_gate_not_passed_common_bottleneck_integration_v1.md`
- `domain_specific_vs_reusable_split_note_v1.md`

### C. 살아남은 데이터

probe 기준으로 실제로 떠오른 것:

- object candidates:
  - `에이전트 애플리케이션`
  - `생산성/코딩`
  - `모델 work`
  - `전략/방향성`
- layer hints:
  - `설명/해석 층`
  - `구현/실행 층`
  - `질문 유도 층`
- relation hints:
  - `reinforcement_hint`
  - `execution_shift_hint`
  - `transition_hint`
  - `question_generation_hint`

하지만 동시에 반복적으로 남은 약점:

- `question-inducing candidate` non-zero absence
- `fallback_grounded` dominant recovery
- weak role-like reading
- scaffold carryover risk

즉 이 자산에서 살아남은 것은
- 풍부한 signal 그 자체
- 그리고 그 signal이 곧 기관이 되지 못했다는 blocker 기억
둘 다다.

### D. 발견 방식

- `segmentation support probe`
- `windowed comparison`
- `object / layer / relation hint counting`
- `purpose reading`
- `common blocker integration`
- `domain-specific vs reusable split`

사람 수동 판단 개입:

- object/layer/relation counts는 자동으로 나오지만,
  그것을 `reusable attitude`인지 `scaffold-bound institution`인지 분리한 것은 사람이 해석한 결과다.

### E. 방식의 정체

- 단순 추출만은 아니다.
- `약한 신호 보존 + 공통 blocker 추적 + 태도/기관 분리` 방식이다.
- 즉 여기선 “무엇이 된다”보다 “무엇이 아직 institution이 아니다”를 판독하는 기관이 일부 작동 중이다.

### F. 재사용 가능성

- 재사용 가능: `partial`
- 재사용 가능한 부분:
  - segmentation probe
  - object/layer/relation hint counting
  - common blocker 묶음 기록
- 아직 scaffold 의존적인 부분:
  - robust role-like reading
  - question-inducing candidate emergence
  - pivot/compression recurrence

즉 태도는 재사용 가능하지만, 기관은 아직 약하다.

---

## 5. 자산 간 공통 판단 방식

공통으로 보인 판단 방식:

1. `trace first`
   - 모두 결과만 저장하지 않고, receipt / provenance / generated trace를 남긴다.
2. `원문 또는 출발 재료 복귀`
   - active asset은 paragraph reread
   - structured doc는 split_units/source_manifest
   - claude probe는 원문 block/window 기준 재독해
3. `약한 신호를 버리지 않음`
   - provisional binding
   - residue
   - blocker
   - watchpoint
4. `더 좋은 binding이 생기면 점진 승격`
   - choi asset saved_connection upgrade가 대표적이다.

---

## 6. 아직 scaffold 의존적인 판단 방식

- `question-inducing candidate`
  - 반복 signal은 있으나 non-zero recurrence를 안정적으로 만들지 못한다.
- `robust role-like reading`
  - 태도는 남지만 institution은 weak_medium 수준에 머문다.
- `wider explore queryability`
  - active asset reread는 열렸지만, 객체를 넣고 공간 전체를 넓게 질의하는 단계는 아직 약하다.
- `meaning-unit widening`
  - `/operating`과 `/explore`에서 읽는 단위가 충분히 넓은 의미 구조인지 아직 재검증이 필요하다.

---

## 7. reusable institution 후보

1. `structured doc routing + receipt`
   - 문서를 처리 가능한 사건으로 바꾸고 흔적을 남기는 기관
2. `fragment + provenance + canonical binding`
   - 원문 조각을 값 언어와 추적 가능한 기록으로 바꾸는 기관
3. `canonical-better upgrade`
   - provisional을 버리지 않고 더 좋은 binding으로 승격시키는 기관

이 셋은 이미 기관에 가깝다.

---

## 8. 이번 턴 판정

- 판정: `부분 전진 + 일반화 검증 가능`

이유:

- `choi_ai_classroom_vlm`에서는 saved_connection canonical loop가 실제로 닫혔다.
- `structured doc routing + receipt`는 이미 반복 가능한 기관이다.
- `claude_code_index`에서는 풍부한 signal과 blocker 유지 방식이 확인됐다.

하지만 아직 바로 일반화 검증으로 넓히면 안 되는 부분이 있다.

- active asset canonical onboarding은 다른 asset raw shape에도 먹히는지 확인이 더 필요하다.
- explore/query 쪽은 여전히 asset-local query 성격이 강하다.
- 2차 기관(question-inducing / role-like / pivot-compression)은 아직 scaffold 의존적이다.

즉 다음 단계는 “다 됐다”가 아니라,
이미 기관인 것과 아직 기관이 아닌 것을 분리한 채
일반화 검증을 더 좁혀서 들어가야 한다.

---

## 9. supervisor-judgment-ready record

이번 판독이 다음 단계에 필요한 이유:

- 지금 공간 안에서 이미 작동하는 기관과 아직 태도 수준에 머무는 것을 분리했기 때문이다.
- 따라서 다음 지시는 “새 기능 추가”가 아니라,
  - 이미 기관인 것을 다른 asset에 cross-check 할지
  - 아직 기관이 아닌 것을 더 다질지
  둘 중 하나로 좁힐 수 있다.

이번에 읽힌 것:

- active asset reread + canonical binding + saved_connection upgrade
- structured doc routing + receipt lineage
- probe/counting + blocker integration + 태도/기관 분리

이번에 아직 불충분한 것:

- active asset 전반 canonical onboarding cross-check
- explore의 wider queryability
- 1차 의미 단위의 충분성
- 2차 기관의 non-scaffold recurrence

다음 턴에서 먼저 cross-check 해야 할 것:

- `active asset canonical onboarding`을 다른 active asset 1~2개에 적용해,
  현재 성공이 특정 자산 특례인지 reusable path인지 확인할 것

---

## 10. one-line summary

> 이번 교차 판독에서 확인된 것은, 이 공간 안에는 이미 `receipt`, `fragment`, `canonical binding`, `saved_connection upgrade` 같은 기관이 실제로 형성되어 있지만, `question-inducing candidate`, `robust role-like reading`, `wider explore queryability`는 아직 scaffold 의존적인 태도 수준에 머물러 있다는 점이다.
