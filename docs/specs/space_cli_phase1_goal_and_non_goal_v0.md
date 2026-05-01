# Space CLI Phase 1 Goal And Non Goal v0

## Status

- phase: `phase1_cli_space_enablement`
- authority: `working_spec`
- relation_to_existing_baseline: 이 문서는 기존 baseline을 대체하지 않고, Codex CLI가 기존 공간을 같은 질서로 읽기 위한 얇은 운영 고정 문서다.
- created_for: 질문 해석 -> 공간 탐색 -> Codex 판단 -> merge/diff/hold -> 재유입 루프

## Execution

Phase 1의 목표는 화면/UI가 아니라 공간 자체를 CLI가 읽고 쓸 수 있게 만드는 것이다.

Phase 1에서 고정하는 최소 흐름:

1. 사용자 질문을 구조화된 interpretation packet으로 바꾼다.
2. packet을 근거로 공간 자산을 탐색한다.
3. 탐색 결과를 evidence bundle로 묶는다.
4. 공간 근거와 Codex 판단을 동일시하지 않고 비교한다.
5. 결과를 merge/diff/hold 중 하나로 정리한다.
6. 최종 응답과 과정 흔적을 다시 공간에 reingress record로 남긴다.

현재 잠금 방향:

- 화면/UX는 보류한다.
- 공간 자체를 CLI가 사용할 수 있게 만드는 것이 우선이다.
- 병목은 retrieval 자체보다 translation/handoff 층이다.
- 외부 도구는 공간 본체가 아니라 확장 기관이다.
- 공간은 실행기보다 숙성 기반이다.
- 새 구조를 발명하기보다 이미 있는 구조를 CLI가 같은 것으로 읽게 만든다.

이번 작업의 비목표:

- UI/페이지/패널 설계
- React/Vite 화면 구축
- 다중 에이전트 orchestration 본격화
- ontology 재설계
- 전체 repo 이동
- 자동 루프 완전 자율화
- 외부 툴 deep integration

## Interpretation

지금 필요한 것은 새 구조가 아니라 읽기 지도다. 이미 repo에는 `CURRENT.md`, `vectorfl_status.md`, `source_assets/baselines`, `docs/policies`, `docs/specs`, `runtime/contracts` 같은 층이 존재한다. 문제는 자산 부족이 아니라, CLI가 질문을 받았을 때 어떤 순서로 읽고 어떤 자산을 어떤 권위로 취급해야 하는지 매번 다시 추론해야 하는 점이다.

Phase 1은 실행기를 새로 만드는 단계가 아니다. 질문을 작업 구조로 번역하고, 공간의 근거를 회수하고, Codex의 외부 판단과 공간의 내부 위치를 비교해, 다음 질문에서 재사용 가능한 흔적으로 남기는 translation/handoff 기반을 세우는 단계다.

## Validation

- Codex 첫 진입 기준은 `space_reading_order_for_codex_v0.md`에 둔다.
- 권위 구분은 `source_authority_ladder_v0.md`에 둔다.
- 자산 위치 지도는 `space_asset_map_v0.md`에 둔다.
- 질문 유형별 탐색 시작점은 `question_type_to_search_path_map_v0.md`에 둔다.
- 기존 canonical path 이동이나 삭제는 하지 않는다.

## Stage 1 Closeout

- Verdict: `PASS`
- Files created: 이 문서와 Stage 1 companion 문서 4개
- Key decisions: Phase 1은 UI가 아니라 CLI 읽기/해석/탐색/병합/재유입 기반이다.
- Risks: 일부 path 권위는 아직 working baseline과 final lock이 섞여 있으므로 authority ladder에서 `PROVISIONAL`로 다룬다.
- Entry condition for next stage: 질문을 바로 검색하지 않고 packet으로 번역하는 계약을 만든다.
