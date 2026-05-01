# Space-CLI Scenario Test Catalog v0

## 1. purpose

This catalog defines thought-experiment scenarios for testing a lightweight space-CLI attachment and reflux process.

The scenarios compare:

```text
native CLI behavior
vs
space-referenced CLI behavior
```

The goal is to identify missing context, overreach, alignment, contradiction, residue, and reflux candidates.

## 2. scenario record format

```yaml
scenario_id:
input_type:
source_surface_candidate:
native_cli_expected_behavior:
space_referenced_expected_behavior:
diff:
  missing:
  overreach:
  alignment:
  contradiction:
  residue:
reflux_candidate:
  risk_memory:
  reuse_hint:
  pattern_candidate:
  hold_signal:
  next_move_candidate:
user_facing_card:
  쓸 수 있나?
  왜?
  다음엔?
  조심할 점은?
verdict:
```

## 3. Scenario 1. external material enters

```yaml
scenario_id: scenario_1_external_material_enters
input_type: external CLI operating material or multi-agent failure case
source_surface_candidate: external_material_file
native_cli_expected_behavior: summarize the material and extract general lessons
space_referenced_expected_behavior: read as bounded external material, not doctrine
diff:
  missing: native may miss local source-surface routing and over-promotion guardrails
  overreach: native may convert external claims into local rules
  alignment: both may identify useful operational patterns
  contradiction: external claims may conflict with local lightweight-memory posture
  residue: external framing can remain comparison residue
reflux_candidate:
  risk_memory: external material over-promotion risk
  reuse_hint: split external material into borrow / do-not-borrow / risk / next comparison
  pattern_candidate: external references require bounded reference reading
  hold_signal: hold automation or controller implementation
  next_move_candidate: compare one concrete external claim against current flow
user_facing_card:
  쓸 수 있나?: 참고자료로는 쓸 수 있음.
  왜?: 외부 자료는 힌트를 줄 수 있지만 우리 기준을 통과한 것은 아님.
  다음엔?: 빌릴 것과 빌리지 않을 것을 나눠 비교한다.
  조심할 점은?: 외부 표현을 baseline이나 doctrine으로 올리지 않는다.
verdict: PASS_WITH_NOTE
```

## 4. Scenario 2. Codex worker_return enters

```yaml
scenario_id: scenario_2_codex_worker_return_enters
input_type: Codex PASS_WITH_NOTE return with created files
source_surface_candidate: worker_return
native_cli_expected_behavior: read as completion report
space_referenced_expected_behavior: read expected-vs-observed before accepting
diff:
  missing: native may skip expected-vs-observed and residual risk
  overreach: PASS_WITH_NOTE may be treated as done or baseline
  alignment: created files may match requested scope
  contradiction: claimed pass may conflict with unverified behavior
  residue: return can become follow-up material
reflux_candidate:
  risk_memory: do not mistake PASS_WITH_NOTE for completion
  reuse_hint: read Codex returns as worker_return
  pattern_candidate: every worker return starts with expected-vs-observed
  hold_signal: hold baseline lock until real material trial
  next_move_candidate: lower created outputs into one actual material trial
user_facing_card:
  쓸 수 있나?: 쓸 수 있지만 완료 기준은 아님.
  왜?: 반환물은 작업 증거이지 최종 판단이 아니기 때문.
  다음엔?: 기대와 관측을 비교하고 실제 재료 trial로 내린다.
  조심할 점은?: PASS_WITH_NOTE를 baseline으로 올리지 않는다.
verdict: PASS_WITH_NOTE
```

## 5. Scenario 3. implementation pressure appears

```yaml
scenario_id: scenario_3_implementation_pressure_appears
input_type: user says "이제 구현해줘"
source_surface_candidate: conversation_material
native_cli_expected_behavior: begin scripts, bridge, automation, or implementation
space_referenced_expected_behavior: read as implementation pressure before structure lock
diff:
  missing: native may miss unresolved structure boundaries
  overreach: native may build tool setup before space structure is ready
  alignment: implementation pressure may indicate a real next action desire
  contradiction: user urgency may conflict with hold signals
  residue: repeated implementation pressure can shape future packet boundaries
reflux_candidate:
  risk_memory: tool setup can outrun the space body
  reuse_hint: split implementation request into structure / thought test / implementable unit
  pattern_candidate: implementation pressure requires boundary classification first
  hold_signal: hold before scripts or bridge work
  next_move_candidate: identify the smallest non-structural test
user_facing_card:
  쓸 수 있나?: 바로 구현으로 가기 전 재료로 쓸 수 있음.
  왜?: 구현 압력 자체가 다음 경계 판단 재료이기 때문.
  다음엔?: 구현 가능한 부분과 사고실험이 필요한 부분을 먼저 나눈다.
  조심할 점은?: 도구 셋업이 공간 본체를 앞서지 않게 한다.
verdict: PASS_WITH_NOTE
```

