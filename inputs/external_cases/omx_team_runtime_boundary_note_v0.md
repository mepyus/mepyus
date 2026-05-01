[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# OMX team runtime boundary note v0

## source metadata

- source_title: `Oh-my-Codex / Opencode community runtime discussion`
- source_author: `community talk speaker`
- source_type: `external talk transcript`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo from local raw capture`
- raw_source_file: `inputs/external_cases/oh_my_opencode_openai_community.txt`

## why this source matters

This source matters because it distinguishes simple subagent parallelism from a more actively coordinated team runtime where the orchestrator keeps intervening during execution.

It overlaps with current pressures in our space around:

- bounded team coordination
- continuous orchestration instead of fire-and-forget delegation
- runtime lightness as a condition for multi-lane operation
- hook and recovery surfaces

## core claim

The source argues that a team runtime is not just parallel workers.

Its value comes from:

- ongoing orchestration
- mid-run checks and re-alignment
- reduced merge cost by intervening early
- lightweight runtime conditions that make persistent coordination feasible

The source also contrasts systems with fewer hooks or fewer orchestration surfaces against systems that can support richer intervention and recovery.

## structural pattern

### 1. bounded orchestrator intervention

The orchestrator should not disappear until the very end. It should keep checking and adjusting workers during execution.

### 2. lightweight runtime matters

Heavy runtime overhead makes continuous orchestration harder.

### 3. hooks and recovery surfaces matter

Automation is limited if the runtime does not expose enough control points.

### 4. team runtime is different from unrestricted multi-agent freedom

The argument is not "let every agent act freely." It is "use bounded coordination surfaces that keep work aligned."

## relevance to our current space

This source is useful because it reinforces:

- bounded surface over universal agent freedom
- structure before uncontrolled delegation
- orchestrated intervention as a runtime discipline

It should still be treated as a pattern reference, not as a direct runtime import order.

## bounded judgment

Current bounded judgment:

- useful as a bounded coordination reference
- relevant to weak recurrence around surface-bounded orchestration
- not a direct import instruction
- keep as thin external reread material with no promotion

