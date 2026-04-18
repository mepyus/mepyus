# vectorfl internal reading casebook v0

## purpose

이 문서는 내부 공간을 다시 읽으면서
내가 실제로 무엇을 인식하는지,
어디서부터 추정이 들어가는지,
어디가 아직 blindness로 남는지
12개 사례로 기록한다.

순서는 `baseline-memory -> staged corridor -> utility-sidecar`를 따른다.

---

## case_01_work_map_entry

### source_materials
- `app/work/folder_status.md`
- `app/work/work_maturity_map_v0.md`

### raw_first_reading
- `app/work/` 전체를 하나의 실험장으로 읽지 말고,
  기준선, 단계형 probe, 보조 sidecar를 분리해서 읽으라는 entrypoint다.

### what_i_can_confidently_recognize
- `current_layer_baseline`는 가장 먼저 읽어야 하는 baseline-memory다.
- stage1~stage5 corridor는 lineage로 읽어야 한다.
- `observer_ingest_min`, `operating_ui`, `processor_compare`는 utility-sidecar다.

### what_i_am_inferring
- 이후 많은 drift가 생긴 이유 중 하나는
  이 상위 maturity map을 계속 기준선으로 쓰지 않았기 때문이라고 추정된다.

### what_i_still_cannot_read
- 각 utility-sidecar가 실제로 얼마나 성숙했는지는
  여기만 읽어서는 모른다.

### linked_status_or_generated_artifacts
- `app/work/current_layer_baseline/folder_status.md`
- `app/work/observer_ingest_min/folder_status.md`

### why_it_matters_for_vectorfl_paper
- Paper가 내부를 읽을 때도
  폴더를 같은 위상으로 보여주면 안 되고
  baseline / staged lineage / sidecar를 구분해야 한다.

### next_verification_or_recall
- baseline-memory를 먼저 읽고
  그 다음 staged corridor를 lineage로 내려간다.

### recognition_level
- `clear`

---

## case_02_baseline_entry

### source_materials
- `app/work/current_layer_baseline/folder_status.md`

### raw_first_reading
- 이 폴더는 일반 실험 폴더가 아니라
  현재 엔진 철학과 운영 계약을 고정하는 헌법 entry다.

### what_i_can_confidently_recognize
- reading order가 명시돼 있다.
- `engine_philosophy_declaration_v1.md`
- `current_layer_baseline_contract_v1.md`
- `reference_sheet_officeout_v1.md`

### what_i_am_inferring
- 이후 surface나 lane을 설계할 때도
  이 폴더를 먼저 통과하지 않으면
  current-reading, mixed hold, promotion 금지 규칙이 흔들릴 가능성이 크다.

### what_i_still_cannot_read
- `reference_sheet_officeout_v1.md`의 실제 역할은 아직 이 case에서는 읽지 않았다.

### linked_status_or_generated_artifacts
- `app/work/current_layer_baseline/engine_philosophy_declaration_v1.md`
- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

### why_it_matters_for_vectorfl_paper
- Paper의 list/detail/audit가 아무리 좋아도
  mixed를 어떻게 보여줄지에 대한 기준은 여기서 나온다.

### next_verification_or_recall
- baseline 두 핵심 문서를 실제로 읽고
  `mixed hold`, `observer-first`, `promotion 금지`를 비교 기록한다.

### recognition_level
- `usable`

---

## case_03_engine_philosophy

### source_materials
- `app/work/current_layer_baseline/engine_philosophy_declaration_v1.md`

### raw_first_reading
- 이 문서는 VectorFL가 정답 생산기가 아니라
  위치값을 만들고 숙성시키는 엔진이라는 헌법을 선언한다.

### what_i_can_confidently_recognize
- 우선순위는 `위치 -> 반복 -> 방향 -> 숙성 -> 정합성`이다.
- mixed는 실패가 아니라 productive hold다.
- 공간은 결과 저장소가 아니라 흐름을 다시 만나게 하는 장이다.
- 출력값은 결론이 아니라 다음 행동의 씨앗이다.