## 6. Scenario 4. Gemini result looks too neat

```yaml
scenario_id: scenario_4_gemini_result_looks_too_neat
input_type: Gemini returns PASS or all self-check yes
source_surface_candidate: worker_return
native_cli_expected_behavior: trust the neat result
space_referenced_expected_behavior: reread as worker_return and check judgment depth
diff:
  missing: native may miss shallow evidence or source-surface flattening
  overreach: self-check yes may be treated as validation proof
  alignment: format compliance may still be useful
  contradiction: clean form may conflict with weak evidence
  residue: neat-but-thin outputs become skepticism training material
reflux_candidate:
  risk_memory: Gemini self-check yes overtrust risk
  reuse_hint: Gemini result is always reread as worker_return
  pattern_candidate: separate format compliance from judgment compliance
  hold_signal: HOLD before rerun when evidence is weak
  next_move_candidate: ask for missing evidence or source-surface separation
user_facing_card:
  쓸 수 있나?: 초안 증거로는 쓸 수 있음.
  왜?: 깔끔한 형식이 판단 깊이를 보장하지 않음.
  다음엔?: worker_return으로 다시 읽고 근거와 과승격을 확인한다.
  조심할 점은?: 모든 yes를 검증 완료로 믿지 않는다.
verdict: PASS_WITH_NOTE
```

## 7. Scenario 5. runtime_event enters

```yaml
scenario_id: scenario_5_runtime_event_enters
input_type: one runtime ledger event
source_surface_candidate: runtime_event
native_cli_expected_behavior: summarize event as system status
space_referenced_expected_behavior: read as one event slice only
diff:
  missing: native may miss source/receipt linkage needs
  overreach: one event may become whole-system success proof
  alignment: both can identify that an event occurred
  contradiction: event existence may not prove claimed result
  residue: event can point to source, receipt, or worker_return
reflux_candidate:
  risk_memory: do not expand one event into whole-system proof
  reuse_hint: runtime_event starts with evidence/event lens
  pattern_candidate: event reading requires linked source or receipt check
  hold_signal: hold global success claim
  next_move_candidate: inspect source / receipt / worker_return connection
user_facing_card:
  쓸 수 있나?: 실행 흔적으로는 쓸 수 있음.
  왜?: 특정 시점의 사건이지 전체 성공 증명은 아니기 때문.
  다음엔?: 연결된 source, receipt, worker_return을 확인한다.
  조심할 점은?: event 1건을 안정화나 완료로 확대하지 않는다.
verdict: PASS_WITH_NOTE
```

## 8. Scenario 6. repeated similar inputs appear

```yaml
scenario_id: scenario_6_repeated_similar_inputs_appear
input_type: repeated Codex / Gemini / external material / implementation pressure
source_surface_candidate: mixed_repeated_material
native_cli_expected_behavior: repeat similar explanation each time
space_referenced_expected_behavior: retrieve prior reflux memory and change reading position
diff:
  missing: native may lack accumulated warning memory
  overreach: native may generalize too early from repetition
  alignment: repetition can reveal a real pattern
  contradiction: repeated signals may still not justify baseline lock
  residue: repeated cases can mature into pattern candidates
reflux_candidate:
  risk_memory: repeated risks should trigger compressed warning
  reuse_hint: include compact prior memory in the next packet
  pattern_candidate: repeated judgment flow candidate
  hold_signal: hold promotion until repeated evidence is specific enough
  next_move_candidate: make a small pattern test instead of broad implementation
user_facing_card:
  쓸 수 있나?: 반복 패턴 후보로는 쓸 수 있음.
  왜?: 같은 위험과 처리 흐름이 다시 나타나기 때문.
  다음엔?: 이전 환류 기억을 꺼내 다음 입력 판독에 붙인다.
  조심할 점은?: 반복을 곧바로 baseline이나 자동 규칙으로 승격하지 않는다.
verdict: PASS_WITH_NOTE
```
