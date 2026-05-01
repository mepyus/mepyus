# Reingress Learning Examples v0

## Example: Useful Grounding

```json
{
  "evidence_depth_summary": {
    "pointer_only": 0,
    "direct_grounded": 2,
    "cross_supported": 2,
    "total": 4
  },
  "useful_excerpt_modes": ["heading_plus_block"],
  "reuse_candidate_assets": [
    "docs/specs/source_authority_ladder_v0.md"
  ],
  "future_validation_hint": "Reuse heading_plus_block extraction for authority questions."
}
```

## Example: Thin Grounding

```json
{
  "weak_grounding_areas": [
    "runtime/views/generated_large_surface.md"
  ],
  "unresolved_grounding_note": "Pointer-only fallback remained for generated view.",
  "next_probe_hint": "Use source docs instead of generated latest views first."
}
```

## Interpretation

Learning fields should make the next run cheaper and more honest. They identify reusable assets, working excerpt modes, and weak areas without pretending the current run solved them.
