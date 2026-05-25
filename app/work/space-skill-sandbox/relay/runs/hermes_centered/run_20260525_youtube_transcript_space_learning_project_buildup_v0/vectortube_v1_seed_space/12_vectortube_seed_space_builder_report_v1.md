DONE: 벡터튜브 v1 방향 수정 반영

verdict: READY_WITH_HOLD

핵심 변경:
- 이름: 벡터튜브 / VectorTube
- v0의 검색/수집기 중심에서 v1의 사용자 seed 영상 기반 mini-space builder로 전환.
- 자동 검색은 기본 OFF. 사용자가 저장/기록한 영상에서 시작한다.
- seed 영상 transcript를 먼저 공간의 사고방식으로 읽고, 그 다음 모델 추론으로 필요한 보강/강화/반대/누락 관점 후보를 만든다.
- 관련 영상 스크립트는 자동 수집이 아니라 user-approved candidate 또는 사용자가 추가로 준 URL을 기준으로 읽는다.
- VectorFL 본공간에 바로 넣지 않고 벡터튜브 mini-space에서 혼동/편향/층위/부품화를 거친 뒤 HOLD push packet으로 넘긴다.

run_dir:
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_youtube_transcript_space_learning_project_buildup_v0/vectortube_v1_seed_space

주요 산출물:
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_youtube_transcript_space_learning_project_buildup_v0/vectortube_v1_seed_space/hermes_exec/09_space_use_precheck_vectortube_v1.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_youtube_transcript_space_learning_project_buildup_v0/vectortube_v1_seed_space/project_spec/10_vectortube_seed_space_builder_spec_v1.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_youtube_transcript_space_learning_project_buildup_v0/vectortube_v1_seed_space/shared_handoff/11_CODEX_SPACE_MATCHING_REQUEST_VECTORTUBE_SEED_SPACE_V1.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_youtube_transcript_space_learning_project_buildup_v0/vectortube_v1_seed_space/12_vectortube_seed_space_builder_report_v1.md

HOLD:
- 자동 검색 없음
- 영상 다운로드 없음
- transcript만 seed/승인 related에 한정
- Codex/Gemini 호출 없음
- VectorFL main space push 없음
- authority/current-position/registry mutation 없음

NEXT_SAFE_LANE:
- 사용자가 seed YouTube URL 1개를 주면, 검색 없이 transcript fetch → seed source card → seed space reading card → enrichment_need_card → mini-space skeleton까지 dry-run.
