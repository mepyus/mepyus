# Space-CLI Reflux Memory State Model v0

## 1. definition of reflux

Recovery means bringing a result back.

Reflux means the recovered result enters the space as memory that may change the next space action.

Recovery asks:

```text
What did the CLI return?
```

Reflux asks:

```text
What should this return change about future input reading, packet formation, guardrail choice, or hold decisions?
```

## 2. reflux targets

The following can become reflux material:

- CLI answer
- CLI execution result
- Codex worker_return
- Gemini worker_return
- runtime_event
- generated_report
- native vs space-referenced diff
- failure
- error
- distrust signal
- over-promotion risk
- user confusion

Each target must still be judged by source surface.

## 3. reflux states

## note_only

Remember lightly.

Weak automatic effect on the next task.

Use when:

- the trace is useful but not recurring
- the result explains a local decision
- over-recording would be heavier than the memory value

## reuse_hint

Retrieve in similar future tasks.

Use when:

- the material gives a practical reading shortcut
- the same input type may reappear
- a future packet should include a compact reminder

## risk_memory

Use as a warning in similar future tasks.

Use when:

- over-promotion risk recurs
- PASS can be mistaken for final authority
- external material can be mistaken for doctrine
- runtime event can be mistaken for whole-system proof

## pattern_candidate

Candidate for a repeated pattern.

Use when:

- similar cases recur
- the same reading flow works repeatedly
- the candidate still needs more evidence before lock

## hold_signal

Pause before continuing.

Use when:

- implementation pressure outruns structure
- source surface is confused
- evidence is too thin
- automation or controller work appears too early

## next_move_candidate

Possible next action.

This is not execution permission.

## deeper_probe_needed

Separate thought experiment or verification is needed.

Use when:

- the difference is structural
- a 4-line card is insufficient
- source relation is unclear
- token cost or memory weight cannot be judged lightly

## 4. effect on next space action

Reflux memory may influence:

- next input routing
- next source surface judgment
- next CLI task packet
- next guardrail selection
- next user-facing card
- next thought-experiment candidate
- next implement-or-hold judgment

Example:

```text
Prior risk_memory:
PASS_WITH_NOTE can be overread as completion.

Next worker_return packet:
Include guardrail:
Do not treat PASS_WITH_NOTE as baseline, completion, or proof.
```

## 5. no automatic execution

Reflux memory is not an automatic execution trigger.

`next_move_candidate` means:

```text
possible next move
```

not:

```text
run this now
```

User or supervisor judgment is required before action.

## 6. weight elevation rule

Memory can become heavier only when:

- it reappears across multiple materials
- it improves routing or guardrail choice
- it reduces repeated explanation
- it prevents a known overreach
- it remains bounded and source-surface aware

Memory should not become heavier because:

- it sounds elegant
- it appeared once
- a worker returned PASS
- it fits an attractive architecture
- it helps justify immediate implementation
