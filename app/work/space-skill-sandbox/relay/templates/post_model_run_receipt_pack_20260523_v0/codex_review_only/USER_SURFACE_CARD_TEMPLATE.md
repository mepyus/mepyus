# POST_MODEL_RUN_USER_SURFACE_CARD_TEMPLATE

status: USER_SURFACE_TEMPLATE_WITH_HOLD

## 쉬운 요약

<모델 실행 결과를 사람이 읽을 수 있게 요약한다.>

## 반드시 유지할 말

- raw는 authority가 아니다.
- lite는 approval이 아니다.
- receipt는 promotion이 아니다.
- 결과는 candidate/review evidence일 뿐이다.

## HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: approved_single_lane_only
real_gemini_execution: depends_on_selected_lane
real_codex_execution: depends_on_selected_lane
approval_applied: explicit_user_approval_required
live_db_intake: HOLD
schema_mutation: no
snapshot_mutation: no
router_runner_claim: no
write_ui: no
authority_database: no
shared_db_mutation: no
v1_snapshot_creation: no
m4_reusable_module: no
module_promotion: no
program_alpha_ready: no

