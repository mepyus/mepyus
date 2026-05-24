# Gemini External Tool Planning Trial Set A Return Review 20260506 v0

## Status

```yaml
status: worker_plan_review
date: 2026-05-06
source_worker: gemini_manual_relay
baseline_lock: false
automation: false
schema: false
registry: false
authority_state: interpreted_candidate_only
```

## Source

```text
worker: Gemini
prompt_packet: app/work/space-skill-sandbox/relay/prompts/gemini_external_tool_planning_trial_set_a_20260506_v0.md
delivery_route: user_manual_relay
review_date: 2026-05-06
```

## Gate Review

| gate | pass / hold | evidence |
| --- | --- | --- |
| Pre-Plan Gate | pass | Worker returned `PLAN_BASIS` before `BOUNDED PLAN`; route and canonical PVs were stated. |
| Plan Sizing Gate | pass | Worker selected broad-but-bounded and avoided default multi-session decomposition. |
| Runtime Re-Entry Gate | pass_with_watch | Worker planned internal validation, but runtime re-entry still needs a real execution trial. |
| Closeout / Return-to-Space Gate | pass_with_watch | Worker returned reusable judgment and issue/watch, but final `AUTHORITY` / `TRIAL_PLAN_READY` language required downshift. |

## Required Checks

```yaml
plan_basis_before_plan: true
route_used: ROUTE_EXTERNAL_TOOL_PLANNING
canonical_pvs_used: true
broad_bounded_default: true
blocking_split_reason_if_any: none
non_inspected_scope_stated: true
hard_boundary_vs_watch_separated: partial
return_to_space_value_present: true
authority_claim_absent: false
```

## Review Label

```text
PASS_WITH_WATCH
```

The worker recommended `PASS_AS_SPACE_GROUNDED_PLAN`, but Codex downgrades to `PASS_WITH_WATCH` because the final report used authority/status language.

## Accepted Values

- Build useful-shape maturation boundary.
- Build active/residue marker policy.
- Build external tool runner reliability watch.
- Keep all three as candidate specs, not baseline.

## Corrections Needed

Gemini ended with:

```text
AUTHORITY: SESSION 47 — SPACE_MEANING_RE_ATTACHMENT_PATCH
STATUS: TRIAL_PLAN_READY
```

Codex downshifts this to:

```yaml
authority_state: worker_plan_candidate
trial_status: reviewed_pass_with_watch
memory_promotion: interpreted_candidate_only
```

## Watch Items

- `user_relay_burden_watch` remains active until scripted Gemini runner reliability improves.
- Residue markers could become archive taxonomy if applied broadly.
- Useful-shape maturation labels could become hidden authority if not tied to Movement Records.

## Return-to-Space Value

- Reusable finding: Set A successfully changed worker behavior from direct plan to Plan Basis before plan.
- Reusable finding: route/PV fields are useful as acceptance criteria for external planning.
- Future reuse note: next trial should test the same gates with an actual implementation-heavy or external-material intake request.
