# PHASE2_SOURCE_SELECTION_RULE_CANDIDATE_V0

classification: HOLD_CANDIDATE_SOURCE_SELECTION_RULE

{
  "primary_refs": "Use current user original + immediate predecessor PASS/HOLD report + latest next-work card + one domain/pressure artifact if it changes judgment.",
  "secondary_refs": "Use older/broader space artifacts only when current refs conflict, are insufficient, or trigger architecture/layer ambiguity.",
  "required_for_each_ref": [
    "absolute_path",
    "exists",
    "sha256",
    "used_for",
    "changed_judgment"
  ],
  "reject_ref_when": [
    "no changed_judgment",
    "citation is only decorative",
    "reference increases operator load without changing decision",
    "reference is authority/current-position/registry unless explicitly approved for read-only orientation"
  ],
  "max_default_refs": 4,
  "escalate_to_heavy_when": [
    "source refs conflict",
    "space_reference_delta unclear",
    "architecture/principle pressure appears",
    "Codex/Gemini disagreement is needed",
    "authority/promotion pressure appears"
  ],
  "output_requirement": "Every Phase2 packet must include space_reference_delta before being called space-referenced."
}

HOLD: no authority/registry/current-position/promotion.
