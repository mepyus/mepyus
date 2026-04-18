# vectorfl internal recall evidence bundles v0

## purpose

이 문서는 내부 읽기 사례집 다음 단계로,
spec와 generated artifact를 함께 묶어
실제로 Paper에서 보여줄 수 있는
`line recall evidence bundle` 초안을 남긴다.

핵심은
spec만 읽고 만든 교리적 해석이 아니라,
generated 결과까지 따라가며
어떤 판단이 실제 evidence를 갖는지 분리하는 것이다.

---

## bundle_01_raw_intake_middle_layer_gap

### source set
- `docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md`
- `runtime/receipts/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_operation_receipt.md`
- `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `runtime/views/multi_lens_document_reading/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_multi_lens_readout_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`

### raw first reading
- raw intake weakness를 middle-layer 부재 문제로 본 보고서와,
  그 뒤에 실제로 남은 receipt/GMD/multi-lens artifact를 한 묶음으로 읽는다.

### evidence actually present
- 보고서는 `topic-bearing signal을 provisional case structure로 올리지 못한다`고 진단한다.
- receipt는 GMD native read가 실제로 기록되었고
  `segmentation_basis`, `ordering_basis`, `semantic commentary`, `translation-ready material`이 생겼다고 보여준다.
- GMD json은 role hint와 relation clue를 실제로 남긴다.
- multi-lens readout은 linked segments와 linkage reason을 남긴다.

### what this bundle lets me confidently say
- intake는 이제 단순 split만 남기지 않고
  line 이전의 번역 재료를 남기기 시작했다.
- 다만 아직 final line 완성이나 deep recall까지는 아니다.

### what remains weak
- GMD 결과의 unresolved count가 `0`이라
  uncertainty retention은 아직 약해 보인다.
- multi-lens readout의 linkage reason이 거의 `unfinished_claim` 중심이라
  relation 다양성이 충분한지 아직 약하다.

### paper-ready translation
- 자료가 들어오면 곧바로 line을 잠그는 게 아니라,
  먼저 원본 구조와 연결 단서를 남겨서
  나중에 line을 다시 해석할 수 있게 만드는 묶음이다.

### why it matters for vectorfl paper
- `작업 상세`의 왼쪽 source read,
  가운데 line 후보,
  오른쪽 inspector recall을 연결하는 첫 실제 bundle이다.

---

## bundle_02_reentry_survival_without_promotion

### source set
- `app/work/mixed_reentry_probe_stage1/mixed_reentry_probe_stage1_spec.md`
- `app/work/mixed_reentry_observer_stage2/mixed_reentry_observer_stage2_spec.md`
- `app/work/mixed_reentry_observer_stage2/generated/corridor_ledger_stage2.json`
- `app/work/mixed_reentry_observer_stage2/generated/corridor_strength_trend_report.json`
- `app/work/mixed_reentry_observer_stage2/generated/corridor_survivor_cards.md`

### raw first reading
- mixed hold corridor가 후속 입력에서 실제로 살아남는지를
  spec와 generated ledger로 같이 읽는 bundle이다.

### evidence actually present
- stage1은 re-entry candidate / match / strength / closure delta 정의를 잠근다.
- stage2 ledger는 세 corridor 모두 reentry_count와 latest_closure_state를 남긴다.
- strength trend report는 세 corridor 모두 `strong_reentry_but_still_hold`로 읽는다.
- survivor cards는 strongest reentry와 왜 아직 canonical이 아닌지를 md 카드로 남긴다.

### what this bundle lets me confidently say
- mixed hold는 진짜로 dead-end가 아니라 re-entry 가능한 corridor다.
- reinforcement가 생겨도 stable closure가 없으면 canonical promotion은 아니다.

### what remains weak
- observer evidence가 왜 uneven한지,
  어떤 matched input이 정확히 어떤 arrival axis를 강화했는지는 추가 compare가 더 필요하다.
- initial_hold_reason 문구가 business/organization corridor에 동일하게 남는 부분은
  artifact wording quality 보강이 필요해 보인다.

### paper-ready translation
- 어떤 line이나 corridor는 다시 살아난다.
  하지만 다시 살아났다는 사실과 닫혔다는 사실은 다르다.

### why it matters for vectorfl paper
- `흔적 감사`와 `line 들여다보기`에서
  `다시 붙었음`과 `승격됨`을 분리해서 보여주는 핵심 bundle이다.

---

## bundle_03_meaning_vs_format_disentangle

### source set
- `app/work/mixed_corridor_format_disentangle_stage4/mixed_corridor_format_disentangle_stage4_spec.md`
- `app/work/mixed_corridor_format_disentangle_stage4/generated/corridor_disentangle_ledger.json`
- `app/work/mixed_corridor_format_disentangle_stage4/generated/meaning_vs_format_cards.md`
- `app/work/mixed_corridor_format_disentangle_stage4/generated/format_disentangle_decision_note.md`

### raw first reading
- strongest corridor가 진짜 meaning 때문인지,
  format/source-family echo가 일부 밀어주는지를 분리하는 관찰 묶음이다.

### evidence actually present
- stage4 spec는 judgment를 `meaning_driven / format_assisted / family_assisted / format_noisy / unclear`로 분리한다.
- ledger는
  `technical->business::ai_business = format_noisy`
  `technical->organization::* = mostly_meaning_driven`
  를 실제로 기록한다.
- decision note는 cleaner corridor와 noisier corridor를 구분한다.

### what this bundle lets me confidently say
- לפחות 두 corridor는 mostly meaning-driven 쪽으로 읽힌다.
- business corridor는 여전히 noisy focus다.
- disentangle는 confidence를 올리지만 stable closure를 만들지는 않는다.

### what remains weak
- `same_format_different_meaning_response = meaningful / corridor_specific_reentry / unclear` 같은 항목은
  아직 why unclear인지 더 세부 근거가 필요하다.
- family bias risk가 medium으로 남는 이유를 더 세분화한 artifact가 추가로 필요하다.

### paper-ready translation
- 비슷하게 보인다고 다 같은 의미는 아니다.
  어떤 연결은 진짜 뜻 때문에 붙고,
  어떤 연결은 형식 echo 때문에 붙는다.

### why it matters for vectorfl paper
- `line 비교`, `내부 자료 다시 보기`에서
  meaning-driven vs format-noisy를 분리해서 보여줄 수 있어야 한다.

---

## bundle_04_business_corridor_subaxis_mix

### source set
- `app/work/technical_business_corridor_decompose_stage5/technical_business_corridor_decompose_stage5_spec.md`
- `app/work/technical_business_corridor_decompose_stage5/generated/business_corridor_decomposition_ledger.json`
- `app/work/technical_business_corridor_decompose_stage5/generated/business_corridor_decision_note.md`

### raw first reading
- business corridor 하나로 뭉쳐 보이는 흐름 안에
  실제로는 어떤 하위 arrival axis가 섞여 있는지 observer layer에서 좁혀보는 bundle이다.

### evidence actually present
- spec는 sub-axis 후보를 5개 제시한다.
- decomposition ledger는
  `strongest_axis = startup_thesis`
  `secondary_axes = monetization_value_capture, org_business_boundary`
  `current_reading = multi_axis_business_mix`
  로 남긴다.
- decision note는 noise 주원인을
  `axis 혼합 + format/family noise의 혼합`
  으로 읽는다.

### what this bundle lets me confidently say
- `technical->business::ai_business`는 단일 corridor로만 보기엔 너무 평평하다.
- observer layer에서는 split 후보를 유지하는 편이 더 정확하다.

### what remains weak
- axis별 match report 전체를 아직 다 읽지 않았기 때문에
  strongest/secondary 분포가 얼마나 안정적인지는 더 봐야 한다.

### paper-ready translation
- business로 보이는 line도 실제론
  startup, monetization, 조직경계 같은 여러 축이 섞여 움직일 수 있다.

### why it matters for vectorfl paper
- `외부 자료 계획`, `lane 비교 결과`, `팀 관리`에서
  business를 한 덩어리 값처럼 넘기지 않게 만드는 근거 bundle이다.

---

## bundle_05_visible_split_to_recall_surface

### source set
- `app/work/observer_ingest_min/observer_ingest_min_spec.md`
- `app/work/observer_ingest_min/generated/operator_summary_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`
- `app/work/observer_ingest_min/generated/readable_input_board_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`
- `runtime/views/multi_lens_document_reading/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_multi_lens_readout_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`

### raw first reading
- 얇은 visible split sidecar가
  어디까지 사람과 다음 layer를 도울 수 있는지 보는 bundle이다.

### evidence actually present
- operator summary는 input kind, split mode, 흐름 앞/중간/뒤를 한 장으로 요약한다.
- readable input board는 15 heading block을 실제 unit 목록으로 보여준다.
- multi-lens readout은 몇 개 unit이 unfinished claim 기준으로 다시 묶였는지 보여준다.

### what this bundle lets me confidently say
- 최소한 지금 intake는
  `입력 인식 -> unit 분해 -> 사람이 볼 수 있는 board -> linked segment`
  까지는 간다.

### what remains weak
- 아직 linked segment의 semantic class가 다양하지 않다.
- operator summary는 친화적이지만,
  why-this-unit-matters 수준의 richer gloss는 더 필요하다.

### paper-ready translation
- 원본이 어떻게 잘렸는지와
  어떤 부분이 같이 봐야 하는지 정도는
  이미 한 장에 보여줄 수 있다.

### why it matters for vectorfl paper
- `자료 목록`과 `작업 상세` 왼쪽 panel의 최소 usable surface가 된다.

---

## bundle synthesis

### what improved
- 이제 internal reading이 spec-only가 아니라
  generated evidence까지 붙은 bundle로 내려왔다.
- `mixed hold`, `meaning vs format`, `business sub-axis`, `intake middle-layer`
  같은 핵심 주제들이 실제 artifact 근거를 갖기 시작했다.

### what still needs hardening
- multi-lens readout에서 linkage diversity가 충분한지 더 확인해야 한다.

### next step
- 이 bundle 5개를 바탕으로
  Paper의 `작업 상세 / line 들여다보기 / 내부 자료 다시 보기 / 외부 자료 계획`
  에 들어갈 evidence blocks를 실제 payload 구조로 다시 내린다.

---

## bundle_06_boundary_specificity_without_closure

### source set
- `app/work/mixed_corridor_boundary_probe_stage3/mixed_corridor_boundary_probe_stage3_spec.md`
- `app/work/mixed_corridor_boundary_probe_stage3/generated/boundary_corridor_specificity_ledger.json`
- `app/work/mixed_corridor_boundary_probe_stage3/generated/boundary_probe_group_comparison.json`
- `app/work/mixed_corridor_boundary_probe_stage3/generated/boundary_probe_decision_note.md`
- `app/work/mixed_corridor_boundary_probe_stage3/generated/boundary_survivor_cards.md`

### raw first reading
- reinforcing / adjacent / off-axis 입력을 분리해서,
  corridor가 진짜 specific한지 아니면 broad resonance인지 다시 누르는 bundle이다.

### evidence actually present
- group comparison은 reinforcing / adjacent / off_axis가 실제로 다른 양상으로 갈린다고 남긴다.
- specificity ledger는 3개 corridor 모두 `specific`으로 읽히지만 `promotion_readiness = still_observe`를 유지한다.
- survivor cards는 `why_still_not_canonical`를 직접 적어 둔다.
- decision note는 `specificity is not closure`를 명시한다.

### what this bundle lets me confidently say
- 일부 mixed corridor는 단순 broad resonance가 아니라 boundary challenge에서도 specificity를 유지한다.
- 그렇더라도 stable closure가 반복되지 않으면 여전히 observer-only다.

### what remains weak
- 아직 negative-control을 더 늘려야 한다.
- specificity가 유지되는 이유가 arrival axis 차원에서 얼마나 안정적인지 추가 반복이 더 필요하다.

### paper-ready translation
- 어떤 corridor는 경계 시험에서도 살아남는다.
  하지만 살아남는 것과 닫히는 것은 다르다.

### why it matters for vectorfl paper
- `흔적 감사`, `넘김과 배정`, `line 들여다보기`에서
  specificity와 closure를 분리해서 보여주는 핵심 bundle이다.

---

## bundle_07_axis_stability_distribution

### source set
- `app/work/technical_business_corridor_decompose_stage5/generated/business_corridor_match_report.json`
- `app/work/technical_business_corridor_decompose_stage5/generated/business_axis_group_comparison.json`
- `app/work/technical_business_corridor_decompose_stage5/generated/business_corridor_readable_cards.md`
- `app/work/technical_business_corridor_decompose_stage5/generated/business_corridor_noise_watch.md`

### raw first reading
- business corridor를 축별로 다시 나눴을 때,
  어떤 axis는 안정적으로 붙고 어떤 axis는 noise가 강한지 비교하는 bundle이다.

### evidence actually present
- match report는 `monetization_value_capture`, `startup_thesis`, `org_business_boundary`에서 strong axis-specific reentry를 보여준다.
- 반면 `software_value_shift`는 `bridge_partial_echo / unclear` 또는 `format_noisy` 쪽으로 기운다.
- axis group comparison은 축별 tested_count / strong_count / dominant judgment를 요약한다.

### what this bundle lets me confidently say
- business corridor 안에서도 axis별 안정도 차이가 크다.
- startup_thesis는 strong하지만 multi-axis mix가 남고,
  software_value_shift는 아직 noise가 더 많다.

### what remains weak
- readable cards와 noise watch를 더 깊게 읽어
  왜 특정 축이 noise에 더 취약한지 설명을 두껍게 해야 한다.

### paper-ready translation
- business처럼 한 덩어리로 보이는 흐름도,
  실제로는 어떤 축은 비교적 안정적이고 어떤 축은 아직 noise가 더 크다.

### why it matters for vectorfl paper
- `외부 자료 계획`, `lane 비교 결과`, `넘김과 배정`에서
  business를 한 값으로 보내지 않고,
  axis별로 다른 태도를 취하게 만드는 근거 bundle이다.
