# Space-CLI Native vs Space-Referenced Diff Protocol v0

## 1. comparison target

This protocol reads the difference between two expected or actual CLI outputs.

## native_cli_response

CLI response without space context.

It may be fast, general, and useful, but it may miss local line, axis, guardrail, source surface, and reflux memory.

## space_referenced_response

CLI response with lightweight space context:

- line
- axis
- relation
- flow
- guardrail
- memory card
- source surface
- stop condition

The space-referenced response is not automatically correct. It must still be read as a worker return or generated report.

## 2. comparison axes

## missing

Context absent from native CLI but recovered by space reference.

Examples:

- source surface distinction
- over-promotion guardrail
- prior risk memory
- relation to existing flow

## overreach

CLI moves too far into implementation, baseline, controller, schema, or final decision.

## alignment

Parts that match the space direction.

## contradiction

Parts that conflict with existing space memory or current boundary.

## compression_gain

User explanation became shorter because the space supplied context internally.

## token_cost

Extra context cost introduced by the space.

This cost must be justified by better routing, lower rework, clearer guardrails, or useful reflux.

## reflux_value

Whether the difference should become future space material.

Possible values:

- none
- note_only
- reuse_hint
- risk_memory
- pattern_candidate
- hold_signal
- next_move_candidate
- deeper_probe_needed

## 3. merge judgment

Do not simply merge both responses.

Choose one or more of these judgments:

## use_native_part

Use the CLI's general answer where it is clean and harmless.

## use_space_part

Use the space-referenced part where local context makes it more accurate.

## discard_native_overreach

Remove broad implementation, baseline, automation, or controller suggestions.

## keep_as_comparison_residue

Keep the difference as comparison material without using it as a conclusion.

## needs_deeper_probe

Use when the difference is large, ambiguous, or potentially structural.

## 4. output format

```yaml
comparison_id:
input:
native_cli_expected:
space_referenced_expected:
diff:
  missing:
  overreach:
  alignment:
  contradiction:
  compression_gain:
  token_cost:
  reflux_value:
merge_decision:
reflux_candidate:
user_direction_value:
verdict:
```

## 5. verdict rule

Use `PASS` only when:

- source surface is preserved
- overreach is identified or absent
- merge judgment is bounded
- reflux candidate is not over-weighted

Use `PASS_WITH_NOTE` when:

- comparison is useful but evidence is thin
- token cost is uncertain
- reflux weight may be too high

Use `HOLD` when:

- native and space-referenced outputs conflict on structure
- implementation pressure appears before boundary judgment
- result suggests automation or controller work too early

Use `FAIL` when:

- the comparison collapses into tool setup
- source surface is lost
- the response claims final authority
