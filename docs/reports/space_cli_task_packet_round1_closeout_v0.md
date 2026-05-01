# Space-CLI Task Packet Round 1 Closeout v0

## 1. core conclusion

The space should not feed the whole space to the CLI.

The space should pass only the minimum memory, line, axis, guardrail, and pointer needed for the current task.

The packet is a bounded work aid.

It is not a schema, not JSON, not runtime structure, and not authority transfer.

## 2. minimum packet principles

Keep the packet:

- short
- role-limited
- guardrail-aware
- pointer-based for sources
- memory-card-based for prior reflux
- explicit about stop conditions
- explicit that `next_move_candidate` is not automatic execution
- explicit that CLI results must be reread as `worker_return` or another current source surface

The packet should help the CLI avoid overreach without requiring the CLI to become the space.

## 3. still not finalized

Do not finalize:

- JSON schema
- runtime packet
- verification return
- bridge script
- automatic dispatch
- automatic reflux
- baseline lock
- controller design
- source-surface taxonomy change

The minimum field list is still a thought-experiment candidate.

## 4. round 1 field judgment

Required fields:

- `request_summary`
- `source_surface`
- `user_goal`
- `guardrails`
- `cli_role`
- `expected_output`
- `stop_conditions`

Recommended fields:

- `relevant_lines`
- `relevant_axis`
- `memory_cards`
- `source_pointers`
- `return_surface`

Optional fields:

- `reflux_candidate`

Only-when-needed fields:

- detailed source excerpt
- native-vs-space comparison prompt
- expanded internal diff axes
- deeper probe question

## 5. memory card judgment

Memory cards should be the default way to pass prior reflux memory.

Minimum card fields:

- `memory_id` or `short_label`
- `memory_type`
- `one_line_summary`
- `why_relevant_now`
- `guardrail_link`
- `source_pointer`
- `weight`
- `expiry_or_recheck_condition`

Memory cards should usually be limited to three to five cards.

If more is needed, use pointer-based source check rather than expanding the packet.

## 6. token and memory conclusion

The token-saving route is:

```text
source surface
-> relevant line / axis
-> compact memory cards
-> source pointers
-> minimal expected output
-> stop conditions
```

Avoid:

```text
full onboarding
full conversation
all documents
all risks
full source text by default
```

This keeps the space light and keeps the CLI task bounded.

## 7. next step candidates

Next step can be one of two non-implementation moves:

1. Apply the minimum packet example to one real material as a dry-run.
2. Give Gemini a draft-only minimum packet and compare native vs space-referenced output again.

Do not implement yet.

Do not create scripts, runtime structure, JSON schema, verification packet/return structure, or bridge.

## 8. closeout verdict

```yaml
verdict: PASS_WITH_NOTE
minimum_packet_fields_defined: true
memory_card_retrieval_defined: true
token_memory_lightweight_preserved: true
schema_created: false
json_packet_created: false
runtime_structure_created: false
bridge_created: false
scripts_created: false
baseline_lock: false
next_allowed_move: dry_run_one_real_material_or_gemini_draft_only_comparison
```
