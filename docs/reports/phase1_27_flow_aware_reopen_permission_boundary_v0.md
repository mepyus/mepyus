# Phase 1.27 Flow-Aware Reopen Permission Boundary v0

## Purpose

This note fixes the boundary of what a reopen request may and may not do.

## Base Rule

Without trigger evidence:

- reopen is not permitted

Without an evidence log:

- reopen is not permitted

## Allowed Reopen Scope

Reopen is allowed only at the family or bucket level.

Allowed:

- family-level placement recheck
- family-local reread recheck
- conditional bucket check

Not allowed:

- global heuristic rewrite
- broad family sweep
- allow-list / block-list rebuild
- lower emitter reopen
- classifier reopen
- schema reopen

## Allowed Reopen Depth

### placement recheck only

Use when:

- the current family placement may no longer be honest enough

### family-local reread only

Use when:

- a bounded local slice may have been repeatedly missed

### conditional bucket check only

Use when:

- a middle case may now exist that current buckets cannot place honestly

## Disallowed Escalation

Do not escalate directly from family-level evidence into:

- emitter tuning
- classifier tuning
- schema change
- global flow-aware default

Those layers remain closed unless a separate later package justifies them.

## Unresolved Guard

Do not read unresolved hold as tuning permission.

Unresolved means:

- keep current placement
- wait for trigger evidence
- reopen narrowly if and only if trigger evidence is logged

It does not mean:

- tuning should continue
- the current freeze is weak
- broad experimentation is permitted

## Permission Sequence

The required order is:

1. detect trigger
2. check current trigger checklist
3. write bounded evidence log
4. reopen only the affected family or bucket

If one of these steps is missing:

- do not reopen
