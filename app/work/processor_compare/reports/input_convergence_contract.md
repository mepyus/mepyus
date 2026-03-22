# Input Convergence Contract

- role: operational baseline, not final ontology
- handoff target: bridge / local space

## contract
```json
{
  "generated_at": "2026-03-21T05:49:11.543968Z",
  "contract_name": "input convergence contract",
  "contract_role": "operational baseline, not final ontology",
  "required_fields": {
    "source_identity": [
      "source_type",
      "source_ref",
      "source_origin_id",
      "dust_input_id"
    ],
    "anchor_bundle": [
      "anchors",
      "representative_anchors",
      "supporting_anchors",
      "dropped_weak_anchors"
    ],
    "processing_values": [
      "D",
      "I",
      "S",
      "scene",
      "flow"
    ],
    "observer_or_ambiguity_trace": [
      "available",
      "merged",
      "items"
    ],
    "transformable_handles": [
      "short_label",
      "sibling_ids",
      "source_ref"
    ]
  },
  "downstream_handoff_expectations": {
    "bridge": [
      "must consume canonical anchors directly",
      "should preserve scene/flow overlap as processing overlap",
      "should preserve rejected overlap when available"
    ],
    "local_space": [
      "must preserve representative/supporting anchors",
      "should preserve dropped weak aggregate",
      "should expose transition/state deltas rather than only labels"
    ]
  },
  "current_runtime_mapping": {
    "material_metadata": [
      "anchors",
      "anchor_bundle",
      "processing_values",
      "observer_or_ambiguity_trace",
      "transformable_handles"
    ],
    "local_space": [
      "representative_anchors",
      "supporting_anchors",
      "dropped_weak_anchors",
      "state"
    ],
    "bridge_trace": [
      "shared_anchors",
      "note",
      "bridge_reason_kind",
      "processing_overlap"
    ]
  }
}
```
