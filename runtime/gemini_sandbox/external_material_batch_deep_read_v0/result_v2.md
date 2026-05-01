# Gemini Deep Validation: Retry Batch (Material 2 & 3)

## 1. Material 2 (oh_my_opencode_openai_community.txt)
case_id: material_2_retry
source_surface: external_material_file
lens_order: technical -> maker-intent -> user-intent -> line/axis -> risk -> residue
verdict: PASS_WITH_NOTE

### Evidence Table
| claim | evidence_ref | evidence_summary | supports | does_not_support | confidence |
| --- | --- | --- | --- | --- | --- |
| Community scalability is value | section 1 | Open source ecosystem growth | yes | Closed system value | medium |
| High auditability | section 2 | Community-driven review | yes | Black-box model reliability | medium |

### Deep Audit
- Expected vs Observed: Expected structured community feedback, Observed qualitative notes.
- HOLD Candidates: 1. Code quality vs. external PRs, 2. Security hardening, 3. Long-term maintenance burden.
- What Was Not Verified: Actual execution of external PRs, internal compatibility of community features.
- Over-promotion Check: Material is reference only; not a baseline replacement.

## 2. Material 3 (codex_pipeline.md)
case_id: material_3_retry
source_surface: external_material_file
lens_order: technical -> maker-intent -> user-intent -> line/axis -> risk -> residue
verdict: PASS

### Evidence Table
| claim | evidence_ref | evidence_summary | supports | does_not_support | confidence |
| --- | --- | --- | --- | --- | --- |
| Deterministic processing | section 1 | Fixed pipeline stages | yes | Random execution | high |
| Validation gates present | section 2 | Intermediate gate checks | yes | Bypass paths | high |

### Deep Audit
- Expected vs Observed: Observed pipeline matches intended deterministic flow.
- HOLD Candidates: 1. Exceptional state bypass, 2. Complex input processing limitations, 3. Pipeline version alignment.
- What Was Not Verified: Performance metrics under high load, pipeline version compatibility.
- Over-promotion Check: Pipeline logic is descriptive, not architecture-defining.

## Batch-level self-check
- Independent processing: Yes
- Full contract compliance: Yes
- No over-promotion: Yes
