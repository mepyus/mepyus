# Validation Round 3

## Target

Validate a real external material intake:

```text
external URL
-> gstack_geeknews_note.md
-> external-material-intake.v0_1.skill.md
-> run_003_external_material_intake_gstack.md
```

## Criteria

```text
1. One external material is used.
2. Internal references stay at two or fewer.
3. The run avoids implementation, installation, and adoption drift.
4. The run separates value from risk.
5. The footer gives the user a concrete next judgment.
6. The run reduces copy/paste and re-explanation burden.
7. The result does not become baseline or command authority.
```

## Evidence

```yaml
material_file: test_materials/gstack_geeknews_note.md
run_file: runs/run_003_external_material_intake_gstack.md
source_urls:
  - https://news.hada.io/topic?id=27756
  - https://github.com/garrytan/gstack
internal_reference_count: 2
footer_exists: true
implementation_jump: false
installation_jump: false
baseline_created: false
automation_created: false
user_decision_clear: true
```

## Analysis

This run is stronger than the Graphify-note simulation because it uses a current external URL as intake material.

The skill successfully lowered gstack into:

- comparison material
- borrow-later patterns
- caution asset

The run did not treat gstack as a tool to install. It preserved the useful patterns:

- worker roles as repeatable skills
- guard/freeze/careful as preflight inspiration
- investigate before fix
- qa-only as report-without-modification
- cross-model review as validation

It also preserved the risks:

- role over-promotion
- command-center drift
- auto-plan to implementation compression
- project setup/team-mode authority changes
- long skill/context weight

## User burden check

```yaml
repeated_copy_paste_reduced: true
internal_comparison_done: true
footer_decision_clear: true
next_action_clear: true
remaining_burden: user still decides whether any pattern deserves a later skill extraction
```

## Verdict

```yaml
verdict: OK
reason: real external material intake completed inside sandbox with no implementation/adoption drift
next_allowed_move: extract_one_pattern_only
recommended_pattern: preflight_guard_from_gstack_guard_careful_freeze
```

## Do not

- Do not install gstack.
- Do not add gstack to Claude/Codex/Gemini project config.
- Do not adopt slash commands wholesale.
- Do not promote AI roles to internal authority.
- Do not turn this into controller or automation architecture.
