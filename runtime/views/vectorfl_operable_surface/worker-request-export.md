# worker request export
- request_id: `wrk_codex_line_refine_v1`
- adapter: `codex-cli`
- target: `Codex rewrite worker`
- selected_line: `# raw intake gap analysis before middle-layer fix`
- selected_bundle: `bundle_01_raw_intake_middle_layer_gap`
- compare_target: `## 1. compared paths - structured document path - front door: [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorf...`

## intent
rewrite selected line with bundle-grounded language while preserving recall order

## payload
{
  "source_line": "# raw intake gap analysis before middle-layer fix",
  "human_translation": "# raw intake gap analysis before middle-layer fix",
  "bundle_ids": [
    "bundle_01_raw_intake_middle_layer_gap",
    "bundle_05_visible_split_to_recall_surface",
    "bundle_03_meaning_vs_format_disentangle"
  ],
  "rewrite_goal": "Keep evidence-grounded wording and expose what still needs reread.",
  "return_format": [
    "raw",
    "internal_reading",
    "refined",
    "user_language"
  ]
}

## approval gate
Re-evaluate after next runtime refresh and preflight guard recheck.