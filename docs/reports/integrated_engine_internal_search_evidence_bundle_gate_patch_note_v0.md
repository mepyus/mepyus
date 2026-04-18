# Integrated Engine Internal Search Evidence Bundle Gate Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

An internal search / evidence bundle gate was added before VectorFL current work packet formation.

This does not implement a full search engine. It makes the current work package visibly pass through a bounded evidence gate before the packet is read as formed.

## 2. Why This Is The Next Correction Before Multi-Work Board

The body/process audit found that the UI had improved frame, mediation, and candidate visibility, but still lacked the second and third process steps:

```text
internal search
-> evidence bundle
```

Building a multi-work board before this gate would multiply shallow session/candidate cards. A work item first needs to show whether it has memory/evidence attached.

## 3. Internal Search Gate Shape

Changed file:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`

The gate appears before `current work packet formation` and shows:

- search state
- request basis
- evidence bundle summary
- evidence limitation
- expandable attached evidence bundle items

Current states:

- `completed`
- `skipped`
- `thin evidence`
- `missing evidence`

The state is derived from current bounded refs and prompt intent. It is intentionally thin and visible, not a hidden automation claim.

## 4. Evidence Bundle Shape

Each attached ref is read as a bundle item with:

- ref path
- evidence kind
- source state
- why attached

Current evidence kinds include:

- governing lock
- current state
- language / mapping
- prior CLI turn
- runtime artifact
- screen/code evidence
- source ref

This turns a raw file list into a bounded evidence bundle, while still showing that most refs are user-provided.

## 5. How Packet Formation Now Depends On Evidence Bundle

The visible order is now:

```text
packet input details
-> internal search / evidence bundle gate
-> current work packet formation
-> packet confirmation / Send Codex Turn
```

The Codex prompt also now includes:

- internal search gate state
- evidence bundle summary
- evidence limitation

So the outgoing turn is evidence-aware, even though the evidence was not produced by a full search engine.

## 6. What Still Remains Manual

- The user still provides most context refs.
- The gate does not scan the repository.
- The gate does not select the best documents automatically.
- Evidence classification is heuristic and filename/content-context based.
- `completed` means bounded refs are attached and the prompt requests reading; it does not mean exhaustive search complete.
- Engine internal search process is not yet implemented.

## 7. Watchpoints

1. Do not treat this as full internal search.
2. Do not hide user-provided refs behind "internal" language.
3. Do not treat a thin evidence bundle as sufficient proof.
4. Do not build multi-work board until one work package can carry this gate clearly.
5. Do not expand this into a giant asset browser.
6. Do not make evidence bundle canonical memory or deposit.

## 8. Next Smallest Validation Step

Open the VectorFL surface and confirm the first operating chain reads:

```text
input details
-> internal search / evidence bundle gate
-> current work packet formation
-> send
```

Pass condition:

- the gate is visible before packet formation
- search state is clear
- evidence bundle feels like a bundle, not only a file list
- missing/thin evidence is not hidden
- the panel does not become a giant search console

If this passes, the next audit should decide whether Engine Surface needs a matching internal-search process strip or whether surface language should be corrected first.
