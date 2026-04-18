# Integrated Engine Process Camera Intent Alignment Note v0

## 1. Purpose

This note aligns the current package with the user's actual intent.

The user is not asking for another camera-only procedure.
The user is asking for the validated way of thinking behind the camera review cycle to become an engine-side process asset.

## 2. What The User Is Asking For

The intended lift is:

```text
validated review cycle -> process camera -> packetizable engine work
```

This means:

- the object under review may change
- the lens may change
- the process skeleton should remain inspectable
- CLI / sub-agents should receive compact execution packets, not the whole chat history
- return records should redeposit the result, risk, decision, and next use back into the space

## 3. Layer Separation

### Target Object

The target object is what a specific run handles.

Examples:

- camera candidate
- lens candidate
- line candidate
- axis hint
- rollback rule asset
- review guideline asset
- internal reusable asset
- instruction-support material

### Process Camera

The process camera is the reusable operating frame.
It decides how the engine handles the target object:

- intake purpose
- lock scope
- discover candidates
- compare candidates
- bundle evidence
- run validation gates
- decide usable / hold / supplement / insufficient
- form execution packet
- save return record

### Execution Packet

The execution packet is the compact unit a CLI, Codex, Gemini, sub-agent, or worker can consume.
It must carry enough context, lens, evidence, allowed actions, forbidden actions, and expected output shape to run bounded work without rereading the entire conversation.

### Return Record

The return record is what comes back into the engine and space.
It must preserve:

- what was attempted
- what evidence was used
- which gates passed or failed
- what decision was made
- what remains hold / risk / next-use material

## 4. Why This Matters

The camera review cycle produced more than a camera-specific result.
It produced process data:

- why validation started with the strongest original note
- why review-stage was bounded first
- why reread paths were validated before rollout
- why weak shadow-fit results stayed weak
- why patching adjacent documents was blocked
- why the final state became original-note-centered inspection tooling

If this process knowledge is not packaged, later CLI/sub-agent workflows will repeat the same long reasoning from scratch or lose the space's accumulated judgment.

## 5. Current Interpretation Lock

The correct current interpretation:

- extract the process logic, not a fake universal template
- keep sample-grounded distinctions visible
- separate target object, process camera, execution packet, and return record
- preserve `directly` vs `weakly` vs `not yet`
- preserve stop rules as data

## 6. Phase 1 Validation

Intent preservation check:

- the user intent is preserved as process-asset extraction, not camera-only note work

Overclaim check:

- this note does not claim the process camera is already validated across all target types

Status remains:

```text
eligible for provisional camera candidate
not promoted
```

