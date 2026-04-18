# Line Thickening Promotion Scope Note v0

## Purpose

This note records the scope-hardening step for `line_thickening`.

The key distinction is:

- `thickness_level` tells us how strong the line looks.
- `promotion_scope` tells us how broadly that strength has been validated.

## Why this is needed

A line can be locally strong without being globally established. If the runtime only emits `status=operating` and `thickness=thick`, the result is easy to overread as global truth. That is too strong for a bounded grounded path.

## Scope levels

- `path_local`: one path or summary-local evidence only
- `source_family_local`: one source family with repeated local grounding
- `surface_family_local`: multiple related surfaces, still local to a family
- `cross_family_candidate`: validated across multiple source families inside one bounded validation route, but still not global
- `global_candidate`: reserved for broader validation
- `global_operating`: reserved and not auto-assigned here

## Scope basis

Scope must be justified with a small basis summary:

- validation path / source family / surface family
- source pointers
- distinct runs or assets when relevant

In this repo, `path` means the validation route that produced the observation packet. Summary-echo preflight rows do not count as path diversity for promotion.

## Promotion discipline

- single grounded path recurrence does not grant global validity
- summary-local preflight lines stay path_local
- strong grounded lines can still remain local in scope
- operating does not imply global operating

## Verification expectation

The registry and promotion log should both say:

- what the line strength is
- where that strength was validated
- why that scope is as broad as it is
