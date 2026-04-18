# folder_tree_duplicate_review_v1

이 문서는 현재 폴더 트리를 다시 점검한 결과,
무엇이 **정상 분리**이고 무엇이 **실제 정리 대상**인지 정리한 리뷰 문서다.

## 1. 최상위 판정

현재 트리는 겉보기보다 중복이 많아 보이지만,
실제 중복은 두 종류로 나뉜다.

### A. 정상 분리
같은 이름이나 비슷한 내용이 보여도 역할이 다른 경우

예:
- `source asset`
- `docs/examples`
- `runtime/observer`
- `runtime/contracts`

이건 같은 내용을 여러 군데 저장한 것이 아니라,
입력 / 설명 / 관측 / 판독 결과를 분리해 둔 것이다.

### B. 실제 정리 대상
정리해도 추적성이 흔들리지 않거나, 단순 잡파일인 경우

예:
- `.DS_Store`
- 의미 불명 임시 파일
- 이미 `source_assets/` 로 옮겼지만 루트에서는 anchor만 남겨도 되는 문서

## 2. 이번 점검에서 확인한 것

### root md count
- 루트 `md` 는 32개로 보인다.
- 하지만 이 중 일부는 실제 본문이 아니라 `root symlink anchor` 다.

### root symlink anchor
아래 파일들은 루트에 보이지만 실제 본문은 `source_assets/` 아래에 있다.

- [codex_summary_today_session_close_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_summary_today_session_close_v1.md)
- [external_case_first_pass_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_v1.md)
- [external_case_first_pass_saltlux_raw_transcript_input_v2.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_saltlux_raw_transcript_input_v2.md)
- [external_case_first_pass_saltlux_secondary_summary_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_saltlux_secondary_summary_input_v1.md)
- [external_case_first_pass_aifrontier_01_28_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_aifrontier_01_28_input_v1.md)
- [external_case_first_pass_oh_my_opencode_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_oh_my_opencode_input_v1.md)
- [external_case_first_pass_enterprise_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_enterprise_input_v1.md)

즉 이건 “진짜 중복”이 아니라,
기존 source_ref 안정성을 위한 anchor 구조다.

## 3. 이번에 실제 정리한 것

### A. `.DS_Store` 제거
- repo 전반의 `.DS_Store` 파일을 제거했다.
- 이건 의미 없는 잡파일이므로 중복이 아니라 정리 대상이었다.

### B. 의미 불명 임시 파일 정리
- 기존 [inputs/1.md](/Users/sungsookim/universe/vectorfl_replica/inputs/1.md) 는
  현재 엔진 입력함에 두기엔 부적절했다.
- 실제 성격은 다른 작업공간용 Codex 지시서 초안에 가까워서
  [tank_process_md_extraction_v2.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/legacy_misc/tank_process_md_extraction_v2.md)
  로 옮겼다.

## 4. 지금 정상으로 봐야 하는 구조

### source_assets vs root anchor
- 정상

### docs/examples vs runtime/observer vs runtime/contracts
- 정상

### folder_status.md 다수 존재
- 정상
- change log / inventory / render 구조에서 render 면이 폴더마다 있기 때문

## 5. 아직 남은 실제 정리 대상

### A. 루트 canonical source asset 본문
아직 루트에 실제 본문으로 남아 있는 declaration / baseline / directive / handoff / reference 문서가 있다.

이건 지금 당장 오류는 아니지만,
다음 migration batch 에서 아래처럼 더 정리할 수 있다.

- declaration -> `source_assets/declarations/`
- baseline -> `source_assets/baselines/`
- directive -> `source_assets/directives/`
- handoff -> `source_assets/handoffs/`

### B. reference_or_interpretation 계열
아래는 아직 루트에 남아 있지만,
지금 당장 이동하기보다 마지막 정리 단계에서 다루는 것이 안전하다.

- [vectorfl_philosophical_interpretation_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_philosophical_interpretation_v1.md)
- [tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md](/Users/sungsookim/universe/vectorfl_replica/tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md)
- [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)

## 6. 현재 최종 판정

현재 트리는 “생각보다 중복이 많다”기보다,
아래가 같이 보여서 복잡해 보이는 상태다.

- 정상적인 역할 분리
- root symlink anchor
- 아직 다음 migration batch 를 기다리는 canonical asset

즉 지금 기준으로는
`잡파일 정리` 는 한 번 닫혔고,
다음은 `canonical source asset 2차 이동` 이 핵심 정리 작업이다.
