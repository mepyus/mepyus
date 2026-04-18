# Integrated Engine Panel Proliferation Course Correction Note v0

## 1. Verdict

HOLD_FOR_PROCESS_CORRECTION

The recent screen work improved several visible pieces, but the user's critique is correct:

```text
If every structural correction becomes another visible panel, the integrated engine will not scale.
```

The screen must not grow by piling panels. It must grow by making the engine process itself visible and operable.

## 2. What Went Wrong

The implementation drifted toward this pattern:

```text
structural gap found
-> add a panel or focus card
-> label the panel with the intended role
-> assume readability improved
```

That is not enough.

The user is not asking for more visible cards. The user is asking for the system to behave like an integrated engine:

```text
instruction intake
-> internal search
-> evidence bundle
-> VectorFL mediation / packetization
-> User organization
-> Engine main processing
-> VectorFL reflux
-> record / sedimentation
```

The current screen shows many parts of that process, but it still asks the user to mentally prove that the process actually happened.

## 3. Symptom vs Cause

### Symptom

- Too much information is visible at once.
- Many panels explain roles, but the actual work movement remains hard to feel.
- The user still has to infer which panel is the current process owner.
- New work risks becoming another card instead of a process-bearing object.

### Cause

The current UI is still too panel-centered.

It does not yet treat the work package as the main operating object that moves through process stages.

The screen should first answer:

```text
Where is this work package in the engine process?
What evidence has it actually gathered?
What surface currently owns the next transformation?
What is candidate-only, held, returned, or sedimented?
```

Only after that should panels appear as views into the current process.

## 4. Corrected Interpretation

The big frame is not:

```text
User page + VectorFL page + Engine page + many panels
```

The big frame is:

```text
work package moving through the fixed 3-surface body
```

The three surfaces are not information containers. They are different transformation roles:

| surface | process role | must primarily show |
| --- | --- | --- |
| User | purpose / organization / decision | what should be assigned, decided, held, or opened |
| VectorFL | internal search / evidence / mediation / packetization / reflux | whether the work package is grounded enough to move |
| Engine | processing / return / extraction / validation / deposit material | what was processed and what returned as candidate material |

Panels are secondary. They should only expose the relevant process state for the current surface.

## 5. What The UI Must Stop Doing

The UI must stop treating every missing concept as a new visible block.

Specifically:

- Do not add another explanatory card for every process step.
- Do not expose all space information on every surface.
- Do not make the shared spine a dense dashboard.
- Do not make VectorFL a stack of all evidence, all CLI controls, all line tools, and all results at once.
- Do not let User Surface become a mixed team board plus packet board plus log board.
- Do not let Engine Surface become a mock control room or return feed pile.

## 6. What The UI Must Do Instead

The next screen structure should be process-first:

```text
current work package
-> current process stage
-> evidence state
-> surface owner
-> next transformation candidate
-> trace / sedimentation state
```

Each surface should then show only the local view of that same object.

This means the next correction should not be a new panel. It should be a tighter operating object model for the screen:

- one current work package identity
- process stage within the 8-step physiology
- evidence bundle state
- authority state
- surface-local next action
- trace / sedimentation candidate state

## 7. Re-Reading Current Additions

### Shared Spine

Useful, but risky if it becomes a dashboard.

Correct role:

```text
thin orientation layer
```

Not:

```text
all-state display
```

### Surface Local Focus

Useful as a first reading layer.

Risk:

It can become three more explanatory panels unless it is tied to a formal current work package stage.

### VectorFL Packet Formation Layer

Useful, but currently still closer to:

```text
input summary + mediation frame
```

than:

```text
internal-search-backed packet
```

### Internal Team / Language Loop Panel

Useful for User Surface assignment.

Risk:

It can become a card list unless it is subordinated to:

```text
what work package was assigned, to whom, for which process stage
```

### Engine Return Panel

Useful for return material.

Risk:

It can remain a return feed unless it is tied to:

```text
what process stage produced this return
```

## 8. Correct Next Priority

The next priority is not:

```text
more panels
```

It is:

```text
formal current work package object draft
```

But this must not be implemented as a giant object card.

It should be implemented as a minimal operating object behind the screen that every surface reads from:

- work package id
- purpose
- current process stage
- evidence state
- packet state
- surface owner
- authority state
- next candidate action
- trace / sedimentation state

The screen should then render fewer, clearer local views from that object.

## 9. New Rule Before Further Implementation

Before adding any visible UI element, answer:

```text
Is this a new process state of the current work package,
or just another panel explaining something we already failed to structure?
```

If it is only explanation, do not add it.

Instead, adjust:

- the underlying work package object
- the process stage mapping
- the local surface reading
- or the visibility hierarchy

## 10. What Must Be Verified Next

The next validation should not ask:

```text
Can the user see the new panel?
```

It should ask:

```text
Can the user tell where the current work package is in the process without reading every panel?
Can the user tell what evidence has been gathered or is missing?
Can the user tell which surface currently owns the next transformation?
Can the user tell what is candidate-only and not canonical?
```

## 11. What Must Not Be Done Next

- no new visible panel as the default solution
- no multi-work board yet
- no session history expansion
- no Gemini adapter
- no async/background expansion
- no full language polish pass
- no deposit ingestion automation
- no new surface
- no giant dashboard

## 12. Locked Correction

From this point, the screen work must be judged by:

```text
Does this reduce the user's need to mentally assemble the engine process?
```

not by:

```text
Does this show another piece of information?
```

The immediate correction path is:

```text
process-first current work package object
-> surface-specific local readings
-> fewer visible panels
-> only then multi-work handling
```
