# Excerpt Quality Examples v0

## Poor: Title Only

```text
# Source Authority Ladder v0
```

Why poor: the excerpt identifies the file but not the authority rule.

## Usable: Local Context

```text
Conflict handling:

- Higher authority wins only when the same meaning is directly in conflict.
- Lower authority can expose a gap or newer operational condition.
```

Why usable: it gives relevant local context and supports authority comparison.

## Strong: Operative Rule

```text
- If two high-authority sources conflict, mark `HOLD` and request user decision.
```

Why strong: it directly supports hold behavior for authority conflict.

## Usable But Not Strong: Status Metadata

```text
- phase: `phase1_6_evidence_grounding_hardening`
- authority: `working_spec`
```

Why not strong: useful for status but not enough to support merge/diff/hold behavior.

## Validation

The examples show that quality depends on support value, not raw excerpt length.
