# CLI-side Space Interaction Contract v0.1 Final Addendum: Preflight Guard
# Topic: Ensuring Integrity for High-Impact CLI Operations

## 0. Declaration
- **Mode:** Addendum note only / Synthesis.
- **Scope:** Read-only reference; no modification of source-space documents.
- **Status:** Strategic reference material only; no implementation.
- **Authority:** All findings remain provisional strategic reference material.
- **Date:** 2026-04-26

## 1. Why This Addendum Exists
The initial "Interaction Contract v0.1" (Final Integration) successfully established the general flow, but dry-runs revealed a critical oversight: high-impact operations (e.g., baseline changes, file deletions) were reaching `HUMAN_REVIEW_REQUIRED` *after* the mutation had already occurred. This addendum mandates a **Preflight Guard** protocol to ensure sovereignty-impacting decisions are intercepted *before* the filesystem is touched.

## 2. Correction 1: High-impact Actions Need Preflight
**Rule:** High-impact actions require preflight classification *before* any mutation.
- **Flow:** `High-impact Request` -> `Preflight Footer` -> `HUMAN_REVIEW_REQUIRED / HOLD` -> `[NO FILE MODIFIED]` -> `Human Lock` -> `Implementation Packet`.

## 3. Correction 2: Label/Text Change vs. File Rename
- **Label/Text Change:** Semantic shift in labels. `Status: VALIDATION_REQUIRED`. Requires verification that logic is untouched.
- **File Rename:** Referential shift. Requires a mandatory `reference/import verification` evidence object (Failure Trace) to ensure the system doesn't break due to broken paths.

## 4. Correction 3: "No File Modified" Requirement
When in `HOLD` or `PREFLIGHT` mode, the footer MUST explicitly state: 
`note: Baseline-impacting change. Do not modify before user lock.`
`summary: ... [Action Proposed]. No file modified.`

## 5. Corrected Flow Examples

### Baseline Proposal (Preflight)
```text
--- STRUCTURED FOOTER v0.1 ---
status: HUMAN_REVIEW_REQUIRED
task_intent: Propose baseline timeout change
packet_type: validation
scope: baseline_proposal
summary: Proposed changing default timeout from 300s to 600s. No file modified.
source_ref: user_instruction_04
risk_signal: high
validation_required: yes
human_review_required: yes
evidence_ref: docs/reports/proposal_v0.md
next_packet_candidate: hold
note: Baseline-impacting change. Do not modify before user lock.
--- END FOOTER ---
```

### File Rename (Validation Required)
```text
--- STRUCTURED FOOTER v0.1 ---
status: VALIDATION_REQUIRED
task_intent: Rename utility component
packet_type: implementation
scope: code_change
summary: Renamed utils/helper.js to utils/helper_v2.js.
source_ref: user_instruction_06
risk_signal: medium
validation_required: yes
human_review_required: no
evidence_ref: [import_search_results]
next_packet_candidate: validation
note: Reference/import path verification required.
--- END FOOTER ---
```

## 6. Contract Rules to Preserve
- **OK != Lock:** Executing successfully is not equivalent to finalizing a rule.
- **Provenance-First:** A summary without an `evidence_ref` is a claim, not an asset.
- **Research/Implementation Separation:** Research results (`Research Packet`) cannot auto-transition to `Implementation`.
- **Worker/Observer Decoupling:** The UI surface observes/triages; it does not control or execute.

## 7. Remaining Ambiguities
- **Worker Preflight Detection:** How the CLI worker internally detects "Preflight" vs "Auto-execute" without a central controller.
- **Evidence Formatting:** How to present `evidence_ref` (the diff/import check) inside a CLI session concisely.
- **Sovereignty Thresholds:** Precise definition of when a "small" logic change becomes a "baseline" proposal requiring human lock.

## 8. What This Addendum Is Not
- Not an implementation plan.
- Not a UI design spec.
- Not a router/controller design.
- Not an approval mechanism.

## 9. Closeout
This addendum note is strategic guidance only.
No source-space document was modified.
No implementation, UI, parser, schema, router, controller, automation, verification UI, bridge logic, drill-down design, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, JSON schema, CLI trace contract, aggregation threshold, or agent architecture was created.
All findings remain provisional strategic reference material.
