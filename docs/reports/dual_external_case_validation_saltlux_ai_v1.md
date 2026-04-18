# dual external case validation result

## 1. test 1 — saltlux original + summary
- canonical input: [saltlux_ai.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/saltlux_ai.txt)
- secondary summary: [saltlux_ai_summary.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/saltlux_ai_summary.txt)
- canonical preserved: YES
- summary remained secondary: YES
- status: PASS_WITH_NOTE

## 2. test 2 — saltlux + ontology_youtube
- case A canonical input: [saltlux_ai.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/saltlux_ai.txt)
- case B canonical input: [ontology_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/ontology_youtube.txt)
- repeated outer frame detected: YES
- vendor-specific rhetoric separated: YES
- refinement candidate clarified: YES
- status: PASS_WITH_NOTE

## 3. created artifacts
- [dual_external_case_validation_instruction_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/dual_external_case_validation_instruction_v1.md)
- [saltlux_ai_summary_pair_validation_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/saltlux_ai_summary_pair_validation_input_v1.md)
- [saltlux_ai_vs_ontology_youtube_compare_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/saltlux_ai_vs_ontology_youtube_compare_input_v1.md)
- [external_case_summary_pair_validation_saltlux_ai_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_summary_pair_validation_saltlux_ai_v1.md)
- [external_case_compare_saltlux_ai_vs_ontology_youtube_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_compare_saltlux_ai_vs_ontology_youtube_v1.md)
- [dual_external_case_validation_saltlux_ai_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/dual_external_case_validation_saltlux_ai_v1.md)

## 4. surface updates
- current_asset_map_v1: NO
- repo_delta_log_latest_v1: YES

## 5. verification
- source hierarchy preserved: YES
- source vs derived separated: YES
- report vs evidence separated: YES
- repo-wide rewrite avoided: YES
- core touched: NO

## 6. one-line summary
- summary pair에서는 canonical-vs-secondary 경계가 유지됐고, ontology 비교에서는 vendor-specific rhetoric을 걷어낸 반복 outer frame이 더 선명해졌다.
