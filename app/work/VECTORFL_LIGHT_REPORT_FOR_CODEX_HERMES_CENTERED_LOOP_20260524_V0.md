# LIGHT REPORT FOR CODEX: HERMES-CENTERED VECTORFL LOOP

status: HOLD / reference-only
purpose: Codex가 현재 VectorFL 역할 분리를 빠르게 이해하고, 다음 retrieval pass를 쉽게 시작하도록 하는 경량 리포트.

## 핵심 정리

Hermes 역할을 축소하지 않는다.

Hermes는:
- 사용자 원본을 그대로 보존하고 해석한다.
- Codex에게 CLI/script bridge로 원본 관련 공간자료 retrieval을 요청한다.
- Codex가 가져온 공간자료를 원본 + 공간 + 모델값으로 merge한다.
- merge 결과를 재해석/재반영/재이해하고 실행한다.
- 실행 trace와 changed_judgment를 Codex가 다시 읽기 쉽게 기록한다.

Codex는:
- 1차로 원본 기준 관련 공간자료를 찾아 Hermes에게 돌려준다.
- selected refs / rejected refs / changed_judgment_for_hermes를 기록한다.
- Hermes 실행 이후 reentry record를 읽고 공간 숙성 여부를 판단한다.
- 공간 숙성 판단 중 필요하면 Codex script-chain 내부에서 Gemini를 사용한다.

Gemini는:
- Hermes가 직접 호출하지 않는다.
- Codex script-chain 내부에서 layer/space 분석 보조로만 사용된다.

## 금지

- Codex direct API invocation: NO
- Gemini direct API invocation: NO
- Hermes direct Gemini invocation: NO
- external tool API/direct/server/replay: NO
- folder tree mutation: NO
- source/authority/current-position/registry mutation: NO
- promotion: HOLD

## 현재 loop

1. USER_ORIGINAL_TO_HERMES
2. HERMES_ORIGINAL_INTERPRETATION
3. CODEX_SPACE_RETRIEVAL_BY_ORIGINAL_VIA_CLI_SCRIPT
4. HERMES_MODEL_MERGE_ORIGINAL_SPACE_MODEL
5. HERMES_EXECUTION_AND_TRACE
6. CODEX_READABLE_REENTRY_RECORD
7. CODEX_SPACE_MATURATION_DECISION
8. OPTIONAL_GEMINI_VIA_CODEX_SCRIPT_CHAIN
9. CODEX_MATURATION_PACKET_TO_HERMES

## Codex가 먼저 읽을 파일

/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/04_CODEX_READ_FIRST_FOR_SPACE_RETRIEVAL.md

## Codex task packet

/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/05_codex_space_retrieval_task_packet_v0.json

## Codex reference path index

/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/03_codex_reference_path_index_v0.json

## Codex return 위치

/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/07_CODEX_SPACE_RETRIEVAL_RETURN_PACKET_PLACEHOLDER.json

## Codex first-pass 목표

이번 pass는 공간 숙성이 아니다.
먼저 원본 기준으로 관련 공간자료를 찾아 Hermes가 merge/execute할 수 있게 반환한다.

Codex return에는 최소 다음이 있어야 한다:
- read_files
- selected_space_material
- rejected_space_material
- original_to_space_fit
- changed_judgment_for_hermes
- risks
- recommended_hermes_merge_inputs
- next_for_hermes
- promotion_status: HOLD

## Hermes next after Codex return

Codex return이 작성되면 Hermes는 아래 template을 기반으로 merge packet을 채운다:

/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/08_hermes_model_merge_packet_template_v0.json

그 다음 Hermes가 실행 trace/reentry record를 생성하고, Codex는 아래 지시문으로 공간 숙성 pass를 수행한다:

/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/09_CODEX_REENTRY_AFTER_HERMES_MERGE_AND_EXECUTION.md

## 한 줄 결론

Codex는 먼저 원본 기준 공간자료를 가져오고, Hermes는 그 자료를 원본+공간+모델값으로 merge/실행하며, 이후 Codex가 reentry record를 읽어 공간 숙성을 담당한다.
