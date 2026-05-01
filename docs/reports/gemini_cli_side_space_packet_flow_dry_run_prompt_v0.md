# Gemini Prompt: CLI-Side Space Packet Flow Dry-run 001

You are Gemini acting as a bounded dry-run worker.

Mode:

- READ-ONLY
- STRUCTURE DRY-RUN ONLY
- NO IMPLEMENTATION
- NO FILE MODIFICATION
- NO INDEX UPDATE
- NO BASELINE / SCHEMA / AUTOMATION CREATION

## Purpose

Run one simulated case through the CLI-side space packet flow:

```text
Routing -> Packet -> Recovery -> State -> Transition
```

The goal is to test whether this operating structure is too heavy, whether judgment fields are missing, and whether it preserves user sovereignty, evidence, and layer-aware reading.

Do not implement anything.
Do not conclude "now implement this."

## Default Dry-run Case

Codex returned a report result.

The user wants to validate the result and decide whether it can move to the next task.

Use this as the input case:

```text
User input:
Codex가 어떤 리포트 결과를 반환했다. 이 결과를 검증하고 다음 작업으로 넘겨도 되는지 판단해줘.
```

## Required Flow

Perform the following steps:

1. Route the user input.
2. Select the appropriate Packet.
3. Explain why that Packet was selected.
4. Draft the Packet contents.
5. Create a simulated Worker result.
6. Write a Recovery Card.
7. Classify the recovered State.
8. Write a Transition Card.
9. Suggest the next Packet candidate.
10. Evaluate whether the structure is too heavy or missing fields.

## Packet Types

Use one of:

- Research Packet
- Implementation Packet
- Validation Packet
- Refactor Packet
- Space Intake Packet
- Chat Summary Packet
- Hold / Clarify Packet

## Recovery Card Fields

Use this structure:

```text
packet_type:
source_task:
verdict:
primary_event:
evidence_anchor:
what_changed:
what_was_learned:
risk_or_warning:
reuse_hint:
pattern_candidate:
human_lock_required:
recommended_next_state:
do_not_promote_as:
next_packet_candidate:
```

## State Classification

Choose from:

- discard
- raw_trace_only
- residue_candidate
- risk_memory
- reuse_hint
- pattern_candidate
- human_review_candidate
- locked_rule
- quarantine

Rules:

- `locked_rule` is allowed only after explicit user lock.
- AI can raise material only to `human_review_candidate`.
- Status is a maturation signal, not fixed ontology.

## Transition Card Fields

Use this structure:

```text
current_packet:
verdict:
recovered_state:
risk_level:
human_lock_required:
can_continue:
next_packet:
must_include_note:
forbidden_next_step:
why:
```

## Safeguards

Preserve these rules:

1. AI is a worker; the user is the final judge.
2. AI can make candidates but cannot lock or promote.
3. A summary without evidence is a claim.
4. Evidence should be collapsed, not deleted.
5. Status is a maturation signal, not ontology.
6. External material or research does not transition directly to implementation.
7. Research -> Implementation is forbidden.
8. Implementation results must pass through Validation.
9. Refactor requires `logic_changed=false`.
10. Human-lock items do not auto-transition.

## Forbidden

- Do not modify files.
- Do not implement anything.
- Do not update indexes.
- Do not create baseline, schema, registry, classifier, dispatcher, controller, automation, UI, runtime bridge, or agent architecture.
- Do not finalize internal structure.
- Do not conclude "now implement this."

## Output Format

```text
Verdict:
PASS / PASS_WITH_NOTE / NEEDS_RETRY / NEEDS_USER_REVIEW

Dry-run case:

Routing result:

Selected packet:

Packet selection reason:

Packet draft:

Simulated worker result:

Recovery Card:

State classification:

Transition Card:

Next packet candidate:

Missing fields:

Overweight fields:

Risks:

Recommended adjustment:

Do not proceed to implementation yet:
Yes / No
```

Expected stance:

- Prefer `PASS_WITH_NOTE` if the flow works but feels heavy or needs field trimming.
- Use `NEEDS_USER_REVIEW` if the simulated result would require lock, promotion, or direction choice.
- Never return `Do not proceed to implementation yet: No` unless the prompt explicitly asks for implementation readiness and no guardrail remains.
