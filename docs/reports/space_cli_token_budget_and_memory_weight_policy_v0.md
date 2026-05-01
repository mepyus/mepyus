# Space-CLI Token Budget and Memory Weight Policy v0

## 1. core principle

The space is not a device for reading more.

The space is a device for retrieving less, precisely.

The default posture is:

```text
small relevant memory first
pointer second
source slice third
full source only when necessary
```

## 2. reading levels

## Level 1. input routing

Purpose:

- judge source surface
- read user purpose and tension
- decide whether this is conversation material, worker return, generated report, external material, runtime event, or program artifact

Default rule:

- do not read the whole source
- do not load all space assets
- do not attach full prior conversation

## Level 2. memory card retrieval

Purpose:

- retrieve only relevant line, axis, guardrail, risk memory, or reuse hint
- prefer compact memory over full document text

Default rule:

- no full original source reading
- no full onboarding packet
- no repeated philosophy block unless the task is about philosophy

## Level 3. pointer-based source check

Purpose:

- verify a specific claim, boundary, or reference point
- inspect a specific document section or artifact slice

Default rule:

- read only the needed source slice
- preserve pointer to the larger source
- avoid turning source check into full reingestion

## Level 4. full source reading

Purpose:

- use only when source slice is insufficient
- use when contradiction, ambiguity, or deep probe requires it

Default rule:

- full source reading is exceptional
- full source reading is not the default packet shape

## 3. CLI task packet token limit principle

A CLI task packet should include only:

- purpose
- source surface
- 1 to 3 relevant lines
- 1 to 2 relevant axes
- 3 to 7 guardrails
- reference pointers
- expected output
- stop conditions

Do not include:

- full space onboarding
- all related documents
- long philosophy replay
- full previous conversation
- all runtime records
- every possible risk

The CLI should receive enough context to act, not enough context to become the space.

## 4. reflux memory weight grades

## none

Use when record value is low.

## note_only

Use for a light trace that may be useful later but should not affect the next packet by default.

## reuse_hint

Use when the memory should be checked in a similar future task.

## risk_memory

Use when the memory should warn against a repeated risk.

## pattern_candidate

Use when repeated evidence may mature into a pattern, but the pattern is not locked.

## hold_signal

Use when automatic continuation should pause before implementation, promotion, or structural change.

## next_move_candidate

Use for a possible next action.

This is not an automatic execution trigger.

## deeper_probe_needed

Use when a 4-line card or lightweight packet is insufficient and a separate thought experiment or verification is needed.

## 5. rules against memory weight inflation

- Do not store every return in full.
- Do not promote every result into a pattern.
- Do not treat PASS as a standard.
- Do not auto-execute `next_move_candidate`.
- Keep originals as pointers when possible.
- Compress judgment traces.
- Increase weight only through repeated, specific re-emergence.
- Separate `risk_memory` from `pattern_candidate`.
- Separate `next_move_candidate` from permission to act.

## 6. packet compression rule

If a packet feels heavy, remove in this order:

1. full background explanation
2. repeated philosophy
3. broad asset lists
4. previous conversation excerpts
5. non-current examples
6. redundant guardrails

Keep:

- source surface
- current purpose
- needed line / axis / guardrail
- expected output
- stop condition

This is how the space reduces CLI token use without becoming shallow.
