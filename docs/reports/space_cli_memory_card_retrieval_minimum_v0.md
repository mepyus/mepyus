# Space-CLI Memory Card Retrieval Minimum v0

## 1. purpose of memory cards

A memory card is not a replacement for the original source.

A memory card is not a full summary of the space.

A memory card is the smallest useful judgment trace that helps the CLI keep direction without reading everything.

The purpose is:

```text
retrieve less
preserve the right caution
avoid repeated explanation
reduce token load
```

## 2. minimum memory card structure

Each card should carry only these fields:

- `memory_id` or `short_label`
- `memory_type`
- `one_line_summary`
- `why_relevant_now`
- `guardrail_link`
- `source_pointer`
- `weight`
- `expiry_or_recheck_condition`

This is a thought-format minimum, not a schema.

## 3. memory_type candidates

- `risk_memory`
- `reuse_hint`
- `pattern_candidate`
- `hold_signal`
- `next_move_candidate`
- `note_only`
- `deeper_probe_needed`

## 4. weight standard

## light

Use when the memory is only a reference for this task.

It should not strongly shape the packet.

## medium

Use when the memory affects current judgment or expected output.

## strong

Use when the memory directly creates a guardrail or HOLD condition.

Strong memory should still not become automatic execution or baseline.

## 5. retrieval principles

Use this order:

1. Find memories matching the current source surface.
2. Keep only memories linked to the relevant line or axis.
3. Limit retrieval to three to five memory cards.
4. If cards are insufficient, use source pointers for a partial source check.
5. Full source reading is the last resort.

Do not retrieve:

- all prior notes
- all memories with similar wording
- old broad philosophy unless directly relevant
- every possible risk
- full source text when a pointer is enough

## 6. memory card examples

## risk_memory example

```text
memory_id:
pass_with_note_overpromotion_risk

memory_type:
risk_memory

one_line_summary:
PASS_WITH_NOTE must not be read as system completion.

why_relevant_now:
The current input is a worker_return with neat verdict wording.

guardrail_link:
Do not treat PASS, PASS_WITH_NOTE, or created-file lists as baseline, completion, or proof.

source_pointer:
docs/reports/space_cli_dry_thought_test_round1_closeout_v0.md

weight:
strong

expiry_or_recheck_condition:
Recheck when worker_return evidence includes actual execution, tests, and expected-vs-observed closure.
```

## hold_signal example

```text
memory_id:
implementation_before_structure_hold

memory_type:
hold_signal

one_line_summary:
Implementation requests should be split before scripts, bridge, automation, or controller work.

why_relevant_now:
The user request contains implementation pressure before structure is locked.

guardrail_link:
Hold implementation until structure / thought experiment / implementable unit are separated.

source_pointer:
docs/reports/space_cli_dry_thought_test_round1_closeout_v0.md

weight:
strong

expiry_or_recheck_condition:
Recheck after a bounded implementable unit is explicitly approved.
```

## reuse_hint example

```text
memory_id:
external_material_bounded_reference_read

memory_type:
reuse_hint

one_line_summary:
External material should be read as one core claim plus guardrail pointer plus borrow / do-not-borrow split.

why_relevant_now:
The current input is external_material_file or a comparison note derived from external material.

guardrail_link:
Do not convert external material into baseline, doctrine, controller, or automation standard.

source_pointer:
docs/reports/space_boundary_material_application_examples_trial_note_v0.md

weight:
medium

expiry_or_recheck_condition:
Recheck if the external material has already been validated by local trials.
```

## 7. retrieval closeout

Memory cards are useful only if they stay small.

If a memory card becomes a full report, it stops doing its job.

If five cards are not enough, the task probably needs pointer-based source check or deeper probe rather than a larger packet.
