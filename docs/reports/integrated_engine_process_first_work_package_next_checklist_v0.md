# Integrated Engine Process-First Work Package Next Checklist v0

## 1. Verdict

PASS_WITH_NOTE

This checklist replaces the panel-first implementation habit with a process-first work package loop.

The next work must not begin by asking:

```text
Which panel should we add?
```

It must begin by asking:

```text
What process state does the current work package need to carry?
```

## 2. Fixed Target

The target is:

```text
one current work package moving through the fixed 3-surface engine body
```

Not:

```text
many panels explaining the 3 surfaces
```

## 3. Checklist Step 1: Define The Current Work Package Object

Goal:

Create or identify the minimal object that the screen treats as the current work package.

Minimum fields:

- `work_package_id`
- `purpose`
- `process_stage`
- `surface_owner`
- `evidence_state`
- `evidence_bundle_summary`
- `packet_state`
- `authority_state`
- `next_action_candidate`
- `trace_state`
- `sedimentation_state`

Validation:

```text
Can the screen answer "what work package are we operating?" without reading several panels?
```

Stop condition:

If this becomes a giant visible card, stop. The object is a structure behind the screen; surfaces read from it.

## 4. Checklist Step 2: Map The Object To The 8-Step Process

Goal:

Each current work package must sit at one of the engine process stages:

1. instruction intake
2. internal search
3. evidence bundle
4. VectorFL mediation / packetization
5. User organization
6. Engine main processing
7. VectorFL reflux
8. record / sedimentation

Validation:

```text
Can the user tell which process stage owns the current work now?
```

Stop condition:

If the answer is "read the surrounding panels and infer it," the model is not ready.

## 5. Checklist Step 3: Make Surfaces Read The Same Object Differently

Goal:

User / VectorFL / Engine must not show the same dense information.

They should read the same object by role:

| surface | local reading |
| --- | --- |
| User | purpose, assignment, decision, hold/open choice |
| VectorFL | evidence, mediation, route, reread, guard |
| Engine | input, process, return, extraction, validation/deposit candidate |

Validation:

```text
Can the user switch surfaces and still feel this is the same work package?
Can each surface avoid showing information it should not own?
```

Stop condition:

If every surface shows the full object, the 3-surface split is being erased.

## 6. Checklist Step 4: Reduce Panel Visibility, Do Not Add More

Goal:

Existing panels should be reused as local views into the process object.

Before adding a panel, classify the need:

- process state
- evidence state
- authority state
- trace state
- sedimentation state
- only explanation

If it is only explanation, do not add a panel.

Validation:

```text
Can one existing panel be demoted, collapsed, or fed by the current work package instead?
```

Stop condition:

If the implementation adds another panel without reducing mental assembly, reject it.

## 7. Checklist Step 5: Verify With One Real Turn

Goal:

Run or simulate one small work package through:

```text
User purpose
-> VectorFL evidence / packet
-> CLI / Engine return
-> VectorFL reread
-> User decision or deposit candidate
```

Validation questions:

- What is the current work package?
- What process stage is it in?
- What evidence is attached or missing?
- What surface owns the next transformation?
- What is candidate-only / not canonical?
- What record or sedimentation state exists?

Stop condition:

If the answer requires reading many disconnected panels, the screen has not solved the problem.

## 8. Next Implementation Gate

Only after Steps 1-5 pass should the project consider:

- multi-work board
- session history
- Gemini adapter
- async/background
- stronger deposit ingestion

## 9. Immediate Next Work

The immediate next work is:

```text
current work package object draft + surface read mapping
```

This should be implemented with minimal visual change first.

The key move is not to add a new panel. The key move is to make existing User / VectorFL / Engine readings derive from the same current work package object.
