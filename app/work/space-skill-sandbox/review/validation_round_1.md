# Validation Round 1

## Target

Validate the first sandbox cycle:

```text
README
-> external-material-intake.skill.md
-> graphify_note.md
-> run_001_external_material_intake_graphify.md
```

## Criteria

```text
1. Existing source-space documents remain untouched.
2. Sandbox stays small.
3. At least one lens exists.
4. At least one skill exists.
5. The skill is short enough for a worker to use.
6. One external material is applied.
7. Internal references are limited to 1-2.
8. Output includes a 4-line footer.
9. The run does not jump to implementation.
10. The user can decide proceed / hold / review-needed.
```

## Result

```yaml
verdict: NEEDS_RETRY
source_space_untouched: true
sandbox_small: true
lens_exists: false
skill_exists: true
skill_too_long: true
external_material_applied: true
internal_reference_count: 2
footer_exists: true
implementation_jump: false
user_decision_clear: partial
```

## Findings

- The first run is safe and useful, but it is still more of a report than a reusable sandbox loop.
- The sandbox lacks a separate lens file, even though the sandbox approach says lens -> skill -> run.
- The skill is 119 lines, which is too long for the intended "short worker guide" direction.
- The run correctly avoids Graphify adoption, hook, MCP, and whole-space graphification.
- The footer is useful, but the next step still points to another dry-run rather than a concrete review verdict.

## Corrections for retry

1. Add one lens file.
2. Add one short worker guide.
3. Add a shorter v0.1 skill.
4. Re-run Graphify intake with the shorter skill.
5. Review whether the user decision is clearer.
