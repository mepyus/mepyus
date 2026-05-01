# Phase 1.24 Flow-Aware Reopen Trigger Note v0

## Purpose

This note defines when the current flow-aware rule may be reopened.

Without these triggers, broad reopening is not justified.

## Global Reopen Rule

Do not reopen because:

- flow exists in one sample
- a family looks structurally similar to an allow-list family
- unresolved hold remains somewhere
- an operator prefers more tuning headroom

Reopen only from evidence-based triggers.

## Reopen Trigger: `general_line_vs_flow`

Reopen only if one of the following occurs.

1. repeated samples show that bounded local conditions consistently justify a middle bucket better than current default
2. default begins to miss a better local slice in a repeatable way
3. carry-forward behavior shifts from stable low-value toward actual reroute usefulness across repeated cases

Without one of these, keep current placement:

- default-sufficient with unresolved pressure

## Reopen Trigger: `raw_intake_gap`

Reopen only if one of the following occurs.

1. repeated reread outcomes show current default is no longer honest enough
2. flow-aware repeatedly adds noise or overreach such that the family should be pushed toward block-list
3. carry-forward evidence or local slice evidence changes enough to make current weak default-sufficient placement unstable

Without one of these, keep current placement:

- keep default-sufficient

## Reopen Trigger: `conditional-only` Bucket

Reopen only if one of the following occurs.

1. a family repeatedly lands between default-sufficient and allow-list without honest placement in either
2. a bounded local cue pattern appears that is too strong for unresolved pressure but too weak for full allow-list
3. repeated contradiction shows the current buckets cannot place a middle case cleanly

Without one of these, keep current bucket state:

- structurally open
- operationally empty

## Reopen Trigger: `input_layer_wrapper`

Reopen only if one of the following occurs.

1. default begins missing a better local slice repeatedly
2. carry-forward shifts from stable low-value to actual reroute handle in a repeatable way
3. bounded flow-aware mode produces material narrowing beyond current default in repeated cases

Without one of these, keep current placement:

- protect as default-sufficient

## Trigger Evidence Types

Acceptable trigger evidence includes:

- new family sample accumulation
- repeated contradiction against current placement
- repeated failure of the current default or protected-default rule
- carry-forward classification drift
- repeatable bounded reroute gain

Unacceptable trigger evidence includes:

- single anecdotal sample
- naming intuition
- generic flow wording
- broad desire to continue tuning

## Trigger Without Broad Reopen

Even when a trigger appears:

- reopen only the affected family or bucket
- do not reopen allow-list / block-list globally
- do not reopen emitter work by default
- do not treat one trigger as permission to restart broad tuning
