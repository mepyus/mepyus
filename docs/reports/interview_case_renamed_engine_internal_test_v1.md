# interview case renamed engine internal test result

## 1. test setup
- original sources:
  - [dario_amodei_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/dario_amodei_youtube.txt)
  - [andrej_karpathy_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_youtube.txt)
  - [alexkarp_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/alexkarp_youtube.txt)
- renamed variants:
  - [interview_case_alpha.txt](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/interview_support/middle_layer_experiments/input_variants/interview_case_alpha.txt)
  - [interview_case_beta.txt](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/interview_support/middle_layer_experiments/input_variants/interview_case_beta.txt)
  - [interview_case_gamma.txt](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/interview_support/middle_layer_experiments/input_variants/interview_case_gamma.txt)

## 2. executed probes
- raw engine-only probe:
  - [interview_case_variants_raw_probe_20260328.json](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/interview_support/middle_layer_experiments/generated/interview_case_variants_raw_probe_20260328.json)
- middle-layer probe:
  - [middle_layer_interview_probe_20260327T231007Z.json](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/interview_support/middle_layer_experiments/generated/middle_layer_interview_probe_20260327T231007Z.json)

## 3. raw path read
- alpha:
  - dominant scene/flow stayed `review / compare`
  - top anchors still included generic discourse such as `우리가`, `당신이`, `있습니다`
- beta:
  - dominant scene/flow stayed `review / compare`
  - some topic term appeared (`LRM`) but flattening remained
- gamma:
  - dominant scene/flow stayed `review / compare`
  - generic discourse anchors still dominated the top list

### raw summary
- 이름을 바꿔도 raw path는 여전히 형식 공통성 쪽으로 눌리고,
  인터뷰 3건을 case-specific frame으로 분화시키지 못했다.

## 4. middle-layer read
- alpha:
  - dominant roles:
    - `mechanism_role`
    - `verification_or_evaluation_role`
- beta:
  - dominant roles:
    - `reflection_or_gap_role`
    - `problem_or_constraint_role`
- gamma:
  - dominant roles:
    - `problem_or_constraint_role`
    - `control_or_deployment_role`

### middle-layer summary
- 이름 힌트를 줄여도 middle-layer packet은 기존과 거의 같은 dominant role mix를 유지했다.
- 즉 현재 분화는 파일명보다 내용 기반 signal과 role resolution에 더 기대고 있다고 읽는 것이 맞다.

## 5. interpretation
- raw-only path:
  - still name-insensitive in a bad way
  - because it flattens all three into generic discourse and `review / compare`
- middle-layer path:
  - name-insensitive in a useful way
  - because it keeps case-specific role divergence even after the file names are neutralized

## 6. verification
- manual first-pass added: NO
- canonical originals untouched: YES
- work-only renamed variants used: YES
- raw flattening still visible: YES
- middle-layer role divergence retained: YES
- current asset map updated: NO

## 7. result
- status: PASS_WITH_NOTE

## 8. one-line summary
- 이름 힌트를 줄인 뒤에도 raw path는 그대로 평평했고, middle-layer는 여전히 Dario/Andrej/Alex에 대응하는 role mix를 유지해서 현재 분화가 파일명보다 내용 신호에 더 기대고 있음을 보여줬다.