### what_i_am_inferring
- line도 결국 완성 문장이 아니라
  위치값과 행동 원형의 중간 단위로 읽어야 한다는 해석이 자연스럽다.

### what_i_still_cannot_read
- 이 철학이 실제 intake, lane, audit 코드에 얼마나 일관되게 반영돼 있는지는
  이 선언문만으로는 판단할 수 없다.

### linked_status_or_generated_artifacts
- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`
- `docs/reports/line_generation_vs_extraction_boundary_validation_v0.md`

### why_it_matters_for_vectorfl_paper
- Paper는 `정답 보여주기 UI`가 아니라
  hold, re-entry, 숙성, 다음 행동을 같이 보여주는 운영면이어야 한다.

### next_verification_or_recall
- line review와 inspector가
  이 철학을 실제로 반영하는지 대조한다.

### recognition_level
- `clear`

---

## case_04_current_layer_contract

### source_materials
- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

### raw_first_reading
- 이 문서는 현재 레이어가 무엇을 해도 되고 무엇은 하면 안 되는지 잠근 운영 계약이다.

### what_i_can_confidently_recognize
- 현재 레이어 역할은 `조기 폐기 방지 + hold 이유 기록 + 재진입 가능성 보존 + observer-first 운영`이다.
- `bridge 없음 -> unreadable`, `bridge 있음 + stable closure 없음 -> mixed`, `bridge 있음 + stable closure 도달 -> canonical`.
- mixed 카드는 최소
  `transition_from`, `transition_to`, `hold_reason`, `bridge fragments`, `closure_gap`, `why_not_canonical`
  을 보여야 한다.
- promotion 논의는 금지다.

### what_i_am_inferring
- Paper의 `작업 상세`, `넘김과 배정`, `흔적 감사`는
  이 계약을 중심으로 재배치되어야 한다.

### what_i_still_cannot_read
- 실제 generated mixed cards가 이 최소 계약을 어디까지 만족하는지는 별도 출력 확인이 더 필요하다.

### linked_status_or_generated_artifacts
- `app/work/mixed_reentry_probe_stage1/mixed_reentry_probe_stage1_spec.md`
- `app/work/mixed_corridor_format_disentangle_stage4/generated/corridor_disentangle_ledger.json`

### why_it_matters_for_vectorfl_paper
- right inspector와 routing surface가 어떤 항목을 보여야 하는지의 기준이 된다.

### next_verification_or_recall
- staged corridor 사례들과 연결해
  contract가 실제로 보존되는지 확인한다.

### recognition_level
- `clear`

---

## case_05_observer_ingest_min

### source_materials
- `app/work/observer_ingest_min/folder_status.md`
- `app/work/observer_ingest_min/observer_ingest_min_spec.md`

### raw_first_reading
- 이 경로는 깊은 판독 엔진이 아니라
  입력을 쉽게 넣고 어떻게 나뉘었는지 빠르게 확인하는 얇은 ingest sidecar다.

### what_i_can_confidently_recognize
- 목적은 `easy ingest + visible split + readable trace`다.
- canonical/mixed 판독, bridge admission, corridor 분석은 비목표다.
- split 우선순위는 `timestamp -> heading -> paragraph`.

### what_i_am_inferring
- 이 경로를 코어 판독기로 오해하면
  line meaning이 빈약해지는 drift가 다시 생긴다.

### what_i_still_cannot_read
- 실제 generated 결과가 사람이 얼마나 잘 읽히는지는 output sample을 봐야 한다.

### linked_status_or_generated_artifacts
- `app/work/observer_ingest_min/generated/folder_status.md`
- `app/work/observer_ingest_min/generated/operator_summary_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`
- `app/work/observer_ingest_min/generated/readable_input_board_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`

### why_it_matters_for_vectorfl_paper
- Paper의 source panel은 이 sidecar 출력과 잘 맞아야 한다.
- 다만 여기서 line meaning까지 끝난 것처럼 보이면 안 된다.

### next_verification_or_recall
- operator summary와 readable board를 사례로 읽어
  visible split이 어디까지 충분한지 본다.

### recognition_level
- `usable`

---

## case_06_raw_intake_gap_analysis

### source_materials
- `docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md`

### raw_first_reading
- structured path, external case path, raw engine-only path를 비교해
  raw intake가 왜 빈약한지 middle-layer 관점에서 진단한 보고서다.

### what_i_can_confidently_recognize
- 문제는 noisy anchors만이 아니다.
- 더 깊은 문제는 topic-bearing signal이 provisional case structure로 올라가지 않는다는 점이다.
- missing middle-layer functions로
  `generic discourse suppression`, `source-type aware normalization`, `case-level aggregation`, `provisional frame sketching`, `compare-ready packaging`
  이 제시된다.

### what_i_am_inferring
- GMD를 intake에 붙인 이유가 바로 이 missing middle-layer를 일부 메우기 위한 것이라고 읽힌다.

### what_i_still_cannot_read
- 여기서 제안한 middle-layer가 실제로 얼마나 구현됐는지는 후속 generated artifact를 봐야 한다.

### linked_status_or_generated_artifacts
- `runtime/receipts/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_operation_receipt.md`
- `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`

### why_it_matters_for_vectorfl_paper
- `작업 상세` 좌측 source read와 중앙 line 생성 사이에
  왜 native structure 설명이 들어가야 하는지 설명해 준다.

### next_verification_or_recall
- GMD native read output이 이 보고서의 요구를 실제로 얼마나 반영하는지 대조한다.

### recognition_level
- `clear`

---

## case_07_receipt_as_contract_evidence

### source_materials
- `runtime/receipts/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_operation_receipt.md`

### raw_first_reading
- structured intake가 실제로 어떤 산출물과 어떤 GMD read 결과를 남겼는지 확인하는 receipt다.

### what_i_can_confidently_recognize
- `gmd_native_read_written` 이벤트가 실제로 append됐다.
- GMD native read가
  `segmentation_basis`, `ordering_basis`, `grouping_logic`, `role_hint_count`, `relation_clue_count`, `semantic commentary`, `translation-ready material`
  을 남긴다.
- provisional line block count는 `8`이다.

### what_i_am_inferring
- 최소한 현재 intake는
  “왜 이렇게 나뉘는지”를 남기기 시작했고,
  Paper에서 `원본 읽기 -> line 이전 재료`를 보여줄 수 있는 상태다.

### what_i_still_cannot_read
- relation clues와 provisional line block의 품질은 receipt만으로는 판단하기 어렵다.

### linked_status_or_generated_artifacts
- `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`

### why_it_matters_for_vectorfl_paper
- Paper에 `source-backed recall`을 넣을 때
  receipt는 line의 출생 증거와 provenance surface가 된다.

### next_verification_or_recall
- 실제 gmd json을 읽어
  role / relation / provisional line의 질을 본다.

### recognition_level
- `usable`

---

## case_08_gmd_native_read_output

### source_materials
- `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`

### raw_first_reading
- 이 파일은 원본을 바로 VectorFL line으로 환원하지 않고,
  native structure와 translation-ready material을 남기는 중간 산출물이다.

### what_i_can_confidently_recognize
- ordering basis는 `input_to_processing_to_result`다.
- role hints는 `context`, `adoption`, `contrast`, `handoff`, `principle` 같은 역할을 준다.
- relation clues는 `follows`, `contrasted_by`, `routes_to`, `grounds` 같은 관계를 준다.
- semantic commentary가 line 이전의 사람말 설명층 역할을 한다.

### what_i_am_inferring
- line이 태어날 때 역할과 관계를 함께 들고 나오게 하려면
  이 중간 산출물을 더 중심에 놓아야 한다.

### what_i_still_cannot_read
- 아직 unresolved count가 `0`이라
  uncertainty retention이 실제로 충분한지는 의심이 남는다.

### linked_status_or_generated_artifacts
- `app/work/observer_ingest_min/generated/operator_summary_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`
- `app/work/observer_ingest_min/generated/readable_input_board_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`

### why_it_matters_for_vectorfl_paper
- `작업 상세` 왼쪽 source read와 오른쪽 inspector recall 사이를 잇는 핵심 원재료다.

### next_verification_or_recall
- 다른 source에도 GMD native read를 적용해
  role/relation 품질이 유지되는지 봐야 한다.

### recognition_level
- `usable`

---

## case_09_stage1_reentry_probe

### source_materials
- `app/work/mixed_reentry_probe_stage1/mixed_reentry_probe_stage1_spec.md`

### raw_first_reading
- mixed corridor가 후속 입력에서 다시 붙는지 read-only로 검증하는 첫 단계 spec이다.

### what_i_can_confidently_recognize
- re-entry candidate와 re-entry match가 명시돼 있다.
- strength 단계와 closure delta 단계가 분리돼 있다.
- 성공 조건은 hold 가치 증명이지 승격이 아니다.

### what_i_am_inferring
- 이 spec는 VectorFL가 mixed를 dead-end가 아니라 관찰 가능한 자산으로 다루는 핵심 예시다.

### what_i_still_cannot_read
- 실제 generated probe 결과에서 어떤 corridor가 meaningful/strong이었는지는 이 spec만으로는 모른다.

### linked_status_or_generated_artifacts
- `app/work/mixed_reentry_observer_stage2/mixed_reentry_observer_stage2_spec.md`

### why_it_matters_for_vectorfl_paper
- `흔적 감사`와 `line 들여다보기`에서
  “다시 붙는 값”을 어떻게 보여줄지의 기준이 된다.

### next_verification_or_recall
- stage2와 같이 읽어 누적 ledger 관점으로 넘어간다.

### recognition_level
- `usable`

---

## case_10_stage2_reentry_accumulation

### source_materials
- `app/work/mixed_reentry_observer_stage2/mixed_reentry_observer_stage2_spec.md`

### raw_first_reading
- stage1의 single re-entry probe를 corridor ledger 누적 관찰로 확장한 단계다.

### what_i_can_confidently_recognize
- corridor_id는 `transition_from -> transition_to :: anchor_group` 형식이다.
- 세 축을 본다:
  - `technical -> organization :: harness_agent`
  - `technical -> organization :: ai_business`
  - `technical -> business :: ai_business`
- 목적은 accumulation 확인이지 promotion이 아니다.

### what_i_am_inferring
- Paper의 `line family`나 `case lineage`도
  corridor_id 같은 명시적인 누적 키가 있어야 재현 가능해진다.

### what_i_still_cannot_read
- 실제 누적 강도의 차이는 generated ledger나 후속 stage를 봐야 한다.

### linked_status_or_generated_artifacts
- `app/work/mixed_corridor_format_disentangle_stage4/generated/corridor_disentangle_ledger.json`

### why_it_matters_for_vectorfl_paper
- `line 하나`보다 `재등장 corridor`를 보여주는 audit grammar가 필요하다는 근거가 된다.

### next_verification_or_recall
- stage4 ledger와 붙여 strong/weak corridor 차이를 읽는다.

### recognition_level
- `usable`

---

## case_11_stage4_meaning_vs_format

### source_materials
- `app/work/mixed_corridor_format_disentangle_stage4/mixed_corridor_format_disentangle_stage4_spec.md`
- `app/work/mixed_corridor_format_disentangle_stage4/generated/corridor_disentangle_ledger.json`

### raw_first_reading
- strongest corridor들이 진짜 meaning 때문에 붙는지,
  format/source-family 껍질이 일부 밀어주는지 observer layer에서 분리하는 단계다.

### what_i_can_confidently_recognize
- judgment는 `meaning_driven`, `format_assisted`, `family_assisted`, `format_noisy`, `unclear`로 구분된다.
- ledger 기준으로
  `technical->business::ai_business`는 `format_noisy`, `format_noise_risk=high`, `promotion_readiness=far_from_ready`다.
- `technical->organization::ai_business`, `technical->organization::harness_agent`는 `mostly_meaning_driven`이다.

### what_i_am_inferring
- 내가 내부를 읽을 때도
  “이건 진짜 의미를 본 것인지, 형식 echo를 읽은 것인지”를 분리 기록해야 한다.

### what_i_still_cannot_read
- stage3 boundary challenge를 직접 읽지 않아
  stage4가 무엇을 inherited 했는지 완전히는 모른다.

### linked_status_or_generated_artifacts
- `app/work/mixed_corridor_boundary_probe_stage3/folder_status.md`
- `app/work/technical_business_corridor_decompose_stage5/technical_business_corridor_decompose_stage5_spec.md`

### why_it_matters_for_vectorfl_paper
- Paper의 `내부 자료 다시 보기`와 `line 비교`는
  meaning-driven vs format-noisy를 같이 보여줄 수 있어야 한다.

### next_verification_or_recall
- stage5 분해로 넘어가
  noisy corridor 내부의 sub-axis 가능성을 본다.

### recognition_level
- `clear`

---

## case_12_stage5_business_axis_decompose

### source_materials
- `app/work/technical_business_corridor_decompose_stage5/technical_business_corridor_decompose_stage5_spec.md`

### raw_first_reading
- `technical->business::ai_business` corridor를
  business 내부 arrival axis 후보로 더 좁혀 보는 observer layer 분해 spec이다.

### what_i_can_confidently_recognize
- positive control은 organization corridors다.
- business 쪽 하위 후보는
  `business_leverage`, `monetization_value_capture`, `startup_thesis`, `org_business_boundary`, `software_value_shift`.
- 목적은 코어 분할이 아니라 observer split 후보 기록이다.

### what_i_am_inferring
- 현재 내가 내부를 읽으며 자꾸 `business`를 한 덩어리로 읽었다면
  실제론 여러 하위 축이 섞여 있는 noisy case를 평평하게 본 셈일 수 있다.

### what_i_still_cannot_read
- 각 하위 axis 후보가 실제로 얼마나 분리되는지는
  generated outputs 없이는 아직 모른다.

### linked_status_or_generated_artifacts
- `app/work/mixed_corridor_format_disentangle_stage4/generated/corridor_disentangle_ledger.json`
- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

### why_it_matters_for_vectorfl_paper
- `외부 자료 계획`, `lane 비교 결과`, `팀 관리`에서
  business를 한 덩어리로 넘기지 않고 sub-axis 후보를 보이게 해야 하는 이유가 된다.

### next_verification_or_recall
- stage5 generated outputs가 있는지 더 찾아보고
  axis별 반응 차이를 실제 사례로 추가해야 한다.

### recognition_level
- `partial`

---

## current synthesis

### what i can now say
- 내부 공간은 그냥 자료 저장소가 아니라
  baseline-memory, staged corridor, utility-sidecar로 위계가 나뉜다.
- baseline은 `위치값/숙성/hold/re-entry`를 보호한다.
- staged corridor는 `mixed hold`를 버리지 않고
  re-entry, specificity, meaning-vs-format, business sub-axis로 보수적으로 좁혀 간다.
- utility-sidecar는 깊은 판독이 아니라
  visible split, receipt, native structure 보존 같은 전처리와 보조 표면 역할을 한다.

### what i still fail to do well
- generated outputs를 많이 읽기 전에
  spec만 보고 too-early translation 하는 경향이 있다.
- format/noise와 meaning을 충분히 분리하지 못한 채 surface wording으로 넘기려는 경향이 있다.
- folder status를 entrypoint로는 잘 쓰지만
  generated ledger / receipt / readout까지 끝까지 따라가는 밀도가 아직 부족하다.

### why this matters
- 이 casebook이 없으면
  다음 세션마다 다시 surface만 다듬고 내부를 얕게 읽는 루프가 반복된다.
- 이 기록은 앞으로 내가 내부를 읽을 때의 recognition boundary를 기억으로 남기는 첫 보수 ledger다.
