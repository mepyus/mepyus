# run_063_inventory_revalidation

## Role Boundary

- Gemini performs read-only observation and classification.
- Codex provides direction and later analyzes the returned result.
- User controls execution, approval, and any movement between spaces.

## Goal

Create a package-level inventory and classification of Package 012+ sandbox artifacts after run_062_formal_reset.

This run must not approve integration. It only prepares a structured map for later user decisions.

## Starting Trusted Baseline

- Last trusted official completed state: Run 060 / Package 011.
- run_061 is VOID and quarantined.
- run_062 is an official formal reset / baseline recovery record.
- Package 012 and later directories must be revalidated before being treated as official.

## Observation Scope

Inspect package directories under:

```text
app/work/space-skill-sandbox/packages/
```

Focus on:

- `package_012_revised_metadata_scan_application`
- `package_013_*` and later package directories
- any package directories that appear to have no matching run record
- any artifacts that appear to be Codex direct-write outputs
- any package directories whose numbering or naming conflicts with run ledger continuity

Do not inspect the whole repository.
Do not treat package number alone as official proof.

## Classification States

For each observed package/artifact, assign exactly one:

| State | Meaning |
|---|---|
| Candidate-Official | Appears consistent with prior user-authorized Gemini execution, but still requires user approval. |
| Hold | Requires manual user review, missing evidence, unclear run linkage, or insufficient provenance. |
| Void/Quarantine | Appears related to mistaken Codex direct-write, boundary violation, or already voided material. |
| Out-of-Scope | Exists but should not be decided in run_063. |

## Required Package-Level Fields

For each package, report:

- `package_path`
- `package_name`
- `observed_files_summary`
- `matching_run_record_found`: `true` / `false` / `unclear`
- `classification`
- `rationale`
- `recommended_user_decision`
- `recommended_next_action`

## Important Checks

- Identify ledger gaps between run records and package directories.
- Identify duplicate or conflicting package numbers/names.
- Identify packages that have closeout/user_summary but no run record.
- Identify packages that look like later experiments beyond the trusted baseline.
- Identify any artifacts connected to voided run_061.
- Preserve uncertainty. Do not overstate confidence.

## Constraints

- Read-only report task.
- Do not modify, move, delete, or create files.
- Do not append to `RUNLOG.jsonl`.
- Do not promote anything to source-space.
- Do not create automation.
- Do not modify scripts.
- Do not create graph, ontology, router, controller, hook, MCP, watch mode, or baseline.
- Do not mark anything as officially integrated.
- Do not treat run_061 as valid.

## Required Output

### 1. Status

### 2. Inventory Summary

Briefly summarize how many package directories were observed and the main ledger pattern.

### 3. Classification Table

Use this table format:

| Package | Matching Run? | Classification | Rationale | Recommended User Decision |
|---|---:|---|---|---|

### 4. Ledger Gap Findings

List run/package mismatches, missing run records, duplicate package numbers, or ambiguous sequence breaks.

### 5. Boundary Risk Findings

List possible Codex direct-write, unauthorized artifacts, over-automation risk, or misleading metadata risks.

### 6. Recommended Package Batches

Group packages into:

- Batch A: likely safe candidates for user review
- Batch B: hold/manual review
- Batch C: void/quarantine candidates
- Batch D: out-of-scope

### 7. Recommended Next Official Run

Propose the next run name and purpose.
Do not start it.
