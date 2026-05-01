# Phase 1.21 Flow-Aware Unresolved Boundary Note v0

## Purpose

This note records the boundary items that should remain unresolved even after the current freeze candidate pass.

## raw_intake_gap Boundary

Current reading:

- default-sufficient for now
- not strong enough to enter block-list confidently

Why unresolved:

- flow-aware does not improve the read
- but the family still does not look definitively misleading in the way preprocess or compact cases do

Next narrowing question:

- is `raw_intake_gap` simply weak-flow, or does flow-aware actually increase reader-side bias risk?

## general_line_vs_flow Boundary

Current reading:

- default-sufficient for now
- thin flow survives

Why unresolved:

- this is the clearest case where a future `conditional-only` bucket might become useful
- current evidence is still too light to promote that bucket

Next narrowing question:

- does thin independent flow stay stable enough across more local slices to justify a middle bucket?

## input_layer_wrapper Retention Rule

Current reading:

- relatively strong default-sufficient candidate

Why it should stay default:

- default already lands on a flow-bearing local slice
- tuning does not improve enough to justify a switch

Next narrowing question:

- can future reader tuning accidentally disturb a family that is already default-sufficient?

## Why the Conditional-Only Bucket Is Empty Right Now

Current interpretation:

- not because the bucket is permanently unnecessary
- but because the current sample set does not force a clean middle case strongly enough

In other words:

- some families clearly deserve allow-list treatment
- some clearly deserve block/default treatment
- the middle remains sample-light, not conceptually impossible

## If Another Round Is Needed, Narrow It With These Questions

1. Does `general_line_vs_flow` stay merely default-sufficient, or does it repeatedly behave like a thin conditional-only family?
2. Does `raw_intake_gap` stay weak-flow, or should it move to block-list because flow-aware mainly adds noise?
3. Can `input_layer_wrapper` remain stable under future reader tuning without needing a protective exception rule?

