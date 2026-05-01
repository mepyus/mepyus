# Validation Round 5

## Target

Validate optional worker guide update candidate:

```text
worker_guide_v0_1.md
-> run_005_worker_guide_v0_1_routing_check.md
```

## Criteria

```text
1. Existing worker_guide_v0 remains unchanged.
2. v0.1 guide stays candidate, not baseline.
3. It routes external material to external intake.
4. It routes destructive/install/baseline requests to preflight guard.
5. It does not over-block read-only existence checks.
6. It does not create automation, commands, hooks, or source-space edits.
```

## Evidence

```yaml
new_guide_file: worker_guides/worker_guide_v0_1.md
old_guide_preserved: true
run_file: runs/run_005_worker_guide_v0_1_routing_check.md
cases_tested: 5
external_case_routed: true
dangerous_cases_escalated: 3
low_risk_case_allowed: 1
baseline_created: false
automation_created: false
source_space_modified: false
```

## Analysis

The v0.1 worker guide makes the sandbox more usable without changing the source space.

It gives the worker a short choice between:

- `external_material_intake`
- `preflight_guard`
- observation-only for low-risk read-only checks

This reduces repeated user explanation and keeps the guide under candidate status.

The main risk is guide creep. If each new skill is added immediately, the worker guide can become a heavy operating contract.

## Verdict

```yaml
verdict: OK
reason: candidate worker guide update routes current sandbox tasks correctly without implementation or promotion
human_judgment_required_now: false
next_allowed_move: structured_footer_skill_candidate
```

## Do not

- Do not replace `worker_guide_v0`.
- Do not promote `worker_guide_v0_1` to baseline.
- Do not add automation or commands.
- Do not update main/source-space guide automatically.
