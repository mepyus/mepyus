# Space Anchor Stack Operating Setup v0

## 1. Status

```yaml
status: setup_candidate
created: 2026-05-06
baseline_lock: false
automation: false
writer_created: false
scope: plan_from_space_session_convergence_prevention
```

This setup turns the current "Plan from Space, not from Model Default" discussion into a small operating layer for external-tool planning.

It does not replace the existing space exploration contract, context bundle, review gate, or return record materials. It binds them into a lighter pre-plan anchor stack.

## 2. Core Principle

```text
Plan from Space.
Execute within Space Boundary.
Loop with Space Re-Entry.
Closeout as Return-to-Space.
```

Short form:

```text
Plan from Space, not from Model Default.
```

Operational form:

```text
Plans are generated only after the current work has passed through a small space anchor.
```

## 3. Problem

External tools often plan from model-default decomposition:

```text
analysis -> design -> execution -> verification -> review -> closeout
```

That decomposition can be useful, but it becomes a VectorFL failure pattern when it appears before space records are activated.

Observed risks:

- small session convergence
- user relay burden
- repeated closeout without movement
- confusion between hard boundary and watch item
- output completion without Return-to-Space Value
- external tool log or memory mistaken for VectorFL memory

## 4. Anchor Stack

### 4.1 Stable Space Operating Anchor

Role:

- hold the common direction across tasks
- prevent model-default planning before space reference
- keep external tools as movement organs, not source of truth

Primary output:

- `docs/specs/stable_space_operating_anchor_v0.md`

### 4.2 Line Asset Map

Role:

- map a mature enough long-flow line to reusable space assets
- keep exploration bounded by activation route
- provide package-sizing and stop/continue memory

First line:

- `Plan from Space / Session Convergence Prevention`

Primary output:

- `docs/indexes/plan_from_space_line_asset_map_v0.md`

### 4.3 Session Space Anchor

Role:

- bind a current task to line / axis / camera / lens
- state package sizing and stop/continue rules before planning
- give the external tool a small re-entry card for runtime checks

Primary output:

- `docs/specs/session_space_anchor_template_v0.md`
- `app/work/SESSION_SPACE_ANCHOR_20260506_PLAN_FROM_SPACE_V0.md`

### 4.3.1 Plan Basis

Role:

- force plan-mode output to reveal its space grounding before it proposes tasks
- make model-default plans detectable
- connect line / axis / camera / lens to package sizing

Primary output:

- `docs/specs/plan_basis_template_v0.md`

### 4.4 Movement Record

Role:

- make closeout a return action, not a completion phrase
- preserve reusable judgment and future reuse notes
- keep Gemini/Codex logs as raw trace until interpreted

Primary output:

- `docs/specs/movement_record_template_v0.md`

### 4.5 Plan Mode Reference Pack

Role:

- provide the actual compact pack to send before an external tool drafts a plan
- combine stable anchor, line map, session anchor, Plan Basis, and return contract

Primary outputs:

- `docs/specs/external_tool_plan_mode_reference_pack_v0.md`
- `app/work/PLAN_MODE_REFERENCE_PACK_20260506_PLAN_FROM_SPACE_V0.md`
- `docs/specs/external_tool_plan_prompt_wrapper_v0.md`

### 4.6 Gate Checklist

Role:

- manually review whether a worker plan actually passed the anchor stack
- reject model-default plans that lack Plan Basis or package sizing judgment

Primary output:

- `docs/specs/anchor_stack_gate_checklist_v0.md`

### 4.7 Manifest

Role:

- keep the current candidate setup discoverable without becoming a registry

Primary output:

- `docs/indexes/anchor_stack_manifest_v0.md`

## 5. Gate Placement

### Pre-Plan Gate

Before plan generation, check:

- stable anchor
- relevant line asset map
- current user purpose
- current work type

No plan should be accepted as space-grounded unless it includes a plan basis.

### Plan Sizing Gate

Default:

```text
broad-but-bounded package
```

Small session split is an exception that must be justified by a blocking reason.

Allowed split reasons:

- user decision changes direction
- unapproved implementation or file modification would be needed
- broad scan is required
- evidence gap is blocking
- tool role is unclear
- current line cannot be selected
- return shape is unclear

### Runtime Re-Entry Gate

Re-read the session anchor before:

- splitting work into separate sessions
- treating a watch item as a stop
- producing final / ready / complete language
- asking the user to relay tool output
- closeout

### Closeout / Return-to-Space Gate

Closeout must state:

- activated line / axis / camera / lens
- evidence or read trace
- issue / watch item
- Return-to-Space Value
- future reuse note

## 6. Existing Sources Bound By This Setup

- `docs/specs/space_exploration_contract_v0.md`
- `docs/reports/space_cli_token_budget_and_memory_weight_policy_v0.md`
- `app/work/CONTEXT_BUNDLE_TEMPLATE_V0.md`
- `app/work/REVIEW_RECOVERY_GATE_V0.md`
- `app/work/PACKAGE_END_FIX_REVIEW_V0.md`
- `app/work/PROGRAM_FRAME_EXTERNAL_PATTERN_MAP_V0.md`
- `app/work/SESSION_43_RESULTS_V0.md`
- `app/work/SESSION_44_RESULTS_V0.md`
- `app/work/SESSION_45_RESULTS_V0.md`
- `app/work/SESSION_46_RESULTS_V0.md`
- `app/work/SESSION_47_RESULTS_V0.md`
- `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md`
- `docs/specs/line_maturity_and_operating_anchor_direction_lock_v0.md`

## 7. Gemini Delegation

The token-heavy bounded exploration pass is delegated to Gemini through:

- `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_exploration_packet_20260506_v0.md`

Gemini output is raw trace until interpreted into a Movement Record or a future line-map revision.

The first Gemini exploration attempt timed out. A compact no-tool crosscheck packet was added:

- `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_compact_crosscheck_packet_20260506_v0.md`

## 8. Non-Goals

- no automation runner
- no automatic line promotion
- no baseline declaration
- no writer script
- no broad inventory of the whole space
- no external-tool memory treated as VectorFL memory
